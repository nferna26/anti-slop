---
case_id: diagnosis-vs-validated-learning-benefits-renewal-v2
artifact: v3-design-prep
result_status: partial
prep_date: 2026-05-22
v3_status: design-prep — no v3 case drafted, no v3 benchmark frozen, no model run, no scoring
---

# v3 Eval-Design Prep — diagnosis-vs-validated-learning benefits-renewal

This is public-safe **design prep** for a future v3 of the
`diagnosis-vs-validated-learning` benefits-renewal contradiction-preservation eval.
It operationalises the lessons in `postmortem.md` into concrete, drafted rubric
text, a dependency rule, a control recipe, a calibration-anchor requirement, and a
scenario shape — the inputs a later goal needs to draft and freeze the actual v3
case.

## What this is and is not

- **Is:** a design specification. It contains drafted criterion wording and design
  requirements ready to be lifted into a v3 `case.md` / `run-packet.md`.
- **Is not:** a frozen case. No v3 `case.md`, scenario prose, Advisor prompt, run
  packet, or judge packet is created here. No model is run, nothing is judged or
  scored, and no `## Result` or status changes. The v2 case stays `partial` /
  `do_not_promote`.
- The v3 case, when drafted, opens a **new benchmark version** — proposed
  `diagnosis-vs-validated-learning-benefits-renewal-v2-v3`, or a fresh `-v3` case
  id at the operator's choice — and re-freezes. The v2 case and its receipts are
  the design / dry-run record and are not edited in place.

## Lineage

Built directly on `postmortem.md` in this folder, which analysed the v2
`do_not_promote` outcome. The five v2 failure surfaces this prep addresses: the
rubric's C5/C6 internal contradiction; C4 being too permissive (the v2 Advisor
prompt pre-answered it); the criteria-prompted control leaking the whole rubric;
the scenario's cheap constrained-hybrid escape hatch; and the absence of a
pre-registered independent-judge gate.

## What v3 keeps from v2 (the instrumentation worked)

The v2 design machinery was sound and carries over unchanged: freeze-before-run;
blind, condition-anonymised judging; the equal-length `vanilla_long_prompt` control
(it did its job — it scored *lowest* under both judges, cleanly ruling out a
more-tokens effect); ≥8 real runs per condition; one fixed generator; ≥2 blind
judges from different model families; per-criterion binary pass/fail scoring; a
pre-registered criterion dependency rule; a pre-registered positive rule and
falsifier. v3 changes only the rubric wording, the criteria-prompted control, the
scenario shape, the calibration-anchor requirement, and the judge-independence gate.

## v3 rubric draft — six binary criteria

Six criteria, each `pass`/`fail`, scored per condition per run; per-run score is the
count passed (0–6). C1–C3 are carried from v2 with C1 clarified; C4–C6 are rewritten.

**C1 — Identifies the live tension.**
Passes when the answer treats *both* approaches — diagnose the challenge from
existing evidence and act, and generate the missing evidence by cheap experiment
first — as legitimate, competing ways to read the decision. It scores **substantive
engagement** of both approaches, whether or not the answer attaches labels to them.
Fails when only one approach is presented, or the choice is treated as obvious.
*(v2 fix: C1 was judge-sensitive on literal labelling vs substantive engagement —
v3 fixes the bar on substantive engagement explicitly.)*

**C2 — Anchors in the scenario's specific facts.**
Passes when the answer uses the v3 scenario's load-bearing cues as actually
load-bearing — reasoning *from* them, not reciting them. Fails when it reasons
generically or treats the named cause as established. The specific-cue list is
re-pinned to the v3 scenario at case-drafting time (see `## v3 scenario shape`).

**C3 — Preserves the diagnosis-first objection.**
Passes when the answer keeps live, as a serious consideration bearing on its
recommendation, the diagnosis-first objection — that a real diagnosis singles out
what is *critical* from the available evidence, so scattered experiments may test
tactics without ever naming the critical cause, and that a confident-but-undisciplined
first guess is not a diagnosis. Fails when it omits this objection or sets it up as a
strawman. *(Carried from v2 — C3 was the one criterion that genuinely discriminated,
because the scenario does not spoon-feed it. Keep that property.)*

**C4 — Detects and uses the under-evidence problem.**
Passes when the answer, **without being told**, (a) recognises that the named cause
is not established — it identifies the gap between a plausible story and a tested
cause from the scenario's clues — and (b) connects that to why it matters *here*:
that an under-evidenced cause does not justify a near-irreversible, budget-consuming
commitment, and that the situation calls for generating the missing evidence. Fails
when it omits the objection, treats the working group's confidence as settling the
matter, or notes uncertainty only generically without doing (a)+(b).
*(v2 fix: v2 C4 was passed by parroting "no one has tested it" — a fact the v2
prompt handed the model. The v3 scenario must not state the cause is untested; C4
now requires the model to **detect** it. See `## v3 scenario shape`.)*

