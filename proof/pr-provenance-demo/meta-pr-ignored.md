<!--
SAMPLE "meta" PR body, same as meta-pr.md but using the explicit ESCAPE HATCH:
the fabricated example references are wrapped in an ignore-start/ignore-end
block, so anti-slop-pr does not treat them as real claims and the body PASSES.
The real reference outside the block is still checked. Not canon, not source
truth.
-->

# Document the provenance checker

This PR documents the checker. The example references it discusses are wrapped so
the checker does not treat them as real claims:

<!-- anti-slop-pr: ignore-start -->

As an example, an AI-written PR might cite a nonexistent issue #9999, claim it
added `docs/does-not-exist.md`, and cite a fabricated card `BK-9999-card-001`.

<!-- anti-slop-pr: ignore-end -->

The real change adds `docs/example.md` — checked normally, and it resolves.
