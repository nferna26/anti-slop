#!/usr/bin/env python3
"""Demo of the GitHub-event wrapper (`pr_provenance_from_github_event`).

Runs the wrapper over committed fixture event payloads, resolving their PR bodies
against the self-contained demo fixture root — so it is deterministic and needs
no GitHub API, network, or model. Asserts the five adoption behaviours:

  clean PR event        -> PASS (exit 0)
  fabricated PR event   -> FAIL (exit 1)
  fabricated + --report -> exit 0 (advisory)
  non-PR event          -> SKIP (exit 0)
  ignore-directive PR   -> PASS, with ignored-lines audit

It also runs the wrapper on a saved REAL PR body (shaped as an event) in --report
mode against the repo root — informational only (exit 0; live-tree snapshot).
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEMO = ROOT / "proof" / "pr-provenance-demo"
EVENTS = DEMO / "events"
FIXTURE_ROOT = DEMO / "fixture-root"
REGISTRY = FIXTURE_ROOT / "issue-registry.txt"

sys.path.insert(0, str(ROOT / "scripts"))
import pr_provenance_from_github_event as wrap  # noqa: E402


def run(event: str, *extra: str) -> int:
    argv = ["--event", str(EVENTS / event), "--root", str(FIXTURE_ROOT),
            "--issue-registry", str(REGISTRY), *extra]
    return wrap.main(argv)


def main() -> int:
    print("== anti-slop-pr GitHub-event wrapper demo ==")
    print(f"Events: {EVENTS.relative_to(ROOT)}; fixture root: {FIXTURE_ROOT.relative_to(ROOT)}\n")

    clean = run("clean-pr-event.json", "--event-name", "pull_request")
    fab = run("fabricated-pr-event.json", "--event-name", "pull_request")
    fab_report = run("fabricated-pr-event.json", "--event-name", "pull_request", "--report")
    non_pr = run("non-pr-event.json", "--event-name", "push")
    # ignore audit: run the gate ONCE via check_event, then render + derive rc.
    ign_receipt = wrap.check_event(str(EVENTS / "ignored-pr-event.json"), "pull_request",
                                   str(FIXTURE_ROOT), wrap.pr.load_issue_registry(REGISTRY), False)
    print(wrap.pr.render(ign_receipt))
    ign_rc = 0 if ign_receipt["passed"] else 1
    ign_lines = ign_receipt["ignores"]["ignored_lines"]

    print("\n-- results --")
    print(f"clean PR event           -> exit {clean} (expect 0)")
    print(f"fabricated PR event      -> exit {fab} (expect 1)")
    print(f"fabricated + --report    -> exit {fab_report} (expect 0)")
    print(f"non-PR event             -> exit {non_pr} (expect 0, SKIP)")
    print(f"ignore-directive PR      -> exit {ign_rc} (expect 0), ignored_lines={ign_lines} (expect >=1)")

    print("\n-- informational: real saved PR body via event, --report against repo root --")
    real = wrap.main(["--event", str(EVENTS / "real-pr-26-event.json"), "--event-name",
                      "pull_request", "--root", str(ROOT), "--report"])
    print(f"real PR body (report)    -> exit {real} (expect 0; live-tree, informational)")

    ok = (clean == 0 and fab == 1 and fab_report == 0 and non_pr == 0
          and ign_rc == 0 and ign_lines >= 1)
    if ok:
        print("\nEVENT WRAPPER DEMO PASSED.")
        return 0
    print("\nEVENT WRAPPER DEMO FAILED.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
