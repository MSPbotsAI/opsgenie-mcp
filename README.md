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

**213 tools** across 28 categories, generated from Opsgenie's official
documentation at `docs.opsgenie.com` (Alert, Incident, Incident Timeline,
Integration, Heartbeat, Alert & Notification Policy, Policy (legacy v1),
Maintenance, Account, User, Custom User Role, Contact, Notification Rule
(+ Step), Team (+ Member/Role/Routing Rule), Schedule (+ Rotation/Override),
Escalation, Who Is On Call, Forwarding Rule, Service (+ Incident Rules/
Templates), Incident Templates).

MSPbots' own stored integration config for this vendor calls exactly **1**
endpoint (`GET /v2/alerts`, read-only). Per explicit user decision, this
build covers the **full public API including write operations** (create/
update/delete/enable/disable across every resource), not just that one
read-only call — see **Known Gaps** for which tools mutate real data.

Source data was extracted by fetching all ~29 `docs.opsgenie.com/docs/*-api`
pages and structuring each documented operation (method, path, path/query
params, JSON body fields) into a machine-readable format, then generating
all 213 tool functions from that structured data — the same
codegen-from-structured-spec approach used for other large-API vendors in
this program (ConnectSecure, Dynu, Jira Data Center), adapted here because
Opsgenie has no downloadable OpenAPI/Postman spec, only prose documentation.

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

