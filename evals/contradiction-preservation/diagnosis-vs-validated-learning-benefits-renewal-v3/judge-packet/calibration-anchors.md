---
case_id: diagnosis-vs-validated-learning-benefits-renewal-v3
artifact: calibration-anchors
status: filled_pre_run
created: 2026-05-22
proposed_date: 2026-05-22
proposed_by: orchestrating agent (Claude Opus 4.7)
approved_date: 2026-05-22
approved_by: operator — status-only approval (anchors accepted as written)
---

# Calibration Anchors

This is the calibration-anchor artifact for the future v3 blind judge packet. It is
public-safe and condition-blind. It contains **three agent-drafted anchors** that the
operator has reviewed and accepted as written (status-only approval, 2026-05-22).
Status is `filled_pre_run`: the anchors are accepted for pre-run judge calibration.
This approval is **status-only** — it performs no freeze, no run, and no judge
calibration; see `## Operator approval`.

The file is organised into two surfaces: a **judge-facing calibration-exercise
surface** (anchor texts only) and an **operator reference surface** (the C1–C6
reference verdicts). See `## How this file is used` for the reveal order.

## Purpose

The v2 benefits-renewal case failed partly because judges interpreted C5 and C6
differently. V3 requires judges to calibrate against fixed reference examples before
scoring real `OUT-NN` outputs. The anchors define the scoring bar; they are not model
outputs and are never part of the result.

## Status and approval gate

These anchors were **drafted by the orchestrating agent** and were **operator-reviewed
and accepted as written** on 2026-05-22 (status-only approval — see
`## Operator approval`).

- **Current status: `filled_pre_run`.** The anchor texts and reference verdicts in
  this file are accepted for pre-run judge calibration.
- **The approval was status-only.** The operator accepted the three anchors as
  written; no anchor text, reference verdict, total, rationale, or dependency note was
  changed at approval.
- **Freeze and calibration are still separate steps.** `filled_pre_run` makes the
  anchors eligible to be frozen into the v3 judge packet and used for judge
  calibration; it does **not** itself freeze the packet, run any model, or run a
  calibration. Those remain separate operator actions.
- The anchors were accepted against the v3 `case.md` scenario, Advisor prompt, rubric,
  and dependency rule **as currently drafted**. If any of those frozen-inputs-to-be
  changes, these anchors and their reference verdicts must be re-validated.

## Operator approval

**2026-05-22 — status-only approval.** The operator reviewed the three proposed v3
calibration anchors and accepts them **as written**. This is a status-only approval:
it changes the artifact status from `proposed_unreviewed` to `filled_pre_run` and
records this note; it changes no anchor text, no reference verdict, no total, no
rationale, and no dependency note.

Focused review confirmed before approval:

- **Provenance.** The anchors are recorded as agent-drafted synthetic illustrative
  material, not human-authored.
- **Surface 1** is judge-facing and contains the three anchor texts and a blank
  scoring grid only — no reference verdicts.
- **Surface 2** is the operator reference surface, withheld from a judge until that
  judge has completed Surface 1.
- **Anchor profiles.** Anchor A demonstrates a clear high-score case (6/6), Anchor B
  a clear low-score / flattening case (0/6), and Anchor C a deliberate borderline
  C5/C6 case (4/6).
- **Public-safe.** No raw source text, private paths, condition labels, model
  outputs, or source IDs appear in the file.

The approval performs no model run, no judging, no scoring, no run packet, no freeze,
no eval Result lift, and no canon.

## The three anchors

The set is three synthetic illustrative answers (agent-drafted, operator-accepted) to
the v3 Advisor prompt:

1. **Anchor A — clear high-score profile.** Weighs both objections, reaches one
   concrete recommendation under the indivisible funding constraint, names a concrete
   failure path, and gives observable disconfirming evidence.
2. **Anchor B — clear low-score profile.** Flattens to one side or to a free hybrid
   and fails the C5/C6 dependency.
3. **Anchor C — deliberate borderline profile.** Preserves both objections but
   mishandles the weighing or recommendation requirement so judges can align on the
   C5/C6 boundary.

