# Repository Organization and Submission Guide

## Current organization

```text
capstone_nlp_erp/
├── README.md
├── requirements.txt
├── .gitignore
├── P2P_MCP_Three_Model_Colab_Experiment_95pct_Documented.ipynb
├── tool_catalog.json
├── data/
│   ├── P2P_MCP_4000_Additional_Test_Prompts.csv
│   ├── p2p_conversations.csv
│   ├── p2p_conversations.jsonl
│   └── scenario_metadata.jsonl
├── scripts/
│   └── validate_dataset.py
├── mcp_capstone_outputs/
│   ├── cleaned_dataset.csv
│   ├── split_assignments.csv
│   ├── experiment_metadata.json
│   ├── final_test_scored_long.csv
│   ├── final_test_hypothesis_tests_95pct.csv
│   ├── test_*_predictions.jsonl
│   ├── validation_*
│   └── fig1_...png through fig7_...png
└── docs/
    ├── REPOSITORY_GUIDE.md
    └── pilot/README.md
```

The existing `output` file at repository root appears to be a one-byte stray file. It has **not** been deleted.

## Recommended review order

1. Root README: research questions, methodology and results.
2. Main Colab notebook: experiment and scoring code.
3. Expanded dataset in `data/`.
4. Experiment metadata and split assignments in `mcp_capstone_outputs/`.
5. Held-out scores and performance charts.
6. Historical pilot documentation and validator.

## Checks required before final academic submission

1. **Correct RQ2 hypothesis CSV:** The committed file currently reports Gemma RQ2 as **139/660**, whereas the gold-eligible denominator is **760**. Recompute tests and confidence intervals with the finalized metric.
2. **Fix dataset provenance URL:** `experiment_metadata.json` points to `/master/`, but the repository's default branch is `main`. Update metadata only after verifying the source checksum and intended input.
3. **Notebook alignment:** Verify that the committed notebook contains the same final scorer used to produce the report, including extra-parameter penalties and gold-based eligibility.
4. **Separate pilot and final dataset:** The pilot validator expects 400 conversations and 420 turns. The final experiment uses 4,000 turns and requires its own validation checks.
5. **Environment:** Record actual Python/package versions, model endpoint settings and hardware when available. The supplied requirements file is not a frozen environment.
6. **Secrets:** Audit notebook source, output cells and Git history. Adding `.gitignore` does not erase previously committed credentials.
7. **Reproducibility:** Document whether reruns invoke remote models or reuse stored predictions; actual model inference may incur costs.
8. **Limitations:** Gold plans are synthetic, not independently ERP-execution-validated. RQ3 is conditional; scenario-family labels may span train/test partitions.

## Non-destructive organization

For this submission, preserve all existing data and notebook paths. Moving files into new directories could break hard-coded paths. Reorganize physically only after testing the notebook and updating references. The documentation separates the original pilot from the final study without moving experimental evidence.
