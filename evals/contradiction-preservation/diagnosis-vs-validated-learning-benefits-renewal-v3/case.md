---
case_id: diagnosis-vs-validated-learning-benefits-renewal-v3
eval_type: contradiction-preservation
status: draft
created: 2026-05-22
source_packet: reviewed_public_artifact_packet
expected_output: tension-aware constrained recommendation
model_conditions:
  - vanilla
  - famous_sources_supplied
  - substrate_workflow
  - vanilla_long_prompt
  - generic_advice_prompted
scoring_status: unscored
---

# Eval Case

## What this eval tests

This is the v3 scaffold for the `diagnosis-vs-validated-learning` benefits-renewal
contradiction-preservation eval. It tests whether an advisor can preserve the
tension between acting from a disciplined diagnosis and generating missing evidence
through cheap tests when the decision has a binding resource constraint.

It is drafted from the v2 postmortem and `v3-design-prep.md`. The v2 case remains
the design / dry-run record and stays `partial` / `do_not_promote`; this v3 scaffold
does not edit or supersede v2 receipts. No model has been run for v3, no outputs
exist, nothing is scored, and no `## Result` or canon status is promoted.

## Lineage

- `strategy-diagnosis-vs-validated-learning` - reviewed claim/tension card
  (synthesis-level). The live tension: disciplined strategy starts from a diagnosis
  of the critical challenge, while validated learning treats the diagnosis itself as
  a hypothesis when the facts are not yet known.
- `BK-0001-card-001` - reviewed source card (evidence-level). Carries the
  diagnosis-first side: a strategy kernel begins with a diagnosis that singles out
  what is critical, and action should cohere with that diagnosis.
- `BK-0007-card-001` - reviewed source card (evidence-level). Carries the
  validated-learning side: under uncertainty, progress comes from testing
  assumptions against real behavior rather than treating activity or conviction as
  learning.

No book map is evidence for this case. Book maps are discovery aids only. The
source cards are evidence-level, the claim/tension card is synthesis-level, and none
of them is canon.

## Scenario

Synthetic and invented - no real person, office, or program.

Riverton's city benefits office helps residents renew food and housing assistance.
Over the past year, the completion rate for started renewals fell from 64% to 42%.
The director has one week to advise the city manager before a one-time improvement
appropriation is allocated.

A staff working group is confident that the main problem is handoff confusion. Their
evidence is plausible but indirect: call-center tags show many residents asking
where their case sits, caseworker interviews mention repeated document routing
questions, and several abandoned renewals had multiple department touches. During
the same period, however, three other things changed: the document checklist grew,
the phone vendor changed its callback flow, and the online portal added a new login
step. The same facts can support a handoff story, but they do not by themselves
show that handoffs are the critical cause.

The appropriation is indivisible and non-reservable. If Riverton accepts it this
cycle, it must commit it now to a named program; it cannot hold the money while
waiting for pilot results. If Riverton declines it, the money returns to the city
pool and the next comparable window is a year away.

Three staff positions are being argued:

- **Full navigator program now.** Hire 12 navigators and buy workflow software so
  one named staff member carries each resident from first contact to submission.
  This uses nearly the entire appropriation and locks staffing and software
  commitments for at least six months.
- **Pilots first.** Use ordinary operating funds for three four-week, reversible
  tests: document reminders, a callback scheduler, and a two-person navigator
  prototype. The pilots probe different possible causes, but choosing them means
  letting this cycle's appropriation lapse.
- **Partial intake desk now.** Accept the appropriation but fund a narrower intake
  desk that fixes only the first handoff and uses a smaller software module. This
  is not free optionality: it consumes the same one-time appropriation, locks a
  narrower handoff bet for six months, and forecloses both the full navigator
  program and a clean pilot-first test this year.

The case is built as a trilemma. The full program bets heavily on a plausible but
not-established cause. The pilot path generates evidence but forfeits a real annual
funding window. The partial program is not "both"; it is a third bet that spends the
scarce option on a narrower version of the same causal story.

## Advisor prompt

