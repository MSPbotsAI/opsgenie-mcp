import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import OpsgenieClient, OpsgenieError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], OpsgenieClient | None]) -> None:

    @mcp.tool()
    async def opsgenie_escalation_create_escalation(body: dict) -> str:
        """Create Escalation.

        API: POST /v2/escalations

        Args:
            body: Required. JSON request payload. Fields: `name`, `description`, `rules`, `ownerTeam`, `repeat`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.post("/v2/escalations", params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_escalation_delete_escalation(identifier: str, identifier_type: str | None = None) -> str:
        """Delete Escalation.

        API: DELETE /v2/escalations/:identifier

        Args:
            identifier: Required. Identifier of the escalation to delete
            identifier_type: Optional. Type of the identifier provided as in-line parameter. Possible values are id and name. Default value is id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/escalations/{identifier}"
        params = {"identifierType": identifier_type}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_escalation_get_escalation(identifier: str, identifier_type: str | None = None) -> str:
        """Get Escalation.

        API: GET /v2/escalations/:identifier

        Args:
            identifier: Required. Identifier of the escalation
            identifier_type: Optional. Type of the identifier provided as in-line parameter. Possible values are id and name. Default value is id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/escalations/{identifier}"
        params = {"identifierType": identifier_type}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_escalation_list_escalations() -> str:
        """List Escalations.

        API: GET /v2/escalations

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.get("/v2/escalations", params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_escalation_update_escalation(identifier: str, body: dict, identifier_type: str | None = None) -> str:
        """Update Escalation.

        API: PATCH /v2/escalations/:identifier

        Args:
            identifier: Required. Identifier of the escalation to update
            body: Required. JSON request payload. Fields: `name`, `description`, `rules`, `ownerTeam`, `repeat`. See the Opsgenie API docs for exact types/constraints.
            identifier_type: Optional. Type of the identifier provided as in-line parameter. Possible values are id and name. Default value is id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/escalations/{identifier}"
        params = {"identifierType": identifier_type}
        try:
            result = await client.patch(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"
