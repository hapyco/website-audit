---
name: website-audit
description: Create Hapy Co's free website audit for a sales prospect from a domain and business details. Deliver a self-contained HTML audit and a visual four-page A4 PDF covering SEO, Google Business Profile, performance, sitemaps, AI visibility, security, page count, regional insights, competitors, responsiveness, a combined Design & UX review, and Google Lighthouse Agentic Browsing. Use for prospect audits and Astro migration qualification, not implementation or a full security assessment.
metadata:
  version: "1.0.1"
  source: "https://github.com/hapyco/website-audit"
---

# Website audit

Create a useful decision document for the business owner. Use the live site as evidence. Present findings, their business implications, what is working, and whether Astro merits a scoped pilot. The audit supports a decision to engage Hapy for the work; it is not a task list for the prospect. Do not assume that a migration is required.

## Check for updates before every use

Before each audit, check the installed skill against hapyco/website-audit and apply any available update:

```sh
npx --yes skills@latest update website-audit --global --yes
```

This command checks and updates only this skill. Do not update unrelated skills. If this install has no tracked source, install the current repository version with:

```sh
npx --yes skills@latest add hapyco/website-audit --skill website-audit --agent codex --global --yes
```

After an update, read the updated SKILL.md and required references before continuing. Keep client reports outside the skill folder. Preserve local skill edits before replacement; move them to the source repository. If access or network failure prevents the check, state that the update check failed and use the installed version if the audit can proceed. Never claim that the skill is current after a failed check.

## Intake

Start with the domain and any supplied business details. Optional fields: contact name, contact email, business description, target market, primary conversion, competitors, current platform, and report folder. Use the public site to fill gaps. Label inferred details. Ask only if a missing detail changes the audit. A missing email must not block research.

Example:

> Use $website-audit for https://example.com. Contact: Jane Smith, jane@example.com. Business: local home services. Market: Houston. Goal: booked estimates. Create the HTML audit and four-page A4 PDF.

Do not copy example client details into a new report. Keep the contact email in the private intake record unless it helps the client report. Creation does not authorize emailing the prospect, changing sharing permissions, editing their site, submitting their forms, or starting recurring paid checks.

## Research

1. Read [the audit rubric](references/audit-rubric.md). Open the homepage and representative service, contact, and conversion pages. Follow robots.txt. Inspect linked sitemaps recursively. Record redirects, HTTP status, metadata, canonical, headings, schema, links, forms, and scripts. Use a bounded same-origin crawl; default to 100 HTML URLs at low concurrency. Record limits and blocked URLs. Stop at login, payment, or personal-data collection.
2. Capture desktop screenshots at exactly 1280 CSS px wide and mobile screenshots at exactly 390 CSS px wide. Default viewport heights are 720 px and 844 px respectively; increase height only when the evidence needs it. Save the complete viewport capture. Keep the full height of each saved image visible in the report; preserve its aspect ratio and do not crop it to fit a fixed frame. Inspect 360, 390, 768, and 1440 CSS-pixel widths where tools permit. Open navigation and check the primary CTA without submitting anything. Check visible phone text against its tel link. Confirm defects in the rendered page, not only source HTML. Complete [the Design & UX review](references/design-audit.md): accessibility, grids, blocks, buttons, typography, sizing, spacing, padding, contrast and user-journey errors. Present the material findings in one combined client section.
3. Measure homepage performance on mobile and desktop with PageSpeed Insights or Lighthouse. Also measure one main service or paid landing page when it has a different template. Save raw results, URL, timestamp, version, device, and throttling. Prefer three successful runs per device and report the median. If only one run succeeds, label it a single lab run. Never turn a failed run into a score. Keep CrUX field data separate; lab TBT is not field INP.
4. Verify business identity and market. Use Google Business Profile evidence when eligible. With OpenSEO, list projects, then query the prospect explicitly; do not overwrite Hapy's project context or save prospect tracking there. A claimed profile is not proof of ownership access. Retain the place ID or CID and public Maps URL.
5. Choose two competitors that serve the same customer or location. Read their own pages and compare equivalent visible features. Explain why each was selected. Do not call them ranking leaders without dated, localized SERP evidence.
6. Inspect AI search readiness separately from observed AI answers. If available, sample 2-3 neutral buyer questions with country and engine recorded. Save exact prompts, answers, citations, and dates. An API answer is an API sample, not a consumer ChatGPT rank or market share. If unavailable, say that direct visibility was not measured. Do not seed the prospect's name into a discovery prompt. Do not configure paid tracking. Follow tool-specific spending requirements.
7. Run [Google Lighthouse Agentic Browsing](references/agent-readiness.md) on the homepage. Keep agent usability separate from AI answer visibility. Preserve each check outcome and unsupported or blocked checks.
8. Maintain a private evidence record: finding ID, area, URL, time, observation, raw artifact or screenshot, scope, confidence, business effect, action, effort, and owner. Recheck any high-priority claim before export.

If a tool fails, try one reasonable alternative. Report remaining gaps. Do not turn missing access into a negative finding. Use current primary documentation for platform rules and technical thresholds.

