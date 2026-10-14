# Google Lighthouse Agentic Browsing

Run this category as part of each website audit. It assesses machine interaction, separate from whether the business appears in AI search answers. Check current Google documentation and the installed Lighthouse category before execution. The audit set can change.

Official references:
- https://developer.chrome.com/blog/agent-ready-toolkit
- https://developer.chrome.com/docs/lighthouse/agentic-browsing/scoring

## Run and retain

Use the installed Lighthouse CLI or a supported DevTools tool. Enable the Agentic Browsing category explicitly; an ordinary performance run may omit it. In Lighthouse 13.5.0, the dedicated core/config/agentic-browsing-config.js config with --only-categories=agentic-browsing enables the category. Use the current installed path. Google documents Chrome 150 or newer and origin-trial support for WebMCP checks. Verify the actual browser version. Do not enable a client origin trial, change their site, or submit a form to complete an audit.

Save raw JSON and HTML, URL, timestamp, Lighthouse and browser versions, device settings and warnings. Read every category auditRef and its result. Current checks can include agent accessibility tree, CLS, WebMCP registrations/form coverage/schema, llms.txt and ARD catalog discovery. Preserve notApplicable, informative, error and runtime limits. A timeout is a failed fetch, not proof that a file is absent. Make one direct HTTP recheck where useful and retain its status separately. A 403 means that request was blocked.

## Client findings

Use a small native table with Check, Result and Observed evidence. Show check results rather than a 0-100 readiness grade. The category uses a fraction display and is experimental. Do not count not-applicable checks as successful tests. Report any incomplete check distinctly and keep the denominator explicit if a pass count is used. Do not infer zero tools or invalid integration from unsupported WebMCP checks. Passing accessibility-tree checks does not prove that the booking journey works; inspect the actual journey separately without submitting it.
