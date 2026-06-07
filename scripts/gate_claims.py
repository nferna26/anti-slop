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
import json
import re
import subprocess
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gate_pr_provenance as pr  # noqa: E402

CHANGED_WORD_RE = re.compile(
    r"\b(add|adds|added|update|updates|updated|change|changes|changed|"
    r"modify|modifies|modified|touch|touches|touched)\b",
    re.IGNORECASE,
)


def _line_text(text: str, line: int) -> str:
    lines = text.splitlines()
    if 1 <= line <= len(lines):
        return lines[line - 1].strip()
    return ""


def _entry(ref: pr.Ref, ref_type: str, tier: str, status: str, reason: str,
           evidence: dict, text: str) -> dict:
    return {
        "line": ref.line,
        "text": _line_text(text, ref.line),
        "ref": ref.value,
        "type": ref_type,
        "tier": tier,
        "status": status,
        "reason": reason,
        "resolver_evidence": evidence,
    }


def _prepared_text(path: Path) -> tuple[str, dict]:
    deignored, ignore_info = pr.apply_ignores(pr.read_text(path))
    return pr.strip_html_comments(deignored), ignore_info


def _file_evidence(ref: pr.Ref, root: Path) -> tuple[str, str, dict]:
    result = pr.check_files([ref], root)
    target = root / ref.value
    evidence = {
        "resolver": "gate_pr_provenance.check_files",
        "path": ref.value,
        "absolute_path": str(target.resolve()),
        "exists": target.is_file(),
    }
    if target.is_file():
        line_count = len(pr.read_text(target).splitlines())
        evidence["line_count"] = line_count
        if ref.detail:
            evidence["required_line"] = int(ref.detail)
    if result.unresolved:
        return "fail", result.unresolved[0], evidence
    return "pass", "file reference resolves", evidence


def _test_evidence(ref: pr.Ref, root: Path) -> tuple[str, str, dict]:
    result = pr.check_tests([ref], root)
    file_part, _, node = ref.value.partition("::")
    target = root / file_part
    evidence = {
        "resolver": "gate_pr_provenance.check_tests",
        "path": file_part,
        "node": node,
        "exists": target.is_file(),
    }
    if result.unresolved:
        return "fail", result.unresolved[0], evidence
    return "pass", "test reference resolves", evidence


def _issue_evidence(ref: pr.Ref, registry: set[str] | None) -> tuple[str, str, str, dict]:
    result = pr.check_issues([ref], registry)
    evidence = {
        "resolver": "gate_pr_provenance.check_issues",
        "registry_provided": registry is not None,
    }
    if result.unresolved:
        return "hard", "fail", result.unresolved[0], evidence
    if result.advisory:
        return "advisory", "advisory", result.advisory[0], evidence
    return "hard", "pass", "issue reference resolves in registry", evidence


def _commit_evidence(ref: pr.Ref, root: Path) -> tuple[str, str, dict]:
    result = pr.check_commits([ref], root)
    evidence = {
        "resolver": "gate_pr_provenance.check_commits",
        "local_git_only": True,
    }
    if result.advisory:
        return "advisory", result.advisory[0], evidence
    return "pass", "commit reference resolves locally", evidence


def _lineage_entries(text: str, artifact_path: Path, root: Path,
                     require_reviewed_cards: bool) -> list[dict]:
    index = pr.lineage.build_index(root)
    own_card_id = pr.lineage.read_frontmatter(artifact_path).get("card_id")
    entries: list[dict] = []
    with tempfile.TemporaryDirectory() as tmp:
        temp = Path(tmp) / artifact_path.name
        temp.write_text(text, encoding="utf-8")
        refs = pr.lineage.line_refs(temp)
    for ref in refs:
        ok = True
        detail = ref.kind
        evidence = {
            "resolver": "gate_citation_lineage",
            "kind": ref.kind,
            "require_reviewed_cards": require_reviewed_cards,
        }
        if ref.kind == "source_id":
            ok = ref.value in index.sources
            evidence["known_sources"] = ok
        elif ref.kind == "source_card":
            exists = ref.value in index.source_cards
            reviewed = ref.value in index.reviewed_source_cards
            evidence["source_card_exists"] = exists
            evidence["reviewed_source_card"] = reviewed
            if not exists:
                ok = False
            elif require_reviewed_cards and ref.value != own_card_id and not reviewed:
                ok = False
                detail = "unreviewed source_card (cited as reviewed lineage)"
        elif ref.kind == "card_id":
            ok = ref.value in index.all_card_ids or index.resolves_idish(ref.value)
            evidence["known_card_or_eval_label"] = ok
        elif ref.kind == "card_path":
            ok = pr.lineage.resolve_card_path(index, ref.value)
            evidence["card_path_exists"] = ok
        reason = "lineage reference resolves" if ok else f"unresolved {detail} reference: {ref.value}"
        entries.append({
            "line": ref.line,
            "text": _line_text(text, ref.line),
            "ref": ref.value,
            "type": ref.kind,
            "tier": "hard",
            "status": "pass" if ok else "fail",
            "reason": reason,
            "resolver_evidence": evidence,
        })
    return entries


