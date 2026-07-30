import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import OpsgenieClient, OpsgenieError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], OpsgenieClient | None]) -> None:

    @mcp.tool()
    async def opsgenie_service_incident_rule_create_incident_rule(service_id: str, body: dict) -> str:
        """Create Incident Rule.

        API: POST /v1/services/:serviceId/incident-rules

        Args:
            service_id: Required. Id of the service on which the incident rule will be created. Max 130 characters.
            body: Required. JSON request payload. Fields: `conditionMatchType`, `conditions`, `incidentProperties`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/services/{service_id}/incident-rules"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_service_incident_rule_delete_incident_rule(service_id: str, incident_rule_id: str) -> str:
        """Delete Incident Rule.

        API: DELETE /v1/services/:serviceId/incident-rules/:incidentRuleId

        Args:
            service_id: Required. Id of the service on which the incident rule exists. Max 130 characters.
            incident_rule_id: Required. Id of the incident rule to be deleted. Max 130 characters.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/services/{service_id}/incident-rules/{incident_rule_id}"
        params = {}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_service_incident_rule_get_incident_rules(service_id: str) -> str:
        """Get Incident Rules.

        API: GET /v1/services/:serviceId/incident-rules

        Args:
            service_id: Required. Id of the service from which incident rules will be retrieved. Max 130 characters.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/services/{service_id}/incident-rules"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_service_incident_rule_update_incident_rule(service_id: str, incident_rule_id: str, body: dict) -> str:
        """Update Incident Rule.

        API: PUT /v1/services/:serviceId/incident-rules/:incidentRuleId

        Args:
            service_id: Required. Id of the service on which the incident rule exists. Max 130 characters.
            incident_rule_id: Required. Id of the incident rule to be updated. Max 130 characters.
            body: Required. JSON request payload. Fields: `conditionMatchType`, `conditions`, `incidentProperties`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/services/{service_id}/incident-rules/{incident_rule_id}"
        params = {}
        try:
            result = await client.put(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"
