# Research Paper - LaTeX Template

This directory contains the LaTeX source for your CPSC-298 research paper.

## File Structure

```
paper/
├── main.tex                    # Main document file
├── references.bib              # Bibliography (BibTeX format)
├── sections/                   # Individual sections
│   ├── abstract.tex
│   ├── introduction.tex
│   ├── related-work.tex
│   ├── methodology.tex
│   ├── results.tex
│   ├── discussion.tex
│   ├── conclusion.tex
│   └── appendix-AI-usage.tex
└── figures/                    # Place your figures here
```

## Compiling the Paper

### Option 1: Overleaf (Recommended for beginners)

1. Go to [Overleaf](https://www.overleaf.com/)
2. Create a new project → Upload Project
3. Upload all files from this `paper/` directory
4. The PDF will compile automatically
5. To download: Menu → PDF (or Source for all files)

### Option 2: Local Compilation

**Requirements:**
- A LaTeX distribution installed (e.g., TeX Live, MiKTeX, MacTeX)
- `pdflatex` and `bibtex` commands available

**Steps:**

```bash
cd paper/

# First compilation
pdflatex main.tex

# Generate bibliography
bibtex main

# Two more compilations for cross-references
pdflatex main.tex
pdflatex main.tex

# View the PDF
open main.pdf  # macOS
# or
xdg-open main.pdf  # Linux
# or
start main.pdf  # Windows
```

### Option 3: Using latexmk (if available)

```bash
cd paper/
latexmk -pdf main.tex
```

This automatically handles multiple compilations and bibliography.

## Editing Your Paper

1. **Edit the section files** in `sections/` directory, not `main.tex`
2. **Add references** to `references.bib` 
   - Get BibTeX entries from Google Scholar (click "Cite" → "BibTeX")
   - Cite in text using `\cite{key}` where `key` is the BibTeX entry name
3. **Add figures** to `figures/` directory
   - Reference in text: `\includegraphics{figures/your-figure.pdf}`
   - Supported formats: PDF, PNG, JPG
4. **Update author info** in `main.tex`

## Common Issues

**Problem:** Bibliography not showing
- **Solution:** Make sure to run bibtex, then pdflatex twice more

**Problem:** Figure not found
- **Solution:** Check that the file is in `figures/` and the path is correct

**Problem:** Undefined references
- **Solution:** Compile multiple times (LaTeX needs multiple passes)

**Problem:** Package not found
- **Solution:** Install missing packages using your LaTeX distribution's package manager

## Tips

- **Compile frequently** to catch errors early
- **Use comments** (%) to document your LaTeX code
- **Version control**: Commit often, especially before major changes
- **Backup**: Keep copies on multiple devices or use Overleaf cloud sync
- **Learn by example**: Look at the analyzed paper's structure

## Getting Help

- LaTeX errors: [TeX StackExchange](https://tex.stackexchange.com/)
- Overleaf: [Documentation](https://www.overleaf.com/learn)
- Templates: [Overleaf Templates](https://www.overleaf.com/latex/templates)
- ACM formatting: [ACM LaTeX Guide](https://www.acm.org/publications/proceedings-template)

## Resources

- [LaTeX Wikibook](https://en.wikibooks.org/wiki/LaTeX) - Comprehensive guide
- [Detexify](http://detexify.kirelabs.org/classify.html) - Draw symbols to find LaTeX commands
- [Tables Generator](https://www.tablesgenerator.com/) - Generate LaTeX tables visually

