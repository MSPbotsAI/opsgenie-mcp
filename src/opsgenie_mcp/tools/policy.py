import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import OpsgenieClient, OpsgenieError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], OpsgenieClient | None]) -> None:

    @mcp.tool()
    async def opsgenie_policy_change_policy_order(identifier: str, body: dict) -> str:
        """Change Policy Order.

        API: POST /v1/policies/:identifier/change-order

        Args:
            identifier: Required. ID of the policy
            body: Required. JSON request payload. Fields: `targetIndex`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/policies/{identifier}/change-order"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_policy_create_policy(body: dict) -> str:
        """Create Policy.

        API: POST /v1/policies

        Args:
            body: Required. JSON request payload. Fields: `type`, `name`, `enabled`, `policyDescription`, `filter`, `timeRestrictions`, `duration`, `maxRepeatCount`, `deduplicationActionType`, `count`, `delayOption`, `untilMinute`, `untilHour`, `message`, `continue`, `alias`, `description`, `entity`, `source`, `ignoreOriginalAlertActions`, `alertActions`, `ignoreOriginalDetails`, `details`, `ignoreOriginalRecipients`, `recipients`, `ignoreOriginalTags`, `tags`, `ignoreOriginalTeams`, `priority`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.post("/v1/policies", params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_policy_delete_policy(identifier: str) -> str:
        """Delete Policy.

        API: DELETE /v1/policies/:identifier

        Args:
            identifier: Required. ID of the policy
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/policies/{identifier}"
        params = {}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_policy_disable_policy(identifier: str) -> str:
        """Disable Policy.

        API: POST /v1/policies/:identifier/disable

        Args:
            identifier: Required. ID of the policy
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/policies/{identifier}/disable"
        params = {}
        try:
            result = await client.post(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_policy_enable_policy(identifier: str) -> str:
        """Enable Policy.

        API: POST /v1/policies/:identifier/enable

        Args:
            identifier: Required. ID of the policy
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/policies/{identifier}/enable"
        params = {}
        try:
            result = await client.post(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_policy_get_policy(identifier: str) -> str:
        """Get Policy.

        API: GET /v1/policies/:identifier

        Args:
            identifier: Required. ID of the policy
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/policies/{identifier}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_policy_list_policies() -> str:
        """List Policies.

        API: GET /v1/policies

        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        params = {}
        try:
            result = await client.get("/v1/policies", params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_policy_update_policy(identifier: str, body: dict) -> str:
        """Update Policy.

        API: PUT /v1/policies/:identifier

        Args:
            identifier: Required. ID of the policy
            body: Required. JSON request payload. Fields: `type`, `name`, `enabled`, `policyDescription`, `filter`, `timeRestrictions`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v1/policies/{identifier}"
        params = {}
        try:
            result = await client.put(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"
