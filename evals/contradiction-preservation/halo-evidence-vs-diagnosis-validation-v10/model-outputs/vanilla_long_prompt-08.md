---
run_id: halo-evidence-vs-diagnosis-validation-v10-vanilla-long-prompt-08
created: 2026-05-24
eval_type: contradiction-preservation
case_id: halo-evidence-vs-diagnosis-validation-v10
benchmark_version: halo-evidence-vs-diagnosis-validation-v10-v1
model_condition: vanilla_long_prompt
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
seed: 804
prompt_source: condition packet (vanilla_long_prompt) - frozen added material plus frozen Advisor prompt; see run-packet.md
prompt_sha256: 61d771e2bff7fd2e18be1d2999d0f601760656e3e69b4622989ca7bffd3aff8e
source_packet: a neutral equal-length filler plus transition, then the frozen Advisor prompt; no substrate artifact - see run-packet.md
source_packet_sha256: 725394e5c302c1e30265374a9742db053b2cd62aaaaf76c7381b6fcdd8c7558b
condition_packet_sha256: 725394e5c302c1e30265374a9742db053b2cd62aaaaf76c7381b6fcdd8c7558b
output_file: model-outputs/vanilla_long_prompt-08.md
judge_model_id: pending - judge receipts recorded separately under judge-packet
judge_prompt_sha256: pending - judge receipts recorded separately under judge-packet
judge_independence: pending - judge receipts recorded separately under judge-packet
raw_model_output_public_safe: true
---

# Model Output - vanilla_long_prompt (run 08)

## Condition

Benchmark version `halo-evidence-vs-diagnosis-validation-v10-v1`, condition `vanilla_long_prompt`, run 8 of 8. Real local-model run: `gemma-4-31b-it-mlx:2` via lmstudio, seed 804, on the frozen condition packet.

## Output

**Recommendation:** Run the **Claim File Review**.

**Why:** Your current success is a "mirage" created by lagging indicators and sales incentives. Expansion bookings are inflated by temporary bundle pricing, and usage spikes are driven by managers performing retrospective audits rather than adjusters utilizing the tool for live claims. Most critically, you have a "black box" problem: in regulated segments, the tool is abandoned because it lacks explainability. The Claim File Review is the only option that provides a ground-truth audit of whether DraftPath actually solves the core problem (effective claim steering) or if it is merely a novelty that managers like and adjusters ignore.

**Strongest Reason Against:** It is the slowest, most manual process of the three validation tests. Unlike the Usage Quality Sprint (automated tracking) or the Commercial Cleanroom (sales gating), this requires human labor to manually audit files, which may feel too slow given the twelve-day budget deadline.

**Evidence That Would Change My Mind:** If the "wrong recommendation" support tickets—even those rerouted to training—show a statistically significant drop in *actual error rates* (not just ticket volume) across all segments, it would suggest the product is fundamentally sound and the issue is purely one of enablement. In that case, I would shift the recommendation to the **Usage Quality Sprint** to optimize the rollout rather than auditing the core utility.
