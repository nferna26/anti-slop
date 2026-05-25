---
run_id: halo-evidence-vs-diagnosis-validation-v12-famous-sources-supplied-04
created: 2026-05-24
eval_type: contradiction-preservation
case_id: halo-evidence-vs-diagnosis-validation-v12
benchmark_version: halo-evidence-vs-diagnosis-validation-v12-v1
model_condition: famous_sources_supplied
run_number: 4
model_name: gemma-4-31b-it-mlx:2
model_id: gemma-4-31b-it-mlx:2
model_snapshot: LM Studio MLX 8-bit model id lmstudio-community/gemma-4-31B-it-MLX-8bit; loaded_context_length 65536
runtime: LM Studio local OpenAI-compatible HTTP server; MLX runtime
provider: local
temperature: 0.7
top_p: 0.9
num_ctx: 65536
max_tokens: 2048
seed: 402
prompt_source: condition packet (famous_sources_supplied) - frozen added material plus frozen Advisor prompt; see run-packet.md
prompt_sha256: 81621976eaf302301d88434e895bffe7f264ddbe9d86bbb0dd82120c2f65f2aa
source_packet: a name-level list of famous source titles and authors, then the frozen Advisor prompt; no benefits cases, summaries, source cards, or tension card - see run-packet.md
source_packet_sha256: fbda9621700ea5a031af698b8700a95ac925370d84a60c86c1d7bce543e8cc3b
condition_packet_sha256: fbda9621700ea5a031af698b8700a95ac925370d84a60c86c1d7bce543e8cc3b
output_file: model-outputs/famous_sources_supplied-04.md
judge_model_id: pending - judge receipts recorded separately under judge-packet
judge_prompt_sha256: pending - judge receipts recorded separately under judge-packet
judge_independence: pending - judge receipts recorded separately under judge-packet
raw_model_output_public_safe: true
---

# Model Output - famous_sources_supplied (run 04)

## Condition

Benchmark version `halo-evidence-vs-diagnosis-validation-v12-v1`, condition `famous_sources_supplied`, run 4 of 8. Real local-model run: `gemma-4-31b-it-mlx:2` via lmstudio, seed 402, on the frozen condition packet.

## Output

**Recommendation:** Run the Case Evidence Review.

**Why:** Your current success is "entangled," meaning your lagging indicators (expansion bookings and shortened sales cycles) are likely being driven by temporary pricing incentives and the *promise* of a roadmap rather than the actual *value* of the product. The usage data is equally deceptive: high frequency among managers (who aren't the primary users) and early-stage spikes among analysts who then abandon the tool.

The core risk is a "value gap"—specifically, the inability of analysts to explain recommendations to reviewers (critical in public sector) and a reliance on manual notes. The Adoption Quality Sprint tracks *if* they use it, and the Demand Cleanroom tracks *if* they will pay for it, but neither explains *why* it is failing in the workflow. The Case Evidence Review is the only option that provides a ground-truth audit of the product's utility. By seeing exactly what was overridden or rewritten, you can determine if PlanPilot is a genuine productivity booster or merely a "drafting tool" that creates more work for the analyst to fix.

**The strongest reason against it:** This is a qualitative, slow-velocity approach that does not provide the "hard" financial or behavioral data (like churn or conversion rates) that a Board typically demands during budget locking. It risks being viewed as "academic" while the Sales team is currently winning deals based on the product's perceived momentum.

**Observable evidence that would change my mind:** If the "Demand Cleanroom" results were to show that expansion bookings remain high and renewal objections remain low even *without* the bundle pricing and roadmap pitches. This would prove that the market value is decoupled from the workflow friction, suggesting that the "perceived value" is high enough to sustain growth regardless of the internal analyst struggle.
