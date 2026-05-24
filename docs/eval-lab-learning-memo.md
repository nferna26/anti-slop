# Eval Lab Learning Memo

Cross-case learning notes from the contradiction-preservation eval surface. The
memo records what the lab has learned, what it has **not** shown, and what
honestly follows. It is methodology synthesis, not advice and not canon. The
controlled vocabulary for any individual case's status remains
`docs/eval-result-status-policy.md`; the operating frame remains
`docs/eval-lab-protocol.md`. This memo never lifts a case's `## Result`.

A negative or inconclusive eval result is progress: it tells us what is **not**
yet shown, narrows the next case design, and prevents an unsupported advice
claim from being promoted. The lab's job is to record those honestly.

## 2026-05-24 — v12 fixed judge readiness but the criteria prompt matched substrate

The `halo-evidence-vs-diagnosis-validation-v12` run tested the v11 lesson
directly. V11 was blocked by unresolved judge disagreement with no eligible
third route, so v12 pre-registered three routes before generation: hosted
OpenAI `gpt-5.4`, hosted Anthropic `claude-opus-4-7`, and local
`gpt-oss:20b`. All three passed the C4-C6 calibration gate and a new
judge-disagreement smoke test before any full generation. The local route then
scored all 48 blinded outputs rather than serving as an after-the-fact repair.

The machinery worked, but the result stayed `partial` / `do_not_promote`.
Pooled `substrate_workflow` beat `vanilla`, `famous_sources_supplied`,
`vanilla_long_prompt`, and `generic_advice_prompted` by +2.000 total points,
and none of those controls passed C4-C6. The hard
`criteria_prompted_no_sources` control matched or beat the substrate: pooled
mean total 5.250 versus substrate 5.000, with C4 0.83 versus substrate 0.67,
C5 0.75 versus substrate 0.67, and C6 tied at 0.67. The positive rule's
total-score margin, critical-criterion margin, judge-level stability, and
no-unresolved-judge-trigger clauses failed.

The methodological lesson is sharper than v11: the third-route readiness
problem can be fixed, but the current halo/evidence-quality substrate has not
shown lift over a well-written criteria prompt. The next attempt should not
keep polishing this surface toward promotion. Either test a source-specific
boundary that an abstract criteria prompt cannot name, or narrow the public
claim to what the evidence actually supports: separation from generic and
equal-length prompting, not from explicit criteria prompting.

## 2026-05-24 — v11 separated on C4-C6 but exposed the third-judge gap

The `halo-evidence-vs-diagnosis-validation-v11` run tested the v10 lesson
directly. C1-C3 remained scored and reported, but v11 made them
non-promotional; the positive rule depended on C4-C6 only. The case kept the
two-sided substrate-feasibility probe and full public-safe source-card packet.
The probe passed before freeze: no-source outputs passed C4 in 0/6 runs, while
substrate outputs passed C4 in 3/3 runs.

The full run produced 48 real LM Studio MLX outputs, two hosted judges passed
the C4-C6 calibration gate before generation, and aggregate-only reconciliation
completed from committed hashes. The substrate separated strongly: pooled
`substrate_workflow` mean total was 5.875 versus 2.938 for
`generic_advice_prompted`, 3.000 for `vanilla_long_prompt`, and 4.062 for
`criteria_prompted_no_sources`. The C4-C6 composite margins cleared every
pre-registered control margin, and no key control saturated C4-C6.

The result still stayed `partial` / `do_not_promote` because the
pre-registered judge-disagreement trigger fired. OpenAI and Anthropic disagreed
on C4-C6 for 3/8 `criteria_prompted_no_sources` outputs, above the 20 percent
per-condition trigger. The local `gpt-oss:20b` route had been named before
generation, but did not clear calibration because it omitted Anchor H and
reported an arithmetic total mismatch on Anchor G; it therefore scored zero
outputs and could not resolve the disagreement. The methodological lesson is
now narrower: the substrate/control separation can be made visible on C4-C6,
but a promotion-grade run needs an actually eligible third route or a
pre-frozen disagreement policy that skeptical readers will accept.

## 2026-05-24 — v10 showed substrate lift on C4-C6 but C3 was non-discriminating