## Verify and quantify findings

Complete the checks before writing client findings. Follow sitemap URLs and internal HTML links until the public crawl queue is empty or a stated crawl limit is reached. Reconcile unique canonical pages, successful URL variants, archives, redirects and broken destinations. Report the count found and its composition. Do not stop at a sitemap count when the public pages can be checked. Keep private, orphan and access limits in the evidence record; include a client limit only when it changes interpretation.

Give affected counts and denominators for SEO, zoom settings and header findings. Name the actual control or header. For contrast, inspect the affected rendered control, record its colors and font size, and show the measured ratio and relevant reference. For responsiveness, record page, widths, overflow and menu behavior. Keep automated sample counts separate from whole-site counts.

Use direct finding headings and concrete evidence. For example: "9 pages lack meta descriptions", "9 distinct pages across 10 working URLs", or "Booking-button contrast: 3.29:1; reference 4.5:1". State the observed business consequence where useful. Avoid filler such as "search information is limited", "some controls may be harder to read", or repeated generic audit disclaimers. Keep genuine uncertainty specific. Do not remove an audit area because its current copy is weak; finish its checks and improve the finding.

## Decide

Rank findings by business effect. A broken contact path normally comes before cosmetic or metadata work. Use **Priority finding**, **Other finding**, **Working well**, **Not measured**, and **Not applicable**. Keep confidence separate from priority. Do not invent tool scores or revenue loss. Include the requested Hapy assessment out of 10 as an editorial judgment. Record its evidence and category ratings privately; keep its editorial basis in private notes and its accessible label, separate from Lighthouse results. Never copy a prior prospect's rating.

For each leading finding, give evidence and its likely business effect. Do not assign implementation tasks to the prospect or use per-finding Action blocks. Keep remediation steps, effort, and owners in the private evidence record. Use a separate, short closing to explain how Hapy can handle the work and invite a scoping discussion. Mark forecasts and service proposals as such. Retain the client's working features and proven search assets. Request analytics and Search Console access only for the next phase; public research must not imply access to traffic, leads, indexing totals, or revenue.

Read [the offer context](references/offer-context.md) before recommending migration. Choose one outcome: repair the current site, run a limited Astro pilot, or scope a migration. State what evidence would change the decision. A faster framework does not repair a missing form, invalid offer, or weak local profile by itself.

## Produce in HTML and PDF

HTML/CSS is the default authoring format. Deliver one self-contained HTML file with four A4 portrait pages and its verified PDF export. Use [the HTML reference](references/html-reference.md) and [the report specification](references/report-spec.md). Hapy fonts, logos, CSS tokens, HTML template and render/export scripts are bundled in this skill; no website checkout is required.

Follow the business story: enquiry and contact; Design & UX and agent readiness; speed, SEO, sitemap and security; local visibility, competitors and where Hapy can help. Put screenshots beside their findings. Lead chart sections with the main finding. Keep the body readable and the content breathable. Use HTML tables and CSS or SVG charts from saved measurements. Never use generated images for audit evidence.

Keep text editable in the HTML source. Embed fonts, logo and screenshots as data URIs so the report opens offline as one file. Keep the research record separate; do not embed private evidence JSON or intake email. Omit visible source lists and numbered citations. Keep short sampling limits. Use the supplied theme without copying website navigation or unrelated marketing content.

Use 210 x 297 mm page containers and @page A4 with zero outer print margins. Keep content inside each page with safe inner margins and explicit page breaks. Wait for fonts and images before PDF export. Check fit, page count and A4 dimensions; render and inspect all four PDF pages. Fix layout rather than hide overflowing content. Browser Print / Save PDF must use background graphics, 100 percent scale and no browser headers/footers. Google Slides and Canva are historical alternatives; use them only when requested.

Keep skill files in the global skills folder. Keep reports and evidence under ~/Documents/Codex/audits/ unless the user specifies another location. Do not store client artifacts in website worktrees. Do not run website builds or unrelated tests for an audit. Deliver the HTML and PDF and the most important finding with any material coverage limits. Apply reusable review corrections to this global skill.

Use plain report headings, such as "[Business] website audit". Avoid slogans, dramatic contrasts or sales hooks. On the opening page, omit the redundant section label, keep all page titles at 32 CSS px, place the bold numerical assessment alone to its right, and keep the top-right audit/domain header on one line.

Use descriptive titles on all pages: "[Business] website audit", "Design and usability", "Performance and technical health", and "Local visibility and competitors". Adapt them when the report content changes. Avoid paired slogans or dramatic claims.

Every audit booking CTA must use a UTM-tagged link. Use `{{BOOKING_URL}}` in the HTML body or CTA template so the renderer adds `utm_source=website-audit`, `utm_medium=report`, `utm_campaign=website-audit`, and `utm_content` equal to the prospect's normalized public domain. Preserve the booking destination, existing query parameters and fragment. Do not put contact names, email addresses or other private intake data in UTMs. Verify the final HTML booking link has these parameters. Keep the same link in a requested PDF export. These tags identify audit traffic; they do not prove that destination analytics or booking attribution is configured.
