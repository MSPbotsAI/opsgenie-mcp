import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import OpsgenieClient, OpsgenieError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], OpsgenieClient | None]) -> None:

    @mcp.tool()
    async def opsgenie_team_role_create_team_role(team_identifier: str, body: dict, team_identifier_type: str | None = None) -> str:
        """Create Team Role.

        API: POST /v2/teams/:teamIdentifier/roles

        Args:
            team_identifier: Required. Identifier of the team
            body: Required. JSON request payload. Fields: `name`, `rights`. See the Opsgenie API docs for exact types/constraints.
            team_identifier_type: Optional. Type of the team identifier that is provided. Possible values are 'id' or 'name'. Default: id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/teams/{team_identifier}/roles"
        params = {"teamIdentifierType": team_identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_team_role_delete_team_role(team_identifier: str, identifier: str, team_identifier_type: str | None = None, identifier_type: str | None = None) -> str:
        """Delete Team Role.

        API: DELETE /v2/teams/:teamIdentifier/roles/:identifier

        Args:
            team_identifier: Required. Identifier of the team
            identifier: Required. Identifier of the team role
            team_identifier_type: Optional. Type of the team identifier that is provided. Possible values are 'id' or 'name'. Default: id
            identifier_type: Optional. Type of the team role identifier that is provided. Possible values are 'id' or 'name'. Default: id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/teams/{team_identifier}/roles/{identifier}"
        params = {"teamIdentifierType": team_identifier_type, "identifierType": identifier_type}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_team_role_get_team_role(team_identifier: str, identifier: str, team_identifier_type: str | None = None, identifier_type: str | None = None) -> str:
        """Get Team Role.

        API: GET /v2/teams/:teamIdentifier/roles/:identifier

        Args:
            team_identifier: Required. Identifier of the team
            identifier: Required. Identifier of the team role
            team_identifier_type: Optional. Type of the team identifier that is provided. Possible values are 'id' or 'name'. Default: id
            identifier_type: Optional. Type of the team role identifier that is provided. Possible values are 'id' or 'name'. Default: id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/teams/{team_identifier}/roles/{identifier}"
        params = {"teamIdentifierType": team_identifier_type, "identifierType": identifier_type}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_team_role_list_team_roles(team_identifier: str, team_identifier_type: str | None = None) -> str:
        """List Team Roles.

        API: GET /v2/teams/:teamIdentifier/roles

        Args:
            team_identifier: Required. Identifier of the team
            team_identifier_type: Optional. Type of the team identifier that is provided. Possible values are 'id' or 'name'. Default: id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/teams/{team_identifier}/roles"
        params = {"teamIdentifierType": team_identifier_type}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_team_role_update_team_role_partial(team_identifier: str, identifier: str, body: dict, team_identifier_type: str | None = None, identifier_type: str | None = None) -> str:
        """Update Team Role (Partial).

        API: PATCH /v2/teams/:teamIdentifier/roles/:identifier

        Args:
            team_identifier: Required. Identifier of the team
            identifier: Required. Identifier of the team role
            body: Required. JSON request payload. Fields: `name`, `rights`. See the Opsgenie API docs for exact types/constraints.
            team_identifier_type: Optional. Type of the team identifier that is provided. Possible values are 'id' or 'name'. Default: id
            identifier_type: Optional. Type of the team role identifier that is provided. Possible values are 'id' or 'name'. Default: id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/teams/{team_identifier}/roles/{identifier}"
        params = {"teamIdentifierType": team_identifier_type, "identifierType": identifier_type}
        try:
            result = await client.patch(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"