| Category | Tool | 功能 | 方法+路径 | 参数 |
|---|---|---|---|---|
| account | `opsgenie_account_get_account_info` | Get Account Info. | GET /v2/account | 无 |
| alert | `opsgenie_alert_acknowledge_alert` | Acknowledge Alert. | POST /v2/alerts/:identifier/acknowledge | identifier(必填), body(必填), identifier_type(可选) |
| alert | `opsgenie_alert_add_details_custom_properties_to_alert` | Add Details (Custom Properties) to Alert. | POST /v2/alerts/:identifier/details | identifier(必填), body(必填), identifier_type(可选) |
| alert | `opsgenie_alert_add_note_to_alert` | Add Note to Alert. | POST /v2/alerts/:identifier/notes | identifier(必填), body(必填), identifier_type(可选) |
| alert | `opsgenie_alert_add_responder_to_alert` | Add Responder to Alert. | POST /v2/alerts/:identifier/responders | identifier(必填), body(必填), identifier_type(可选) |
| alert | `opsgenie_alert_add_tags_to_alert` | Add Tags to Alert. | POST /v2/alerts/:identifier/tags | identifier(必填), body(必填), identifier_type(可选) |
| alert | `opsgenie_alert_add_team_to_alert` | Add Team to Alert. | POST /v2/alerts/:identifier/teams | identifier(必填), body(必填), identifier_type(可选) |
| alert | `opsgenie_alert_assign_alert` | Assign Alert. | POST /v2/alerts/:identifier/assign | identifier(必填), body(必填), identifier_type(可选) |
| alert | `opsgenie_alert_close_alert` | Close Alert. | POST /v2/alerts/:identifier/close | identifier(必填), body(必填), identifier_type(可选) |
| alert | `opsgenie_alert_count_alerts` | Count Alerts. | GET /v2/alerts/count | query(可选), search_identifier(可选), search_identifier_type(可选) |
| alert | `opsgenie_alert_create_a_saved_search` | Create a Saved Search. | POST /v2/alerts/saved-searches | body(必填) |
| alert | `opsgenie_alert_create_alert` | Create Alert. | POST /v2/alerts | body(必填) |
| alert | `opsgenie_alert_create_alert_attachment` | Create Alert Attachment. | POST /v2/alerts/:alertIdentifier/attachments | alert_identifier(必填), body(必填), alert_identifier_type(可选) |
| alert | `opsgenie_alert_delete_alert` | Delete Alert. | DELETE /v2/alerts/:identifier | identifier(必填), identifier_type(可选), user(可选), source(可选) |
| alert | `opsgenie_alert_delete_alert_attachment` | Delete Alert Attachment. | DELETE /v2/alerts/:alertIdentifier/attachments/:attachmentId | alert_identifier(必填), attachment_id(必填), alert_identifier_type(可选), user(可选) |
| alert | `opsgenie_alert_delete_saved_search` | Delete Saved Search. | DELETE /v2/alerts/saved-searches/:identifier | identifier(必填), identifier_type(可选) |
| alert | `opsgenie_alert_escalate_alert_to_next` | Escalate Alert to Next. | POST /v2/alerts/:identifier/escalate | identifier(必填), body(必填), identifier_type(可选) |
| alert | `opsgenie_alert_execute_custom_action` | Execute Custom Action. | POST /v2/alerts/:identifier/actions/:action | identifier(必填), action(必填), body(必填), identifier_type(可选) |
| alert | `opsgenie_alert_get_alert` | Get Alert. | GET /v2/alerts/:identifier | identifier(必填), identifier_type(可选) |
| alert | `opsgenie_alert_get_alert_attachment` | Get Alert Attachment. | GET /v2/alerts/:alertIdentifier/attachments/:attachmentId | alert_identifier(必填), attachment_id(必填), alert_identifier_type(可选) |
| alert | `opsgenie_alert_get_request_status` | Get Request Status. | GET /v2/alerts/requests/:requestId | request_id(必填) |
| alert | `opsgenie_alert_get_saved_search` | Get Saved Search. | GET /v2/alerts/saved-searches/:identifier | identifier(必填), identifier_type(可选) |
| alert | `opsgenie_alert_list_alert_attachments` | List Alert Attachments. | GET /v2/alerts/:alertIdentifier/attachments | alert_identifier(必填), alert_identifier_type(可选) |
| alert | `opsgenie_alert_list_alert_logs` | List Alert Logs. | GET /v2/alerts/:identifier/logs | identifier(必填), identifier_type(可选), offset(可选), direction(可选), limit(可选), order(可选) |
| alert | `opsgenie_alert_list_alert_notes` | List Alert Notes. | GET /v2/alerts/:identifier/notes | identifier(必填), identifier_type(可选), offset(可选), direction(可选), limit(可选), order(可选) |
| alert | `opsgenie_alert_list_alert_recipients` | List Alert Recipients. | GET /v2/alerts/:identifier/recipients | identifier(必填), identifier_type(可选) |
| alert | `opsgenie_alert_list_alerts` | List Alerts. | GET /v2/alerts | query(可选), search_identifier(可选), search_identifier_type(可选), offset(可选), limit(可选), sort(可选), order(可选) |
| alert | `opsgenie_alert_list_saved_searches` | List Saved Searches. | GET /v2/alerts/saved-searches | 无 |
| alert | `opsgenie_alert_remove_details_custom_properties_from_alert` | Remove Details (Custom Properties) from Alert. | DELETE /v2/alerts/:identifier/details | identifier(必填), keys(必填), identifier_type(可选), user(可选), source(可选), note(可选) |
| alert | `opsgenie_alert_remove_tags_from_alert` | Remove Tags from Alert. | DELETE /v2/alerts/:identifier/tags | identifier(必填), tags(必填), identifier_type(可选), user(可选), source(可选), note(可选) |
| alert | `opsgenie_alert_snooze_alert` | Snooze Alert. | POST /v2/alerts/:identifier/snooze | identifier(必填), body(必填), identifier_type(可选) |
| alert | `opsgenie_alert_unacknowledge_alert` | Unacknowledge Alert. | POST /v2/alerts/:identifier/unacknowledge | identifier(必填), body(必填), identifier_type(可选) |
| alert | `opsgenie_alert_update_alert_description` | Update Alert Description. | POST /v2/alerts/:identifier/description | identifier(必填), body(必填), identifier_type(可选) |
| alert | `opsgenie_alert_update_alert_message` | Update Alert Message. | POST /v2/alerts/:identifier/message | identifier(必填), body(必填), identifier_type(可选) |
| alert | `opsgenie_alert_update_alert_priority` | Update Alert Priority. | PUT /v2/alerts/:identifier/priority | identifier(必填), body(必填), identifier_type(可选) |
| alert | `opsgenie_alert_update_saved_search` | Update Saved Search. | PATCH /v2/alerts/saved-searches/:identifier | identifier(必填), body(必填), identifier_type(可选) |
| alert_notification_policy | `opsgenie_alert_notification_policy_change_policy_order` | Change Policy Order. | POST /v2/policies/:identifier/change-order | identifier(必填), body(必填), team_id(可选) |
| alert_notification_policy | `opsgenie_alert_notification_policy_create_policy` | Create Policy. | POST /v2/policies | body(必填), team_id(可选) |
| alert_notification_policy | `opsgenie_alert_notification_policy_delete_policy` | Delete Policy. | DELETE /v2/policies/:identifier | identifier(必填), team_id(可选) |
| alert_notification_policy | `opsgenie_alert_notification_policy_disable_policy` | Disable Policy. | POST /v2/policies/:identifier/disable | identifier(必填), team_id(可选) |
| alert_notification_policy | `opsgenie_alert_notification_policy_enable_policy` | Enable Policy. | POST /v2/policies/:identifier/enable | identifier(必填), team_id(可选) |
| alert_notification_policy | `opsgenie_alert_notification_policy_get_policy` | Get Policy. | GET /v2/policies/:identifier | identifier(必填), team_id(可选) |
| alert_notification_policy | `opsgenie_alert_notification_policy_list_alert_policies` | List Alert Policies. | GET /v2/policies/alert | team_id(可选) |
| alert_notification_policy | `opsgenie_alert_notification_policy_list_notification_policies` | List Notification Policies. | GET /v2/policies/notification | team_id(必填) |
| alert_notification_policy | `opsgenie_alert_notification_policy_update_policy` | Update Policy. | PUT /v2/policies/:identifier | identifier(必填), body(必填), team_id(可选) |
| contact | `opsgenie_contact_create_contact` | Create Contact. | POST /v2/users/:userIdentifier/contacts | user_identifier(必填), body(必填) |
| contact | `opsgenie_contact_delete_contact` | Delete Contact. | DELETE /v2/users/:userIdentifier/contacts/:contactId | user_identifier(必填), contact_id(必填) |
| contact | `opsgenie_contact_disable_contact` | Disable Contact. | POST /v2/users/:userIdentifier/contacts/:contactId/disable | user_identifier(必填), contact_id(必填) |
| contact | `opsgenie_contact_enable_contact` | Enable Contact. | POST /v2/users/:userIdentifier/contacts/:contactId/enable | user_identifier(必填), contact_id(必填) |
| contact | `opsgenie_contact_get_contact` | Get Contact. | GET /v2/users/:userIdentifier/contacts/:contactId | user_identifier(必填), contact_id(必填) |
| contact | `opsgenie_contact_list_contacts` | List Contacts. | GET /v2/users/:userIdentifier/contacts | user_identifier(必填) |
| contact | `opsgenie_contact_update_contact_partial` | Update Contact (Partial). | PATCH /v2/users/:userIdentifier/contacts/:contactId | user_identifier(必填), contact_id(必填), body(必填) |
| custom_user_role | `opsgenie_custom_user_role_create_custom_user_role` | Create Custom User Role. | POST /v2/roles | body(必填) |
| custom_user_role | `opsgenie_custom_user_role_delete_custom_user_role` | Delete Custom User Role. | DELETE /v2/roles/:identifier | identifier(必填), identifier_type(可选) |
| custom_user_role | `opsgenie_custom_user_role_get_custom_user_role` | Get Custom User Role. | GET /v2/roles/:identifier | identifier(必填), identifier_type(可选) |
| custom_user_role | `opsgenie_custom_user_role_list_custom_user_roles` | List Custom User Roles. | GET /v2/roles | 无 |
| custom_user_role | `opsgenie_custom_user_role_update_custom_user_role` | Update Custom User Role. | PUT /v2/roles/:identifier | identifier(必填), body(必填), identifier_type(可选) |
| escalation | `opsgenie_escalation_create_escalation` | Create Escalation. | POST /v2/escalations | body(必填) |
| escalation | `opsgenie_escalation_delete_escalation` | Delete Escalation. | DELETE /v2/escalations/:identifier | identifier(必填), identifier_type(可选) |
| escalation | `opsgenie_escalation_get_escalation` | Get Escalation. | GET /v2/escalations/:identifier | identifier(必填), identifier_type(可选) |
| escalation | `opsgenie_escalation_list_escalations` | List Escalations. | GET /v2/escalations | 无 |
| escalation | `opsgenie_escalation_update_escalation` | Update Escalation. | PATCH /v2/escalations/:identifier | identifier(必填), body(必填), identifier_type(可选) |
| forwarding_rule | `opsgenie_forwarding_rule_create_forwarding_rule` | Create Forwarding Rule. | POST /v2/forwarding-rules | body(必填) |
| forwarding_rule | `opsgenie_forwarding_rule_delete_forwarding_rule` | Delete Forwarding Rule. | DELETE /v2/forwarding-rules/:identifier | identifier(必填), identifier_type(可选) |
| forwarding_rule | `opsgenie_forwarding_rule_get_forwarding_rule` | Get Forwarding Rule. | GET /v2/forwarding-rules/:identifier | identifier(必填), identifier_type(可选) |
| forwarding_rule | `opsgenie_forwarding_rule_list_forwarding_rules` | List Forwarding Rules. | GET /v2/forwarding-rules | 无 |
| forwarding_rule | `opsgenie_forwarding_rule_update_forwarding_rule` | Update Forwarding Rule. | PUT /v2/forwarding-rules/:identifier | identifier(必填), body(必填), identifier_type(可选) |
| heartbeat | `opsgenie_heartbeat_add_heartbeat_request` | Add Heartbeat Request. | POST /v2/heartbeats | body(必填) |
| heartbeat | `opsgenie_heartbeat_delete_heartbeat_request` | Delete Heartbeat Request. | DELETE /v2/heartbeats/:heartbeatName | heartbeat_name(必填) |
| heartbeat | `opsgenie_heartbeat_disable_heartbeat_request` | Disable Heartbeat Request. | POST /v2/heartbeats/:heartbeatName/disable | heartbeat_name(必填) |
| heartbeat | `opsgenie_heartbeat_enable_heartbeat_request` | Enable Heartbeat Request. | POST /v2/heartbeats/:heartbeatName/enable | heartbeat_name(必填) |
| heartbeat | `opsgenie_heartbeat_get_heartbeat_request` | Get Heartbeat Request. | GET /v2/heartbeats/:heartbeatName | heartbeat_name(必填) |
| heartbeat | `opsgenie_heartbeat_list_heartbeats` | List Heartbeats. | GET /v2/heartbeats | 无 |
| heartbeat | `opsgenie_heartbeat_ping_heartbeat_request` | Ping Heartbeat Request. | GET /v2/heartbeats/:heartbeatName/ping | heartbeat_name(必填) |
| heartbeat | `opsgenie_heartbeat_update_heartbeat_request` | Update Heartbeat Request. | PATCH /v2/heartbeats/:heartbeatName | heartbeat_name(必填), body(必填) |
| incident | `opsgenie_incident_add_details_custom_properties_to_incident` | Add Details(Custom Properties) to Incident. | POST /v1/incidents/:identifier/details | identifier(必填), body(必填), identifier_type(可选) |
| incident | `opsgenie_incident_add_note_to_incident` | Add Note to Incident. | POST /v1/incidents/:identifier/notes | identifier(必填), body(必填), identifier_type(可选) |
| incident | `opsgenie_incident_add_responder_to_incident` | Add Responder to Incident. | POST /v1/incidents/:identifier/responders | identifier(必填), body(必填), identifier_type(可选) |
| incident | `opsgenie_incident_add_tags_to_incident` | Add Tags to Incident. | POST /v1/incidents/:identifier/tags | identifier(必填), body(必填), identifier_type(可选) |
| incident | `opsgenie_incident_close_incident` | Close Incident. | POST /v1/incidents/:identifier/close | identifier(必填), body(必填), identifier_type(可选) |
| incident | `opsgenie_incident_create_incident` | Create Incident. | POST /v1/incidents/create | body(必填) |
| incident | `opsgenie_incident_delete_incident` | Delete Incident. | DELETE /v1/incidents/:identifier | identifier(必填), identifier_type(可选) |
| incident | `opsgenie_incident_get_associated_alerts` | Get Associated Alerts. | GET /v1/incidents/:identifier/associated-alert-ids | identifier(必填), identifier_type(可选), offset(可选), direction(可选), limit(可选), order(可选) |
| incident | `opsgenie_incident_get_incident` | Get Incident. | GET /v1/incidents/:identifier | identifier(必填), identifier_type(可选) |
| incident | `opsgenie_incident_get_request_status` | Get Request Status. | GET /v1/incidents/requests/:requestId | request_id(必填) |
| incident | `opsgenie_incident_get_responder_alerts` | Get Responder Alerts. | GET /v1/incidents/:identifier/responder-alert-ids | identifier(必填), identifier_type(可选), offset(可选), direction(可选), limit(可选), order(可选) |
| incident | `opsgenie_incident_list_incident_logs` | List Incident Logs. | GET /v1/incidents/:identifier/logs | identifier(必填), identifier_type(可选), offset(可选), direction(可选), limit(可选), order(可选) |
| incident | `opsgenie_incident_list_incident_notes` | List Incident Notes. | GET /v1/incidents/:identifier/notes | identifier(必填), identifier_type(可选), offset(可选), direction(可选), limit(可选), order(可选) |
| incident | `opsgenie_incident_list_incidents` | List Incidents. | GET /v1/incidents | query(可选), offset(可选), limit(可选), sort(可选), order(可选) |
| incident | `opsgenie_incident_remove_details_custom_properties_from_incident` | Remove Details(Custom Properties) from Incident. | DELETE /v1/incidents/:identifier/details | identifier(必填), keys(必填), identifier_type(可选), note(可选) |
| incident | `opsgenie_incident_remove_tags_from_incident` | Remove Tags from Incident. | DELETE /v1/incidents/:identifier/tags | identifier(必填), tags(必填), identifier_type(可选), note(可选) |
| incident | `opsgenie_incident_reopen_incident` | Reopen Incident. | POST /v1/incidents/:identifier/reopen | identifier(必填), body(必填), identifier_type(可选) |
| incident | `opsgenie_incident_resolve_incident` | Resolve Incident. | POST /v1/incidents/:identifier/resolve | identifier(必填), body(必填), identifier_type(可选) |
| incident | `opsgenie_incident_update_incident_description` | Update Incident Description. | POST /v1/incidents/:identifier/description | identifier(必填), body(必填), identifier_type(可选) |
| incident | `opsgenie_incident_update_incident_message` | Update Incident Message. | POST /v1/incidents/:identifier/message | identifier(必填), body(必填), identifier_type(可选) |
| incident | `opsgenie_incident_update_incident_priority` | Update Incident Priority. | POST /v1/incidents/:identifier/priority | identifier(必填), body(必填), identifier_type(可选) |
| incident_template | `opsgenie_incident_template_create_incident_template` | Create Incident Template. | POST /v1/incident-templates | body(必填) |
| incident_template | `opsgenie_incident_template_delete_incident_template` | Delete Incident Template. | DELETE /v1/incident-templates/:incidentTemplateId | incident_template_id(必填) |
| incident_template | `opsgenie_incident_template_get_incident_templates` | Get Incident Templates. | GET /v1/incident-templates | 无 |
| incident_template | `opsgenie_incident_template_update_incident_template` | Update Incident Template. | PUT /v1/incident-templates/:incidentTemplateId | incident_template_id(必填), body(必填) |
| incident_timeline | `opsgenie_incident_timeline_add_incident_timeline_entry` | Add Incident Timeline Entry. | POST /v2/incident-timelines/:incidentId/entries | incident_id(必填), body(必填) |
| incident_timeline | `opsgenie_incident_timeline_delete_incident_timeline_entry` | Delete Incident Timeline Entry. | DELETE /v2/incident-timelines/:incidentId/entries/:timelineEntryId | incident_id(必填), timeline_entry_id(必填) |
| incident_timeline | `opsgenie_incident_timeline_get_incident_timeline_entry` | Get Incident Timeline Entry. | GET /v2/incident-timelines/:incidentId/entries/:timelineEntryId | incident_id(必填), timeline_entry_id(必填), content_type(可选) |
| incident_timeline | `opsgenie_incident_timeline_hide_incident_timeline_entry` | Hide Incident Timeline Entry. | PATCH /v2/incident-timelines/:incidentId/entries/:timelineEntryId/hide | incident_id(必填), timeline_entry_id(必填) |
| incident_timeline | `opsgenie_incident_timeline_list_incident_timeline_entries` | List Incident Timeline Entries. | GET /v2/incident-timelines/:incidentId/entries | incident_id(必填), group(可选), discard_hidden(可选), offset(可选), order(可选), limit(可选), content_type(可选) |
| incident_timeline | `opsgenie_incident_timeline_unhide_incident_timeline_entry` | Unhide Incident Timeline Entry. | PATCH /v2/incident-timelines/:incidentId/entries/:timelineEntryId/unhide | incident_id(必填), timeline_entry_id(必填) |
| incident_timeline | `opsgenie_incident_timeline_update_incident_timeline_entry` | Update Incident Timeline Entry. | PUT /v2/incident-timelines/:incidentId/entries/:timelineEntryId | incident_id(必填), timeline_entry_id(必填), body(必填) |
| integration | `opsgenie_integration_authenticate_integration` | Authenticate Integration. | POST /v2/integrations/authenticate | body(必填) |
| integration | `opsgenie_integration_create_a_new_integration_action` | Create a New Integration Action. | POST /v2/integrations/:integrationId/actions | integration_id(必填), body(必填) |
| integration | `opsgenie_integration_create_api_based_integration` | Create API Based Integration. | POST /v2/integrations | body(必填) |
| integration | `opsgenie_integration_delete_integration` | Delete Integration. | DELETE /v2/integrations/:integrationId | integration_id(必填) |
| integration | `opsgenie_integration_disable_integration` | Disable Integration. | POST /v2/integrations/:integrationId/disable | integration_id(必填) |
| integration | `opsgenie_integration_enable_integration` | Enable Integration. | POST /v2/integrations/:integrationId/enable | integration_id(必填) |
| integration | `opsgenie_integration_get_integration` | Get Integration. | GET /v2/integrations/:integrationId | integration_id(必填) |
| integration | `opsgenie_integration_get_integration_actions` | Get Integration Actions. | GET /v2/integrations/:integrationId/actions | integration_id(必填) |
| integration | `opsgenie_integration_list_integrations` | List Integrations. | GET /v2/integrations | type(可选), team_id(可选), team_name(可选) |
| integration | `opsgenie_integration_update_all_integration_actions` | Update All Integration Actions. | PUT /v2/integrations/:integrationId/actions | integration_id(必填), body(必填) |
| integration | `opsgenie_integration_update_integration` | Update Integration. | PUT /v2/integrations/:integrationId | integration_id(必填), body(必填) |
| maintenance | `opsgenie_maintenance_cancel_maintenance` | Cancel Maintenance. | POST /v1/maintenance/:maintenanceId/cancel | maintenance_id(必填) |
| maintenance | `opsgenie_maintenance_change_maintenance_end_date` | Change Maintenance End Date. | POST /v1/maintenance/:maintenanceId/change-end-date | maintenance_id(必填), body(必填) |
| maintenance | `opsgenie_maintenance_create_maintenance` | Create Maintenance. | POST /v1/maintenance | body(必填) |
| maintenance | `opsgenie_maintenance_delete_maintenance` | Delete Maintenance. | DELETE /v1/maintenance/:maintenanceId | maintenance_id(必填) |
| maintenance | `opsgenie_maintenance_get_maintenance` | Get Maintenance. | GET /v1/maintenance/:maintenanceId | maintenance_id(必填) |
| maintenance | `opsgenie_maintenance_list_maintenance` | List Maintenance. | GET /v1/maintenance | type(可选) |
| maintenance | `opsgenie_maintenance_update_maintenance` | Update Maintenance. | PUT /v1/maintenance/:maintenanceId | maintenance_id(必填), body(必填) |
| notification_rule | `opsgenie_notification_rule_copy_notification_rules_to_other_users` | Copy Notification Rules to Other Users. | PATCH /v2/users/:userIdentifier/notification-rules/copy-to | user_identifier(必填), body(必填) |
| notification_rule | `opsgenie_notification_rule_create_notification_rule` | Create Notification Rule. | POST /v2/users/:userIdentifier/notification-rules | user_identifier(必填), body(必填) |
| notification_rule | `opsgenie_notification_rule_delete_notification_rule` | Delete Notification Rule. | DELETE /v2/users/:userIdentifier/notification-rules/:ruleId | user_identifier(必填), rule_id(必填) |
| notification_rule | `opsgenie_notification_rule_disable_notification_rule` | Disable Notification Rule. | POST /v2/users/:userIdentifier/notification-rules/:ruleId/disable | user_identifier(必填), rule_id(必填) |
| notification_rule | `opsgenie_notification_rule_enable_notification_rule` | Enable Notification Rule. | POST /v2/users/:userIdentifier/notification-rules/:ruleId/enable | user_identifier(必填), rule_id(必填) |
| notification_rule | `opsgenie_notification_rule_get_notification_rule` | Get Notification Rule. | GET /v2/users/:userIdentifier/notification-rules/:ruleId | user_identifier(必填), rule_id(必填) |
| notification_rule | `opsgenie_notification_rule_list_notification_rule` | List Notification Rule. | GET /v2/users/:userIdentifier/notification-rules | user_identifier(必填) |
| notification_rule | `opsgenie_notification_rule_update_notification_rule_partial` | Update Notification Rule (Partial). | PATCH /v2/users/:userIdentifier/notification-rules/:ruleId | user_identifier(必填), rule_id(必填), body(必填) |
| notification_rule_step | `opsgenie_notification_rule_step_create_notification_rule_step` | Create Notification Rule Step. | POST /v2/users/:userIdentifier/notification-rules/:ruleId/steps | user_identifier(必填), rule_id(必填), body(必填) |
| notification_rule_step | `opsgenie_notification_rule_step_delete_notification_rule_step` | Delete Notification Rule Step. | DELETE /v2/users/:userIdentifier/notification-rules/:ruleId/steps/:stepId | user_identifier(必填), rule_id(必填), step_id(必填) |
| notification_rule_step | `opsgenie_notification_rule_step_disable_notification_rule_step` | Disable Notification Rule Step. | POST /v2/users/:userIdentifier/notification-rules/:ruleId/steps/:stepId/disable | user_identifier(必填), rule_id(必填), step_id(必填) |
| notification_rule_step | `opsgenie_notification_rule_step_enable_notification_rule_step` | Enable Notification Rule Step. | POST /v2/users/:userIdentifier/notification-rules/:ruleId/steps/:stepId/enable | user_identifier(必填), rule_id(必填), step_id(必填) |
| notification_rule_step | `opsgenie_notification_rule_step_get_notification_rule_step` | Get Notification Rule Step. | GET /v2/users/:userIdentifier/notification-rules/:ruleId/steps/:stepId | user_identifier(必填), rule_id(必填), step_id(必填) |
| notification_rule_step | `opsgenie_notification_rule_step_list_notification_rule_steps` | List Notification Rule Steps. | GET /v2/users/:userIdentifier/notification-rules/:ruleId/steps | user_identifier(必填), rule_id(必填) |
| notification_rule_step | `opsgenie_notification_rule_step_update_notification_rule_step_partial` | Update Notification Rule Step (Partial). | PATCH /v2/users/:userIdentifier/notification-rules/:ruleId/steps/:stepId | user_identifier(必填), rule_id(必填), step_id(必填), body(必填) |
| policy | `opsgenie_policy_change_policy_order` | Change Policy Order. | POST /v1/policies/:identifier/change-order | identifier(必填), body(必填) |
| policy | `opsgenie_policy_create_policy` | Create Policy. | POST /v1/policies | body(必填) |
| policy | `opsgenie_policy_delete_policy` | Delete Policy. | DELETE /v1/policies/:identifier | identifier(必填) |
| policy | `opsgenie_policy_disable_policy` | Disable Policy. | POST /v1/policies/:identifier/disable | identifier(必填) |
| policy | `opsgenie_policy_enable_policy` | Enable Policy. | POST /v1/policies/:identifier/enable | identifier(必填) |
| policy | `opsgenie_policy_get_policy` | Get Policy. | GET /v1/policies/:identifier | identifier(必填) |
| policy | `opsgenie_policy_list_policies` | List Policies. | GET /v1/policies | 无 |
| policy | `opsgenie_policy_update_policy` | Update Policy. | PUT /v1/policies/:identifier | identifier(必填), body(必填) |
| schedule | `opsgenie_schedule_create_schedule` | Create Schedule. | POST /v2/schedules | body(必填) |
| schedule | `opsgenie_schedule_delete_schedule` | Delete Schedule. | DELETE /v2/schedules/:identifier | identifier(必填), identifier_type(可选) |
| schedule | `opsgenie_schedule_export_schedule` | Export Schedule. | GET /v2/schedules/:identifier.ics | identifier(必填), identifier_type(可选) |
| schedule | `opsgenie_schedule_get_schedule` | Get Schedule. | GET /v2/schedules/:identifier | identifier(必填), identifier_type(可选) |
| schedule | `opsgenie_schedule_get_schedule_timeline` | Get Schedule Timeline. | GET /v2/schedules/:identifier/timeline | identifier(必填), identifier_type(可选), expand(可选), interval(可选), interval_unit(可选), date(可选) |
| schedule | `opsgenie_schedule_list_schedules` | List Schedules. | GET /v2/schedules | expand(可选) |
| schedule | `opsgenie_schedule_update_schedule_partial` | Update Schedule (Partial). | PATCH /v2/schedules/:identifier | identifier(必填), body(必填), identifier_type(可选) |
| schedule_override | `opsgenie_schedule_override_create_schedule_override` | Create Schedule Override. | POST /v2/schedules/:scheduleIdentifier/overrides | schedule_identifier(必填), body(必填), schedule_identifier_type(可选) |
| schedule_override | `opsgenie_schedule_override_delete_schedule_override` | Delete Schedule Override. | DELETE /v2/schedules/:scheduleIdentifier/overrides/:alias | schedule_identifier(必填), alias(必填), schedule_identifier_type(可选) |
| schedule_override | `opsgenie_schedule_override_get_schedule_override` | Get Schedule Override. | GET /v2/schedules/:scheduleIdentifier/overrides/:alias | schedule_identifier(必填), alias(必填), schedule_identifier_type(可选) |
| schedule_override | `opsgenie_schedule_override_list_schedule_overrides` | List Schedule Overrides. | GET /v2/schedules/:scheduleIdentifier/overrides | schedule_identifier(必填), schedule_identifier_type(可选) |
| schedule_override | `opsgenie_schedule_override_update_schedule_override` | Update Schedule Override. | PUT /v2/schedules/:scheduleIdentifier/overrides/:alias | schedule_identifier(必填), alias(必填), body(必填), schedule_identifier_type(可选) |
| schedule_rotation | `opsgenie_schedule_rotation_create_rotation` | Create Rotation. | POST /v2/schedules/:scheduleIdentifier/rotations | schedule_identifier(必填), body(必填), schedule_identifier_type(可选) |
| schedule_rotation | `opsgenie_schedule_rotation_delete_rotation` | Delete Rotation. | DELETE /v2/schedules/:scheduleIdentifier/rotations/:id | schedule_identifier(必填), id(必填), schedule_identifier_type(可选) |
| schedule_rotation | `opsgenie_schedule_rotation_get_rotation` | Get Rotation. | GET /v2/schedules/:scheduleIdentifier/rotations/:id | schedule_identifier(必填), id(必填), schedule_identifier_type(可选) |
| schedule_rotation | `opsgenie_schedule_rotation_list_rotations` | List Rotations. | GET /v2/schedules/:scheduleIdentifier/rotations | schedule_identifier(必填), schedule_identifier_type(可选) |
| schedule_rotation | `opsgenie_schedule_rotation_update_rotation` | Update Rotation. | PATCH /v2/schedules/:scheduleIdentifier/rotations/:id | schedule_identifier(必填), id(必填), body(必填), schedule_identifier_type(可选) |
| service | `opsgenie_service_create_service` | Create Service. | POST /v1/services | body(必填) |
| service | `opsgenie_service_delete_service` | Delete Service. | DELETE /v1/services/:id | id(必填) |
| service | `opsgenie_service_get_service` | Get Service. | GET /v1/services/:id | id(必填) |
| service | `opsgenie_service_list_services` | List Services. | GET /v1/services/ | query(可选), limit(可选), sort(可选), order(可选), offset(可选) |
| service | `opsgenie_service_update_service` | Update Service. | PATCH /v1/services/:id | id(必填), body(必填) |
| service_incident_rule | `opsgenie_service_incident_rule_create_incident_rule` | Create Incident Rule. | POST /v1/services/:serviceId/incident-rules | service_id(必填), body(必填) |
| service_incident_rule | `opsgenie_service_incident_rule_delete_incident_rule` | Delete Incident Rule. | DELETE /v1/services/:serviceId/incident-rules/:incidentRuleId | service_id(必填), incident_rule_id(必填) |
| service_incident_rule | `opsgenie_service_incident_rule_get_incident_rules` | Get Incident Rules. | GET /v1/services/:serviceId/incident-rules | service_id(必填) |
| service_incident_rule | `opsgenie_service_incident_rule_update_incident_rule` | Update Incident Rule. | PUT /v1/services/:serviceId/incident-rules/:incidentRuleId | service_id(必填), incident_rule_id(必填), body(必填) |
| service_incident_template | `opsgenie_service_incident_template_create_incident_template` | Create Incident Template. | POST /v1/services/:serviceId/incident-templates | service_id(必填), body(必填) |
| service_incident_template | `opsgenie_service_incident_template_delete_incident_template` | Delete Incident Template. | DELETE /v1/services/:serviceId/incident-templates/:incidentTemplateId | service_id(必填), incident_template_id(必填) |
| service_incident_template | `opsgenie_service_incident_template_get_incident_templates` | Get Incident Templates. | GET /v1/services/:serviceId/incident-templates | service_id(必填) |
| service_incident_template | `opsgenie_service_incident_template_update_incident_template` | Update Incident Template. | PUT /v1/services/:serviceId/incident-templates/:incidentTemplateId | service_id(必填), incident_template_id(必填), body(必填) |
| team | `opsgenie_team_create_team` | Create Team. | POST /v2/teams | body(必填) |
| team | `opsgenie_team_delete_team` | Delete Team. | DELETE /v2/teams/:identifier | identifier(必填), identifier_type(可选) |
| team | `opsgenie_team_get_team` | Get Team. | GET /v2/teams/:identifier | identifier(必填), identifier_type(可选) |
| team | `opsgenie_team_list_team_logs` | List Team Logs. | GET /v2/teams/:identifier/logs | identifier(必填), identifier_type(可选), limit(可选), order(可选), offset(可选) |
| team | `opsgenie_team_list_teams` | List Teams. | GET /v2/teams | 无 |
| team | `opsgenie_team_update_team_partial` | Update Team (Partial). | PATCH /v2/teams/:teamId | team_id(必填), body(必填) |
| team_member | `opsgenie_team_member_add_team_member` | Add Team Member. | POST /v2/teams/:teamIdentifier/members | team_identifier(必填), body(必填), team_identifier_type(可选) |
| team_member | `opsgenie_team_member_remove_team_member` | Remove Team Member. | DELETE /v2/teams/:teamIdentifier/members/:memberIdentifier | team_identifier(必填), member_identifier(必填), team_identifier_type(可选) |
| team_role | `opsgenie_team_role_create_team_role` | Create Team Role. | POST /v2/teams/:teamIdentifier/roles | team_identifier(必填), body(必填), team_identifier_type(可选) |
| team_role | `opsgenie_team_role_delete_team_role` | Delete Team Role. | DELETE /v2/teams/:teamIdentifier/roles/:identifier | team_identifier(必填), identifier(必填), team_identifier_type(可选), identifier_type(可选) |
| team_role | `opsgenie_team_role_get_team_role` | Get Team Role. | GET /v2/teams/:teamIdentifier/roles/:identifier | team_identifier(必填), identifier(必填), team_identifier_type(可选), identifier_type(可选) |
| team_role | `opsgenie_team_role_list_team_roles` | List Team Roles. | GET /v2/teams/:teamIdentifier/roles | team_identifier(必填), team_identifier_type(可选) |
| team_role | `opsgenie_team_role_update_team_role_partial` | Update Team Role (Partial). | PATCH /v2/teams/:teamIdentifier/roles/:identifier | team_identifier(必填), identifier(必填), body(必填), team_identifier_type(可选), identifier_type(可选) |
| team_routing_rule | `opsgenie_team_routing_rule_change_team_routing_rule_order` | Change Team Routing Rule Order. | POST /v2/teams/:teamIdentifier/routing-rules/:id/change-order | team_identifier(必填), id(必填), body(必填), team_identifier_type(可选) |
| team_routing_rule | `opsgenie_team_routing_rule_create_team_routing_rule` | Create Team Routing Rule. | POST /v2/teams/:teamIdentifier/routing-rules | team_identifier(必填), body(必填), team_identifier_type(可选) |
| team_routing_rule | `opsgenie_team_routing_rule_delete_team_routing_rule` | Delete Team Routing Rule. | DELETE /v2/teams/:teamIdentifier/routing-rules/:id | team_identifier(必填), id(必填), team_identifier_type(可选) |
| team_routing_rule | `opsgenie_team_routing_rule_get_team_routing_rule` | Get Team Routing Rule. | GET /v2/teams/:teamIdentifier/routing-rules/:id | team_identifier(必填), id(必填), team_identifier_type(可选) |
| team_routing_rule | `opsgenie_team_routing_rule_list_team_routing_rules` | List Team Routing Rules. | GET /v2/teams/:teamIdentifier/routing-rules | team_identifier(必填), team_identifier_type(可选) |
| team_routing_rule | `opsgenie_team_routing_rule_update_team_routing_rule_partial` | Update Team Routing Rule (Partial). | PATCH /v2/teams/:teamIdentifier/routing-rules/:id | team_identifier(必填), id(必填), body(必填), team_identifier_type(可选) |
| user | `opsgenie_user_create_user` | Create User. | POST /v2/users | body(必填) |
| user | `opsgenie_user_delete_saved_search` | Delete Saved Search. | DELETE /v1/incidents/saved-searches/:identifier | identifier(必填), identifier_type(可选) |
| user | `opsgenie_user_delete_user` | Delete User. | DELETE /v2/users/:identifier | identifier(必填) |
| user | `opsgenie_user_get_saved_search` | Get Saved Search. | GET /v2/users/saved-searches/:identifier | identifier(必填), identifier_type(可选) |
| user | `opsgenie_user_get_user` | Get User. | GET /v2/users/:identifier | identifier(必填), expand(可选) |
| user | `opsgenie_user_list_saved_searches` | List Saved Searches. | GET /v2/users/saved-searches | 无 |
| user | `opsgenie_user_list_user` | List User. | GET /v2/users | limit(可选), offset(可选), sort(可选), order(可选), query(可选) |
| user | `opsgenie_user_list_user_escalations` | List User Escalations. | GET /v2/users/:identifier/escalations | identifier(必填) |
| user | `opsgenie_user_list_user_forwarding_rules` | List User Forwarding Rules. | GET /v2/users/:identifier/forwarding-rules | identifier(必填) |
| user | `opsgenie_user_list_user_schedules` | List User Schedules. | GET /v2/users/:identifier/schedules | identifier(必填) |
| user | `opsgenie_user_list_user_teams` | List User Teams. | GET /v2/users/:identifier/teams | identifier(必填) |
| user | `opsgenie_user_update_user_partial` | Update User (Partial). | PATCH /v2/users/:identifier | identifier(必填), body(必填) |
| who_is_on_call | `opsgenie_who_is_on_call_export_on_call_user` | Export On-Call User. | GET /v2/schedules/on-calls/:identifier.ics | identifier(必填) |
| who_is_on_call | `opsgenie_who_is_on_call_get_next_on_calls` | Get Next On Calls. | GET /v2/schedules/:scheduleIdentifier/next-on-calls | schedule_identifier(必填), schedule_identifier_type(可选), flat(可选), date(可选) |
| who_is_on_call | `opsgenie_who_is_on_call_get_on_calls` | Get On Calls. | GET /v2/schedules/:scheduleIdentifier/on-calls | schedule_identifier(必填), schedule_identifier_type(可选), flat(可选), date(可选) |
| who_is_on_call | `opsgenie_who_is_on_call_list_on_calls` | List On Calls. | GET /v2/schedules/on-calls | flat(可选), date(可选) |

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

