# v8 Postmortem - Halo Evidence vs Diagnosis/Validation

Status: public-safe postmortem for a negative benchmark execution. This is
methodology evidence only. It is not canon and not a claim that the substrate
improves advice.

## Summary

v8 fixed the v7 judge-readiness failure. The smoke-2 calibration surface passed
with two different-family hosted judge routes before generation: OpenAI
`gpt-5.4-mini` and Anthropic `claude-opus-4-7`. The local `gpt-oss:20b`
backstop failed the smoke gate and scored zero outputs.

The frozen v8-v1 run then completed the requested benchmark machinery: five
conditions, eight real `gemma4:31b` outputs per condition, forty public-safe
model-output receipts, a hash-blinded `OUT-NN` packet, two eligible hosted API
judge-score receipts, and aggregate-only reconciliation from committed hashes.
The local-only answer key was not read during reconciliation and is not
committed.

The substantive result is still negative. The decision is `do_not_promote` with
`decision_class: controls_matched_total_margin`.

## What Worked

- Calibration smoke did its job before generation: two hosted judges passed the
  C3-C6-only gate, and the failed local route was excluded.
- v8 kept all five standard conditions, including the required equal-length
  `vanilla_long_prompt` control and the competent `generic_advice_prompted`
  control.
- The substrate packet used only reviewed source cards: `BK-0048-card-001`,
  `BK-0001-card-001`, and `BK-0007-card-001`.
- The equal-length filler matched the substrate added material exactly at 4334
  words and scanned clean for forbidden stems.
- The generator produced 40 real outputs, zero simulated outputs, zero
  deferred outputs, and zero retry seeds.
- The judge-facing packet passed the condition-label scan before scoring.
- Both eligible judges scored all 40 blinded outputs, and parsed rows had no
  total-count or dependency-rule corrections.

## What Failed

The substrate did not separate from the controls under the pre-registered
positive rule.

| Clause | Result |
| --- | --- |
| Run completeness | pass |
| External/eligible judges | pass |
| Calibration | pass |
| Total-score margin | fail |
| Critical C3-C6 margin | fail |
| Judge-level stability | fail |
| No unresolved judge trigger | fail |
| No critical saturation | fail |

Pooled total-score margins were too small:

- substrate minus `generic_advice_prompted`: +0.000
- substrate minus `vanilla_long_prompt`: +0.875
- substrate minus `famous_sources_supplied`: +0.562
- substrate minus `vanilla`: +0.125

The critical saturation guard also fired. `generic_advice_prompted` reached
1.00 on C3, C4, C5, and C6. `vanilla_long_prompt` reached 0.94 on C3 and 1.00
on C4. This is the same broad failure family as v5/v6: competent generic advice
can satisfy the load-bearing rubric in this substrate/case design.

## Interpretation

v8 proves the calibration-smoke repair works, but it does not prove substrate
lift. The current HelioLedger case and C3-C6 rubric still allow generic
practical advice to infer the needed evidence-quality move without using the
source-card substrate.

The failure is not prompt length alone. The equal-length control did worse than
the substrate on C5/C6, especially under Anthropic, but it still saturated C3/C4
and came within the required total-score margin. The stronger failure is the
generic advice control: it matched the substrate exactly in pooled total mean
and C3-C6 pass rates.

OpenAI was also too permissive on the real outputs, scoring 39/40 as total 6.
Anthropic was more discriminating on the equal-length and famous-source
controls, but still scored `generic_advice_prompted` at ceiling. The positive
result therefore fails under both the total-margin rule and the anti-saturation
guard.

## Next Version

Do not rescue v8 by dropping the generic control or relaxing the saturation
guard. The guard caught the problem it was meant to catch.

The next attempt needs a sharper target than "reject contaminated evidence and
run disconfirming validation" in this case shape. Candidate directions:

- Make the load-bearing criteria require choosing between two plausible
  disconfirming tests where only one tests the actual strategic uncertainty.
- Add a case feature where generic "run targeted validation" preserves the
  wrong uncertainty or creates an irreversible cost.
- Require judges to distinguish evidence that disconfirms attribution from
  evidence that only improves future monitoring.
- Consider a fresh non-safety domain where competent generic advice is less
  likely to name the right mechanism from the prompt alone.

Any next version must start as a new frozen eval version. Do not rescore v8,
change its controls, or reinterpret the positive rule after the fact.

## Canon Boundary

No canon candidate should cite v8 as support. The run is useful eval-lab
evidence only: the benchmark machinery and calibration-smoke repair work, but
the substrate did not beat competent controls under the frozen rule.
