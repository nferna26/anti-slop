<!--
SAMPLE PR description (passing). Every reference resolves against the demo
fixture root (proof/pr-provenance-demo/fixture-root/). anti-slop-pr should PASS
this body (exit 0). Not canon, not source truth — a fixture for the demo only.
-->

# Add the example widget

Closes #42.

## What

- Adds `docs/example.md` documenting the widget.
- Covered by `tests/test_example.py::test_widget` and
  `tests/test_example.py::test_locator`.
- The behaviour note is supported by reviewed lineage `BK-7001-card-001`
  (source `BK-7001`).

## Notes

The module header is at `tests/test_example.py:L1`. See #7 for the follow-up.
