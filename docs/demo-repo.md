# Demo Repo Assets

This document is the reproducible demo asset checklist for a future public demo
repo or screen recording. It does not add outreach and does not claim more than
reference/receipt resolution only.

## Reproducible Demo Script

From this repo:

```sh
make agent-claim-demo
```

Expected story:

- The fake report FAILS with exact line reasons.
- The receipt-backed report PASSES after local receipts exist.
- The sample output is committed at
  `proof/agent-claim-demo/sample-output.md`.

For the report-mode workflow surface:

```sh
make adoption-smoke
```

Expected story:

- The workflow template runs `anti-slop-pr-event --root . --report`.
- Report mode exits 0 even when fabricated refs are reported.
- Optional receipt steps run `anti-slop-run -- make validate` and
  `anti-slop-claims --receipts .anti-slop/receipts --json
  .anti-slop/claims.json --report AGENT_FINAL_REPORT.md`.
- GitHub Actions appends compact tables to `GITHUB_STEP_SUMMARY` when that file
  is available.
- `.anti-slop/receipts/*.json` and `.anti-slop/claims.json` are retention
  artifacts, not correctness evidence.

## screenshot checklist

- Terminal showing `make agent-claim-demo`.
- Fake report section with FAIL and line-level unresolved reference reasons.
- Receipt-backed report section with PASS.
- Workflow Step Summary table showing report-mode findings.
- Artifact upload list showing receipts JSON and claims JSON.
- README non-goal text visible enough to show the narrow claim boundary.

## GIF checklist

- Keep under 60 seconds.
- Start with the fake report FAIL.
- Run or show the receipt-producing command.
- End on the receipt-backed report PASS.
- Include one frame of the Step Summary/report-mode workflow.
- Avoid cropped output that hides `--report`, line reasons, or the non-goals.

## HN-sized launch copy

Anti-Slop Receipts makes AI coding agents cite receipts, not vibes. It checks
whether files, tests, issues, commits, local command receipts, and simple metric
receipts cited in agent reports actually resolve against the repo. It is local,
stdlib-only, report-mode by default, and intentionally narrow: reference/receipt
resolution only, not correctness or source truth.

## X-sized launch copy

Anti-Slop Receipts checks AI-agent reports for resolvable files, tests, commits,
commands, and metrics. Local, stdlib-only, report mode by default. It proves
reference/receipt resolution only, not correctness.
