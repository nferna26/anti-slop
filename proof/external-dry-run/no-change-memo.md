# External Dry-Run No-Change Memo

Decision: no resolver repair in CORE-977.

The top cluster is `issue refs advisory without registry`, which is intentional because the checker has no GitHub API/token dependency and cannot know issue state offline without a supplied registry. The hard-failure clusters are missing file/test/source-card references in saved PR bodies or documented examples; those are appropriate benchmark regression inputs and docs reminders, not a reason to relax resolver semantics.

Before/after impact is unchanged because no resolver code changed:

- Checkable claims: 92 -> 92
- Hard unresolved rate: 17.6% -> 17.6%
- Advisory rate: 16.3% -> 16.3%
- Cluster observations: 27 -> 27

Boundary: this memo is about deterministic reference/receipt resolution only. It does not judge correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.
