# Agent Claim Verification

Anti-Slop is deterministic **agent claim verification** for AI coding agents:
make the agent cite receipts, then check whether those references resolve.

Tagline: **Make AI coding agents cite receipts, not vibes.**

This is a narrow resolver contract. It checks references and receipts against
repo state where a mechanical check is possible. It does **not** verify
correctness, relevance, source truth, support, advice quality, reasoning,
safety, or canon.

PR descriptions are surface #1 through `anti-slop-pr` and
`anti-slop-pr-event`. The category is broader: any agent-authored claim surface
can be made more inspectable by requiring concrete references and receipts.

## Supported-Claims Matrix

| Claim type | Tier | Required artifact | What is verified | What is not verified | Example failure |
| --- | --- | --- | --- | --- | --- |
| File refs | Hard | A visible path-like file reference such as `docs/foo.md` or `scripts/tool.py:L42` | The referenced file exists under `--root`; line refs are within file length | Whether the file is relevant, correct, newly added, or semantically supports the claim | PR says "Adds `docs/rate-limits.md`" but that file is absent |
| Changed-file claims | Advisory | A cited file path plus review/diff context outside the resolver | The cited path can resolve as a file ref when path-like | Whether the file was changed in this PR, whether the diff is meaningful, or whether the edit implements the described behavior | PR says "Updated `docs/api.md`" but the path exists only from an earlier commit |
| Test refs | Hard | A test node such as `tests/test_api.py::test_limits` | The test file exists and defines the named test/class node | Whether the test was run, passed, covers the claimed behavior, or proves correctness | PR says it is covered by `tests/test_api.py::test_limits` but that node is missing |
| Issue refs | Advisory by default; hard with registry | `#123` plus an optional numbers-only issue registry passed with `--issue-registry` | With a registry, the issue number appears in that registry; without a registry, the ref is reported advisory only | Issue state, labels, priority, user intent, or whether the PR fixes it | PR says "Fixes #4123" but `4123` is absent from the supplied registry |
| Commit refs | Advisory | A 7-40 character hex token checked against local git at `--root` | Local git can resolve the token as a commit object when possible | Whether the commit belongs to this branch/PR, why it matters, or whether a hex token was intended as a commit | PR cites `9f3a2b1`, but local git cannot resolve it |
| Command receipts | Advisory | A command named in the PR body and/or a cited receipt artifact committed under the repo | Any cited receipt path can be resolved as a file ref | Whether the command actually ran in the stated environment, whether output is complete, or whether the result remains true after later edits | PR says "`make validate` passed" but cites no receipt and the acceptance gate later fails |
| Benchmark receipts | Advisory | A public-safe benchmark/eval receipt path, decision doc, or run packet | The cited receipt artifact resolves if path-like | Benchmark correctness, judge quality, source truth, hidden condition maps, raw outputs, or any claim outside the frozen decision boundary | PR says a benchmark supports a broad advice claim when the cited decision only supports mechanical lineage |
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

- `anti-slop-pr`: checks an agent-written PR body against a repo root.
- `anti-slop-pr-event`: reads the PR body from GitHub Actions event JSON without
  a GitHub API token and runs `anti-slop-pr`.
- `anti-slop-lineage`: resolves public-KB source/card lineage and is reused by
  `anti-slop-pr` for source-card refs.

All current surfaces are stdlib-only and do not call a model, hosted API,
network service, vector store, RAG layer, or runtime server.
