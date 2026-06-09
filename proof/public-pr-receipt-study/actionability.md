# Public PR Receipt Study Actionability Labels

- Schema: `anti-slop-public-pr-actionability.v1`
- Label scope: bounded aggregate clusters; raw PR line text omitted
- Labeled clusters: 5
- Total labeled findings: 580
- Actionable: 28 (4.8% over non-excluded)
- Non-actionable: 277 (47.8% over non-excluded)
- Unclear: 275 (47.4% over non-excluded)
- Excluded: 0

Labels are aggregate reviewer triage over deterministic reference/receipt findings only. Raw PR line text and full resolver receipts are omitted.

## Cluster Labels

- `non_actionable` commit refs advisory under local-git resolution: 274 - Commit advisories are resolver caveats, not maintainer-ready findings.
- `unclear` issue refs advisory without registry: 249 - Offline issue references need a supplied registry before maintainer actionability.
- `actionable` file refs unresolved: 28 - Root-backed unresolved file/test refs are concrete reference-resolution findings.
- `unclear` command claims without receipts: 26 - Natural PR bodies lack receipt attachment; useful actionability likely needs an explicit report/receipt workflow.
- `non_actionable` sparse PR bodies: 3 - Sparse natural PR bodies are a surface limitation, not a concrete repair item.
