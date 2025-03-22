# Alexandre DO-O ALMEIDA — CV

This repository contains the LaTeX source for my one-page résumé.

## 📄 Preview

![Preview](image.png)

## 🧰 Prerequisites

Make sure you have a working LaTeX distribution. Recommended:

- [TeX Live](https://www.tug.org/texlive/) (Linux/macOS)
- [MikTeX](https://miktex.org/) (Windows)
- [Overleaf](https://overleaf.com) (alternative online editor)

Fonts and packages needed:

- `noto` (Noto Sans)
- `fontawesome`
- `tikz`, `titlesec`, `xcolor`, `geometry`, `hyperref`, etc.

Make sure your LaTeX install supports `fontspec` (i.e. use `xelatex` or `lualatex`, **not** `pdflatex`).

## 🚀 Build Instructions

In the root directory:

```bash
xelatex cv.tex
```
