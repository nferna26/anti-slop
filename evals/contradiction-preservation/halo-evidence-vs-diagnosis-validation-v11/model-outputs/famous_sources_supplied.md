---
run_id: halo-evidence-vs-diagnosis-validation-v11-famous-sources-supplied-01
created: 2026-05-24
eval_type: contradiction-preservation
case_id: halo-evidence-vs-diagnosis-validation-v11
benchmark_version: halo-evidence-vs-diagnosis-validation-v11-v1
model_condition: famous_sources_supplied
run_number: 1
model_name: gemma-4-31b-it-mlx:2
model_id: gemma-4-31b-it-mlx:2
model_snapshot: LM Studio MLX 8-bit model id lmstudio-community/gemma-4-31B-it-MLX-8bit; loaded_context_length 65536
runtime: LM Studio local OpenAI-compatible HTTP server; MLX runtime
provider: local
temperature: 0.7
top_p: 0.9
num_ctx: 65536
max_tokens: 1024
seed: 102
prompt_source: condition packet (famous_sources_supplied) - frozen added material plus frozen Advisor prompt; see run-packet.md
prompt_sha256: 18fa1d51f6167dbbf1f7ece676734d5cdb459384bca25e1508dd96cd4745e42d
source_packet: a name-level list of famous source titles and authors, then the frozen Advisor prompt; no claims, summaries, source cards, or tension card - see run-packet.md
source_packet_sha256: 5f0d18f3e982d60319cdf56d83f5bfcb60ca486dc8eccd9dfcda42bea551750c
condition_packet_sha256: 5f0d18f3e982d60319cdf56d83f5bfcb60ca486dc8eccd9dfcda42bea551750c
output_file: model-outputs/famous_sources_supplied.md
judge_model_id: pending - judge receipts recorded separately under judge-packet
judge_prompt_sha256: pending - judge receipts recorded separately under judge-packet
judge_independence: pending - judge receipts recorded separately under judge-packet
raw_model_output_public_safe: true
---

# Model Output - famous_sources_supplied (run 01)

## Condition

Benchmark version `halo-evidence-vs-diagnosis-validation-v11-v1`, condition `famous_sources_supplied`, run 1 of 8. Real local-model run: `gemma-4-31b-it-mlx:2` via lmstudio, seed 102, on the frozen condition packet.

## Output

**Recommendation:** Run the **Claim File Review**.

**Why:**
Your current success is an "entangled" signal. The financial growth is likely a result of pricing bundles and sales narrative (the "Halo Effect") rather than product value. The usage data is a vanity metric: managers are using the tool for auditing/training, while the actual end-users (adjusters) are abandoning it.

The Claim File Review is the only option that addresses the core risk: a lack of "Jobs-to-be-Done" fit. By analyzing whether suggestions were accepted, overridden, or "impossible to explain," you move past aggregated usage percentages and discover *why* the product is failing in regulated segments and why adjusters revert to manual notes. This provides the ground-truth evidence needed to decide if SignalPath requires a pivot in logic, better explainability features, or a narrower market focus before you commit next year's budget to scaling a leaky bucket.

**The strongest reason against it:**
It is the slowest and most labor-intensive of the three validation tests. Unlike the Usage Quality Sprint (which relies on automated dashboards) or the Commercial Cleanroom (which relies on sales outcomes), a file review requires manual qualitative analysis. By choosing this, you sacrifice the ability to immediately quantify the financial impact of the bundle-pricing distortion (the Cleanroom) and the ability to track real-time behavioral shifts (the Sprint).

**Observable evidence that would change my mind:**
If the "regional carriers" who intend to remove SignalPath provide specific, documented feedback stating that their objection is purely based on the *price* of the bundle rather than the *utility* of the feature. If the friction is purely commercial and not functional, the Commercial Cleanroom would become the priority to determine the true price elasticity of the product.
