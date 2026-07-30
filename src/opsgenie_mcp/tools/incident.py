import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import OpsgenieClient, OpsgenieError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], OpsgenieClient | None]) -> None:

    @mcp.tool()
    async def opsgenie_incident_add_details_custom_properties_to_incident(identifier: str, body: dict, identifier_type: str | None = None) -> str:
        """Add Details(Custom Properties) to Incident.

        API: POST /v1/incidents/:identifier/details

        Args:
            identifier: Required. Identifier of the incident.
            body: Required. JSON request payload. Fields: `details`, `note`. See the Opsgenie API docs for exact types/constraints.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny. Default id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/incidents/{identifier}/details"
        params = {"identifierType": identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_add_note_to_incident(identifier: str, body: dict, identifier_type: str | None = None) -> str:
        """Add Note to Incident.

        API: POST /v1/incidents/:identifier/notes

        Args:
            identifier: Required. Identifier of the incident.
            body: Required. JSON request payload. Fields: `note`. See the Opsgenie API docs for exact types/constraints.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny. Default id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/incidents/{identifier}/notes"
        params = {"identifierType": identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_add_responder_to_incident(identifier: str, body: dict, identifier_type: str | None = None) -> str:
        """Add Responder to Incident.

        API: POST /v1/incidents/:identifier/responders

        Args:
            identifier: Required. Identifier of the incident.
            body: Required. JSON request payload. Fields: `responder`, `note`. See the Opsgenie API docs for exact types/constraints.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny. Default id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/incidents/{identifier}/responders"
        params = {"identifierType": identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_add_tags_to_incident(identifier: str, body: dict, identifier_type: str | None = None) -> str:
        """Add Tags to Incident.

        API: POST /v1/incidents/:identifier/tags

        Args:
            identifier: Required. Identifier of the incident.
            body: Required. JSON request payload. Fields: `tags`, `note`. See the Opsgenie API docs for exact types/constraints.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny. Default id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/incidents/{identifier}/tags"
        params = {"identifierType": identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_close_incident(identifier: str, body: dict, identifier_type: str | None = None) -> str:
        """Close Incident.

        API: POST /v1/incidents/:identifier/close

        Args:
            identifier: Required. Identifier of the incident.
            body: Required. JSON request payload. Fields: `note`. See the Opsgenie API docs for exact types/constraints.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny. Default id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/incidents/{identifier}/close"
        params = {"identifierType": identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_create_incident(body: dict) -> str:
        """Create Incident.

        API: POST /v1/incidents/create

        Args:
            body: Required. JSON request payload. Fields: `message`, `description`, `responders`, `tags`, `details`, `priority`, `note`, `impactedServices`, `statusPageEntry`, `notifyStakeholders`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.post("/v1/incidents/create", params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_delete_incident(identifier: str, identifier_type: str | None = None) -> str:
        """Delete Incident.

        API: DELETE /v1/incidents/:identifier

        Args:
            identifier: Required. Identifier of the incident.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny. Default id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/incidents/{identifier}"
        params = {"identifierType": identifier_type}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_get_associated_alerts(identifier: str, identifier_type: str | None = None, offset: str | None = None, direction: str | None = None, limit: str | None = None, order: str | None = None) -> str:
        """Get Associated Alerts.

        API: GET /v1/incidents/:identifier/associated-alert-ids

        Args:
            identifier: Required. Identifier of the incident.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny. Default id.
            offset: Optional. Starting value of the offset property. Minimum value 1.
            direction: Optional. Page direction. Default next.
            limit: Optional. Maximum number of items in the result. Default 20, max 25.
            order: Optional. Sorting order of the result set. Possible values desc, asc. Default desc.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/incidents/{identifier}/associated-alert-ids"
        params = {"identifierType": identifier_type, "offset": offset, "direction": direction, "limit": limit, "order": order}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_get_incident(identifier: str, identifier_type: str | None = None) -> str:
        """Get Incident.

        API: GET /v1/incidents/:identifier

        Args:
            identifier: Required. Identifier of the incident.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny. Default id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/incidents/{identifier}"
        params = {"identifierType": identifier_type}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_get_request_status(request_id: str) -> str:
        """Get Request Status.

        API: GET /v1/incidents/requests/:requestId

        Args:
            request_id: Required. Universally unique identifier of the questioned request.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/incidents/requests/{request_id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_get_responder_alerts(identifier: str, identifier_type: str | None = None, offset: str | None = None, direction: str | None = None, limit: str | None = None, order: str | None = None) -> str:
        """Get Responder Alerts.

        API: GET /v1/incidents/:identifier/responder-alert-ids

        Args:
            identifier: Required. Identifier of the incident.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny. Default id.
            offset: Optional. Starting value of the offset property. Minimum value 1.
            direction: Optional. Page direction. Default next.
            limit: Optional. Maximum number of items in the result. Default 20, max 25.
            order: Optional. Sorting order of the result set. Possible values desc, asc. Default desc.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/incidents/{identifier}/responder-alert-ids"
        params = {"identifierType": identifier_type, "offset": offset, "direction": direction, "limit": limit, "order": order}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_list_incident_logs(identifier: str, identifier_type: str | None = None, offset: str | None = None, direction: str | None = None, limit: str | None = None, order: str | None = None) -> str:
        """List Incident Logs.

        API: GET /v1/incidents/:identifier/logs

        Args:
            identifier: Required. Identifier of the incident.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny. Default id.
            offset: Optional. Starting value of the offset property. Minimum value 1.
            direction: Optional. Page direction. Default next.
            limit: Optional. Maximum number of items in the result. Default 20, max 100.
            order: Optional. Sorting order of the result set. Possible values desc, asc. Default desc.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/incidents/{identifier}/logs"
        params = {"identifierType": identifier_type, "offset": offset, "direction": direction, "limit": limit, "order": order}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_list_incident_notes(identifier: str, identifier_type: str | None = None, offset: str | None = None, direction: str | None = None, limit: str | None = None, order: str | None = None) -> str:
        """List Incident Notes.

        API: GET /v1/incidents/:identifier/notes

        Args:
            identifier: Required. Identifier of the incident.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny. Default id.
            offset: Optional. Starting value of the offset property. Minimum value 1.
            direction: Optional. Page direction. Default next.
            limit: Optional. Maximum number of items in the result. Default 20, max 100.
            order: Optional. Sorting order of the result set. Possible values desc, asc. Default desc.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/incidents/{identifier}/notes"
        params = {"identifierType": identifier_type, "offset": offset, "direction": direction, "limit": limit, "order": order}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_list_incidents(query: str | None = None, offset: str | None = None, limit: str | None = None, sort: str | None = None, order: str | None = None) -> str:
        """List Incidents.

        API: GET /v1/incidents

        Args:
            query: Optional. Search query to apply while filtering the incidents.
            offset: Optional. Start index of the result set (pagination). Default 0.
            limit: Optional. Maximum number of items in the result. Default 20, max 100.
            sort: Optional. Field name to sort by. Default insertedAt. Possible values createdAt, insertedAt, updatedAt, status, priority, postmortemStatus, postmortemPublishDueDate.
            order: Optional. Sorting order of the result set. Possible values desc, asc. Default desc.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"query": query, "offset": offset, "limit": limit, "sort": sort, "order": order}
        try:
            result = await client.get("/v1/incidents", params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_remove_details_custom_properties_from_incident(identifier: str, keys: str, identifier_type: str | None = None, note: str | None = None) -> str:
        """Remove Details(Custom Properties) from Incident.

        API: DELETE /v1/incidents/:identifier/details

        Args:
            identifier: Required. Identifier of the incident.
            keys: Required. Comma separated list of keys to remove from the custom properties of the incident. Max 10 keys.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny. Default id.
            note: Optional. Additional incident note to add. Max 25000 characters.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/incidents/{identifier}/details"
        params = {"keys": keys, "identifierType": identifier_type, "note": note}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_remove_tags_from_incident(identifier: str, tags: str, identifier_type: str | None = None, note: str | None = None) -> str:
        """Remove Tags from Incident.

        API: DELETE /v1/incidents/:identifier/tags

        Args:
            identifier: Required. Identifier of the incident.
            tags: Required. Comma separated list of tags to remove from the incident. Max 20 x 50 characters.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny. Default id.
            note: Optional. Additional incident note to add. Max 25000 characters.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/incidents/{identifier}/tags"
        params = {"tags": tags, "identifierType": identifier_type, "note": note}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_reopen_incident(identifier: str, body: dict, identifier_type: str | None = None) -> str:
        """Reopen Incident.

        API: POST /v1/incidents/:identifier/reopen

        Args:
            identifier: Required. Identifier of the incident.
            body: Required. JSON request payload. Fields: `note`. See the Opsgenie API docs for exact types/constraints.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny. Default id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/incidents/{identifier}/reopen"
        params = {"identifierType": identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_resolve_incident(identifier: str, body: dict, identifier_type: str | None = None) -> str:
        """Resolve Incident.

        API: POST /v1/incidents/:identifier/resolve

        Args:
            identifier: Required. Identifier of the incident.
            body: Required. JSON request payload. Fields: `note`. See the Opsgenie API docs for exact types/constraints.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny. Default id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/incidents/{identifier}/resolve"
        params = {"identifierType": identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_update_incident_description(identifier: str, body: dict, identifier_type: str | None = None) -> str:
        """Update Incident Description.

        API: POST /v1/incidents/:identifier/description

        Args:
            identifier: Required. Identifier of the incident.
            body: Required. JSON request payload. Fields: `description`. See the Opsgenie API docs for exact types/constraints.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny. Default id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/incidents/{identifier}/description"
        params = {"identifierType": identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_update_incident_message(identifier: str, body: dict, identifier_type: str | None = None) -> str:
        """Update Incident Message.

        API: POST /v1/incidents/:identifier/message

        Args:
            identifier: Required. Identifier of the incident.
            body: Required. JSON request payload. Fields: `message`. See the Opsgenie API docs for exact types/constraints.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny. Default id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/incidents/{identifier}/message"
        params = {"identifierType": identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_update_incident_priority(identifier: str, body: dict, identifier_type: str | None = None) -> str:
        """Update Incident Priority.

        API: POST /v1/incidents/:identifier/priority

        Args:
            identifier: Required. Identifier of the incident.
            body: Required. JSON request payload. Fields: `priority`. See the Opsgenie API docs for exact types/constraints.
            identifier_type: Optional. Type of the identifier provided in-line. Possible values id, tiny. Default id.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/incidents/{identifier}/priority"
        params = {"identifierType": identifier_type}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"
