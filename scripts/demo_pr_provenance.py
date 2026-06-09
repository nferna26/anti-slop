#!/usr/bin/env python3
"""Stranger-reproducible demo of anti-slop-pr (the PR-provenance checker).

Fully offline — no GitHub API, no model, no network, no credential. It runs
gate_pr_provenance over four committed sample PR bodies, resolving their
references against a self-contained fixture root:

  - pass-pr.md          -> every reference resolves                  -> PASS
  - fail-pr.md          -> fake issue/file/test-node/card + bad line -> FAIL
  - meta-pr.md          -> documents fabricated example refs         -> FAIL
  - meta-pr-ignored.md  -> same, wrapped in ignore directives        -> PASS
                           (examples suppressed; the real ref still checked)

Exit 0 only when the checker PASSES the good body, FAILS the slop and meta
bodies, and PASSES the ignore-wrapped meta body — showing it catches fabricated
references and that the explicit ignore escape hatch works.
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
    meta = check(DEMO / "meta-pr.md")              # documents fabricated examples -> FAIL
    meta_ig = check(DEMO / "meta-pr-ignored.md")   # same, wrapped in ignore -> PASS
    for name, rec in (("pass", good), ("fail", bad), ("meta", meta), ("meta-ignored", meta_ig)):
        (out_dir / f"{name}-receipt.json").write_text(json.dumps(rec, indent=2), encoding="utf-8")

    good_unresolved = sum(len(c["unresolved"]) for c in good["checks"].values())
    bad_unresolved = sum(len(c["unresolved"]) for c in bad["checks"].values())
    print(f"[1/4] pass-pr.md         -> passed={good['passed']} (expect True), "
          f"unresolved={good_unresolved} (expect 0)")
    print(f"[2/4] fail-pr.md         -> passed={bad['passed']} (expect False), "
          f"unresolved={bad_unresolved} (expect >=4: fake issue, missing file, bad test node, fake card)")
    print(f"[3/4] meta-pr.md         -> passed={meta['passed']} (expect False — documents fabricated examples)")
    print(f"[4/4] meta-pr-ignored.md -> passed={meta_ig['passed']} (expect True — examples wrapped in "
          f"ignore; {meta_ig['ignores']['ignored_lines']} lines ignored), real ref still checked")
    print(f"\nReceipts: {out_dir}")

    ok = (good["passed"] is True and bad["passed"] is False and bad_unresolved >= 4
          and meta["passed"] is False
          and meta_ig["passed"] is True and meta_ig["ignores"]["ignored_lines"] >= 1)
    if ok:
        print("PR-PROVENANCE DEMO PASSED: accepted resolvable refs, rejected fabricated ones, "
              "and the explicit ignore directive cleanly suppressed documented examples.")
        return 0
    print("PR-PROVENANCE DEMO FAILED: checker did not behave as expected.")
    print(json.dumps({"good": good, "bad": bad, "meta": meta, "meta_ig": meta_ig}, indent=2))
    return 1


if __name__ == "__main__":
    sys.exit(main())
