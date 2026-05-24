---
run_id: halo-evidence-vs-diagnosis-validation-v12-famous-sources-supplied-05
created: 2026-05-24
eval_type: contradiction-preservation
case_id: halo-evidence-vs-diagnosis-validation-v12
benchmark_version: halo-evidence-vs-diagnosis-validation-v12-v1
model_condition: famous_sources_supplied
run_number: 5
model_name: gemma-4-31b-it-mlx:2
model_id: gemma-4-31b-it-mlx:2
model_snapshot: LM Studio MLX 8-bit model id lmstudio-community/gemma-4-31B-it-MLX-8bit; loaded_context_length 65536
runtime: LM Studio local OpenAI-compatible HTTP server; MLX runtime
provider: local
temperature: 0.7
top_p: 0.9
num_ctx: 65536
max_tokens: 2048
seed: 502
prompt_source: condition packet (famous_sources_supplied) - frozen added material plus frozen Advisor prompt; see run-packet.md
prompt_sha256: 81621976eaf302301d88434e895bffe7f264ddbe9d86bbb0dd82120c2f65f2aa
source_packet: a name-level list of famous source titles and authors, then the frozen Advisor prompt; no benefits cases, summaries, source cards, or tension card - see run-packet.md
source_packet_sha256: fbda9621700ea5a031af698b8700a95ac925370d84a60c86c1d7bce543e8cc3b
condition_packet_sha256: fbda9621700ea5a031af698b8700a95ac925370d84a60c86c1d7bce543e8cc3b
output_file: model-outputs/famous_sources_supplied-05.md
judge_model_id: pending - judge receipts recorded separately under judge-packet
judge_prompt_sha256: pending - judge receipts recorded separately under judge-packet
judge_independence: pending - judge receipts recorded separately under judge-packet
raw_model_output_public_safe: true
---

# Model Output - famous_sources_supplied (run 05)

## Condition

Benchmark version `halo-evidence-vs-diagnosis-validation-v12-v1`, condition `famous_sources_supplied`, run 5 of 8. Real local-model run: `gemma-4-31b-it-mlx:2` via lmstudio, seed 502, on the frozen condition packet.

## Output

I recommend that you commit to the **Case Evidence Review**.

### Why this recommendation?
Your current success is "entangled," meaning the positive lagging indicators (expansion bookings, shortened sales cycles) are likely being driven by sales incentives and roadmap promises rather than actual product value. You have a critical "signal" problem:
1. **Financials are skewed:** The expansion is tied to temporary bundle pricing (price-driven, not value-driven).
2. **Usage is misleading:** High frequency is driven by managers practicing on closed samples, not analysts solving live problems.
3. **The "Value Gap" is visible:** Analysts abandon the tool when they cannot explain the logic to reviewers (the "black box" problem).

The *Adoption Quality Sprint* measures *if* people use it, and the *Demand Cleanroom* measures if people *buy* it, but neither tells you *why* the product is failing in the actual workflow. The Case Evidence Review is the only option that audits the "job to be done." By identifying exactly which suggestions are overridden or impossible to explain, you move from guessing about "enablement" to identifying specific product failures in the logic engine.

### The strongest reason against it
This approach is slow and qualitative. It provides a "snapshot" of past behavior rather than a real-time experimental result. While you are reviewing case files, the Sales team may continue to sell a version of PlanPilot that doesn't actually work for the end-user, potentially increasing the "churn debt" you will have to pay when those regional administrators' procurement windows finally close.

### Observable evidence that would change my mind
I would switch to the **Demand Cleanroom** if you discovered that the "impossible to explain" feedback was limited strictly to the public sector, while private-sector analysts showed high "acceptance/no-override" rates in their workflows. If the product is fundamentally sound for 80% of your market and the only issue is a sales-led pricing bubble, you need to validate commercial demand (the Cleanroom) rather than refine the product logic.
