---
run_id: halo-evidence-vs-diagnosis-validation-v10-criteria-prompted-no-sources-03
created: 2026-05-24
eval_type: contradiction-preservation
case_id: halo-evidence-vs-diagnosis-validation-v10
benchmark_version: halo-evidence-vs-diagnosis-validation-v10-v1
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
prompt_sha256: 61d771e2bff7fd2e18be1d2999d0f601760656e3e69b4622989ca7bffd3aff8e
source_packet: an abstract evidence-quality criteria reminder, then the frozen Advisor prompt; no source names, source cards, or case-specific answer hint - see run-packet.md
source_packet_sha256: 99e91b34c6105209d4266fed0bcb0ab798bcedfae3a4ab5516c3c91fc972adaa
condition_packet_sha256: 99e91b34c6105209d4266fed0bcb0ab798bcedfae3a4ab5516c3c91fc972adaa
output_file: model-outputs/criteria_prompted_no_sources-03.md
judge_model_id: pending - judge receipts recorded separately under judge-packet
judge_prompt_sha256: pending - judge receipts recorded separately under judge-packet
judge_independence: pending - judge receipts recorded separately under judge-packet
raw_model_output_public_safe: true
---

# Model Output - criteria_prompted_no_sources (run 03)

## Condition

Benchmark version `halo-evidence-vs-diagnosis-validation-v10-v1`, condition `criteria_prompted_no_sources`, run 3 of 8. Real local-model run: `gemma-4-31b-it-mlx:2` via lmstudio, seed 306, on the frozen condition packet.

## Output

**Recommendation:** Run the Claim File Review.

**Reasoning:** The current evidence of success is heavily contaminated. Expansion bookings are tied to temporary pricing incentives rather than perceived value, and positive customer sentiment was elicited by sales teams promising future roadmap improvements. Usage metrics are misleading; high activity is driven by managers performing retrospective audits rather than adjusters executing live workflows. Furthermore, the drop in "wrong recommendation" tickets is likely an artifact of users misclassifying bugs as training requests.

The Claim File Review is the only intervention that targets the core risk: a gap between proposed actions and actual utility. Unlike the Usage Quality Sprint, which tracks *if* people click (behavior), or the Commercial Cleanroom, which tracks *if* people pay (financials), this review examines *what* happened inside the claim file (outcome). It will reveal whether the software is actually solving a problem or if adjusters are simply performing "compliance theater" for their managers.

**Strongest Reason Against:** This approach is slow and labor-intensive compared to automated analytics. It provides a snapshot of historical data rather than a real-time signal of market demand, potentially delaying the decision to scale or pivot until after the budget is locked.

**Evidence that would change my mind:** If you discover that the regional carriers removing DraftPath are doing so specifically because of a lack of training/enablement—rather than a failure of the tool's logic or an inability to explain actions to reviewers—I would shift the recommendation to the Usage Quality Sprint. This would indicate the product is valuable but the delivery mechanism is broken, making behavioral tracking and enablement more urgent than a quality audit.
