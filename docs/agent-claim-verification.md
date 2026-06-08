# Agent Claim Verification

Anti-Slop is deterministic **agent claim verification** for AI coding agents:
make the agent cite receipts, then check whether those references resolve.

Tagline: **Make AI coding agents cite receipts, not vibes.**

This is a narrow resolver contract. It checks references and receipts against
repo state where a mechanical check is possible. It does **not** verify
correctness, relevance, source truth, support, advice quality, reasoning,
safety, or canon.

`anti-slop-claims` is the generic artifact-checking entrypoint. PR descriptions
are surface #1 through the compatibility preset `anti-slop-pr` and its GitHub
Actions event wrapper `anti-slop-pr-event`. The category is broader: any
agent-authored claim surface can be made more inspectable by requiring concrete
references and receipts.

## Supported-Claims Matrix

| Claim type | Tier | Required artifact | What is verified | What is not verified | Example failure |
| --- | --- | --- | --- | --- | --- |
| File refs | Hard | A visible path-like file reference such as `docs/foo.md` or `scripts/tool.py:L42` | The referenced file exists under `--root`; line refs are within file length | Whether the file is relevant, correct, newly added, or semantically supports the claim | PR says "Adds `docs/rate-limits.md`" but that file is absent |
| Changed-file claims | Hard with `--diff`; advisory/skipped without it | Changed-file language near a path-like file ref plus a local git diff/range | The cited path resolves, and with `--diff`, the path appears in `git diff --name-only <range>` | Whether the diff is meaningful, complete, correct, or implements the described behavior | Agent says "Updated `docs/api.md`"; the file exists, but it is absent from the supplied diff |
| Test refs | Hard | A test node such as `tests/test_api.py::test_limits` | The test file exists and defines the named test/class node | Whether the test was run, passed, covers the claimed behavior, or proves correctness | PR says it is covered by `tests/test_api.py::test_limits` but that node is missing |
| Issue refs | Advisory by default; hard with registry | `#123` plus an optional numbers-only issue registry passed with `--issue-registry` | With a registry, the issue number appears in that registry; without a registry, the ref is reported advisory only | Issue state, labels, priority, user intent, or whether the PR fixes it | PR says "Fixes #4123" but `4123` is absent from the supplied registry |
| Commit refs | Advisory | A 7-40 character hex token checked against local git at `--root` | Local git can resolve the token as a commit object when possible | Whether the commit belongs to this branch/PR, why it matters, or whether a hex token was intended as a commit | PR cites `9f3a2b1`, but local git cannot resolve it |
| Command receipts | Hard for detected command-pass/exit claims | A fresh `anti-slop-command-receipt.v1` JSON receipt under `--receipts` | The command string/tag matches the claim, the receipt exit code matches the claimed result, and the receipt git head matches current `--root` HEAD when available | Whether the command proves correctness, whether output is complete, whether the environment was appropriate, or whether later edits invalidate the result semantically | Agent says "`make validate` passed" but no matching fresh receipt exists, the receipt is nonzero, or its git head is stale |
| Benchmark metric receipts | Hard for detected simple metric claims | A fresh command receipt with `metrics`, passed through `--receipts` | A stated scalar value (`score is 0.82`) or before/after pair (`score improved from 0.70 to 0.82`) appears exactly in a fresh receipt | Benchmark validity, judge quality, sample quality, statistical meaning, source truth, hidden condition maps, raw outputs, or any claim outside the receipt values | Agent says "score is 0.82" but the receipt says `0.81`, is stale, or is missing |
| Docs-updated claims | Advisory | A cited docs path such as `docs/foo.md` or `README.md` | The cited doc path resolves when path-like | Whether the doc was changed in this PR, accurately reflects behavior, or covers all user-facing surfaces | PR says "Docs updated" but only cites an existing unchanged README |
| Fixed / safe / supported claims | Out of scope | No artifact makes these mechanically verifiable by this resolver | Nothing beyond any references embedded inside the claim | Correctness, safety, security, user impact, causal fix quality, source support, advice quality, or reasoning quality | PR says "Fixed the race condition safely" while all refs resolve; the resolver still cannot prove the fix or safety claim |

## Boundary Rules

- A passing resolver result means referenced artifacts resolved. It is not a
  quality verdict.
- Report mode is the adoption default: print findings, exit 0, and let reviewers
  decide when to enforce.
- Enforcement is useful for hard resolution claims only. Use it to block missing
  file/test/card refs, not to claim the code is correct.
- Ignore directives are for intentionally fabricated examples in documentation.
  They should be line-scoped and auditable, not a broad escape from review.

## Current Surfaces

- `anti-slop-claims`: generic Markdown/text artifact checker for files such as
  `AGENT_FINAL_REPORT.md`; reuses the `anti-slop-pr` resolver engine. Supports
  structured `anti-slop-claims.v1` JSON receipts with per-ref line/type/tier/
  status/reason/evidence entries, plus optional local-git `--diff` changed-file
  checks and `--receipts` command/metric receipt checks.
- `anti-slop-run`: local command receipt writer for `anti-slop-command-receipt.v1`
  JSON. Hashes stdout/stderr by default and can record explicit metrics.
- `anti-slop-pr`: PR-body surface #1 and compatibility wrapper/preset.
- `anti-slop-pr-event`: reads the PR body from GitHub Actions event JSON without
  a GitHub API token and runs `anti-slop-pr`.
- `anti-slop-lineage`: resolves public-KB source/card lineage and is reused by
  `anti-slop-pr` for source-card refs.

## Proof and Adoption Surface

- `make agent-claim-demo`: 60-second offline demo. A fake agent report fails
  with line-level reasons; a receipt-backed report passes. Sample output:
  [`../proof/agent-claim-demo/sample-output.md`](../proof/agent-claim-demo/sample-output.md).
- `make agent-claim-benchmark`: deterministic 50-case synthetic checker corpus
  across file, changed-file, test, issue, commit, command-receipt, and
  metric-receipt claims. It measures resolver behavior, not agent/model quality.
- `make agent-claim-audit`: public-safe report-mode density audit over committed
  real PR bodies. It reports checkable-claim density, hard unresolved rate,
  candidate false-positive clusters, top claim types, and the 30-day falsifier
  trend; fewer than 20 real bodies is marked insufficient, not PASS.
- [`adoption-loop.md`](adoption-loop.md): external report-mode adoption playbook
  with target criteria, install prompt, PR template, metrics, opt-out etiquette,
  and candidate repositories for later review.

All current surfaces are stdlib-only and do not call a model, hosted API,
network service, vector store, RAG layer, or runtime server.

Not implemented here: semantic diff review, benchmark validity review, command
output interpretation, or any correctness/support/safety judgment.
