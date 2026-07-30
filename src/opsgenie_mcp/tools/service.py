import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import OpsgenieClient, OpsgenieError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], OpsgenieClient | None]) -> None:

    @mcp.tool()
    async def opsgenie_service_create_service(body: dict) -> str:
        """Create Service.

        API: POST /v1/services

        Args:
            body: Required. JSON request payload. Fields: `name`, `teamId`, `description`, `tags`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.post("/v1/services", params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_service_delete_service(id: str) -> str:
        """Delete Service.

        API: DELETE /v1/services/:id

        Args:
            id: Required. Id of the service to delete.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/services/{id}"
        params = {}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_service_get_service(id: str) -> str:
        """Get Service.

        API: GET /v1/services/:id

        Args:
            id: Required. Id of the service to retrieve. Max 130 characters.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/services/{id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_service_list_services(query: str | None = None, limit: str | None = None, sort: str | None = None, order: str | None = None, offset: str | None = None) -> str:
        """List Services.

        API: GET /v1/services/

        Args:
            query: Optional. Search filter for services.
            limit: Optional. Maximum number of results to return. Default: 20, max: 100, min: 1.
            sort: Optional. Field to sort results by. Possible values: updatedAt, insertedAt, createdAt, name, isExternal. Default: name.
            order: Optional. Sort order direction. Possible values: desc, asc. Default: desc.
            offset: Optional. Pagination start index. Default: 0.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"query": query, "limit": limit, "sort": sort, "order": order, "offset": offset}
        try:
            result = await client.get("/v1/services/", params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_service_update_service(id: str, body: dict) -> str:
        """Update Service.

        API: PATCH /v1/services/:id

        Args:
            id: Required. Id of the service to update. Max 130 characters.
            body: Required. JSON request payload. Fields: `name`, `description`, `tags`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/services/{id}"
        params = {}
        try:
            result = await client.patch(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"
