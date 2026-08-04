import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import OpsgenieClient, OpsgenieError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], OpsgenieClient | None]) -> None:
    @mcp.tool()
    async def opsgenie_alert_acknowledge_alert(identifier: str, body: dict, identifier_type: str | None = None) -> str:
        """Acknowledge Alert.

        API: POST /v2/alerts/:identifier/acknowledge

        Args:
            identifier: Required. Identifier of the alert.
            body: Required. JSON request payload. Fields: `user`, `source`, `note`. See the Opsgenie API docs for exact types/constraints.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny, alias. Default id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/alerts/{identifier}/acknowledge"
        params = {"identifierType": identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_add_note_to_alert(identifier: str, body: dict, identifier_type: str | None = None) -> str:
        """Add Note to Alert.

        API: POST /v2/alerts/:identifier/notes

        Args:
            identifier: Required. Identifier of the alert.
            body: Required. JSON request payload. Fields: `user`, `source`, `note`. See the Opsgenie API docs for exact types/constraints.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny, alias. Default id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/alerts/{identifier}/notes"
        params = {"identifierType": identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_add_responder_to_alert(identifier: str, body: dict, identifier_type: str | None = None) -> str:
        """Add Responder to Alert.

        API: POST /v2/alerts/:identifier/responders

        Args:
            identifier: Required. Identifier of the alert.
            body: Required. JSON request payload. Fields: `responder`, `user`, `source`, `note`. See the Opsgenie API docs for exact types/constraints.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny, alias. Default id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/alerts/{identifier}/responders"
        params = {"identifierType": identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_add_tags_to_alert(identifier: str, body: dict, identifier_type: str | None = None) -> str:
        """Add Tags to Alert.

        API: POST /v2/alerts/:identifier/tags

        Args:
            identifier: Required. Identifier of the alert.
            body: Required. JSON request payload. Fields: `tags`, `user`, `source`, `note`. See the Opsgenie API docs for exact types/constraints.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny, alias. Default id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/alerts/{identifier}/tags"
        params = {"identifierType": identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_add_team_to_alert(identifier: str, body: dict, identifier_type: str | None = None) -> str:
        """Add Team to Alert.

        API: POST /v2/alerts/:identifier/teams

        Args:
            identifier: Required. Identifier of the alert.
            body: Required. JSON request payload. Fields: `team`, `user`, `source`, `note`. See the Opsgenie API docs for exact types/constraints.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny, alias. Default id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/alerts/{identifier}/teams"
        params = {"identifierType": identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_assign_alert(identifier: str, body: dict, identifier_type: str | None = None) -> str:
        """Assign Alert.

        API: POST /v2/alerts/:identifier/assign

        Args:
            identifier: Required. Identifier of the alert.
            body: Required. JSON request payload. Fields: `owner`, `user`, `source`, `note`. See the Opsgenie API docs for exact types/constraints.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny, alias. Default id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/alerts/{identifier}/assign"
        params = {"identifierType": identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_close_alert(identifier: str, body: dict, identifier_type: str | None = None) -> str:
        """Close Alert.

        API: POST /v2/alerts/:identifier/close

        Args:
            identifier: Required. Identifier of the alert.
            body: Required. JSON request payload. Fields: `user`, `source`, `note`. See the Opsgenie API docs for exact types/constraints.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny, alias. Default id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/alerts/{identifier}/close"
        params = {"identifierType": identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_count_alerts(query: str | None = None, search_identifier: str | None = None, search_identifier_type: str | None = None) -> str:
        """Count Alerts.

        API: GET /v2/alerts/count

        Args:
            query: Optional. Search query to apply while filtering the alerts.
            search_identifier: Optional. Identifier of the saved search query to apply while filtering the alerts.
            search_identifier_type: Optional. Identifier type of the saved search query. Possible values id, name. Default id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"query": query, "searchIdentifier": search_identifier, "searchIdentifierType": search_identifier_type}
        try:
            result = await client.get("/v2/alerts/count", params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_create_alert(body: dict) -> str:
        """Create Alert.

        API: POST /v2/alerts

        Args:
            body: Required. JSON request payload. Fields: `message`, `alias`, `description`, `responders`, `visibleTo`, `actions`, `tags`, `details`, `entity`, `source`, `priority`, `user`, `note`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.post("/v2/alerts", params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_delete_alert(identifier: str, identifier_type: str | None = None, user: str | None = None, source: str | None = None) -> str:
        """Delete Alert.

        API: DELETE /v2/alerts/:identifier

        Args:
            identifier: Required. Identifier of the alert.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values are AlertID and tinyID.
            user: Optional. Display name of the request owner. Max 100 characters.
            source: Optional. Display name of the request source. Max 100 characters.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/alerts/{identifier}"
        params = {"identifierType": identifier_type, "user": user, "source": source}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_escalate_alert_to_next(identifier: str, body: dict, identifier_type: str | None = None) -> str:
        """Escalate Alert to Next.

        API: POST /v2/alerts/:identifier/escalate

        Args:
            identifier: Required. Identifier of the alert.
            body: Required. JSON request payload. Fields: `escalation`, `user`, `source`, `note`. See the Opsgenie API docs for exact types/constraints.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny, alias. Default id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/alerts/{identifier}/escalate"
        params = {"identifierType": identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_get_alert(identifier: str, identifier_type: str | None = None) -> str:
        """Get Alert.

        API: GET /v2/alerts/:identifier

        Args:
            identifier: Required. Identifier of the alert.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values are id, tiny and alias. Default is id. Alias cannot be used to retrieve closed alerts.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/alerts/{identifier}"
        params = {"identifierType": identifier_type}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_get_request_status(request_id: str) -> str:
        """Get Request Status.

        API: GET /v2/alerts/requests/:requestId

        Args:
            request_id: Required. Universally unique identifier of the questioned request.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/alerts/requests/{request_id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_list_alert_logs(identifier: str, identifier_type: str | None = None, offset: str | None = None, direction: str | None = None, limit: str | None = None, order: str | None = None) -> str:
        """List Alert Logs.

        API: GET /v2/alerts/:identifier/logs

        Args:
            identifier: Required. Identifier of the alert.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny, alias. Default id.
            offset: Optional. Starting value of the offset property.
            direction: Optional. Page direction to apply for the given offset. Possible values next, prev. Default next.
            limit: Optional. Maximum number of items in the result. Default 20, max 100.
            order: Optional. Sorting order of the result set. Possible values desc, asc. Default desc.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/alerts/{identifier}/logs"
        params = {"identifierType": identifier_type, "offset": offset, "direction": direction, "limit": limit, "order": order}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_list_alert_notes(identifier: str, identifier_type: str | None = None, offset: str | None = None, direction: str | None = None, limit: str | None = None, order: str | None = None) -> str:
        """List Alert Notes.

        API: GET /v2/alerts/:identifier/notes

        Args:
            identifier: Required. Identifier of the alert.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny, alias. Default id.
            offset: Optional. Starting value of the offset property.
            direction: Optional. Page direction to apply for the given offset. Possible values next, prev. Default next.
            limit: Optional. Maximum number of items in the result. Default 20, max 100.
            order: Optional. Sorting order of the result set. Possible values desc, asc. Default desc.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/alerts/{identifier}/notes"
        params = {"identifierType": identifier_type, "offset": offset, "direction": direction, "limit": limit, "order": order}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_list_alerts(query: str | None = None, search_identifier: str | None = None, search_identifier_type: str | None = None, offset: str | None = None, limit: str | None = None, sort: str | None = None, order: str | None = None) -> str:
        """List Alerts.

        API: GET /v2/alerts

        Args:
            query: Optional. Search query to apply while filtering the alerts.
            search_identifier: Optional. Identifier of the saved search query to apply while filtering the alerts.
            search_identifier_type: Optional. Identifier type of the saved search query. Possible values id, name. Default id.
            offset: Optional. Start index of the result set (pagination). Default 0.
            limit: Optional. Maximum number of items in the result. Default 20, max 100.
            sort: Optional. Field name to sort by. Default createdAt. Possible values include updatedAt, tinyId, alias, message, status, acknowledged, isSeen, snoozed, snoozedUntil, count, lastOccurredAt, source, owner, integration.name, integration.type, report.ackTime, report.closeTime, report.acknowledgedBy, report.closedBy.
            order: Optional. Sorting order of the result set. Possible values desc, asc. Default desc.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"query": query, "searchIdentifier": search_identifier, "searchIdentifierType": search_identifier_type, "offset": offset, "limit": limit, "sort": sort, "order": order}
        try:
            result = await client.get("/v2/alerts", params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_remove_tags_from_alert(identifier: str, tags: str, identifier_type: str | None = None, user: str | None = None, source: str | None = None, note: str | None = None) -> str:
        """Remove Tags from Alert.

        API: DELETE /v2/alerts/:identifier/tags

        Args:
            identifier: Required. Identifier of the alert.
            tags: Required. Comma separated list of tags to remove from the alert. Max 20 x 50 characters.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny, alias. Default id.
            user: Optional. Display name of the request owner. Max 100 characters.
            source: Optional. Display name of the request source. Max 100 characters.
            note: Optional. Additional alert note to add. Max 25000 characters.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/alerts/{identifier}/tags"
        params = {"tags": tags, "identifierType": identifier_type, "user": user, "source": source, "note": note}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_snooze_alert(identifier: str, body: dict, identifier_type: str | None = None) -> str:
        """Snooze Alert.

        API: POST /v2/alerts/:identifier/snooze

        Args:
            identifier: Required. Identifier of the alert.
            body: Required. JSON request payload. Fields: `endTime`, `user`, `source`, `note`. See the Opsgenie API docs for exact types/constraints.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny, alias. Default id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/alerts/{identifier}/snooze"
        params = {"identifierType": identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_unacknowledge_alert(identifier: str, body: dict, identifier_type: str | None = None) -> str:
        """Unacknowledge Alert.

        API: POST /v2/alerts/:identifier/unacknowledge

        Args:
            identifier: Required. Identifier of the alert.
            body: Required. JSON request payload. Fields: `user`, `source`, `note`. See the Opsgenie API docs for exact types/constraints.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny, alias. Default id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/alerts/{identifier}/unacknowledge"
        params = {"identifierType": identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_update_alert_description(identifier: str, body: dict, identifier_type: str | None = None) -> str:
        """Update Alert Description.

        API: POST /v2/alerts/:identifier/description

        Args:
            identifier: Required. Identifier of the alert.
            body: Required. JSON request payload. Fields: `description`. See the Opsgenie API docs for exact types/constraints.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny, alias. Default id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/alerts/{identifier}/description"
        params = {"identifierType": identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_update_alert_message(identifier: str, body: dict, identifier_type: str | None = None) -> str:
        """Update Alert Message.

        API: POST /v2/alerts/:identifier/message

        Args:
            identifier: Required. Identifier of the alert.
            body: Required. JSON request payload. Fields: `message`. See the Opsgenie API docs for exact types/constraints.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny, alias. Default id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/alerts/{identifier}/message"
        params = {"identifierType": identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_update_alert_priority(identifier: str, body: dict, identifier_type: str | None = None) -> str:
        """Update Alert Priority.

        API: PUT /v2/alerts/:identifier/priority

        Args:
            identifier: Required. Identifier of the alert.
            body: Required. JSON request payload. Fields: `priority`. See the Opsgenie API docs for exact types/constraints.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny, alias. Default id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/alerts/{identifier}/priority"
        params = {"identifierType": identifier_type}
        try:
            result = await client.put(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

