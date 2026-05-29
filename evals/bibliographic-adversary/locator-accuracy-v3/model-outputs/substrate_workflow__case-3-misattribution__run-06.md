---
run_id: locator-accuracy-v3-substrate-workflow-case-3-misattribution-run-06
created: 2026-05-29
eval_type: bibliographic-adversary
case_id: locator-accuracy-v3
case_key: case-3-misattribution
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
seed: 6063
initial_seed: 6063
retry_reason: none
prompt_source: frozen condition packet substrate_workflow / case-3-misattribution; see run-packet.md
prompt_sha256: a16d4e9133e0bbcadf6870d5417305e5d6fad019f9e093d05ff7640b45e1f12c
source_packet: frozen condition packet assembled from run-packet.md recipes
source_packet_sha256: 3accdac2c73765b32a9f1a58775dc8f9f2d9217980330ab0f7184faf8a790e2f
condition_packet_sha256: 3accdac2c73765b32a9f1a58775dc8f9f2d9217980330ab0f7184faf8a790e2f
substrate_brief_sha256: 070be6067cf273cd686d3e3077645248d2cabb38b3d94fb6e650edb93ca1ad17
output_body_sha256: 5a373671d819f6c7807f5daa3c6535b046daae03a47714d850a742368fff7cd4
output_file: model-outputs/substrate_workflow__case-3-misattribution__run-06.md
local_output_file: local-only/runs/locator-accuracy-v3-v1/outputs/substrate_workflow__case-3-misattribution__run-06.md
judge_model_id: pending - not yet judged
judge_prompt_sha256: pending - not yet judged
judge_independence: pending - not yet judged
raw_model_output_public_safe: true
operator_notes: Real model run via LM Studio OpenAI-compatible local server, not an in-session simulation. Run 6 of 8 for substrate_workflow / case-3-misattribution under frozen benchmark locator-accuracy-v3-v1. The condition packet sha256 was verified before generation. Generation wall time 19.7s; finish_reason stop; prompt_tokens 4702; completion_tokens 265; total_tokens 4967. Initial seed 6063; actual seed 6063; retry_reason none. The verbatim final answer is reproduced below and is what future condition-blind judges will score. A model output is a test artifact, never an authority and never citable as a source. The case is not yet judged, anonymised, scored, or reconciled.
---

# Model Output - substrate_workflow / case-3-misattribution (run 06)

## Condition

Benchmark version `locator-accuracy-v3-v1`, condition `substrate_workflow`, case `case-3-misattribution`, run 6 of 8. Real LM Studio model run: `gemma-4-31b-it-mlx`, seed 6063, on the frozen condition packet `sha256:3accdac2c73765b32a9f1a58775dc8f9f2d9217980330ab0f7184faf8a790e2f`.

## Output

The draft contains a false attribution. The concept of "normalization of deviance" is not attributed to James Reason or `BK-0044-card-002` in the provided reference packet; it is attributed to Vaughan in `BK-0042-card-001`.

**Corrected Note:**
Normalization of deviance is an organizational process where a group repeatedly encounters warning signs or performance departures from expectations and gradually treats these anomalies as acceptable. This shifts the threshold of what is considered a dangerous condition, allowing an organization to operate in a steadily degraded state while perceiving it as routine and safe. This process is driven by the working group's evolving culture, the surrounding professional culture, and "structural secrecy"—the bureaucratic partitioning of information that prevents separate warning signs from being recognized as a single trend.

**Supported Lineage:**
- `BK-0042-card-001`, Chapter 10 (pp. 404–439): Normalization of deviance is the process by which groups treat repeated departures from expected performance as acceptable, moving the threshold of danger and allowing degraded conditions to be regarded as routine. This is driven by evolving culture, professional culture, and structural secrecy (bureaucratic partitioning of information).
