import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import OpsgenieClient, OpsgenieError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], OpsgenieClient | None]) -> None:

    @mcp.tool()
    async def opsgenie_who_is_on_call_export_on_call_user(identifier: str) -> str:
        """Export On-Call User.

        API: GET /v2/schedules/on-calls/:identifier.ics

        Args:
            identifier: Required. Identifier of the user (id or username) whose personal on-call timeline (3 months) will be exported as an .ics file
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/schedules/on-calls/{identifier}.ics"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_who_is_on_call_get_next_on_calls(schedule_identifier: str, schedule_identifier_type: str | None = None, flat: str | None = None, date: str | None = None) -> str:
        """Get Next On Calls.

        API: GET /v2/schedules/:scheduleIdentifier/next-on-calls

        Args:
            schedule_identifier: Required. Identifier of the schedule to retrieve next on-call information for
            schedule_identifier_type: Optional. Type of the schedule identifier provided as in-line parameter (id or name). Default value is id
            flat: Optional. When enabled, retrieves user names of all next on-call participants. Default value is false
            date: Optional. Date time to query next on-call information for, format yyyy-MM-dd'T'HH:mm:ssZ. Default value is the current moment
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/schedules/{schedule_identifier}/next-on-calls"
        params = {"scheduleIdentifierType": schedule_identifier_type, "flat": flat, "date": date}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_who_is_on_call_get_on_calls(schedule_identifier: str, schedule_identifier_type: str | None = None, flat: str | None = None, date: str | None = None) -> str:
        """Get On Calls.

        API: GET /v2/schedules/:scheduleIdentifier/on-calls

        Args:
            schedule_identifier: Required. Identifier of the schedule to retrieve on-call information for
            schedule_identifier_type: Optional. Type of the schedule identifier provided as in-line parameter (id or name). Default value is id
            flat: Optional. When enabled, retrieves user names of all on-call participants (including escalation/team expansion) instead of nested objects. Default value is false
            date: Optional. Date time to query on-call information for, format yyyy-MM-dd'T'HH:mm:ssZ. Default value is the current moment
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/schedules/{schedule_identifier}/on-calls"
        params = {"scheduleIdentifierType": schedule_identifier_type, "flat": flat, "date": date}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_who_is_on_call_list_on_calls(flat: str | None = None, date: str | None = None) -> str:
        """List On Calls.

        API: GET /v2/schedules/on-calls

        Args:
            flat: Optional. When enabled, retrieves user names of all on-call participants. Default value is false
            date: Optional. Date time to query on-call information for, format yyyy-MM-dd'T'HH:mm:ssZ. Default value is the current moment
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"flat": flat, "date": date}
        try:
            result = await client.get("/v2/schedules/on-calls", params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"
