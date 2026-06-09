#!/usr/bin/env python3
"""anti-slop-pr: deterministic PR-description provenance checker.

AI-written PR descriptions often cite things that do not exist: a fabricated
issue number, a doc/file path that was never added, a test node that is not
defined, or a source-card ID that does not resolve. This tool checks, before
merge, that the references a PR description names actually RESOLVE against the
repo (or a fixture root). It is deterministic and stdlib-only: no GitHub API, no
model, no network, no runtime.

It is a *resolver*, not a judge. A passing check means the cited references
resolve; it does NOT prove the PR is correct, that the change is supported, that
the cited file/test is *relevant*, or anything about advice quality, source
truth, or canon. It promotes no canon and lifts no status.

Reference types and tiers
--------------------------
Deterministic (hard; unresolved -> exit 1), resolved against ``--root``:
  - file refs:  ``docs/foo.md``, ``path/to/x.py``, optionally ``path.py:L10``
                (the file must exist; with a line, it must have >= that many
                lines). A ref must be PATH-LIKE (contain a ``/``); a bare
                basename like ``README.md`` or ``Express.js`` is a name, not a
                locatable path, and is ignored. (Dogfooding real PR bodies showed
                bare backtick basenames were the dominant false positive.)
  - test refs:  ``tests/test_x.py::test_name`` (file must exist AND define
                ``def test_name``/``async def test_name``/``class test_name``)
  - card/source refs: ``BK-1234`` / ``BK-1234-card-001`` — delegated to the
                anti-slop-lineage resolver (``gate_citation_lineage``); with
                ``--require-reviewed-cards`` a card must resolve to a *reviewed*
                source card.
Deterministic-against-a-registry (hard only when ``--issue-registry`` is given;
otherwise ADVISORY — reported, never fails the build):
  - issue refs: ``#123`` — offline there is no way to know GitHub issue state
                without a credential, so without a registry these are advisory.
Advisory (always reported, never fails):
  - commit refs: 7-40 hex tokens resolved against the LOCAL git repo at ``--root``
                (``git cat-file``). A hex token is ambiguous (commit SHA vs. a
                non-commit hash), so commit refs are advisory by default and
                degrade gracefully when ``--root`` is not a git repo.

Scoped ignore directives (for PRs that cite fabricated example refs on purpose,
e.g. a PR documenting this tool):
  - ``<!-- anti-slop-pr: ignore-next-line -->`` blanks the following line.
  - ``<!-- anti-slop-pr: ignore-start -->`` … ``<!-- anti-slop-pr: ignore-end -->``
    blank the lines between the markers.
  Auditable + fail-safe: only these exact comments suppress checks; any unknown
  comment never does; an UNCLOSED ``ignore-start`` is a no-op (it hides nothing —
  checks stay ON) and is reported as a warning. The number of ignored lines and
  any warnings are recorded in the report and the JSON receipt.

Output: a human report and (``--json``) a JSON receipt. Exit 0 (all hard refs
resolve), 1 (>=1 hard ref unresolved), 2 (usage/missing input). ``--report``
forces exit 0 (advisory adoption mode).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import argparse
import json
import re
import subprocess
import sys
import tempfile

# Reuse the anti-slop-lineage resolver for card/source refs (sibling module in
# scripts/; no fork — the same build_index/check_paths the CLI and gate use).
sys.path.insert(0, str(Path(__file__).resolve().parent))
import gate_citation_lineage as lineage  # noqa: E402

FILE_EXT = (r"(?:md|markdown|py|sh|txt|ya?ml|json|toml|cfg|ini|rst|js|ts|tsx|jsx"
            r"|go|rs|c|h|cpp|hpp|cc|java|rb|mk|cff|lock)")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
TEST_RE = re.compile(r"\b([\w./-]+\.py)::([A-Za-z_]\w*)\b")
FILE_RE = re.compile(r"(?<![\w/.])([\w./-]+\." + FILE_EXT + r")(?::L?(\d+))?\b")
ISSUE_RE = re.compile(r"(?<![\w&#])#(\d+)\b")
# 7–40 hex with at least one a–f letter, so pure-digit runs (counts, years) are
# not mistaken for SHAs. Still ambiguous (could be a non-commit hash) -> advisory.
COMMIT_RE = re.compile(r"(?<![\w])(?=[0-9a-f]*[a-f])([0-9a-f]{7,40})(?![\w])")
# An async test (`async def test_x`) is still a defined node.
DEF_RE_TMPL = r"(?:^|\n)\s*(?:async\s+)?(?:def|class)\s+{}\b"

# Scoped, EXPLICIT ignore directives (auditable — only these exact comments
# disable checks; any other/unknown comment never does). They are HTML comments,
# so they are also hidden by GitHub and stripped after they are applied.
# Anchored to their OWN line (modulo surrounding whitespace): a directive that
# shares a line with content/refs is NOT recognized — it stays a normal HTML
# comment and suppresses nothing. This keeps suppression predictable and stops a
# directive mentioned in prose from accidentally opening a block.
IGNORE_NEXT_RE = re.compile(r"^\s*<!--\s*anti-slop-pr:\s*ignore-next-line\s*-->\s*$")
IGNORE_START_RE = re.compile(r"^\s*<!--\s*anti-slop-pr:\s*ignore-start\s*-->\s*$")
IGNORE_END_RE = re.compile(r"^\s*<!--\s*anti-slop-pr:\s*ignore-end\s*-->\s*$")


@dataclass(frozen=True)
class Ref:
    kind: str
    value: str
    line: int
    detail: str = ""


@dataclass
class Result:
    refs_checked: int = 0
    unresolved: list[str] = field(default_factory=list)
    advisory: list[str] = field(default_factory=list)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def strip_html_comments(text: str) -> str:
    """Blank out ``<!-- ... -->`` blocks (GitHub hides them, so they are not part
    of the PR's visible claim) while preserving line numbers for accurate
    reporting."""
    return HTML_COMMENT_RE.sub(lambda m: "\n" * m.group(0).count("\n"), text)


def apply_ignores(text: str) -> tuple[str, dict]:
    """Blank lines suppressed by EXPLICIT ignore directives BEFORE ref detection,
    preserving line numbers. Each directive must be on its **own line** (only
    surrounding whitespace allowed); a marker that shares a line with content is
    NOT a directive and suppresses nothing. Two forms:

      ``<!-- anti-slop-pr: ignore-next-line -->`` — blanks the immediately
        following physical line.
      ``<!-- anti-slop-pr: ignore-start -->`` … ``<!-- anti-slop-pr: ignore-end -->``
        — blanks the content lines BETWEEN the markers (the marker lines
        themselves are not refs). Multiple separate blocks are supported.

    Auditable + fail-safe: only these exact own-line directives suppress checks;
    an unknown comment never does. An **unclosed** ``ignore-start`` is a **no-op**
    (it blanks nothing — checks stay ON to end of file) and is reported as a
    warning, so a typo can never silently hide the rest of a PR body. A stray
    ``ignore-end`` and a nested ``ignore-start`` are likewise reported. Returns the
    de-ignored text and an audit dict ``{ignored_lines, warnings}``."""
    lines = text.split("\n")
    blank: set[int] = set()
    warnings: list[str] = []
    open_idx: int | None = None
    for i, line in enumerate(lines):
        if open_idx is None:
            if IGNORE_END_RE.search(line):
                warnings.append(f"line {i + 1}: stray ignore-end (no open ignore-start) — no effect")
            elif IGNORE_START_RE.search(line):
                open_idx = i
        else:
            if IGNORE_END_RE.search(line):
                blank.update(range(open_idx + 1, i))  # content between the markers
                open_idx = None
            elif IGNORE_START_RE.search(line):
                warnings.append(f"line {i + 1}: nested ignore-start (already in an ignore block)")
    if open_idx is not None:
        # Fail-safe: unclosed start ignores NOTHING (do not hide the rest of file).
        warnings.append(
            f"line {open_idx + 1}: unclosed ignore-start — directive ignored, checks left ON to end of file")
    for i, line in enumerate(lines):
        if IGNORE_NEXT_RE.search(line) and i + 1 < len(lines):
            blank.add(i + 1)
    out = ["" if i in blank else line for i, line in enumerate(lines)]
    return "\n".join(out), {"ignored_lines": len(blank), "warnings": warnings}


def load_issue_registry(path: Path | None) -> set[str] | None:
    """Parse a registry of valid issue numbers: one per line, optional leading
    ``#`` (so ``#123`` and ``123`` both work); blank lines and ``# word`` comment
    lines are ignored. Only digit tokens are kept."""
    if path is None:
        return None
    nums: set[str] = set()
    for line in read_text(path).splitlines():
        token = line.strip().lstrip("#").strip()
        if token.isdigit():
            nums.add(token)
    return nums


def detect_refs(text: str) -> tuple[list[Ref], list[Ref], list[Ref], list[Ref]]:
    files: list[Ref] = []
    tests: list[Ref] = []
    issues: list[Ref] = []
    commits: list[Ref] = []
    for number, line in enumerate(text.splitlines(), start=1):
        for m in TEST_RE.finditer(line):
            tests.append(Ref("test", f"{m.group(1)}::{m.group(2)}", number,
                             detail=m.group(2)))
        masked = TEST_RE.sub(lambda m: " " * len(m.group(0)), line)
        for m in FILE_RE.finditer(masked):
            path = m.group(1)
            # A bare basename ('foo.py', 'README.md', 'Express.js') — even in
            # backticks — is a NAME, not a locatable path claim: we cannot know
            # where it lives. Only path-like refs (containing a '/') are checked.
            # Dogfooding real PR bodies showed bare backtick basenames were the
            # dominant false-positive source, so the rule requires a separator.
            if "/" not in path:
                continue
            files.append(Ref("file", path, number, detail=m.group(2) or ""))
        for m in ISSUE_RE.finditer(line):
            issues.append(Ref("issue", m.group(1), number))
        for m in COMMIT_RE.finditer(masked):
            commits.append(Ref("commit", m.group(1), number))
    return files, tests, issues, commits


def check_files(refs: list[Ref], root: Path) -> Result:
    res = Result()
    for ref in refs:
        res.refs_checked += 1
        target = root / ref.value
        if not target.is_file():
            res.unresolved.append(f"line {ref.line}: file does not resolve: {ref.value}")
            continue
        if ref.detail:
            need = int(ref.detail)
            have = len(read_text(target).splitlines())
            if have < need:
                res.unresolved.append(
                    f"line {ref.line}: {ref.value} has {have} lines, ref needs >= {need}")
    return res


def check_tests(refs: list[Ref], root: Path) -> Result:
    res = Result()
    for ref in refs:
        res.refs_checked += 1
        file_part, _, node = ref.value.partition("::")
        target = root / file_part
        if not target.is_file():
            res.unresolved.append(f"line {ref.line}: test file does not resolve: {file_part}")
            continue
        if not re.search(DEF_RE_TMPL.format(re.escape(node)), read_text(target)):
            res.unresolved.append(
                f"line {ref.line}: test node not defined in {file_part}: {node}")
    return res


def check_issues(refs: list[Ref], registry: set[str] | None) -> Result:
    res = Result()
    for ref in refs:
        res.refs_checked += 1
        if registry is None:
            res.advisory.append(
                f"line {ref.line}: #{ref.value} (advisory — no --issue-registry to resolve against)")
        elif ref.value not in registry:
            res.unresolved.append(f"line {ref.line}: issue does not resolve: #{ref.value}")
    return res


def check_commits(refs: list[Ref], root: Path) -> Result:
    """ADVISORY (never fails the build): resolve hex tokens against the LOCAL git
    repo at ``root`` (``git cat-file -e``). A 7–40 hex token is ambiguous — it may
    be a commit SHA or an unrelated hash (e.g. a sha256 fragment) — so this
    category is advisory by default: it reports resolved/unresolved rather than
    failing. Degrades gracefully when ``root`` is not a git repo or git is
    unavailable. Offline; local git only, no network or GitHub API."""
    res = Result()
    if not refs:
        return res
    if not (root / ".git").exists():
        for ref in refs:
            res.refs_checked += 1
            res.advisory.append(
                f"line {ref.line}: {ref.value[:12]} (advisory — root is not a git repo; commit refs not resolved)")
        return res
    for ref in refs:
        res.refs_checked += 1
        try:
            ok = subprocess.run(
                ["git", "-C", str(root), "cat-file", "-e", f"{ref.value}^{{commit}}"],
                capture_output=True).returncode == 0
        except OSError:
            res.advisory.append(f"line {ref.line}: {ref.value[:12]} (advisory — git unavailable)")
            continue
        if not ok:
            res.advisory.append(
                f"line {ref.line}: {ref.value[:12]} does not resolve to a local commit "
                "(advisory — may be a non-commit hash)")
    return res


def check_cards(pr_text: str, root: Path, require_reviewed: bool) -> Result:
    res = Result()
    index = lineage.build_index(root)
    with tempfile.TemporaryDirectory() as tmp:
        tf = Path(tmp) / "pr.md"  # comment-stripped text, line numbers preserved
        tf.write_text(pr_text, encoding="utf-8")
        findings, ref_count = lineage.check_paths([tf], index, require_reviewed=require_reviewed)
    res.refs_checked = ref_count
    for f in findings:
        # findings look like "<abs path>:<line>: <detail>"; keep the line+detail tail
        tail = f.split(":", 1)[1] if ":" in f else f
        res.unresolved.append(tail.strip())
    return res


def run(pr_path: Path, root: Path, registry: set[str] | None,
        require_reviewed_cards: bool) -> dict:
    # Apply explicit ignore directives FIRST, then strip HTML comments (incl. the
    # directive markers), then detect refs — all preserving line numbers.
    deignored, ignore_info = apply_ignores(read_text(pr_path))
    text = strip_html_comments(deignored)
    files, tests, issues, commits = detect_refs(text)
    results = {
        "file": check_files(files, root),
        "test": check_tests(tests, root),
        "issue": check_issues(issues, registry),
        "card": check_cards(text, root, require_reviewed_cards),
        "commit": check_commits(commits, root),  # advisory only — never fails
    }
    # commit refs are advisory (ambiguous hex); they do NOT fail the build.
    hard_unresolved = (results["file"].unresolved + results["test"].unresolved
                       + results["card"].unresolved + results["issue"].unresolved)
    receipt = {
        "pr_file": pr_path.name,
        "root": str(root.resolve()),
        "issue_registry": registry is not None,
        "require_reviewed_cards": require_reviewed_cards,
        "ignores": ignore_info,  # audit trail: {ignored_lines, warnings}
        "checks": {k: {"refs_checked": v.refs_checked,
                       "unresolved": v.unresolved,
                       "advisory": v.advisory} for k, v in results.items()},
        "passed": not hard_unresolved,
    }
    return receipt


def render(receipt: dict) -> str:
    lines = ["== anti-slop-pr provenance check ==",
             f"PR file: {receipt['pr_file']}",
             f"Root: {receipt['root']}",
             f"Issue registry: {'provided' if receipt['issue_registry'] else 'none (issue refs advisory)'}",
             f"Reviewed-cards mode: {receipt['require_reviewed_cards']}"]
    ign = receipt.get("ignores", {"ignored_lines": 0, "warnings": []})
    if ign["ignored_lines"] or ign["warnings"]:
        lines.append(f"Ignored lines (explicit directives): {ign['ignored_lines']}")
        for w in ign["warnings"]:
            lines.append(f"    ignore-warning {w}")
    for kind in ("file", "test", "issue", "card", "commit"):
        c = receipt["checks"][kind]
        lines.append(f"- {kind}: {c['refs_checked']} checked, "
                     f"{len(c['unresolved'])} unresolved, {len(c['advisory'])} advisory")
        for u in c["unresolved"]:
            lines.append(f"    UNRESOLVED {u}")
        for a in c["advisory"]:
            lines.append(f"    advisory   {a}")
    lines.append("Result: PASS" if receipt["passed"] else "Result: FAIL")
    return "\n".join(lines)


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def self_test() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        _write(root / "docs" / "example.md", "# Example\n\nHello.\n")
        _write(root / "README.md", "# Fixture readme\n")
        _write(root / "tests" / "test_example.py",
               "def test_widget():\n    assert True\n\n\nasync def test_async():\n    assert True\n")
        _write(root / "corpus" / "source-cards" / "BK-7001-card-001.md",
               "---\ncard_id: BK-7001-card-001\nsource_id: BK-7001\n"
               "operator_review_status: reviewed\n---\n\n# Card\n\nClaim.\n")
        _write(root / "corpus" / "manifests" / "books-200.yaml", "  - source_id: BK-7001\n")
        _write(root / "issues.txt", "# valid issue numbers\n42\n7\n")
        registry = load_issue_registry(root / "issues.txt")

        good = root / "good.md"
        _write(good, "Closes #42. Adds `docs/example.md`, covered by "
                     "`tests/test_example.py::test_widget`; supported by `BK-7001-card-001`.\n")
        bad = root / "bad.md"
        _write(bad, "Closes #9999. See `docs/missing.md` and "
                    "`tests/test_example.py::test_nope`; per `BK-7099-card-001`.\n")
        # prose body: bare basenames 'Express.js' and `README.md` (no '/', even in
        # backticks) must be IGNORED (names, not path claims); an async test node
        # must resolve. Only path-like refs are checked.
        prose = root / "prose.md"
        _write(prose, "Migrated from Express.js to keep parity. See `README.md`; "
                      "covered by `tests/test_example.py::test_async`.\n")
        # commit body: a hex token in a NON-git tmp root -> advisory (degraded),
        # never a hard failure.
        commitb = root / "commitb.md"
        _write(commitb, "Reverts 1a2b3c4 from the earlier fix.\n")
        # ignore-directive bodies. `docs/fake.md` is a path-like fabricated file
        # that fails unless suppressed by an EXPLICIT ignore directive.
        ign_next = root / "ign_next.md"
        _write(ign_next, "Intro.\n<!-- anti-slop-pr: ignore-next-line -->\n"
                         "Example: `docs/fake.md` (fabricated, intentionally cited).\n")
        nofake = root / "nofake.md"
        _write(nofake, "Example: `docs/fake.md` (fabricated).\n")
        ign_block = root / "ign_block.md"
        _write(ign_block, "<!-- anti-slop-pr: ignore-start -->\n"
                          "Examples: `docs/fake.md` and #9999.\n"
                          "<!-- anti-slop-pr: ignore-end -->\nReal: `docs/example.md`.\n")
        ign_block_out = root / "ign_block_out.md"
        _write(ign_block_out, "<!-- anti-slop-pr: ignore-start -->\n"
                              "`docs/fake.md`.\n<!-- anti-slop-pr: ignore-end -->\n"
                              "Outside: `docs/fake2.md`.\n")
        ign_unclosed = root / "ign_unclosed.md"
        _write(ign_unclosed, "<!-- anti-slop-pr: ignore-start -->\n`docs/fake.md`.\n")
        ign_stray = root / "ign_stray.md"
        _write(ign_stray, "<!-- anti-slop-pr: ignore-end -->\n`docs/fake.md`.\n")
        ign_unknown = root / "ign_unknown.md"
        _write(ign_unknown, "<!-- anti-slop-pr: bogus -->\n`docs/fake.md`.\n")
        # multiple separate blocks, with a real ref in the gap (still checked).
        ign_multi = root / "ign_multi.md"
        _write(ign_multi, "<!-- anti-slop-pr: ignore-start -->\n`docs/fake1.md`\n"
                          "<!-- anti-slop-pr: ignore-end -->\nGap: `docs/example.md`\n"
                          "<!-- anti-slop-pr: ignore-start -->\n`docs/fake2.md`\n"
                          "<!-- anti-slop-pr: ignore-end -->\n")
        # a directive sharing a line with content is NOT a directive (own-line rule):
        # the fabricated ref on that line is still checked.
        ign_inline = root / "ign_inline.md"
        _write(ign_inline, "Content `docs/fake.md` <!-- anti-slop-pr: ignore-start -->\n")

        g = run(good, root, registry, require_reviewed_cards=True)
        b = run(bad, root, registry, require_reviewed_cards=False)
        p = run(prose, root, registry, require_reviewed_cards=False)
        cm = run(commitb, root, None, require_reviewed_cards=False)
        inext = run(ign_next, root, registry, False)
        inofake = run(nofake, root, registry, False)
        iblock = run(ign_block, root, registry, False)
        iblock_out = run(ign_block_out, root, registry, False)
        iunclosed = run(ign_unclosed, root, registry, False)
        istray = run(ign_stray, root, registry, False)
        iunknown = run(ign_unknown, root, registry, False)
        imulti = run(ign_multi, root, registry, False)
        iinline = run(ign_inline, root, registry, False)
        # good with NO registry -> issues advisory, still passes
        g_noreg = run(good, root, None, require_reviewed_cards=True)
        # bad with NO registry -> still fails on file/test/card
        b_noreg = run(bad, root, None, require_reviewed_cards=False)

        checks = [
            ("good resolves all hard refs", g["passed"] is True),
            ("good detected >=1 issue/file/test/card each",
             g["checks"]["issue"]["refs_checked"] >= 1
             and g["checks"]["file"]["refs_checked"] >= 1
             and g["checks"]["test"]["refs_checked"] >= 1
             and g["checks"]["card"]["refs_checked"] >= 1),
            ("bad fails", b["passed"] is False),
            ("bad catches fake issue", any("#9999" in u for u in b["checks"]["issue"]["unresolved"])),
            ("bad catches missing file", any("missing.md" in u for u in b["checks"]["file"]["unresolved"])),
            ("bad catches missing test node", any("test_nope" in u for u in b["checks"]["test"]["unresolved"])),
            ("bad catches fake card", any("BK-7099" in u for u in b["checks"]["card"]["unresolved"])),
            ("no registry -> good still passes (issues advisory)",
             g_noreg["passed"] is True and len(g_noreg["checks"]["issue"]["advisory"]) >= 1),
            ("no registry -> bad still fails on file/test/card", b_noreg["passed"] is False),
            ("prose body passes (no false positives)", p["passed"] is True),
            ("bare/backtick basenames without '/' are NOT file refs (Express.js, README.md ignored)",
             p["checks"]["file"]["refs_checked"] == 0),
            ("async test node resolves",
             p["checks"]["test"]["refs_checked"] == 1 and not p["checks"]["test"]["unresolved"]),
            ("commit refs are advisory and never fail (non-git root degrades gracefully)",
             cm["passed"] is True and cm["checks"]["commit"]["refs_checked"] >= 1
             and len(cm["checks"]["commit"]["advisory"]) >= 1
             and not cm["checks"]["commit"]["unresolved"]),
            ("ignore-next-line suppresses the next line's fabricated ref",
             inext["passed"] is True and inext["ignores"]["ignored_lines"] >= 1),
            ("the same fabricated ref WITHOUT ignore still fails",
             inofake["passed"] is False),
            ("ignore-start/end block suppresses fabricated refs inside",
             iblock["passed"] is True and iblock["ignores"]["ignored_lines"] >= 1),
            ("refs OUTSIDE an ignore block are still checked",
             iblock_out["passed"] is False
             and any("fake2.md" in u for u in iblock_out["checks"]["file"]["unresolved"])),
            ("unclosed ignore-start is a no-op (ref after it still fails) + warning",
             iunclosed["passed"] is False
             and iunclosed["ignores"]["ignored_lines"] == 0
             and any("unclosed" in w for w in iunclosed["ignores"]["warnings"])),
            ("stray ignore-end warns and suppresses nothing",
             istray["passed"] is False
             and any("stray" in w for w in istray["ignores"]["warnings"])),
            ("unknown anti-slop-pr comment does NOT disable checks",
             iunknown["passed"] is False and iunknown["ignores"]["ignored_lines"] == 0),
            ("multiple separate ignore blocks each suppress; the gap ref is still checked",
             imulti["passed"] is True and imulti["ignores"]["ignored_lines"] == 2),
            ("a directive sharing a line with content is NOT a directive (own-line rule)",
             iinline["passed"] is False and iinline["ignores"]["ignored_lines"] == 0
             and not iinline["ignores"]["warnings"]),
        ]
        failed = [name for name, ok in checks if not ok]
        if failed:
            print("pr-provenance self-test FAILED:")
            for name in failed:
                print(f"  - {name}")
            return 1
    print("pr-provenance self-test passed (22 checks: file/test/issue/card resolution, "
          "fake-ref detection, advisory issue/commit behaviour, async test nodes, the "
          "path-like file-ref rule, and explicit own-line ignore directives — next-line, "
          "block, multiple blocks, no-ignore-still-fails, refs-outside-still-checked, "
          "own-line enforcement, and fail-safe unclosed/stray/unknown behaviour).")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("pr_file", nargs="?", type=Path, help="PR description Markdown file")
    p.add_argument("--root", type=Path, default=Path.cwd(),
                   help="repo or fixture root to resolve references against (default: cwd)")
    p.add_argument("--issue-registry", type=Path,
                   help="file of valid issue numbers (one per line); without it, issue refs are advisory")
    p.add_argument("--require-reviewed-cards", action="store_true",
                   help="require every cited source-card to resolve to a reviewed card")
    p.add_argument("--json", type=Path, help="write the JSON receipt to this path")
    p.add_argument("--report", action="store_true",
                   help="advisory mode: print the report but always exit 0 (do not fail on "
                        "unresolved refs) — for advisory adoption before enforcing")
    p.add_argument("--self-test", action="store_true", help="run the deterministic self-test")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.self_test:
        return self_test()
    if not args.pr_file:
        print("Usage: python3 scripts/gate_pr_provenance.py [--root DIR] "
              "[--issue-registry F] [--require-reviewed-cards] [--json OUT] <pr.md>")
        return 2
    if not args.pr_file.exists():
        print(f"Missing input: {args.pr_file}")
        return 2
    registry = load_issue_registry(args.issue_registry)
    receipt = run(args.pr_file.resolve(), args.root, registry, args.require_reviewed_cards)
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
