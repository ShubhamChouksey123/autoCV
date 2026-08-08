# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A LaTeX resume repo based on the [autoCV](https://github.com/jitinnair1/autoCV) template, hosting **multiple people's CVs** under `people/<person>/`. There is no application code — editing a CV means editing its `.tex` file directly.

- `people/shubham-chouksey/cv.tex` — Shubham Chouksey's primary resume, and the **default** (published via the build pipeline; this is the "official" `DIR`/`FILE` in CI).
- `people/shubham-chouksey/cv-long.tex` — a more verbose/expanded variant of the same resume with the same structure, longer bullet points, and additional skill call-outs. Keep it structurally in sync with `cv.tex` when the layout changes; content can diverge.
- `people/nikhlesh-sahu/cv.tex` — an unrelated CV for Nikhlesh Kumar Sahu (a physiotherapist), built from source material in `people/nikhlesh-sahu/certificates/` (scanned training/registration certificates). When updating it, treat those certificates as the source of truth for credentials, dates, and registration numbers rather than guessing.

All CV files share the same preamble/macro structure (see Architecture below) — when adding a new person's CV, create `people/<new-person>/cv.tex` by copying an existing file rather than starting from the template preamble.

Each person directory also has an `info.md` (e.g. `people/shubham-chouksey/info.md`) — check it before editing that person's CV. For Shubham it holds: contact info/links, a "Work Experience" section kept **in sync with `cv.tex`'s trimmed bullets** (update both together when either changes), and a "Keyword shortlist for cv.tex" checklist (ATS/recruiter keywords, `[x]` = already present in `cv.tex`, `[ ]` = candidate) used to track and vet resume keyword additions against product-company screening — don't add a keyword there or to the CV that isn't actually backed by real experience.

`tmp.md` (repo root, gitignored) is the user's scratch pad for ad hoc instructions/facts pasted in before being turned into a request — not part of the documented repo state, just ephemeral working notes.

`mcp-connect.md` (repo root) has working Cloud ID / connection details for the New Relic Confluence MCP tools, used to research facts (e.g. internal architecture docs) when writing CV content — read it if a Confluence tool call fails with a cloud-ID or permission error.

## Commands

The `Makefile` builds `people/$(PERSON)/$(NAME).tex`, defaulting to `PERSON=shubham-chouksey NAME=cv`:

- `make` — compile Shubham's `cv.tex` to `cv.pdf` via `latexmk -pdf`.
- `make NAME=cv-long` — compile Shubham's long variant instead.
- `make PERSON=nikhlesh-sahu` — compile Nikhlesh's `cv.tex` instead.
- `make clean` — remove intermediate build artifacts (`.aux`, `.bbl`, `.log`, etc.) for the selected `PERSON`/`NAME`.
- `make distclean` — `clean` plus removing the compiled PDF.

There are no tests or linters. Validate changes by compiling and visually inspecting the PDF — since there's no way to view a rendered PDF directly in this environment, use `pdftotext -layout <pdf> -` to sanity-check content/ordering and `pdftoppm -png -r 150 <pdf> /tmp/preview` (both from the `poppler` package; `brew install poppler` if missing) then read the resulting PNG(s) to visually verify layout. This is also how to check page count (`pdftotext`'s sibling tool `pdfinfo`, or just count generated `-N.png` files) and check for text-wrapping/overflow.

If `pdflatex`/`latexmk` errors on a missing package (e.g. `biblatex.sty`, `logreq.sty`), install it into the user tree without sudo: `tlmgr init-usertree` once, then `tlmgr --usermode install <package>`. The `biber` binary (biblatex's backend, needed at compile time even though no CV actually renders a bibliography) can't go in a user TeX tree since it's a compiled binary, not a package — install it via `brew install biber` instead.

## Design constraint: `cv.tex` must stay exactly 1 page

`cv.tex` (Shubham's default/CI-published resume) is deliberately kept to a single page; `cv-long.tex` is where in-depth/verbose content belongs instead. When editing `cv.tex`, after any content addition, verify page count stays at 1 (see the `pdftotext`/`pdftoppm` workflow above) and trim if it overflows. Things learned the hard way while doing this:
- **A `\begin{minipage}`-wrapped block cannot split across a page break** — if content overflows by even one line, the *entire* minipage jumps to page 2, not just the overflowing part. The Awards & Achievements section used to be wrapped in a superfluous minipage for exactly this reason and was fixed by removing it (it's not part of a multi-column layout, so it doesn't need one) so its `itemize` can flow/break normally. Only wrap Work Experience bullets in a minipage where the existing per-role pattern already does so.
- A `\customSubHeading` title longer than the other three columns (e.g. "Senior Software Engineer") can wrap to two lines because the four columns are equal-width `X` columns. Force it onto one line with `\customSubHeading{\mbox{Title}}` rather than reworking the column widths.
- When trimming to reclaim a line: shortening prose only helps if it actually reduces the *line count* of that paragraph — a `\hfill`-separated link (as in Projects) often still wraps to the same number of lines even after shortening the body text, because the link needs its own line regardless. Check the rendered output, not just the source diff.

## Architecture

- Every CV file has the same shape: an MIT-licensed preamble (~160 lines: packages, colors, custom commands), then content starting at `\begin{document}`. Two custom macros drive all section layout:
  - `\customHeading{Title}` — a section header with a horizontal rule.
  - `\customSubHeading{a}{b}{c}{d}` — a 4-column row (e.g. role / company / location / dates) used in Work Experience.
  Body content (bullets, skills, projects) uses `tabularx` + `itemize` blocks. Match the existing structure when adding entries rather than introducing new layout patterns.
- **`citations.bib`** — shared BibTeX entries (at repo root) for a publications section via `biblatex` (`authoryear` style). Currently contains placeholder/dummy entries; no CV actually includes it (`biblatex` is loaded as a package but never `\addbibresource`'d), so the publications section is not rendered.
- **`people/nikhlesh-sahu/certificates/`** — scanned/exported certificates (training, registration) used as primary-source input when writing or updating that person's CV. This directory is gitignored (`people/*/certificates/`) — treat it as local reference material, not something to commit.
- **`index.html` / `CNAME`** (repo root) — web publishing for the default (Shubham) pipeline only. `index.html` is a JS redirect to `./cv.pdf`; `CNAME` configures the custom domain for GitHub Pages.

## Build & publish pipeline (`.github/workflows/build.yml`)

On every push, three sequential jobs run, scoped to `DIR`/`FILE` env vars (currently `people/shubham-chouksey` / `cv`):
1. **build** — compiles `cv.tex` with `dante-ev/latex-action`, uploads the PDF as an artifact.
2. **deploy** — force-pushes the PDF to an orphan `build` branch via `peaceiris/actions-gh-pages` (this is the GitHub Pages source).
3. **copy-index-to-build** — copies `index.html` and `CNAME` into the `build` branch so the published site redirects to the latest PDF.

This pipeline only builds and publishes Shubham's `cv.tex`. Other people's CVs (`cv-long.tex`, `nikhlesh-sahu/cv.tex`) are not part of CI/CD — compile and export those manually with `make PERSON=<person> NAME=<file>` when a PDF is needed.

Exported PDF copies (e.g. `people/shubham-chouksey/shubham_chouksey.pdf`) are separately exported files and are **not** the build output — the pipeline always produces `cv.pdf`. If you add a second person to CI publishing, add a matching `DIR`/`FILE` pair and a parallel job (or matrix) rather than overwriting the existing one.
