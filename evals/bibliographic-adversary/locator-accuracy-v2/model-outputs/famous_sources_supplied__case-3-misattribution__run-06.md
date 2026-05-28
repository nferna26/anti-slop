---
run_id: locator-accuracy-v2-famous-sources-supplied-case-3-misattribution-run-06
created: 2026-05-28
eval_type: bibliographic-adversary
case_id: locator-accuracy-v2
case_key: case-3-misattribution
benchmark_version: locator-accuracy-v2-v1
model_condition: famous_sources_supplied
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
seed: 6053
initial_seed: 6053
retry_reason: none
prompt_source: frozen condition packet famous_sources_supplied / case-3-misattribution; see run-packet.md
prompt_sha256: 7a0e8e5d3af4d6c3ef958d3773453b158ac190063c748f55e019a51487b61a0b
source_packet: frozen condition packet assembled from run-packet.md recipes
source_packet_sha256: e4213fbe0907bad5e7cb443563fa5cc1b113321f9f79829bd7fde0cd39b47195
condition_packet_sha256: e4213fbe0907bad5e7cb443563fa5cc1b113321f9f79829bd7fde0cd39b47195
substrate_brief_sha256: not_applicable
output_body_sha256: 762b8e40617091093957dd77167f789b36b109f2554d3d888d2b6bd0e1e67705
output_file: model-outputs/famous_sources_supplied__case-3-misattribution__run-06.md
local_output_file: local-only/runs/locator-accuracy-v2-v1/outputs/famous_sources_supplied__case-3-misattribution__run-06.md
judge_model_id: pending - not yet judged
judge_prompt_sha256: pending - not yet judged
judge_independence: pending - not yet judged
raw_model_output_public_safe: true
operator_notes: Real model run via LM Studio OpenAI-compatible local server, not an in-session simulation. Run 6 of 8 for famous_sources_supplied / case-3-misattribution under frozen benchmark locator-accuracy-v2-v1. The condition packet sha256 was verified before generation. Generation wall time 9.4s; finish_reason stop; prompt_tokens 441; completion_tokens 103; total_tokens 544. Initial seed 6053; actual seed 6053; retry_reason none. The verbatim final answer is reproduced below and is what future condition-blind judges will score. A model output is a test artifact, never an authority and never citable as a source. The case is not yet judged, anonymised, scored, or reconciled.
---

# Model Output - famous_sources_supplied / case-3-misattribution (run 06)

## Condition

Benchmark version `locator-accuracy-v2-v1`, condition `famous_sources_supplied`, case `case-3-misattribution`, run 6 of 8. Real LM Studio model run: `gemma-4-31b-it-mlx`, seed 6053, on the frozen condition packet `sha256:e4213fbe0907bad5e7cb443563fa5cc1b113321f9f79829bd7fde0cd39b47195`.

## Output

The provided public KB packet contains no claim, summary, card ID, or authority relation for the listed titles. Specifically:

- There is no available material to verify that James Reason introduced "normalization of deviance" in *Human Error* Chapter 8.
- There is no record of source card `BK-0044-card-002` in the provided lineage.

Because these references are unsupported by the available public KB material, they cannot be included in a corrected note.
