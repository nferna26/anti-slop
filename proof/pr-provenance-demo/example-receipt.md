# anti-slop-pr Demo Receipt (example)

Example of the JSON receipt `anti-slop-pr --json` (and the demo) produce. Not
canon, not source truth. Deterministic and offline.

## pass-pr.md — PASS (exit 0)

```json
{
  "pr_file": "pass-pr.md",
  "root": "<.../proof/pr-provenance-demo/fixture-root>",
  "issue_registry": true,
  "require_reviewed_cards": true,
  "checks": {
    "file":  {"refs_checked": 2, "unresolved": [], "advisory": []},
    "test":  {"refs_checked": 2, "unresolved": [], "advisory": []},
    "issue": {"refs_checked": 2, "unresolved": [], "advisory": []},
    "card":  {"refs_checked": 3, "unresolved": [], "advisory": []}
  },
  "passed": true
}
```

## fail-pr.md — FAIL (exit 1)

```json
{
  "pr_file": "fail-pr.md",
  "checks": {
    "file":  {"refs_checked": 2, "unresolved": ["line 18: file does not resolve: docs/missing.md", "line 24: docs/example.md has 4 lines, ref needs >= 99"]},
    "test":  {"refs_checked": 1, "unresolved": ["line 19: test node not defined in tests/test_example.py: test_nope"]},
    "issue": {"refs_checked": 1, "unresolved": ["line 14: issue does not resolve: #9999"]},
    "card":  {"refs_checked": 3, "unresolved": ["20: unresolved source_card reference: BK-7099-card-001", "20: unresolved source_id reference: BK-7099", "20: unresolved card_id reference: BK-7099-card-001"]}
  },
  "passed": false
}
```

A receipt records a deterministic reference-resolution check, not PR correctness,
support, source truth, or canon. Line numbers and counts are reproducible; the
absolute `root` path varies by checkout.
