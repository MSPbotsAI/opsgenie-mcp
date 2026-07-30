import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import OpsgenieClient, OpsgenieError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], OpsgenieClient | None]) -> None:

    @mcp.tool()
    async def opsgenie_incident_timeline_add_incident_timeline_entry(incident_id: str, body: dict) -> str:
        """Add Incident Timeline Entry.

        API: POST /v2/incident-timelines/:incidentId/entries

        Args:
            incident_id: Required. Identifier of the related incident.
            body: Required. JSON request payload. Fields: `description`, `time`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/incident-timelines/{incident_id}/entries"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_timeline_delete_incident_timeline_entry(incident_id: str, timeline_entry_id: str) -> str:
        """Delete Incident Timeline Entry.

        API: DELETE /v2/incident-timelines/:incidentId/entries/:timelineEntryId

        Args:
            incident_id: Required. Identifier of the incident.
            timeline_entry_id: Required. Identifier of the incident timeline entry.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/incident-timelines/{incident_id}/entries/{timeline_entry_id}"
        params = {}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_timeline_get_incident_timeline_entry(incident_id: str, timeline_entry_id: str, content_type: str | None = None) -> str:
        """Get Incident Timeline Entry.

        API: GET /v2/incident-timelines/:incidentId/entries/:timelineEntryId

        Args:
            incident_id: Required. Identifier of the related incident.
            timeline_entry_id: Required. Identifier of the incident timeline entry.
            content_type: Optional. Type of the content. Only 'plain_text' supported currently. Default plain_text.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/incident-timelines/{incident_id}/entries/{timeline_entry_id}"
        params = {"contentType": content_type}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_timeline_hide_incident_timeline_entry(incident_id: str, timeline_entry_id: str) -> str:
        """Hide Incident Timeline Entry.

        API: PATCH /v2/incident-timelines/:incidentId/entries/:timelineEntryId/hide

        Args:
            incident_id: Required. Identifier of the incident.
            timeline_entry_id: Required. Identifier of the incident timeline entry.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/incident-timelines/{incident_id}/entries/{timeline_entry_id}/hide"
        params = {}
        try:
            result = await client.patch(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_timeline_list_incident_timeline_entries(incident_id: str, group: str | None = None, discard_hidden: str | None = None, offset: str | None = None, order: str | None = None, limit: str | None = None, content_type: str | None = None) -> str:
        """List Incident Timeline Entries.

        API: GET /v2/incident-timelines/:incidentId/entries

        Args:
            incident_id: Required. Identifier of the incident.
            group: Optional. Filter by entry group(s). Possible values: custom, incident, responderAlert, stakeholderUpdate, statusPage, iccSessionLifecycle, iccSessionDetails, integration.
            discard_hidden: Optional. If true, returns only unhidden entries. Default false.
            offset: Optional. Offset of the previous incident timeline entry page (nextOffset value of previous query).
            order: Optional. Sort order by eventTime. Default desc.
            limit: Optional. Item count per page. Between 1 and 20. Default 20.
            content_type: Optional. Type of the content. Only 'plain_text' supported. Default plain_text.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/incident-timelines/{incident_id}/entries"
        params = {"group": group, "discardHidden": discard_hidden, "offset": offset, "order": order, "limit": limit, "contentType": content_type}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_timeline_unhide_incident_timeline_entry(incident_id: str, timeline_entry_id: str) -> str:
        """Unhide Incident Timeline Entry.

        API: PATCH /v2/incident-timelines/:incidentId/entries/:timelineEntryId/unhide

        Args:
            incident_id: Required. Identifier of the incident.
            timeline_entry_id: Required. Identifier of the incident timeline entry.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/incident-timelines/{incident_id}/entries/{timeline_entry_id}/unhide"
        params = {}
        try:
            result = await client.patch(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_timeline_update_incident_timeline_entry(incident_id: str, timeline_entry_id: str, body: dict) -> str:
        """Update Incident Timeline Entry.

        API: PUT /v2/incident-timelines/:incidentId/entries/:timelineEntryId

        Args:
            incident_id: Required. Identifier of the related incident.
            timeline_entry_id: Required. Identifier of the incident timeline entry.
            body: Required. JSON request payload. Fields: `description`, `time`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/incident-timelines/{incident_id}/entries/{timeline_entry_id}"
        params = {}
        try:
            result = await client.put(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"
