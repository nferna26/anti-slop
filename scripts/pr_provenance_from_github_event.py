#!/usr/bin/env python3
"""Run anti-slop-pr on the PR body from a GitHub Actions event payload.

Reads a pull_request event JSON (from ``--event`` or ``$GITHUB_EVENT_PATH``),
extracts the PR description, and runs the deterministic provenance checker
(``gate_pr_provenance``) against the local checkout (``--root``). It checks
whether the references a PR description cites resolve — nothing stronger.

No GitHub API: the event payload + local files only. NON-PR events SKIP (exit 0),
so the same workflow step is harmless on push / schedule / comment triggers.

Exit: 0 if every hard reference resolves (or SKIP, or ``--report``); 1 if a hard
reference is unresolved. Supports ``--root``, ``--issue-registry``,
``--require-reviewed-cards``, ``--report``, ``--json``.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gate_pr_provenance as pr  # noqa: E402

PR_EVENTS = ("pull_request", "pull_request_target")


def extract_pr(event_path: str | None, event_name: str | None) -> tuple[dict | None, str]:
    """Return (pull_request_dict, reason). pull_request_dict is None when this is
    not a PR event (reason explains the SKIP)."""
    if not event_path:
        return None, "no event payload (--event or $GITHUB_EVENT_PATH); not a PR context"
    if event_name and event_name not in PR_EVENTS:
        return None, f"event '{event_name}' is not a pull_request event"
    try:
        event = json.loads(Path(event_path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return None, f"could not read event JSON ({type(exc).__name__})"
    pr_obj = event.get("pull_request") if isinstance(event, dict) else None
    if not isinstance(pr_obj, dict) or "body" not in pr_obj:
        return None, "event payload has no pull_request.body; not a PR event"
    return pr_obj, ""


def check_event(event_path, event_name, root, registry, require_reviewed_cards) -> dict | None:
    """Return the gate receipt, or None for SKIP."""
    pr_obj, reason = extract_pr(event_path, event_name)
    if pr_obj is None:
        print(f"SKIP: {reason}.")
        return None
    body = pr_obj.get("body")
    body = body if isinstance(body, str) else ""  # null / non-string -> empty (no crash)
    number = pr_obj.get("number")
    print(f"anti-slop-pr: checking PR #{number} description "
          f"({len(body)} chars) against root {root}")
    with tempfile.TemporaryDirectory() as tmp:
        bf = Path(tmp) / "pr-body.md"
        bf.write_text(body, encoding="utf-8")
        receipt = pr.run(bf, Path(root), registry, require_reviewed_cards)
    receipt["pr_file"] = f"PR #{number} body"
    return receipt


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--event", help="event JSON path (default: $GITHUB_EVENT_PATH)")
    p.add_argument("--event-name", help="event name (default: $GITHUB_EVENT_NAME)")
    p.add_argument("--root", default=".", help="repo checkout root (default: cwd)")
    p.add_argument("--issue-registry", type=Path,
                   help="file of valid issue numbers; without it issue refs are advisory")
    p.add_argument("--require-reviewed-cards", action="store_true")
    p.add_argument("--report", action="store_true",
                   help="advisory mode: print findings but always exit 0")
    p.add_argument("--json", type=Path, help="write the JSON receipt to this path")
    p.add_argument("--self-test", action="store_true", help="run the deterministic self-test")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.self_test:
        return self_test()
    event_path = args.event or os.environ.get("GITHUB_EVENT_PATH")
    # An explicit --event is trusted on its own: only fall back to the ambient
    # $GITHUB_EVENT_NAME when no --event was given (so handing a PR event file
    # directly is not skipped by an unrelated ambient event name like 'push').
    event_name = args.event_name or (None if args.event else os.environ.get("GITHUB_EVENT_NAME"))
    registry = pr.load_issue_registry(args.issue_registry)
    receipt = check_event(event_path, event_name, args.root, registry,
                          args.require_reviewed_cards)
    if receipt is None:
        return 0  # SKIP
    print(pr.render(receipt))
    if args.json:
        args.json.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
        print(f"Receipt: {args.json}")
    if args.report:
        print("(--report: advisory mode, exit 0 regardless of unresolved refs)")
        return 0
    return 0 if receipt["passed"] else 1


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def self_test() -> int:
    # Hermetic: clear ambient GitHub env so the no-event SKIP check does not read
    # a real event when the self-test itself runs inside GitHub Actions.
    saved = {k: os.environ.pop(k, None) for k in ("GITHUB_EVENT_PATH", "GITHUB_EVENT_NAME")}
    try:
        return _self_test_body()
    finally:
        for k, v in saved.items():
            if v is not None:
                os.environ[k] = v


def _self_test_body() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "repo"
        _write(root / "docs" / "example.md", "# Example\n\nHi.\n")
        _write(root / "corpus" / "source-cards" / "BK-7001-card-001.md",
               "---\ncard_id: BK-7001-card-001\nsource_id: BK-7001\n"
               "operator_review_status: reviewed\n---\n\n# Card\n\nClaim.\n")
        _write(root / "corpus" / "manifests" / "books-200.yaml", "  - source_id: BK-7001\n")
        reg = pr.load_issue_registry(None)  # issues advisory in the self-test

        counter = [0]

        def event(body) -> str:
            counter[0] += 1  # deterministic unique name (no hash-bucket collision)
            ev = Path(tmp) / f"ev{counter[0]}.json"
            ev.write_text(json.dumps({"pull_request": {"number": 1, "body": body}}),
                          encoding="utf-8")
            return str(ev)

        clean = event("Adds `docs/example.md`, supported by `BK-7001-card-001`.")
        fab = event("Adds `docs/ghost.md` per `BK-9999-card-001`.")
        ign = event("<!-- anti-slop-pr: ignore-start -->\n"
                    "Example: `docs/ghost.md`.\n<!-- anti-slop-pr: ignore-end -->\n"
                    "Real: `docs/example.md`.")
        nonstr = event(12345)  # non-string body must be handled (no crash) -> PASS
        non_pr = Path(tmp) / "push.json"
        non_pr.write_text(json.dumps({"ref": "refs/heads/main", "commits": []}), encoding="utf-8")

        r = str(root)
        checks = [
            ("clean PR event -> PASS (exit 0)",
             main(["--event", clean, "--event-name", "pull_request", "--root", r]) == 0),
            ("fabricated PR event -> FAIL (exit 1)",
             main(["--event", fab, "--event-name", "pull_request", "--root", r]) == 1),
            ("fabricated PR event + --report -> exit 0",
             main(["--event", fab, "--event-name", "pull_request", "--root", r, "--report"]) == 0),
            ("non-PR event (by name) -> SKIP exit 0",
             main(["--event", clean, "--event-name", "push", "--root", r]) == 0),
            ("non-PR event (no pull_request in payload) -> SKIP exit 0",
             main(["--event", str(non_pr), "--root", r]) == 0),
            ("no event path -> SKIP exit 0", main(["--root", r]) == 0),
            ("ignore-directive PR event -> PASS with ignored-lines audit",
             main(["--event", ign, "--event-name", "pull_request", "--root", r]) == 0
             and check_event(ign, "pull_request", r, reg, False)["ignores"]["ignored_lines"] >= 1),
            ("non-string PR body -> handled, no crash, PASS exit 0",
             main(["--event", nonstr, "--event-name", "pull_request", "--root", r]) == 0),
        ]
    failed = [name for name, ok in checks if not ok]
    if failed:
        print("pr-provenance-event self-test FAILED:")
        for name in failed:
            print(f"  - {name}")
        return 1
    print("pr-provenance-event self-test passed (8 checks: clean PASS, fabricated FAIL, "
          "--report non-fail, non-PR skip by name, non-PR skip by payload, no-event skip, "
          "ignore-directive PASS with audit, non-string-body handled).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
