# Real-Checkout Comparison

- Schema: `anti-slop-real-checkout-comparison.v1`
- Status: `dry_run_not_adoption`

| Mode | Artifacts | Claims | Claims/100 lines | Hard unresolved | Advisory |
| --- | ---: | ---: | ---: | ---: | ---: |
| Empty root subset | 5 | 15 | 8.72 | 100.0% | 46.7% |
| Real checkout subset | 5 | 15 | 8.72 | 25.0% | 40.0% |

Interpretation: Real checkouts test whether empty-root hard failures remain unresolved when the target repo tree is available.
