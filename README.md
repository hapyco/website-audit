# Website audit

A Codex skill for Hapy Co's free prospect audits. Give it a domain and business details. It reviews the public site and creates one self-contained HTML file with four A4 pages and a PDF export.

The package includes Hapy fonts, logos, Hamid's portrait, CSS, HTML templates, and rendering scripts. It does not require the Hapy website repository.

## Install for Codex

Install Node.js 20 or newer. You need access to this private GitHub repository. If you use GitHub CLI, sign in with `gh auth login` first.

Run:

```sh
npx skills@latest add hapyco/website-audit --skill website-audit --agent codex --global
```

For installation without prompts:

```sh
npx --yes skills@latest add hapyco/website-audit --skill website-audit --agent codex --global --yes
```

The global flag makes the skill available across projects. Start a new Codex chat after installation so Codex can load it.

## Use in Codex

```text
Use $website-audit for https://example.com.
Contact: Jane Smith.
Business: local home services.
Market: Houston.
Goal: booked estimates.
Create the HTML audit and four-page A4 PDF.
```

The domain is required. Business details are optional. The skill can read the public site to fill gaps.

It covers SEO, Google Business Profile, performance, sitemap structure, AI visibility, security, public page count, regional insights, competitors, responsiveness, design and UX, and Google Lighthouse Agentic Browsing. Findings must come from checked evidence. The report presents findings and business effects, with a short Hapy service close.

## Updates

The skill must check for updates before every use. It runs:

```sh
npx --yes skills@latest update website-audit --global --yes
```

This checks the installed source and applies updates to `website-audit` only. After an update, Codex must read the updated instructions before it continues. If the source is not tracked, run the installation command again. A failed check must be reported; it must not be described as up to date.

Keep reports and evidence outside the installed skill. Put reusable changes in this repository so an update does not replace local work.

CLI reference: [vercel-labs/skills](https://github.com/vercel-labs/skills).

## Output and design

- One portable HTML file with embedded fonts, logo, portrait, and evidence images.
- Four A4 portrait pages, 210 x 297 mm.
- Plain 32 px page headings, readable body text, tables, and measured charts.
- Desktop evidence at 1280 px wide; mobile evidence at 390 px wide. Show the full images without cropping.
- Orange marks negative findings; teal marks positive findings. Flat cards use a 3 px status line inset 8 px.
- An editorial assessment out of 10, with its evidence and ratings kept in private notes.
- Source records stay in private evidence. The client report omits source lists.

Reports and client evidence belong under `~/Documents/Codex/audits/`, or another folder you specify. Do not place them in a website worktree. If you ask for HTML review only, the skill must leave the PDF unchanged until you request an export.

## Rendering tools

Codex can use its bundled Python, Node, Chrome, and PDF tools. On another machine, install Python 3, Node.js 20 or newer, and Google Chrome. Install the Node dependency from a clone of this repository:

```sh
npm install
```

Build the HTML from approved report data:

```sh
python3 scripts/render_audit.py --data /absolute/path/audit-data.json --output /absolute/path/audit.html
```

Export the HTML to PDF:

```sh
node scripts/export_pdf.cjs /absolute/path/audit.html /absolute/path/audit.pdf
```

Set `CHROME_PATH` if Chrome is not at the default macOS path. The export script uses `puppeteer-core`; if the runtime supplies it elsewhere, set `NODE_PATH` to that package folder.

The JSON needs `client`, `contact`, `domain`, `date`, `pages`, and `images`. Each page has `section`, `title`, optional `lede`, and approved HTML `body`. The optional `assessment` object has `value` and `maximum`. Image placeholders use `{{IMG_NAME}}` with a matching local path in `images`. The bundled CTA uses `{{ASSET_HAMID}}`. See [the HTML reference](references/html-reference.md).

Wait for fonts and images before export. Check page fit, confirm exactly four A4 pages, and inspect every rendered PDF page. Do not hide content to make a page fit.

## Included files

- `SKILL.md`: research, verification, writing, update checks, and output rules.
- `references/`: audit rubric and detailed research and report guidance.
- `assets/`: fonts, font licenses, logos, portrait, and CSS.
- `templates/`: HTML report shell and portrait CTA.
- `scripts/`: self-contained HTML builder and Chrome PDF exporter.
- `agents/openai.yaml`: Codex skill metadata.

The fonts include their Open Font License files. Hapy's logo and portrait remain Hapy brand assets.
