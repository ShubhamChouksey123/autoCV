#!/usr/bin/env python3
"""Render a plain cover-letter.md (paragraphs of prose, blank-line separated) to a PDF
using pdflatex, so the repo doesn't need a new dependency (pandoc/wkhtmltopdf) beyond
the existing LaTeX toolchain. Usage: md_to_pdf.py <input.md> <output.pdf>
"""
import re
import subprocess
import sys
import tempfile
import shutil
import os

def normalize_unicode(text):
    replacements = [
        ('—', '---'),  # em dash
        ('–', '--'),   # en dash
        ('‘', "`"), ('’', "'"),   # smart single quotes
        ('“', "``"), ('”', "''"), # smart double quotes
        ('…', '...'),  # ellipsis
        (' ', ' '),    # nbsp
    ]
    for a, b in replacements:
        text = text.replace(a, b)
    return text

def escape_latex(text):
    text = normalize_unicode(text)
    replacements = [
        ('\\', r'\textbackslash{}'),
        ('&', r'\&'),
        ('%', r'\%'),
        ('$', r'\$'),
        ('#', r'\#'),
        ('_', r'\_'),
        ('{', r'\{'),
        ('}', r'\}'),
        ('~', r'$\sim$'),
        ('^', r'\textasciicircum{}'),
    ]
    for a, b in replacements:
        text = text.replace(a, b)
    return text

def linkify(text):
    url_re = re.compile(r'(https?://[^\s]+|[\w.+-]+@[\w.-]+\.\w+)')
    parts = []
    last = 0
    for m in url_re.finditer(text):
        parts.append(escape_latex(text[last:m.start()]))
        url = m.group(0).rstrip('.,)')
        trail = m.group(0)[len(url):]
        href = url if url.startswith('http') else f'mailto:{url}'
        parts.append(r'\href{%s}{%s}' % (href, escape_latex(url)) + escape_latex(trail))
        last = m.end()
    parts.append(escape_latex(text[last:]))
    return ''.join(parts)

def main():
    src, dst = sys.argv[1], sys.argv[2]
    with open(src) as f:
        raw = f.read()

    paragraphs = [p.strip() for p in raw.split('\n\n') if p.strip()]
    rendered = []
    for p in paragraphs:
        lines = [linkify(line) for line in p.split('\n')]
        rendered.append(r'\\'.join(lines))
    body = '\n\n'.join(rendered)

    tex = r"""
\documentclass[11pt]{article}
\usepackage[a4paper,margin=1in]{geometry}
\usepackage{parskip}
\usepackage[unicode]{hyperref}
\hypersetup{colorlinks=true, urlcolor=blue, linkcolor=blue}
\usepackage[utf8]{inputenc}
\pagestyle{empty}
\begin{document}
\sloppy
""" + body + r"""
\end{document}
"""

    with tempfile.TemporaryDirectory() as tmp:
        tex_path = os.path.join(tmp, 'letter.tex')
        with open(tex_path, 'w') as f:
            f.write(tex)
        result = subprocess.run(
            ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'letter.tex'],
            cwd=tmp, capture_output=True, text=True
        )
        pdf_path = os.path.join(tmp, 'letter.pdf')
        if not os.path.exists(pdf_path):
            print(result.stdout[-3000:])
            print(result.stderr[-3000:])
            sys.exit(1)
        shutil.copy(pdf_path, dst)
    print(f"Wrote {dst}")

if __name__ == '__main__':
    main()
