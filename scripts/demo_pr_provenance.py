#!/usr/bin/env python3
"""Stranger-reproducible demo of anti-slop-pr (the PR-provenance checker).

Fully offline — no GitHub API, no model, no network, no credential. It runs
gate_pr_provenance over two committed sample PR bodies, resolving their
references against a self-contained fixture root:

  - pass-pr.md  -> every issue/file/test/card reference resolves -> PASS (exit 0)
  - fail-pr.md  -> fake issue, missing doc, bad test node, fabricated card,
                   and an out-of-range line ref           -> FAIL (exit 1)

Exit 0 only when the checker PASSES the good body and FAILS the slop body, so it
both shows the tool working and proves it catches fabricated references.
"""

from __future__ import annotations

import json
import pathlib
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEMO = ROOT / "proof" / "pr-provenance-demo"
FIXTURE_ROOT = DEMO / "fixture-root"
REGISTRY = FIXTURE_ROOT / "issue-registry.txt"

sys.path.insert(0, str(ROOT / "scripts"))
import gate_pr_provenance as pr  # noqa: E402


def check(body: pathlib.Path) -> dict:
    registry = pr.load_issue_registry(REGISTRY)
    return pr.run(body, FIXTURE_ROOT, registry, require_reviewed_cards=True)


def main() -> int:
    out_dir = pathlib.Path(tempfile.mkdtemp(prefix="pr-provenance-demo-"))
    print("== anti-slop-pr provenance demo ==")
    print(f"Fixture root: {FIXTURE_ROOT.relative_to(ROOT)}")
    print(f"Working dir (transient): {out_dir}")

    good = check(DEMO / "pass-pr.md")
    bad = check(DEMO / "fail-pr.md")
    (out_dir / "pass-receipt.json").write_text(json.dumps(good, indent=2), encoding="utf-8")
    (out_dir / "fail-receipt.json").write_text(json.dumps(bad, indent=2), encoding="utf-8")

    good_unresolved = sum(len(c["unresolved"]) for c in good["checks"].values())
    bad_unresolved = sum(len(c["unresolved"]) for c in bad["checks"].values())
    print(f"[1/2] pass-pr.md -> passed={good['passed']} (expect True), "
          f"unresolved={good_unresolved} (expect 0)")
    print(f"[2/2] fail-pr.md -> passed={bad['passed']} (expect False), "
          f"unresolved={bad_unresolved} (expect >=4: fake issue, missing file, "
          f"bad test node, fake card)")
    print(f"\nReceipts: {out_dir}")

    ok = good["passed"] is True and bad["passed"] is False and bad_unresolved >= 4
    if ok:
        print("PR-PROVENANCE DEMO PASSED: checker accepted all resolvable references "
              "and rejected the fabricated ones.")
        return 0
    print("PR-PROVENANCE DEMO FAILED: checker did not behave as expected.")
    print(json.dumps({"good": good, "bad": bad}, indent=2))
    return 1


if __name__ == "__main__":
    sys.exit(main())
