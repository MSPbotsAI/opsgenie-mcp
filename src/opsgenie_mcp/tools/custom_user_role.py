import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import OpsgenieClient, OpsgenieError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], OpsgenieClient | None]) -> None:

    @mcp.tool()
    async def opsgenie_custom_user_role_create_custom_user_role(body: dict) -> str:
        """Create Custom User Role.

        API: POST /v2/roles

        Args:
            body: Required. JSON request payload. Fields: `name`, `extendedRole`, `grantedRights`, `disallowedRights`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.post("/v2/roles", params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_custom_user_role_delete_custom_user_role(identifier: str, identifier_type: str | None = None) -> str:
        """Delete Custom User Role.

        API: DELETE /v2/roles/:identifier

        Args:
            identifier: Required. Identifier of the custom user role
            identifier_type: Optional. Type of the custom user role identifier provided as an in-line parameter; id or name; default id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/roles/{identifier}"
        params = {"identifierType": identifier_type}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_custom_user_role_get_custom_user_role(identifier: str, identifier_type: str | None = None) -> str:
        """Get Custom User Role.

        API: GET /v2/roles/:identifier

        Args:
            identifier: Required. Identifier of the custom user role
            identifier_type: Optional. Type of the custom user role identifier provided as an in-line parameter; id or name; default id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/roles/{identifier}"
        params = {"identifierType": identifier_type}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_custom_user_role_list_custom_user_roles() -> str:
        """List Custom User Roles.

        API: GET /v2/roles

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.get("/v2/roles", params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_custom_user_role_update_custom_user_role(identifier: str, body: dict, identifier_type: str | None = None) -> str:
        """Update Custom User Role.

        API: PUT /v2/roles/:identifier

        Args:
            identifier: Required. Identifier of the custom user role
            body: Required. JSON request payload. Fields: `name`, `extendedRole`, `grantedRights`, `disallowedRights`. See the Opsgenie API docs for exact types/constraints.
            identifier_type: Optional. Type of the custom user role identifier provided as an in-line parameter; id or name; default id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/roles/{identifier}"
        params = {"identifierType": identifier_type}
        try:
            result = await client.put(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"
