---
run_id: locator-accuracy-v2-substrate-workflow-case-1-missing-card-run-04
created: 2026-05-28
eval_type: bibliographic-adversary
case_id: locator-accuracy-v2
case_key: case-1-missing-card
benchmark_version: locator-accuracy-v2-v1
model_condition: substrate_workflow
run_number: 4
model_name: gemma-4-31b-it-mlx
model_id: gemma-4-31b-it-mlx
model_snapshot: LM Studio /v1/models exposes model id gemma-4-31b-it-mlx only; no separate snapshot exposed
runtime: LM Studio local OpenAI-compatible server at http://127.0.0.1:1234
provider: local
temperature: 0.1
top_p: 0.9
max_tokens: 800
timeout_seconds: 300
seed: 4061
initial_seed: 4061
retry_reason: none
prompt_source: frozen condition packet substrate_workflow / case-1-missing-card; see run-packet.md
prompt_sha256: 7a0e8e5d3af4d6c3ef958d3773453b158ac190063c748f55e019a51487b61a0b
source_packet: frozen condition packet assembled from run-packet.md recipes
source_packet_sha256: 0352af4e081cb9366e3438551196fb9eb5d1a55703e7f0b2516b75b01ee04952
condition_packet_sha256: 0352af4e081cb9366e3438551196fb9eb5d1a55703e7f0b2516b75b01ee04952
substrate_brief_sha256: e1391a54f84fdad9ec6b2792801b07b049eb63cfb8ddac2e8b2df7f7173280f5
output_body_sha256: cda5265294f0c1884283a44dd3d8cf2ac55dba80f43faae7f2bb29b814b1d751
output_file: model-outputs/substrate_workflow__case-1-missing-card__run-04.md
local_output_file: local-only/runs/locator-accuracy-v2-v1/outputs/substrate_workflow__case-1-missing-card__run-04.md
judge_model_id: pending - not yet judged
judge_prompt_sha256: pending - not yet judged
judge_independence: pending - not yet judged
raw_model_output_public_safe: true
operator_notes: Real model run via LM Studio OpenAI-compatible local server, not an in-session simulation. Run 4 of 8 for substrate_workflow / case-1-missing-card under frozen benchmark locator-accuracy-v2-v1. The condition packet sha256 was verified before generation. Generation wall time 26.3s; finish_reason stop; prompt_tokens 4632; completion_tokens 175; total_tokens 4807. Initial seed 4061; actual seed 4061; retry_reason none. The verbatim final answer is reproduced below and is what future condition-blind judges will score. A model output is a test artifact, never an authority and never citable as a source. The case is not yet judged, anonymised, scored, or reconciled.
---

# Model Output - substrate_workflow / case-1-missing-card (run 04)

## Condition

Benchmark version `locator-accuracy-v2-v1`, condition `substrate_workflow`, case `case-1-missing-card`, run 4 of 8. Real LM Studio model run: `gemma-4-31b-it-mlx`, seed 4061, on the frozen condition packet `sha256:0352af4e081cb9366e3438551196fb9eb5d1a55703e7f0b2516b75b01ee04952`.

## Output

Corrected note:

The halo effect in business analysis is the tendency for a general impression of a company's overall performance to drive how observers rate specific attributes (such as culture, strategy, or leadership). A key scope condition is that this effect applies when attributes are narrative-coded rather than independently and blindly measured; trait assessments formed after the performance signal is known do not constitute independent evidence (`BK-0048-card-001`, Chapter 4).

**Lineage Corrections:**
- The draft's reference to a "second BK-0048 source card" is unsupported; only `BK-0048-card-001` is available in the provided packet.
- The requested verbatim citation "halo applies only when trait assessment is performance-aware" is not present in the available source material.
