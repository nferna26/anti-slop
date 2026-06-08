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

from decimal import Decimal, InvalidOperation
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
COMMAND_EXIT_RE = re.compile(r"\bcommand\s+`([^`]+)`\s+exited\s+(-?\d+)\b", re.IGNORECASE)
MAKE_PASSED_RE = re.compile(r"\bmake\s+([A-Za-z0-9_.:-]+)\s+pass(?:ed|es)?\b", re.IGNORECASE)
PYTEST_PASSED_RE = re.compile(r"\bpytest\b.*\bpass(?:ed|es)?\b", re.IGNORECASE)
TESTS_PASS_RE = re.compile(r"\btests?\s+pass(?:ed|es)?\b", re.IGNORECASE)
NUM_RE = r"-?\d+(?:\.\d+)?"
METRIC_SCALAR_RE = re.compile(
    rf"\b(score|accuracy|f1|precision|recall|auc|pass_rate)\s+(?:is|=)\s+({NUM_RE})\b",
    re.IGNORECASE,
)
METRIC_IMPROVED_RE = re.compile(
    rf"\b(?:metric|([A-Za-z_][\w.-]*))\s+improved\s+from\s+({NUM_RE})\s+to\s+({NUM_RE})\b",
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


def _git_head(root: Path) -> tuple[str | None, str]:
    try:
        proc = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
        )
    except OSError as exc:
        return None, f"git unavailable: {exc}"
    if proc.returncode != 0:
        return None, (proc.stderr or proc.stdout).strip() or "git rev-parse failed"
    return proc.stdout.strip() or None, ""


def _norm_command(command: str) -> str:
    return " ".join(command.strip().split())


def _load_receipts(receipts_dir: Path | None) -> dict:
    if receipts_dir is None:
        return {
            "path": None,
            "mode": "not_supplied",
            "reason": "no --receipts supplied",
            "receipts": [],
            "errors": [],
        }
    if not receipts_dir.is_dir():
        return {
            "path": str(receipts_dir),
            "mode": "missing",
            "reason": f"receipt directory does not exist: {receipts_dir}",
            "receipts": [],
            "errors": [],
        }
    receipts: list[dict] = []
    errors: list[str] = []
    for path in sorted(receipts_dir.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path}: {exc}")
            continue
        data["_receipt_path"] = str(path)
        receipts.append(data)
    return {
        "path": str(receipts_dir),
        "mode": "loaded",
        "reason": "",
        "receipts": receipts,
        "errors": errors,
    }


def _receipt_is_stale(receipt: dict, current_head: str | None) -> bool:
    return current_head is not None and receipt.get("git_head") != current_head


def _receipt_evidence(receipt: dict | None, current_head: str | None, current_head_reason: str,
                      extra: dict | None = None) -> dict:
    evidence = {
        "resolver": "anti-slop-command-receipt.v1",
        "current_git_head": current_head,
        "current_git_head_reason": current_head_reason,
    }
    if receipt:
        evidence.update({
            "receipt_path": receipt.get("_receipt_path"),
            "schema_version": receipt.get("schema_version"),
            "command_string": receipt.get("command_string"),
            "command_tags": receipt.get("command_tags", []),
            "exit_code": receipt.get("exit_code"),
            "git_head": receipt.get("git_head"),
            "stale": _receipt_is_stale(receipt, current_head),
        })
    if extra:
        evidence.update(extra)
    return evidence


def _command_claims(text: str) -> list[dict]:
    claims: list[dict] = []
    for number, line in enumerate(text.splitlines(), start=1):
        for match in COMMAND_EXIT_RE.finditer(line):
            claims.append({
                "line": number,
                "ref": _norm_command(match.group(1)),
                "match_kind": "exact",
                "expected_exit": int(match.group(2)),
            })
        for match in MAKE_PASSED_RE.finditer(line):
            target = match.group(1)
            claims.append({
                "line": number,
                "ref": f"make {target}",
                "match_kind": "make",
                "target": target,
                "expected_exit": 0,
            })
        if PYTEST_PASSED_RE.search(line):
            claims.append({
                "line": number,
                "ref": "pytest passed",
                "match_kind": "pytest",
                "expected_exit": 0,
            })
        if TESTS_PASS_RE.search(line):
            claims.append({
                "line": number,
                "ref": "tests pass",
                "match_kind": "tests",
                "expected_exit": 0,
            })
    return claims


