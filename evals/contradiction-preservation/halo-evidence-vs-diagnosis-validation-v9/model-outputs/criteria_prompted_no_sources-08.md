---
run_id: halo-evidence-vs-diagnosis-validation-v9-criteria-prompted-no-sources-08
created: 2026-05-24
eval_type: contradiction-preservation
case_id: halo-evidence-vs-diagnosis-validation-v9
benchmark_version: halo-evidence-vs-diagnosis-validation-v9-v1
model_condition: criteria_prompted_no_sources
run_number: 8
model_name: gemma-4-31b-it-mlx
model_id: gemma-4-31b-it-mlx
model_snapshot: LM Studio MLX 8-bit model id lmstudio-community/gemma-4-31B-it-MLX-8bit
runtime: LM Studio local OpenAI-compatible HTTP server; MLX runtime
provider: local
temperature: 0.7
top_p: 0.9
num_ctx: 32768
max_tokens: 1024
seed: 806
prompt_source: condition packet (criteria_prompted_no_sources) - frozen added material plus frozen Advisor prompt; see run-packet.md
prompt_sha256: 61d771e2bff7fd2e18be1d2999d0f601760656e3e69b4622989ca7bffd3aff8e
source_packet: an abstract evidence-quality criteria reminder, then the frozen Advisor prompt; no source names, source cards, or case-specific answer hint - see run-packet.md
source_packet_sha256: 99e91b34c6105209d4266fed0bcb0ab798bcedfae3a4ab5516c3c91fc972adaa
condition_packet_sha256: 99e91b34c6105209d4266fed0bcb0ab798bcedfae3a4ab5516c3c91fc972adaa
output_file: model-outputs/criteria_prompted_no_sources-08.md
judge_model_id: pending - judge receipts recorded separately under judge-packet
judge_prompt_sha256: pending - judge receipts recorded separately under judge-packet
judge_independence: pending - judge receipts recorded separately under judge-packet
raw_model_output_public_safe: true
---

# Model Output - criteria_prompted_no_sources (run 08)

## Condition

Benchmark version `halo-evidence-vs-diagnosis-validation-v9-v1`, condition `criteria_prompted_no_sources`, run 8 of 8. Real local-model run: `gemma-4-31b-it-mlx` via lmstudio, seed 806, on the frozen condition packet.

## Output

**Recommendation:** Run the Claim File Review.

**Reasoning:** The current success indicators are heavily contaminated. Expansion bookings were driven by pricing incentives rather than product value, and positive customer sentiment was elicited via a forward-looking roadmap pitch rather than current utility. Usage data is misleading; the increase is driven by managers performing retrospective audits, while front-line adjusters—the primary users—demonstrate a pattern of abandonment. The decrease in "wrong recommendation" tickets is likely a reporting shift to training channels rather than an improvement in accuracy.

The Claim File Review is the only intervention that prioritizes disconfirming evidence by looking at actual claim outcomes rather than proxy metrics. It reveals whether the software is actually solving a problem (accepted suggestions) or creating friction (overridden/unexplainable suggestions). In contrast, the Usage Quality Sprint tracks activity without quality, and the Commercial Cleanroom tests sales tactics rather than product-market fit.

**Strongest reason against:** This approach is slow and qualitative. It will not provide a statistically significant sample size across all segments in twelve days, potentially leaving the CEO with "anecdotal" evidence while Sales argues that the bundle pricing is a proven revenue lever.

**Evidence that would change my mind:** If you discover that the "unexplainable" actions in health-liability are not due to product failure, but are instead a result of adjusters lacking basic training on the existing tool. If evidence shows that users who override suggestions still complete their workflows 20% faster than those not using the tool, I would shift the recommendation to scaling DraftPath broadly.
