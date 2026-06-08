# Command And Metric Receipts

`anti-slop-run` records local command facts that `anti-slop-claims` can later
resolve. It is stdlib-only and local: no model, hosted API, network service,
GitHub API, or token.

The claim boundary is narrow. A command receipt can prove that a command was run
locally at a git head and exited with a recorded code. A metric receipt can prove
that a local receipt contains a stated number. Neither proves correctness,
relevance, source truth, support, benchmark validity, safety, advice quality,
reasoning, or canon.

For a copyable final-report structure and common stack examples, see
[`agent-report-contract.md`](agent-report-contract.md).
For package/install naming, see
[`docs/package-install-naming.md`](package-install-naming.md). For privacy,
artifact upload risk, and forbidden receipt content, see
[`docs/privacy-security.md`](privacy-security.md).

## Write A Command Receipt

```sh
anti-slop-run -- make validate
anti-slop-run -- pytest
```

Receipts are written under `.anti-slop/receipts/*.json` by default. Nonzero
commands still write receipts and `anti-slop-run` exits with the command's exit
code.

To write bounded stdout/stderr excerpts, opt in explicitly:

```sh
anti-slop-run --excerpt-bytes 1000 -- make validate
```

By default, stdout and stderr are hashed, not stored. Do not use excerpts for
commands that may print secrets, credentials, raw API JSON, `.env` content,
private paths, answer keys, or raw copyrighted text.

## Schema V1

`anti-slop-run` writes `anti-slop-command-receipt.v1` JSON:

```json
{
  "schema_version": "anti-slop-command-receipt.v1",
  "receipt_type": "command",
  "command": ["make", "validate"],
  "command_string": "make validate",
  "command_tags": ["make:validate"],
  "cwd": "/repo",
  "exit_code": 0,
  "duration_ms": 1234,
  "git_head": "0123456789abcdef0123456789abcdef01234567",
  "started_at": "2026-06-08T00:00:00Z",
  "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "stdout_bytes": 0,
  "stderr_bytes": 0,
  "tool_version": "0.1.0",
  "metrics": {}
}
```

Required fields are: `command`, `cwd`, `exit_code`, `duration_ms`, `git_head`,
`started_at`, `stdout_sha256`, `stderr_sha256`, `tool_version`.

Optional excerpt fields appear only when `--excerpt-bytes` is used:
`stdout_excerpt`, `stderr_excerpt`, `stdout_excerpt_bytes`,
`stderr_excerpt_bytes`, `stdout_excerpt_truncated`, and
`stderr_excerpt_truncated`.

## Check Command Claims

```sh
anti-slop-claims --root . --receipts .anti-slop/receipts AGENT_FINAL_REPORT.md
```

Supported command claim shapes include:

- `make validate passed`
- `pytest passed`
- `tests pass`
- ``command `make validate` exited 0``

Passing example:

```sh
anti-slop-run -- make validate
printf 'make validate passed.\n' > AGENT_FINAL_REPORT.md
anti-slop-claims --root . --receipts .anti-slop/receipts AGENT_FINAL_REPORT.md
```

Failure examples:

- Missing receipt: the artifact says `pytest passed`, but no matching receipt
  exists.
- Nonzero receipt: the artifact says `make validate passed`, but the matching
  receipt has `exit_code` other than `0`.
- Stale receipt: the artifact says `make validate passed`, but the matching
  receipt's `git_head` differs from the current `--root` git HEAD.

Freshness is checked when `--root` is a git checkout. If git HEAD cannot be read,
Anti-Slop records that fact in resolver evidence and does not claim git-head
freshness.

## Metric Receipts

Metrics are stored on command receipts:

```sh
anti-slop-run --metric score=0.82 -- python3 scripts/report_score.py
anti-slop-run --metric score.before=0.70 --metric score.after=0.82 -- python3 scripts/report_score.py
```

Supported metric claim shapes include:

- `score is 0.82`
- `score improved from 0.70 to 0.82`
- `metric improved from 0.70 to 0.82`

`anti-slop-claims --receipts <dir>` checks only that a fresh receipt contains the
stated metric value or before/after pair. It does not validate the benchmark,
judge, sample, rubric, statistical claim, semantic meaning, or whether an
improvement matters.
