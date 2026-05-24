---
run_id: halo-evidence-vs-diagnosis-validation-v12-substrate-workflow-04
created: 2026-05-24
eval_type: contradiction-preservation
case_id: halo-evidence-vs-diagnosis-validation-v12
benchmark_version: halo-evidence-vs-diagnosis-validation-v12-v1
model_condition: substrate_workflow
run_number: 4
model_name: gemma-4-31b-it-mlx:2
model_id: gemma-4-31b-it-mlx:2
model_snapshot: LM Studio MLX 8-bit model id lmstudio-community/gemma-4-31B-it-MLX-8bit; loaded_context_length 65536
runtime: LM Studio local OpenAI-compatible HTTP server; MLX runtime
provider: local
temperature: 0.7
top_p: 0.9
num_ctx: 65536
max_tokens: 2048
seed: 403
prompt_source: condition packet (substrate_workflow) - frozen added material plus frozen Advisor prompt; see run-packet.md
prompt_sha256: 81621976eaf302301d88434e895bffe7f264ddbe9d86bbb0dd82120c2f65f2aa
source_packet: a substrate preamble plus the full public-safe text of three reviewed source cards, then the frozen Advisor prompt - see run-packet.md
source_packet_sha256: b6cd135fd92e629c778a8282ec7993f44f89675e5f6dceea2232399cd10f2424
condition_packet_sha256: b6cd135fd92e629c778a8282ec7993f44f89675e5f6dceea2232399cd10f2424
output_file: model-outputs/substrate_workflow-04.md
judge_model_id: pending - judge receipts recorded separately under judge-packet
judge_prompt_sha256: pending - judge receipts recorded separately under judge-packet
judge_independence: pending - judge receipts recorded separately under judge-packet
raw_model_output_public_safe: true
---

# Model Output - substrate_workflow (run 04)

## Condition

Benchmark version `halo-evidence-vs-diagnosis-validation-v12-v1`, condition `substrate_workflow`, run 4 of 8. Real local-model run: `gemma-4-31b-it-mlx:2` via lmstudio, seed 403, on the frozen condition packet.

## Output

I recommend the **Demand Cleanroom**.

### The Recommendation: Demand Cleanroom
You should recommend the Demand Cleanroom to the CEO. This is the only option that isolates whether your strong quarter was driven by product value or by temporary financial incentives and sales narratives.

The current "success" signal is heavily contaminated by the **halo effect** (BK-0048-card-001). Because expansion bookings rose and renewals closed early, leadership is now attributing specific traits to the product team—describing them as "focused," "commercially disciplined," and "aligned." However, the evidence suggests these trait assessments are reflections of the performance signal rather than independent evidence: expansion dollars were driven by temporary bundle pricing, and customer enthusiasm was gathered after sales pitched PlanPilot as a future centerpiece.

Without the Demand Cleanroom, you are risking a "scale broadly" decision based on halo-tinted data. The Cleanroom provides the necessary empirical evidence to determine if buyers value PlanPilot itself or merely the discount and the promise of a roadmap.

### The Strongest Reason Against It
The Demand Cleanroom creates immediate friction with the Sales organization and risks a short-term dip in expansion bookings for the matched set of accounts. By removing bundle pricing and withholding the roadmap pitch, you are intentionally removing the two primary levers that drove the "surprisingly strong quarter." In a high-pressure environment with a board meeting in twelve days, this may be perceived as sabotaging momentum or "fighting" the sales team during a winning streak.

### The Observable Evidence That Would Change My Mind
I would change this recommendation to the **Case Evidence Review** if you could provide evidence that the primary driver of the current growth is not the bundle pricing, but a high "acceptance rate" of PlanPilot’s core logic.

Currently, your usage data is a "vanity metric" (BK-0007-card-001): high frequency is driven by managers rerunning samples for meetings, not analysts using the tool to solve cases. If a preliminary audit showed that front-line analysts were keeping PlanPilot suggestions intact (rather than manually rewriting them or abandoning the tool in the public sector), it would suggest the product has "validated learning" (BK-0007-card-001) regarding its value proposition. In that case, the risk shifts from "do they want it?" to "how do we make it usable?", making the Case Evidence Review the higher-leverage move.
