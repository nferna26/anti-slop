#!/usr/bin/env python3
"""Lightweight lint for the maintained Markdown KB front door.

Checks:
- kb/index.md exists.
- kb/log.md exists.
- AGENTS.md exists at repo root.
- README.md has no "Archived Legacy Work" section.
- README.md contains "Objective", "Publication Rule", "Proof Surface", and "Start" sections.
- Local Markdown links are not broken.
- Public Markdown files do not name raw-source filename extensions (.epub, .pdf,
  .mobi, .azw, .azw3, .djvu, .cbz, .cbr) except inside .gitignore,
  docs/legal-publication-policy.md, or the README's Publication Rule section.

Standard library only.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
KB = ROOT / "kb"
INDEX = KB / "index.md"
LOG = KB / "log.md"
AGENTS = ROOT / "AGENTS.md"
README = ROOT / "README.md"

EXCLUDED_PARTS = {".git", "_archive", "local-only", "__pycache__"}
WIKI_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

REQUIRED_README_SECTIONS = ["Objective", "Publication Rule", "Proof Surface", "Start"]
README_FORBIDDEN_SECTION = "Archived Legacy Work"

RAW_EXTENSION_RE = re.compile(
    r"\.(epub|pdf|mobi|azw|azw3|djvu|cbz|cbr)\b", re.IGNORECASE
)
RAW_EXTENSION_ALLOWLIST = {
    Path(".gitignore"),
    Path("docs/legal-publication-policy.md"),
}
PUBLICATION_RULE_HEADING_RE = re.compile(
    r"^##\s+Publication Rule\s*$", re.MULTILINE
)
NEXT_H2_RE = re.compile(r"^##\s+", re.MULTILINE)


def public_markdown_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        if any(part in EXCLUDED_PARTS for part in path.relative_to(ROOT).parts):
            continue
        files.append(path)
    return sorted(files)


def local_link_target(source: Path, href: str) -> Path | None:
    if href.startswith(("http://", "https://", "mailto:", "#")):
        return None
    clean = href.split("#", 1)[0].strip()
    if not clean:
        return None
    return (source.parent / clean).resolve()


def has_section_heading(text: str, name: str) -> bool:
    pattern = re.compile(rf"^#{{1,6}}\s+{re.escape(name)}\b", re.MULTILINE)
    return bool(pattern.search(text))


def strip_publication_rule_section(text: str) -> str:
    """Return README text with the Publication Rule section removed."""
    match = PUBLICATION_RULE_HEADING_RE.search(text)
    if not match:
        return text
    start = match.start()
    next_match = NEXT_H2_RE.search(text, match.end())
    end = next_match.start() if next_match else len(text)
    return text[:start] + text[end:]


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    # Required files
    if not KB.exists():
        errors.append("kb/ folder is missing")
    if not INDEX.exists():
        errors.append("kb/index.md is missing")
    if not LOG.exists():
        errors.append("kb/log.md is missing")
    if not AGENTS.exists():
        errors.append("AGENTS.md (repo root) is missing")
    if not README.exists():
        errors.append("README.md (repo root) is missing")

    # kb/index.md expected anchors (existing warnings, kept)
    if INDEX.exists():
        index_text = INDEX.read_text(encoding="utf-8")
        for required in ["Project README", "KB log", "Proof Surface", "Authority Reminder"]:
            if required not in index_text:
                warnings.append(f"kb/index.md missing expected section/text: {required}")

    # kb/log.md template + dated entry
    if LOG.exists():
        log_text = LOG.read_text(encoding="utf-8")
        if "Log Entry Template" not in log_text:
            warnings.append("kb/log.md missing log entry template")
        if not re.search(r"^##\s+\d{4}-\d{2}-\d{2}\s*$", log_text, re.MULTILINE):
            warnings.append("kb/log.md has no dated entry")

    # README.md structural checks
    if README.exists():
        readme_text = README.read_text(encoding="utf-8")
        if has_section_heading(readme_text, README_FORBIDDEN_SECTION):
            errors.append(
                f"README.md must not contain a '{README_FORBIDDEN_SECTION}' section"
            )
        for section in REQUIRED_README_SECTIONS:
            if not has_section_heading(readme_text, section):
                errors.append(f"README.md missing required section: {section}")

    # Broken local links + raw-extension check on public Markdown files
    for path in public_markdown_files():
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)

        for match in WIKI_LINK_RE.finditer(text):
            href = match.group(1)
            target = local_link_target(path, href)
            if target is None:
                continue
            if not target.exists():
                display = (
                    target.relative_to(ROOT) if ROOT in target.parents else target
                )
                errors.append(f"{relative}: broken local link to {display}")

        if relative in RAW_EXTENSION_ALLOWLIST:
            continue

        text_for_ext_check = text
        if relative == Path("README.md"):
            text_for_ext_check = strip_publication_rule_section(text_for_ext_check)

        found_extensions: list[str] = []
        for ext_match in RAW_EXTENSION_RE.finditer(text_for_ext_check):
            found_extensions.append(ext_match.group(0))
        if found_extensions:
            unique = sorted(set(e.lower() for e in found_extensions))
            errors.append(
                f"{relative}: contains raw-source extension(s) {unique} outside allowed scope"
            )

    if warnings:
        print("KB lint warnings:")
        for warning in warnings:
            print(f"  - {warning}")
    if errors:
        print("KB lint failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("KB lint passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
