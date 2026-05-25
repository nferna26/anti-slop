---
run_id: halo-evidence-vs-diagnosis-validation-v12-criteria-prompted-no-sources-05
created: 2026-05-24
eval_type: contradiction-preservation
case_id: halo-evidence-vs-diagnosis-validation-v12
benchmark_version: halo-evidence-vs-diagnosis-validation-v12-v1
model_condition: criteria_prompted_no_sources
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
seed: 506
prompt_source: condition packet (criteria_prompted_no_sources) - frozen added material plus frozen Advisor prompt; see run-packet.md
prompt_sha256: 81621976eaf302301d88434e895bffe7f264ddbe9d86bbb0dd82120c2f65f2aa
source_packet: an abstract evidence-quality criteria reminder, then the frozen Advisor prompt; no source names, source cards, or case-specific answer hint - see run-packet.md
source_packet_sha256: eedcb93e6e1ac3648b936a1b5b4926243f86d4779861ecb7569972e407df3b14
condition_packet_sha256: eedcb93e6e1ac3648b936a1b5b4926243f86d4779861ecb7569972e407df3b14
output_file: model-outputs/criteria_prompted_no_sources-05.md
judge_model_id: pending - judge receipts recorded separately under judge-packet
judge_prompt_sha256: pending - judge receipts recorded separately under judge-packet
judge_independence: pending - judge receipts recorded separately under judge-packet
raw_model_output_public_safe: true
---

# Model Output - criteria_prompted_no_sources (run 05)

## Condition

Benchmark version `halo-evidence-vs-diagnosis-validation-v12-v1`, condition `criteria_prompted_no_sources`, run 5 of 8. Real local-model run: `gemma-4-31b-it-mlx:2` via lmstudio, seed 506, on the frozen condition packet.

## Output

**Recommendation**

Run the Demand Cleanroom.

**Reasoning**

The current growth indicators are heavily contaminated by temporary financial incentives and sales messaging rather than product utility. The 16% rise in expansion bookings is tied to bundle pricing, and the "enthusiastic" feedback was collected after sales promised a future roadmap, creating a confirmation bias.

The usage data is misleading: high activity is driven by managers practicing on closed samples (non-productive use) and analysts who abandon the tool once initial novelty fades or when they face internal scrutiny. The decline in "wrong recommendation" tickets is likely an artifact of users shifting their complaints to training channels, hiding the actual error rate.

The Case Evidence Review would show that analysts are overriding the tool, but it wouldn't prove if customers would pay for it without a discount. The Adoption Quality Sprint focuses on "cleaner enablement," which assumes the product is fundamentally valuable and only needs better training—a dangerous assumption given that public-sector users cannot explain the logic to reviewers. Only the Demand Cleanroom isolates whether there is organic commercial demand for PlanPilot's current state, stripped of pricing lures and future promises.

**Strongest Reason Against**

This intervention creates immediate commercial risk. By withholding bundle pricing and the roadmap pitch, you may intentionally slow down current quarter velocity or trigger objections in a high-stakes renewal window, potentially upsetting the sales team and creating a temporary dip in expansion bookings.

**Evidence that would change this recommendation**

If the Case Evidence Review were modified to include a "willingness-to-pay" survey for those who accepted the suggestions without overrides, and that data showed a high percentage of analysts would personally advocate for the budget regardless of bundle pricing, I would pivot to the Case Evidence Review. This would prove the value is realized at the user level, making the sales-tactic test redundant.
