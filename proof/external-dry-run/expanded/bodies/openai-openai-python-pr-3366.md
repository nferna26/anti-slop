## Summary

- Remove the daily cron trigger from the `Create releases` workflow.
- Keep the push-to-`main` trigger so release-please still runs when commits land on main.

## Why

The scheduled run asks for the `publish` environment approval before the release-please step can even determine whether there is anything to release. That creates noisy approval prompts for daily no-op release checks. Relying on the commit-driven release-please flow keeps releases tied to main branch changes.

## Validation

- Inspected the workflow diff; change is limited to removing the two-line `schedule` block.
- No local tests run; this is a GitHub Actions trigger-only change.