> I run Riverton's city benefits office. We help residents renew food and housing
> assistance. Over the past year, the share of residents who start a renewal and
> finish it fell from 64% to 42%.
>
> A staff working group is confident the main problem is handoff confusion. Their
> evidence is plausible: call-center tags show many residents asking where their
> case sits, caseworker interviews mention repeated document routing questions,
> and several abandoned renewals had multiple department touches. During the same
> period, the document checklist grew, the phone vendor changed its callback flow,
> and the online portal added a new login step.
>
> I have one week to advise the city manager before a one-time improvement
> appropriation is allocated. The money is indivisible and non-reservable: if we
> accept it this cycle, we must commit it now to a named program; we cannot hold it
> while waiting for later results. If we decline it, the money returns to the city
> pool and the next comparable window is a year away.
>
> Three positions are being argued. The working group wants a full navigator
> program now: 12 navigators plus workflow software, using nearly the whole
> appropriation and locking staffing and software commitments for at least six
> months. The deputy director wants to let the appropriation go and run three
> four-week, reversible tests from ordinary operating funds: document reminders, a
> callback scheduler, and a two-person navigator prototype. The finance office has
> floated a partial intake desk now: accept the appropriation but spend it on a
> narrower first-handoff desk and a smaller software module; that would also lock
> the money for six months and would foreclose both the full navigator program and
> a clean pilot-first test this year.
>
> What should I recommend this week? Give one concrete recommendation, the
> strongest reason against it, and the observable evidence that would change your
> mind.

## Expected reasoning

A good answer must:

1. Treat diagnosis-and-act and validate-before-scale as live, competing readings.
   It may recommend one of them, but it must not treat either as obvious.
2. Use the scenario's load-bearing facts, especially the 64% to 42% fall, the
   indirect nature of the handoff evidence, the same-period changes, the
   indivisible non-reservable appropriation, the six-month lock-in, and the
   one-year delay if the money lapses.
3. Preserve the diagnosis-first objection: scattered pilots can become motion
   without a theory of the critical cause, and the working group may have named a
   plausible story without yet making it a disciplined diagnosis.
4. Preserve the validated-learning objection: a plausible handoff story is not the
   same as a tested cause, and a near-irreversible commitment could spend the scarce
   option on the wrong problem.
5. Weigh those objections against each other rather than merely listing them. A
   definite recommendation can pass if it explains why the losing objection is
   outweighed in this scenario.
6. Give a concrete recommendation under the actual constraint. The answer must not
   pretend the appropriation can be reserved, split without cost, or revisited
   after pilots. It must name a concrete failure path and a concrete observable
   disconfirmer.

## Expected source behavior

- `vanilla` - Advisor prompt only. Baseline; expect generic operational advice,
  premature confidence in one position, or a low-cost synthesis that the scenario
  actually forecloses.
- `famous_sources_supplied` - Advisor prompt plus name-level awareness of relevant
  famous books and decoys only. It supplies no claim about what any source argues,
  no framework summary, no source-card text, and no tension-card text. It tests
  whether famous-name priming or model memory reproduces the substrate effect.
- `substrate_workflow` - Advisor prompt plus the reviewed public claim/tension card
  and reviewed public source cards named in `## Lineage`. The packet must contain
  no raw source text, no book-map evidence, and no canon language. The artifacts are
  evidence aids, not authorities that settle the case.
- `vanilla_long_prompt` - Advisor prompt plus neutral filler length-matched to the
  `substrate_workflow` added material, with no substrate artifacts and no
  domain-adjacent advice. It separates a substrate effect from a prompt-length
  effect.
- `generic_advice_prompted` - Advisor prompt plus only a short generic request for
  thorough, balanced, well-reasoned advice that takes tradeoffs seriously and is
  honest about uncertainty. It must not enumerate this rubric, name the two
  readings, mention "no flattening", ask for disconfirming evidence, or leak an
  answer key. It separates a substrate effect from being asked for better advice.

A correct answer never treats a source card, tension card, book, author, model
output, or judge score as canon.

## Failure modes

- **Commit-now flattening.** Treats the working group's plausible handoff story as
  enough to justify the full navigator program without facing the under-evidence
  problem.
- **Pilot-first flattening.** Treats testing as always superior without owning the
  lost annual appropriation and the cost of delay.
- **Free hybrid.** Recommends "some of both" while pretending the money can be held,
  split without consequence, or converted later into the full program.
- **Partial-program laundering.** Calls the intake desk a prudent compromise without
  recognizing that it spends the same scarce option on a narrower causal bet.
- **Source prestige.** Uses a famous book, framework, source card, or tension card as
  the authority that settles the case rather than reasoning from the scenario.
- **Prompt recitation.** Repeats facts without using them to decide whether the
  diagnosis is strong enough or whether the testing cost is worth paying.

## Scoring rubric

