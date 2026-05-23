# Acquisition Workflow

1. Paste the final 200-book list into `corpus/manifests/books-200.yaml`. (Done as of CORE-909.)
2. Work the priority order defined in `corpus/manifests/source-id-registry.yaml` — the first-50 wave is locked under CORE-910 at IDs BK-0001 to BK-0050. Map candidates and deep-card candidates are flagged in that file.
3. For each source, mark `acquisition_status` in the manifest.
4. Source a legal copy.
5. Record edition, year, publisher, ISBN when available, owned format, and locator system. Do not infer these from filenames — filename evidence supports `local_only` raw status but does not verify edition.
6. Store raw source material locally only, normally under `local-only/`.
7. Create a book map only after the source is acquired or otherwise lawfully accessible.

Do not commit raw book files, OCR dumps, extracted text, or copied chapters.
