<!--
SAMPLE "meta" PR body for the anti-slop-pr demo: a PR that DOCUMENTS the checker
and therefore cites fabricated example references on purpose. Without an ignore
directive, anti-slop-pr (correctly) FAILS it — those example refs do not resolve.
This is the known boundary the ignore directives exist for. Not canon, not
source truth.
-->

# Document the provenance checker

This PR documents the checker. As an example, an AI-written PR might cite a
nonexistent issue #9999, claim it added `docs/does-not-exist.md`, and cite a
fabricated card `BK-9999-card-001` — none of which resolve.

The real change adds `docs/example.md`.
