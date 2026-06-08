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
| Non-actionable after repairs | Kill risk if `>50%` findings are non-actionable after repairs | UNKNOWN: no human actionability labels yet |
| Useful findings | Kill risk if `<20%` findings are useful | UNKNOWN: no maintainer/reviewer usefulness labels yet |
| Install success | Kill risk if `<70%` install success | UNKNOWN: no external install attempts yet |
| Command receipt dogfood | Kill risk if `<25%` command receipt dogfood | UNKNOWN: first external dry-run sample is PR-body only |
| Maintainer keep-rate | Kill risk if `0/10` maintainers keep the workflow | UNKNOWN: no outreach or adoption PRs were opened |
| Stale proof metrics | Kill risk if README/proof metrics drift from committed summaries | PASS: `make launch-check` validates current proof metric links |
| Platform clone risk | Kill risk if platform-native clones make repo workflow unnecessary | UNKNOWN: no platform-comparison data yet |

The dashboard status is `watch`: the first sample is dense enough to continue
report-mode learning, but most adoption-quality criteria are still unknown.
