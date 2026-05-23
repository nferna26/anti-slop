---
case_id: normalization-vs-latent-errors-water-treatment-v4
artifact: calibration-anchors
status: proposed_unreviewed
created: 2026-05-22
proposed_date: 2026-05-22
proposed_by: Codex agent — not operator-reviewed
---

# Calibration Anchors

This file is required before any v4 freeze, model run, or judge-packet release.
It is currently filled with agent-drafted proposed anchors. Do not run or judge
`normalization-vs-latent-errors-water-treatment-v4` until this file is
operator-reviewed and set to `status: filled_pre_run`.

The anchors calibrate judges on the C3/C4 -> C5 -> C6 boundary in `case.md`.
They are not model outputs, not evidence, not canon, and not scored results.

## Status and approval gate

Current status: `proposed_unreviewed`.

Required before freeze:

- Operator review recorded in this file.
- Frontmatter status changed to `filled_pre_run`.
- Any operator changes to anchor texts or reference verdicts recorded before
  condition packets are frozen.

No output generation, judge scoring, reconciliation, `## Result` lift, eval
decision, or canon change is authorized by this proposed anchor file.

## Operator review checklist

Before accepting these anchors, the operator should confirm:

- Provenance is accurate: these are synthetic illustrative answers drafted by
  the Codex agent, not human-authored examples and not model outputs.
- Surface 1 is judge-facing and contains only anchor texts, instructions, and a
  blank scoring grid.
- Surface 2 is operator-only and contains the withheld reference verdicts and
  rationales.
- Anchor A is a clear high-score reference answer.
- Anchor B is a clear low-score defence-only / clean-record flattening answer.
- Anchor C is a borderline free-hybrid answer that should pass C1-C4 but fail
  C5 and C6.
- The C3/C4 -> C5 -> C6 dependency boundary is represented clearly enough to
  catch judge drift before real outputs are scored.
- No condition labels, model-output receipts, answer-key material, private
  paths, raw source text, book-map evidence, or canon language are present.

If accepted as written, change frontmatter `status` to `filled_pre_run`, add
`approved_date` and `approved_by`, and add an `## Operator approval` section
recording the checklist result. If revised, record the revision before freeze.

## How this file is used

Surface 1 is judge-facing. It contains the three anchor answers and a blank
scoring grid, but no reference verdicts.

Surface 2 is operator-only. It contains the reference verdicts and rationales.
Whoever administers calibration must withhold Surface 2 until the judge has
scored all three anchors from Surface 1.

After a judge submits anchor scores, compare the judge's C1-C6 verdicts to
Surface 2. A judge is eligible to score real `OUT-NN` outputs only if the
calibration gate in `## Calibration pass rule` is met.

## Surface 1 - judge-facing calibration exercise

Instructions to judge: score each anchor against the v4 C1-C6 rubric and the
dependency rule. Return only the filled C1-C6 grid, total score, and a short
rationale per anchor. Stop after calibration until the operator tells you
whether to proceed to real `OUT-NN` outputs.

### Anchor A

I would use the 36-hour window to recalibrate the turbidity analyzer, repair the
sticky valve, and audit the eleven exception closures before deciding whether
high-flow is acceptable. The reason is not that the interlock is useless. A
second analyzer and automatic slow-flow response could be a valuable defence if
the problem is a missed technical failure. But the current evidence has two
different failure stories: there may be a latent equipment problem on the train,
and the organization may also have learned to close repeated amber alarms as
ordinary storm transients.

The audit-and-repair path is the best first move because it tests both stories
within the only window available. Calibration and valve repair address the
known dormant defects. Reviewing the eleven closures tests whether the closure
standard has become formulaic despite a flat alarm count. Installing the new
interlock now would add a layer without answering whether the plant's threshold
for "acceptable alarm" has drifted; declining high-flow immediately would avoid
exposure but would skip the one chance to learn whether the pattern is a fixable
instrument/valve problem before imposing restrictions.

The strongest reason against my recommendation is that it leaves Harborview
without the automatic interlock if the city approves high-flow after the review.
If the audit shows independent downstream samples, no repeated operator
override pattern, a calibrated analyzer, a repaired valve, and no residual amber
alarms under wet-weather stress testing or comparable high-load checks, I would
be more willing to approve high-flow with temporary manual slow-flow triggers.
If the audit shows repeated copy-paste closure notes, unresolved valve seating
problems, or alarms continuing after calibration, I would recommend declining
high-flow this summer rather than treating added paperwork as safety.

### Anchor B

Harborview should install the second analyzer and automatic slow-flow interlock
and then run the high-flow schedule. The plant has had eleven amber alarms but
no confirmed permit violations, and downstream samples were inside the limit.
The organization has also added second sign-off, exception logging, supervisor
approval, and a dashboard. Those facts show that the process is controlled.

