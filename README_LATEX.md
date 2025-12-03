# GATE Mathematical Physics Study Guide - LaTeX Document

## Overview
This comprehensive LaTeX document covers all essential topics for GATE 2026 Mathematical Physics preparation:
- Vector Calculus (grad, div, curl, line/surface integrals)
- Complex Analysis (Cauchy theorem, residue calculus, contour integration)
- Differential Equations (Frobenius method, special functions)
- Linear Algebra (eigenvalues, diagonalization, Hermitian matrices)

## Compilation

### Requirements
You need a LaTeX distribution installed:
- **TeX Live** (Linux/Mac/Windows)
- **MiKTeX** (Windows)
- **MacTeX** (Mac)

### Required Packages
The document uses the following packages (usually included in standard distributions):
- `amsmath`, `amssymb`, `amsthm` - Mathematical symbols and environments
- `physics` - Physics-related commands
- `geometry` - Page layout
- `tikz`, `pgfplots` - Graphics (optional, for future diagrams)
- `hyperref` - Hyperlinks
- `enumitem` - List formatting
- `xcolor` - Colors
- `fancyhdr` - Headers/footers
- `tcolorbox` - Colored boxes
- `multicol` - Multiple columns

### Compilation Steps

1. **Basic compilation:**
   ```bash
   pdflatex gate_mathematical_physics_study_guide.tex
   ```

2. **For proper cross-references and table of contents (recommended):**
   ```bash
   pdflatex gate_mathematical_physics_study_guide.tex
   pdflatex gate_mathematical_physics_study_guide.tex
   ```
   (Run twice to resolve all references)

3. **If using BibTeX for references:**
   ```bash
   pdflatex gate_mathematical_physics_study_guide.tex
   bibtex gate_mathematical_physics_study_guide
   pdflatex gate_mathematical_physics_study_guide.tex
   pdflatex gate_mathematical_physics_study_guide.tex
   ```

### Online Compilation
If you don't have LaTeX installed locally, you can use:
- **Overleaf** (https://www.overleaf.com) - Upload the .tex file and compile online
- **ShareLaTeX** - Similar online LaTeX editor

## Document Structure

1. **Introduction** - Overview of topics
2. **Vector Calculus** - Complete coverage with examples
3. **Complex Analysis** - Detailed theory and applications
4. **Differential Equations** - Methods and special functions
5. **Linear Algebra** - Eigenvalues, diagonalization, Hermitian matrices
6. **Quick Reference** - Summary formulas
7. **Study Strategy** - Preparation plan

## Features

- **Color-coded boxes:**
  - Red boxes: Important concepts
  - Blue boxes: Key formulas
  - Green boxes: Worked examples

- **Comprehensive coverage:**
  - All fundamental concepts
  - Multiple worked examples
  - Practice problems
  - Physical interpretations

- **Well-organized:**
  - Clear section structure
  - Table of contents
  - Cross-references
  - Professional formatting

## Study Tips

1. Work through all examples step-by-step
2. Solve the practice problems at the end of each section
3. Focus on understanding physical interpretations
4. Master coordinate transformations
5. Practice previous GATE papers
6. Review the quick reference section regularly

## Customization

You can customize the document by:
- Adjusting margins in `\geometry{margin=1in}`
- Changing colors in the `tcolorbox` definitions
- Adding more examples or problems
- Modifying the study strategy section

## Notes

- The document is designed to be comprehensive - "leave no stone unturned"
- Mathematical Physics is emphasized as the foundation
- All topics are covered in great detail as requested
- The document is ready for 2026 GATE preparation

Good luck with your preparation!