**C5 — Weighs the two objections against each other.**
Passes when the answer's reasoning actually **trades the two objections off** — it
engages how the diagnosis-first concern and the under-evidence concern pull in
opposite directions and works through that tension toward its recommendation. A
**definite, single-sided recommendation passes C5** as long as the reasoning weighed
the losing objection and explained why it is outweighed here. Fails when the answer
(a) **flattens** — commits to one side without engaging why the other side's
objection does not defeat it — or (b) **dissolves** the tension into an unspecified
"hybrid" / "both" that does not divide the tradeoff (which commitments are reversible,
which are not, how the binding constraint is met).
*(v2 fix: v2 C5 ("keeps the decision genuinely open") read as "do not decide" and
contradicted C6 ("reach a recommendation") — the contradiction drove the 20/40 C5
judge split. v3 C5 is about the **reasoning**, not the decision: reaching a clear
recommendation is fully compatible with passing C5.)*

**Why C5 is not just "C3 and C4."** C3 and C4 ask whether each objection is
*present and serious*. C5 asks whether the two are *weighed against each other*. An
answer can state both objections (pass C3 and C4) and still fail C5 — by listing
them and then picking one side without engaging the other, or by offering "a bit of
both" with no division of the tradeoff. C5 scores the tradeoff work, not the
presence of the objections.

**C6 — Concrete recommendation under the binding constraint.**
Passes when the answer (a) commits to a specific, actionable recommendation — a
named course of action, not a menu of options handed back to the asker; (b)
explicitly engages the scenario's binding constraint by its actual mechanism, and
does **not** rely on a move the scenario forecloses (e.g. deferring a funding
decision when the budget is non-reservable); (c) names a specific, plausible way
the recommendation could be wrong — a concrete failure path, not a generic hedge;
and (d) states at least one concrete, **observable** piece of evidence that would
change the recommendation — an observation that could actually be made. Fails when
any of (a)–(d) is missing.
*(v2 fix: v2 C6 was passed by any answer that gestured at "time pressure" and
"evidence" — v3 requires engagement with the *specific* binding mechanism and a
*concrete observable* disconfirmer.)*

## v3 criterion dependency rule — unambiguous, no judge discretion