- **Full API coverage was an explicit user decision**, matching the pattern
  used for other large public APIs in this program (ConnectSecure, Cove
  Data Protection, Dynu, Jira Data Center). MSPbots itself only calls 1
  endpoint (`GET /v2/alerts`); everything else — including destructive
  operations like `opsgenie_team_delete_team`,
  `opsgenie_schedule_delete_schedule`, `opsgenie_integration_delete_integration`,
  `opsgenie_user_delete_user`, and any `close`/`delete`/`disable` tool —
  mutates real Opsgenie configuration or alert/incident state. Treat these
  as **destructive/irreversible** and confirm with a human before invoking.
- **`body` parameters are untyped (`dict`)** rather than fully modeled — each
  tool's docstring lists the field names extracted from Opsgenie's docs, but
  reproducing all of them as typed Python parameters was out of scope for a
  213-tool generation across 28 categories.
- **Source data was extracted from prose documentation, not a machine
  spec** — Opsgenie has no downloadable OpenAPI/Postman collection, so every
  operation's method/path/params was parsed from `docs.opsgenie.com`'s HTML
  by multiple independent research passes (cross-checked against the actual
  page text, not summarized). A few pages intermittently served a Cloudflare
  bot-check to browser-based fetches; those categories were extracted via
  the plain HTTP fetch path instead.
- Only `opsgenie_alert_list_alerts` (MSPbots' own endpoint) was live-verified
  with real data returned; `opsgenie_team_list_teams` and
  `opsgenie_account_get_account_info` were verified to reach the real API
  and return a correctly-parsed error (the test key's permission scope, not
  a code issue). The remaining 210 tools are structurally correct (schema
  validated, MCP-protocol `tools/list` confirmed, all 213 pass `compile()`)
  but not individually smoke-tested — most are write/destructive operations
  that would create, modify, or delete real teams, schedules, escalations,
  integrations, or alerts, so they weren't exercised against the live test
  account.
- **Vendor is reaching end-of-support** (see the warning banner at the top
  of this README) — Atlassian recommends migrating to Jira Service
  Management or Compass. This MCP targets the still-live Opsgenie public API
  as of this build.
