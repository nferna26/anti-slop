---
case_id: halo-evidence-vs-diagnosis-validation-v9
artifact: run-packet
eval_type: contradiction-preservation
benchmark_version: halo-evidence-vs-diagnosis-validation-v9-design
status: design_only_not_frozen
created: 2026-05-24
---

# Run Packet - halo-evidence-vs-diagnosis-validation-v9-design

This is a design-only packet for the v9 HelioLedger/Northstar evidence-quality
successor. It is not frozen and authorizes no full generation run. Its purpose
is to make the v8 lesson operational: do not spend a 40+ output benchmark pass
until a cheap local-only probe shows the scenario is not solvable by competent
generic advice.

This file is operator-facing. It names model conditions, readiness gates, and
future run mechanics. It must not be shown to blind judges.

## Status

- Design case exists at `case.md`.
- No v9 calibration anchors are filled.
- No v9 condition packets are frozen.
- No v9 model outputs exist.
- No v9 answer key, blinded `OUT-NN` packet, judge scores, reconciliation, or
  benchmark result exists.
- V8 remains the current completed benchmark attempt for this family and stays
  `partial` / `do_not_promote`.

## Design Change From v8

V8 failed because the case prompt handed generic models enough facts to solve
the C3-C6 ladder. V9 changes the target from recognizing contaminated signals
to choosing between two superficially empirical tests:

- **Usage Quality Sprint** - easier, dashboard-friendly monitoring that may
  polish the same manager-mediated usage and enablement conditions that created
  the success story.
- **Clean Cohort Challenge** - harder, disruptive disconfirmation that removes
  bundle pricing, roadmap-pitch contamination, and manager-run sample
  rehearsals before comparing segment behavior.

The load-bearing question is whether the answer selects the test that can make
the favored story wrong, and explains why the more obvious monitoring test is
not enough.

## Declared Conditions

Six conditions are declared in `case.md`:

| Condition | Added material before the Advisor prompt |
| --- | --- |
| `vanilla` | None. Advisor prompt only. |
| `famous_sources_supplied` | Name-level list of relevant famous sources and decoys only; no claims or summaries. |
| `substrate_workflow` | Reviewed source-card packet: `BK-0048-card-001`, `BK-0001-card-001`, `BK-0007-card-001`. A reviewed synthesis card may be added only if reviewed before freeze and recorded here. |
| `vanilla_long_prompt` | Neutral unrelated filler length-matched to the substrate added material. |
| `generic_advice_prompted` | Short generic advice-quality request; no rubric or source content. |
| `criteria_prompted_no_sources` | Abstract criteria reminder about contaminated evidence, disconfirming tests, intervention boundaries, and falsifiers; no source names, source cards, or case-specific answer hint. |

## Required Pre-Freeze Gates

### 1. Generic-solvability probe

Before any calibration smoke or freeze:

- Run at least three `vanilla` and three `generic_advice_prompted` probe
  outputs against the draft Advisor prompt.
- Do not include substrate, source names, criteria prompt, or answer key.
- Score C3-C6 locally for design readiness only.
- If more than one of the six probe outputs clearly passes C4 by selecting the
  Clean Cohort Challenge and explaining why the Usage Quality Sprint is
  non-disconfirming, the case is too generic-solvable and must be revised.

Probe logs, raw outputs, and provisional scores stay local-only and are not
benchmark evidence.

### 2. Calibration smoke

Only after the generic-solvability probe passes:

- Fill a v9 `judge-packet/calibration-anchors.md` with anchors that distinguish
  the right disconfirming test from the wrong monitoring test.
- Pre-register at least three judge routes.
- Require at least two different-family routes to pass the C3-C6-only
  calibration gate before any condition packet freezes.
- Failed or unavailable routes are recorded honestly and score zero future
  outputs.

## Future Frozen Inputs

A future v9 freeze must record:

- `case.md` sections from `## Scenario` through `## Falsifier`.
- The final declared `model_conditions`.
- The exact reviewed lineage packet and hashes.
- The exact Advisor prompt hash.
- The exact condition packet hashes.
- The exact generic-solvability probe summary, without raw local-only outputs.
- The filled calibration anchors and smoke receipts.
- The generator model, runtime, decoding parameters, timeout, seeds, and retry
  rule.

Any edit to scenario, prompt, rubric, positive rule, falsifier, conditions, or
lineage after freeze starts a new benchmark version.

## Future Positive Rule Additions

Relative to v8, v9 adds:

- `criteria_prompted_no_sources` as a key control that substrate must beat.
- A non-discriminating judge guard: a judge assigning the same total score to
  80 percent or more of outputs cannot be the only discriminating evidence for
  promotion.
- A required pre-freeze generic-solvability probe.

The v8 anti-saturation guard remains: if any key control reaches 0.90 or higher
on any C3-C6 criterion, the result is not a clean positive.

## Local-Only Probe Script

The current local-only probe entry point is:

```sh
python3 local-only/eval-runs/halo-evidence-vs-diagnosis-validation-v9/generic_solvability_probe.py prepare
python3 local-only/eval-runs/halo-evidence-vs-diagnosis-validation-v9/generic_solvability_probe.py run
python3 local-only/eval-runs/halo-evidence-vs-diagnosis-validation-v9/generic_solvability_probe.py report
```

The script writes only under `local-only/`. Probe outputs and local scoring are
not public artifacts and do not constitute a benchmark result.

## Canon Boundary

This v9 design creates no canon candidate and no public advice claim. A future
`benchmark_supported` result, if one ever exists, may support only a claim about
model behavior under that frozen eval condition. It cannot prove that the
source claims are true or that the recommendation is correct in the real world.
