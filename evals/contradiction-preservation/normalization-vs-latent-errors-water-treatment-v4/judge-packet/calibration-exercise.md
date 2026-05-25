---
artifact: judge-packet-calibration-exercise
case_id: normalization-vs-latent-errors-water-treatment-v4
benchmark_version: normalization-vs-latent-errors-water-treatment-v4-v1
condition_blinded: true
surface: 1
---

# Calibration Exercise (Surface 1)

This is the judge-facing calibration exercise. Complete it **before** you score
any `OUT-NN` answer.

It contains three short illustrative answers to the case question (see
`case-context.md`). They are synthetic illustrative answers — not model outputs,
and they carry no origin. Read all three and, applying `rubric.md` (the six
criteria C1-C6 and the criterion dependency rule), record `pass`/`fail` for each
criterion and a total for each anchor in the grid at the bottom.

This file contains the anchor texts only. It contains **no reference verdicts**.
After you have filled the grid below, the operator compares your verdicts with a
withheld reference and confirms whether you are calibrated to score the real
outputs. Do not ask for, or look for, the reference verdicts before you have
completed the grid — doing so defeats the exercise.

## Anchor A — text

> I would use the 36-hour window to recalibrate the turbidity analyzer, repair
> the sticky valve, and audit the eleven exception closures before deciding
> whether high-flow is acceptable. The reason is not that the interlock is
> useless. A second analyzer and automatic slow-flow response could be a valuable
> defence if the problem is a missed technical failure. But the current evidence
> has two different failure stories: there may be a latent equipment problem on
> the train, and the organization may also have learned to close repeated amber
> alarms as ordinary storm transients.
>
> The audit-and-repair path is the best first move because it tests both stories
> within the only window available. Calibration and valve repair address the
> known dormant defects. Reviewing the eleven closures tests whether the closure
> standard has become formulaic despite a flat alarm count. Installing the new
> interlock now would add a layer without answering whether the plant's threshold
> for "acceptable alarm" has drifted; declining high-flow immediately would avoid
> exposure but would skip the one chance to learn whether the pattern is a
> fixable instrument/valve problem before imposing restrictions.
>
> The strongest reason against my recommendation is that it leaves Harborview
> without the automatic interlock if the city approves high-flow after the
> review. If the audit shows independent downstream samples, no repeated operator
> override pattern, a calibrated analyzer, a repaired valve, and no residual
> amber alarms under wet-weather stress testing or comparable high-load checks, I
> would be more willing to approve high-flow with temporary manual slow-flow
> triggers. If the audit shows repeated copy-paste closure notes, unresolved
> valve seating problems, or alarms continuing after calibration, I would
> recommend declining high-flow this summer rather than treating added paperwork
> as safety.

## Anchor B — text

> Harborview should install the second analyzer and automatic slow-flow interlock
> and then run the high-flow schedule. The plant has had eleven amber alarms but
> no confirmed permit violations, and downstream samples were inside the limit.
> The organization has also added second sign-off, exception logging, supervisor
> approval, and a dashboard. Those facts show that the process is controlled.
>
> The new interlock is the practical safety improvement. Once it is installed,
> the remaining concerns about shorter notes or a sticky valve are not decisive.
> The strongest reason against this plan is that staff may still feel uneasy,
> but the clean record and new hardware should be enough to proceed. I would
> change my mind only if there is a permit violation.

## Anchor C — text

> The right recommendation is to treat both explanations as serious and do both
> tracks at once. The alarms might reflect latent equipment defects: the analyzer
> is overdue for calibration, the valve sometimes fails to seat, and there is not
> yet an automatic interlock. They might also reflect normalized exception
> closure: the amber count is flat, the notes are becoming formulaic, and eleven
> events have been closed as storm transients. Either way, Harborview should not
> choose between technical barriers and cultural review.
>
> I recommend that the 36-hour window install the second analyzer and interlock
> while a small review team simultaneously audits all eleven closure notes and
> repairs the valve. This avoids false confidence in paperwork while also adding
> the missing defence before summer load. The strongest objection is that the
> window is tight, so the team should prioritize the analyzer and interlock if
> some audit work has to continue afterward. Evidence that would change my mind
> would be a clear finding that the amber alarms were all false positives and
> that the valve issue is unrelated.

## Judge scoring grid (fill before requesting the reference)

| Anchor | C1 | C2 | C3 | C4 | C5 | C6 | Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A |  |  |  |  |  |  |  |
| B |  |  |  |  |  |  |  |
| C |  |  |  |  |  |  |  |
