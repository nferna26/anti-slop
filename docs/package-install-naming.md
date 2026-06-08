# Package And Install Naming

Anti-Slop Receipts is the product name.

The public launch posture keeps the product name separate from current package
and command names so adopters can install without a compatibility migration.

## Policy

- Anti-Slop Receipts is the product name.
- anti-slop-lineage remains the current Python distribution name.
- anti-slop-claims is the canonical checker for Markdown/text agent reports.
- anti-slop-run is the receipt producer for local command/metric receipts.
- anti-slop-pr-event is the GitHub PR-body preset for Actions event payloads.
- anti-slop-pr remains the PR-body compatibility wrapper.
- anti-slop-lineage remains the source/card lineage resolver command.
- No release or tag is created by this install guidance.
- Do not rename adopter workflows to a broad slop detector.

The names are intentionally conservative. `anti-slop-lineage` predates the
Anti-Slop Receipts product wording and remains the install distribution for
compatibility. The newer commands describe the current hierarchy:
`anti-slop-run` writes receipts, `anti-slop-claims` checks reports, and
`anti-slop-pr-event` is a PR-body preset.

## Install Guidance

Preview install:

```sh
pip install "anti-slop-lineage @ git+https://github.com/nferna26/anti-slop"
```

Pinned install for repeatable CI:

```sh
pip install "anti-slop-lineage @ git+https://github.com/nferna26/anti-slop@<tag-or-full-sha>"
```

The preview install tracks repo head. A pinned tag or full commit SHA is the
safer supply-chain posture for CI. This document does not create a release, tag,
alias, package rename, or enforcement default.

## Boundary

The install surface verifies deterministic reference/receipt resolution only. It
does not verify correctness, relevance, source truth, support, safety, advice
quality, reasoning, benchmark validity, statistical meaning, or canon.

For data-handling rules, see [`docs/privacy-security.md`](privacy-security.md).