def _command_receipts(receipts_info: dict) -> list[dict]:
    return [
        r for r in receipts_info.get("receipts", [])
        if r.get("receipt_type") == "command"
        or r.get("schema_version") == "anti-slop-command-receipt.v1"
    ]


def _command_matches(claim: dict, receipt: dict) -> bool:
    command_string = _norm_command(str(receipt.get("command_string", "")))
    tags = set(receipt.get("command_tags") or [])
    kind = claim["match_kind"]
    if kind == "exact":
        return command_string == claim["ref"]
    if kind == "make":
        return command_string == claim["ref"] or f"make:{claim['target']}" in tags
    if kind == "pytest":
        return "pytest" in tags or command_string.startswith("pytest")
    if kind == "tests":
        return "tests" in tags
    return False


def _command_entries(text: str, root: Path, receipts_info: dict) -> list[dict]:
    claims = _command_claims(text)
    if not claims:
        return []
    current_head, current_head_reason = _git_head(root)
    receipts = _command_receipts(receipts_info)
    entries: list[dict] = []
    for claim in claims:
        matches = [r for r in receipts if _command_matches(claim, r)]
        fresh = [r for r in matches if not _receipt_is_stale(r, current_head)]
        expected = claim["expected_exit"]
        passing = [r for r in fresh if r.get("exit_code") == expected]
        evidence_extra = {
            "receipt_dir": receipts_info.get("path"),
            "receipt_mode": receipts_info.get("mode"),
            "receipt_errors": receipts_info.get("errors", []),
            "match_kind": claim["match_kind"],
            "expected_exit": expected,
            "matching_receipts": [r.get("_receipt_path") for r in matches],
        }
        if passing:
            status = "pass"
            prefix = "fresh " if current_head is not None else ""
            reason = f"{prefix}command receipt matches expected exit_code {expected}"
            evidence = _receipt_evidence(passing[0], current_head, current_head_reason, evidence_extra)
        elif not matches:
            status = "fail"
            reason = f"missing command receipt for claim: {claim['ref']}"
            evidence = _receipt_evidence(None, current_head, current_head_reason, evidence_extra)
        elif not fresh:
            status = "fail"
            reason = f"stale command receipt for claim: {claim['ref']}"
            evidence = _receipt_evidence(matches[0], current_head, current_head_reason, evidence_extra)
        else:
            status = "fail"
            actual = fresh[0].get("exit_code")
            reason = f"matching command receipt exit_code {actual}, expected {expected}"
            evidence = _receipt_evidence(fresh[0], current_head, current_head_reason, evidence_extra)
        ref = pr.Ref("command_receipt", claim["ref"], claim["line"])
        entries.append(_entry(ref, "command_receipt", "hard", status, reason, evidence, text))
    return entries


def _decimal(value: object) -> Decimal | None:
    try:
        return Decimal(str(value))
    except (InvalidOperation, ValueError):
        return None


def _metric_claims(text: str) -> list[dict]:
    claims: list[dict] = []
    for number, line in enumerate(text.splitlines(), start=1):
        for match in METRIC_SCALAR_RE.finditer(line):
            name = match.group(1).lower()
            value = match.group(2)
            claims.append({
                "line": number,
                "ref": f"{name}={value}",
                "match_kind": "scalar",
                "metric": name,
                "value": value,
            })
        for match in METRIC_IMPROVED_RE.finditer(line):
            metric = match.group(1).lower() if match.group(1) else None
            before = match.group(2)
            after = match.group(3)
            claims.append({
                "line": number,
                "ref": f"{metric or 'metric'}:{before}->{after}",
                "match_kind": "improvement",
                "metric": metric,
                "before": before,
                "after": after,
            })
    return claims


def _metrics(receipt: dict) -> dict:
    metrics = receipt.get("metrics")
    return metrics if isinstance(metrics, dict) else {}


