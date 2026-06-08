<!-- AI/LLM agents: be concise and specific. Do not check the box below. -->

HUMAN:


- [x] A human has tested these changes.

AGENT:

---

## Why

The runtime API was receiving continuous `GET /sessions/{id}` requests for stopped sandboxes. `_get_sandbox_by_session_api_key_legacy` was the source: when a session key had no hash stored in the DB it fell through two stages:

1. `GET /list` — only returns *running* runtimes, so a stopped sandbox key never matched and always fell through to stage 2.
2. Iterate **every** `StoredRemoteSandbox` in the DB (including long-stopped ones) and call `_get_runtime` → `GET /sessions/{id}` for each, looking for a `session_api_key` match. This is the direct cause of the spurious stopped-sandbox queries.

The legacy method was needed for sandboxes created before the `session_api_key_hash` column was added. Since sandboxes expire after 2 weeks and the hash column has been in place far longer, no unhashed sandboxes remain. All new sandboxes have their hash stored immediately in `start_sandbox`, and any old sandbox that was successfully looked up via the legacy path had its hash backfilled at that time.

## Summary

- Deleted `_get_sandbox_by_session_api_key_legacy` (~50 lines) from `RemoteSandboxService`.
- `get_sandbox_by_session_api_key` now returns `None` immediately when the hash DB lookup finds nothing — no `GET /list` call, no per-sandbox `GET /sessions/{id}` calls.
- Removed three legacy-path tests; simplified the "not found" test to match the new behaviour.

## Issue Number

N/A

## How to Test

The three removed tests covered the deleted code paths. The surviving tests (`test_get_sandbox_by_session_api_key_with_hash`, `test_get_sandbox_by_session_api_key_not_found`, `test_get_sandbox_by_session_api_key_runtime_error`) exercise the full remaining logic.

To verify the runtime API noise is gone: check that `GET /sessions/{id}` requests for stopped sandboxes no longer appear in runtime API logs after deploying.

## Video/Screenshots

Conversations start:
<img width="1026" height="589" alt="image" src="https://github.com/user-attachments/assets/c288c2af-adfe-4684-9f8c-dadd0f9961ec" />

Conversations Can be paused, resumed, deleted
<img width="1028" height="550" alt="image" src="https://github.com/user-attachments/assets/e7937267-2b17-4ceb-9515-ec41caefa746" />


## Type

- [ ] Bug fix
- [ ] Feature
- [x] Refactor
- [ ] Breaking change
- [ ] Docs / chore

## Notes

This is a safe cleanup — the legacy code path has had no effect for longer than the 2-week sandbox TTL. The only caller of `_get_sandbox_by_session_api_key_legacy` was `get_sandbox_by_session_api_key` itself (line 442 before this change).

_This PR was created by an AI agent (OpenHands) on behalf of the user._

---

To run this PR locally, use the following command:

GUI with Docker:
```
docker run -it --rm   -p 3000:3000   -v /var/run/docker.sock:/var/run/docker.sock   --add-host host.docker.internal:host-gateway   --name openhands-app-0e53a46   docker.openhands.dev/openhands/openhands:0e53a46
```
