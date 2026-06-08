# Agent Claim Density Audit

Report-mode audit over committed public-safe real artifacts. This does not contact external repos, call a model/API, or read local-only artifacts.

Scope note: the committed saved-PR-body corpus currently has 8 PR bodies, so this audit uses 8 saved PR bodies plus 12 curated `kb/log.md` tranche/report entries. The KB entries are real public-safe project reports, not synthetic benchmark cases.

A finding here means a reference or receipt did or did not resolve in the current checkout. It does not judge correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.

## Summary

- Artifacts: 20 ({'kb-log-entry': 12, 'saved-pr-body': 8})
- Checkable claim density: 41.98 claims / 100 lines
- Hard unresolved rate: 12.8%
- Artifacts with at least one claim: 20
- 30-day falsifier trend: PASS

## Top Claim Types

- file: 66
- changed_file: 16
- source_id: 14
- source_card: 12
- issue: 12
- card_id: 11
- commit: 7
- command_receipt: 3
- card_path: 2
- test: 1

## Candidate False-Positive Clusters

- unresolved card_id reference: 4
- path refs that do not resolve in current checkout: 4
- unresolved source_card reference: 3
- missing command receipts for historical validation claims: 3

## Artifact Detail

- saved-pr-11 (saved-pr-body, proof/pr-provenance-dogfood/bodies/pr-11.txt): 8 claims, 0 hard unresolved, 47.06 claims/100 lines
- saved-pr-19 (saved-pr-body, proof/pr-provenance-dogfood/bodies/pr-19.txt): 3 claims, 0 hard unresolved, 8.57 claims/100 lines
- saved-pr-21 (saved-pr-body, proof/pr-provenance-dogfood/bodies/pr-21.txt): 22 claims, 3 hard unresolved, 62.86 claims/100 lines
- saved-pr-22 (saved-pr-body, proof/pr-provenance-dogfood/bodies/pr-22.txt): 24 claims, 0 hard unresolved, 68.57 claims/100 lines
- saved-pr-24 (saved-pr-body, proof/pr-provenance-dogfood/bodies/pr-24.txt): 15 claims, 0 hard unresolved, 34.88 claims/100 lines
- saved-pr-25 (saved-pr-body, proof/pr-provenance-dogfood/bodies/pr-25.txt): 6 claims, 0 hard unresolved, 16.22 claims/100 lines
- saved-pr-26 (saved-pr-body, proof/pr-provenance-dogfood/bodies/pr-26.txt): 9 claims, 0 hard unresolved, 25.0 claims/100 lines
- saved-pr-27 (saved-pr-body, proof/pr-provenance-dogfood/bodies/pr-27.txt): 27 claims, 8 hard unresolved, 60.0 claims/100 lines
- kb-log-01 (kb-log-entry, kb/log.md:13): 4 claims, 0 hard unresolved, 80.0 claims/100 lines
- kb-log-02 (kb-log-entry, kb/log.md:15): 7 claims, 0 hard unresolved, 140.0 claims/100 lines
- kb-log-03 (kb-log-entry, kb/log.md:16): 1 claims, 0 hard unresolved, 20.0 claims/100 lines
- kb-log-04 (kb-log-entry, kb/log.md:17): 1 claims, 0 hard unresolved, 20.0 claims/100 lines
- kb-log-05 (kb-log-entry, kb/log.md:25): 2 claims, 0 hard unresolved, 40.0 claims/100 lines
- kb-log-06 (kb-log-entry, kb/log.md:27): 3 claims, 0 hard unresolved, 60.0 claims/100 lines
- kb-log-07 (kb-log-entry, kb/log.md:28): 1 claims, 0 hard unresolved, 20.0 claims/100 lines
- kb-log-08 (kb-log-entry, kb/log.md:29): 1 claims, 0 hard unresolved, 20.0 claims/100 lines
- kb-log-09 (kb-log-entry, kb/log.md:37): 4 claims, 1 hard unresolved, 80.0 claims/100 lines
- kb-log-10 (kb-log-entry, kb/log.md:39): 3 claims, 2 hard unresolved, 60.0 claims/100 lines
- kb-log-11 (kb-log-entry, kb/log.md:40): 1 claims, 0 hard unresolved, 20.0 claims/100 lines
- kb-log-12 (kb-log-entry, kb/log.md:41): 2 claims, 0 hard unresolved, 40.0 claims/100 lines
