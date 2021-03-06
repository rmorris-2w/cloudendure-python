# CloudEndureAuditLogEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | username (typically an email) of user who initiated action (in UI or via API) which resulted in this audit log entry being added.  | [optional]
**event_name** | **str** | Unique event name.  One of:  - replicationConfigurationChanged  - blueprintChanged  - ... @todo: complete  | [optional]
**participating_machines** | **list[object]** | List of machine-identifiers objects.  Only present if Audit Log entry relates to one or more machines.  | [optional]
**description** | **str** | Long-form human-readable description of Audit Log entry. | [optional]
**changed_fields** | [**list[CloudEndureAuditLogChangedField]**](CloudEndureAuditLogChangedField.md) | Map of fields that have been changed and their old an new values. Only present when eventName is replicationConfigurationChanged or blueprintChanged  | [optional]
**timestamp** | **datetime** | RFC 3339 compliant date-time string of when Audit Log entry was created/ event described by audit log entry happened.  | [optional]
**job_id** | **str** | ID of Job due to which this log entry was created (only included if log entry is result of a Job) | [optional]

[[Back to Model list]](API_README.md#documentation-for-models) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to README]](API_README.md)

