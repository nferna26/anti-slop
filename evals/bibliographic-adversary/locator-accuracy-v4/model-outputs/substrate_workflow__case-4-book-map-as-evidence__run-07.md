---
run_id: locator-accuracy-v4-substrate-workflow-case-4-book-map-as-evidence-run-07
created: 2026-05-29
eval_type: bibliographic-adversary
case_id: locator-accuracy-v4
case_key: case-4-book-map-as-evidence
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
seed: 7064
initial_seed: 7064
retry_reason: none
prompt_source: frozen condition packet substrate_workflow / case-4-book-map-as-evidence; see run-packet.md
prompt_sha256: a16d4e9133e0bbcadf6870d5417305e5d6fad019f9e093d05ff7640b45e1f12c
source_packet: frozen condition packet assembled from run-packet.md recipes
source_packet_sha256: 29d6d8d908f45ca388bed86b3f98ca33bec63a4618187a0a2153a77cfe681e3d
condition_packet_sha256: 29d6d8d908f45ca388bed86b3f98ca33bec63a4618187a0a2153a77cfe681e3d
substrate_brief_sha256: b0c8b97206715147b5f3b5c43e064d08225c6c6bdc7c80b058d78c2cf7e990d8
output_body_sha256: 60fc8c4f6f26dd2cb5daa1802561d6a0a90cdb63cfcd611ff49d347e32905d41
output_file: model-outputs/substrate_workflow__case-4-book-map-as-evidence__run-07.md
local_output_file: local-only/runs/locator-accuracy-v4-v1/outputs/substrate_workflow__case-4-book-map-as-evidence__run-07.md
judge_model_id: pending - not yet judged
judge_prompt_sha256: pending - not yet judged
judge_independence: pending - not yet judged
raw_model_output_public_safe: true
operator_notes: Real model run via LM Studio OpenAI-compatible local server, not an in-session simulation. Run 7 of 8 for substrate_workflow / case-4-book-map-as-evidence under frozen benchmark locator-accuracy-v4-v1. The condition packet sha256 was verified before generation. Generation wall time 14.0s; finish_reason stop; prompt_tokens 4730; completion_tokens 186; total_tokens 4916. Initial seed 7064; actual seed 7064; retry_reason none. The verbatim final answer is reproduced below and is what future condition-blind judges will score. A model output is a test artifact, never an authority and never citable as a source. The case is not yet judged, anonymised, scored, or reconciled.
---

# Model Output - substrate_workflow / case-4-book-map-as-evidence (run 07)

## Condition

Benchmark version `locator-accuracy-v4-v1`, condition `substrate_workflow`, case `case-4-book-map-as-evidence`, run 7 of 8. Real LM Studio model run: `gemma-4-31b-it-mlx`, seed 7064, on the frozen condition packet `sha256:29d6d8d908f45ca388bed86b3f98ca33bec63a4618187a0a2153a77cfe681e3d`.

## Output

Corrected note:

Andy Grove proposes that a manager's output is not their own personal activity, but the output of the organizational units for which the manager is responsible (including directly supervised units and neighboring units they influence).

**Supported Lineage:**
- `BK-0002-card-001`, Chapter 3: A manager's output is the output of the organizational units the manager is responsible for, rather than the manager's own activity.

**Corrections:**
- Removed reference to `corpus/book-maps/BK-0002.md`; book maps are discovery aids and not evidence units.
- Removed "Part II" divider locator; per the reviewed source card, part dividers are not used as locators for this source.
- Corrected the claim to specify that output includes both supervised and influenced units, as per the reviewed card.
