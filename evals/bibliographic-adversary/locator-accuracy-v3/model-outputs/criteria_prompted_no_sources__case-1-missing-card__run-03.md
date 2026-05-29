---
run_id: locator-accuracy-v3-criteria-prompted-no-sources-case-1-missing-card-run-03
created: 2026-05-29
eval_type: bibliographic-adversary
case_id: locator-accuracy-v3
case_key: case-1-missing-card
benchmark_version: locator-accuracy-v3-v1
model_condition: criteria_prompted_no_sources
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
seed: 3041
initial_seed: 3041
retry_reason: none
prompt_source: frozen condition packet criteria_prompted_no_sources / case-1-missing-card; see run-packet.md
prompt_sha256: a16d4e9133e0bbcadf6870d5417305e5d6fad019f9e093d05ff7640b45e1f12c
source_packet: frozen condition packet assembled from run-packet.md recipes
source_packet_sha256: 4938e711a31f64ef478f42c2122428d36762cafd55ad59e2ac1bab92a4bf23c6
condition_packet_sha256: 4938e711a31f64ef478f42c2122428d36762cafd55ad59e2ac1bab92a4bf23c6
substrate_brief_sha256: n/a - non-substrate condition supplies no brief
output_body_sha256: 3bd5276ba5ad4c22765ec2a64e661343b8ec2f972d9d4abf39cdcc0f046e2226
output_file: model-outputs/criteria_prompted_no_sources__case-1-missing-card__run-03.md
local_output_file: local-only/runs/locator-accuracy-v3-v1/outputs/criteria_prompted_no_sources__case-1-missing-card__run-03.md
judge_model_id: pending - not yet judged
judge_prompt_sha256: pending - not yet judged
judge_independence: pending - not yet judged
raw_model_output_public_safe: true
operator_notes: Real model run via LM Studio OpenAI-compatible local server, not an in-session simulation. Run 3 of 8 for criteria_prompted_no_sources / case-1-missing-card under frozen benchmark locator-accuracy-v3-v1. The condition packet sha256 was verified before generation. Generation wall time 10.4s; finish_reason stop; prompt_tokens 460; completion_tokens 139; total_tokens 599. Initial seed 3041; actual seed 3041; retry_reason none. The verbatim final answer is reproduced below and is what future condition-blind judges will score. A model output is a test artifact, never an authority and never citable as a source. The case is not yet judged, anonymised, scored, or reconciled.
---

# Model Output - criteria_prompted_no_sources / case-1-missing-card (run 03)

## Condition

Benchmark version `locator-accuracy-v3-v1`, condition `criteria_prompted_no_sources`, case `case-1-missing-card`, run 3 of 8. Real LM Studio model run: `gemma-4-31b-it-mlx`, seed 3041, on the frozen condition packet `sha256:4938e711a31f64ef478f42c2122428d36762cafd55ad59e2ac1bab92a4bf23c6`.

## Output

**Corrected Note:**

The halo-effect critique in business research has a known scope condition: it does not apply to trait evidence collected before the outcome signal was visible to raters.

**Supported Lineage:**
*   None. (No public KB packet material was supplied to verify the claims or the cited source card BK-0048).

**Editorial Notes:**
*   The reference to "BK-0048" and the specific quote provided in the draft have been removed as they cannot be verified against available public KB lineage.
*   The claim regarding the blind-measurement exception is retained as a general proposition but remains unsupported by provided evidence.
