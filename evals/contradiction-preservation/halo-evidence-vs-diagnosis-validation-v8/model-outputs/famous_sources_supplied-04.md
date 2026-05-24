---
run_id: halo-evidence-vs-diagnosis-validation-v8-famous-sources-supplied-04
created: 2026-05-24
eval_type: contradiction-preservation
case_id: halo-evidence-vs-diagnosis-validation-v8
benchmark_version: halo-evidence-vs-diagnosis-validation-v8-v1
model_condition: famous_sources_supplied
run_number: 4
model_name: gemma4:31b
model_id: gemma4:31b
model_snapshot: Ollama model ID 6316f0629137
runtime: Ollama local HTTP server; version 0.24.0
provider: local
temperature: 0.7
top_p: 0.9
num_ctx: 32768
seed: 402
prompt_source: condition packet (famous_sources_supplied) - frozen added material plus frozen Advisor prompt; see run-packet.md
prompt_sha256: 5a42e17859b4a23ae36d2682474f8d0369ffc492c200375fd79a14bf3b322262
source_packet: a name-level list of famous source titles and authors, then the frozen Advisor prompt; no claims, summaries, source cards, or tension card - see run-packet.md
source_packet_sha256: a8f837584b6b87efa42fb92f178885d67f9a6373379ee1ede9671b0a54d4d2f8
condition_packet_sha256: a8f837584b6b87efa42fb92f178885d67f9a6373379ee1ede9671b0a54d4d2f8
output_file: model-outputs/famous_sources_supplied-04.md
judge_model_id: pending - judge receipts recorded separately under judge-packet
judge_prompt_sha256: pending - judge receipts recorded separately under judge-packet
judge_independence: pending - judge receipts recorded separately under judge-packet
raw_model_output_public_safe: true
---

# Model Output - famous_sources_supplied (run 04)

## Condition

Benchmark version `halo-evidence-vs-diagnosis-validation-v8-v1`, condition `famous_sources_supplied`, run 4 of 8. Real local-model run: `gemma4:31b` via Ollama, seed 402, on the frozen condition packet.

## Output

**Recommendation**
Recommend the **targeted evidence pass**.

**Why**
The current "upbeat story" is a classic example of the **Halo Effect**: the board is attributing a temporary spike in revenue (driven by discounts and early renewals) to a fundamental shift in company discipline and market fit. In reality, the leading indicators suggest a failure in product-market fit for the actual end-user.

While NRR is up, the quality of that revenue is low (artificial discount-driven expansion). More critically, the behavioral data is alarming: a 31% first-week retention rate among front-line reviewers indicates that the product is not solving the "Job to be Done" for the primary user. The "success" is currently being carried by a small group of champions and a sales narrative that ignores the "hidden" churn and the "explainability" blocker in the insurance segment. Scaling now (Option A) would be "Bad Strategy" because it mistakes a tactical pricing win for a strategic product win, effectively scaling a leaky bucket. Narrowing to regulated insurance (Option C) is premature because you have not yet decoupled the "champion" behavior from the "front-line" failure across the broader mid-market.

**The strongest reason against it**
**Loss of perceived momentum.** The board and sales leadership are currently in a "winning" mindset. Pausing discounts and slowing the rollout to conduct a "science project" may be perceived as a lack of confidence or a failure to "strike while the iron is hot." In a B2B environment, the psychological momentum of a "market wedge" often outweighs the nuance of usage data in the eyes of a CEO, and this pause could risk the budget allocation for the coming year.

**Observable evidence that would change my mind**
I would pivot to the broad scale (Option A) if the "champion" usage (the small group rerunning sample queues) can be linked to a **quantifiable, high-value business outcome** that the customer's executive leadership cares about—even if the front-line reviewers hate it. If the "champion" is using the tool to provide a level of oversight or reporting that is so valuable it justifies the cost regardless of front-line adoption, the "wedge" is real, but it is a "Management" wedge rather than a "Reviewer" wedge.