The `halo-evidence-vs-diagnosis-validation-v10` run added the missing
two-sided readiness check from v9: before freeze, no-source probe outputs had
to fail C4 while substrate probe outputs had to pass C4. That probe passed
0/6 no-source C4 and 3/3 substrate C4. V10 also used the full public-safe text
of the three reviewed source cards rather than compact card summaries, enabled
by the LM Studio MLX model's 65,536-token loaded context.

The full run produced 48 real outputs, two hosted judges passed calibration and
scored all blinded outputs, and aggregate-only reconciliation completed from
committed hashes. The substrate finally separated strongly on the intended
boundary: pooled `substrate_workflow` mean total was 6.000 versus 3.000 for
`generic_advice_prompted`, 2.938 for `vanilla_long_prompt`, and 3.500 for
`criteria_prompted_no_sources`; both judges gave substrate 8/8 C4-C6 passes.
The result still stayed `partial` / `do_not_promote` because the frozen
positive rule required margin on every C3-C6 criterion. C3 saturated in key
controls (`generic_advice_prompted` 1.00; `vanilla_long_prompt` and
`criteria_prompted_no_sources` 0.94), and the judge-disagreement trigger fired
for `criteria_prompted_no_sources`. The methodological lesson is that basic
contaminated-evidence recognition is now too easy to be a load-bearing margin
criterion. Future designs should keep C3 as descriptive or as a saturation
monitor, but make the positive critical composite track the hard boundary that
v10 actually isolated: selecting and defending the right disconfirming
intervention, then making a constrained recommendation with a falsifier.

## 2026-05-24 — v9 showed that generic failure is not substrate success

The `halo-evidence-vs-diagnosis-validation-v9` run added a local-only
generic-solvability probe before freeze. That probe passed: no-source outputs
reliably chose the Claim File Review decoy and failed the Commercial Cleanroom
C4 boundary. The full benchmark then ran six conditions with eight real LM
Studio MLX outputs per condition, a compact reviewed-source substrate packet,
hash-blinded `OUT-NN` outputs, hosted OpenAI and Anthropic API judges that both
passed pre-generation calibration, and aggregate-only reconciliation.

The positive rule still failed. Both judges scored every output in every
condition as 3/6: C1-C3 pass, C4-C6 fail. Every condition recognized the
contaminated evidence problem, but no condition, including `substrate_workflow`,
selected the Commercial Cleanroom as the load-bearing evidence standard. The
new non-discriminating-judge guard also fired because both judges assigned the
same total to 48/48 outputs. The methodological lesson is that making generic
advice fail is not enough; the substrate must be shown, before the full run, to
move the generator across the same counterintuitive boundary.

## 2026-05-24 — v8 showed that rubric hardening cannot rescue a telegraphing scenario

The `halo-evidence-vs-diagnosis-validation-v8` run repaired the v7 judge
calibration failure and then failed substantively. Hosted OpenAI and hosted
Anthropic both passed the pre-generation C3-C6 smoke gate, 40 real generator
outputs were produced, blinded, scored, and reconciled aggregate-only, and all
receipt gates passed. The positive rule still failed: `generic_advice_prompted`
matched `substrate_workflow` at 6.000 and saturated C3-C6 at 1.00, while
`vanilla_long_prompt` saturated C3/C4. The methodological lesson is that
hardening criteria is insufficient when the scenario itself lists the
contaminated signals and the obvious evidence pass. V9 therefore adds a
pre-freeze generic-solvability probe and changes the load-bearing question to
whether the answer can distinguish the commercial disconfirmation test from
plausible product-diagnostic usage or workflow tests.

## 2026-05-22 — three scored cases, three `do_not_promote` decisions

Three contradiction-preservation cases are in `scoring_status: scored` /
`## Result: partial` with eval decisions of `do_not_promote`:

