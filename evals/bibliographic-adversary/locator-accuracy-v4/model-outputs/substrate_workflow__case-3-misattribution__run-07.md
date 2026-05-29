---
run_id: locator-accuracy-v4-substrate-workflow-case-3-misattribution-run-07
created: 2026-05-29
eval_type: bibliographic-adversary
case_id: locator-accuracy-v4
case_key: case-3-misattribution
benchmark_version: locator-accuracy-v4-v1
model_condition: substrate_workflow
run_number: 7
model_name: gemma-4-31b-it-mlx
model_id: gemma-4-31b-it-mlx
model_snapshot: LM Studio /v1/models exposes model id gemma-4-31b-it-mlx only; no separate snapshot exposed
runtime: LM Studio local OpenAI-compatible server at http://127.0.0.1:1234
provider: local
temperature: 0.1
top_p: 0.9
max_tokens: 800
timeout_seconds: 300
seed: 7063
initial_seed: 7063
retry_reason: none
prompt_source: frozen condition packet substrate_workflow / case-3-misattribution; see run-packet.md
prompt_sha256: a16d4e9133e0bbcadf6870d5417305e5d6fad019f9e093d05ff7640b45e1f12c
source_packet: frozen condition packet assembled from run-packet.md recipes
source_packet_sha256: e831362368d4143454ff8513f5322915f05b600899104333213d95220b05b299
condition_packet_sha256: e831362368d4143454ff8513f5322915f05b600899104333213d95220b05b299
substrate_brief_sha256: b0c8b97206715147b5f3b5c43e064d08225c6c6bdc7c80b058d78c2cf7e990d8
output_body_sha256: 4e34d32e227e27e26cfee6bfac20b1f4725d39baf5d4e26d24172434569841d4
output_file: model-outputs/substrate_workflow__case-3-misattribution__run-07.md
local_output_file: local-only/runs/locator-accuracy-v4-v1/outputs/substrate_workflow__case-3-misattribution__run-07.md
judge_model_id: pending - not yet judged
judge_prompt_sha256: pending - not yet judged
judge_independence: pending - not yet judged
raw_model_output_public_safe: true
operator_notes: Real model run via LM Studio OpenAI-compatible local server, not an in-session simulation. Run 7 of 8 for substrate_workflow / case-3-misattribution under frozen benchmark locator-accuracy-v4-v1. The condition packet sha256 was verified before generation. Generation wall time 20.0s; finish_reason stop; prompt_tokens 4722; completion_tokens 269; total_tokens 4991. Initial seed 7063; actual seed 7063; retry_reason none. The verbatim final answer is reproduced below and is what future condition-blind judges will score. A model output is a test artifact, never an authority and never citable as a source. The case is not yet judged, anonymised, scored, or reconciled.
---

# Model Output - substrate_workflow / case-3-misattribution (run 07)

## Condition

Benchmark version `locator-accuracy-v4-v1`, condition `substrate_workflow`, case `case-3-misattribution`, run 7 of 8. Real LM Studio model run: `gemma-4-31b-it-mlx`, seed 7063, on the frozen condition packet `sha256:e831362368d4143454ff8513f5322915f05b600899104333213d95220b05b299`.

## Output

The draft contains a false attribution. The concept of "normalization of deviance" is not attributed to James Reason or `BK-0044-card-002` in the provided reference packet; it is attributed to Vaughan in `BK-0042-card-001`.

**Corrected Note:**

Normalization of deviance is an organizational process where a group repeatedly encounters warning signs or performance departures from expectations and gradually treats these anomalies as acceptable. This shifts the threshold of what is considered a dangerous condition, allowing an organization to operate in a steadily degraded state while perceiving it as routine and safe. This process is driven by the working group's evolving culture, the surrounding professional culture, and "structural secrecy"—the bureaucratic partitioning of information that prevents separate warning signs from being recognized as a single trend.

**Supported Lineage:**

- `BK-0042-card-001`, Chapter 10 (pp. 404–439): Normalization of deviance is the process by which groups treat repeated departures from expected performance as acceptable, moving the threshold of danger outward and allowing degraded conditions to be regarded as routine. This is driven by evolving culture, wider organizational/professional culture, and structural secrecy (bureaucratic partitioning of information).