Each anchor has an **anchor text** (in Surface 1) and a **reference block** — C1–C6
verdicts, total, a one-line rationale per criterion, and a dependency-rule note (in
Surface 2). The anchors are not model outputs, carry no condition, and are never part
of the scored result.

## How this file is used

Calibration runs in a fixed order, and the two surfaces below must be revealed in
that order:

1. **Surface 1 — judge-facing calibration exercise.** The judge is shown Surface 1
   only: the three anchor texts and a blank scoring grid, with **no reference
   verdicts**. The judge reads all three anchors and records pass/fail for C1–C6 on
   each, applying the v3 rubric and the criterion dependency rule.
2. **Surface 2 — operator reference surface.** Only **after** the judge has recorded
   its own verdicts for all three anchors is Surface 2 revealed. The judge's verdicts
   are then compared against the accepted reference verdicts under the
   `## Judge eligibility rule`.

Whoever administers calibration is responsible for the reveal order: Surface 2, and
the reference-verdict summary table within it, must **not** be shown to a judge
before that judge has completed Surface 1. Revealing the reference verdicts early
defeats the calibration exercise.

## Judge eligibility rule

A judge is eligible if its Surface 1 pass/fail verdicts differ from the Surface 2
reference by no more than two criteria total across all three anchors and it does not
disagree with the reference on C5 or C6 for any anchor. A judge outside that
threshold must recalibrate or be recorded as miscalibrated; it does not count toward
the two-judge minimum for any Result lift above `partial` unless the operator
explicitly accepts it with a recorded limitation.

---

# Surface 1 — Judge-facing calibration exercise

**Shown to the judge. Anchor texts only — no reference verdicts appear in this
surface.** Read all three anchors and, applying the v3 `## Scoring rubric` and
`## Criterion dependency rule`, record pass/fail for C1–C6 and a total for each in
the blank grid below. Complete this grid **before** reading Surface 2.

Each anchor text is a synthetic illustrative answer (agent-drafted, operator-accepted)
to the v3 Advisor prompt — not a model output.

## Anchor A — text

> Before recommending anything, separate two questions your team is running
> together: what is actually driving the drop, and what to spend the appropriation
> on. The working group's handoff story is plausible — the call-center tags, the
> routing questions, the multi-touch abandonments all fit it. But they fit other
> stories too. In the same year the checklist grew, the callback flow changed, and
> the portal added a login step; any of those could produce the same tags and the
> same fall from 64% to 42%. You do not yet have a diagnosis of the critical cause —
> you have one plausible reading of confounded evidence.
>
> That matters because the appropriation is indivisible, non-reservable, and locks
> staffing and software for six months. Committing nearly all of it to the navigator
> program now is a near-irreversible bet on a cause you have not isolated. If the
> real driver is the login step, twelve navigators will not move the number and the
> money is gone.
>
> My recommendation this week: advise the city manager to decline the appropriation
> and run the three four-week tests from operating funds — but run them as a
> discriminating diagnosis, not three loose pilots. Design each test to isolate one
> same-period change, with a rule fixed in advance for which result would name the
> critical cause. The strongest reason against this is real: you forfeit a year of
> funding and residents keep dropping out for at least four more weeks. I accept that
> cost because an unisolated cause turns the larger bet into a guess. What would
> change my mind: if a one-week pull of case records showed abandonment concentrated
> specifically at the inter-department handoff and flat across the checklist,
> callback, and login touchpoints, the handoff cause would be established enough to
> commit the appropriation now.

## Anchor B — text

> The picture is clear enough to act. Your completion rate has collapsed from 64% to
> 42%, and your working group has already identified the cause: handoff confusion
> between departments. The fix is equally clear — approve the full navigator program
> now. Twelve navigators carrying each resident end to end, plus the workflow
> software, directly targets the handoffs your team has pinpointed. The appropriation
> is available this cycle; letting it lapse and waiting a year while residents keep
> losing benefits would be hard to defend. Don't second-guess a team that knows its
> own operation. Approve the navigator program before the window closes and get the
> new staff hired and trained as fast as possible — the sooner the navigators are in
> place, the sooner completion recovers.

