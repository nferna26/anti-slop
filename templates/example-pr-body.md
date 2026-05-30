<!--
Example PR description for anti-slop-pr. Adapt it for your own PR, then run:
  anti-slop-pr --root . templates/example-pr-body.md
The real references below are path-like and resolve against THIS repo, so the
example PASSES. (#1 is advisory unless you pass --issue-registry; a bare basename
without a '/' is treated as a name, not a path, and is not checked.) The
illustrative example refs in "Notes" are wrapped in an ignore block so they do
not flag.
-->

# Example: document the provenance checker

Relates to #1.

## What

- Updates `docs/pr-provenance.md` with usage notes.
- Implemented in `scripts/gate_pr_provenance.py`.

## Notes

Swap in your real references. The checker fails if any cited HARD reference (a
path-like file, a test node, or a source-card ID) does not resolve; issue refs
without a registry and commit-SHA refs are advisory. The illustrative examples
below are wrapped so they do not flag:

<!-- anti-slop-pr: ignore-start -->
e.g. a test node `tests/test_x.py::test_name` or a source-card ID
`BK-1234-card-001` that you would replace with real ones.
<!-- anti-slop-pr: ignore-end -->
