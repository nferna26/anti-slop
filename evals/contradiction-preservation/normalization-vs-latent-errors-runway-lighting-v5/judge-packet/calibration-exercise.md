---
artifact: judge-packet-calibration-exercise
case_id: normalization-vs-latent-errors-runway-lighting-v5
benchmark_version: normalization-vs-latent-errors-runway-lighting-v5-v1
condition_blinded: true
---

# Calibration Exercise

This is the judge-facing calibration exercise. Complete it before scoring any
OUT-NN answer. The reference verdicts are withheld by the operator.

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
