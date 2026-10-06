# Data Access

This repository provides working source URLs, access instructions, representative
sample records, schemas, and reproducibility information.

## External datasets

### API-Bank
Purpose: API/tool-use benchmark.

Official source:
https://github.com/AlibabaResearch/DAMO-ConvAI/tree/main/api-bank

Instructions:
1. Visit the official repository.
2. Follow its current dataset acquisition/preparation instructions.
3. Place the locally obtained data under `data/external/API-Bank/`.
4. Do not redistribute it unless its current license permits redistribution.

Representative structure: `data/external/API-Bank/sample.json`

### ToolBench / ToolLLM
Purpose: large-scale tool/API-use benchmark.

Official source:
https://github.com/OpenBMB/ToolBench

Instructions:
1. Visit the official repository.
2. Follow its current dataset preparation instructions.
3. Place the locally obtained data under `data/external/ToolBench/`.
4. Follow the dataset's license and terms.

Representative structure: `data/external/ToolBench/sample.json`

### Berkeley Function Calling Leaderboard (BFCL)
Purpose: function-calling and agentic/stateful tool-use evaluation.

Official source:
https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard

Instructions:
1. Visit the official repository.
2. Follow its current installation and dataset preparation instructions.
3. Place the locally obtained data under `data/external/BFCL/`.
4. Follow the current license and terms.

Representative structure: `data/external/BFCL/sample.json`

## Original ERP-AgentBench

ERP-AgentBench is the research-specific benchmark proposed for this project.
It evaluates natural-language ERP interaction under user context, organizational
policy, authorization, ERP state, approval, and multi-step execution constraints.

The repository contains:
- schemas
- representative records
- data dictionary
- reproducible generator

Generate the experimental dataset locally with:

```bash
python data/erp-agent-benchmark/generator/generate_dataset.py
```

The complete external datasets are not redistributed in this repository.
