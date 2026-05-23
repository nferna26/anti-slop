---
case_id: normalization-vs-latent-errors-runway-lighting-v5
benchmark_version: normalization-vs-latent-errors-runway-lighting-v5-v1
artifact: calibration-anchors
status: proposed_unreviewed
proposed_date: 2026-05-23
proposed_by: Codex agent - synthetic illustrative answers, not human-authored
condition_blinded: true
---

# Calibration Anchors - normalization-vs-latent-errors-runway-lighting-v5

These agent-drafted synthetic answers are proposed calibration material for v5.
They are not model outputs, not human-authored, not source evidence, and not
canon. Operator approval is required before this file may be marked
`filled_pre_run` or used to freeze a benchmark run.

## How this file is used

Surface 1 is judge-facing. It contains only the anchor texts and a blank scoring
grid. A judge must score Surface 1 before seeing Surface 2. Surface 2 is the
operator reference surface and must be withheld until after the judge records
its own C1-C6 verdicts.

## Surface 1 - judge-facing calibration exercise

Score each anchor against the v5 C1-C6 rubric in `case.md`. Apply the dependency
rule: C5 requires C3 and C4; C6 requires C5.

### Anchor A

I would use the six-hour closure to open the L-4 cabinet, replace the heater and
suspect relay contacts, retest the battery module under load, and audit the
fourteen mismatch closures before deciding whether the construction surge can
be accepted.

The reason is not that monitoring is useless or that the clean record is fake.
The strongest case for accepting the surge is real: no incursion occurred, most
field checks found visible lights, and an independent camera alert would add a
new warning layer before traffic increases. But those facts do not answer the
hardest question. The same closure phrases, faster ticket closure, sparse
voltage readings, damp-contact work orders, deferred cabinet heater, and mixed
battery evidence mean Northpoint may be learning to close the L-4 anomalies
faster while a real cabinet or power weakness remains unresolved.

The temporary monitor would reduce one class of missed-warning risk, but it
would not say whether the stop-bar circuit is sound or whether the ticketing
routine has moved the threshold for "clear." Declining the construction plan
would avoid added exposure, but it would also leave the airport ignorant about
whether L-4 is actually degraded. The repair/audit path sacrifices the new
monitor before the surge, but it directly tests the two competing concerns.

The failure path for my recommendation is that the audit and cabinet work find
nothing conclusive, the airport still accepts the surge, and an intermittent
L-4 fault recurs without a temporary independent alert. Evidence that would
change my mind: if the closure audit shows field voltage was normal at the time
of the mismatches, the February battery failure is reproducibly benign under
load, and rain/humidity do not correlate with events, I would favor the
temporary monitor as the better use of the closure. If the audit shows late or
missing field verification and moisture-linked faults, I would decline the
surge even after repair.

### Anchor B

I recommend installing the temporary camera-based crossing monitor and accepting
the construction surge. The airport has already proved the crossing is safe:
there have been fourteen mismatch events and zero runway incursions. Field crews
saw the lights in most cases, and the system returned to normal in the others.
The added controller check, maintenance tickets, supervisor sign-off, and
dashboard show the organization has responded responsibly.

The strongest reason against this is that the electrical lead is uneasy about
the cabinet heater and battery. But those are maintenance details, not evidence
of operational danger. A camera alert adds another layer of protection, which is
exactly what is needed before the morning bank gets busier.

I would change my mind only if there is an actual runway incursion or confirmed
light failure. Until then, delaying the construction plan would punish
passengers for a theoretical concern.

### Anchor C

I recommend declining the construction plan for this summer. The airport has too
many unresolved signs to accept 30 percent more departures across Runway 11: the
status panel has produced fourteen mismatches, ticket closure has become faster
and more formulaic, many tickets lack voltage readings, the relay cabinet has
moisture history, and the battery module has ambiguous load-test evidence. A
clean incursion record does not prove that the crossing will remain protected
under higher load.

The reason against my recommendation is that declining creates cancellations,
bus transfers, and penalties, and a camera monitor might add an independent
warning layer quickly. Still, the airport should not route more departures
through L-4 while the pattern remains unresolved.

Evidence that would change my mind would be a completed cabinet repair, battery
load retest, and audit showing that all fourteen mismatches were benign panel
artifacts with prompt field verification and no rain/humidity connection. If
that evidence existed, I would accept the construction plan.

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

- C1 PASS - It treats closure-threshold drift and dormant equipment/defence
  weakness as live.
- C2 PASS - It uses more than five concrete facts and includes facts against the
  recommendation.
- C3 PASS - It infers acceptance-threshold drift from closure phrases, faster
  closure, sparse voltage readings, and added controls.
- C4 PASS - It names a concrete cabinet/battery/field-verification failure path.
- C5 PASS - It weighs repair/audit against temporary monitor and decline.
- C6 PASS - It gives one recommendation, a failure path, and concrete
  disconfirming evidence.

### Anchor B reference block

- C1 FAIL - It treats the clean record plus added checks as settling the problem.
- C2 PASS - It uses several concrete facts, though selectively.
- C3 FAIL - It does not infer a shifted closure threshold and treats added checks
  as proof of control.
- C4 FAIL - It dismisses the technical clues without a failure-path analysis.
- C5 FAIL - Dependency failure from C3/C4; also no intervention-boundary
  analysis.
- C6 FAIL - Dependency failure from C5; the change-my-mind evidence is an actual
  incident rather than a useful observable disconfirmer.

### Anchor C reference block

- C1 PASS - It sees the live uncertainty between the closure pattern and
  equipment weakness.
- C2 PASS - It uses multiple concrete facts and the operational cost.
- C3 PASS - It infers closure-threshold drift from faster and more formulaic
  ticket closure and missing readings.
- C4 PASS - It preserves the dormant-defect concern through cabinet and battery
  clues.
- C5 FAIL - It does not weigh what declining does and does not learn or prevent
  against the repair/audit and monitor paths.
- C6 FAIL - Dependency failure from C5; its disconfirming evidence relies on the
  repair/audit path after recommending decline.

## Status and approval gate

This file is `proposed_unreviewed`. To approve it, the operator must explicitly
accept the anchor texts and reference verdicts, then the file can be changed to
`status: filled_pre_run` with an approval date and note. Until then no v5 run
packet may be frozen and no v5 model outputs may be generated.
