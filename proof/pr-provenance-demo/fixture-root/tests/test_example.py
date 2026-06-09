"""Fixture test module for the anti-slop-pr demo (not run as a real test).

Defines test nodes the passing PR body resolves to, so the provenance checker
can confirm a cited `tests/test_example.py::test_widget` node actually exists.
"""


def test_widget():
    assert True


def test_locator():
    assert True
