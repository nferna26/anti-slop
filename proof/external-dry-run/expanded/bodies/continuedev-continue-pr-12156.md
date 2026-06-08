Adds mercury-2 to the Inception Labs provider. 128k context, tools, OpenAI-compatible.

- llm-info: new `inception` provider with mercury-2, mercury-edit-2, mercury-coder-small
- GUI Add Chat form: Inception Labs entry with mercury-2 preset
- tool support: mercury-2 flagged as tool-capable

Dynamic model fetching works out of the box via inherited OpenAI `listModels()`.

## Test plan
- [ ] Add Inception provider in GUI with API key, confirm mercury-2 preset + dynamic list appear
- [ ] Chat with mercury-2, confirm streaming
- [ ] Tool call with mercury-2

<!-- This is an auto-generated description by cubic. -->
---
## Summary by cubic
Adds the Inception Labs provider with the Mercury 2 diffusion model (128k context) and tool calling. Users can add Inception in the GUI and chat with Mercury 2 using an OpenAI-compatible API.

- **New Features**
  - `llm-info`: new `inception` provider with `mercury-2`, `mercury-edit-2`, `mercury-coder-small`.
  - GUI Add New Model: Inception provider with API key input and a Mercury 2 preset.
  - Tool support: `mercury-2` marked as tool-capable in `PROVIDER_TOOL_SUPPORT`.
  - Dynamic model list via inherited OpenAI `listModels()`.

- **Bug Fixes**
  - Updated provider copy to describe Mercury 2 as a diffusion model and scope the blurb to Mercury 2.

<sup>Written for commit b576e39998eea7bfd98ed64d1884e53e53771365. Summary will update on new commits.</sup>

<!-- End of auto-generated description by cubic. -->