The v2 rule used "should" language ("if C4 fails, C6 *should* fail; record a reason
if it passes") which left judges discretion. v3 makes every dependency a hard rule:

- **C5 requires C3 and C4.** A judge may **not** record `pass` for C5 on an output
  whose C3 *or* C4 it failed. You cannot weigh two objections against each other if
  one of them was never preserved.
- **C6 requires C5.** A judge may **not** record `pass` for C6 on an output whose C5
  it failed. A recommendation not built on a genuine weighing of both objections is
  not a sound recommendation under the constraint.
- **C1, C2, C3, C4 are scored independently** of each other and of the final
  recommendation. C3 may pass on an output whose C6 fails (C3 is necessary, not
  sufficient).

This yields a clean ladder: **C3 ∧ C4 → enables C5 → enables C6.** There is no
"reason required" escape and no criterion whose pass condition contradicts another's.

**Open question for case-drafting:** because C5 and C6 are now gated by C3/C4, the
six criteria are correlated by construction. The operator should confirm, when the
v3 positive rule is drafted, whether the pre-registered criterion-margin set stays
C4/C5/C6 or moves to the independent criteria — flagged, not decided here.

## v3 conditions — weaken the criteria-prompted control

Five conditions, four carried from v2 unchanged: `vanilla`, `famous_sources_supplied`,
`substrate_workflow`, `vanilla_long_prompt` (still equal-length-matched to the
`substrate_workflow` added material).

The fifth control is **rewritten and renamed**. v2's `criteria_prompted_no_sources`
paraphrased all six rubric criteria in operational detail — effectively the grading
key — so under a capable judge it sat at ceiling and could not be separated from the
substrate. v3 replaces it with a **generic advice-quality** control:

- **`generic_advice_prompted`** (proposed name) — a short preamble that asks only for
  *thorough, balanced, well-reasoned advice that takes the situation's tradeoffs
  seriously and is honest about what is uncertain*. It enumerates **no** criterion,
  names no reading, objection, "hybrid", "do not flatten", "reason against", or
  "disconfirming evidence", and supplies no source. It conveys advice-quality
  expectations only — the spirit, not the rubric. This isolates a substrate effect
  from a mere being-asked-for-good-advice effect, without handing the model the
  grading key.

*Optional extension (operator's call, not required):* keep a graded ladder — both a
weak `generic_advice_prompted` control and a stronger criteria-style control — so the
substrate is measured against a range. v3 prep recommends the single weakened control
for simplicity unless the operator wants the ladder.

## Judge calibration anchors — required pre-run artifact

To attack the v2 judge divergence (C5 differed on 20/40 outputs, C6 on 22/40), v3
**requires** a calibration-anchor artifact, frozen before any model is run.

- **Artifact.** `judge-packet/calibration-anchors.md` — a committed, condition-blind
  part of the judge packet. It contains a small set (recommend **3**) of **synthetic,
  hand-authored illustrative answers** — one a clear `pass` profile, one a clear
  low-score profile, one a deliberate borderline — each with the operator's reference
  C1–C6 verdicts and a one-line rationale per criterion.
- **Not model outputs.** The anchors are authored by the operator as rubric
  illustrations. They are explicitly not generated by any model, carry no condition,
  and are not part of the 40 scored outputs.
- **Freeze rule.** The anchor texts and their reference verdicts are authored and
  frozen at v3 case-drafting time, **before** the generator runs — same freeze
  discipline as the rubric itself.
- **Judge use.** Each judge scores the anchors first and checks its verdicts against
  the reference before scoring the real `OUT-NN` outputs. A judge whose anchor scores
  diverge materially from the reference recalibrates against the rationale or is
  recorded as miscalibrated; the run packet defines the divergence threshold.
- **Scope note.** This prep **defines the requirement and format** only. It does not
  author the anchor texts or their scores — that is part of drafting the v3 case,
  where the final rubric wording and scenario are fixed and the anchors can be
  written against them cleanly. Inventing scored anchors here, before the v3 scenario
  exists, would not be sound.

## v3 scenario shape — a costed trilemma, no free hybrid

The v2 scenario let a generic constrained hybrid pass the rubric almost by
construction: the Advisor prompt itself listed "do some constrained version of both"
as an option, and a cheap escape hatch existed — secure the funding line now, gate
the spend on the pilots — so the window constraint never truly bound. v3 must make
the hybrid a **real third horn with its own distinct, named cost**.

Keep the domain (a city benefits office, renewal completion has dropped, a fixed
funding window) — it fits the diagnosis-vs-validated-learning tension well. Change
the constraint structure:

1. **The budget is indivisible and non-reservable.** The funding is an all-or-nothing
   appropriation for *this* cycle: it cannot be partially reserved or its decision
   deferred. Take it now and it must be committed to a defined program now; decline
   it and it is gone for a year. This removes the v2 escape hatch ("secure funding,
   decide later").
2. **A partial commitment consumes the option it spends.** Any program funded this
   cycle uses staffing / contract capacity that then cannot be redeployed — a partial
   build is itself near-irreversible for the same horizon as a full build.
3. **The hybrid is a genuine third option with its own loss.** Make it concrete: a
   *partial* program funded now that addresses only one of the suspected causes. Its
   distinct cost — it spends the budget on a narrow bet that may miss the real cause,
   and it forecloses *both* a clean experiment and the full program. It is not "both,
   lite"; it is its own horn.

The result is a genuine **trilemma**, each horn carrying a real, distinct, named cost:
- **(A) Commit fully now** — bets nearly the whole budget, near-irreversibly, on a
  cause that is not established.
- **(B) Experiment first** — forfeits this cycle's funding entirely; the next window
  is a year out.
- **(C) Partial / hybrid commitment now** — spends the budget on a narrow bet that
  may address the wrong cause, and forecloses both a clean test and the full program.

No horn is free, so the rubric cannot be passed by reflexively selecting "the
hybrid."

Two further scenario rules, both operationalising postmortem lessons:

- **Do not spoon-feed the under-evidence problem (for C4).** The v3 scenario must
  *not* state that the named cause is untested. Present the working group as
  *confident* in its cause, and leave the under-evidence inferable from clues — for
  example, the evidence offered is correlational only, other changes happened in the
  same period, and no causal test has been run. C4 then requires the model to
  *detect* the gap, not echo a sentence.
- **Do not script the option menu (for C5).** The Advisor prompt should not bless "a
  constrained version of both" as a pre-named option. Present the situation and the
  stakeholders' positions and let the model construct and cost the option space
  itself. If options must be named for cross-condition comparability, name them only
  as stakeholders' positions, with the prompt itself endorsing none.

## Independent / human-judge gate — pre-registered for v3

v3 must pre-register, as a frozen `## Judge protocol` clause, that **no Result lift
above `partial` is possible until at least one judge that is not the orchestrating
agent has scored the packet** — ideally a human judge, or a genuinely external model
evaluation. A judge run inside the orchestrating session does not count toward the
two-independent-judge minimum. In v2 this was a retrospective caveat on the Claude
Opus pass; in v3 it is a gate set *before* the run.

## Open questions deferred to v3 case-drafting

This prep deliberately leaves the following to the goal that drafts and freezes the
v3 case:

1. The full v3 scenario prose and the Advisor prompt wording (shape is specified
   above; final prose is case-drafting work).
2. The calibration-anchor texts and their reference scores (authored against the
   final rubric and scenario).
3. Whether the positive-rule criterion-margin set stays C4/C5/C6 given the new
   dependency chain (see `## v3 criterion dependency rule`).
4. Final condition naming (`generic_advice_prompted` is proposed) and whether to add
   the optional graded-ladder second control.
5. The exact judge anchor-divergence threshold for the run packet.

## Discipline note

This is design prep. It promotes nothing, scores nothing, runs no model, and confers
no authority on any model output, judge score, source card, or tension card. The v2
case stays `partial` and `do_not_promote`; nothing here changes that. A model output,
and a judge's score of one, is a test artifact — never an authority, never citable as
a source.
