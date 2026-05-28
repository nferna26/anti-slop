---
run_id: locator-accuracy-v2-substrate-workflow-case-1-missing-card-run-03
created: 2026-05-28
eval_type: bibliographic-adversary
case_id: locator-accuracy-v2
case_key: case-1-missing-card
benchmark_version: locator-accuracy-v2-v1
model_condition: substrate_workflow
run_number: 3
model_name: gemma-4-31b-it-mlx
model_id: gemma-4-31b-it-mlx
model_snapshot: LM Studio /v1/models exposes model id gemma-4-31b-it-mlx only; no separate snapshot exposed
runtime: LM Studio local OpenAI-compatible server at http://127.0.0.1:1234
provider: local
temperature: 0.1
top_p: 0.9
max_tokens: 800
timeout_seconds: 300
seed: 3061
initial_seed: 3061
retry_reason: none
prompt_source: frozen condition packet substrate_workflow / case-1-missing-card; see run-packet.md
prompt_sha256: 7a0e8e5d3af4d6c3ef958d3773453b158ac190063c748f55e019a51487b61a0b
source_packet: frozen condition packet assembled from run-packet.md recipes
source_packet_sha256: 0352af4e081cb9366e3438551196fb9eb5d1a55703e7f0b2516b75b01ee04952
condition_packet_sha256: 0352af4e081cb9366e3438551196fb9eb5d1a55703e7f0b2516b75b01ee04952
substrate_brief_sha256: e1391a54f84fdad9ec6b2792801b07b049eb63cfb8ddac2e8b2df7f7173280f5
output_body_sha256: 89f74df2eb7d36841e9afe925b9e16c9adc3fbbfb6072435c6989c45a71ae435
output_file: model-outputs/substrate_workflow__case-1-missing-card__run-03.md
local_output_file: local-only/runs/locator-accuracy-v2-v1/outputs/substrate_workflow__case-1-missing-card__run-03.md
judge_model_id: pending - not yet judged
judge_prompt_sha256: pending - not yet judged
judge_independence: pending - not yet judged
raw_model_output_public_safe: true
operator_notes: Real model run via LM Studio OpenAI-compatible local server, not an in-session simulation. Run 3 of 8 for substrate_workflow / case-1-missing-card under frozen benchmark locator-accuracy-v2-v1. The condition packet sha256 was verified before generation. Generation wall time 27.3s; finish_reason stop; prompt_tokens 4632; completion_tokens 186; total_tokens 4818. Initial seed 3061; actual seed 3061; retry_reason none. The verbatim final answer is reproduced below and is what future condition-blind judges will score. A model output is a test artifact, never an authority and never citable as a source. The case is not yet judged, anonymised, scored, or reconciled.
---

# Model Output - substrate_workflow / case-1-missing-card (run 03)

## Condition

Benchmark version `locator-accuracy-v2-v1`, condition `substrate_workflow`, case `case-1-missing-card`, run 3 of 8. Real LM Studio model run: `gemma-4-31b-it-mlx`, seed 3061, on the frozen condition packet `sha256:0352af4e081cb9366e3438551196fb9eb5d1a55703e7f0b2516b75b01ee04952`.

## Output

Corrected note:

The halo effect in business analysis is the tendency for a general impression of a company's overall performance to drive how observers rate specific attributes (such as culture, strategy, or leadership). This effect applies when trait assessments are narrative-coded after the performance signal is known; it does not establish that every retrospective business claim is halo-tinted, only that assessments formed after the performance signal are not independent evidence (`BK-0048-card-001`, Chapter 4).

**Lineage Correction:**
The draft's reference to a "second BK-0048 source card" regarding blind-measurement exceptions is unsupported. Only `BK-0048-card-001` is available in the provided KB lineage. The scope conditions regarding independent/blind measurement are contained within `BK-0048-card-001`.
