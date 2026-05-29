---
run_id: locator-accuracy-v3-vanilla-long-prompt-case-3-misattribution-run-01
created: 2026-05-29
eval_type: bibliographic-adversary
case_id: locator-accuracy-v3
case_key: case-3-misattribution
benchmark_version: locator-accuracy-v3-v1
model_condition: vanilla_long_prompt
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
seed: 1023
initial_seed: 1023
retry_reason: none
prompt_source: frozen condition packet vanilla_long_prompt / case-3-misattribution; see run-packet.md
prompt_sha256: a16d4e9133e0bbcadf6870d5417305e5d6fad019f9e093d05ff7640b45e1f12c
source_packet: frozen condition packet assembled from run-packet.md recipes
source_packet_sha256: fc3f95ac6ae72f897590ce8bc87bed7d10cbe28914fd49d6088e15d28c965312
condition_packet_sha256: fc3f95ac6ae72f897590ce8bc87bed7d10cbe28914fd49d6088e15d28c965312
substrate_brief_sha256: n/a - non-substrate condition supplies no brief
output_body_sha256: 2855953bed7fd91d24143718ab5d03597125ffb3479c5f244c8596ebbf0a5c24
output_file: model-outputs/vanilla_long_prompt__case-3-misattribution__run-01.md
local_output_file: local-only/runs/locator-accuracy-v3-v1/outputs/vanilla_long_prompt__case-3-misattribution__run-01.md
judge_model_id: pending - not yet judged
judge_prompt_sha256: pending - not yet judged
judge_independence: pending - not yet judged
raw_model_output_public_safe: true
operator_notes: Real model run via LM Studio OpenAI-compatible local server, not an in-session simulation. Run 1 of 8 for vanilla_long_prompt / case-3-misattribution under frozen benchmark locator-accuracy-v3-v1. The condition packet sha256 was verified before generation. Generation wall time 14.8s; finish_reason stop; prompt_tokens 3749; completion_tokens 97; total_tokens 3846. Initial seed 1023; actual seed 1023; retry_reason none. The verbatim final answer is reproduced below and is what future condition-blind judges will score. A model output is a test artifact, never an authority and never citable as a source. The case is not yet judged, anonymised, scored, or reconciled.
---

# Model Output - vanilla_long_prompt / case-3-misattribution (run 01)

## Condition

Benchmark version `locator-accuracy-v3-v1`, condition `vanilla_long_prompt`, case `case-3-misattribution`, run 1 of 8. Real LM Studio model run: `gemma-4-31b-it-mlx`, seed 1023, on the frozen condition packet `sha256:fc3f95ac6ae72f897590ce8bc87bed7d10cbe28914fd49d6088e15d28c965312`.

## Output

The requested source card `BK-0044-card-002` and the attribution of "normalization of deviance" to James Reason in *Human Error* Chapter 8 are not supported by the available public KB material.

**Corrected Note:**
The provided draft claims that James Reason introduced the concept of "normalization of deviance" in *Human Error* Chapter 8; however, this attribution cannot be verified using the available public KB lineage.
