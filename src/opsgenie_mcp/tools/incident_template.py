import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import OpsgenieClient, OpsgenieError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], OpsgenieClient | None]) -> None:

    @mcp.tool()
    async def opsgenie_incident_template_create_incident_template(body: dict) -> str:
        """Create Incident Template.

        API: POST /v1/incident-templates

        Args:
            body: Required. JSON request payload. Fields: `name`, `message`, `description`, `tags`, `details`, `priority`, `impactedServices`, `stakeholderProperties`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.post("/v1/incident-templates", params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_template_delete_incident_template(incident_template_id: str) -> str:
        """Delete Incident Template.

        API: DELETE /v1/incident-templates/:incidentTemplateId

        Args:
            incident_template_id: Required. Id of the incident template to delete. Max 130 characters.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/incident-templates/{incident_template_id}"
        params = {}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_template_get_incident_templates() -> str:
        """Get Incident Templates.

        API: GET /v1/incident-templates

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.get("/v1/incident-templates", params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_incident_template_update_incident_template(incident_template_id: str, body: dict) -> str:
        """Update Incident Template.

        API: PUT /v1/incident-templates/:incidentTemplateId

        Args:
            incident_template_id: Required. Id of the incident template to update. Max 130 characters.
            body: Required. JSON request payload. Fields: `name`, `message`, `description`, `tags`, `details`, `priority`, `impactedServices`, `stakeholderProperties`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/incident-templates/{incident_template_id}"
        params = {}
        try:
            result = await client.put(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"