def _changed_file_refs(text: str) -> set[tuple[int, str]]:
    changed: set[tuple[int, str]] = set()
    files, _, _, _ = pr.detect_refs(text)
    for ref in files:
        line = _line_text(text, ref.line)
        if CHANGED_WORD_RE.search(line):
            changed.add((ref.line, ref.value))
    return changed


def _git_changed_paths(root: Path, diff_range: str) -> tuple[set[str] | None, str]:
    try:
        proc = subprocess.run(
            ["git", "-C", str(root), "diff", "--name-only", diff_range],
            capture_output=True,
            text=True,
        )
    except OSError as exc:
        return None, f"git unavailable: {exc}"
    if proc.returncode != 0:
        reason = (proc.stderr or proc.stdout).strip() or "git diff failed"
        return None, reason
    return {line.strip() for line in proc.stdout.splitlines() if line.strip()}, ""


def _changed_file_entries(text: str, root: Path, diff_range: str | None) -> tuple[list[dict], dict]:
    changed_refs = _changed_file_refs(text)
    if diff_range:
        changed_paths, reason = _git_changed_paths(root, diff_range)
        diff_info = {
            "range": diff_range,
            "mode": "checked" if changed_paths is not None else "unavailable",
            "changed_paths": sorted(changed_paths or []),
            "reason": reason,
        }
    else:
        changed_paths = None
        diff_info = {
            "range": None,
            "mode": "not_supplied",
            "changed_paths": [],
            "reason": "no --diff supplied; changed-file claims are advisory/skipped",
        }

    entries: list[dict] = []
    for line, path in sorted(changed_refs):
        ref = pr.Ref("changed_file", path, line)
        if diff_range and changed_paths is not None:
            status = "pass" if path in changed_paths else "fail"
            reason = ("changed-file claim matches supplied diff"
                      if status == "pass"
                      else f"changed-file claim not found in supplied diff: {path}")
            tier = "hard"
        else:
            status = "advisory"
            tier = "advisory"
            reason = diff_info["reason"]
        entries.append(_entry(ref, "changed_file", tier, status, reason, {
            "resolver": "git diff --name-only",
            "diff_range": diff_range,
            "diff_mode": diff_info["mode"],
            "changed_paths": diff_info["changed_paths"],
        }, text))
    return entries, diff_info


def structured_receipt(artifact_path: Path, root: Path, registry: set[str] | None,
                       require_reviewed_cards: bool, diff_range: str | None = None) -> dict:
    text, ignore_info = _prepared_text(artifact_path)
    files, tests, issues, commits = pr.detect_refs(text)
    entries: list[dict] = []
    for ref in files:
        status, reason, evidence = _file_evidence(ref, root)
        entries.append(_entry(ref, "file", "hard", status, reason, evidence, text))
    for ref in tests:
        status, reason, evidence = _test_evidence(ref, root)
        entries.append(_entry(ref, "test", "hard", status, reason, evidence, text))
    for ref in issues:
        tier, status, reason, evidence = _issue_evidence(ref, registry)
        entries.append(_entry(ref, "issue", tier, status, reason, evidence, text))
    entries.extend(_lineage_entries(text, artifact_path, root, require_reviewed_cards))
    for ref in commits:
        status, reason, evidence = _commit_evidence(ref, root)
        entries.append(_entry(ref, "commit", "advisory", status, reason, evidence, text))
    changed_entries, diff_info = _changed_file_entries(text, root, diff_range)
    entries.extend(changed_entries)

    entries.sort(key=lambda e: (e["line"], e["type"], e["ref"]))
    hard_fail = any(e["tier"] == "hard" and e["status"] == "fail" for e in entries)
    legacy = pr.run(artifact_path, root, registry, require_reviewed_cards)
    # Preserve existing reference semantics and add only the changed-file hard
    # failures on top.
    passed = legacy["passed"] and not hard_fail
    return {
        "schema_version": "anti-slop-claims.v1",
        "artifact_path": str(artifact_path.resolve()),
        "artifact_file": artifact_path.name,
        "pr_file": artifact_path.name,
        "root": str(root.resolve()),
        "passed": passed,
        "issue_registry": registry is not None,
        "require_reviewed_cards": require_reviewed_cards,
        "diff": diff_info,
        "ignores": ignore_info,
        "claims": entries,
        "checks": legacy["checks"],
    }