Six criteria, each scored **pass** or **fail** per output. Per-output score is the
count passed (0-6). Score against this rubric only; do not add, remove, or re-weight
criteria after outputs exist.

| # | Criterion | Passes when... | Fails when... |
|---|---|---|---|
| C1 | Identifies the live tension | the answer substantively treats diagnosis-and-act and validate-before-scale as legitimate, competing approaches to this decision, with or without labels | it presents only one approach, treats the choice as obvious, or makes the other side a strawman |
| C2 | Anchors in scenario facts | it reasons from at least three load-bearing scenario facts, including at least one constraint fact about the appropriation or lock-in | it is generic, merely recites facts, invents material facts, or ignores the binding funding structure |
| C3 | Preserves the diagnosis-first objection | it keeps live the objection that action needs a disciplined diagnosis of the critical cause, and that scattered pilots may test tactics without identifying what matters most | it ignores this objection, treats experimentation as automatically superior, or caricatures diagnosis as endless analysis |
| C4 | Detects and uses the under-evidence problem | it infers from the scenario that the handoff story is plausible but not established, and connects that gap to the risk of a near-irreversible budget commitment | it treats the working group's confidence as settling the cause, notes uncertainty only generically, or fails to connect uncertainty to the commitment |
| C5 | Weighs the two objections against each other | it trades the diagnosis-first and under-evidence objections off in the reasoning; a definite single-sided recommendation can pass if the losing objection is weighed and answered | it lists both objections without weighing them, commits to one side while ignoring the other, or dissolves the tension into an unspecified "hybrid" |
| C6 | Concrete recommendation under the binding constraint | it gives one actionable recommendation, engages the indivisible non-reservable appropriation and six-month lock-in, names a concrete failure path, and states observable evidence that would change the recommendation | it hands back a menu, relies on a foreclosed move, gives no strongest reason against its choice, or gives only generic disconfirming evidence |

The eval's signal is comparative across runs and conditions. A single high-scoring
answer is not a result.

## Criterion dependency rule

These dependencies are pre-registered for v3 and leave no judge-discretion escape:

- **C5 requires C3 and C4.** A judge may not record `pass` for C5 if the same output
  failed C3 or C4.
- **C6 requires C5.** A judge may not record `pass` for C6 if the same output failed
  C5.
- **C1, C2, C3, and C4 are otherwise scored independently.** C3 may pass even when
  C6 fails; preserving one objection is necessary, not sufficient.

The ladder is: **C3 and C4 enable C5; C5 enables C6.**

## Positive result

This draft pre-registers the v3 positive rule for the future frozen benchmark pass.
The result may be considered for `benchmark_supported` only if every clause below is
met and the broader `docs/eval-benchmark-upgrade.md` checklist also passes.

- **Run completeness.** At least 8 real runs per declared condition, no simulated
  outputs in the comparison set, a current receipt index, and complete benchmark
  provenance for every scored receipt.
- **Judge eligibility.** At least two eligible blind judges from different model
  families score the packet. At least one eligible judge must be independent of the
  orchestrating agent, preferably a human or externally operated model judge. A
  judge counts as eligible only if it completes the calibration-anchor step in
  `judge-packet/calibration-anchors.md` within the pre-registered threshold.
- **Total-score margin.** The `substrate_workflow` mean score beats
  `vanilla_long_prompt` and `generic_advice_prompted` by at least 1.0 point on the
  0-6 scale, beats `famous_sources_supplied` by at least 0.75 point, and beats
  `vanilla` by at least 1.25 points.
- **Critical-criterion margin.** Against both `vanilla_long_prompt` and
  `generic_advice_prompted`, `substrate_workflow` pass rates exceed the control by
  at least 0.20 on C3, C4, C5, and C6, and the substrate pass rate is at least 0.60
  on C5 and C6.
- **Judge-level stability.** Each eligible judge independently shows
  `substrate_workflow` beating both `vanilla_long_prompt` and
  `generic_advice_prompted` by at least 0.75 point on mean total score. If only the
  averaged judge score meets the margin, the result is judge-sensitive and stays
  `partial`.

Only if all clauses hold may a later goal consider lifting the Result above
`partial`. Even then, model outputs remain test artifacts, not authorities.

## Falsifier

This eval does not support the substrate hypothesis if any of the following occurs:

- `vanilla_long_prompt` matches or beats `substrate_workflow` within the
  pre-registered margin, suggesting a prompt-length effect.
- `generic_advice_prompted` matches or beats `substrate_workflow` within the
  pre-registered margin, suggesting generic advice-quality prompting explains the
  effect.