def _metric_scalar_candidate(claim: dict, receipt: dict) -> bool:
    return claim["metric"] in _metrics(receipt)


def _metric_scalar_matches(claim: dict, receipt: dict) -> bool:
    value = _decimal(_metrics(receipt).get(claim["metric"]))
    return value is not None and value == Decimal(claim["value"])


def _metric_pairs(metrics: dict, metric: str | None) -> list[tuple[object, object]]:
    pairs: list[tuple[object, object]] = []
    names = [metric] if metric else sorted({k.rsplit(".", 1)[0] for k in metrics if "." in k})
    for name in names:
        if not name:
            continue
        for before_key, after_key in ((f"{name}.before", f"{name}.after"),
                                      (f"{name}.from", f"{name}.to")):
            if before_key in metrics and after_key in metrics:
                pairs.append((metrics[before_key], metrics[after_key]))
    return pairs


def _metric_improvement_candidate(claim: dict, receipt: dict) -> bool:
    return bool(_metric_pairs(_metrics(receipt), claim["metric"]))


def _metric_improvement_matches(claim: dict, receipt: dict) -> bool:
    before = Decimal(claim["before"])
    after = Decimal(claim["after"])
    for got_before, got_after in _metric_pairs(_metrics(receipt), claim["metric"]):
        got_before_dec = _decimal(got_before)
        got_after_dec = _decimal(got_after)
        if got_before_dec == before and got_after_dec == after:
            return True
    return False


