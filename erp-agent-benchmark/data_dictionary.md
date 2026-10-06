# ERP-AgentBench Data Dictionary

| Field | Description |
|---|---|
| request_id | Unique test-instance identifier |
| organization_id | Organization associated with request |
| user_id | Requesting user |
| role | User's organizational role |
| natural_language_request | Original user request |
| expected_intent | Ground-truth ERP operation |
| expected_parameters | Ground-truth entities and parameters |
| capability_id | ERP capability/function |
| policy_id | Applicable policy |
| policy_version | Governing policy version |
| erp_state | Relevant ERP state |
| authorization_status | Whether user is authorized |
| approval_status | Whether approval is required |
| expected_decision | ALLOW, DENY, REQUIRE_APPROVAL, or CLARIFICATION |
| expected_state_transition | Expected resulting state |
| actual_decision | Agent-generated decision |
| actual_action | Agent-generated ERP action |
| execution_status | Execution result |
| error_type | Error category |
