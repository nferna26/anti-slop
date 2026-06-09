# Expanded External Sample Actionability Labels

- Schema: `anti-slop-actionability-labels.v1`
- Scope: aggregate clusters only; raw line text is omitted.
- Total labeled findings: 23
- Actionable findings: 0
- Non-actionable findings: 10
- Unclear findings: 5
- Excluded findings: 8
- Useful findings status: FAIL (`0.0%` actionable in the non-excluded sample)

## Labels

| Count | Label | Cluster | Reason |
| ---: | --- | --- | --- |
| 10 | non_actionable | commit refs advisory under local-git resolution | Advisory commit refs in a root-unavailable sample do not justify maintainer action without local checkout context. |
| 8 | excluded | file refs that do not resolve | External checkouts are not committed, so empty-root path failures are excluded from usefulness rates. |
| 5 | unclear | issue refs advisory without registry | Issue refs could become actionable with a registry, but this dry run has no registry or maintainer context. |

These labels are human triage over aggregate resolver findings. They do not
judge correctness, relevance, source truth, support, safety, advice quality,
reasoning, benchmark validity, statistical meaning, or canon.
