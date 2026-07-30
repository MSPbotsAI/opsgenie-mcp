import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import OpsgenieClient, OpsgenieError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], OpsgenieClient | None]) -> None:

    @mcp.tool()
    async def opsgenie_maintenance_cancel_maintenance(maintenance_id: str) -> str:
        """Cancel Maintenance.

        API: POST /v1/maintenance/:maintenanceId/cancel

        Args:
            maintenance_id: Required. ID of the maintenance
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/maintenance/{maintenance_id}/cancel"
        params = {}
        try:
            result = await client.post(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_maintenance_change_maintenance_end_date(maintenance_id: str, body: dict) -> str:
        """Change Maintenance End Date.

        API: POST /v1/maintenance/:maintenanceId/change-end-date

        Args:
            maintenance_id: Required. ID of the maintenance
            body: Required. JSON request payload. Fields: `endDate`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/maintenance/{maintenance_id}/change-end-date"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_maintenance_create_maintenance(body: dict) -> str:
        """Create Maintenance.

        API: POST /v1/maintenance

        Args:
            body: Required. JSON request payload. Fields: `description`, `time`, `rules`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.post("/v1/maintenance", params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_maintenance_delete_maintenance(maintenance_id: str) -> str:
        """Delete Maintenance.

        API: DELETE /v1/maintenance/:maintenanceId

        Args:
            maintenance_id: Required. ID of the maintenance
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/maintenance/{maintenance_id}"
        params = {}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_maintenance_get_maintenance(maintenance_id: str) -> str:
        """Get Maintenance.

        API: GET /v1/maintenance/:maintenanceId

        Args:
            maintenance_id: Required. ID of the maintenance
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/maintenance/{maintenance_id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_maintenance_list_maintenance(type: str | None = None) -> str:
        """List Maintenance.

        API: GET /v1/maintenance

        Args:
            type: Optional. Filter by status: all (default), non-expired, or past
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"type": type}
        try:
            result = await client.get("/v1/maintenance", params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_maintenance_update_maintenance(maintenance_id: str, body: dict) -> str:
        """Update Maintenance.

        API: PUT /v1/maintenance/:maintenanceId

        Args:
            maintenance_id: Required. ID of the maintenance
            body: Required. JSON request payload. Fields: `description`, `time`, `rules`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/maintenance/{maintenance_id}"
        params = {}
        try:
            result = await client.put(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"
