# Agent Claim Corpus v0.1 Summary

This benchmark measures deterministic reference/receipt resolution only.
It does not measure agent quality, correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.

- Cases: 50
- Expectation match rate: 100.0%
- Catch rate over enforceable false cases: 100.0%
- False-fail rate over expected-valid cases: 0.0%
- Advisory false cases not counted as enforceable misses: 6

## Per-Claim Breakdown

| Claim type | Cases | Catch rate | False-fail rate | Advisory false cases |
| --- | ---: | ---: | ---: | ---: |
| changed_file | 8 | 100.0% | 0.0% | 1 |
| command_receipt | 8 | 100.0% | 0.0% | 0 |
| commit | 6 | n/a | 0.0% | 3 |
| file | 8 | 100.0% | 0.0% | 0 |
| issue | 6 | 100.0% | 0.0% | 2 |
| metric_receipt | 6 | 100.0% | 0.0% | 0 |
| test | 8 | 100.0% | 0.0% | 0 |

## Expectation Mismatches

None.
