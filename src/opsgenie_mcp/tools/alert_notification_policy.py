import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import OpsgenieClient, OpsgenieError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], OpsgenieClient | None]) -> None:

    @mcp.tool()
    async def opsgenie_alert_notification_policy_change_policy_order(identifier: str, body: dict, team_id: str | None = None) -> str:
        """Change Policy Order.

        API: POST /v2/policies/:identifier/change-order

        Args:
            identifier: Required. ID of the policy
            body: Required. JSON request payload. Fields: `targetIndex`. See the Opsgenie API docs for exact types/constraints.
            team_id: Optional. Team identifier; null for global policies
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/policies/{identifier}/change-order"
        params = {"teamId": team_id}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_notification_policy_create_policy(body: dict, team_id: str | None = None) -> str:
        """Create Policy.

        API: POST /v2/policies

        Args:
            body: Required. JSON request payload. Fields: `type`, `name`, `enabled`, `policyDescription`, `filter`, `timeRestrictions`, `message`, `continue`, `alias`, `description`, `entity`, `source`, `ignoreOriginalActions`, `actions`, `ignoreOriginalDetails`, `details`, `ignoreOriginalResponders`, `responders`, `ignoreOriginalTags`, `tags`, `priority`, `autoRestartAction`, `autoCloseAction`, `deduplicationAction`, `delayAction`, `suppress`. See the Opsgenie API docs for exact types/constraints.
            team_id: Optional. Team identifier; if not provided the policy is global
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"teamId": team_id}
        try:
            result = await client.post("/v2/policies", params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_notification_policy_delete_policy(identifier: str, team_id: str | None = None) -> str:
        """Delete Policy.

        API: DELETE /v2/policies/:identifier

        Args:
            identifier: Required. ID of the policy
            team_id: Optional. Team identifier; null for global policies
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/policies/{identifier}"
        params = {"teamId": team_id}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_notification_policy_disable_policy(identifier: str, team_id: str | None = None) -> str:
        """Disable Policy.

        API: POST /v2/policies/:identifier/disable

        Args:
            identifier: Required. ID of the policy
            team_id: Optional. Team identifier; null for global policies
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/policies/{identifier}/disable"
        params = {"teamId": team_id}
        try:
            result = await client.post(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_notification_policy_enable_policy(identifier: str, team_id: str | None = None) -> str:
        """Enable Policy.

        API: POST /v2/policies/:identifier/enable

        Args:
            identifier: Required. ID of the policy
            team_id: Optional. Team identifier; null for global policies
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/policies/{identifier}/enable"
        params = {"teamId": team_id}
        try:
            result = await client.post(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_notification_policy_get_policy(identifier: str, team_id: str | None = None) -> str:
        """Get Policy.

        API: GET /v2/policies/:identifier

        Args:
            identifier: Required. ID of the policy
            team_id: Optional. Team identifier; null for global policies
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/policies/{identifier}"
        params = {"teamId": team_id}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_notification_policy_list_alert_policies(team_id: str | None = None) -> str:
        """List Alert Policies.

        API: GET /v2/policies/alert

        Args:
            team_id: Optional. Team identifier; null for global policies
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"teamId": team_id}
        try:
            result = await client.get("/v2/policies/alert", params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_notification_policy_list_notification_policies(team_id: str) -> str:
        """List Notification Policies.

        API: GET /v2/policies/notification

        Args:
            team_id: Required. Team identifier for which notification policies are listed
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {"teamId": team_id}
        try:
            result = await client.get("/v2/policies/notification", params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_alert_notification_policy_update_policy(identifier: str, body: dict, team_id: str | None = None) -> str:
        """Update Policy.

        API: PUT /v2/policies/:identifier

        Args:
            identifier: Required. ID of the policy
            body: Required. JSON request payload. Fields: `type`, `name`, `enabled`, `policyDescription`, `filter`, `timeRestrictions`, `message`, `continue`, `alias`, `description`, `entity`, `source`, `ignoreOriginalActions`, `actions`, `ignoreOriginalDetails`, `details`, `ignoreOriginalResponders`, `responders`, `ignoreOriginalTags`, `tags`, `priority`, `autoRestartAction`, `autoCloseAction`, `deduplicationAction`, `delayAction`, `suppress`. See the Opsgenie API docs for exact types/constraints.
            team_id: Optional. Team identifier; null for global policies
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/policies/{identifier}"
        params = {"teamId": team_id}
        try:
            result = await client.put(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"
