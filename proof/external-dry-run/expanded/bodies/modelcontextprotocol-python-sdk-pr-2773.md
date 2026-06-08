The stdio test suite has a long flake history (#1775, #1158, #559, #401). Auditing it surfaced real bugs in the client transport's shutdown path. This PR fixes the transport and rebuilds the stdio tests so they are deterministic.

## Motivation and Context

**Shutdown bugs fixed** (each has a regression test that fails on `main`):

1. Cancelling `stdio_client` could deadlock shutdown forever.
   - Cleanup was not shielded, so a cancelled client fell into anyio's `Process.aclose()`, which waits for *all pipes* to close — and a server with a child of its own (`npx ...`, `uv run ...`) holds the pipes open indefinitely.
2. Tree-kill silently did nothing when the server process had already died.
   - `os.getpgid()` raises once the leader is reaped, leaking every surviving child. The group is now killed via the spawn-time pgid.
3. "Did the server exit?" actually checked "did all pipes close?".
   - `process.wait()` is pipe-gated on asyncio 3.11+, so a server that exited promptly but left a background child running was misclassified as hung and its whole tree killed. The wait now keys on `returncode`, which reflects process death alone.
4. The Windows fallback's `wait()` could not be cancelled.
   - It ran in a non-cancellable worker thread, so the timeout around it could never fire and escalation was unreachable.
5. I/O on a dead server leaked raw backend exceptions.
   - Writing leaked `ConnectionResetError`; reading leaked `BrokenResourceError`. Both now surface as clean session closure. Fixes #1960.
6. A killed process was never reaped.
   - The unclosed subprocess transport leaked a `ResourceWarning` into whatever ran next.

The whole sequence now lives in one cancellation-shielded function with named timeouts: close stdin → grace period keyed on process death → terminate tree → bounded wait → kill tree. See `docs/migration.md`.

**Test rebuild:**

- Transport logic (framing, parse errors, escalation timing, shutdown edges) now runs in process against a small fake process. No sleeps, no polling; escalation timing is pinned on trio's virtual clock.
- Real subprocesses remain only where the OS itself is under test: group kill semantics (including a dead leader), SIGKILL after an ignored SIGTERM, exec failure. 5 tests, down from 14.
- New `tests/transports/stdio/` suite pins the end-to-end lifecycle on both platforms: clean exit without escalation, cancellation kills the whole tree, stderr routing, and the child-survival policy.
- Deleted the `tee`-based tests and `test_1027_win_unreachable_cleanup.py` (their properties are re-pinned above). `test_552_windows_hang.py` now asserts real outcomes instead of swallowing exceptions.

## How Has This Been Tested?

- 100% line+branch coverage; the stdio surface runs in ~5s (was ~10.8s)
- Every fix verified two ways: its regression test fails on `main`, and the OS-level claims were verified empirically on asyncio and trio
- 600 clean full-suite runs on GitHub-hosted runners (300 Windows / 300 Ubuntu, Python 3.10–3.14), plus stress runs under xdist and CPU saturation: zero failures, zero orphan processes

## Breaking Changes

- `terminate_windows_process` (deprecated) is removed; `terminate_windows_process_tree` no longer takes the unused `timeout_seconds`.
- POSIX: a server that exits cleanly no longer has its surviving background children killed (the old kill was a side effect of bug 3). A server that ignores shutdown still gets its whole tree killed.
- Windows: surviving job members are reaped deterministically at shutdown rather than at GC time.

Details in `docs/migration.md`.

## Types of changes

- [x] Bug fix (non-breaking change which fixes an issue)
- [x] Breaking change (fix or feature that would cause existing functionality to change)

## Checklist

- [x] I have read the [MCP Documentation](https://modelcontextprotocol.io)
- [x] My code follows the repository's style guidelines
- [x] New and existing tests pass locally
- [x] I have added appropriate error handling
- [x] I have added or updated documentation as needed

## Additional context

Two known limitations are documented in code rather than fixed:

- The shielded shutdown holds against anyio-level cancellation, but a native `task.cancel()` delivered mid-cleanup can still abort it (no backend-neutral way to refuse native cancellation).
- On Windows, children spawned before the Job Object assignment completes are outside the job (pre-existing; a `CREATE_SUSPENDED` spawn is the follow-up if it bites).

<sub>[AI Disclaimer](https://gist.github.com/maxisbey/6123d132484e4c533eab519a2800693d)</sub>
