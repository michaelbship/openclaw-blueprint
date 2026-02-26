---
name: md-to-pdf
description: |
  Convert Markdown files to professionally formatted PDFs.
  Use when user asks to convert markdown to PDF or needs formal documents.
---

# md-to-pdf

Convert Markdown files to professionally formatted PDFs.

## Tool

`pandoc` with LaTeX backend. Lightweight and reliable.

## Basic Usage

```bash
# Convert single file
pandoc document.md -o document.pdf
```

## With Options

```bash
# Custom margins
pandoc document.md -o document.pdf -V geometry:margin=1in

# Letter size (default is A4)
pandoc document.md -o document.pdf -V papersize=letter
```

## Batch Convert

```bash
# All markdown files in directory
for f in *.md; do pandoc "$f" -o "${f%.md}.pdf"; done
```

## Workflow

1. Create/edit markdown file in appropriate location
2. Run `pandoc <file>.md -o <file>.pdf`
3. PDF appears in same directory

## Requirements

Install on VPS if not present:
- `pandoc` (markdown processor)
- `texlive-latex-extra` (PDF generation via LaTeX)

```bash
apt-get install -y pandoc texlive-latex-extra
```

## Notes

- Pandoc is lightweight and reliable for document conversion
- For simple documents, pandoc is preferred over heavier tools
