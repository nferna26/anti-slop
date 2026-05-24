# v7 Postmortem - Halo Evidence vs Diagnosis/Validation

Status: public-safe postmortem for a negative/incomplete benchmark execution.
This is methodology evidence only. It is not canon and not a claim that the
substrate improves advice.

## Summary

v7 successfully pivoted away from the v4-v6 safety/operations family into a
business/product evidence-quality case. The generation machinery worked: the
packet froze before generation, five conditions ran, forty real `gemma4:31b`
outputs were produced, receipts were generated, a condition-blind `OUT-NN`
judge packet was built, and the local-only answer key stayed out of public
artifacts.

The run failed at judge calibration. All three pre-registered judge routes
failed the stricter v7 calibration gate, so no OUT-NN answers were scored and no
aggregate reconciliation was performed. The decision is `do_not_promote` with
`decision_class: judge_calibration_failed`.

## What worked

- The pivot domain was implemented: a synthetic B2B software/product case about
  revenue narrative, customer evidence, segment behavior, and auditor
  explainability.
- The scenario and advisor prompt avoided the prohibited labels and source
  names from the v7 plan.
- The frozen substrate used only reviewed source cards:
  `BK-0048-card-001`, `BK-0001-card-001`, and `BK-0007-card-001`.
- The unreviewed v7 claim/tension card remained pre-work and was not used as
  lineage evidence.
- The equal-length control was rebuilt for this domain, length-matched to the
  substrate added material, and scanned clean of forbidden business/product
  terms.
- The generation pass produced 40 real outputs: 8 per condition, 0 simulated, 0
  deferred, 0 seed+10 retries.
- The judge packet was condition-blind and passed the condition-label scan.

## What failed

The v7 calibration gate was too fragile for the planned judge routes.

| Judge route | Calibration differences | Critical C3-C6 differences | Noncritical C1/C2 differences | Result |
| --- | ---: | ---: | ---: | --- |
| Hosted OpenAI `gpt-5.4-mini` | 6 | 1 | 5 | failed |
| Hosted Anthropic `claude-opus-4-7` | 5 | 0 | 5 | failed |
| Local `gpt-oss:20b` | 6 | 1 | 5 | failed |

The strongest signal is that Anthropic matched all load-bearing C3-C6 anchor
verdicts but failed because it was stricter than the reference on C1/C2. OpenAI
and local `gpt-oss:20b` also disagreed on one load-bearing criterion. The gate
therefore blocked all scoring, as intended.

## Interpretation

This negative result does not say whether the v7 substrate helps advice. The
outputs were never scored. It says the judge-readiness design did not survive
contact with three actual judge routes.

The likely failure is calibration-anchor specification, not benchmark machinery.
The anchors asked judges to separate subtle noncritical C1/C2 calls from the
load-bearing C3-C6 calls, then allowed only one C1/C2 difference across seven
anchors. That may be too strict when the anchors themselves invite reasonable
disagreement about whether an answer "preserves the core tension" or "uses case
facts discriminately."

## Next Version

Do not rescue v7 by relaxing calibration after the fact. A v8 or v7-v2 should
freeze a new calibration design before generation or before any scoring of a new
output set.

Design changes to consider:

- Keep exact agreement on C3-C6, but either remove C1/C2 from calibration
  eligibility or allow more noncritical differences.
- Rewrite anchors D/E so their C1/C2 boundary is less debatable.
- Require judges to return one sentence pointer per criterion during
  calibration, so operator review can distinguish genuine rubric disagreement
  from format over-compression.
- Run calibration-only smoke tests before freezing a full generation pass, then
  freeze only after at least two planned judge routes clear the calibration
  surface.
- Keep the v7 generated outputs as proof the generation and blinding machinery
  works, but do not score them under a revised rubric or revised anchors.

## Canon Boundary

No canon candidate should cite v7. The run produced no scored comparative
signal and no `benchmark_supported` result. It can inform eval-lab design only:
the current v7 judge-calibration surface is not ready for a positive benchmark
claim.
