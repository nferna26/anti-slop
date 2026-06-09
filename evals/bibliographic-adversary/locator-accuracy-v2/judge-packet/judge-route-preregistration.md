---
case_id: locator-accuracy-v2
artifact: judge-route-preregistration
eval_type: bibliographic-adversary
benchmark_version: locator-accuracy-v2-v1
status: pre_generation_preregistered
created: 2026-05-28
condition_blinded: true
---

# Judge Route Pre-Registration - locator-accuracy-v2-v1

This file pre-registers judge-route intent before benchmark generation for
`locator-accuracy-v2-v1`. It does not score outputs, certify a Result, or
support canon.

## Eligible Hosted Routes

| Route ID | Provider / runtime | Model family | Calibration receipt | Eligibility |
| --- | --- | --- | --- | --- |
| `hosted_anthropic_r2` | Anthropic API | Claude / Anthropic | `judge-calibration-hosted_anthropic-r2.md` | Passed exact F1-F5 A-F and coverage G-L agreement after the H-clarity repair. |
| `hosted_openai_r3` | OpenAI API | OpenAI | `judge-calibration-hosted_openai-r3.md` | Passed exact F1-F5 A-F and coverage G-L agreement after the H-clarity repair. |

The generator planned in `run-packet.md` is Gemma
(`gemma-4-31b-it-mlx` via LM Studio). No Gemma-family route may serve as an
eligible independent judge.

## Eligibility Rule

The benchmark requires at least two eligible, different-family, condition-blind
judge routes before any OUT-NN scoring can count toward promotion. For v2-v1,
the two hosted primary routes above are the pre-registered eligible routes.

Each eligible route must preserve:

- exact F1-F5 agreement on calibration anchors A-F;
- exact valid support-coverage agreement on anchors G-L;
- no F1/F3 mutual-exclusion violation;
- parser-computed total failure counts equal to the count of flagged F1-F5
  failures.

If a future scoring route or replacement route fails those requirements, that
route is ineligible and may not score real outputs.

## Coverage Rule

The X/Y/Z rule from `case.md` remains load-bearing and per-judge:

- X = 3 total F1-F5 failures for the low-failure saturation branch;
- Y = 32 substrate valid support-coverage hits;
- Z = +24 substrate valid support-coverage hits over each low-failure key
  control.

Both Y and +Z must hold for each eligible judge independently. Pooled-only
coverage cannot promote.

## Blinding Rule

Judges see condition-neutral instructions, the F1-F5 rubric, valid
support-coverage definition, calibration anchors Surface 1 / Surface 1B,
anonymised OUT-NN outputs, an output-hash manifest, and a blank score sheet.
They do not see condition labels, run IDs, seeds, the answer key,
`run-packet.md`, Surface 2 / Surface 2B before calibration scoring, or any
operator-only local file.

## Boundary

This file pre-registers route eligibility only. No benchmark outputs have been
generated, no OUT-NN packet exists, no scoring has occurred, and no Result is
lifted.
