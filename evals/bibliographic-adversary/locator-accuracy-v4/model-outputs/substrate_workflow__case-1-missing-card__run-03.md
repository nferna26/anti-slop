---
run_id: locator-accuracy-v4-substrate-workflow-case-1-missing-card-run-03
created: 2026-05-29
eval_type: bibliographic-adversary
case_id: locator-accuracy-v4
case_key: case-1-missing-card
benchmark_version: locator-accuracy-v4-v1
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
prompt_sha256: a16d4e9133e0bbcadf6870d5417305e5d6fad019f9e093d05ff7640b45e1f12c
source_packet: frozen condition packet assembled from run-packet.md recipes
source_packet_sha256: feb6e07fb52295dcb91ed18c210fa4e785d579221cb3722e24d2d42796bd7a00
condition_packet_sha256: feb6e07fb52295dcb91ed18c210fa4e785d579221cb3722e24d2d42796bd7a00
substrate_brief_sha256: b0c8b97206715147b5f3b5c43e064d08225c6c6bdc7c80b058d78c2cf7e990d8
output_body_sha256: edb89fd639caa9970a6a7b72d4fe5f23b7760d8778df48301ad652ff8c3a53c9
output_file: model-outputs/substrate_workflow__case-1-missing-card__run-03.md
local_output_file: local-only/runs/locator-accuracy-v4-v1/outputs/substrate_workflow__case-1-missing-card__run-03.md
judge_model_id: pending - not yet judged
judge_prompt_sha256: pending - not yet judged
judge_independence: pending - not yet judged
raw_model_output_public_safe: true
operator_notes: Real model run via LM Studio OpenAI-compatible local server, not an in-session simulation. Run 3 of 8 for substrate_workflow / case-1-missing-card under frozen benchmark locator-accuracy-v4-v1. The condition packet sha256 was verified before generation. Generation wall time 17.1s; finish_reason stop; prompt_tokens 4740; completion_tokens 227; total_tokens 4967. Initial seed 3061; actual seed 3061; retry_reason none. The verbatim final answer is reproduced below and is what future condition-blind judges will score. A model output is a test artifact, never an authority and never citable as a source. The case is not yet judged, anonymised, scored, or reconciled.
---

# Model Output - substrate_workflow / case-1-missing-card (run 03)

## Condition

Benchmark version `locator-accuracy-v4-v1`, condition `substrate_workflow`, case `case-1-missing-card`, run 3 of 8. Real LM Studio model run: `gemma-4-31b-it-mlx`, seed 3061, on the frozen condition packet `sha256:feb6e07fb52295dcb91ed18c210fa4e785d579221cb3722e24d2d42796bd7a00`.

## Output

### Corrected Note: Halo Effect Boundary Conditions

The halo effect in business analysis occurs when a general impression of a company's overall performance drives the rating of its specific attributes (such as culture, strategy, leadership, or customer focus). This effect is present when trait assessments are formed after the performance signal is known; consequently, these ratings do not constitute independent evidence of those attributes.

**Supported Lineage:**
- `BK-0048-card-001`, Chapter 4: The halo effect is the tendency for overall performance impressions to drive ratings of specific attributes; trait assessments formed after the performance signal are not independent evidence.

**Lineage Corrections:**
- **Unsupported Source Card:** The draft's reference to a "second BK-0048 source card" regarding blind-measurement exceptions is not supported by the provided reference packet. Only `BK-0048-card-001` is available.
- **Unsupported Quote:** The requested verbatim citation ("halo applies only when trait assessment is performance-aware") is not present in the available reviewed material.
