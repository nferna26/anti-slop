---
case_id: normalization-vs-latent-errors-water-treatment-v4
benchmark_version: normalization-vs-latent-errors-water-treatment-v4-v1
artifact: judge-score
judge_model_id: claude-opus-4-7
judge_model_snapshot: claude-opus-4-7
judge_model_family: Claude Opus (Anthropic)
judge_provider: Anthropic API
judge_runtime: Anthropic API via Codex local-only script using operator-provided API key
generator_model_id: gemma4:31b
judge_status: eligible external API blind judge pass - calibration passed; operator route acceptance recorded
judge_independence: independent of the orchestrating agent
judge_route_operation: agent-operated hosted API call, operator-accepted for v4 result-lifting
calibration_result: passed - 0 criteria differences, no Anchor C C5/C6 disagreement
outputs_scored: 40
judge_date: 2026-05-23
condition_blinded: true
result_status: partial
note: Hosted Anthropic model scored the 40 anonymised OUT-NN answers through the Anthropic API. The model is independent of the orchestrating agent and remained condition-blind. On 2026-05-23 the operator accepted hosted API judge calls run by Codex with operator-provided keys as result-lifting judge routes for v4 when the receipt records the route honestly. No OUT-NN to condition mapping.
---

# Anthropic API Blind Judge Score - Claude Opus 4.7

This is a condition-blind judge pass of the contradiction-preservation eval `normalization-vs-latent-errors-water-treatment-v4`, benchmark version `normalization-vs-latent-errors-water-treatment-v4-v1`. The judge is the hosted Anthropic model `claude-opus-4-7` (`Claude Opus 4.7`).

This receipt records C1-C6 scores only. It is **not** a `## Result` change, **not** a condition reconciliation, and **not** a `benchmark_supported` step. The case stays `partial`; `scoring_status` stays `unscored` until aggregate reconciliation is intentionally performed; and no `OUT-NN` is mapped to conditions here.

## Judge identity and independence

- **Judge model:** `claude-opus-4-7` (`Claude Opus 4.7`) - hosted Anthropic Claude Opus family.
- **Provider / runtime:** Anthropic API via a local-only Codex script. API model-list metadata records `created_at: 2026-04-14T00:00:00Z`, `max_input_tokens: 1000000`, and `max_tokens: 128000` for this model. The API rejected explicit `temperature` for this model as deprecated, so the scoring call used no explicit temperature parameter.
- **Response IDs:** calibration `msg_01Kb5ShLrwT25PuEVrGgcc4G`; scoring `msg_018W4s5aSeqC7y8tp8BHd4AH`.
- **Input hashes:** calibration packet sha256 `775af8660474b7585111790e38cb1975e8a69f3f115fc9dd45d270bf865cba72`; scoring packet sha256 `c7b66309038b3750691e6562e0b632826ec5db774790ac174db3eb50252cdd5a`.
- **Raw output hashes:** calibration response sha256 `ecb8815c2735f8e646e8f4f61308bb5ae3cbb06924c0df275986c27f3d41f77c`; scoring response sha256 `f8da96f668c5840e534f9e6ea42f4e4e0f9fd1f8ad8862309a64f49b0322cac3`. Raw transcripts remain local-only and are not committed.
- **API usage:** calibration input tokens `6320`, output tokens `173`; scoring input tokens `34986`, output tokens `4866`. Service tier: `standard`; inference geo: `global`.
- **Hosted model judge, not a human judge.** The scoring call is a real external Anthropic API run, not a simulated output and not an in-session model self-score.
- **Route eligibility decision:** the frozen v4 route originally named a hosted Anthropic Opus-family judge operated by the human operator outside the orchestration session. This run was operated by the Codex orchestration session using an operator-provided API key. On 2026-05-23, the operator explicitly accepted these hosted API paths as result-lifting judges for v4. Under that operator decision, this receipt counts as one eligible external API judge pass: the hosted Anthropic model did not author the case, rubric, anchors, run packet, judge packet, or outputs, and it did not receive the answer key or condition labels.
- **Condition-blind.** The judge received only `independent-judge-packet-calibration.md` and, after calibration passed, `independent-judge-packet-scoring.md`. It did not receive `model-outputs/`, the local-only `OUT-NN` to condition answer key, `calibration-anchors.md` Surface 2 before calibration, or any condition label.

## Calibration

The judge scored the three Surface 1 calibration anchors first. The returned verdicts matched the operator-only Surface 2 reference exactly:

```text
[ANCHOR-A] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-B] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
[ANCHOR-C] C1=PASS C2=PASS C3=PASS C4=PASS C5=FAIL C6=FAIL TOTAL=4
```

Against the withheld reference: **0 criteria differences**, and **no Anchor C C5/C6 disagreement**. The calibration gate passed; real-output scoring then proceeded.

## Method

Each `OUT-NN` was scored against the six frozen criteria C1-C6 in the rubric, with the dependency rule applied (C5 requires C3 and C4; C6 requires C5). The verdicts below are copied from the parsed API transcript; rationales are whitespace-normalized for table formatting. A consistency check confirmed every stated TOTAL equals its PASS count and no row violates the dependency rule.

## Score sheet

| Output | C1 | C2 | C3 | C4 | C5 | C6 | Total | Rationale |
|---|---|---|---|---|---|---|---|---|
| OUT-01 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Treats both mechanisms substantively, anchors in multiple scenario facts including the window and high-flow load, weighs what audit/repair reaches versus what an interlock provides, and gives concrete recommendation with failure path and disconfirming evidence. |
| OUT-02 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Identifies competing mechanisms, names the interlock tradeoff explicitly, recommends Option B under the constraint, and gives concrete disconfirming evidence about late sampling or structural degradation. |
| OUT-03 | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 | Recommends decline but largely frames it through normalization; the disconfirming evidence essentially asks for Option 2, which contradicts the recommendation and shows the intervention boundary is not coherently weighed. |
| OUT-04 | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 | Brief recommendation to decline mentions both mechanisms but does not weigh what each intervention reaches; the disconfirming evidence relies on the foreclosed alternative path without addressing the boundary. |
| OUT-05 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Engages both mechanisms, explicitly notes that adding procedural surface may be absorbed, weighs the missing interlock as the strongest reason against, and gives concrete observable evidence. |
| OUT-06 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Names the tension, anchors in facts, weighs what Option 2 reaches versus what an interlock would, and provides a concrete recommendation with disconfirming evidence tied to financial asymmetry. |
| OUT-07 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Recommends Option B, weighs the lack of automated fail-safe against the diagnostic value, and names specific disconfirming evidence (audit showing benign sensor artifact). |
| OUT-08 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Treats both mechanisms, anchors in multiple facts, weighs the boundary clearly between diagnosis and automation, and provides concrete disconfirming evidence. |
| OUT-09 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Although terse, it recommends Option 2, names the missing interlock as strongest reason against, weighs both sides, and gives audit-based disconfirming evidence about pencil-whipping or late samples. |
| OUT-10 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Explicitly addresses both mechanisms with named tensions, weighs the boundary between defence-adding and threshold work, recommends Option B, and gives concrete disconfirming evidence pointing to Option C. |
| OUT-11 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Names both readings, weighs Option 1 as "safety theater" against Option 2's diagnostic value, recommends B, and gives concrete disconfirming evidence about negligent closures. |
| OUT-12 | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 | Recommends decline citing both mechanisms, but doesn't really weigh what the interlock could and couldn't reach; the disconfirming evidence relies on the foreclosed Option B path without explaining the boundary tradeoff. |
| OUT-13 | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 | Recommends decline with strong reasoning on both sides, but the disconfirming evidence requires Option B's completion in the same window without acknowledging Option B itself forecloses decline's preparation; doesn't weigh what each intervention reaches. |
| OUT-14 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Explicitly weighs Option B's diagnostic value against Option A's automated barrier, recommends B, and provides distinct disconfirming evidence pointing to both decline and Option A scenarios. |
| OUT-15 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Treats both mechanisms substantively, weighs the missing fail-safe against the diagnostic benefit, recommends Option B, and names specific audit findings that would flip to decline. |
| OUT-16 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Recommends Option B with clear weighing of what each intervention reaches, identifies the human-reliance concern with operators writing formulaic notes, and gives concrete disconfirming evidence. |
| OUT-17 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Concise but covers both mechanisms, weighs the missing interlock against the diagnostic value, and provides concrete disconfirming evidence. |
| OUT-18 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Explicitly engages both mechanisms with the boundary argument that adding defences may be absorbed by drifted culture, recommends Option B, and names concrete disconfirming evidence about sensor artifacts. |
| OUT-19 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Weighs both mechanisms, explicitly notes that defence-strengthening doesn't reach cultural drift, recommends Option B, and gives concrete disconfirming evidence about capacity limits. |
| OUT-20 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Recommends Option B then decline, weighs the complexity Option A adds against diagnostic value, names economic cost as strongest reason against, and gives concrete disconfirming evidence. |
| OUT-21 | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 | Recommends decline with both mechanisms named, but the disconfirming evidence requires completing Option B as part of the foreclosed window; doesn't substantively weigh what each intervention reaches. |
| OUT-22 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Brief but recommends Option B, explicitly names the missing fail-safe as the strongest reason against, and provides concrete disconfirming evidence about near-miss patterns. |
| OUT-23 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Recommends Option B then decline, weighs both mechanisms, names economic cost as strongest reason against, and gives concrete disconfirming evidence about audit findings. |
| OUT-24 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Explicitly engages both mechanisms with named tension, weighs the missing fail-safe, recommends Option B, and provides concrete disconfirming evidence about benign causes. |
| OUT-25 | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 | Recommends decline with both mechanisms acknowledged, but the disconfirming evidence assumes Option B can be completed in the foreclosed window without weighing the interlock-vs-threshold boundary. |
| OUT-26 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Recommends Option B, weighs the risk that audit may force decline as strongest reason against, and provides concrete disconfirming evidence about false positives and load testing. |
| OUT-27 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Brief but recommends Option B, names the missing automated fail-safe, and gives concrete disconfirming evidence about sensor-only causation. |
| OUT-28 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Engages both mechanisms substantively, weighs why Option A's "blind redundancy" fails to reach the underlying issues, recommends Option B contingent on audit, and gives concrete disconfirming evidence pointing to decline. |
| OUT-29 | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 | Recommends decline with both mechanisms named, but the disconfirming evidence relies on completing Option B in the same foreclosed window and doesn't explicitly weigh what each intervention reaches. |
| OUT-30 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Weighs Option A as "detect and react" against Option B's root-cause approach, recommends B, names the missing fail-safe, and gives concrete disconfirming evidence about sampling practices. |
| OUT-31 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Explicitly engages both mechanisms with cards-style references, weighs why adding defence may deepen drift, recommends Option B, and gives concrete disconfirming evidence about false positives flipping to Option A. |
| OUT-32 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Recommends Option B and decline, weighs Option A as a dangerous bandage, and provides concrete disconfirming evidence about documented electronic glitches. |
| OUT-33 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Engages both mechanisms with explicit boundary argument that defence-strengthening can be absorbed by drifted culture, recommends Option B, names the missing fail-safe, and gives concrete disconfirming evidence. |
| OUT-34 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Explicit on both mechanisms and the intervention boundary, recommends Option B, names the missing automated fail-safe, and gives concrete disconfirming evidence about false positives. |
| OUT-35 | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 | Recommends decline with both mechanisms present, but the disconfirming evidence assumes Option B can be completed in the foreclosed window; doesn't substantively weigh the boundary between interventions. |
| OUT-36 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Recommends Option B with decline, weighs Option A as bandage against root-cause work, names economic cost as strongest reason against, and gives concrete disconfirming evidence (while noting why it's unlikely). |
| OUT-37 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Recommends Option B, weighs the lack of hard automated safeguard, dismisses Option A as a bandage, and gives concrete disconfirming evidence about benign electrical interference. |
| OUT-38 | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 | Recommends decline with both mechanisms named, but disconfirming evidence requires Option B's completion in the foreclosed window and doesn't weigh the interlock-vs-threshold boundary. |
| OUT-39 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Recommends Option B, names the missing automated fail-safe as strongest reason against, and provides concrete disconfirming evidence about external raw-water characteristics. |
| OUT-40 | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 | Recommends decline citing both mechanisms, but the disconfirming evidence relies on completing Option B in the foreclosed window without explicitly weighing what each intervention reaches. |

Score distribution across the forty blinded answers: 4/6 x10, 6/6 x30. This distribution is over `OUT-NN` labels only; it is **not** a per-condition aggregate, and no `OUT-NN` to condition mapping is recorded here.

## What this receipt is not

This is one hosted Anthropic API judge score receipt. It is not an eval `## Result`, not a condition reconciliation, and not a promotion. Under the 2026-05-23 operator route-eligibility decision, it satisfies the second eligible external judge pass for v4, from a different provider/family than the OpenAI API judge. Reconciliation and any `do_not_promote` or positive-result decision remain separate later steps.

A model output, and a judge score of one, is a test artifact - never an authority.
