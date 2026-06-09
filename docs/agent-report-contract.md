# Agent Report Contract

Use this contract when an AI coding agent writes a final report that will be
checked by `anti-slop-claims`.

Anti-Slop resolves references and receipts only. It does not prove correctness,
relevance, source truth, support, safety, advice quality, reasoning, benchmark
validity, statistical meaning, or canon.

Package/install naming is documented in
[`docs/package-install-naming.md`](package-install-naming.md). Privacy/security
rules and forbidden report/receipt content are documented in
[`docs/privacy-security.md`](privacy-security.md).

## Local Receipt Flow

Run commands through `anti-slop-run` before claiming they passed:

```sh
anti-slop-run -- make validate
anti-slop-claims --root . --receipts .anti-slop/receipts --json .anti-slop/claims.json --report AGENT_FINAL_REPORT.md
```

Use report mode first. Drop `--report` only when a repo intentionally wants
hard failures for missing references/receipts.

## Copyable `AGENT_FINAL_REPORT.md`

```md
# Agent Final Report

## Summary

- Changed `path/to/file.ext`.
- Updated `docs/specific-doc.md`.

## Receipts

- `make validate` passed.
- `pytest` passed.

## References

- Main code: `src/module.py`
- Tests: `tests/test_module.py::test_behavior`
- Docs: `docs/specific-doc.md`

## Known Limits

- Anti-Slop verifies these references and receipts only.
- It does not prove correctness, relevance, source truth, support, safety,
  advice quality, reasoning, benchmark validity, statistical meaning, or canon.
```

Keep claims concrete. Prefer "changed `src/module.py`" and "`make validate`
passed" over "fixed the bug safely" or "fully supported."

## Receipt Examples

### pytest

```sh
anti-slop-run -- pytest
```

Report claim:

```md
- `pytest` passed.
```

### npm

```sh
anti-slop-run -- npm test
anti-slop-run -- npm run lint
```

Report claim:

```md
- command `npm test` exited 0.
- command `npm run lint` exited 0.
```

### pnpm

```sh
anti-slop-run -- pnpm test
anti-slop-run -- pnpm lint
```

Report claim:

```md
- command `pnpm test` exited 0.
- command `pnpm lint` exited 0.
```

### cargo

```sh
anti-slop-run -- cargo test
anti-slop-run -- cargo clippy -- -D warnings
```

Report claim:

```md
- command `cargo test` exited 0.
- command `cargo clippy -- -D warnings` exited 0.
```

### go

```sh
anti-slop-run -- go test ./...
```

Report claim:

```md
- command `go test ./...` exited 0.
```

### make

```sh
anti-slop-run -- make validate
anti-slop-run -- make package-smoke
```

Report claim:

```md
- `make validate` passed.
- command `make package-smoke` exited 0.
```

## Metrics

Metric claims require explicit metric values on a command receipt:

```sh
anti-slop-run --metric score=0.82 -- python3 scripts/report_score.py
anti-slop-run --metric score.before=0.70 --metric score.after=0.82 -- python3 scripts/report_score.py
```

Report claim:

```md
- score is 0.82.
- score improved from 0.70 to 0.82.
```

Anti-Slop checks only that a fresh receipt contains the stated metric value or
before/after pair. It does not validate the benchmark, judge, sample, rubric,
statistical meaning, or whether the metric matters.

## Diff-Aware Changed Files

For claims like "updated `docs/api.md`", add a diff range when checking:

```sh
anti-slop-claims --root . --diff HEAD~1..HEAD --report AGENT_FINAL_REPORT.md
```

Without `--diff`, changed-file language is advisory/skipped. With a supplied
diff range, the cited path must appear in `git diff --name-only <range>`.

## Do Not Put In Reports

- Secrets, credentials, `.env` values, private paths, raw API JSON, answer keys,
  raw transcripts, raw copyrighted text, or hidden maps.
- Broad claims like "fixed", "safe", "production-ready", "fully supported", or
  "correct" unless they are clearly outside the resolver and backed by human
  review elsewhere.
- Raw stdout/stderr excerpts from commands that may contain sensitive data.
