

<!-- This is an auto-generated description by cubic. -->
## Summary by cubic
Skip screenshots on new-tab pages and drop placeholder images before LLM serialization. This reduces noise and prevents placeholders from leaking across steps or tabs.

- **Bug Fixes**
  - In `get_user_message`, always disable vision when `is_new_tab_page(url)` is true.
  - Exclude `PLACEHOLDER_4PX_SCREENSHOT` before deciding to include screenshots and when labeling them.

- **Dependencies**
  - Bump `browser-use` version to 0.12.9.

<sup>Written for commit 103313ed63fbe7e2ba34779a04feeaf65cd645b0. Summary will update on new commits. <a href="https://cubic.dev/pr/browser-use/browser-use/pull/4920?utm_source=github">Review in cubic</a></sup>

<!-- End of auto-generated description by cubic. -->
