import contextvars
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.types import ASGIApp, Receive, Scope, Send

from .api_client import OpsgenieClient
from .config import Settings

# Per-request credential isolation via contextvars.
# GatewayTokenMiddleware sets this before the MCP handler runs.
# Python asyncio copies context per task, so concurrent SSE connections are isolated.
_gateway_creds_var: contextvars.ContextVar[tuple[str, str] | None] = contextvars.ContextVar(
    "opsgenie_gateway_creds", default=None
)


def get_client_from_context() -> OpsgenieClient | None:
    """Resolve the active OpsgenieClient for the current request context."""
    creds = _gateway_creds_var.get()
    if not creds:
        return None
    api_key, base_url = creds
    return OpsgenieClient(api_key, base_url)


class GatewayTokenMiddleware:
    """ASGI middleware.

    Reads X-Opsgenie-Api-Key (required) and X-Opsgenie-Base-Url (optional —
    for EU-instance customers who need https://api.eu.opsgenie.com; defaults
    to settings.opsgenie_base_url otherwise) from request headers and stores
    them in the contextvar. Returns 401 if the API key is missing on /mcp
    requests.
    """

    def __init__(self, app: ASGIApp, settings: Settings):
        self.app = app
        self.settings = settings

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        path = scope.get("path", "")
        if not path.startswith("/mcp"):
            await self.app(scope, receive, send)
            return

        request = Request(scope)
        api_key = request.headers.get("x-opsgenie-api-key")
        if not api_key:
            response = JSONResponse(
                {
                    "error": "Missing credentials",
                    "message": "This server requires the X-Opsgenie-Api-Key header",
                    "required_headers": ["X-Opsgenie-Api-Key"],
                    "optional_headers": ["X-Opsgenie-Base-Url"],
                },
                status_code=401,
            )
            await response(scope, receive, send)
            return

        base_url = request.headers.get("x-opsgenie-base-url") or self.settings.opsgenie_base_url

        ctx_token = _gateway_creds_var.set((api_key, base_url))
        try:
            await self.app(scope, receive, send)
        finally:
            _gateway_creds_var.reset(ctx_token)


def create_mcp_server(settings: Settings) -> FastMCP:
    """Build the FastMCP server instance and register all Opsgenie tools."""
    # DNS-rebinding protection is a browser-oriented safeguard that rejects
    # non-localhost Host headers with 421. Disable it so the server works
    # correctly behind a reverse proxy or docker network.
    mcp = FastMCP(
        name="opsgenie-mcp",
        transport_security=TransportSecuritySettings(enable_dns_rebinding_protection=False),
    )

    client_factory: Callable[[], OpsgenieClient | None] = get_client_from_context

    from .tools import (
        account,
        alert,
        alert_notification_policy,
        contact,
        custom_user_role,
        escalation,
        forwarding_rule,
        heartbeat,
        incident,
        incident_template,
        incident_timeline,
        integration,
        maintenance,
        notification_rule,
        notification_rule_step,
        policy,
        schedule,
        schedule_override,
        schedule_rotation,
        service,
        service_incident_rule,
        service_incident_template,
        team,
        team_member,
        team_role,
        team_routing_rule,
        user,
        who_is_on_call,
    )

    for mod in (
        account,
        alert,
        alert_notification_policy,
        contact,
        custom_user_role,
        escalation,
        forwarding_rule,
        heartbeat,
        incident,
        incident_template,
        incident_timeline,
        integration,
        maintenance,
        notification_rule,
        notification_rule_step,
        policy,
        schedule,
        schedule_override,
        schedule_rotation,
        service,
        service_incident_rule,
        service_incident_template,
        team,
        team_member,
        team_role,
        team_routing_rule,
        user,
        who_is_on_call,
    ):
        mod.register(mcp, client_factory)

    return mcp
