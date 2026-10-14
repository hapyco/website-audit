# HTML audit package

The default changed to HTML/CSS on 14 October 2026. All four A4 pages live in one HTML file. Google Slides is retained as historical evidence only.

## Bundled assets

- assets/heading.woff2: Funnel Display Light, for headings.
- assets/body.woff2: Google Sans Flex 72pt Regular, for body.
- assets/Funnel-OFL.txt and GoogleSans-OFL.txt: font licenses; retain when sharing the package.
- assets/hapy-logo.svg and hapy-logo.png: Hapy logo; SVG is embedded inline for browser PDF output; PNG is included as a fallback.
- assets/audit.css: brand tokens, A4 layout, tables, charts and print rules.
- templates/audit.html: single-file shell with print button.
- scripts/render_audit.py: Python standard library builder, embeds fonts and images.
- scripts/export_pdf.cjs: headless Chrome PDF export and page fit/image checks. Requires Node and puppeteer-core. Set NODE_PATH when supplied by the host and CHROME_PATH if Chrome is elsewhere. It does not need the website repo.

Palette: paper #F1F0EC, ink #261201, teal #006561, pale green #CFD6C5, peach #F2DBCC, blue #D4E4F0 and lime #DEE884. Default screen canvas is fixed A4, not a fluid website; horizontal scrolling on a small screen preserves print geometry.

## Report data and build

Supply JSON with client, contact, domain, date, pages, and images. Each page has section (plain text), title (approved HTML), optional lede (plain text), and body (approved HTML). Images is a mapping from names to local evidence paths; body slots use {{IMG_NAME}}. The builder escapes metadata. Title and body accept trusted author-written markup only; never insert raw scraped HTML. Client files are external to the skill package. Do not bundle the example client's details or evidence.

Run python3 scripts/render_audit.py --data /absolute/client.json --output /absolute/audit.html, then node scripts/export_pdf.cjs /absolute/audit.html /absolute/audit.pdf. Use absolute paths. Run the scripts from their package folder or use their absolute paths.

## Verification

Require 4 pages, A4 portrait, no page overflow or missing images. Confirm a safe gap before each footer. Render the final PDF and inspect all pages, including repeated logos and running headers. Preserve screenshot aspect ratios. Use CSS bars or SVG with common zero-based scales and visible numerical labels. Never invent metrics or a composite score. Keep verified copy, chart values, sample limits and public page counts intact.

Keep generous inner margins, short parallel columns, readable body copy and consistent headers/footers. Retain all twelve audit areas. Use the complete research rubric for checks; the report shows material findings, not separate checklist rows for every design property.

## Opening and editorial assessment

Use a factual title, 32 CSS px, with no opening section label. The top-right audit/domain text stays on one line. Optional assessment data contains value and maximum; the first-page title row places its block on the right. Show only the bold numeric fraction (for example 4/10). Keep Hapy assessment in the accessible label and its editorial basis in private data. For the requested out-of-10 assessment, rate contact path, navigation, design and usability, performance, and local trust from 0 to 2 each: material obstacle, mixed findings, or working well. Record the ratings and evidence in private report data. This is editorial judgment across those categories, not a validated whole-site health measure. Do not average Lighthouse scores into it or reuse an example rating for another prospect.

The bundled score-bold.woff2 uses Funnel Display Bold for the numerical assessment; the existing Funnel OFL license applies.

Score styling: values below 8/10 use orange #B84B00 on pale peach #F2DBCC. Values of 8/10 or more keep teal. Normalize by the maximum when another scale is supplied. The card uses 8 px vertical and 10 px horizontal padding; the score uses 54 px bold type with a 34 px denominator.

All page titles use 32 CSS px. Use plain descriptive titles for the audit overview, design and usability, performance and technical health, and local visibility and competitors. Do not use paired slogans.

## Screenshot dimensions and display

Capture desktop evidence at exactly 1280 CSS px wide and mobile evidence at exactly 390 CSS px wide. Defaults: 1280 x 720 and 390 x 844. Capture the relevant viewport after navigation or scrolling; a viewport screenshot is not a full-page website capture. Do not crop the saved image in the report. For a desktop/mobile pair, use a common display height (260 CSS px in this template), natural aspect ratios, auto widths, object-fit contain and separate captions. Both full image bounds must be visible. Change the shared display height or rearrange content if needed for A4 fit; never use cover, stretch images, or clip overflow. Keep responsive testing at 360, 390, 768 and 1440 separate from these standard evidence widths.

## Finding status and closing CTA

Use orange #FF7420 for negative finding borders and #B84B00 for readable orange text. Negative finding numbers use orange. Put short parallel design defects in flat white cards with an inset orange line and no shadow. A block led by an accessibility defect uses pale peach and an orange border, even when its body also records working controls. Use text headings as well as color to identify the finding. Keep positive trust blocks teal/green.

Keep the client Lighthouse note short: version, run count, and lab-versus-field distinction. Device settings and full diagnostics remain in private evidence.

Use templates/cta.html for the report close, adapted from Hapy's default CTA. Hamid's bundled portrait is on the left; the right column holds the heading, short copy and orange pill button. The asset token {{ASSET_HAMID}} is embedded by the renderer. Keep the service scope specific and migration conditional. The report does not embed a booking widget.

Use the same flat card style for the parallel SEO and page-inventory findings. The orange line is 3 px wide and inset 8 px from the top, left and bottom; it is not a card border. Keep the portrait CTA background transparent.

Full-width zoom and review bands use the same 3 px line inset 8 px from top, left and bottom. Use orange for the negative zoom finding and teal for the positive review block. The Agentic Browsing section heading is 20 CSS px on screen and print. Remove the portrait CTA left padding so its image aligns with the content margin.

Keep the closing description short. Mention evolving web stacks and Hapy assessing whether a move to Astro suits the site, alongside the observed contact and performance work. Do not claim that a migration is automatically required or invent market-adoption statistics.

## Booking attribution

Use `{{BOOKING_URL}}` for every booking CTA. The renderer builds the URL from optional `booking_url` (default https://hapy.co/get-started/) and the prospect domain. It preserves other query parameters and the fragment, then sets utm_source=website-audit, utm_medium=report, utm_campaign=website-audit and utm_content=<public-domain>. Use the same URL in the HTML and PDF. Verify the rendered anchor, not only its visible label. Do not claim that analytics or a booking integration records the attribution unless that has been checked.