def render(receipt: dict) -> str:
    """Reuse the PR resolver report shape with generic artifact labels."""
    base = (pr.render(receipt)
            .replace("== anti-slop-pr provenance check ==",
                     "== anti-slop-claims artifact check ==", 1)
            .replace("PR file:", "Artifact file:", 1))
    changed = [c for c in receipt.get("claims", []) if c.get("type") == "changed_file"]
    if not changed:
        return base
    lines = [base, "- changed_file: "
             f"{len(changed)} checked, "
             f"{sum(1 for c in changed if c['status'] == 'fail')} failed, "
             f"{sum(1 for c in changed if c['status'] == 'advisory')} advisory"]
    for claim in changed:
        prefix = "FAIL" if claim["status"] == "fail" else claim["status"]
        lines.append(f"    {prefix} line {claim['line']}: {claim['reason']}")
    return "\n".join(lines)


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
        mixed = root / "mixed" / "AGENT_FINAL_REPORT.md"
        json_out = root / "claims-receipt.json"
        _write(valid, "# Agent Final Report\n\nUpdated `docs/agent-final-report.md`.\n")
        _write(fabricated, "# Agent Final Report\n\nUpdated `docs/missing-final-report.md`.\n")
        _write(mixed, "# Agent Final Report\n\nUpdated `docs/agent-final-report.md`.\n"
                      "Also cites `docs/missing-final-report.md` and #123.\n")

        ok = pr.run(valid, root, registry=None, require_reviewed_cards=False)
        bad = pr.run(fabricated, root, registry=None, require_reviewed_cards=False)
        json_exit = main(["--root", str(root), "--json", str(json_out), str(mixed)])
        json_data = json.loads(json_out.read_text(encoding="utf-8")) if json_out.exists() else {}

        diff_root = root / "diff-root"
        _write(diff_root / "docs" / "changed.md", "# Changed\n\nbefore\n")
        _write(diff_root / "docs" / "unchanged.md", "# Unchanged\n\nstable\n")
        subprocess.run(["git", "-C", str(diff_root), "init"], capture_output=True, check=True)
        subprocess.run(["git", "-C", str(diff_root), "config", "user.email", "test@example.invalid"],
                       capture_output=True, check=True)
        subprocess.run(["git", "-C", str(diff_root), "config", "user.name", "Anti Slop Test"],
                       capture_output=True, check=True)
        subprocess.run(["git", "-C", str(diff_root), "add", "."], capture_output=True, check=True)
        subprocess.run(["git", "-C", str(diff_root), "commit", "-m", "base"],
                       capture_output=True, check=True)
        _write(diff_root / "docs" / "changed.md", "# Changed\n\nafter\n")
        changed_report = root / "diff" / "changed.md"
        not_changed_report = root / "diff" / "not_changed.md"
        no_diff_report = root / "diff" / "no_diff.md"
        ordinary_report = root / "diff" / "ordinary.md"
        diff_json = root / "diff.json"
        not_changed_json = root / "not-changed.json"
        no_diff_json = root / "no-diff.json"
        _write(changed_report, "# Agent Final Report\n\nUpdated `docs/changed.md`.\n")
        _write(not_changed_report, "# Agent Final Report\n\nUpdated `docs/unchanged.md`.\n")
        _write(no_diff_report, "# Agent Final Report\n\nUpdated `docs/changed.md`.\n")
        _write(ordinary_report, "# Agent Final Report\n\nReferences `docs/unchanged.md`.\n")
        changed_exit = main(["--root", str(diff_root), "--diff", "HEAD", "--json",
                             str(diff_json), str(changed_report)])
        not_changed_exit = main(["--root", str(diff_root), "--diff", "HEAD", "--json",
                                 str(not_changed_json), str(not_changed_report)])
        no_diff_exit = main(["--root", str(diff_root), "--json", str(no_diff_json),
                             str(no_diff_report)])
        ordinary_exit = main(["--root", str(diff_root), "--diff", "HEAD", str(ordinary_report)])
        diff_data = json.loads(diff_json.read_text(encoding="utf-8")) if diff_json.exists() else {}
        not_changed_data = (json.loads(not_changed_json.read_text(encoding="utf-8"))
                            if not_changed_json.exists() else {})
        no_diff_data = json.loads(no_diff_json.read_text(encoding="utf-8")) if no_diff_json.exists() else {}

        checks = [
            ("generic final report valid file ref passes", ok["passed"] is True),
            ("generic final report checks one file ref",
             ok["checks"]["file"]["refs_checked"] == 1),
            ("generic final report fabricated file ref fails", bad["passed"] is False),
            ("fabricated failure is line-level",
             any("line 3: file does not resolve: docs/missing-final-report.md" in u
                 for u in bad["checks"]["file"]["unresolved"])),
            ("generic JSON receipt writes even on hard failure", json_exit == 1 and json_out.is_file()),
            ("JSON receipt has required top-level fields",
             {"artifact_path", "root", "passed", "claims"}.issubset(json_data)),
            ("JSON receipt records a hard pass",
             any(c.get("type") == "file" and c.get("ref") == "docs/agent-final-report.md"
                 and c.get("tier") == "hard" and c.get("status") == "pass"
                 for c in json_data.get("claims", []))),
            ("JSON receipt records a hard fail",
             any(c.get("type") == "file" and c.get("ref") == "docs/missing-final-report.md"
                 and c.get("tier") == "hard" and c.get("status") == "fail"
                 and c.get("line") == 4
                 for c in json_data.get("claims", []))),
            ("JSON receipt records an advisory issue without registry",
             any(c.get("type") == "issue" and c.get("ref") == "123"
                 and c.get("tier") == "advisory" and c.get("status") == "advisory"
                 for c in json_data.get("claims", []))),
            ("diff mode changed file passes",
             changed_exit == 0 and any(c.get("type") == "changed_file"
                                       and c.get("ref") == "docs/changed.md"
                                       and c.get("status") == "pass"
                                       for c in diff_data.get("claims", []))),
            ("diff mode existing but not changed fails hard",
             not_changed_exit == 1 and any(c.get("type") == "changed_file"
                                           and c.get("ref") == "docs/unchanged.md"
                                           and c.get("tier") == "hard"
                                           and c.get("status") == "fail"
                                           for c in not_changed_data.get("claims", []))),
            ("missing diff leaves changed-file claim advisory",
             no_diff_exit == 0 and any(c.get("type") == "changed_file"
                                       and c.get("ref") == "docs/changed.md"
                                       and c.get("tier") == "advisory"
                                       and c.get("status") == "advisory"
                                       for c in no_diff_data.get("claims", []))),
            ("ordinary file resolution still works in diff mode",
             ordinary_exit == 0),
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
          "with a line-level reason; JSON records hard pass/fail/advisory; "
          "diff mode checks changed-file claims).")
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
    parser.add_argument("--json", type=Path,
                        help="write structured anti-slop-claims JSON receipt")
    parser.add_argument("--diff", dest="diff_range",
                        help="local git diff/range for changed-file claim checks")
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
    receipt = structured_receipt(args.artifact_file.resolve(), args.root, registry,
                                 args.require_reviewed_cards, args.diff_range)
    print(render(receipt))
    if args.json:
        args.json.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
        print(f"Receipt: {args.json}")
    if args.report:
        print("(--report: advisory mode, exit 0 regardless of unresolved refs)")
        return 0
    return 0 if receipt["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
