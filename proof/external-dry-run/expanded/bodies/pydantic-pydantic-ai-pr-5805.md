Documentation-only change; no linked issue (trivial CE / doc improvement).

This writes down the VCR-maximalist testing philosophy that the project already enforces in review but whose rationale currently lives only in maintainers' heads and private `CLAUDE.local` notes — not where review agents or contributors can cite it. The new `## Testing philosophy` section makes the default (VCR + public-API tests against real recorded provider responses) and the carve-out for unit tests (definitory internal behavior, including cases VCR can't protect because cassette matchers aren't always body-sensitive) explicit. It also adds the missing worked `@dataclass Case` example to `## Parametrization with Expectations`, disambiguating it from the existing `EXPECTATIONS`-dict pattern: `Case` for heterogeneous feature-centric files run through one comprehensive parametrized test, the dict for a pure cartesian `(model, stream)` output lookup.

### Checklist

- [ ] Any **AI generated code** has been reviewed line-by-line by the human PR author, who stands by it.
- [x] No **breaking changes** in accordance with the [version policy](https://github.com/pydantic/pydantic-ai/blob/main/docs/version-policy.md).
- [x] **PR title** is fit for the [release changelog](https://github.com/pydantic/pydantic-ai/releases).
