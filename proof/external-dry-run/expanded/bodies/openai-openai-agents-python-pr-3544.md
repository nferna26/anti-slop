### Summary

`src/agents/models/_openai_retry.py` was at 77% coverage: several low-level helpers (header parsing, retry-after parsing, status/error-code extraction) and a few `get_openai_retry_advice` branches were untested. This adds focused unit tests that bring the module to 95% without touching any runtime code.

### Changes

- New `tests/models/test_openai_retry_helpers.py` covering:
  - `_header_lookup` for plain mappings (case-insensitive) and `httpx.Headers`.
  - `_get_header_value` via the `response_headers` attribute path.
  - `_parse_retry_after_ms` and `_parse_retry_after` for numeric, HTTP-date, negative, and invalid inputs.
  - `_get_status_code` via `status_code` and `status` attributes.
  - `_get_error_code` via nested and top-level `body` mappings.
  - `get_openai_retry_advice` for the `unsafe_to_replay`, websocket-request, `x-should-retry: false`, and retry-after-only branches.

### Test plan

- `uv run pytest tests/models/test_openai_retry_helpers.py` passes (11 tests).
- Combined with the existing `test_model_retry.py`, `_openai_retry.py` coverage rises from 77% to 95%.
- `ruff format`, `ruff check`, and `mypy` are clean on the new file.
