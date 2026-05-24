---
run_id: halo-evidence-vs-diagnosis-validation-v12-vanilla-long-prompt-04
created: 2026-05-24
eval_type: contradiction-preservation
case_id: halo-evidence-vs-diagnosis-validation-v12
benchmark_version: halo-evidence-vs-diagnosis-validation-v12-v1
model_condition: vanilla_long_prompt
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
seed: 404
prompt_source: condition packet (vanilla_long_prompt) - frozen added material plus frozen Advisor prompt; see run-packet.md
prompt_sha256: 81621976eaf302301d88434e895bffe7f264ddbe9d86bbb0dd82120c2f65f2aa
source_packet: a neutral equal-length filler plus transition, then the frozen Advisor prompt; no substrate artifact - see run-packet.md
source_packet_sha256: 98ca8c241ae7ac2a811e9012d1dcc7202739138b0b2a830b3ed8ef5ba847b45e
condition_packet_sha256: 98ca8c241ae7ac2a811e9012d1dcc7202739138b0b2a830b3ed8ef5ba847b45e
output_file: model-outputs/vanilla_long_prompt-04.md
judge_model_id: pending - judge receipts recorded separately under judge-packet
judge_prompt_sha256: pending - judge receipts recorded separately under judge-packet
judge_independence: pending - judge receipts recorded separately under judge-packet
raw_model_output_public_safe: true
---

# Model Output - vanilla_long_prompt (run 04)

## Condition

Benchmark version `halo-evidence-vs-diagnosis-validation-v12-v1`, condition `vanilla_long_prompt`, run 4 of 8. Real local-model run: `gemma-4-31b-it-mlx:2` via lmstudio, seed 404, on the frozen condition packet.

## Output

I recommend that you commit to the **Case Evidence Review**.

**Why:**
Your current growth metrics are "entangled" and likely illusory. The rise in expansion bookings is tied to temporary pricing bundles rather than intrinsic value, and usage spikes are driven by managers performing "sanity checks" (rerunning closed samples) rather than analysts deriving value from live workflows. Most critically, the public-sector abandonment and analyst fallback to manual notes suggest a "black box" problem: users don't trust or cannot explain the output. Before scaling or attempting to clean the sales funnel, you must determine if PlanPilot is actually solving the core problem or if it is simply a "demo-ware" feature that looks impressive to buyers but fails in the actual workflow. The Case Evidence Review is the only option that provides a ground-truth audit of whether the output is accepted, overridden, or impossible to explain.

**The strongest reason against it:**
This approach is slow and qualitative. While you are conducting a manual review of case files, the "leaky bucket" continues: regional administrators are already planning to remove the feature from their contracts, and the board may view a manual review as an academic exercise that doesn't provide the immediate "hard" data (like the Adoption Quality Sprint) or revenue protection (like the Demand Cleanroom) they desire before locking the budget.

**Observable evidence that would change my mind:**
If you discover that the "manual notes" fallback and public-sector abandonment are caused exclusively by a lack of training/enablement rather than poor output quality (e.g., if the Case Evidence Review shows that analysts *do* accept the suggestions but simply lack the vocabulary to explain them), I would shift the recommendation to the **Adoption Quality Sprint** to focus on enablement and return rates.
