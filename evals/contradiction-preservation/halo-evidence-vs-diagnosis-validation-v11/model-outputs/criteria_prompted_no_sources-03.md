---
run_id: halo-evidence-vs-diagnosis-validation-v11-criteria-prompted-no-sources-03
created: 2026-05-24
eval_type: contradiction-preservation
case_id: halo-evidence-vs-diagnosis-validation-v11
benchmark_version: halo-evidence-vs-diagnosis-validation-v11-v1
model_condition: criteria_prompted_no_sources
run_number: 3
model_name: gemma-4-31b-it-mlx:2
model_id: gemma-4-31b-it-mlx:2
model_snapshot: LM Studio MLX 8-bit model id lmstudio-community/gemma-4-31B-it-MLX-8bit; loaded_context_length 65536
runtime: LM Studio local OpenAI-compatible HTTP server; MLX runtime
provider: local
temperature: 0.7
top_p: 0.9
num_ctx: 65536
max_tokens: 1024
seed: 306
prompt_source: condition packet (criteria_prompted_no_sources) - frozen added material plus frozen Advisor prompt; see run-packet.md
prompt_sha256: 18fa1d51f6167dbbf1f7ece676734d5cdb459384bca25e1508dd96cd4745e42d
source_packet: an abstract evidence-quality criteria reminder, then the frozen Advisor prompt; no source names, source cards, or case-specific answer hint - see run-packet.md
source_packet_sha256: 50fbf7f03eb7162af1196144f49fb4b1f5366ec098b65051c926600c569a4fe7
condition_packet_sha256: 50fbf7f03eb7162af1196144f49fb4b1f5366ec098b65051c926600c569a4fe7
output_file: model-outputs/criteria_prompted_no_sources-03.md
judge_model_id: pending - judge receipts recorded separately under judge-packet
judge_prompt_sha256: pending - judge receipts recorded separately under judge-packet
judge_independence: pending - judge receipts recorded separately under judge-packet
raw_model_output_public_safe: true
---

# Model Output - criteria_prompted_no_sources (run 03)

## Condition

Benchmark version `halo-evidence-vs-diagnosis-validation-v11-v1`, condition `criteria_prompted_no_sources`, run 3 of 8. Real local-model run: `gemma-4-31b-it-mlx:2` via lmstudio, seed 306, on the frozen condition packet.

## Output

**Recommendation:** Run the Claim File Review.

**Reasoning:** The current growth metrics are contaminated by financial incentives (bundle pricing) and sales narratives (roadmap promises). Usage data is misleading because it captures manager-led training exercises rather than adjuster productivity. The Claim File Review is the only intervention that isolates actual utility by examining the final output—the claim file. It reveals whether the software is solving a problem or being bypassed, and specifically tests if the "explainability" gap in regulated segments is a systemic failure or a training issue. In contrast, the Usage Quality Sprint tracks activity without quality, and the Commercial Cleanroom tests pricing elasticity rather than product value.

**Strongest Reason Against:** This approach is a lagging indicator and small-sample study. It will not provide the statistically significant "proof" of scale that the board likely wants for a budget lock, and it may uncover negative truths (high override rates) that undermine the current positive momentum with leadership.

**Evidence That Would Change My Mind:** If you discover that front-line adjusters in non-regulated segments are not just using the tool for two days, but are actually incorporating the proposed actions into their final claim files without overrides, the need for a deep file review vanishes. In that case, I would switch to the Commercial Cleanroom to determine if the growth is driven by product value or merely by the temporary bundle pricing.
