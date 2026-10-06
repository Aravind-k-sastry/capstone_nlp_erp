# Agent-First ERP — Data Access Package

This package provides data-access documentation, representative samples, schemas,
a data dictionary, and reproducibility instructions for the Agent-First ERP NLP research.

Complete external datasets are intentionally NOT included. Obtain them from their
official sources and follow the instructions in `DATA_ACCESS.md`.

## Included
- `DATA_ACCESS.md` — consolidated access instructions
- `data/external/` — official-source notes and representative samples
- `data/erp-agent-benchmark/` — ERP-specific schemas, samples, dictionary, and generator

## Reproduce the ERP benchmark

```bash
python data/erp-agent-benchmark/generator/generate_dataset.py
```
