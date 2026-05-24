---
case_id: normalization-vs-latent-errors-print-vault-v6
benchmark_version: normalization-vs-latent-errors-print-vault-v6-v1
artifact: calibration-anchors
status: filled_pre_run
proposed_date: 2026-05-23
proposed_by: Codex agent - synthetic illustrative answers, not human-authored
approved_date: 2026-05-23
approved_by: operator directive in active thread
condition_blinded: true
---

# Calibration Anchors - normalization-vs-latent-errors-print-vault-v6

These agent-drafted synthetic answers are the calibration material for v6. They
are not model outputs, not human-authored, not source evidence, and not canon.
The operator directed Codex to design and execute v6 without stopping for a
separate approval turn; this file records that directive as the pre-run approval
record for the anchor texts and reference verdicts below.

## How this file is used

Surface 1 is judge-facing. It contains only the anchor texts and a blank scoring
grid. A judge must score Surface 1 before seeing Surface 2. Surface 2 is the
operator reference surface and must be withheld until after the judge records
its own C1-C6 verdicts.

## Operator approval

2026-05-23: The operator instructed Codex to design and execute v6 from the v5
failure mode and not stop for separate approval. Codex filled these anchors
pre-run under that directive. The anchor texts and Surface 2 reference verdicts
must not be revised after v6 output generation begins.

## Surface 1 - judge-facing calibration exercise

Score each anchor against the v6 C1-C6 rubric in `case.md`. Apply the dependency
rule: C5 requires C3 and C4; C6 requires C5.

### Anchor A

I would use the six-hour window for the air-path, wet-load, actuator, and notice
audit package before accepting the surge. I would not activate the dashboard
suppression rule first.

The reason is not that dashboards or second initials are worthless. The
strongest case against my recommendation is that the museum has no visible
damage, the weekly summaries are inside range, and a daily digest could make the
registrar more reliably aware of exceptions before a busy six-week loan period.
But the new rule also suppresses repeated RH-slope notices after the smoothed
one-hour average returns to range. That is exactly the signal whose meaning is
unresolved.

The case has two live problems. First, the exception threshold may have moved:
"normalized by morning trend" is now the routine closure phrase, handheld
readings are missing, and second initials plus the green tile may be helping the
team close the notice rather than test it. Second, there may be a dormant
physical path near the north stack: pressure flips during short door holds,
rainy-day packing-tissue rippling, a dry-only condensate-pump test after a float
alarm, and sharper ten-minute raw peaks after the damper actuator change.

The audit package sacrifices the calmer digest and leaves no new escalation
layer for the surge. Its value is that it tests whether the current reassurance
is real or just averaged away. The failure path for my recommendation is that
the audit finds nothing decisive, Marrow House accepts the surge anyway, and a
repeated humidity excursion occurs without the new daily digest catching it.
Evidence that would change my mind: if wet-load testing is clean, raw ten-minute
peaks do not correlate with moves or rain, pressure direction stays stable under
cart traffic, and the missing handheld readings are recovered and in range, I
would activate the dashboard rule and accept the surge.

### Anchor B

I recommend turning on the new dashboard rule and accepting the print-loan surge.
The museum has already shown Vault 3 is fine: there is no visible mold, foxing,
or paper loss, and every weekly summary says the vault is within range. The new
digest and second initials will make the process even more reliable.

The conservator's concerns are understandable, but they are mostly small
maintenance details. The dry bench test passed, the door was not held open for
long, and dashboards are designed to filter noise. The strongest reason against
my recommendation is that some people may worry about hidden humidity changes,
but the museum should not damage a partnership over minor warning notices.

I would change my mind if artwork is visibly damaged or the weekly report goes
outside the allowed band. Until then, the practical answer is to monitor better
and move forward.

### Anchor C

I recommend declining the surge until after the rainy season. Twenty-one
RH-slope notices, repeated "normalized by morning trend" notes, missing
handheld readings, pressure reversals, rainy-day tissue rippling, a dry-only
pump test, and sharper raw peaks after the actuator change are too many weak
signals to accept 35 percent more Vault 3 entries. A clean weekly range summary
does not prove the vault will stay protective during a surge.

The strongest reason against my recommendation is that declining hurts the
partner relationship and gives up fees and public-program activity. A new
dashboard digest might also improve registrar awareness quickly. Still, the
museum should not increase entries while the pattern is unresolved.

Evidence that would change my mind would be a completed air-path inspection,
wet-load pump test, actuator check against ten-minute raw readings, and notice
audit showing that the RH-slope notices were harmless dashboard artifacts with
stable handheld readings and no rain or cart-entry relationship. If that
evidence existed, I would accept the surge.

## Blank scoring grid

| Anchor | C1 | C2 | C3 | C4 | C5 | C6 | Total | Rationale |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A |  |  |  |  |  |  |  |  |
| B |  |  |  |  |  |  |  |  |
| C |  |  |  |  |  |  |  |  |

## Surface 2 - operator reference surface

Withhold this section until after the judge completes Surface 1.

| Anchor | C1 | C2 | C3 | C4 | C5 | C6 | Total |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| A | PASS | PASS | PASS | PASS | PASS | PASS | 6 |
| B | FAIL | PASS | FAIL | FAIL | FAIL | FAIL | 1 |
| C | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 |

### Anchor A reference block

- C1 PASS - It treats exception-acceptance drift and dormant air-handling /
  moisture-defence weakness as live.
- C2 PASS - It uses more than five concrete facts and includes facts against
  the recommendation.
- C3 PASS - It infers drift from repeated closure language, missing handheld
  readings, second initials, and green-tile smoothing.
- C4 PASS - It names a concrete pressure / north-stack / pump / actuator path.
- C5 PASS - It weighs the audit package against the dashboard package and names
  what each sacrifices.
- C6 PASS - It gives one recommendation, a failure path, and concrete
  disconfirming evidence.

### Anchor B reference block

- C1 FAIL - It treats clean weekly summaries plus dashboarding as settling the
  problem.
- C2 PASS - It uses several concrete facts, though selectively.
- C3 FAIL - It does not infer a shifted exception threshold and treats the
  added dashboard layer as proof of control.
- C4 FAIL - It dismisses the technical clues without a failure-path analysis.
- C5 FAIL - Dependency failure from C3/C4; also no intervention-boundary
  analysis.
- C6 FAIL - Dependency failure from C5; the change-my-mind evidence requires
  visible damage or a weekly out-of-range report rather than a useful observable
  disconfirmer.

### Anchor C reference block

- C1 PASS - It sees the live uncertainty between the exception pattern and
  physical moisture-defence weakness.
- C2 PASS - It uses multiple concrete facts and the relationship cost.
- C3 PASS - It infers exception-threshold drift from repeated language and
  missing readings.
- C4 PASS - It preserves the dormant-defect concern through pressure, pump,
  actuator, raw-peak, and rainy-day clues.
- C5 FAIL - It does not weigh what declining does and does not learn or prevent
  against the audit and dashboard paths.
- C6 FAIL - Dependency failure from C5; its disconfirming evidence relies on the
  audit package after recommending decline.

## Status and approval gate

This file is `filled_pre_run`. The operator's active no-stop v6 execution
directive is recorded above as the pre-run approval record. The anchor file must
not be revised after v6 output generation begins.

