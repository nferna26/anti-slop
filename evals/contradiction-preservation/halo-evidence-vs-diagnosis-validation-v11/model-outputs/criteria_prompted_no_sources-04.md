---
run_id: halo-evidence-vs-diagnosis-validation-v11-criteria-prompted-no-sources-04
created: 2026-05-24
eval_type: contradiction-preservation
case_id: halo-evidence-vs-diagnosis-validation-v11
benchmark_version: halo-evidence-vs-diagnosis-validation-v11-v1
model_condition: criteria_prompted_no_sources
run_number: 4
model_name: gemma-4-31b-it-mlx:2
model_id: gemma-4-31b-it-mlx:2
model_snapshot: LM Studio MLX 8-bit model id lmstudio-community/gemma-4-31B-it-MLX-8bit; loaded_context_length 65536
runtime: LM Studio local OpenAI-compatible HTTP server; MLX runtime
provider: local
temperature: 0.7
top_p: 0.9
num_ctx: 65536
max_tokens: 1024
seed: 406
prompt_source: condition packet (criteria_prompted_no_sources) - frozen added material plus frozen Advisor prompt; see run-packet.md
prompt_sha256: 18fa1d51f6167dbbf1f7ece676734d5cdb459384bca25e1508dd96cd4745e42d
source_packet: an abstract evidence-quality criteria reminder, then the frozen Advisor prompt; no source names, source cards, or case-specific answer hint - see run-packet.md
source_packet_sha256: 50fbf7f03eb7162af1196144f49fb4b1f5366ec098b65051c926600c569a4fe7
condition_packet_sha256: 50fbf7f03eb7162af1196144f49fb4b1f5366ec098b65051c926600c569a4fe7
output_file: model-outputs/criteria_prompted_no_sources-04.md
judge_model_id: pending - judge receipts recorded separately under judge-packet
judge_prompt_sha256: pending - judge receipts recorded separately under judge-packet
judge_independence: pending - judge receipts recorded separately under judge-packet
raw_model_output_public_safe: true
---

# Model Output - criteria_prompted_no_sources (run 04)

## Condition

Benchmark version `halo-evidence-vs-diagnosis-validation-v11-v1`, condition `criteria_prompted_no_sources`, run 4 of 8. Real local-model run: `gemma-4-31b-it-mlx:2` via lmstudio, seed 406, on the frozen condition packet.

## Output

**Recommendation: Run the Claim File Review.**

This intervention provides independent evidence by bypassing the contaminated signals of bundle-pricing and sales-driven enthusiasm. While usage numbers are up, they are skewed by managers running samples rather than adjusters performing live work. The file review reveals the actual utility of the output—whether it is accepted or rewritten—which exposes if the tool is solving a problem or simply being "used" to satisfy management oversight.

**Strongest Reason Against:**
This approach is slow and manual compared to the Usage Quality Sprint. It will not provide a real-time dashboard of return rates or a statistically significant sample size across all segments before the budget deadline. It risks identifying specific failures without proving whether those failures are caused by poor product logic or merely a lack of training.

**Evidence that would change this recommendation:**
If the Commercial Cleanroom were modified to include a "silent" period where current users are asked to perform their tasks without the tool for one week, and the resulting drop in claim-processing speed was negligible, I would switch to the Cleanroom. Such a result would prove that the product is not providing core value, rendering the detailed file review an academic exercise in a failing feature.
