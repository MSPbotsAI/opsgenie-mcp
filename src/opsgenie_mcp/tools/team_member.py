import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import OpsgenieClient, OpsgenieError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], OpsgenieClient | None]) -> None:

    @mcp.tool()
    async def opsgenie_team_member_add_team_member(team_identifier: str, body: dict, team_identifier_type: str | None = None) -> str:
        """Add Team Member.

        API: POST /v2/teams/:teamIdentifier/members

        Args:
            team_identifier: Required. Identifier of the team
            body: Required. JSON request payload. Fields: `user`, `role`. See the Opsgenie API docs for exact types/constraints.
            team_identifier_type: Optional. Type of the team identifier that is provided. Possible values are 'id' or 'name'. Default: id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/teams/{team_identifier}/members"
        params = {"teamIdentifierType": team_identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_team_member_remove_team_member(team_identifier: str, member_identifier: str, team_identifier_type: str | None = None) -> str:
        """Remove Team Member.

        API: DELETE /v2/teams/:teamIdentifier/members/:memberIdentifier

        Args:
            team_identifier: Required. Identifier of the team
            member_identifier: Required. User id or username of the member to remove from the team
            team_identifier_type: Optional. Type of the team identifier that is provided. Possible values are 'id' or 'name'. Default: id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/teams/{team_identifier}/members/{member_identifier}"
        params = {"teamIdentifierType": team_identifier_type}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"
