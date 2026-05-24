---
run_id: halo-evidence-vs-diagnosis-validation-v12-famous-sources-supplied-06
created: 2026-05-24
eval_type: contradiction-preservation
case_id: halo-evidence-vs-diagnosis-validation-v12
benchmark_version: halo-evidence-vs-diagnosis-validation-v12-v1
model_condition: famous_sources_supplied
run_number: 6
model_name: gemma-4-31b-it-mlx:2
model_id: gemma-4-31b-it-mlx:2
model_snapshot: LM Studio MLX 8-bit model id lmstudio-community/gemma-4-31B-it-MLX-8bit; loaded_context_length 65536
runtime: LM Studio local OpenAI-compatible HTTP server; MLX runtime
provider: local
temperature: 0.7
top_p: 0.9
num_ctx: 65536
max_tokens: 2048
seed: 602
prompt_source: condition packet (famous_sources_supplied) - frozen added material plus frozen Advisor prompt; see run-packet.md
prompt_sha256: 81621976eaf302301d88434e895bffe7f264ddbe9d86bbb0dd82120c2f65f2aa
source_packet: a name-level list of famous source titles and authors, then the frozen Advisor prompt; no benefits cases, summaries, source cards, or tension card - see run-packet.md
source_packet_sha256: fbda9621700ea5a031af698b8700a95ac925370d84a60c86c1d7bce543e8cc3b
condition_packet_sha256: fbda9621700ea5a031af698b8700a95ac925370d84a60c86c1d7bce543e8cc3b
output_file: model-outputs/famous_sources_supplied-06.md
judge_model_id: pending - judge receipts recorded separately under judge-packet
judge_prompt_sha256: pending - judge receipts recorded separately under judge-packet
judge_independence: pending - judge receipts recorded separately under judge-packet
raw_model_output_public_safe: true
---

# Model Output - famous_sources_supplied (run 06)

## Condition

Benchmark version `halo-evidence-vs-diagnosis-validation-v12-v1`, condition `famous_sources_supplied`, run 6 of 8. Real local-model run: `gemma-4-31b-it-mlx:2` via lmstudio, seed 602, on the frozen condition packet.

## Output

**Recommendation:** Run the Case Evidence Review.

**Why:** Your current success is "entangled," meaning your lagging indicators (expansion bookings, shortened sales cycles) are likely being driven by sales incentives and the "Halo Effect" of a new roadmap pitch rather than actual product value. The usage data is equally deceptive: high frequency is driven by managers (not the primary users) and initial novelty, while the public sector reveals a critical failure in "explainability."

Scaling now would be betting on a facade. The Adoption Quality Sprint tracks *behavior* (return rates), but not *value* (whether the plan was actually used to solve a problem). The Demand Cleanroom tests *willingness to pay*, but not *product efficacy*. Only the Case Evidence Review identifies the "Jobs to be Done" (per Christensen) by revealing exactly where the software provides a useful output versus where it is being manually overridden or ignored. You must determine if PlanPilot is a functional tool or a sales ornament before committing next year's budget to scaling it.

**The strongest reason against this:** It is the slowest and most manual of the three validation options. In a twelve-day window before the board locks the budget, this qualitative deep dive provides less "hard data" for a slide deck than a Demand Cleanroom or an Adoption Sprint, potentially making the product team look hesitant or unable to quantify success to a bullish executive team.

**Observable evidence that would change my mind:** If the "wrong recommendation" tickets in the training channel showed a statistically significant decline across all segments (including public sector) and were accompanied by verified logs showing that front-line analysts are sticking with the tool *after* the first two days of rollout without manager intervention. This would suggest the "explainability" gap is a training issue rather than a fundamental product failure, shifting the priority toward the Adoption Quality Sprint.
