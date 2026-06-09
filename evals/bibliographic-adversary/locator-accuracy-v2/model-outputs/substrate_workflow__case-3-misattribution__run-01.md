---
run_id: locator-accuracy-v2-substrate-workflow-case-3-misattribution-run-01
created: 2026-05-28
eval_type: bibliographic-adversary
case_id: locator-accuracy-v2
case_key: case-3-misattribution
benchmark_version: locator-accuracy-v2-v1
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
seed: 1063
initial_seed: 1063
retry_reason: none
prompt_source: frozen condition packet substrate_workflow / case-3-misattribution; see run-packet.md
prompt_sha256: 7a0e8e5d3af4d6c3ef958d3773453b158ac190063c748f55e019a51487b61a0b
source_packet: frozen condition packet assembled from run-packet.md recipes
source_packet_sha256: a694ac7493d4b64ead768308356878698f24dc2a1ab770d853b4ebbd66f1eebe
condition_packet_sha256: a694ac7493d4b64ead768308356878698f24dc2a1ab770d853b4ebbd66f1eebe
substrate_brief_sha256: e1391a54f84fdad9ec6b2792801b07b049eb63cfb8ddac2e8b2df7f7173280f5
output_body_sha256: 06d08529e0b5db0e8c10a63e9861f19d92248df30ec08612d3e1e56608ec3d03
output_file: model-outputs/substrate_workflow__case-3-misattribution__run-01.md
local_output_file: local-only/runs/locator-accuracy-v2-v1/outputs/substrate_workflow__case-3-misattribution__run-01.md
judge_model_id: pending - not yet judged
judge_prompt_sha256: pending - not yet judged
judge_independence: pending - not yet judged
raw_model_output_public_safe: true
operator_notes: Real model run via LM Studio OpenAI-compatible local server, not an in-session simulation. Run 1 of 8 for substrate_workflow / case-3-misattribution under frozen benchmark locator-accuracy-v2-v1. The condition packet sha256 was verified before generation. Generation wall time 26.1s; finish_reason stop; prompt_tokens 4614; completion_tokens 183; total_tokens 4797. Initial seed 1063; actual seed 1063; retry_reason none. The verbatim final answer is reproduced below and is what future condition-blind judges will score. A model output is a test artifact, never an authority and never citable as a source. The case is not yet judged, anonymised, scored, or reconciled.
---

# Model Output - substrate_workflow / case-3-misattribution (run 01)

## Condition

Benchmark version `locator-accuracy-v2-v1`, condition `substrate_workflow`, case `case-3-misattribution`, run 1 of 8. Real LM Studio model run: `gemma-4-31b-it-mlx`, seed 1063, on the frozen condition packet `sha256:a694ac7493d4b64ead768308356878698f24dc2a1ab770d853b4ebbd66f1eebe`.

## Output

The draft contains a lineage error: "normalization of deviance" is not attributed to James Reason or `BK-0044-card-002`. According to the provided brief, that concept is attributed to Vaughan in `BK-0042-card-001`.

**Corrected Note:**

Normalization of deviance is an organizational process where a group repeatedly encounters warning signs or performance departures from expectations and gradually treats them as acceptable. This shifts the threshold of what is considered dangerous, allowing an organization to operate in a steadily degraded condition while perceiving it as routine and safe. This process is driven by the working group's evolving culture, the surrounding professional culture, and "structural secrecy"—the bureaucratic partitioning of information that prevents separate warning signs from being recognized as a single trend (`BK-0042-card-001`, Chapter 10).