- `famous_sources_supplied` matches or beats `substrate_workflow` within the
  pre-registered margin, suggesting famous-source priming or model memory explains
  the effect.
- `substrate_workflow` wins total score but does not win C3, C4, C5, and C6 against
  both controls.
- The positive read depends on choosing a favorable judge, or eligible judges
  disagree on whether the positive rule is met.

In those cases the result stays `partial`, becomes `inconclusive`, or becomes
`falsified`, depending on the scored pattern. Do not cite it as benchmark-supported
evidence.

## Judge protocol

- **Calibration first.** Before scoring real outputs, each judge scores the frozen
  anchors in `judge-packet/calibration-anchors.md` and compares its verdicts with
  the reference verdicts. A judge whose anchor pass/fail verdicts differ from the
  reference by more than two criteria total, or differ on C5 or C6 for any anchor,
  is not eligible until recalibrated or explicitly accepted by the operator with a
  recorded limitation.
- **Blind and condition-anonymised.** Generated outputs are anonymised before any
  judge sees them. Judges see `OUT-NN` labels only, never condition names, seeds, or
  the answer key.
- **At least two eligible judges.** Judges must be from different model families
  when model judges are used; at least one eligible judge must be independent of the
  orchestrating agent before any Result lift above `partial`.
- **Criterion-level scoring.** Judges record pass/fail for C1-C6, total score, and
  a short rationale for every output, applying the dependency rule exactly.
- **Third-judge trigger.** A third eligible blind judge is required if the first two
  eligible judges disagree on C5 or C6 for more than 20% of outputs, disagree on
  any condition's pass-rate margin by more than 0.20, or disagree on whether the
  positive rule is met.
- **Judge-sensitive outcomes stay `partial`.** If the positive result depends on
  judge selection or on a fragile aggregation choice, it is not a win.

## Calibration-anchor requirement

The future frozen judge packet must include `judge-packet/calibration-anchors.md`.
That file holds three agent-drafted anchors that the operator reviewed and accepted
as written on 2026-05-22 (status-only approval); the file is now
`status: filled_pre_run` — the anchors are accepted for pre-run judge calibration. A
separate operator action is still required to freeze the v3 benchmark packet.

The anchor file must contain three synthetic illustrative answers (agent-drafted) to
this v3 scenario:

1. a clear high-score answer that weighs both objections and makes a concrete
   recommendation under the funding constraint;
2. a clear low-score answer that flattens the case to one side or a free hybrid;
3. a deliberate borderline answer that preserves both objections but mishandles C5
   or C6.

Each anchor must include reference C1-C6 verdicts and one-line rationales. Anchors
are not model outputs, carry no condition, and are never part of the scored result.
The anchor file is organised into two surfaces — a judge-facing calibration-exercise
surface (anchor texts only) and an operator reference surface (the C1-C6 reference
verdicts) — and a judge is shown the reference surface only after recording its own
anchor verdicts.

## Anti-overfitting safeguards

- Freeze the Advisor prompt, condition recipes, rubric, dependency rule, positive
  result, falsifier, calibration anchors, judge protocol, and run count before any
  model output is generated.
- Do not edit the rubric, scenario, anchors, or judge instructions after outputs
  exist. A needed change starts a new benchmark version.
- Do not inspect condition-labelled outputs before anonymisation.
- Do not edit source cards or the tension card to make the eval pass.
- Record all timeouts, exclusions, and failed attempts; do not replace an awkward
  output without a public receipt of the attempt.

## Model outputs

None yet for v3. `model-outputs/.gitkeep` is present only to hold the folder. Any
future output must be a real model-output receipt with full provenance before it can
contribute to a benchmark result.

`run-packet.md` freezes the v3 condition packet recipes, packet hashes, the
equal-length filler and its scan, the run parameters, and the judge-packet
structure for benchmark version `diagnosis-vs-validated-learning-benefits-renewal-v3-v1`.
Its inputs are frozen, but **no run has occurred and no model outputs exist**.

## Score sheet

See `score-sheet.md` in this case folder. It is an unscored scaffold with
`## Result: partial`, a judge-facing blind scoring surface, and an operator-only
post-reconciliation aggregate surface.

## Judge notes

No judge pass exists for v3. The first future judge packet must include completed
calibration anchors, condition-neutral case context, condition-neutral rubric,
blind scoring instructions, anonymised outputs, and an output manifest. No
`OUT-NN` -> condition answer key may be committed.
