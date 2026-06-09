# Public PR Receipt Study

This memo records the first public-repo receipt-mining loop for Anti-Slop
Receipts. It is a learning artifact, not outreach and not enforcement. The loop
is report mode only.

Aggregate proof:

- `proof/public-pr-receipt-study/targets.json`
- `proof/public-pr-receipt-study/summary.json`
- `proof/public-pr-receipt-study/summary.md`
- `proof/public-pr-receipt-study/actionability.json`
- `proof/public-pr-receipt-study/actionability.md`

Schema: `anti-slop-public-pr-receipt-study.v1`.

## Method

The live loop fetched recent merged public PR metadata/bodies with `gh pr list`
from a manifest of 20 popular public AI/devtool repositories. Selection
preferred agent/receipt-ish language and reference patterns: agent, Codex,
Claude, Copilot, generated, validation, tests pass, pytest, make, benchmark,
metric, score, updated, added, changed, issue refs, file refs, test refs, and
commit refs.

The run checked 50 selected PR bodies across 10 repositories. For each selected
PR body, the harness shallow-cloned a temporary public checkout, checked out the
public merge commit, and ran Anti-Slop in report mode:

- `anti-slop-pr` for file, test, issue, commit, and card/source refs.
- `anti-slop-claims --receipts <empty-dir>` for command and metric receipt
  claims.

No outreach happened. No external PRs, comments, issues, maintainer contact, or
enforcement happened. No target project tests/builds were run. Temporary
checkouts, raw PR body text, raw resolver receipts, raw API JSON, temp paths,
credentials, secrets, and external repo contents were not committed.

## Results

Current aggregate from `proof/public-pr-receipt-study/summary.json`:

| Metric | Value |
| --- | ---: |
| PR bodies | 50 |
| Repositories | 10 |
| Checkout success | 50 |
| Checkable claims | 780 |
| Claims per 100 lines | 28.43 |
| Hard unresolved rate | 36.5% |
| Advisory rate | 67.0% |
| Sparse selected PR bodies | 3 |

Top aggregate clusters:

| Cluster | Count | Label |
| --- | ---: | --- |
| commit refs advisory under local-git resolution | 274 | non-actionable |
| issue refs advisory without registry | 249 | unclear |
| file refs unresolved | 28 | actionable |
| command claims without receipts | 26 | unclear |
| sparse PR bodies | 3 | non-actionable |

The bounded actionability label pass is aggregate-only. It labels clusters, not
raw external lines. The current labeled finding mix is 28 actionable, 277
non-actionable, 275 unclear, and 0 excluded.

## Surface Read

Natural PR bodies contain mechanically checkable claims, but they are noisy as a
receipt surface. The biggest clusters are advisory commit/issue references and
validation claims without attached machine-readable command receipts.

`AGENT_FINAL_REPORT.md` remains the cleaner hypothesis for receipt-backed
adoption because it can require explicit command and metric receipt citations.
This study does not prove that `AGENT_FINAL_REPORT.md` is better; it only shows
that natural public PR bodies often mention validation without attaching
machine-readable receipts.

## Boundary

This study checks deterministic reference/receipt resolution only. It does not
prove correctness, relevance, source truth, support, safety, advice quality,
reasoning, benchmark validity, statistical meaning, or canon. In short: it does
not prove correctness.

Machine-checkable boundary phrase: this study does not prove correctness.

The result is publishable as a narrow internal/public-safe learning memo, not as
maintainer-ready evidence and not as a launch blast. The next useful loop is to
run friendly opt-in installs or compare structured `AGENT_FINAL_REPORT.md`
artifacts against the same style of public-safe aggregate metrics.
