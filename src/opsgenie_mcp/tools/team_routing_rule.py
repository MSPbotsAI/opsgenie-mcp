import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import OpsgenieClient, OpsgenieError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], OpsgenieClient | None]) -> None:

    @mcp.tool()
    async def opsgenie_team_routing_rule_change_team_routing_rule_order(team_identifier: str, id: str, body: dict, team_identifier_type: str | None = None) -> str:
        """Change Team Routing Rule Order.

        API: POST /v2/teams/:teamIdentifier/routing-rules/:id/change-order

        Args:
            team_identifier: Required. Identifier of the team
            id: Required. Id of the routing rule whose order is being changed
            body: Required. JSON request payload. Fields: `order`. See the Opsgenie API docs for exact types/constraints.
            team_identifier_type: Optional. Type of the team identifier that is provided. Possible values are 'id' or 'name'. Default: id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/teams/{team_identifier}/routing-rules/{id}/change-order"
        params = {"teamIdentifierType": team_identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_team_routing_rule_create_team_routing_rule(team_identifier: str, body: dict, team_identifier_type: str | None = None) -> str:
        """Create Team Routing Rule.

        API: POST /v2/teams/:teamIdentifier/routing-rules

        Args:
            team_identifier: Required. Identifier of the team
            body: Required. JSON request payload. Fields: `name`, `order`, `timezone`, `criteria`, `timeRestriction`, `notify`. See the Opsgenie API docs for exact types/constraints.
            team_identifier_type: Optional. Type of the team identifier that is provided. Possible values are 'id' or 'name'. Default: id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/teams/{team_identifier}/routing-rules"
        params = {"teamIdentifierType": team_identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_team_routing_rule_delete_team_routing_rule(team_identifier: str, id: str, team_identifier_type: str | None = None) -> str:
        """Delete Team Routing Rule.

        API: DELETE /v2/teams/:teamIdentifier/routing-rules/:id

        Args:
            team_identifier: Required. Identifier of the team
            id: Required. Id of the routing rule
            team_identifier_type: Optional. Type of the team identifier that is provided. Possible values are 'id' or 'name'. Default: id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/teams/{team_identifier}/routing-rules/{id}"
        params = {"teamIdentifierType": team_identifier_type}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_team_routing_rule_get_team_routing_rule(team_identifier: str, id: str, team_identifier_type: str | None = None) -> str:
        """Get Team Routing Rule.

        API: GET /v2/teams/:teamIdentifier/routing-rules/:id

        Args:
            team_identifier: Required. Identifier of the team
            id: Required. Id of the routing rule
            team_identifier_type: Optional. Type of the team identifier that is provided. Possible values are 'id' or 'name'. Default: id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/teams/{team_identifier}/routing-rules/{id}"
        params = {"teamIdentifierType": team_identifier_type}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_team_routing_rule_list_team_routing_rules(team_identifier: str, team_identifier_type: str | None = None) -> str:
        """List Team Routing Rules.

        API: GET /v2/teams/:teamIdentifier/routing-rules

        Args:
            team_identifier: Required. Identifier of the team
            team_identifier_type: Optional. Type of the team identifier that is provided. Possible values are 'id' or 'name'. Default: id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/teams/{team_identifier}/routing-rules"
        params = {"teamIdentifierType": team_identifier_type}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_team_routing_rule_update_team_routing_rule_partial(team_identifier: str, id: str, body: dict, team_identifier_type: str | None = None) -> str:
        """Update Team Routing Rule (Partial).

        API: PATCH /v2/teams/:teamIdentifier/routing-rules/:id

        Args:
            team_identifier: Required. Identifier of the team
            id: Required. Id of the routing rule
            body: Required. JSON request payload. Fields: `name`, `timezone`, `criteria`, `timeRestriction`, `notify`. See the Opsgenie API docs for exact types/constraints.
            team_identifier_type: Optional. Type of the team identifier that is provided. Possible values are 'id' or 'name'. Default: id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/teams/{team_identifier}/routing-rules/{id}"
        params = {"teamIdentifierType": team_identifier_type}
        try:
            result = await client.patch(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"
