---
run_id: locator-accuracy-v3-substrate-workflow-case-1-missing-card-run-01
created: 2026-05-29
eval_type: bibliographic-adversary
case_id: locator-accuracy-v3
case_key: case-1-missing-card
benchmark_version: locator-accuracy-v3-v1
model_condition: substrate_workflow
run_number: 1
model_name: gemma-4-31b-it-mlx
model_id: gemma-4-31b-it-mlx
model_snapshot: LM Studio /v1/models exposes model id gemma-4-31b-it-mlx only; no separate snapshot exposed
runtime: LM Studio local OpenAI-compatible server at http://127.0.0.1:1234
provider: local
temperature: 0.1
top_p: 0.9
max_tokens: 800
timeout_seconds: 300
seed: 1061
initial_seed: 1061
retry_reason: none
prompt_source: frozen condition packet substrate_workflow / case-1-missing-card; see run-packet.md
prompt_sha256: a16d4e9133e0bbcadf6870d5417305e5d6fad019f9e093d05ff7640b45e1f12c
source_packet: frozen condition packet assembled from run-packet.md recipes
source_packet_sha256: 36abf2eabc705bebc8c072c03567abc83df7e1162c188277262a39fb634b297c
condition_packet_sha256: 36abf2eabc705bebc8c072c03567abc83df7e1162c188277262a39fb634b297c
substrate_brief_sha256: 070be6067cf273cd686d3e3077645248d2cabb38b3d94fb6e650edb93ca1ad17
output_body_sha256: c7b105f49e89a40b882fae77655aff48d3db74c97062fa33b99d69c6336847dd
output_file: model-outputs/substrate_workflow__case-1-missing-card__run-01.md
local_output_file: local-only/runs/locator-accuracy-v3-v1/outputs/substrate_workflow__case-1-missing-card__run-01.md
judge_model_id: pending - not yet judged
judge_prompt_sha256: pending - not yet judged
judge_independence: pending - not yet judged
raw_model_output_public_safe: true
operator_notes: Real model run via LM Studio OpenAI-compatible local server, not an in-session simulation. Run 1 of 8 for substrate_workflow / case-1-missing-card under frozen benchmark locator-accuracy-v3-v1. The condition packet sha256 was verified before generation. Generation wall time 26.0s; finish_reason stop; prompt_tokens 4720; completion_tokens 224; total_tokens 4944. Initial seed 1061; actual seed 1061; retry_reason none. The verbatim final answer is reproduced below and is what future condition-blind judges will score. A model output is a test artifact, never an authority and never citable as a source. The case is not yet judged, anonymised, scored, or reconciled.
---

# Model Output - substrate_workflow / case-1-missing-card (run 01)

## Condition

Benchmark version `locator-accuracy-v3-v1`, condition `substrate_workflow`, case `case-1-missing-card`, run 1 of 8. Real LM Studio model run: `gemma-4-31b-it-mlx`, seed 1061, on the frozen condition packet `sha256:36abf2eabc705bebc8c072c03567abc83df7e1162c188277262a39fb634b297c`.

## Output

### Corrected Note: Halo Effect Boundary Conditions

The halo effect in business analysis occurs when a general impression of a company's overall performance drives the rating of its specific attributes (such as culture, strategy, or leadership). A key scope condition is that this effect applies to retrospective analyses where attributes are narrative-coded rather than independently and blindly measured.

**Supported Lineage:**
- `BK-0048-card-001`, Chapter 4: The halo effect is the tendency for a general impression of overall performance to drive ratings of specific attributes; trait assessments formed after the performance signal are not independent evidence.

**Lineage Corrections:**
- **Unsupported Source Card:** The draft's reference to a "second BK-0048 source card" regarding a blind-measurement exception is not supported by the provided reference packet. Only `BK-0048-card-001` is available.
- **Unsupported Quote:** The requested verbatim citation ("halo applies only when trait assessment is performance-aware") is not present in the available reviewed material.
