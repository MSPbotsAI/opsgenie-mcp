import json
from collections.abc import Callable

from mcp.server.fastmcp import FastMCP

from ..api_client import OpsgenieClient, OpsgenieError
from ._common import NO_TOKEN


def register(mcp: FastMCP, client_factory: Callable[[], OpsgenieClient | None]) -> None:

    @mcp.tool()
    async def opsgenie_contact_create_contact(user_identifier: str, body: dict) -> str:
        """Create Contact.

        API: POST /v2/users/:userIdentifier/contacts

        Args:
            user_identifier: Required. Identifier of the user that the contact will belong to; either id or username of the user
            body: Required. JSON request payload. Fields: `method`, `to`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{user_identifier}/contacts"
        params = {}
        try:
            result = await client.post(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_contact_delete_contact(user_identifier: str, contact_id: str) -> str:
        """Delete Contact.

        API: DELETE /v2/users/:userIdentifier/contacts/:contactId

        Args:
            user_identifier: Required. Identifier of the user that the contact belongs to; either id or username of the user
            contact_id: Required. Id of the contact
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{user_identifier}/contacts/{contact_id}"
        params = {}
        try:
            result = await client.delete(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_contact_disable_contact(user_identifier: str, contact_id: str) -> str:
        """Disable Contact.

        API: POST /v2/users/:userIdentifier/contacts/:contactId/disable

        Args:
            user_identifier: Required. Identifier of the user that the contact belongs to; either id or username of the user
            contact_id: Required. Id of the contact
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{user_identifier}/contacts/{contact_id}/disable"
        params = {}
        try:
            result = await client.post(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_contact_enable_contact(user_identifier: str, contact_id: str) -> str:
        """Enable Contact.

        API: POST /v2/users/:userIdentifier/contacts/:contactId/enable

        Args:
            user_identifier: Required. Identifier of the user that the contact belongs to; either id or username of the user
            contact_id: Required. Id of the contact
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{user_identifier}/contacts/{contact_id}/enable"
        params = {}
        try:
            result = await client.post(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_contact_get_contact(user_identifier: str, contact_id: str) -> str:
        """Get Contact.

        API: GET /v2/users/:userIdentifier/contacts/:contactId

        Args:
            user_identifier: Required. Identifier of the user that the contact belongs to; either id or username of the user
            contact_id: Required. Id of the contact
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{user_identifier}/contacts/{contact_id}"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_contact_list_contacts(user_identifier: str) -> str:
        """List Contacts.

        API: GET /v2/users/:userIdentifier/contacts

        Args:
            user_identifier: Required. Identifier of the user that the contacts belong to; either id or username of the user
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{user_identifier}/contacts"
        params = {}
        try:
            result = await client.get(path, params=params)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"

    @mcp.tool()
    async def opsgenie_contact_update_contact_partial(user_identifier: str, contact_id: str, body: dict) -> str:
        """Update Contact (Partial).

        API: PATCH /v2/users/:userIdentifier/contacts/:contactId

        Args:
            user_identifier: Required. Identifier of the user that the contact belongs to; either id or username of the user
            contact_id: Required. Id of the contact
            body: Required. JSON request payload. Fields: `to`. See the Opsgenie API docs for exact types/constraints.
        """
        client = client_factory()
        if client is None:
            return NO_TOKEN
        path = f"/v2/users/{user_identifier}/contacts/{contact_id}"
        params = {}
        try:
            result = await client.patch(path, params=params, json_body=body)
            return json.dumps(result, indent=2, default=str)
        except OpsgenieError as e:
            return f"Error: {e}"
