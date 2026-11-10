# Historical Pilot Dataset — v0.1

This documents the **original pilot**, distinct from the 4,000-turn final experiment.

- **400 synthetic conversations and 420 user turns**
- **20 parameterized scenario families**
- **15 descriptive MCP tool contracts**
- Generation seed: **20261015**
- Structurally validated reference plans; **not execution-validated against an ERP**

## Original pilot files (kept in their existing locations)

- [CSV](../../data/p2p_conversations.csv)
- [JSONL](../../data/p2p_conversations.jsonl)
- [Scenario metadata](../../data/scenario_metadata.jsonl)
- [Tool catalog](../../tool_catalog.json)
- [Structural validator](../../scripts/validate_dataset.py)

From the repository root, run `python scripts/validate_dataset.py`. This checks JSON structure, unique IDs, behavior labels, tool names and prior result bindings; it asserts **400 conversations and 420 turns**, so **do not use it unchanged for the final 4,000-turn experiment**. It does not execute tool calls or verify business-state transitions.

The pilot uses illustrative synthetic purchasing policies, not validated rules for any particular commercial ERP. For the completed four-system benchmark, see the [main README](../../README.md).
