---
run_id: halo-evidence-vs-diagnosis-validation-v12-famous-sources-supplied-03
created: 2026-05-24
eval_type: contradiction-preservation
case_id: halo-evidence-vs-diagnosis-validation-v12
benchmark_version: halo-evidence-vs-diagnosis-validation-v12-v1
model_condition: famous_sources_supplied
run_number: 3
model_name: gemma-4-31b-it-mlx:2
model_id: gemma-4-31b-it-mlx:2
model_snapshot: LM Studio MLX 8-bit model id lmstudio-community/gemma-4-31B-it-MLX-8bit; loaded_context_length 65536
runtime: LM Studio local OpenAI-compatible HTTP server; MLX runtime
provider: local
temperature: 0.7
top_p: 0.9
num_ctx: 65536
max_tokens: 2048
seed: 302
prompt_source: condition packet (famous_sources_supplied) - frozen added material plus frozen Advisor prompt; see run-packet.md
prompt_sha256: 81621976eaf302301d88434e895bffe7f264ddbe9d86bbb0dd82120c2f65f2aa
source_packet: a name-level list of famous source titles and authors, then the frozen Advisor prompt; no benefits cases, summaries, source cards, or tension card - see run-packet.md
source_packet_sha256: fbda9621700ea5a031af698b8700a95ac925370d84a60c86c1d7bce543e8cc3b
condition_packet_sha256: fbda9621700ea5a031af698b8700a95ac925370d84a60c86c1d7bce543e8cc3b
output_file: model-outputs/famous_sources_supplied-03.md
judge_model_id: pending - judge receipts recorded separately under judge-packet
judge_prompt_sha256: pending - judge receipts recorded separately under judge-packet
judge_independence: pending - judge receipts recorded separately under judge-packet
raw_model_output_public_safe: true
---

# Model Output - famous_sources_supplied (run 03)

## Condition

Benchmark version `halo-evidence-vs-diagnosis-validation-v12-v1`, condition `famous_sources_supplied`, run 3 of 8. Real local-model run: `gemma-4-31b-it-mlx:2` via lmstudio, seed 302, on the frozen condition packet.

## Output

**Recommendation:** Commit to the **Case Evidence Review**.

**Why:** Your current success is "entangled," meaning your lagging indicators (expansion bookings, shortened sales cycles) are likely being driven by pricing incentives and sales narratives rather than product value. The "strong quarter" is a noisy signal: the bundle pricing creates an artificial spike in bookings, and the "enthusiastic comments" are reactions to a promised roadmap, not the current tool.

Crucially, your usage data is misleading. High frequency from managers rerunning samples suggests the tool is being used for *demonstration/enablement* rather than *production*. The fact that analysts abandon the tool in the public sector because they cannot explain the "why" to reviewers indicates a fundamental failure in the product's core value proposition: trust and auditability.

The Adoption Quality Sprint measures *if* they use it (which you already know is inconsistent), and the Demand Cleanroom measures *if* they will pay for it (which is a lagging indicator of value). Only the Case Evidence Review looks at the "work" itself to determine if PlanPilot is actually solving the problem or simply being bypassed by analysts who prefer manual notes. You cannot scale a product that is being "overridden" or "manually rewritten" without first understanding the gap between the proposal and the required outcome.

**The strongest reason against it:** It is a slow, qualitative process that provides "small set" evidence at a moment when the board and executive team are riding a wave of quantitative optimism. By choosing this, you risk appearing "un-commercial" or overly cautious while the sales team is arguing that the momentum should be capitalized on through broad scaling.

**Observable evidence that would change my mind:** If the "wrong recommendation" tickets in the training channel were actually a negligible fraction of total volume and the "manual notes" fallback was limited to only 5% of analysts, it would suggest the product is functionally sound and the issue is purely a sales/pricing one. In that case, the Demand Cleanroom would be the superior choice to isolate the true commercial appetite.
