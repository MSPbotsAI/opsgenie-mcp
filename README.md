# opsgenie-mcp

MCP server for **Opsgenie** (Atlassian's incident/alert management and
on-call platform) — exposes the full public Opsgenie REST API as MCP tools.

> **⚠️ Vendor note**: Atlassian has announced Opsgenie is reaching
> [end of support](http://atlassian.com/blog/announcements/evolution-of-it-operations)
> and recommends migrating to Jira Service Management or Compass. The public
> API documented here (`docs.opsgenie.com`) is still live and unchanged as of
> this build, but expect it to eventually be deprecated.

## Overview

- Stateless HTTP service. No credentials are ever persisted — each request
  supplies its own API key via a header, used only for the lifetime of that
  single request.
- Supports concurrent requests; per-request credential isolation is done via
  Python `contextvars`, not a global/shared client instance.
- Entry points: `POST /mcp` (MCP protocol) and `GET /health` (health check).
- Default port: `8080` (configurable via `MCP_HTTP_PORT`).

## Scope

**22 tools**, trimmed down from an original 213-tool full-API build
(2026-08-04), all in the single `alert` category. MSPbots' own stored
integration config for this vendor calls exactly **1** endpoint
(`GET /v2/alerts`, read-only, → `opsgenie_alert_list_alerts`). Per the
"actual usage + same-category core CRUD" scope decision, every *other*
category (Incident, Incident Timeline, Integration, Heartbeat, Alert &
Notification Policy, Policy (legacy v1), Maintenance, Account, User,
Custom User Role, Contact, Notification Rule (+ Step), Team (+ Member/
Role/Routing Rule), Schedule (+ Rotation/Override), Escalation, Who Is On
Call, Forwarding Rule, Service (+ Incident Rules/Templates), Incident
Templates — 27 categories, ~178 tools) was removed entirely, since
MSPbots doesn't touch any of them; within the `alert` category itself,
35 original tools were cut to the 22 core alert-lifecycle operations
(list/get/create/close/delete/acknowledge/unacknowledge/note/tags/
assign/responder/team/escalate/snooze/update message-description-priority/
count/logs/request-status) — dropped were the saved-search sub-feature (5
tools), the attachment sub-feature (4 tools), custom-properties add/remove
(2 tools), `execute_custom_action` (1), and `list_alert_recipients` (1),
none of which are core alert CRUD.

Source data for the kept tools was originally extracted by fetching
`docs.opsgenie.com/docs/alert-api` and structuring each documented
operation (method, path, path/query params, JSON body fields) into a
machine-readable format — the same codegen-from-structured-spec approach
used for other large-API vendors in this program (ConnectSecure, Dynu,
Jira Data Center), adapted here because Opsgenie has no downloadable
OpenAPI/Postman spec, only prose documentation. If a removed category is
needed later, the same source pages (`docs.opsgenie.com/docs/*-api`) can
be re-parsed the same way.

## Authentication

Opsgenie uses a static **API key** tied to a specific Opsgenie integration
(created in Opsgenie's Settings → Integrations → API). MSPbots' own
integration convention sends this key as `Authorization: GenieKey <apiKey>`,
matching Opsgenie's own documented format, and this server forwards it
exactly that way.

### HEADER 授权参数说明

| Header | 类型 | 是否必填 | 默认值 | 枚举值 | 字段描述 | Example |
|---|---|---|---|---|---|---|
| `X-Opsgenie-Api-Key` | string | 是 | 无 | 无 | Opsgenie 集成 API Key，原样转发为上游 `Authorization: GenieKey <apiKey>` 请求头 | `X-Opsgenie-Api-Key: a1b2c3d4-e5f6-7890-abcd-ef1234567890` |
| `X-Opsgenie-Base-Url` | string | 否 | `https://api.opsgenie.com` | 无 | Opsgenie API 基础 URL；EU 实例客户需传 `https://api.eu.opsgenie.com` | `X-Opsgenie-Base-Url: https://api.eu.opsgenie.com` |

Missing the required header returns `401`:
```json
{
  "error": "Missing credentials",
  "message": "This server requires the X-Opsgenie-Api-Key header",
  "required_headers": ["X-Opsgenie-Api-Key"],
  "optional_headers": ["X-Opsgenie-Base-Url"]
}
```

## Environment Variables

| Variable | 类型 | 是否必填 | 默认值 | 说明 |
|---|---|---|---|---|
| `MCP_HTTP_PORT` | int | 否 | `8080` | HTTP 监听端口 |
| `MCP_HTTP_HOST` | string | 否 | `0.0.0.0` | HTTP 监听地址 |
| `OPSGENIE_BASE_URL` | string | 否 | `https://api.opsgenie.com` | 默认 Opsgenie API 基础 URL（可被请求头 `X-Opsgenie-Base-Url` 覆盖） |

## MCP Endpoint

- `POST /mcp` — MCP protocol (streamable HTTP transport)
- `GET /health` — health check, returns `{"status": "ok", "service": "opsgenie-mcp", "transport": "http"}`

## Tool List

Tool names are `opsgenie_<category>_<operation>`, derived from each
operation's heading in the official docs (e.g. "List Alerts" in the `alert`
category → `opsgenie_alert_list_alerts`). `body` parameters are accepted as
a generic `dict` — the exact field list for each is documented in that
tool's own docstring (extracted from the source docs), and the full field
schema is available in Opsgenie's own API reference (linked below).

| Category | Tool | Description | Method + Path | Params |
|---|---|---|---|---|
| alert | `opsgenie_alert_acknowledge_alert` | Acknowledge Alert. | POST /v2/alerts/:identifier/acknowledge | identifier(required), body(required), identifier_type(optional) |
| alert | `opsgenie_alert_add_note_to_alert` | Add Note to Alert. | POST /v2/alerts/:identifier/notes | identifier(required), body(required), identifier_type(optional) |
| alert | `opsgenie_alert_add_responder_to_alert` | Add Responder to Alert. | POST /v2/alerts/:identifier/responders | identifier(required), body(required), identifier_type(optional) |
| alert | `opsgenie_alert_add_tags_to_alert` | Add Tags to Alert. | POST /v2/alerts/:identifier/tags | identifier(required), body(required), identifier_type(optional) |
| alert | `opsgenie_alert_add_team_to_alert` | Add Team to Alert. | POST /v2/alerts/:identifier/teams | identifier(required), body(required), identifier_type(optional) |
| alert | `opsgenie_alert_assign_alert` | Assign Alert. | POST /v2/alerts/:identifier/assign | identifier(required), body(required), identifier_type(optional) |
| alert | `opsgenie_alert_close_alert` | Close Alert. | POST /v2/alerts/:identifier/close | identifier(required), body(required), identifier_type(optional) |
| alert | `opsgenie_alert_count_alerts` | Count Alerts. | GET /v2/alerts/count | query(optional), search_identifier(optional), search_identifier_type(optional) |
| alert | `opsgenie_alert_create_alert` | Create Alert. | POST /v2/alerts | body(required) |
| alert | `opsgenie_alert_delete_alert` | Delete Alert. | DELETE /v2/alerts/:identifier | identifier(required), identifier_type(optional), user(optional), source(optional) |
| alert | `opsgenie_alert_escalate_alert_to_next` | Escalate Alert to Next. | POST /v2/alerts/:identifier/escalate | identifier(required), body(required), identifier_type(optional) |
| alert | `opsgenie_alert_get_alert` | Get Alert. | GET /v2/alerts/:identifier | identifier(required), identifier_type(optional) |
| alert | `opsgenie_alert_get_request_status` | Get Request Status. | GET /v2/alerts/requests/:requestId | request_id(required) |
| alert | `opsgenie_alert_list_alert_logs` | List Alert Logs. | GET /v2/alerts/:identifier/logs | identifier(required), identifier_type(optional), offset(optional), direction(optional), limit(optional), order(optional) |
| alert | `opsgenie_alert_list_alert_notes` | List Alert Notes. | GET /v2/alerts/:identifier/notes | identifier(required), identifier_type(optional), offset(optional), direction(optional), limit(optional), order(optional) |
| alert | `opsgenie_alert_list_alerts` | List Alerts. | GET /v2/alerts | query(optional), search_identifier(optional), search_identifier_type(optional), offset(optional), limit(optional), sort(optional), order(optional) |
| alert | `opsgenie_alert_remove_tags_from_alert` | Remove Tags from Alert. | DELETE /v2/alerts/:identifier/tags | identifier(required), tags(required), identifier_type(optional), user(optional), source(optional), note(optional) |
| alert | `opsgenie_alert_snooze_alert` | Snooze Alert. | POST /v2/alerts/:identifier/snooze | identifier(required), body(required), identifier_type(optional) |
| alert | `opsgenie_alert_unacknowledge_alert` | Unacknowledge Alert. | POST /v2/alerts/:identifier/unacknowledge | identifier(required), body(required), identifier_type(optional) |
| alert | `opsgenie_alert_update_alert_description` | Update Alert Description. | POST /v2/alerts/:identifier/description | identifier(required), body(required), identifier_type(optional) |
| alert | `opsgenie_alert_update_alert_message` | Update Alert Message. | POST /v2/alerts/:identifier/message | identifier(required), body(required), identifier_type(optional) |
| alert | `opsgenie_alert_update_alert_priority` | Update Alert Priority. | PUT /v2/alerts/:identifier/priority | identifier(required), body(required), identifier_type(optional) |

## 测试示例

```bash
# Health check
curl -s http://localhost:8080/health

# Call a tool via the MCP protocol (streamable HTTP) — requires an
# initialize handshake first per the MCP spec; abbreviated example below
# shows the tool-call request body only:
curl -s -X POST http://localhost:8080/mcp \
  -H "X-Opsgenie-Api-Key: <your-opsgenie-api-key>" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -H "mcp-session-id: <session-id-from-initialize>" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
      "name": "opsgenie_alert_list_alerts",
      "arguments": {"limit": "5"}
    }
  }'
```

**Live-verified** (2026-07-30): `opsgenie_alert_list_alerts` (the same
endpoint MSPbots itself calls) was called end-to-end through this running
server with a real test API key and returned real alert data (message,
status, priority, responders, integration, etc.) from the account. Two
other tools in different categories (`opsgenie_team_list_teams`,
`opsgenie_account_get_account_info`) were also called with the same key and
correctly returned Opsgenie's own `403 API Key is not granted with
configuration access` — confirming the request/auth-header plumbing works
correctly outside the `alert` category too; this specific test key is just
scoped to alert-level access only (a normal Opsgenie integration-key
restriction, not a bug).

## API Reference

- Overview: https://docs.opsgenie.com/docs/api-overview
- Authentication: https://docs.opsgenie.com/docs/authentication
- Per-category docs are linked from the sidebar at https://docs.opsgenie.com/docs/alert-api

## Known Gaps

- **Trimmed from 213 to 22 tools on 2026-08-04.** The original build
  covered the full public API across 28 categories per an earlier scope
  decision. A later scope decision cut this back to MSPbots' actually-used
  category (`alert`) plus its core CRUD — see the Scope section above for
  exactly what was kept/dropped within `alert` and the full list of the 27
  removed categories (~178 tools). If a removed category is needed later,
  the same `docs.opsgenie.com/docs/*-api` pages can be re-parsed the same
  way the kept tools were generated.
- Several kept tools still mutate real Opsgenie alert state
  (`opsgenie_alert_delete_alert`, `opsgenie_alert_close_alert`,
  `opsgenie_alert_create_alert`, etc.) — treat these as
  **irreversible/state-changing** and confirm with a human before invoking.
- **`body` parameters are untyped (`dict`)** rather than fully modeled — each
  tool's docstring lists the field names extracted from Opsgenie's docs, but
  reproducing all of them as typed Python parameters was out of scope for a
  mechanically-generated server.
- **Source data was extracted from prose documentation, not a machine
  spec** — Opsgenie has no downloadable OpenAPI/Postman collection, so every
  operation's method/path/params was parsed from `docs.opsgenie.com`'s HTML.
- Only `opsgenie_alert_list_alerts` (MSPbots' own endpoint) was
  live-verified with real data returned. The remaining 21 tools are
  structurally correct (schema validated, MCP-protocol `tools/list`
  confirmed, all pass `compile()`) but not individually smoke-tested —
  several are write/destructive operations that would create, modify, or
  close real alerts, so they weren't exercised against the live test
  account.
- **Vendor is reaching end-of-support** (see the warning banner at the top
  of this README) — Atlassian recommends migrating to Jira Service
  Management or Compass. This MCP targets the still-live Opsgenie public API
  as of this build.
