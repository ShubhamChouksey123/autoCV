# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A single-file LaTeX resume for Shubham Chouksey, based on the [autoCV](https://github.com/jitinnair1/autoCV) template. The entire CV lives in `cv.tex`; everything else is build tooling and web publishing glue. Editing the resume means editing `cv.tex` — there is no application code.

## Commands

- `make` — compile `cv.tex` to `cv.pdf` via `latexmk -pdf` (requires a local LaTeX/TeX Live install).
- `make clean` — remove intermediate build artifacts (`.aux`, `.bbl`, `.log`, etc.).
- `make distclean` — `clean` plus removing `cv.pdf`.

There are no tests or linters. Validate changes by compiling and visually inspecting the PDF.

## Architecture

- **`cv.tex`** — the resume. The first ~160 lines are preamble (packages, colors, custom commands); content starts at `\begin{document}`. Two custom macros drive all section layout:
  - `\customHeading{Title}` — a section header with a horizontal rule.
  - `\customSubHeading{a}{b}{c}{d}` — a 4-column row (e.g. role / company / location / dates) used in Work Experience.
  Body content (bullets, skills, projects) uses `tabularx` + `itemize` blocks. Match the existing structure when adding entries rather than introducing new layout patterns.
- **`citations.bib`** — BibTeX entries for a publications section via `biblatex` (`authoryear` style). Currently contains placeholder/dummy entries; the publications section is not actively rendered in the document body.
- **`index.html` / `CNAME`** — web publishing. `index.html` is a JS redirect to `./cv.pdf`; `CNAME` configures the custom domain for GitHub Pages.

## Build & publish pipeline (`.github/workflows/build.yml`)

On every push, three sequential jobs run:
1. **build** — compiles `cv` (set by the `FILE` env var) with `dante-ev/latex-action`, uploads the PDF as an artifact.
2. **deploy** — force-pushes the PDF to an orphan `build` branch via `peaceiris/actions-gh-pages` (this is the GitHub Pages source).
3. **copy-index-to-build** — copies `index.html` and `CNAME` into the `build` branch so the published site redirects to the latest PDF.

The committed `shubham_chouksey.pdf` is a separately exported copy and is **not** the build output — the pipeline produces `cv.pdf`. If you rename the LaTeX source, update the `FILE` env var in the workflow to match.
