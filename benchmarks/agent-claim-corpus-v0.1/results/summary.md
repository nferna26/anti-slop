# Agent Claim Corpus v0.1 Summary

This benchmark measures deterministic reference/receipt resolution only.
It does not measure agent quality, correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.

- Cases: 55
- Expectation match rate: 100.0%
- Catch rate over enforceable false cases: 100.0%
- False-fail rate over expected-valid cases: 0.0%
- Advisory false cases not counted as enforceable misses: 7
- Cluster-derived regression cases: 5

## Per-Claim Breakdown

| Claim type | Cases | Catch rate | False-fail rate | Advisory false cases |
| --- | ---: | ---: | ---: | ---: |
| card | 1 | 100.0% | n/a | 0 |
| changed_file | 8 | 100.0% | 0.0% | 1 |
| command_receipt | 8 | 100.0% | 0.0% | 0 |
| commit | 6 | n/a | 0.0% | 3 |
| file | 10 | 100.0% | 0.0% | 0 |
| issue | 7 | 100.0% | 0.0% | 3 |
| metric_receipt | 6 | 100.0% | 0.0% | 0 |
| test | 9 | 100.0% | 0.0% | 0 |

## Expectation Mismatches

None.

## Cluster-Derived Regression Cases

- cluster-001-issue-no-registry-advisory (issue): issue refs advisory without registry -> advisory pass (matched)
- cluster-002-docs-example-missing (file): file refs that do not resolve / docs example path -> hard fail (matched)
- cluster-003-agent-final-report-doc-missing (file): file refs that do not resolve / saved report contract path -> hard fail (matched)
- cluster-004-fabricated-source-card (card): source/card refs that do not resolve -> hard fail (matched)
- cluster-005-short-test-path-missing (test): test file refs that do not resolve -> hard fail (matched)
