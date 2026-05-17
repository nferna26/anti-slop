#!/usr/bin/env python3
"""Resolve canon_boost for the consult Skill from `<kb_root>/.consult.yaml`.

Always exits 0. Prints the integer boost to stdout. Non-default paths emit a
stderr warning so the Skill's trace can capture the reason. Fall back to
DEFAULT_BOOST (+2) on every failure mode; the consult Skill needs an integer
no matter what.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

DEFAULT_BOOST = 2


def _try_import_yaml():
    try:
        import yaml
        return yaml
    except ImportError:
        return None


def load_canon_boost(kb_root: Path) -> tuple[int, str | None]:
    """Return (boost, warning_or_none). Always succeeds."""
    config_path = kb_root / ".consult.yaml"
    if not config_path.exists():
        return DEFAULT_BOOST, None
    yaml = _try_import_yaml()
    if yaml is None:
        return DEFAULT_BOOST, (
            f"PyYAML not installed; cannot parse {config_path}, "
            f"falling back to +{DEFAULT_BOOST}"
        )
    try:
        cfg = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    except Exception as e:
        return DEFAULT_BOOST, (
            f"{config_path}: YAML parse failed ({e!r}); falling back to +{DEFAULT_BOOST}"
        )
    if not isinstance(cfg, dict):
        return DEFAULT_BOOST, (
            f"{config_path}: top-level is {type(cfg).__name__}, not a mapping; "
            f"falling back to +{DEFAULT_BOOST}"
        )
    if "canon_boost" not in cfg:
        return DEFAULT_BOOST, (
            f"{config_path}: key 'canon_boost' not present; falling back to +{DEFAULT_BOOST}"
        )
    value = cfg["canon_boost"]
    if isinstance(value, bool) or not isinstance(value, int):
        return DEFAULT_BOOST, (
            f"{config_path}: 'canon_boost' is {type(value).__name__} ({value!r}), "
            f"not a plain int; falling back to +{DEFAULT_BOOST}"
        )
    return value, None


# Test cases for the with-PyYAML branch: (label, file_content, expected_boost, expect_warning)
_YAML_CASES = [
    ("3. YAML parse failure",      "canon_boost: [unclosed\n",          DEFAULT_BOOST, True),
    ("4. top-level not a mapping", "- canon_boost: 5\n",                DEFAULT_BOOST, True),
    ("5. missing canon_boost",     "other_key: 7\n",                    DEFAULT_BOOST, True),
    ("6a. value is a string",      "canon_boost: \"not-a-number\"\n",   DEFAULT_BOOST, True),
    ("6b. value is a float",       "canon_boost: 1.5\n",                DEFAULT_BOOST, True),
    ("6c. value is a bool",        "canon_boost: true\n",               DEFAULT_BOOST, True),
    ("7a. clean positive int",     "canon_boost: 3\n",                  3,             False),
    ("7b. clean zero",             "canon_boost: 0\n",                  0,             False),
    ("7c. negative int allowed",   "canon_boost: -2\n",                 -2,            False),
]


def _selftest() -> int:
    """Exercise every case the contract names; return 0 if all pass, 1 otherwise."""
    import tempfile

    failures: list[str] = []

    def run(label: str, setup_fn, expected_boost: int, expect_warning: bool) -> None:
        with tempfile.TemporaryDirectory() as td:
            kb = Path(td)
            setup_fn(kb)
            boost, warning = load_canon_boost(kb)
            problems = []
            if boost != expected_boost:
                problems.append(f"boost={boost}, expected {expected_boost}")
            if expect_warning and warning is None:
                problems.append("expected warning, got none")
            if not expect_warning and warning is not None:
                problems.append(f"unexpected warning: {warning}")
            if problems:
                failures.append(f"FAIL {label}: {'; '.join(problems)}")
                print(f"  FAIL: {label} — {'; '.join(problems)}", file=sys.stderr)
            else:
                print(f"  PASS: {label}", file=sys.stderr)

    print("selftest: load_config.py", file=sys.stderr)

    # Case 1: always testable
    run("1. file absent", lambda kb: None, DEFAULT_BOOST, False)

    yaml_present = _try_import_yaml() is not None
    if not yaml_present:
        # Case 2 is only testable when PyYAML is genuinely absent
        run("2. PyYAML missing (env)",
            lambda kb: (kb / ".consult.yaml").write_text("canon_boost: 5\n"),
            DEFAULT_BOOST, True)
        print("  SKIP: cases 3-7 (require PyYAML)", file=sys.stderr)
    else:
        print("  SKIP: case 2 (PyYAML installed; cannot deterministically test the missing-PyYAML path)",
              file=sys.stderr)
        for label, content, expected, expect_warn in _YAML_CASES:
            run(label, lambda kb, c=content: (kb / ".consult.yaml").write_text(c), expected, expect_warn)

    if failures:
        print(f"\nselftest: {len(failures)} failure(s)", file=sys.stderr)
        return 1
    print("\nselftest: all cases passed", file=sys.stderr)
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--kb-root", type=Path, help="Path to the KB root directory")
    ap.add_argument("--selftest", action="store_true", help="Run the self-test suite and exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return _selftest()
    if args.kb_root is None:
        ap.error("--kb-root is required (or use --selftest)")
    boost, warning = load_canon_boost(args.kb_root.expanduser().resolve())
    print(boost)
    if warning:
        print(f"warning: {warning}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
