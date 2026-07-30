import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import OpsgenieClient, OpsgenieError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], OpsgenieClient | None]) -> None:

    @mcp.tool()
    async def opsgenie_notification_rule_step_create_notification_rule_step(user_identifier: str, rule_id: str, body: dict) -> str:
        """Create Notification Rule Step.

        API: POST /v2/users/:userIdentifier/notification-rules/:ruleId/steps

        Args:
            user_identifier: Required. Identifier of the user; either id or username of the user
            rule_id: Required. Id of the notification rule containing the step
            body: Required. JSON request payload. Fields: `contact`, `sendAfter`, `enabled`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{user_identifier}/notification-rules/{rule_id}/steps"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_notification_rule_step_delete_notification_rule_step(user_identifier: str, rule_id: str, step_id: str) -> str:
        """Delete Notification Rule Step.

        API: DELETE /v2/users/:userIdentifier/notification-rules/:ruleId/steps/:stepId

        Args:
            user_identifier: Required. Identifier of the user; either id or username of the user
            rule_id: Required. Id of the notification rule
            step_id: Required. Id of the notification rule step to delete
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{user_identifier}/notification-rules/{rule_id}/steps/{step_id}"
        params = {}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_notification_rule_step_disable_notification_rule_step(user_identifier: str, rule_id: str, step_id: str) -> str:
        """Disable Notification Rule Step.

        API: POST /v2/users/:userIdentifier/notification-rules/:ruleId/steps/:stepId/disable

        Args:
            user_identifier: Required. Identifier of the user; either id or username of the user
            rule_id: Required. Id of the notification rule
            step_id: Required. Id of the notification rule step to disable
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{user_identifier}/notification-rules/{rule_id}/steps/{step_id}/disable"
        params = {}
        try:
            result = await client.post(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_notification_rule_step_enable_notification_rule_step(user_identifier: str, rule_id: str, step_id: str) -> str:
        """Enable Notification Rule Step.

        API: POST /v2/users/:userIdentifier/notification-rules/:ruleId/steps/:stepId/enable

        Args:
            user_identifier: Required. Identifier of the user; either id or username of the user
            rule_id: Required. Id of the notification rule
            step_id: Required. Id of the notification rule step to enable
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{user_identifier}/notification-rules/{rule_id}/steps/{step_id}/enable"
        params = {}
        try:
            result = await client.post(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_notification_rule_step_get_notification_rule_step(user_identifier: str, rule_id: str, step_id: str) -> str:
        """Get Notification Rule Step.

        API: GET /v2/users/:userIdentifier/notification-rules/:ruleId/steps/:stepId

        Args:
            user_identifier: Required. Identifier of the user; either id or username of the user
            rule_id: Required. Id of the notification rule
            step_id: Required. Id of the notification rule step
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{user_identifier}/notification-rules/{rule_id}/steps/{step_id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_notification_rule_step_list_notification_rule_steps(user_identifier: str, rule_id: str) -> str:
        """List Notification Rule Steps.

        API: GET /v2/users/:userIdentifier/notification-rules/:ruleId/steps

        Args:
            user_identifier: Required. Identifier of the user; either id or username of the user
            rule_id: Required. Id of the notification rule
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{user_identifier}/notification-rules/{rule_id}/steps"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_notification_rule_step_update_notification_rule_step_partial(user_identifier: str, rule_id: str, step_id: str, body: dict) -> str:
        """Update Notification Rule Step (Partial).

        API: PATCH /v2/users/:userIdentifier/notification-rules/:ruleId/steps/:stepId

        Args:
            user_identifier: Required. Identifier of the user; either id or username of the user
            rule_id: Required. Id of the notification rule
            step_id: Required. Id of the notification rule step to update
            body: Required. JSON request payload. Fields: `contact`, `sendAfter`, `enabled`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{user_identifier}/notification-rules/{rule_id}/steps/{step_id}"
        params = {}
        try:
            result = await client.patch(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"
