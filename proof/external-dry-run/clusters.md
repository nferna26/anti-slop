# External Dry-Run Cluster Memo

This memo clusters report-mode dry-run findings by claim type, normalized reason, text pattern, path shape, repo/language metadata when available, and diff availability.

It omits raw line text and full resolver receipts. The output is evidence for resolver learning only, not correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.

- Schema: `anti-slop-external-dry-run-clusters.v1`
- Source summary: `proof/external-dry-run/summary.json`
- Observations: 27
- Clusters: 15
- Recommended actions: {'benchmark_case': 12, 'docs_update': 15}

## Top Clusters

| Count | Claim type | Status | Reason | Text pattern | Path shape | Repo | Language | Diff | Action | Sample targets |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | issue | advisory | issue refs advisory without registry | prose+backticked-ref | issue-number | nferna26/anti-slop | python/markdown | not_supplied | docs_update | anti-slop-pr-26, anti-slop-pr-27, anti-slop-pr-28 |
| 2 | card | fail | source/card refs that do not resolve | bullet+backticked-ref+validation-claim | source-card-id | nferna26/anti-slop | python/markdown | not_supplied | benchmark_case | anti-slop-pr-27 |
| 2 | card | fail | source/card refs that do not resolve | bullet+backticked-ref+example-or-fixture+validation-claim | source-card-id | nferna26/anti-slop | python/markdown | not_supplied | benchmark_case | anti-slop-pr-27 |
| 2 | file | fail | file refs that do not resolve | bullet+backticked-ref+example-or-fixture+validation-claim | docs/ depth=1 ext=.md | nferna26/anti-slop | python/markdown | not_supplied | benchmark_case | anti-slop-pr-27 |
| 2 | file | fail | file refs that do not resolve | bullet+backticked-ref+example-or-fixture | docs/ depth=1 ext=.md | nferna26/anti-slop | python/markdown | not_supplied | benchmark_case | anti-slop-pr-33 |
| 2 | issue | advisory | issue refs advisory without registry | bullet+backticked-ref+validation-claim | issue-number | nferna26/anti-slop | python/markdown | not_supplied | docs_update | anti-slop-pr-26, anti-slop-pr-27 |
| 2 | issue | advisory | issue refs advisory without registry | bullet+backticked-ref | issue-number | nferna26/anti-slop | python/markdown | not_supplied | docs_update | anti-slop-pr-26, anti-slop-pr-32 |
| 2 | issue | advisory | issue refs advisory without registry | bullet+example-or-fixture+validation-claim | issue-number | nferna26/anti-slop | python/markdown | not_supplied | docs_update | anti-slop-pr-28 |
| 1 | file | fail | file refs that do not resolve | bullet+backticked-ref+validation-claim | docs/ depth=1 ext=.md | nferna26/anti-slop | python/markdown | not_supplied | benchmark_case | anti-slop-pr-27 |
| 1 | file | fail | file refs that do not resolve | bullet+backticked-ref | docs/ depth=1 ext=.md | nferna26/anti-slop | python/markdown | not_supplied | benchmark_case | anti-slop-pr-33 |
| 1 | file | fail | file refs that do not resolve | bullet+backticked-ref+example-or-fixture+red-green | absolute-path | nferna26/anti-slop | python/markdown | not_supplied | benchmark_case | anti-slop-pr-34 |
| 1 | issue | advisory | issue refs advisory without registry | bullet+backticked-ref+example-or-fixture+validation-claim | issue-number | nferna26/anti-slop | python/markdown | not_supplied | docs_update | anti-slop-pr-27 |

## Learning Decision

No resolver repair is justified from this first sample. The top cluster is advisory issue references without an issue registry, which is an intentional offline boundary. The hard-failure clusters are good regression inputs, not evidence for broad pattern relaxation.
