[README.md](https://github.com/user-attachments/files/33474439/README.md)
# Synthetic Procure-to-Pay Agent Benchmark (Pilot v0.1)

**400 synthetic scenarios, 420 user turns, 20 scenario families, 15 proposed MCP tools.** A research-oriented dataset for studying how enterprise agents translate employee instructions into tool calls, handle clarification and policy exceptions, and eventually execute procure-to-pay workflows.

> **Status: structurally validated reference plans; NOT execution-validated ground truth.** No real ERP or MCP server has been used to verify business outcomes. Do not claim real-world representativeness or transaction correctness based solely on this dataset.

## Files

- `data/p2p_conversations.csv`: one row per **user turn**. `reference_tool_calls_json`, `conversation_context_json`, `scenario_initial_state_json` and `expected_outcome_json` are JSON strings inside CSV cells.
- `data/p2p_conversations.jsonl`: same records with JSON objects/arrays instead of embedded strings.
- `data/scenario_metadata.jsonl`: scenario family, complexity, number of turns, synthetic provenance.
- `tool_catalog.json`: tool names and required fields (descriptive contracts, not complete JSON Schema).
- `scripts/validate_dataset.py`: validates counts, JSON parsing, known tool names, unique IDs, and `$binding` ordering.

## Example

A request such as "Create a purchase order ... and submit it" has two reference calls:

```json
[
  {"tool":"create_purchase_order","arguments":{"supplier_id":"SUP-001","items":[{"sku":"SKU-101","quantity":10,"unit_price":800}],"currency":"INR","status":"draft"},"result_binding":"po_id"},
  {"tool":"submit_purchase_order","arguments":{"po_id":"$po_id"}}
]
```

`$po_id` denotes the ID returned by an earlier call, not a literal purchase order ID. Optional read-only lookups may be valid even when omitted from the reference. **Compare required actions, arguments, dependencies, forbidden actions, and final ERP state—not byte-for-byte call sequences.**

## Scenario families

20 examples per family: `po_draft`, `po_submit`, `po_requisition`, `po_update`, `po_status`, `po_approve`, `po_unauth`, `po_inactive`, `po_missing`, `po_conflict`, `receipt_full`, `receipt_partial`, `receipt_damage`, `receipt_unapproved`, `receipt_excess`, `invoice_match`, `invoice_quantity`, `invoice_price`, `invoice_duplicate`, `po_then_status`.

`po_missing` has two user turns per conversation: a missing-supplier request requiring clarification, followed by a supplier-providing turn requiring a tool call. Thus 400 conversations produce 420 rows.

## Synthetic business rules (assumptions)

1. Supplier and product must be active to create a PO.
2. PO value above INR 50,000 requires explicit approval; lower values are auto-approved on submission.
3. Draft POs can be edited; approved POs cannot be edited through the provided update tool.
4. Goods receipts require an approved PO; accepted quantities must not exceed outstanding ordered quantities.
5. Invoices require a matching PO and goods receipt; quantity and unit price must match and duplicate supplier invoice numbers are rejected.
6. Only an actor with verified approval authority may approve a PO.
7. Missing or contradictory instructions trigger clarification; unauthorized or prohibited requests are refused.

These policies are illustrative and are not claims about SAP, Oracle, Odoo or other commercial ERPs.

## Generation method and limitations

All 400 scenarios were **generated from 20 parameterized templates with a fixed random seed**. They are synthetic, not sourced from employee logs, and **not 400 statistically independent workflow types**. Scenario parameters vary (SKUs, suppliers, quantities, prices, PO and invoice IDs); language variety remains limited. The initial-state JSON is a minimal scenario fixture, not a complete relational ERP database. Some refusal plans contain read-only diagnostic calls, and clarify plans contain no MCP mutation calls.

The current validator checks structural integrity only. It **does not execute** reference plans or validate that initial state and business semantics fully agree. Before using this as a research benchmark: implement the ERP simulator and MCP schemas; execute and verify every reference plan; independently review semantic alignment; add varied natural-language paraphrases; group train/test splits by scenario family; pilot effect sizes and conduct a power analysis. Do not report `validation_status=structural_validated_unexecuted` as successful ERP execution.

## Run structural checks

```bash
python scripts/validate_dataset.py
```

## Reproducibility and license

Dataset creation used deterministic programmatic templates and a fixed seed (`20261015`), with no external confidential records. **Suggested license:** CC BY 4.0 for the dataset and MIT for scripts; add explicit `LICENSE` files once the repository owner selects licensing. No real organization, supplier or employee data is included.
