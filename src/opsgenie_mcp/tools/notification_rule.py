import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import OpsgenieClient, OpsgenieError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], OpsgenieClient | None]) -> None:

    @mcp.tool()
    async def opsgenie_notification_rule_copy_notification_rules_to_other_users(user_identifier: str, body: dict) -> str:
        """Copy Notification Rules to Other Users.

        API: PATCH /v2/users/:userIdentifier/notification-rules/copy-to

        Args:
            user_identifier: Required. Identifier of the user that the notification rules originally belong to; either id or username of the user
            body: Required. JSON request payload. Fields: `toUsers`, `ruleTypes`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{user_identifier}/notification-rules/copy-to"
        params = {}
        try:
            result = await client.patch(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_notification_rule_create_notification_rule(user_identifier: str, body: dict) -> str:
        """Create Notification Rule.

        API: POST /v2/users/:userIdentifier/notification-rules

        Args:
            user_identifier: Required. Identifier of the user for this notification rule; either id or username of the user
            body: Required. JSON request payload. Fields: `name`, `actionType`, `criteria`, `notificationTime`, `timeRestriction`, `schedules`, `order`, `steps`, `repeat`, `enabled`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{user_identifier}/notification-rules"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_notification_rule_delete_notification_rule(user_identifier: str, rule_id: str) -> str:
        """Delete Notification Rule.

        API: DELETE /v2/users/:userIdentifier/notification-rules/:ruleId

        Args:
            user_identifier: Required. Identifier of the user for this notification rule; either id or username of the user
            rule_id: Required. Id of the notification rule
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{user_identifier}/notification-rules/{rule_id}"
        params = {}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_notification_rule_disable_notification_rule(user_identifier: str, rule_id: str) -> str:
        """Disable Notification Rule.

        API: POST /v2/users/:userIdentifier/notification-rules/:ruleId/disable

        Args:
            user_identifier: Required. Identifier of the user for this notification rule; either id or username of the user
            rule_id: Required. Id of the notification rule
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{user_identifier}/notification-rules/{rule_id}/disable"
        params = {}
        try:
            result = await client.post(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_notification_rule_enable_notification_rule(user_identifier: str, rule_id: str) -> str:
        """Enable Notification Rule.

        API: POST /v2/users/:userIdentifier/notification-rules/:ruleId/enable

        Args:
            user_identifier: Required. Identifier of the user for this notification rule; either id or username of the user
            rule_id: Required. Id of the notification rule
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{user_identifier}/notification-rules/{rule_id}/enable"
        params = {}
        try:
            result = await client.post(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_notification_rule_get_notification_rule(user_identifier: str, rule_id: str) -> str:
        """Get Notification Rule.

        API: GET /v2/users/:userIdentifier/notification-rules/:ruleId

        Args:
            user_identifier: Required. Identifier of the user for this notification rule; either id or username of the user
            rule_id: Required. Id of the notification rule
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{user_identifier}/notification-rules/{rule_id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_notification_rule_list_notification_rule(user_identifier: str) -> str:
        """List Notification Rule.

        API: GET /v2/users/:userIdentifier/notification-rules

        Args:
            user_identifier: Required. Identifier of the user for this notification rule; either id or username of the user
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{user_identifier}/notification-rules"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_notification_rule_update_notification_rule_partial(user_identifier: str, rule_id: str, body: dict) -> str:
        """Update Notification Rule (Partial).

        API: PATCH /v2/users/:userIdentifier/notification-rules/:ruleId

        Args:
            user_identifier: Required. Identifier of the user for this notification rule; either id or username of the user
            rule_id: Required. Id of the notification rule
            body: Required. JSON request payload. Fields: `name`, `criteria`, `notificationTime`, `timeRestriction`, `schedules`, `steps`, `repeat`, `order`, `enabled`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{user_identifier}/notification-rules/{rule_id}"
        params = {}
        try:
            result = await client.patch(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"