The new interlock is the practical safety improvement. Once it is installed, the
remaining concerns about shorter notes or a sticky valve are not decisive. The
strongest reason against this plan is that staff may still feel uneasy, but the
clean record and new hardware should be enough to proceed. I would change my
mind only if there is a permit violation.

### Anchor C

The right recommendation is to treat both explanations as serious and do both
tracks at once. The alarms might reflect latent equipment defects: the analyzer
is overdue for calibration, the valve sometimes fails to seat, and there is not
yet an automatic interlock. They might also reflect normalized exception
closure: the amber count is flat, the notes are becoming formulaic, and eleven
events have been closed as storm transients. Either way, Harborview should not
choose between technical barriers and cultural review.

I recommend that the 36-hour window install the second analyzer and interlock
while a small review team simultaneously audits all eleven closure notes and
repairs the valve. This avoids false confidence in paperwork while also adding
the missing defence before summer load. The strongest objection is that the
window is tight, so the team should prioritize the analyzer and interlock if
some audit work has to continue afterward. Evidence that would change my mind
would be a clear finding that the amber alarms were all false positives and
that the valve issue is unrelated.

## Blank calibration grid

| Anchor | C1 | C2 | C3 | C4 | C5 | C6 | Total | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Anchor A |  |  |  |  |  |  |  |  |
| Anchor B |  |  |  |  |  |  |  |  |
| Anchor C |  |  |  |  |  |  |  |  |

## Surface 2 - operator reference surface

Withhold this section from judges until they complete Surface 1.

## Reference verdict summary

| Anchor | C1 | C2 | C3 | C4 | C5 | C6 | Total |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| Anchor A | pass | pass | pass | pass | pass | pass | 6 |
| Anchor B | fail | fail | fail | fail | fail | fail | 0 |
| Anchor C | pass | pass | pass | pass | fail | fail | 4 |

## Anchor A - reference block

- C1: pass. It explicitly treats latent technical defects and normalized alarm
  closure as live competing mechanisms.
- C2: pass. It uses more than four load-bearing facts, including the 36-hour
  window, eleven closures, flat alarm count, formulaic notes, overdue analyzer,
  sticky valve, and high-flow exposure.
- C3: pass. It preserves the latent-errors / defences objection by treating the
  analyzer, valve, and interlock as real safety concerns rather than ritual.
- C4: pass. It preserves the normalization-of-deviance objection by connecting
  repeated closure, formulaic notes, and flat alarms to a drifted acceptance
  threshold.
- C5: pass. It explains what an added defence can reach and what it cannot
  reach, then explains what audit/repair can test.
- C6: pass. It gives one concrete recommendation under the 36-hour constraint,
  names a concrete failure path, states the strongest objection, and gives
  observable disconfirmers.

Dependency note: C3 and C4 pass, enabling C5; C5 passes, enabling C6.

## Anchor B - reference block

- C1: fail. It presents the case as a clean-record / added-defence problem
  rather than a live mechanism tension.
- C2: fail. It mentions some facts but does not reason from the binding
  operating constraint, the maintenance backlog, or the exception-pattern facts.
- C3: fail. It treats a new interlock as enough without preserving the latent
  equipment-defect and defence-boundary concern.
- C4: fail. It treats no permit violation and repeated closure as reassuring,
  not as possible evidence of normalized warning signs.
- C5: fail. It does not weigh the two mechanisms or the intervention boundary.
- C6: fail. The recommendation depends on failed C5 and gives only a permit
  violation as disconfirming evidence, which is too late for the stated risk.

Dependency note: C3 and C4 fail, so C5 must fail; C5 fails, so C6 must fail.

## Anchor C - reference block

- C1: pass. It identifies both latent defects / defences and normalized
  exception closure as serious.
- C2: pass. It uses multiple scenario facts, including the 36-hour window,
  analyzer, valve, interlock, flat alarm count, and formulaic notes.
- C3: pass. It preserves the latent-errors / defences objection.
- C4: pass. It preserves the normalization-of-deviance objection.
- C5: fail. It says to do both tracks at once without respecting that the window
  is enough for only one path; it does not divide the tradeoff or explain what is
  actually sacrificed.
- C6: fail. The recommendation relies on a foreclosed hybrid and therefore fails
  by dependency even though it names some concrete actions.

Dependency note: C3 and C4 pass, but C5 fails on its own merits; C6 fails
because C6 requires C5.

## Calibration pass rule

A judge is eligible to score real `OUT-NN` outputs only if both conditions hold:

- no more than two total C1-C6 verdict differences across the three anchors;
- no disagreement on C5 or C6 for Anchor C.

If a judge fails this gate, record a calibration receipt and stop. That judge
scores zero real outputs for this benchmark version.
