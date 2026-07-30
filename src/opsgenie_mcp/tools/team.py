import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import OpsgenieClient, OpsgenieError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], OpsgenieClient | None]) -> None:

    @mcp.tool()
    async def opsgenie_team_create_team(body: dict) -> str:
        """Create Team.

        API: POST /v2/teams

        Args:
            body: Required. JSON request payload. Fields: `name`, `description`, `members`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.post("/v2/teams", params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_team_delete_team(identifier: str, identifier_type: str | None = None) -> str:
        """Delete Team.

        API: DELETE /v2/teams/:identifier

        Args:
            identifier: Required. Identifier of the team
            identifier_type: Optional. Type of the identifier that is provided in identifier. Possible values are 'id' or 'name'. Default: id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/teams/{identifier}"
        params = {"identifierType": identifier_type}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_team_get_team(identifier: str, identifier_type: str | None = None) -> str:
        """Get Team.

        API: GET /v2/teams/:identifier

        Args:
            identifier: Required. Identifier of the team
            identifier_type: Optional. Type of the identifier that is provided in identifier. Possible values are 'id' or 'name'. Default: id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/teams/{identifier}"
        params = {"identifierType": identifier_type}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_team_list_team_logs(identifier: str, identifier_type: str | None = None, limit: str | None = None, order: str | None = None, offset: str | None = None) -> str:
        """List Team Logs.

        API: GET /v2/teams/:identifier/logs

        Args:
            identifier: Required. Identifier of the team
            identifier_type: Optional. Type of the identifier that is provided in identifier. Possible values are 'id' or 'name'. Default: id
            limit: Optional. Max number of log items to be provided, between 1 and 100. Default: 20
            order: Optional. Sort order of the logs, 'desc' or 'asc'. Default: desc
            offset: Optional. Pagination offset key used to continue listing from a previous point
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/teams/{identifier}/logs"
        params = {"identifierType": identifier_type, "limit": limit, "order": order, "offset": offset}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_team_list_teams() -> str:
        """List Teams.

        API: GET /v2/teams

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.get("/v2/teams", params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_team_update_team_partial(team_id: str, body: dict) -> str:
        """Update Team (Partial).

        API: PATCH /v2/teams/:teamId

        Args:
            team_id: Required. Id of the team
            body: Required. JSON request payload. Fields: `name`, `description`, `members`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/teams/{team_id}"
        params = {}
        try:
            result = await client.patch(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"
