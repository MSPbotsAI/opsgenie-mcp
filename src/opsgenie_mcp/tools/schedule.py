import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import OpsgenieClient, OpsgenieError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], OpsgenieClient | None]) -> None:

    @mcp.tool()
    async def opsgenie_schedule_create_schedule(body: dict) -> str:
        """Create Schedule.

        API: POST /v2/schedules

        Args:
            body: Required. JSON request payload. Fields: `name`, `description`, `timezone`, `enabled`, `ownerTeam`, `rotations`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.post("/v2/schedules", params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_schedule_delete_schedule(identifier: str, identifier_type: str | None = None) -> str:
        """Delete Schedule.

        API: DELETE /v2/schedules/:identifier

        Args:
            identifier: Required. Identifier of the schedule
            identifier_type: Optional. Type of the identifier that is provided in identifier. Possible values are 'id' or 'name'. Default: id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/schedules/{identifier}"
        params = {"identifierType": identifier_type}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_schedule_export_schedule(identifier: str, identifier_type: str | None = None) -> str:
        """Export Schedule.

        API: GET /v2/schedules/:identifier.ics

        Args:
            identifier: Required. Identifier of the schedule
            identifier_type: Optional. Type of the identifier that is provided in identifier. Possible values are 'id' or 'name'. Default: id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/schedules/{identifier}.ics"
        params = {"identifierType": identifier_type}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_schedule_get_schedule(identifier: str, identifier_type: str | None = None) -> str:
        """Get Schedule.

        API: GET /v2/schedules/:identifier

        Args:
            identifier: Required. Identifier of the schedule
            identifier_type: Optional. Type of the identifier that is provided in identifier. Possible values are 'id' or 'name'. Default: id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/schedules/{identifier}"
        params = {"identifierType": identifier_type}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_schedule_get_schedule_timeline(identifier: str, identifier_type: str | None = None, expand: str | None = None, interval: str | None = None, interval_unit: str | None = None, date: str | None = None) -> str:
        """Get Schedule Timeline.

        API: GET /v2/schedules/:identifier/timeline

        Args:
            identifier: Required. Identifier of the schedule
            identifier_type: Optional. Type of the identifier that is provided in identifier. Possible values are 'id' or 'name'. Default: id
            expand: Optional. Additional data to include in the response. Possible values: 'base', 'forwarding', 'override'
            interval: Optional. Length of the timeline interval. Default: 1
            interval_unit: Optional. Unit of the interval. Possible values: 'days', 'weeks', 'months'. Default: weeks
            date: Optional. Date to start the timeline from, in format yyyy-MM-dd'T'HH:mm:ssZ
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/schedules/{identifier}/timeline"
        params = {"identifierType": identifier_type, "expand": expand, "interval": interval, "intervalUnit": interval_unit, "date": date}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_schedule_list_schedules(expand: str | None = None) -> str:
        """List Schedules.

        API: GET /v2/schedules

        Args:
            expand: Optional. Returns a detailed response of the schedule when set to 'rotation'
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"expand": expand}
        try:
            result = await client.get("/v2/schedules", params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_schedule_update_schedule_partial(identifier: str, body: dict, identifier_type: str | None = None) -> str:
        """Update Schedule (Partial).

        API: PATCH /v2/schedules/:identifier

        Args:
            identifier: Required. Identifier of the schedule
            body: Required. JSON request payload. Fields: `name`, `description`, `timezone`, `enabled`, `ownerTeam`, `rotations`. See the Opsgenie API docs for exact types/constraints.
            identifier_type: Optional. Type of the identifier that is provided in identifier. Possible values are 'id' or 'name'. Default: id
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/schedules/{identifier}"
        params = {"identifierType": identifier_type}
        try:
            result = await client.patch(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"
