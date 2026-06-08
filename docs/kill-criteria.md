# Kill Criteria Dashboard

The kill criteria keep Anti-Slop Receipts honest while external dry runs are
still evidence gathering. They are not adoption claims and they do not measure
correctness, relevance, source truth, support, safety, advice quality,
reasoning, benchmark validity, statistical meaning, or canon.

Machine-readable status lives at
[`proof/external-dry-run/kill-criteria.json`](../proof/external-dry-run/kill-criteria.json).
Unknown data is marked `UNKNOWN`, not `PASS`.

| Criterion | Status rule | Current status |
| --- | --- | --- |
| Claim density | Kill risk if `<5 claims/100 lines` | PASS in the first saved-public sample: 19.33 claims/100 lines |
| Non-actionable after repairs | Kill risk if `>50%` findings are non-actionable after repairs | FAIL in the expanded external aggregate-label pass: 66.7% non-actionable over non-excluded findings |
| Useful findings | Kill risk if `<20%` findings are useful | FAIL in the expanded external aggregate-label pass: 0.0% actionable over non-excluded findings |
| Install success | Kill risk if `<70%` install success | UNKNOWN: no external install attempts yet |
| Command receipt dogfood | Kill risk if `<25%` command receipt dogfood | PASS in one public-safe fixture: 100% receipt-backed command claims passed |
| Maintainer keep-rate | Kill risk if `0/10` maintainers keep the workflow | UNKNOWN: no outreach or adoption PRs were opened |
| Stale proof metrics | Kill risk if README/proof metrics drift from committed summaries | PASS: `make launch-check` validates current proof metric links |
| Platform clone risk | Kill risk if platform-native clones make repo workflow unnecessary | UNKNOWN: no platform-comparison data yet |

Expanded evidence:

- External sample summary:
  [`proof/external-dry-run/expanded/summary.json`](../proof/external-dry-run/expanded/summary.json)
- External sample comparison:
  [`proof/external-dry-run/expanded/comparison.json`](../proof/external-dry-run/expanded/comparison.json)
- Actionability labels:
  [`proof/external-dry-run/expanded/actionability.json`](../proof/external-dry-run/expanded/actionability.json)
- Command receipt dogfood:
  [`proof/command-receipt-dogfood/summary.json`](../proof/command-receipt-dogfood/summary.json)

The dashboard status remains `watch`: density and command-receipt dogfood are
good enough to keep learning, but expanded external actionability is currently
poor and external install / keep-rate / platform-comparison data remain
UNKNOWN.
