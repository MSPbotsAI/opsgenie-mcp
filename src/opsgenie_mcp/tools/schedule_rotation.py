import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import OpsgenieClient, OpsgenieError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], OpsgenieClient | None]) -> None:

    @mcp.tool()
    async def opsgenie_schedule_rotation_create_rotation(schedule_identifier: str, body: dict, schedule_identifier_type: str | None = None) -> str:
        """Create Rotation.

        API: POST /v2/schedules/:scheduleIdentifier/rotations

        Args:
            schedule_identifier: Required. Identifier of the schedule (id or name) that the rotation will be created under
            body: Required. JSON request payload. Fields: `name`, `startDate`, `endDate`, `type`, `length`, `participants`, `timeRestriction`. See the Opsgenie API docs for exact types/constraints.
            schedule_identifier_type: Optional. Type of the schedule identifier provided as in-line parameter. Possible values are id and name. Default value is id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/schedules/{schedule_identifier}/rotations"
        params = {"scheduleIdentifierType": schedule_identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_schedule_rotation_delete_rotation(schedule_identifier: str, id: str, schedule_identifier_type: str | None = None) -> str:
        """Delete Rotation.

        API: DELETE /v2/schedules/:scheduleIdentifier/rotations/:id

        Args:
            schedule_identifier: Required. Identifier of the schedule (id or name) that the rotation belongs to
            id: Required. Identifier of the rotation to delete
            schedule_identifier_type: Optional. Type of the schedule identifier provided as in-line parameter. Possible values are id and name. Default value is id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/schedules/{schedule_identifier}/rotations/{id}"
        params = {"scheduleIdentifierType": schedule_identifier_type}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_schedule_rotation_get_rotation(schedule_identifier: str, id: str, schedule_identifier_type: str | None = None) -> str:
        """Get Rotation.

        API: GET /v2/schedules/:scheduleIdentifier/rotations/:id

        Args:
            schedule_identifier: Required. Identifier of the schedule (id or name) that the rotation belongs to
            id: Required. Identifier of the rotation
            schedule_identifier_type: Optional. Type of the schedule identifier provided as in-line parameter. Possible values are id and name. Default value is id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/schedules/{schedule_identifier}/rotations/{id}"
        params = {"scheduleIdentifierType": schedule_identifier_type}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_schedule_rotation_list_rotations(schedule_identifier: str, schedule_identifier_type: str | None = None) -> str:
        """List Rotations.

        API: GET /v2/schedules/:scheduleIdentifier/rotations

        Args:
            schedule_identifier: Required. Identifier of the schedule (id or name) whose rotations will be listed
            schedule_identifier_type: Optional. Type of the schedule identifier provided as in-line parameter. Possible values are id and name. Default value is id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/schedules/{schedule_identifier}/rotations"
        params = {"scheduleIdentifierType": schedule_identifier_type}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_schedule_rotation_update_rotation(schedule_identifier: str, id: str, body: dict, schedule_identifier_type: str | None = None) -> str:
        """Update Rotation.

        API: PATCH /v2/schedules/:scheduleIdentifier/rotations/:id

        Args:
            schedule_identifier: Required. Identifier of the schedule (id or name) that the rotation belongs to
            id: Required. Identifier of the rotation to update
            body: Required. JSON request payload. Fields: `name`, `startDate`, `endDate`, `type`, `length`, `participants`, `timeRestriction`. See the Opsgenie API docs for exact types/constraints.
            schedule_identifier_type: Optional. Type of the schedule identifier provided as in-line parameter. Possible values are id and name. Default value is id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/schedules/{schedule_identifier}/rotations/{id}"
        params = {"scheduleIdentifierType": schedule_identifier_type}
        try:
            result = await client.patch(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"