| Case | `decision_class` | Mechanism |
|---|---|---|
| `managerial-output-vs-industry-structure` | `weakened_by_blind_judge` | Three blind judges; the substrate-over-equal-length-control margin runs **+3.0 → +0.67 → −0.33** across them. Under hosted OpenAI `gpt-5.4-mini`, `substrate_workflow` is the **lowest**-mean condition (3.67) and **loses** to `vanilla_long_prompt` by 0.33. |
| `diagnosis-vs-validated-learning-benefits-renewal-v2` | `judge_sensitive_controls_matched` | 40 real `gemma4:31b` outputs; two condition-blind judge receipts. Under one judge `substrate_workflow` beats `criteria_prompted_no_sources` by only **+1.25** (below the +1.5 bar) and misses the C4 critical-criterion margin against both controls; under the other judge `criteria_prompted_no_sources`, `vanilla`, and `famous_sources_supplied` **all tie the substrate at 6.00**. The two judges disagree on C5 for **20 of 40** outputs and C6 for **22 of 40** outputs, triggering the third-judge rule. |
| `diagnosis-vs-validated-learning-benefits-renewal-v3` | `c4_saturation_and_judge_count_insufficient` | 40 real `gemma4:31b` outputs; three blind-judge attempts (`gpt-oss:20b` failed calibration; Claude Opus 4.7 scored all 40 but is non-independent / circular — judge-variance only; hosted OpenAI `gpt-5.4-mini` passed calibration exactly and scored all 40 as the first eligible, independent pass). Under the eligible judge, `substrate_workflow` clears every total-score margin but the **C4 pass-rate margin against `vanilla_long_prompt` is +0.00** — substrate C4 = 1.00 and `vanilla_long_prompt` C4 = 1.00 — and the case has **only 1 of ≥2 required eligible judges**. |

Every per-case detail above is sourced from the committed `eval-decision.md`,
`score-sheet.md`, and `run-packet.md` in each case folder, plus the committed
judge receipts under each case's `judge-packet/`.

### 1. What the lab has learned

- **The eval-lab discipline works mechanically.** Frozen condition packets,
  hashed Advisor prompts, equal-length filler with forbidden-vocabulary scans,
  condition-blind anonymisation, pre-registered Positive-result and Falsifier
  rules, judge calibration gates, and aggregate-only reconciliation from
  committed hashes all functioned as designed across the three scored cases.
- **Negative outcomes are recordable without drift.** Each case ended in
  `do_not_promote` with a named `decision_class`, none of them lifted `## Result`,
  and none of them changed canon. The discipline that the result status policy
  prescribes — `partial` stays `partial` when the evidence does not clear the
  pre-registered rule — held in practice.
- **Cross-judge variance is the dominant signal so far.** The managerial case
  produced a margin swing of more than three points across judges; the v2 case
  produced a 20/40 and 22/40 split on C5/C6; the v3 case's two non-independent
  judges produced different criterion-level shapes than the one eligible
  independent judge.

### 2. What claims the current evidence does **not** support

- It does **not** support "Anti-Slop's substrate improves advice." The
  `## Result` of every contradiction-preservation case that has been scored is
  `partial` with `do_not_promote`.
- It does **not** support "substrate beats equal-length controls." The
  equal-length control beat the substrate by 0.33 under one judge in the
  managerial case, and the v3 substrate failed to discriminate against the
  equal-length control on the case's critical criterion (C4, both at 1.00).
- It does **not** support "a single high-scoring judge pass is enough." The
  Positive-result rule in each case requires at least two eligible blind
  judges from different model families with at least one independent of the
  orchestrating agent. No case currently meets that bar.

### 3. What narrower claims the current evidence **may** support

These are about the eval lab itself, not about the substrate's effect on advice.

- The discipline catches drift. Three cases ran to decision without any
  `## Result` being lifted on insufficient evidence, and three distinct failure
  mechanisms were classified by name. That is itself evidence that the
  pre-registered rules and the equal-length control are doing their job.
- Aggregate-only reconciliation from committed hashes (manifest body
  `sha256` joined to model-output receipts) is sufficient to reach a decision
  without committing a per-`OUT-NN` → condition answer key.
