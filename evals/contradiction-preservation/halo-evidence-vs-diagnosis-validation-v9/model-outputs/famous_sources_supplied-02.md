---
run_id: halo-evidence-vs-diagnosis-validation-v9-famous-sources-supplied-02
created: 2026-05-24
eval_type: contradiction-preservation
case_id: halo-evidence-vs-diagnosis-validation-v9
benchmark_version: halo-evidence-vs-diagnosis-validation-v9-v1
model_condition: famous_sources_supplied
run_number: 2
model_name: gemma-4-31b-it-mlx
model_id: gemma-4-31b-it-mlx
model_snapshot: LM Studio MLX 8-bit model id lmstudio-community/gemma-4-31B-it-MLX-8bit
runtime: LM Studio local OpenAI-compatible HTTP server; MLX runtime
provider: local
temperature: 0.7
top_p: 0.9
num_ctx: 32768
max_tokens: 1024
seed: 202
prompt_source: condition packet (famous_sources_supplied) - frozen added material plus frozen Advisor prompt; see run-packet.md
prompt_sha256: 61d771e2bff7fd2e18be1d2999d0f601760656e3e69b4622989ca7bffd3aff8e
source_packet: a name-level list of famous source titles and authors, then the frozen Advisor prompt; no claims, summaries, source cards, or tension card - see run-packet.md
source_packet_sha256: d057ad83d3f7bf7e5568fa060310fc46d54ebd76e09ae17c88d4f64128eb21dd
condition_packet_sha256: d057ad83d3f7bf7e5568fa060310fc46d54ebd76e09ae17c88d4f64128eb21dd
output_file: model-outputs/famous_sources_supplied-02.md
judge_model_id: pending - judge receipts recorded separately under judge-packet
judge_prompt_sha256: pending - judge receipts recorded separately under judge-packet
judge_independence: pending - judge receipts recorded separately under judge-packet
raw_model_output_public_safe: true
---

# Model Output - famous_sources_supplied (run 02)

## Condition

Benchmark version `halo-evidence-vs-diagnosis-validation-v9-v1`, condition `famous_sources_supplied`, run 2 of 8. Real local-model run: `gemma-4-31b-it-mlx` via lmstudio, seed 202, on the frozen condition packet.

## Output

**Recommendation:** Run the Claim File Review.

**Why:** Your current success is an illusion created by "entangled" evidence. You have a classic gap between *commercial signals* (expansion bookings driven by bundle pricing and sales pitches) and *product value* (adjusters abandoning the tool or using it only under managerial surveillance). The Usage Quality Sprint measures *how much* people use the tool, but not *why* or if it is actually solving the problem. The Commercial Cleanroom measures *willingness to pay*, but not *product-market fit*.

The Claim File Review is the only option that addresses the core risk: that DraftPath provides "correct" recommendations (fewer wrong-recommendation tickets) that are nonetheless unusable in a professional workflow (impossible to explain to reviewers). By analyzing the actual delta between a DraftPath suggestion and the final action taken on a file, you determine if the product is providing genuine utility or merely acting as a template that adjusters are manually correcting. This evidence is critical before scaling or narrowing the segment, as it reveals whether the problem is a lack of "enablement" (training) or a fundamental failure in the product's logic.

**The strongest reason against it:** It is slow and labor-intensive compared to the Usage Quality Sprint. By the time you manually review claim files and interview adjusters, the board's twelve-day window will have closed, and you may lack a "hard" quantitative metric (like a return-rate dashboard) to justify the budget to an executive team currently intoxicated by expansion bookings.

**Observable evidence that would change my mind:** If the "training channel" support tickets revealed a specific, easily fixable UI/UX friction point—rather than a conceptual failure to explain the "why" behind a recommendation—I would switch to the Usage Quality Sprint. If the problem is purely "how to use the button," quantitative tracking suffices; if the problem is "the output is indefensible to a regulator," only the Claim File Review will find it.