def _metric_entries(text: str, root: Path, receipts_info: dict) -> list[dict]:
    claims = _metric_claims(text)
    if not claims:
        return []
    current_head, current_head_reason = _git_head(root)
    receipts = [r for r in _command_receipts(receipts_info) if _metrics(r)]
    entries: list[dict] = []
    for claim in claims:
        if claim["match_kind"] == "scalar":
            candidates = [r for r in receipts if _metric_scalar_candidate(claim, r)]
            matches = [r for r in candidates if _metric_scalar_matches(claim, r)]
        else:
            candidates = [r for r in receipts if _metric_improvement_candidate(claim, r)]
            matches = [r for r in candidates if _metric_improvement_matches(claim, r)]
        fresh_matches = [r for r in matches if not _receipt_is_stale(r, current_head)]
        evidence_extra = {
            "receipt_dir": receipts_info.get("path"),
            "receipt_mode": receipts_info.get("mode"),
            "receipt_errors": receipts_info.get("errors", []),
            "match_kind": claim["match_kind"],
            "metric": claim.get("metric"),
            "matching_receipts": [r.get("_receipt_path") for r in matches],
            "candidate_receipts": [r.get("_receipt_path") for r in candidates],
        }
        if fresh_matches:
            status = "pass"
            prefix = "fresh " if current_head is not None else ""
            reason = f"{prefix}metric receipt contains the stated value"
            evidence = _receipt_evidence(fresh_matches[0], current_head, current_head_reason, evidence_extra)
        elif matches:
            status = "fail"
            reason = f"stale metric receipt for claim: {claim['ref']}"
            evidence = _receipt_evidence(matches[0], current_head, current_head_reason, evidence_extra)
        elif candidates:
            status = "fail"
            reason = f"metric receipt mismatch for claim: {claim['ref']}"
            evidence = _receipt_evidence(candidates[0], current_head, current_head_reason, evidence_extra)
        else:
            status = "fail"
            reason = f"missing metric receipt for claim: {claim['ref']}"
            evidence = _receipt_evidence(None, current_head, current_head_reason, evidence_extra)
        ref = pr.Ref("metric_receipt", claim["ref"], claim["line"])
        entries.append(_entry(ref, "metric_receipt", "hard", status, reason, evidence, text))
    return entries


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
        elif diff_range:
            status = "fail"
            tier = "hard"
            reason = f"supplied --diff could not be checked: {diff_info['reason']}"
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
                       require_reviewed_cards: bool, diff_range: str | None = None,
                       receipts_dir: Path | None = None) -> dict:
    text, ignore_info = _prepared_text(artifact_path)
    files, tests, issues, commits = pr.detect_refs(text)
    receipts_info = _load_receipts(receipts_dir)
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
    entries.extend(_command_entries(text, root, receipts_info))
    entries.extend(_metric_entries(text, root, receipts_info))

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
        "receipts": {
            "path": receipts_info.get("path"),
            "mode": receipts_info.get("mode"),
            "reason": receipts_info.get("reason"),
            "count": len(receipts_info.get("receipts", [])),
            "errors": receipts_info.get("errors", []),
        },
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
    grouped = [
        ("changed_file", "changed_file"),
        ("command_receipt", "command_receipt"),
        ("metric_receipt", "metric_receipt"),
    ]
    sections: list[str] = []
    for claim_type, label in grouped:
        claims = [c for c in receipt.get("claims", []) if c.get("type") == claim_type]
        if not claims:
            continue
        lines = [f"- {label}: "
                 f"{len(claims)} checked, "
                 f"{sum(1 for c in claims if c['status'] == 'fail')} failed, "
                 f"{sum(1 for c in claims if c['status'] == 'advisory')} advisory"]
        for claim in claims:
            prefix = "FAIL" if claim["status"] == "fail" else claim["status"]
            lines.append(f"    {prefix} line {claim['line']}: {claim['reason']}")
        sections.append("\n".join(lines))
    if not sections:
        return base
    return "\n".join([base, *sections])


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
        _write(diff_root / "docs" / "existing.md", "# Existing\n\nstable\n")
        subprocess.run(["git", "-C", str(diff_root), "init"], capture_output=True, check=True)
        subprocess.run(["git", "-C", str(diff_root), "config", "user.email", "test@example.invalid"],
                       capture_output=True, check=True)
        subprocess.run(["git", "-C", str(diff_root), "config", "user.name", "Anti Slop Test"],
                       capture_output=True, check=True)
        subprocess.run(["git", "-C", str(diff_root), "add", "."], capture_output=True, check=True)
        subprocess.run(["git", "-C", str(diff_root), "commit", "-m", "base"],
                       capture_output=True, check=True)
        diff_head = subprocess.check_output(
            ["git", "-C", str(diff_root), "rev-parse", "HEAD"], text=True).strip()
        _write(diff_root / "docs" / "changed.md", "# Changed\n\nafter\n")
        changed_report = root / "diff" / "changed.md"
        not_changed_report = root / "diff" / "not_changed.md"
        no_diff_report = root / "diff" / "no_diff.md"
        ordinary_report = root / "diff" / "ordinary.md"
        invalid_diff_report = root / "diff" / "invalid_diff.md"
        diff_json = root / "diff.json"
        not_changed_json = root / "not-changed.json"
        no_diff_json = root / "no-diff.json"
        invalid_diff_json = root / "invalid-diff.json"
        _write(changed_report, "# Agent Final Report\n\nUpdated `docs/changed.md`.\n")
        _write(not_changed_report, "# Agent Final Report\n\nUpdated `docs/unchanged.md`.\n")
        _write(no_diff_report, "# Agent Final Report\n\nUpdated `docs/changed.md`.\n")
        _write(ordinary_report, "# Agent Final Report\n\nReferences `docs/unchanged.md`.\n")
        _write(invalid_diff_report, "# Agent Final Report\n\nUpdated `docs/existing.md`.\n")
        changed_exit = main(["--root", str(diff_root), "--diff", "HEAD", "--json",
                             str(diff_json), str(changed_report)])
        not_changed_exit = main(["--root", str(diff_root), "--diff", "HEAD", "--json",
                                 str(not_changed_json), str(not_changed_report)])
        no_diff_exit = main(["--root", str(diff_root), "--json", str(no_diff_json),
                             str(no_diff_report)])
        invalid_diff_exit = main(["--root", str(diff_root), "--diff", "definitely-not-a-ref",
                                  "--json", str(invalid_diff_json), str(invalid_diff_report)])
        ordinary_exit = main(["--root", str(diff_root), "--diff", "HEAD", str(ordinary_report)])
        diff_data = json.loads(diff_json.read_text(encoding="utf-8")) if diff_json.exists() else {}
        not_changed_data = (json.loads(not_changed_json.read_text(encoding="utf-8"))
                            if not_changed_json.exists() else {})
        no_diff_data = json.loads(no_diff_json.read_text(encoding="utf-8")) if no_diff_json.exists() else {}
        invalid_diff_data = (json.loads(invalid_diff_json.read_text(encoding="utf-8"))
                             if invalid_diff_json.exists() else {})

        command_receipts = root / "receipts" / "command"
        nonzero_receipts = root / "receipts" / "nonzero"
        stale_receipts = root / "receipts" / "stale"
        metric_receipts = root / "receipts" / "metric"
        empty_receipts = root / "receipts" / "empty"
        for d in (command_receipts, nonzero_receipts, stale_receipts, metric_receipts, empty_receipts):
            d.mkdir(parents=True, exist_ok=True)

        def command_receipt(path: Path, command: list[str], exit_code: int,
                            git_head: str = diff_head, metrics: dict | None = None) -> None:
            path.write_text(json.dumps({
                "schema_version": "anti-slop-command-receipt.v1",
                "receipt_type": "command",
                "command": command,
                "command_string": " ".join(command),
                "cwd": str(diff_root),
                "exit_code": exit_code,
                "duration_ms": 1,
                "git_head": git_head,
                "started_at": "2026-06-08T00:00:00Z",
                "stdout_sha256": "0" * 64,
                "stderr_sha256": "0" * 64,
                "stdout_bytes": 0,
                "stderr_bytes": 0,
                "tool_version": "self-test",
                "metrics": metrics or {},
            }), encoding="utf-8")

        command_receipt(command_receipts / "make-validate.json", ["make", "validate"], 0)
        command_receipt(nonzero_receipts / "make-validate.json", ["make", "validate"], 2)
        command_receipt(stale_receipts / "make-validate.json", ["make", "validate"], 0,
                        git_head="0" * 40)
        command_receipt(metric_receipts / "score.json", ["python3", "bench.py"], 0,
                        metrics={"score": 0.82, "score.before": 0.70, "score.after": 0.82})

        command_pass = root / "receipts" / "command-pass.md"
        command_missing = root / "receipts" / "command-missing.md"
        command_nonzero = root / "receipts" / "command-nonzero.md"
        command_stale = root / "receipts" / "command-stale.md"
        metric_pass = root / "receipts" / "metric-pass.md"
        metric_mismatch = root / "receipts" / "metric-mismatch.md"
        metric_missing = root / "receipts" / "metric-missing.md"
        command_pass_json = root / "command-pass.json"
        command_missing_json = root / "command-missing.json"
        command_nonzero_json = root / "command-nonzero.json"
        command_stale_json = root / "command-stale.json"
        metric_pass_json = root / "metric-pass.json"
        metric_mismatch_json = root / "metric-mismatch.json"
        metric_missing_json = root / "metric-missing.json"
        _write(command_pass, "# Agent Final Report\n\nmake validate passed.\n")
        _write(command_missing, "# Agent Final Report\n\npytest passed.\n")
        _write(command_nonzero, "# Agent Final Report\n\nmake validate passed.\n")
        _write(command_stale, "# Agent Final Report\n\nmake validate passed.\n")
        _write(metric_pass, "# Agent Final Report\n\nscore is 0.82. score improved from 0.70 to 0.82.\n")
        _write(metric_mismatch, "# Agent Final Report\n\nscore is 0.83.\n")
        _write(metric_missing, "# Agent Final Report\n\nmetric improved from 0.70 to 0.82.\n")
        command_pass_exit = main(["--root", str(diff_root), "--receipts", str(command_receipts),
                                  "--json", str(command_pass_json), str(command_pass)])
        command_missing_exit = main(["--root", str(diff_root), "--receipts", str(empty_receipts),
                                     "--json", str(command_missing_json), str(command_missing)])
        command_nonzero_exit = main(["--root", str(diff_root), "--receipts", str(nonzero_receipts),
                                     "--json", str(command_nonzero_json), str(command_nonzero)])
        command_stale_exit = main(["--root", str(diff_root), "--receipts", str(stale_receipts),
                                   "--json", str(command_stale_json), str(command_stale)])
        metric_pass_exit = main(["--root", str(diff_root), "--receipts", str(metric_receipts),
                                 "--json", str(metric_pass_json), str(metric_pass)])
        metric_mismatch_exit = main(["--root", str(diff_root), "--receipts", str(metric_receipts),
                                     "--json", str(metric_mismatch_json), str(metric_mismatch)])
        metric_missing_exit = main(["--root", str(diff_root), "--receipts", str(empty_receipts),
                                    "--json", str(metric_missing_json), str(metric_missing)])
        command_pass_data = json.loads(command_pass_json.read_text(encoding="utf-8")) if command_pass_json.exists() else {}
        command_missing_data = (json.loads(command_missing_json.read_text(encoding="utf-8"))
                                if command_missing_json.exists() else {})
        command_nonzero_data = (json.loads(command_nonzero_json.read_text(encoding="utf-8"))
                                if command_nonzero_json.exists() else {})
        command_stale_data = (json.loads(command_stale_json.read_text(encoding="utf-8"))
                              if command_stale_json.exists() else {})
        metric_pass_data = json.loads(metric_pass_json.read_text(encoding="utf-8")) if metric_pass_json.exists() else {}
        metric_mismatch_data = (json.loads(metric_mismatch_json.read_text(encoding="utf-8"))
                                if metric_mismatch_json.exists() else {})
        metric_missing_data = (json.loads(metric_missing_json.read_text(encoding="utf-8"))
                               if metric_missing_json.exists() else {})

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
            ("invalid diff range fails changed-file claims hard",
             invalid_diff_exit == 1
             and invalid_diff_data.get("diff", {}).get("mode") == "unavailable"
             and any(c.get("type") == "changed_file"
                     and c.get("ref") == "docs/existing.md"
                     and c.get("tier") == "hard"
                     and c.get("status") == "fail"
                     for c in invalid_diff_data.get("claims", []))),
            ("ordinary file resolution still works in diff mode",
             ordinary_exit == 0),
            ("command receipt backs make validate passed",
             command_pass_exit == 0 and any(c.get("type") == "command_receipt"
                                            and c.get("status") == "pass"
                                            for c in command_pass_data.get("claims", []))),
            ("missing command receipt fails",
             command_missing_exit == 1 and any(c.get("type") == "command_receipt"
                                               and c.get("status") == "fail"
                                               and "missing" in c.get("reason", "")
                                               for c in command_missing_data.get("claims", []))),
            ("nonzero command receipt fails passed claim",
             command_nonzero_exit == 1 and any(c.get("type") == "command_receipt"
                                               and c.get("status") == "fail"
                                               and "exit_code" in c.get("reason", "")
                                               for c in command_nonzero_data.get("claims", []))),
            ("stale command receipt fails",
             command_stale_exit == 1 and any(c.get("type") == "command_receipt"
                                             and c.get("status") == "fail"
                                             and "stale" in c.get("reason", "")
                                             for c in command_stale_data.get("claims", []))),
            ("metric receipt backs scalar and improvement claims",
             metric_pass_exit == 0
             and sum(1 for c in metric_pass_data.get("claims", [])
                     if c.get("type") == "metric_receipt" and c.get("status") == "pass") == 2),
            ("mismatched metric receipt fails",
             metric_mismatch_exit == 1 and any(c.get("type") == "metric_receipt"
                                               and c.get("status") == "fail"
                                               and "mismatch" in c.get("reason", "")
                                               for c in metric_mismatch_data.get("claims", []))),
            ("missing metric receipt fails",
             metric_missing_exit == 1 and any(c.get("type") == "metric_receipt"
                                              and c.get("status") == "fail"
                                              and "missing" in c.get("reason", "")
                                              for c in metric_missing_data.get("claims", []))),
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
          "diff mode checks changed-file claims; command and metric receipts are checked).")
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
    parser.add_argument("--receipts", type=Path,
                        help="directory of anti-slop-run JSON receipts for command/metric claims")
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
                                 args.require_reviewed_cards, args.diff_range,
                                 args.receipts)
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
