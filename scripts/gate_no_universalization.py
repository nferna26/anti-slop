#!/usr/bin/env python3
"""Flag broad advice claims that are not tied to visible scope conditions.

This is a deliberately conservative first implementation of the
no-universalization gate. It is intended for generated recommendations,
compiled briefs, and canon-candidate prose. It does not prove that a scoped
claim is correct; it catches the simpler failure where local source content is
stated as universal advice without any nearby limiting language.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import argparse
import re
import sys
import tempfile


UNIVERSAL_RE = re.compile(
    r"\b(always|never|every|everyone|all|any|must|should|only|guarantees?|"
    r"proves?|the key is|the answer is|the right move is|the rule is|"
    r"the best approach is|you need to|you have to)\b",
    re.IGNORECASE,
)

SCOPE_RE = re.compile(
    r"\b(if|when|unless|where|under|given|in this case|in this context|"
    r"for this|for these|in cases|in contexts|only if|as long as|depends|"
    r"may|might|can|could|often|usually|tends? to|is bounded by|"
    r"scope|scoped|boundary|condition|because|while|although|rather than|"
    r"instead of|compared with|against|option|package|choice|recommendation|"
    r"available|provided|verified|supported|unsupported|packet|source card|"
    r"public kb|locator|lineage|citation|cite|refuse|cannot supply)\b",
    re.IGNORECASE,
)

SKIP_LINE_RE = re.compile(
    r"^\s*(#|---|<!--|-->|```|\||\[|!\[|[-*]\s+\[[ xX]\])"
)


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    cue: str
    sentence: str


def strip_frontmatter_and_code(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    in_frontmatter = bool(lines and lines[0].strip() == "---")
    in_code = False
    for idx, line in enumerate(lines):
        if idx == 0 and in_frontmatter:
            out.append("")
            continue
        if in_frontmatter:
            if line.strip() == "---":
                in_frontmatter = False
            out.append("")
            continue
        if line.strip().startswith("```"):
            in_code = not in_code
            out.append("")
            continue
        out.append("" if in_code else line)
    return "\n".join(out)


def split_sentences(paragraph: str) -> list[str]:
    text = " ".join(part.strip() for part in paragraph.splitlines() if part.strip())
    if not text:
        return []
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+", text) if part.strip()]


def normalize_sentence(sentence: str) -> str:
    sentence = re.sub(r"^\s*[-*]\s+", "", sentence)
    sentence = re.sub(r"^\s*\d+\.\s+", "", sentence)
    return sentence.strip()


def negated_proof_cue(sentence: str, cue: re.Match[str]) -> bool:
    if not cue.group(0).lower().startswith("prove"):
        return False
    before = sentence[max(0, cue.start() - 40) : cue.start()].lower()
    return bool(re.search(r"\b(cannot|can't|not|never|does not|doesn't|cannot statistically)\b", before))


def check_file(path: Path) -> list[Finding]:
    raw = path.read_text(encoding="utf-8")
    text = strip_frontmatter_and_code(raw)
    findings: list[Finding] = []
    paragraph: list[str] = []
    paragraph_line = 1

    def flush() -> None:
        if not paragraph:
            return
        joined = "\n".join(paragraph)
        for sentence in split_sentences(joined):
            sentence = normalize_sentence(sentence)
            if not sentence:
                continue
            universal = UNIVERSAL_RE.search(sentence)
            if universal and negated_proof_cue(sentence, universal):
                continue
            if universal and not SCOPE_RE.search(sentence):
                findings.append(
                    Finding(
                        path=path,
                        line=paragraph_line,
                        cue=universal.group(0),
                        sentence=sentence,
                    )
                )
        paragraph.clear()

    for number, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if not stripped:
            flush()
            continue
        if SKIP_LINE_RE.match(stripped):
            flush()
            continue
        if not paragraph:
            paragraph_line = number
        paragraph.append(stripped)
    flush()
    return findings


def self_test() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        good = tmp_path / "good.md"
        bad = tmp_path / "bad.md"
        good.write_text(
            "When trait descriptions are formed after performance is known, "
            "they should be treated as non-independent evidence.\n",
            encoding="utf-8",
        )
        bad.write_text(
            "Always treat customer praise as contaminated. The key is diagnosis.\n",
            encoding="utf-8",
        )
        source_editor = tmp_path / "source_editor.md"
        source_editor.write_text(
            "Only BK-0048-card-001 is available in this packet. "
            "Only Chapter 5 is verified by the reviewed source card.\n",
            encoding="utf-8",
        )
        good_findings = check_file(good)
        bad_findings = check_file(bad)
        source_editor_findings = check_file(source_editor)
        if good_findings:
            print("Self-test failed: scoped sentence was flagged.")
            for finding in good_findings:
                print(f"  - {finding.sentence}")
            return 1
        if source_editor_findings:
            print("Self-test failed: source-editor refusal sentence was flagged.")
            for finding in source_editor_findings:
                print(f"  - {finding.sentence}")
            return 1
        if len(bad_findings) < 2:
            print("Self-test failed: universal claims were not flagged.")
            for finding in bad_findings:
                print(f"  - {finding.sentence}")
            return 1
    print("no-universalization self-test passed.")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, help="Markdown files to check")
    parser.add_argument("--self-test", action="store_true", help="run deterministic self-test")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.self_test:
        return self_test()
    if not args.paths:
        print("Usage: python3 scripts/gate_no_universalization.py <file.md> [more.md]")
        return 2

    paths = [path.resolve() for path in args.paths]
    missing = [path for path in paths if not path.exists()]
    if missing:
        for path in missing:
            print(f"Missing input: {path}")
        return 2

    findings: list[Finding] = []
    for path in paths:
        findings.extend(check_file(path))

    print("== no-universalization gate ==")
    print(f"Files checked: {len(paths)}")
    if findings:
        print("Result: FAIL")
        for finding in findings:
            print(
                f"  - {finding.path}:{finding.line}: broad cue "
                f"'{finding.cue}' without visible scope: {finding.sentence}"
            )
        return 1
    print("Result: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
