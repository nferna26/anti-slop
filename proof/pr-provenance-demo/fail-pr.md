<!--
SAMPLE PR description (intentionally failing). It cites references that do NOT
resolve against the demo fixture root, modelling the fabricated citations an
AI-written PR description can contain. anti-slop-pr should FAIL this body
(exit 1). Not canon, not source truth — a fixture for the demo only.

Planted failures: a fake issue (#9999), a missing doc (docs/missing.md), a bad
test node (::test_nope), a fabricated card (BK-7099-card-001), and a line ref
past end of file (docs/example.md:L99).
-->

# Add the example widget

Closes #9999.

## What

- Adds `docs/missing.md` documenting the widget.
- Covered by `tests/test_example.py::test_nope`.
- Supported by `BK-7099-card-001` (source `BK-7099`).

## Notes

The relevant section is at `docs/example.md:L99`.
