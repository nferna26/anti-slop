#!/usr/bin/env python3
"""Offline dogfood of anti-slop-pr over this repo's own PR descriptions.

Runs gate_pr_provenance over a set of committed, public-safe PR-body copies
(`proof/pr-provenance-dogfood/bodies/*.txt`, originally read from this repo's
public PR metadata via `gh`) and resolves their references against the repo
root. It prints an aggregate REPORT and always exits 0 — it is dogfood evidence,
not a gate.

Fully offline: no GitHub API, no model, no network (the bodies are already saved;
commit refs use only local git). Results are a SNAPSHOT against the current tree
— as the repo changes, more or fewer references resolve.

Run: `make pr-provenance-dogfood` or `python3 scripts/dogfood_pr_provenance.py`.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOGFOOD = ROOT / "proof" / "pr-provenance-dogfood"
BODIES = DOGFOOD / "bodies"
REGISTRY = DOGFOOD / "issue-registry.txt"

sys.path.insert(0, str(ROOT / "scripts"))
import gate_pr_provenance as pr  # noqa: E402


def main() -> int:
    registry = pr.load_issue_registry(REGISTRY)
    bodies = sorted(BODIES.glob("pr-*.txt"))
    print("== anti-slop-pr dogfood (snapshot report; always exit 0) ==")
    print(f"Bodies: {len(bodies)} from {BODIES.relative_to(ROOT)}; resolving against repo root.\n")
    totals = {k: 0 for k in ("file", "test", "issue", "card", "commit")}
    unresolved = {k: 0 for k in ("file", "test", "issue", "card")}
    commit_advisory = 0
    n_pass = 0
    print(f"{'body':>10} {'pass':>5} | file  test  issue  card  commit(adv)")
    for b in bodies:
        rec = pr.run(b, ROOT, registry, require_reviewed_cards=False)
        c = rec["checks"]
        if rec["passed"]:
            n_pass += 1
        for k in totals:
            totals[k] += c[k]["refs_checked"]
        for k in unresolved:
            unresolved[k] += len(c[k]["unresolved"])
        commit_advisory += len(c["commit"]["advisory"])
        print(f"{b.stem:>10} {str(rec['passed']):>5} | "
              f"{c['file']['refs_checked']:>2}/{len(c['file']['unresolved'])}   "
              f"{c['test']['refs_checked']}/{len(c['test']['unresolved'])}    "
              f"{c['issue']['refs_checked']}/{len(c['issue']['unresolved'])}    "
              f"{c['card']['refs_checked']:>2}/{len(c['card']['unresolved'])}    "
              f"{c['commit']['refs_checked']}({len(c['commit']['advisory'])})")
    print(f"\nrefs checked: {totals}")
    print(f"hard unresolved: {unresolved}")
    print(f"commit advisory (non-failing): {commit_advisory}")
    print(f"passed {n_pass}/{len(bodies)} bodies")
    print("\nNote: remaining unresolved refs are concentrated in META PRs that document "
          "the tool's own fabricated example IDs (e.g. BK-9999, #9999, docs/foo.md). "
          "See docs/pr-provenance-dogfood-memo.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
