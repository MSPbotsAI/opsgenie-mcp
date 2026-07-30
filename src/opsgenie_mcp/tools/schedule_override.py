import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import OpsgenieClient, OpsgenieError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], OpsgenieClient | None]) -> None:

    @mcp.tool()
    async def opsgenie_schedule_override_create_schedule_override(schedule_identifier: str, body: dict, schedule_identifier_type: str | None = None) -> str:
        """Create Schedule Override.

        API: POST /v2/schedules/:scheduleIdentifier/overrides

        Args:
            schedule_identifier: Required. Identifier of the schedule that the override will be created under
            body: Required. JSON request payload. Fields: `alias`, `user`, `startDate`, `endDate`, `rotations`. See the Opsgenie API docs for exact types/constraints.
            schedule_identifier_type: Optional. Type of the schedule identifier provided as in-line parameter (id or name). Default value is id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/schedules/{schedule_identifier}/overrides"
        params = {"scheduleIdentifierType": schedule_identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_schedule_override_delete_schedule_override(schedule_identifier: str, alias: str, schedule_identifier_type: str | None = None) -> str:
        """Delete Schedule Override.

        API: DELETE /v2/schedules/:scheduleIdentifier/overrides/:alias

        Args:
            schedule_identifier: Required. Identifier of the schedule that the override belongs to
            alias: Required. Alias of the schedule override to delete
            schedule_identifier_type: Optional. Type of the schedule identifier provided as in-line parameter (id or name). Default value is id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/schedules/{schedule_identifier}/overrides/{alias}"
        params = {"scheduleIdentifierType": schedule_identifier_type}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_schedule_override_get_schedule_override(schedule_identifier: str, alias: str, schedule_identifier_type: str | None = None) -> str:
        """Get Schedule Override.

        API: GET /v2/schedules/:scheduleIdentifier/overrides/:alias

        Args:
            schedule_identifier: Required. Identifier of the schedule that the override belongs to
            alias: Required. Alias of the schedule override
            schedule_identifier_type: Optional. Type of the schedule identifier provided as in-line parameter (id or name). Default value is id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/schedules/{schedule_identifier}/overrides/{alias}"
        params = {"scheduleIdentifierType": schedule_identifier_type}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_schedule_override_list_schedule_overrides(schedule_identifier: str, schedule_identifier_type: str | None = None) -> str:
        """List Schedule Overrides.

        API: GET /v2/schedules/:scheduleIdentifier/overrides

        Args:
            schedule_identifier: Required. Identifier of the schedule whose overrides will be listed
            schedule_identifier_type: Optional. Type of the schedule identifier provided as in-line parameter (id or name). Default value is id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/schedules/{schedule_identifier}/overrides"
        params = {"scheduleIdentifierType": schedule_identifier_type}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_schedule_override_update_schedule_override(schedule_identifier: str, alias: str, body: dict, schedule_identifier_type: str | None = None) -> str:
        """Update Schedule Override.

        API: PUT /v2/schedules/:scheduleIdentifier/overrides/:alias

        Args:
            schedule_identifier: Required. Identifier of the schedule that the override belongs to
            alias: Required. Alias of the schedule override to update
            body: Required. JSON request payload. Fields: `user`, `startDate`, `endDate`, `rotations`. See the Opsgenie API docs for exact types/constraints.
            schedule_identifier_type: Optional. Type of the schedule identifier provided as in-line parameter (id or name). Default value is id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/schedules/{schedule_identifier}/overrides/{alias}"
        params = {"scheduleIdentifierType": schedule_identifier_type}
        try:
            result = await client.put(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"
