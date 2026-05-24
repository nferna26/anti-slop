---
run_id: halo-evidence-vs-diagnosis-validation-v9-vanilla-long-prompt-04
created: 2026-05-24
eval_type: contradiction-preservation
case_id: halo-evidence-vs-diagnosis-validation-v9
benchmark_version: halo-evidence-vs-diagnosis-validation-v9-v1
model_condition: vanilla_long_prompt
run_number: 4
model_name: gemma-4-31b-it-mlx
model_id: gemma-4-31b-it-mlx
model_snapshot: LM Studio MLX 8-bit model id lmstudio-community/gemma-4-31B-it-MLX-8bit
runtime: LM Studio local OpenAI-compatible HTTP server; MLX runtime
provider: local
temperature: 0.7
top_p: 0.9
num_ctx: 32768
max_tokens: 1024
seed: 404
prompt_source: condition packet (vanilla_long_prompt) - frozen added material plus frozen Advisor prompt; see run-packet.md
prompt_sha256: 61d771e2bff7fd2e18be1d2999d0f601760656e3e69b4622989ca7bffd3aff8e
source_packet: a neutral equal-length filler plus transition, then the frozen Advisor prompt; no substrate artifact - see run-packet.md
source_packet_sha256: af424c072038c5043883f6cfe6433926f53b7b295e971021e271814b4cf97500
condition_packet_sha256: af424c072038c5043883f6cfe6433926f53b7b295e971021e271814b4cf97500
output_file: model-outputs/vanilla_long_prompt-04.md
judge_model_id: pending - judge receipts recorded separately under judge-packet
judge_prompt_sha256: pending - judge receipts recorded separately under judge-packet
judge_independence: pending - judge receipts recorded separately under judge-packet
raw_model_output_public_safe: true
---

# Model Output - vanilla_long_prompt (run 04)

## Condition

Benchmark version `halo-evidence-vs-diagnosis-validation-v9-v1`, condition `vanilla_long_prompt`, run 4 of 8. Real local-model run: `gemma-4-31b-it-mlx` via lmstudio, seed 404, on the frozen condition packet.

## Output

**Recommendation:** Run the Claim File Review.

**Why:** Your current success metrics are "entangled" and likely illusory. The expansion bookings are skewed by temporary pricing bundles, and the usage spike is driven by managers auditing closed files rather than adjusters managing active claims. Most critically, the "invisible churn" from regional carriers and the abandonment in the health-liability segment suggest a fundamental gap between the tool's output and the user's ability to defend that output to reviewers. You cannot scale or optimize (Usage Quality Sprint) a product if you do not know whether the core output is actually being accepted or rewritten. The Claim File Review provides the only ground-truth data on whether DraftPath is providing genuine value or merely appearing useful in a demo.

**Strongest Reason Against:** It is the slowest and most manual of the three proposed tests. Unlike the Usage Quality Sprint (automated tracking) or the Commercial Cleanroom (sales gating), this requires human labor to audit files and interview adjusters, which may feel too slow given the twelve-day budget window.

**Evidence that would change my mind:** If the "Commercial Cleanroom" results were to show that buyers are still enthusiastically signing expansion agreements at full price without the roadmap pitch or bundle discounts. That would prove the perceived value is high enough to sustain the business while you figure out the usage gaps in the background.
