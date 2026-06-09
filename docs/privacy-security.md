# Privacy And Security

Anti-Slop Receipts is a local reference/receipt resolver. It is designed for
local execution against a checkout and local JSON receipts.

## Runtime Boundary

- Runtime commands use the Python standard library only.
- There is no telemetry.
- There is no model call, hosted API, RAG layer, vector store, or runtime
  service.
- There is no GitHub API token requirement; the PR event preset reads the
  Actions event JSON and local checkout files.
- Install commands may fetch the package through `pip`, but checker/runtime
  commands do not need network access.

## Receipt Contents

`anti-slop-run` writes command receipts under `.anti-slop/receipts/*.json`.
By default it stores stdout/stderr hashes, byte counts, command metadata,
duration, exit code, git head, timestamp, and optional explicit metrics. It does
not store raw stdout/stderr by default.

Bounded excerpts are explicit opt-in through `--excerpt-bytes`. Bounded excerpts
can be useful for local debugging, but they are also the highest-risk receipt
field. Do not enable excerpts for commands that may print secrets, credentials,
`.env` values, private paths, raw API JSON, answer keys, raw transcripts, or raw
copyrighted text.

## Artifact Upload Risk

The vendorable GitHub workflow can upload `.anti-slop/receipts/*.json` and
`.anti-slop/claims.json` as CI artifacts. This is artifact upload risk: those
files may contain command strings, cwd values, git heads, metric names/values,
path-like references, and, if explicitly enabled, bounded excerpts.

Only upload artifacts when that data is appropriate for the repository's CI
visibility and retention settings. Artifact upload preserves local command and
reference facts for review; it is not proof of correctness, relevance, source
truth, support, safety, advice quality, reasoning, benchmark validity,
statistical meaning, or canon.

## Forbidden Report And Receipt Content

Do not put the following in agent reports, command receipts, metric receipts,
workflow summaries, committed fixtures, or uploaded artifacts:

- secrets;
- credentials;
- `.env` values;
- private paths;
- raw API JSON;
- answer keys;
- raw transcripts;
- raw copyrighted text;
- hidden condition maps or hidden canon.

## Workflow Permissions

The shipped report-mode workflow uses read-only checkout permissions. It does
not need write permissions, a GitHub API token, model credentials, telemetry
credentials, or external service credentials.

For package/install naming, see
[`docs/package-install-naming.md`](package-install-naming.md).
