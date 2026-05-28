---
run_id: locator-accuracy-v2-substrate-workflow-case-3-misattribution-run-04
created: 2026-05-28
eval_type: bibliographic-adversary
case_id: locator-accuracy-v2
case_key: case-3-misattribution
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
seed: 4063
initial_seed: 4063
retry_reason: none
prompt_source: frozen condition packet substrate_workflow / case-3-misattribution; see run-packet.md
prompt_sha256: 7a0e8e5d3af4d6c3ef958d3773453b158ac190063c748f55e019a51487b61a0b
source_packet: frozen condition packet assembled from run-packet.md recipes
source_packet_sha256: a694ac7493d4b64ead768308356878698f24dc2a1ab770d853b4ebbd66f1eebe
condition_packet_sha256: a694ac7493d4b64ead768308356878698f24dc2a1ab770d853b4ebbd66f1eebe
substrate_brief_sha256: e1391a54f84fdad9ec6b2792801b07b049eb63cfb8ddac2e8b2df7f7173280f5
output_body_sha256: ff593cce94b7474b90c98eea69e3aa0a83de86b90669ac2df19adc2830dae258
output_file: model-outputs/substrate_workflow__case-3-misattribution__run-04.md
local_output_file: local-only/runs/locator-accuracy-v2-v1/outputs/substrate_workflow__case-3-misattribution__run-04.md
judge_model_id: pending - not yet judged
judge_prompt_sha256: pending - not yet judged
judge_independence: pending - not yet judged
raw_model_output_public_safe: true
operator_notes: Real model run via LM Studio OpenAI-compatible local server, not an in-session simulation. Run 4 of 8 for substrate_workflow / case-3-misattribution under frozen benchmark locator-accuracy-v2-v1. The condition packet sha256 was verified before generation. Generation wall time 28.7s; finish_reason stop; prompt_tokens 4614; completion_tokens 196; total_tokens 4810. Initial seed 4063; actual seed 4063; retry_reason none. The verbatim final answer is reproduced below and is what future condition-blind judges will score. A model output is a test artifact, never an authority and never citable as a source. The case is not yet judged, anonymised, scored, or reconciled.
---

# Model Output - substrate_workflow / case-3-misattribution (run 04)

## Condition

Benchmark version `locator-accuracy-v2-v1`, condition `substrate_workflow`, case `case-3-misattribution`, run 4 of 8. Real LM Studio model run: `gemma-4-31b-it-mlx`, seed 4063, on the frozen condition packet `sha256:a694ac7493d4b64ead768308356878698f24dc2a1ab770d853b4ebbd66f1eebe`.

## Output

The draft contains a lineage error: "normalization of deviance" is not attributed to James Reason in `BK-0044-card-002`. According to the provided brief, that concept is detailed in `BK-0042-card-001`.

**Corrected Note:**

Normalization of deviance is the organizational process where a group repeatedly encounters warning signs or performance departures and gradually treats them as acceptable, shifting the threshold of what is considered dangerous (`BK-0042-card-001`, Chapter 10). This allows an organization to operate under steadily degraded conditions while perceiving them as routine and safe. The process is driven by the working group's evolving culture, the surrounding professional culture, and "structural secrecy"—the bureaucratic partitioning of information that prevents separate warning signs from being recognized as a single trend (`BK-0042-card-001`, Chapter 10).