- The calibration-anchor gate has correctly excluded an ineligible judge in
  practice (v3's `gpt-oss:20b` calibration failure).

### 4. Failure patterns that repeat across cases

- **Criterion saturation against the equal-length control.** In v2, the
  substrate's C4 margin over `vanilla_long_prompt` and
  `criteria_prompted_no_sources` was below the pre-registered +0.33 bar
  (substrate cleared C4 but so did the controls). In v3, the substrate's C4
  pass rate is **1.00 against a `vanilla_long_prompt` C4 pass rate of 1.00**:
  the criterion does not discriminate.
- **Judge sensitivity.** The same blinded outputs produce different aggregate
  shapes under different judges. The managerial case's three-judge margin
  collapse and the v2 case's C5/C6 split are the clearest examples.
- **Eligible-judge and independent-judge bar not cleared.** v2 had two
  condition-blind judge receipts, but the case did not clear the required
  independent-judge and Positive-result bar: the Claude pass was
  non-independent / circular (orchestrating agent), the C5/C6 judge
  disagreement (20/40 and 22/40) triggered the third-judge rule, and neither
  judge cleared the pre-registered Positive-result rule. v3 has only one
  eligible independent judge across three blind-judge attempts, and so the
  ≥2-eligible-judges bar is not met.
- **Rubric items that judges can resolve in opposite directions.** The v2
  postmortem identifies C5 ("no flattening") and C6 ("concrete recommendation")
  as a built-in tension: a single-sided definite recommendation can be read as
  both `C5 pass` (reasoning preserved) and `C5 fail` (decision not kept open).
  Two judges resolved this contradiction in opposite directions, which
  propagated through the dependency rule to a large C5/C6 split.

### 5. What should stop now

- **Stop citing or implying that the substrate improves advice.** The current
  evidence is mixed and non-promotional. No `benchmark_supported` Result
  exists on any contradiction-preservation case; no canon candidate may use
  these results as benchmark evidence.
- **Stop re-running v2 or v3 generation.** Both are scored. Generating more
  outputs against the same frozen packets does not address the C4 saturation,
  the judge-eligibility gap, or the rubric-tension finding.
- **Stop adding conditions or judges to the existing cases** in the hope of
  reaching a positive result. The pre-registered rules are the rules. A v4
  case is the disciplined path; a quiet repair to v2 or v3 is not.
- **Do not introduce a new dashboard, a new gate, or a new receipt type for
  this memo.** The existing dashboards (`make eval-lab-status`,
  `make eval-benchmark-readiness`) and the existing receipt types are
  sufficient.

### 6. What v4 should test (if a v4 is drafted)

This list is a design prompt for a future goal, not an authorisation to start
drafting. It is sourced from the v2 `postmortem.md` and the v3
`eval-decision.md`.

- **A C4 — and C3 — that discriminates against the equal-length control.**
  The "under-evidence problem" criterion needs sharper wording, a scenario
  tweak that makes it harder for an unprimed long-prompt answer to surface, or
  both. A criterion saturating at 1.00 across substrate and control is not
  evidence about the substrate.
- **At least two eligible independent judges arranged before the run.**
  Different model families, at least one operated outside the orchestrating
  agent, both calibration-passing on the anchor file. The current "find a
  second eligible independent judge after the fact" path has produced a
  judge-count-insufficient outcome twice running.
- **Pre-registered handling of the C5 / C6 tension.** Either the rubric is
  rewritten so a single-sided recommendation has a single defined C5 verdict,
  or the dependency rule is reframed so a judge's "keep the decision open"
  vs "reach a recommendation" reading is not the load-bearing axis.
- **A holdout-style case, not a design-against-substrate case.** Per
  `docs/eval-lab-protocol.md` design-vs-holdout distinction, a case whose
  scenario and rubric were not shaped with substrate strengths in view is
  stronger evidence that any effect generalises.
- **Same controls, same instrumentation.** The equal-length control is still
  required. The frozen-packet rule, calibration-anchor gate, and aggregate-only
  reconciliation should be reused as-is.

## Stance

A model output is a test artifact, never an authority. A judge's score is a
test artifact about how one judge scored one set of answers under one rubric,
not evidence about the world. This memo confers no authority on any model
output, judge score, source card, claim/tension card, or canon candidate. The
substrate has not been shown to improve advice; the current evidence is mixed,
non-promotional, and consistent with the discipline doing its job.
