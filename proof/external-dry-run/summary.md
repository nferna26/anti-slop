# External Dry-Run Summary

Status: `dry_run_not_adoption`.

This is a report-mode dry run over committed public-safe saved PR bodies. It does not contact repos at runtime, call GitHub APIs, use tokens, call models, open PRs, post comments, or automate adoption.

A finding means a reference or receipt did or did not resolve. It does not prove correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.

## Aggregate

- Schema: `anti-slop-external-dry-run.v1`
- Policy: `external-dry-run-policy.v1`
- Target: saved public PR bodies from nferna26/anti-slop
- Artifacts: 10 (sufficient_saved_public_artifacts)
- Checkable claims: 92
- Checkable claims per 100 lines: 19.33
- Hard unresolved rate: 17.6%
- Advisory rate: 16.3%
- Kill-criterion risk: pass (fail if checkable_claims_per_100_lines < 5.0)
- Usefulness verdict: useful

## Top Reasons

- issue refs advisory without registry: 15
- file refs that do not resolve: 8
- source/card refs that do not resolve: 4

## Top Claim Types

- file: 63
- issue: 15
- commit: 9
- card: 4
- test: 1

## Sample Targets

- anti-slop-pr-26: nferna26/anti-slop#26 (saved_public_pr_body, anti-slop-pr-event)
- anti-slop-pr-27: nferna26/anti-slop#27 (saved_public_pr_body, anti-slop-pr-event)
- anti-slop-pr-28: nferna26/anti-slop#28 (saved_public_pr_body, anti-slop-pr-event)
- anti-slop-pr-29: nferna26/anti-slop#29 (saved_public_pr_body, anti-slop-pr-event)
- anti-slop-pr-30: nferna26/anti-slop#30 (saved_public_pr_body, anti-slop-pr-event)
- anti-slop-pr-31: nferna26/anti-slop#31 (saved_public_pr_body, anti-slop-pr-event)
- anti-slop-pr-32: nferna26/anti-slop#32 (saved_public_pr_body, anti-slop-pr-event)
- anti-slop-pr-33: nferna26/anti-slop#33 (saved_public_pr_body, anti-slop-pr-event)
- anti-slop-pr-34: nferna26/anti-slop#34 (saved_public_pr_body, anti-slop-pr-event)
- anti-slop-pr-35: nferna26/anti-slop#35 (saved_public_pr_body, anti-slop-pr-event)

## Artifact Metrics

- anti-slop-pr-26: 9 claims, 0 hard unresolved, 3 advisory, 25.71 claims/100 lines
- anti-slop-pr-27: 20 claims, 8 hard unresolved, 3 advisory, 45.45 claims/100 lines
- anti-slop-pr-28: 11 claims, 0 hard unresolved, 3 advisory, 26.19 claims/100 lines
- anti-slop-pr-29: 4 claims, 0 hard unresolved, 1 advisory, 7.55 claims/100 lines
- anti-slop-pr-30: 4 claims, 0 hard unresolved, 1 advisory, 7.55 claims/100 lines
- anti-slop-pr-31: 10 claims, 0 hard unresolved, 1 advisory, 17.24 claims/100 lines
- anti-slop-pr-32: 7 claims, 0 hard unresolved, 1 advisory, 16.28 claims/100 lines
- anti-slop-pr-33: 14 claims, 3 hard unresolved, 0 advisory, 19.72 claims/100 lines
- anti-slop-pr-34: 11 claims, 1 hard unresolved, 2 advisory, 28.21 claims/100 lines
- anti-slop-pr-35: 2 claims, 0 hard unresolved, 0 advisory, 5.26 claims/100 lines