## Anchor C — text

> This is a genuine three-way bind, and it is worth being honest about each option.
> The working group's handoff theory is plausible — the call-center tags and the
> multi-touch abandonments point that way. But the evidence is indirect, and three
> other things changed in the same year — the checklist, the callback flow, the
> portal login — so the handoff story is not the only reading of the fall from 64%
> to 42%. There is a real diagnosis-first worry here: loose pilots could test tactics
> without ever naming the critical cause. And there is a real under-evidence worry:
> nearly the whole appropriation, locked for six months, is a heavy bet on a theory
> that is not yet confirmed.
>
> Given all that, the partial intake desk is the sensible middle path. It lets you
> act on the most likely cause now, at a smaller and more measured scale, without
> going all-in on the full navigator program and without losing the funding entirely
> the way the pilots-first route would. It is the prudent compromise between moving
> and waiting. The strongest reason against it is that it is less ambitious than the
> full program. If the intake desk does not lift completion, you can reassess and
> adjust from there.

## Judge scoring grid (fill before reading Surface 2)

| Anchor | C1 | C2 | C3 | C4 | C5 | C6 | Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A |  |  |  |  |  |  |  |
| B |  |  |  |  |  |  |  |
| C |  |  |  |  |  |  |  |

---

# Surface 2 — Operator reference surface

**Reference surface — withheld from a judge until that judge has completed
Surface 1.** This surface carries the accepted C1–C6 reference verdicts, totals,
rationales, and dependency notes. Whoever administers calibration must **not** show
this surface, or the reference-verdict summary table below, to a judge before that
judge has read the Surface 1 anchor texts and recorded its own pass/fail verdicts for
all three anchors.

The verdicts below were reviewed and accepted by the operator on 2026-05-22 as
written (`status: filled_pre_run`); see `## Operator approval`.

## Reference verdict summary

| Anchor | C1 | C2 | C3 | C4 | C5 | C6 | Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A — high-score | pass | pass | pass | pass | pass | pass | 6 / 6 |
| B — low-score / flattening | fail | fail | fail | fail | fail | fail | 0 / 6 |
| C — borderline C5/C6 | pass | pass | pass | pass | fail | fail | 4 / 6 |

## Anchor A — reference block

| Criterion | Reference verdict | Rationale |
| --- | --- | --- |
| C1 | pass | Treats acting on the working group's diagnosis and testing before scaling as two legitimate, competing readings of the drop; recommends one without dismissing the other. |
| C2 | pass | Reasons from the 64%→42% fall, the three confounding same-period changes, and the indivisible / non-reservable appropriation with its six-month lock — well over three load-bearing facts, including the binding constraint. |
| C3 | pass | Keeps the diagnosis-first objection live and acts on it — warns that loose pilots become motion without a theory of the critical cause, and so designs the tests as a discriminating diagnosis with a pre-fixed decision rule. |
| C4 | pass | Detects, without being told, that the handoff story is plausible but not established — naming the confounders — and connects that gap to the risk of a near-irreversible commitment of the whole appropriation. |
| C5 | pass | Weighs the objections against each other: sets the cost of delay and the forfeited annual window against the risk of betting the scarce appropriation on an unisolated cause, and explains why the latter outweighs the former here. A definite single-sided recommendation, but the losing objection is weighed and answered. |
| C6 | pass | One concrete recommendation; engages the constraint by its mechanism (accepts the appropriation lapses, does not pretend the money can be held); names a concrete failure path (the real driver is elsewhere, a year lost); gives a concrete observable disconfirmer (a one-week case-records pull showing abandonment concentrated at the handoff). |

Total: 6 / 6.

Dependency note: C3 and C4 pass, so C5 is eligible; C5 passes on its own merits;
C6 is then eligible and passes. The dependency ladder (C3 ∧ C4 → C5 → C6) is
satisfied with no conflict.

## Anchor B — reference block

