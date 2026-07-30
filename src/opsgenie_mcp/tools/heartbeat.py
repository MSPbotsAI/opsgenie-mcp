import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import OpsgenieClient, OpsgenieError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], OpsgenieClient | None]) -> None:

    @mcp.tool()
    async def opsgenie_heartbeat_add_heartbeat_request(body: dict) -> str:
        """Add Heartbeat Request.

        API: POST /v2/heartbeats

        Args:
            body: Required. JSON request payload. Fields: `name`, `description`, `interval`, `intervalUnit`, `enabled`, `ownerTeam`, `alertMessage`, `alertTags`, `alertPriority`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.post("/v2/heartbeats", params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_heartbeat_delete_heartbeat_request(heartbeat_name: str) -> str:
        """Delete Heartbeat Request.

        API: DELETE /v2/heartbeats/:heartbeatName

        Args:
            heartbeat_name: Required. Name of the heartbeat to delete
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/heartbeats/{heartbeat_name}"
        params = {}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_heartbeat_disable_heartbeat_request(heartbeat_name: str) -> str:
        """Disable Heartbeat Request.

        API: POST /v2/heartbeats/:heartbeatName/disable

        Args:
            heartbeat_name: Required. Name of the heartbeat to disable
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/heartbeats/{heartbeat_name}/disable"
        params = {}
        try:
            result = await client.post(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_heartbeat_enable_heartbeat_request(heartbeat_name: str) -> str:
        """Enable Heartbeat Request.

        API: POST /v2/heartbeats/:heartbeatName/enable

        Args:
            heartbeat_name: Required. Name of the heartbeat to enable
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/heartbeats/{heartbeat_name}/enable"
        params = {}
        try:
            result = await client.post(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_heartbeat_get_heartbeat_request(heartbeat_name: str) -> str:
        """Get Heartbeat Request.

        API: GET /v2/heartbeats/:heartbeatName

        Args:
            heartbeat_name: Required. Name of the heartbeat to retrieve
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/heartbeats/{heartbeat_name}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_heartbeat_list_heartbeats() -> str:
        """List Heartbeats.

        API: GET /v2/heartbeats

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.get("/v2/heartbeats", params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_heartbeat_ping_heartbeat_request(heartbeat_name: str) -> str:
        """Ping Heartbeat Request.

        API: GET /v2/heartbeats/:heartbeatName/ping

        Args:
            heartbeat_name: Required. Name of the heartbeat to ping
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/heartbeats/{heartbeat_name}/ping"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_heartbeat_update_heartbeat_request(heartbeat_name: str, body: dict) -> str:
        """Update Heartbeat Request.

        API: PATCH /v2/heartbeats/:heartbeatName

        Args:
            heartbeat_name: Required. Name of the heartbeat to update
            body: Required. JSON request payload. Fields: `description`, `interval`, `intervalUnit`, `enabled`, `ownerTeam`, `alertMessage`, `alertTags`, `alertPriority`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/heartbeats/{heartbeat_name}"
        params = {}
        try:
            result = await client.patch(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"
