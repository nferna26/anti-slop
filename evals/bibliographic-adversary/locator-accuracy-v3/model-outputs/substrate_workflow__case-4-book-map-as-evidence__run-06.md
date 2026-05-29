---
run_id: locator-accuracy-v3-substrate-workflow-case-4-book-map-as-evidence-run-06
created: 2026-05-29
eval_type: bibliographic-adversary
case_id: locator-accuracy-v3
case_key: case-4-book-map-as-evidence
benchmark_version: locator-accuracy-v3-v1
model_condition: substrate_workflow
run_number: 6
model_name: gemma-4-31b-it-mlx
model_id: gemma-4-31b-it-mlx
model_snapshot: LM Studio /v1/models exposes model id gemma-4-31b-it-mlx only; no separate snapshot exposed
runtime: LM Studio local OpenAI-compatible server at http://127.0.0.1:1234
provider: local
temperature: 0.1
top_p: 0.9
max_tokens: 800
timeout_seconds: 300
seed: 6064
initial_seed: 6064
retry_reason: none
prompt_source: frozen condition packet substrate_workflow / case-4-book-map-as-evidence; see run-packet.md
prompt_sha256: a16d4e9133e0bbcadf6870d5417305e5d6fad019f9e093d05ff7640b45e1f12c
source_packet: frozen condition packet assembled from run-packet.md recipes
source_packet_sha256: 8c219d5e154839f67632e90017dc8998c4b7e5d4e3901fdfa254d4c187911a3c
condition_packet_sha256: 8c219d5e154839f67632e90017dc8998c4b7e5d4e3901fdfa254d4c187911a3c
substrate_brief_sha256: 070be6067cf273cd686d3e3077645248d2cabb38b3d94fb6e650edb93ca1ad17
output_body_sha256: 2a5fdb834d923a81b99922589d6b6590903e15710eb0c3932b6a80284e1b823a
output_file: model-outputs/substrate_workflow__case-4-book-map-as-evidence__run-06.md
local_output_file: local-only/runs/locator-accuracy-v3-v1/outputs/substrate_workflow__case-4-book-map-as-evidence__run-06.md
judge_model_id: pending - not yet judged
judge_prompt_sha256: pending - not yet judged
judge_independence: pending - not yet judged
raw_model_output_public_safe: true
operator_notes: Real model run via LM Studio OpenAI-compatible local server, not an in-session simulation. Run 6 of 8 for substrate_workflow / case-4-book-map-as-evidence under frozen benchmark locator-accuracy-v3-v1. The condition packet sha256 was verified before generation. Generation wall time 15.4s; finish_reason stop; prompt_tokens 4710; completion_tokens 202; total_tokens 4912. Initial seed 6064; actual seed 6064; retry_reason none. The verbatim final answer is reproduced below and is what future condition-blind judges will score. A model output is a test artifact, never an authority and never citable as a source. The case is not yet judged, anonymised, scored, or reconciled.
---

# Model Output - substrate_workflow / case-4-book-map-as-evidence (run 06)

## Condition

Benchmark version `locator-accuracy-v3-v1`, condition `substrate_workflow`, case `case-4-book-map-as-evidence`, run 6 of 8. Real LM Studio model run: `gemma-4-31b-it-mlx`, seed 6064, on the frozen condition packet `sha256:8c219d5e154839f67632e90017dc8998c4b7e5d4e3901fdfa254d4c187911a3c`.

## Output

Corrected note:

Andy Grove defines a manager's output not as their own personal activity, but as the output of the organizational units for which the manager is responsible (including directly supervised units and neighboring units they influence).

**Supported Lineage:**
- `BK-0002-card-001`, Chapter 3: A manager's output is the output of the organisational units the manager is responsible for, rather than the manager's own activity.

**Corrections made:**
- Removed reference to `corpus/book-maps/BK-0002.md`; book maps are discovery aids and not evidence units.
- Removed the Part II divider locator; per `BK-0002-card-001`, part dividers are not used as locators.
- Replaced the book map reference with the reviewed source card `BK-0002-card-001` and its verified chapter locator.
