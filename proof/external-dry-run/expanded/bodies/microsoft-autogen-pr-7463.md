## Summary
- Restrict `ComponentLoader.load_component()` to only load providers from trusted first-party AutoGen namespaces (`autogen_core`, `autogen_agentchat`, `autogen_ext`, `autogen_studio`, `autogenstudio`), preventing arbitrary module loading via untrusted provider strings
- Add `AUTOGEN_ALLOWED_PROVIDER_NAMESPACES` environment variable so users with custom provider packages can extend the allowlist
- Harden VideoSurfer `extract_audio()` to reject URL inputs (SSRF), enforce `.mp3` extension, and block path traversal
- Add security caution language to AutoGen Studio README, main repo README, and installation docs

## Test plan
- [x] `test_untrusted_provider_rejected` — verifies providers outside trusted namespaces are blocked
- [x] `test_trusted_provider_via_env_var` — verifies env var extends the allowlist
- [x] All 226 autogen-core tests pass
- [x] `poe format` clean
- [x] `poe lint` clean
- [x] `poe pyright` clean (0 errors in autogen-core)
- [x] `poe mypy` clean (0 errors in autogen-core)
- [ ] CI checks pass
