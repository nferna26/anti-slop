# Draft Release Notes

Draft release notes for operator review.

No release tag has been created. These notes are a draft for operator review
only. No outreach, GitHub release, tag action, or enforcement default change is
approved without operator approval.

## Anti-Slop Receipts preview

Anti-Slop Receipts provides deterministic reference/receipt resolution only for
AI-agent reports and PR bodies.

Included surfaces:

- `anti-slop-claims`: generic Markdown/text checker with JSON output, diff-aware
  changed-file checks, command receipt matching, and simple metric receipt
  matching.
- `anti-slop-run`: local command/metric receipt writer that hashes
  stdout/stderr by default.
- `anti-slop-pr-event`: GitHub Actions PR-body preset, report mode by default,
  with optional Step Summary and artifact retention.
- `anti-slop-pr`: PR-body compatibility wrapper.
- `anti-slop-lineage`: source/card lineage compatibility command.

Install examples:

```sh
pip install "anti-slop-lineage @ git+https://github.com/nferna26/anti-slop"
pip install "anti-slop-lineage @ git+https://github.com/nferna26/anti-slop@<tag-or-full-sha>"
```

Boundary: this release resolves references and receipts. It does not prove
correctness, relevance, source truth, support, safety, advice quality,
reasoning, benchmark validity, statistical meaning, or canon.
