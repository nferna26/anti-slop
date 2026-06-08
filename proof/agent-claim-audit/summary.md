# Agent Claim Density Audit

Report-mode audit over committed public-safe real PR bodies. This does not contact external repos at runtime, call a model/API, or read local-only artifacts.

Scope note: the audit sample is the committed `proof/agent-claim-audit/bodies/pr-*.md` fixture set. The runner does not use `kb/log.md` snippets, synthetic benchmark cases, raw transcripts, local-only artifacts, or generated filler.

A finding here means a reference or receipt did or did not resolve in the current checkout. It does not judge correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.

## Summary

- Audit status: complete
- Sample status: sufficient_real_sample (25 / 20 required real artifacts)
- Artifacts: 25 ({'real-pr-body': 25})
- Checkable claim density: 25.55 claims / 100 lines
- Hard unresolved rate: 9.5%
- Artifacts with at least one claim: 25
- 30-day falsifier trend: PASS

## Top Claim Types

- file: 118
- changed_file: 38
- issue: 23
- source_id: 14
- commit: 14
- source_card: 12
- card_id: 11
- card_path: 2
- test: 1

## Candidate False-Positive Clusters

- path refs that do not resolve in current checkout: 8
- unresolved card_id reference: 4
- unresolved source_card reference: 3

## Artifact Detail

- pr-11 (real-pr-body, proof/agent-claim-audit/bodies/pr-11.md): 8 claims, 0 hard unresolved, 47.06 claims/100 lines
- pr-12 (real-pr-body, proof/agent-claim-audit/bodies/pr-12.md): 3 claims, 0 hard unresolved, 16.67 claims/100 lines
- pr-13 (real-pr-body, proof/agent-claim-audit/bodies/pr-13.md): 2 claims, 0 hard unresolved, 10.0 claims/100 lines
- pr-14 (real-pr-body, proof/agent-claim-audit/bodies/pr-14.md): 2 claims, 0 hard unresolved, 9.09 claims/100 lines
- pr-15 (real-pr-body, proof/agent-claim-audit/bodies/pr-15.md): 5 claims, 0 hard unresolved, 21.74 claims/100 lines
- pr-16 (real-pr-body, proof/agent-claim-audit/bodies/pr-16.md): 2 claims, 0 hard unresolved, 9.09 claims/100 lines
- pr-17 (real-pr-body, proof/agent-claim-audit/bodies/pr-17.md): 7 claims, 0 hard unresolved, 33.33 claims/100 lines
- pr-18 (real-pr-body, proof/agent-claim-audit/bodies/pr-18.md): 5 claims, 0 hard unresolved, 19.23 claims/100 lines
- pr-19 (real-pr-body, proof/agent-claim-audit/bodies/pr-19.md): 3 claims, 0 hard unresolved, 8.57 claims/100 lines
- pr-20 (real-pr-body, proof/agent-claim-audit/bodies/pr-20.md): 1 claims, 0 hard unresolved, 2.13 claims/100 lines
- pr-21 (real-pr-body, proof/agent-claim-audit/bodies/pr-21.md): 22 claims, 3 hard unresolved, 62.86 claims/100 lines
- pr-22 (real-pr-body, proof/agent-claim-audit/bodies/pr-22.md): 24 claims, 0 hard unresolved, 68.57 claims/100 lines
- pr-23 (real-pr-body, proof/agent-claim-audit/bodies/pr-23.md): 10 claims, 0 hard unresolved, 27.03 claims/100 lines
- pr-24 (real-pr-body, proof/agent-claim-audit/bodies/pr-24.md): 15 claims, 0 hard unresolved, 35.71 claims/100 lines
- pr-25 (real-pr-body, proof/agent-claim-audit/bodies/pr-25.md): 6 claims, 0 hard unresolved, 16.67 claims/100 lines
- pr-26 (real-pr-body, proof/agent-claim-audit/bodies/pr-26.md): 9 claims, 0 hard unresolved, 25.71 claims/100 lines
- pr-27 (real-pr-body, proof/agent-claim-audit/bodies/pr-27.md): 27 claims, 8 hard unresolved, 61.36 claims/100 lines
- pr-28 (real-pr-body, proof/agent-claim-audit/bodies/pr-28.md): 17 claims, 0 hard unresolved, 40.48 claims/100 lines
- pr-29 (real-pr-body, proof/agent-claim-audit/bodies/pr-29.md): 5 claims, 0 hard unresolved, 9.43 claims/100 lines
- pr-30 (real-pr-body, proof/agent-claim-audit/bodies/pr-30.md): 4 claims, 0 hard unresolved, 7.55 claims/100 lines
- pr-31 (real-pr-body, proof/agent-claim-audit/bodies/pr-31.md): 14 claims, 0 hard unresolved, 24.14 claims/100 lines
- pr-32 (real-pr-body, proof/agent-claim-audit/bodies/pr-32.md): 8 claims, 0 hard unresolved, 18.6 claims/100 lines
- pr-33 (real-pr-body, proof/agent-claim-audit/bodies/pr-33.md): 19 claims, 3 hard unresolved, 26.76 claims/100 lines
- pr-34 (real-pr-body, proof/agent-claim-audit/bodies/pr-34.md): 13 claims, 1 hard unresolved, 33.33 claims/100 lines
- pr-35 (real-pr-body, proof/agent-claim-audit/bodies/pr-35.md): 2 claims, 0 hard unresolved, 5.26 claims/100 lines