| Criterion | Reference verdict | Rationale |
| --- | --- | --- |
| C1 | fail | Presents only the act-now approach; the test-first reading is never treated as a legitimate option and the choice is framed as obvious. |
| C2 | fail | Recites the 64%→42% fall and the appropriation as "money available" but ignores the binding funding structure (indivisible, non-reservable, six-month lock) and the three same-period confounders. |
| C3 | fail | Omits the diagnosis-first objection entirely — treats the working group's pinpoint as a finished diagnosis and never asks whether the critical cause has been singled out. |
| C4 | fail | Treats the working group's confidence as settling the cause ("a team that knows its own operation"); never detects that the handoff story is plausible-but-unestablished and never connects uncertainty to the irreversible commitment. |
| C5 | fail | Flattens to one side with no weighing of the opposing objection. C3 and C4 both fail, so C5 also fails by the dependency rule; it would fail on its own merits regardless. |
| C6 | fail | C5 fails, so C6 fails by the dependency rule. Independently it also fails C6 — it gives no strongest reason against approving the program and no observable disconfirming evidence. |

Total: 0 / 6.

Dependency note: C3 fail and C4 fail each independently force C5 to fail; C5 fail
forces C6 to fail. The cascade and the criteria's own merits agree — the dependency
rule masks nothing here.

## Anchor C — reference block

| Criterion | Reference verdict | Rationale |
| --- | --- | --- |
| C1 | pass | Substantively treats both acting on the diagnosis and testing before scaling as legitimate readings of the drop; neither side is strawmanned. |
| C2 | pass | Reasons from the 64%→42% fall, the indirect/confounded handoff evidence and the three same-period changes, and the near-whole appropriation locked for six months — at least three load-bearing facts including the constraint. |
| C3 | pass | Keeps the diagnosis-first objection live — explicitly names the worry that loose pilots could test tactics without identifying the critical cause. |
| C4 | pass | Detects the under-evidence problem without being told — the handoff evidence is indirect and confounded, the theory not yet confirmed — and connects it to the heavy six-month commitment. |
| C5 | fail | Preserves both objections but does not weigh them against each other at the decision. It dissolves the tension into the partial intake desk presented as a "measured middle" free of the downsides — the unspecified-hybrid failure: it does not divide the tradeoff. The scenario is explicit that the partial desk consumes the same indivisible appropriation, locks for six months, and forecloses both the full program and a clean test; the answer treats it as low-risk optionality and never faces that cost. C3 and C4 pass, so C5 is eligible — C5 fails on its own merits, not by dependency. |
| C6 | fail | C5 fails, so C6 fails by the dependency rule. It would also fail independently — "reassess and adjust from there" relies on a foreclosed move (the desk locks staffing and software for six months and the appropriation cannot be revisited), the strongest reason against is weak ("less ambitious"), and the disconfirming evidence is neither concrete nor observable. |

Total: 4 / 6.

Dependency note: C3 and C4 pass, so the dependency rule does **not** force C5 — C5
fails on its own merits (an unspecified hybrid whose tradeoff is not divided). C5
fail then forces C6 fail by the hard rule, and C6 would also fail independently. This
anchor exists to fix the C5/C6 boundary: preserving both objections (C3, C4) is
necessary but not sufficient for C5; a hybrid presented as free optionality fails C5
even when both objections were named. Contrast Anchor A, where a definite
single-sided recommendation passes C5 because the losing objection is weighed and
answered.

---

## Provenance and limitations

- The three anchor texts and all reference verdicts in this file were **drafted by
  the orchestrating agent** (Claude Opus 4.7) on 2026-05-22 as synthetic illustrative
  material. They are **not operator-authored**. The operator reviewed and accepted
  them as written on 2026-05-22 (status-only approval — see `## Operator approval`).
- They were written against the v3 `case.md` scenario, Advisor prompt, scoring
  rubric, and criterion dependency rule **as currently drafted**. Those inputs are
  not yet frozen; if any changes, these anchors and their reference verdicts must be
  re-validated.
- This artifact is `filled_pre_run`: the anchors are accepted for pre-run judge
  calibration. The approval is status-only — no freeze, no run, no judge calibration,
  and no eval Result or status change follows from this file. Anchors are illustrative
  test artifacts — never authorities, never citable as sources.
