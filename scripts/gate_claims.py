#!/usr/bin/env python3
"""anti-slop-claims: generic artifact reference/receipt resolver.

This is the generic entrypoint for Anti-Slop agent claim verification. It checks
whether references cited by a Markdown/text artifact resolve against a repo or
fixture root. It intentionally reuses the existing anti-slop-pr resolver engine
(`gate_pr_provenance.run`) rather than forking file/test/issue/card/commit
resolution.

Scope is narrow: reference/receipt resolution only. A passing check means cited
hard references resolved. It does NOT prove correctness, relevance, support,
source truth, advice quality, reasoning, safety, or canon.

`anti-slop-pr` remains the PR-body surface/preset with its existing CLI behavior,
output, exit codes, event wrapper, demos, ignore directives, issue-registry
behavior, and advisory commit behavior. This command is the generic artifact
shape for non-PR surfaces such as `AGENT_FINAL_REPORT.md`.
"""

from __future__ import annotations

from pathlib import Path
import argparse
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gate_pr_provenance as pr  # noqa: E402


def render(receipt: dict) -> str:
    """Reuse the PR resolver report shape with generic artifact labels."""
    return (pr.render(receipt)
            .replace("== anti-slop-pr provenance check ==",
                     "== anti-slop-claims artifact check ==", 1)
            .replace("PR file:", "Artifact file:", 1))


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def self_test() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        _write(root / "docs" / "agent-final-report.md",
               "# Agent Final Report Fixture\n\nThis referenced file exists.\n")
        valid = root / "valid" / "AGENT_FINAL_REPORT.md"
        fabricated = root / "fabricated" / "AGENT_FINAL_REPORT.md"
        _write(valid, "# Agent Final Report\n\nUpdated `docs/agent-final-report.md`.\n")
        _write(fabricated, "# Agent Final Report\n\nUpdated `docs/missing-final-report.md`.\n")

        ok = pr.run(valid, root, registry=None, require_reviewed_cards=False)
        bad = pr.run(fabricated, root, registry=None, require_reviewed_cards=False)

        checks = [
            ("generic final report valid file ref passes", ok["passed"] is True),
            ("generic final report checks one file ref",
             ok["checks"]["file"]["refs_checked"] == 1),
            ("generic final report fabricated file ref fails", bad["passed"] is False),
            ("fabricated failure is line-level",
             any("line 3: file does not resolve: docs/missing-final-report.md" in u
                 for u in bad["checks"]["file"]["unresolved"])),
        ]
        failed = [name for name, passed in checks if not passed]
        if failed:
            print("anti-slop-claims self-test FAILED:")
            for name in failed:
                print(f"  - {name}")
            print(render(bad))
            return 1
    print("anti-slop-claims self-test passed (generic AGENT_FINAL_REPORT.md: "
          "valid path-like file ref PASSes; fabricated path-like file ref FAILs "
          "with a line-level reason).")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artifact_file", nargs="?", type=Path,
                        help="generic Markdown/text artifact to check")
    parser.add_argument("--root", type=Path, default=Path.cwd(),
                        help="repo or fixture root to resolve references against (default: cwd)")
    parser.add_argument("--issue-registry", type=Path,
                        help="file of valid issue numbers; without it, issue refs are advisory")
    parser.add_argument("--require-reviewed-cards", action="store_true",
                        help="require every cited source-card to resolve to a reviewed card")
    parser.add_argument("--report", action="store_true",
                        help="advisory mode: print findings but always exit 0")
    parser.add_argument("--self-test", action="store_true",
                        help="run the deterministic generic-artifact self-test")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.self_test:
        return self_test()
    if not args.artifact_file:
        print("Usage: anti-slop-claims [--root DIR] [--issue-registry F] "
              "[--require-reviewed-cards] [--report] <artifact.md>")
        return 2
    if not args.artifact_file.exists():
        print(f"Missing input: {args.artifact_file}")
        return 2

    registry = pr.load_issue_registry(args.issue_registry)
    receipt = pr.run(args.artifact_file.resolve(), args.root, registry,
                     args.require_reviewed_cards)
    print(render(receipt))
    if args.report:
        print("(--report: advisory mode, exit 0 regardless of unresolved refs)")
        return 0
    return 0 if receipt["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
