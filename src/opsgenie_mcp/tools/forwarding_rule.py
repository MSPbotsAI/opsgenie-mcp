import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import OpsgenieClient, OpsgenieError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], OpsgenieClient | None]) -> None:

    @mcp.tool()
    async def opsgenie_forwarding_rule_create_forwarding_rule(body: dict) -> str:
        """Create Forwarding Rule.

        API: POST /v2/forwarding-rules

        Args:
            body: Required. JSON request payload. Fields: `alias`, `fromUser`, `toUser`, `startDate`, `endDate`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.post("/v2/forwarding-rules", params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_forwarding_rule_delete_forwarding_rule(identifier: str, identifier_type: str | None = None) -> str:
        """Delete Forwarding Rule.

        API: DELETE /v2/forwarding-rules/:identifier

        Args:
            identifier: Required. Identifier of the forwarding rule to delete (id or alias)
            identifier_type: Optional. Type of the identifier provided as in-line parameter. Possible values are id and alias. Default value is id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/forwarding-rules/{identifier}"
        params = {"identifierType": identifier_type}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_forwarding_rule_get_forwarding_rule(identifier: str, identifier_type: str | None = None) -> str:
        """Get Forwarding Rule.

        API: GET /v2/forwarding-rules/:identifier

        Args:
            identifier: Required. Identifier of the forwarding rule (id or alias)
            identifier_type: Optional. Type of the identifier provided as in-line parameter. Possible values are id and alias. Default value is id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/forwarding-rules/{identifier}"
        params = {"identifierType": identifier_type}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_forwarding_rule_list_forwarding_rules() -> str:
        """List Forwarding Rules.

        API: GET /v2/forwarding-rules

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.get("/v2/forwarding-rules", params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_forwarding_rule_update_forwarding_rule(identifier: str, body: dict, identifier_type: str | None = None) -> str:
        """Update Forwarding Rule.

        API: PUT /v2/forwarding-rules/:identifier

        Args:
            identifier: Required. Identifier of the forwarding rule to update (id or alias)
            body: Required. JSON request payload. Fields: `alias`, `fromUser`, `toUser`, `startDate`, `endDate`. See the Opsgenie API docs for exact types/constraints.
            identifier_type: Optional. Type of the identifier provided as in-line parameter. Possible values are id and alias. Default value is id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/forwarding-rules/{identifier}"
        params = {"identifierType": identifier_type}
        try:
            result = await client.put(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"
