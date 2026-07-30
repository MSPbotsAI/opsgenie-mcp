import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import OpsgenieClient, OpsgenieError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], OpsgenieClient | None]) -> None:

    @mcp.tool()
    async def opsgenie_user_create_user(body: dict) -> str:
        """Create User.

        API: POST /v2/users

        Args:
            body: Required. JSON request payload. Fields: `username`, `fullName`, `role`, `skypeUsername`, `userAddress`, `tags`, `details`, `timezone`, `locale`, `invitationDisabled`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.post("/v2/users", params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_user_delete_saved_search(identifier: str, identifier_type: str | None = None) -> str:
        """Delete Saved Search.

        API: DELETE /v1/incidents/saved-searches/:identifier

        Args:
            identifier: Required. Identifier of the saved search
            identifier_type: Optional. Type of the saved search identifier provided as an in-line parameter; id or name; default id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/incidents/saved-searches/{identifier}"
        params = {"identifierType": identifier_type}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_user_delete_user(identifier: str) -> str:
        """Delete User.

        API: DELETE /v2/users/:identifier

        Args:
            identifier: Required. Identifier of the user; either id or username
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{identifier}"
        params = {}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_user_get_saved_search(identifier: str, identifier_type: str | None = None) -> str:
        """Get Saved Search.

        API: GET /v2/users/saved-searches/:identifier

        Args:
            identifier: Required. Identifier of the saved search
            identifier_type: Optional. Type of the saved search identifier provided as an in-line parameter; id or name; default id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/saved-searches/{identifier}"
        params = {"identifierType": identifier_type}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_user_get_user(identifier: str, expand: str | None = None) -> str:
        """Get User.

        API: GET /v2/users/:identifier

        Args:
            identifier: Required. Identifier of the user; either id or username
            expand: Optional. Comma separated list of additional fields to include in the response, e.g. contact
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{identifier}"
        params = {"expand": expand}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_user_list_saved_searches() -> str:
        """List Saved Searches.

        API: GET /v2/users/saved-searches

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.get("/v2/users/saved-searches", params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_user_list_user(limit: str | None = None, offset: str | None = None, sort: str | None = None, order: str | None = None, query: str | None = None) -> str:
        """List User.

        API: GET /v2/users

        Args:
            limit: Optional. Maximum number of users to retrieve per page; default 100
            offset: Optional. Number of users to skip before starting to collect results; default 0
            sort: Optional. Field to sort the result set by; one of username, fullName, createdAt; default username
            order: Optional. Sort direction; asc or desc; default asc
            query: Optional. Advanced search query using field:value combinations
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"limit": limit, "offset": offset, "sort": sort, "order": order, "query": query}
        try:
            result = await client.get("/v2/users", params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_user_list_user_escalations(identifier: str) -> str:
        """List User Escalations.

        API: GET /v2/users/:identifier/escalations

        Args:
            identifier: Required. Identifier of the user; either id or username
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{identifier}/escalations"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_user_list_user_forwarding_rules(identifier: str) -> str:
        """List User Forwarding Rules.

        API: GET /v2/users/:identifier/forwarding-rules

        Args:
            identifier: Required. Identifier of the user; either id or username
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{identifier}/forwarding-rules"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_user_list_user_schedules(identifier: str) -> str:
        """List User Schedules.

        API: GET /v2/users/:identifier/schedules

        Args:
            identifier: Required. Identifier of the user; either id or username
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{identifier}/schedules"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_user_list_user_teams(identifier: str) -> str:
        """List User Teams.

        API: GET /v2/users/:identifier/teams

        Args:
            identifier: Required. Identifier of the user; either id or username
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{identifier}/teams"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_user_update_user_partial(identifier: str, body: dict) -> str:
        """Update User (Partial).

        API: PATCH /v2/users/:identifier

        Args:
            identifier: Required. Identifier of the user; either id or username
            body: Required. JSON request payload. Fields: `username`, `fullName`, `role`, `skypeUsername`, `userAddress`, `tags`, `details`, `timezone`, `locale`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{identifier}"
        params = {}
        try:
            result = await client.patch(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"
