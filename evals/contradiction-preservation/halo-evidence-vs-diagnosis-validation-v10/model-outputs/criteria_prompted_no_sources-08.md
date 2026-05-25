---
run_id: halo-evidence-vs-diagnosis-validation-v10-criteria-prompted-no-sources-08
created: 2026-05-24
eval_type: contradiction-preservation
case_id: halo-evidence-vs-diagnosis-validation-v10
benchmark_version: halo-evidence-vs-diagnosis-validation-v10-v1
model_condition: criteria_prompted_no_sources
run_number: 8
model_name: gemma-4-31b-it-mlx:2
model_id: gemma-4-31b-it-mlx:2
model_snapshot: LM Studio MLX 8-bit model id lmstudio-community/gemma-4-31B-it-MLX-8bit; loaded_context_length 65536
runtime: LM Studio local OpenAI-compatible HTTP server; MLX runtime
provider: local
temperature: 0.7
top_p: 0.9
num_ctx: 65536
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

Benchmark version `halo-evidence-vs-diagnosis-validation-v10-v1`, condition `criteria_prompted_no_sources`, run 8 of 8. Real local-model run: `gemma-4-31b-it-mlx:2` via lmstudio, seed 806, on the frozen condition packet.

## Output

**Recommendation:** Run the Commercial Cleanroom.

**Reasoning:** The current growth metrics are contaminated by temporary pricing bundles and sales pitches that promise future capabilities, making it impossible to know if customers are buying the existing product or a promised vision. The Usage Quality Sprint relies on event tracking that already shows adjusters abandon the tool after two days; more dashboards will not explain why they leave. The Claim File Review provides a snapshot of utility but fails to address whether that utility is sufficient to drive independent procurement. The Commercial Cleanroom is the only intervention that removes the financial and psychological incentives (bundle pricing and roadmap promises) to isolate whether DraftPath has standalone commercial value.

**Strongest Reason Against:** This approach risks immediate revenue loss and could create friction with the sales team during a period of perceived momentum, potentially slowing expansion bookings in the short term to gain long-term clarity.

**Evidence that would change this recommendation:** If you discover that the regional carriers planning to remove DraftPath are doing so specifically because of a lack of "explainability" in the health-liability segment, rather than a general lack of value. In that case, I would displace the Commercial Cleanroom with a modified "Narrow Plan" focused on regulated health-liability workflows, sacrificing broad market validation to solve the specific regulatory blocker.
