import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import OpsgenieClient, OpsgenieError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], OpsgenieClient | None]) -> None:

    @mcp.tool()
    async def opsgenie_integration_authenticate_integration(body: dict) -> str:
        """Authenticate Integration.

        API: POST /v2/integrations/authenticate

        Args:
            body: Required. JSON request payload. Fields: `type`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.post("/v2/integrations/authenticate", params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_integration_create_a_new_integration_action(integration_id: str, body: dict) -> str:
        """Create a New Integration Action.

        API: POST /v2/integrations/:integrationId/actions

        Args:
            integration_id: Required. The integration identifier.
            body: Required. JSON request payload. Fields: `type`, `name`, `alias`, `order`, `user`, `note`, `filter`, `source`, `message`, `description`, `entity`, `tags`, `extraProperties`, `ignoreRespondersFromPayload`, `ignoreTeamsFromPayload`, `responders`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/integrations/{integration_id}/actions"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_integration_create_api_based_integration(body: dict) -> str:
        """Create API Based Integration.

        API: POST /v2/integrations

        Args:
            body: Required. JSON request payload. Fields: `type`, `name`, `enabled`, `allowConfigurationAccess`, `allowWriteAccess`, `allowReadAccess`, `allowDeleteAccess`, `ignoreRespondersFromPayload`, `ignoreTeamsFromPayload`, `responders`, `suppressNotifications`, `ownerTeam`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.post("/v2/integrations", params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_integration_delete_integration(integration_id: str) -> str:
        """Delete Integration.

        API: DELETE /v2/integrations/:integrationId

        Args:
            integration_id: Required. The integration identifier.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/integrations/{integration_id}"
        params = {}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_integration_disable_integration(integration_id: str) -> str:
        """Disable Integration.

        API: POST /v2/integrations/:integrationId/disable

        Args:
            integration_id: Required. The integration identifier.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/integrations/{integration_id}/disable"
        params = {}
        try:
            result = await client.post(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_integration_enable_integration(integration_id: str) -> str:
        """Enable Integration.

        API: POST /v2/integrations/:integrationId/enable

        Args:
            integration_id: Required. The integration identifier.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/integrations/{integration_id}/enable"
        params = {}
        try:
            result = await client.post(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_integration_get_integration(integration_id: str) -> str:
        """Get Integration.

        API: GET /v2/integrations/:integrationId

        Args:
            integration_id: Required. The integration identifier.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/integrations/{integration_id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_integration_get_integration_actions(integration_id: str) -> str:
        """Get Integration Actions.

        API: GET /v2/integrations/:integrationId/actions

        Args:
            integration_id: Required. The integration identifier.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/integrations/{integration_id}/actions"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_integration_list_integrations(type: str | None = None, team_id: str | None = None, team_name: str | None = None) -> str:
        """List Integrations.

        API: GET /v2/integrations

        Args:
            type: Optional. Type of the integration. If given, results filtered by type.
            team_id: Optional. The ID of the team. If given, results filtered by teamId.
            team_name: Optional. The name of the team. If given, results filtered by teamName.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"type": type, "teamId": team_id, "teamName": team_name}
        try:
            result = await client.get("/v2/integrations", params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_integration_update_all_integration_actions(integration_id: str, body: dict) -> str:
        """Update All Integration Actions.

        API: PUT /v2/integrations/:integrationId/actions

        Args:
            integration_id: Required. The integration identifier.
            body: Required. JSON request payload. Fields: `ignore`, `create`, `close`, `acknowledge`, `addNote`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/integrations/{integration_id}/actions"
        params = {}
        try:
            result = await client.put(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_integration_update_integration(integration_id: str, body: dict) -> str:
        """Update Integration.

        API: PUT /v2/integrations/:integrationId

        Args:
            integration_id: Required. The integration identifier.
            body: Required. JSON request payload. Fields: `type`, `name`, `emailUsername`, `enabled`, `ignoreRespondersFromPayload`, `ignoreTeamsFromPayload`, `responders`, `suppressNotifications`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/integrations/{integration_id}"
        params = {}
        try:
            result = await client.put(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"
