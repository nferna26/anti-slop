# Local Source Shelf

The local source shelf is where raw copyrighted source material lives **outside** the public repo. Its contents never reach a public artifact. This doc explains what the shelf is, what is and is not allowed there, and how the public KB references it without leaking it.

## Where the shelf lives

The conventional location is the operator's local `local-only/` directory (excluded by `.gitignore`). Other paths are fine if they are unambiguously local and excluded from git. The repo never names the actual directory.

## What may live there

Lawfully acquired raw source files: EPUB, PDF, MOBI, AZW, DJVU, CBZ, CBR, OCR output, extracted text dumps, working notes that quote large excerpts. Anything that would be a rights violation to publish is shelf-only by default.

## What may **not** be committed to the public repo

- Raw book files in any format.
- OCR dumps or extracted text from copyrighted sources.
- Copied chapters or long excerpts.
- Filenames that reveal copyrighted-file extensions.
- Private paths that point into the shelf (e.g., directory paths a reader could guess at).
- Embeddings or vector stores built from copyrighted raw text.

The hard rule in `legal-publication-policy.md` covers the same ground. This doc is the shelf-specific operational view.

## How the public KB references the shelf

Public-safe artifacts use **locators**, not paths:

- Author + title + edition + year + publisher (operator-verified) → bibliographic identity.
- Chapter, section, page range, paragraph number → location inside the work.
- Optional short conservative excerpt → only when it carries the claim and stays within the excerpt budget. Per `legal-publication-policy.md`: prefer paraphrase plus locator over excerpt.

A book map points to chapters and sections, never to a file path. A source card cites a page range, never a byte offset in a local file.

## Acquisition discipline

Only lawful access. The shelf grows only via legitimate channels: operator-owned purchases, library access, lawful open-access editions, public-domain editions for works whose original text is in the public domain. The shelf is not a piracy convenience.

When a source's rights status is uncertain (e.g., online-readable but not operator-verified as public domain), the manifest carries `raw_source_status: metadata_only` and the rights status is flagged for operator verification before any excerpting.

## Filename evidence

Listing filenames in the shelf is a permitted local operation (for example, to confirm a source is available before drafting a card). Filenames never enter public artifacts. The manifest records `local filename evidence present; edition unverified` as the standard public-safe phrasing.

`scripts/check_no_raw_text.py` is the defensive heuristic that catches stray raw paths and oversized text files; `scripts/kb_lint.py` catches raw-source filename extensions appearing in public Markdown. Neither is a legal guarantee. The operator is the last line of defense.

## Shelf hygiene

- Keep edition metadata in your private shelf notes; copy only operator-verified values into the public manifest.
- Do not commit shelf inventories. The public acquisition registry summarizes what exists locally via boolean flags, not names.
- Do not name third-party services that brokered a download; that is not a public-safe note.
