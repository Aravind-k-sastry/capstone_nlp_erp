# ERP-Agnostic MCP Tool-Call Planning: Procure-to-Pay Capstone

**Research repository | Synthetic benchmark | Offline tool-call evaluation (not live ERP execution)**

This capstone evaluates whether pretrained open-weight language models can translate natural-language procure-to-pay (P2P) requests into ERP-agnostic Model Context Protocol (MCP) tool-call plans. It compares three LLMs with an executed deterministic heuristic baseline. The commercial motivation is cost-sensitive ERP automation for small and medium-sized manufacturers; inference costs and willingness to pay were not measured.

## Research questions

- **RQ1 — Routing:** Correct MCP tool-call plan and execute/refuse/clarify behavior.
- **RQ2 — Parameter identification:** All gold-required parameter paths present, with no unsupported extra paths. Use **760 gold-eligible held-out turns per system**; malformed predictions are failures.
- **RQ3 — Value correctness:** All predicted, gold-aligned parameter values correct. This metric is **conditional on prediction**, not end-to-end transaction success.
- **Exploratory baseline comparison:** Compare deterministic rules with LLMs on the same held-out turns.

The synthetic gold-reference JSON is assumed correct. Independent semantic grounding and live ERP execution validation are outside the scope of this study. The 95% target is an evaluation threshold, not a production guarantee.

## Dataset and experiment

**4,000 synthetic user turns** were partitioned by conversation into **2,320 training**, **840 validation**, and **840 held-out test** turns (random seed **42**). The same held-out turns were evaluated by all four systems. Scenario-family labels overlap across splits, limiting claims about unseen-family generalization.

- [Expanded input dataset](data/P2P_MCP_4000_Additional_Test_Prompts.csv)
- [Processed dataset](mcp_capstone_outputs/cleaned_dataset.csv)
- [Split assignments](mcp_capstone_outputs/split_assignments.csv)
- [Experiment metadata](mcp_capstone_outputs/experiment_metadata.json)
- [Historical 400-conversation / 420-turn pilot](docs/pilot/README.md)

## Evaluated systems

| System | Identifier or method |
|---|---|
| Llama 3.3 70B | `meta-llama/Llama-3.3-70B-Instruct` |
| Gemma 4 26B A4B | `google/gemma-4-26B-A4B-it` |
| GPT-OSS 120B | `openai/gpt-oss-120b` |
| Heuristic baseline | Deterministic keyword / rule-based extraction |

These open-weight model families were chosen from established developers to investigate provider-controlled deployment options. The experiment does not establish that self-hosting is cheaper than proprietary APIs. The metadata records an OpenAI-compatible inference interface, not proof of self-hosted inference.

## Held-out results

| System | RQ1 (n=840) | RQ2 (n=760) | RQ3 (conditional) |
|---|---:|---:|---:|
| Llama | 223/840 (26.55%) | 120/760 (15.79%) | 187/720 (25.97%) |
| Gemma | 278/840 (33.10%) | 139/760 (18.29%) | 480/621 (77.29%) |
| GPT-OSS | 223/840 (26.55%) | 123/760 (16.18%) | 298/614 (48.53%) |
| Heuristic baseline | 533/840 (63.45%) | 520/760 (68.42%) | 720/720 (100.00%) |

The heuristic baseline leads on observed RQ1 and RQ2. Its perfect **conditional** RQ3 score does not imply complete arguments or successful ERP transactions.

**Scoring reconciliation required:** The committed `mcp_capstone_outputs/final_test_hypothesis_tests_95pct.csv` currently uses **660** as Gemma's RQ2 denominator (139/660), while the gold-based scoring uses **760** (139/760). This README reports the gold-based metric. Regenerate the hypothesis-test CSV with `gold_eligible` and `gb_all_required_present` before citing it as the final statistical result.

## Repository navigation

| Location | Purpose |
|---|---|
| [Main Colab notebook](P2P_MCP_Three_Model_Colab_Experiment_95pct_Documented.ipynb) | Experiment workflow; verify committed version matches final local scorer |
| [data/](data/) | Historical pilot and expanded synthetic source |
| [tool_catalog.json](tool_catalog.json) | Descriptive MCP tool contracts |
| [scripts/validate_dataset.py](scripts/validate_dataset.py) | **Pilot-only** structural validator; asserts 400 conversations / 420 turns |
| [mcp_capstone_outputs/](mcp_capstone_outputs/) | Processed data, predictions, scores, charts, metadata |
| [Repository guide](docs/REPOSITORY_GUIDE.md) | Organization and reproducibility checks |
| [requirements.txt](requirements.txt) | Python environment dependencies |

## Getting started

1. Clone this repository and create a Python environment, or open the notebook in Google Colab.
2. Install packages: `pip install -r requirements.txt`.
3. Configure the notebook's input paths and model endpoint credentials; **never commit API keys**.
4. For the **historical pilot only**, run `python scripts/validate_dataset.py`.
5. Run the final experiment notebook in cell order if you have inference access; model calls may incur costs. For offline inspection, use committed results under `mcp_capstone_outputs/`.
6. Inspect `final_test_scored_long.csv`, the seven `fig*.png` charts, and the scoring-denominator caveat above.

This repository does not currently establish a verified one-command offline replay or actual ERP/MCP execution. The main notebook and scoring implementation should be checked against the final locally tested version.

## Limitations and license

The benchmark is synthetic and its gold references were not independently execution-validated. Family overlap across partitions and conditional RQ3 restrict generalizability. These scores are not evidence of production transaction safety.

No explicit license was verified in the repository. Suggested licenses in the pilot documentation do not constitute permission; add LICENSE files only after selecting terms.
