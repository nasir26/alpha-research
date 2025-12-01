# Makefile for Twistor Theory and Spin Networks Visualization Project
# =====================================================================

.PHONY: all latex latex-main latex-supplement clean clean-latex clean-manim \
        manim-preview manim-twistor manim-spin manim-combined manim-all \
        help install-deps test

# Default target
all: latex manim-preview

# =====================================================================
# Help
# =====================================================================

help:
	@echo "Twistor Theory and Spin Networks - Build System"
	@echo "==============================================="
	@echo ""
	@echo "LaTeX targets:"
	@echo "  make latex              - Compile all LaTeX documents"
	@echo "  make latex-main         - Compile main document only"
	@echo "  make latex-supplement   - Compile supplement only"
	@echo ""
	@echo "Manim targets:"
	@echo "  make manim-preview      - Render preview scenes (low quality, fast)"
	@echo "  make manim-twistor      - Render all twistor scenes (high quality)"
	@echo "  make manim-spin         - Render all spin network scenes (high quality)"
	@echo "  make manim-combined     - Render all combined scenes (high quality)"
	@echo "  make manim-all          - Render ALL scenes (high quality, ~2-4 hours)"
	@echo ""
	@echo "Utility targets:"
	@echo "  make install-deps       - Install Python dependencies"
	@echo "  make test               - Quick test of LaTeX and Manim setup"
	@echo "  make clean              - Clean all generated files"
	@echo "  make clean-latex        - Clean LaTeX auxiliary files only"
	@echo "  make clean-manim        - Clean Manim output only"
	@echo ""
	@echo "Combined targets:"
	@echo "  make all                - Compile LaTeX + preview scenes (default)"
	@echo "  make full-build         - Complete high-quality build (everything)"

# =====================================================================
# Installation
# =====================================================================

install-deps:
	@echo "Installing Python dependencies..."
	pip install -r requirements.txt
	@echo "Done! Verify with: manim --version"
	@echo ""
	@echo "Note: LaTeX must be installed separately"
	@echo "  Ubuntu/Debian: sudo apt install texlive-full"
	@echo "  macOS: brew install --cask mactex"

# =====================================================================
# LaTeX Compilation
# =====================================================================

latex: latex-main latex-supplement

latex-main:
	@echo "Compiling main document..."
	pdflatex twister_spin_networks.tex
	pdflatex twister_spin_networks.tex
	@echo "Generated: twister_spin_networks.pdf"

latex-supplement:
	@echo "Compiling mathematical supplement..."
	pdflatex mathematical_supplement.tex
	pdflatex mathematical_supplement.tex
	@echo "Generated: mathematical_supplement.pdf"

# =====================================================================
# Manim Rendering - Preview (Low Quality)
# =====================================================================

manim-preview:
	@echo "Rendering preview scenes (low quality)..."
	manim -ql twistor_visualization.py TwistorTheoryComplete
	manim -ql spin_network_visualization.py SpinNetworkComplete
	manim -ql combined_visualization.py FinalSynthesis
	@echo "Preview renders complete!"
	@echo "Output: media/videos/"

# =====================================================================
# Manim Rendering - High Quality
# =====================================================================

TWISTOR_SCENES = TwistorIntroduction ComplexProjectiveSpace IncidenceRelation \
                 SpinorDecomposition PenroseTransform AlphaBetaPlanes \
                 NullTwistors TwistorTheoryComplete

SPIN_SCENES = SpinNetworkIntroduction BasicSpinNetwork SU2Representations \
              IntertwinerVertex SixJSymbol WilsonLoop ThetaGraph \
              AreaQuantization TetrahedralNetwork SpinNetworkComplete

COMBINED_SCENES = TwistorSpinComparison SpinorBridge GeometricInterpretation \
                  QuantumGeometry UnifiedFramework FinalSynthesis

manim-twistor:
	@echo "Rendering twistor theory scenes (high quality)..."
	@for scene in $(TWISTOR_SCENES); do \
		echo "Rendering $$scene..."; \
		manim -pqh twistor_visualization.py $$scene; \
	done
	@echo "Twistor scenes complete!"

manim-spin:
	@echo "Rendering spin network scenes (high quality)..."
	@for scene in $(SPIN_SCENES); do \
		echo "Rendering $$scene..."; \
		manim -pqh spin_network_visualization.py $$scene; \
	done
	@echo "Spin network scenes complete!"

manim-combined:
	@echo "Rendering combined framework scenes (high quality)..."
	@for scene in $(COMBINED_SCENES); do \
		echo "Rendering $$scene..."; \
		manim -pqh combined_visualization.py $$scene; \
	done
	@echo "Combined scenes complete!"

manim-all: manim-twistor manim-spin manim-combined
	@echo ""
	@echo "=========================================="
	@echo "All scenes rendered successfully!"
	@echo "=========================================="
	@echo "Output location: media/videos/"
	@echo "Total scenes: 24"

# =====================================================================
# Full Build
# =====================================================================

full-build: latex manim-all
	@echo ""
	@echo "=========================================="
	@echo "FULL BUILD COMPLETE!"
	@echo "=========================================="
	@echo "LaTeX PDFs:"
	@echo "  - twister_spin_networks.pdf"
	@echo "  - mathematical_supplement.pdf"
	@echo ""
	@echo "Manim videos: media/videos/"
	@echo "  - 8 twistor scenes"
	@echo "  - 10 spin network scenes"
	@echo "  - 6 combined scenes"
	@echo "=========================================="

# =====================================================================
# Testing
# =====================================================================

test:
	@echo "Testing LaTeX installation..."
	@pdflatex --version > /dev/null 2>&1 && echo "✓ LaTeX found" || echo "✗ LaTeX not found"
	@echo ""
	@echo "Testing Python/Manim installation..."
	@python3 --version 2>&1 | head -n1
	@pip show manim > /dev/null 2>&1 && echo "✓ Manim installed" || echo "✗ Manim not installed"
	@echo ""
	@echo "Quick test render (this may take 10-30 seconds)..."
	@manim -ql --dry_run twistor_visualization.py TwistorIntroduction && \
		echo "✓ Manim test passed" || echo "✗ Manim test failed"

# =====================================================================
# Cleaning
# =====================================================================

clean: clean-latex clean-manim

clean-latex:
	@echo "Cleaning LaTeX auxiliary files..."
	rm -f *.aux *.log *.out *.toc *.synctex.gz *.fdb_latexmk *.fls
	@echo "LaTeX cleanup complete!"

clean-manim:
	@echo "Cleaning Manim output..."
	rm -rf media/
	@echo "Manim cleanup complete!"

clean-all: clean
	@echo "Cleaning PDFs..."
	rm -f *.pdf
	@echo "All generated files cleaned!"

# =====================================================================
# Additional Targets
# =====================================================================

# Generate static images instead of videos
manim-images:
	@echo "Generating static images..."
	@mkdir -p images
	@for scene in TwistorTheoryComplete SpinNetworkComplete FinalSynthesis; do \
		echo "Capturing $$scene..."; \
		manim -sqh --format=png twistor_visualization.py $$scene 2>/dev/null || true; \
		manim -sqh --format=png spin_network_visualization.py $$scene 2>/dev/null || true; \
		manim -sqh --format=png combined_visualization.py $$scene 2>/dev/null || true; \
	done
	@echo "Images saved to media/images/"

# Quick preview of specific scene (usage: make preview SCENE=SceneName FILE=filename)
preview:
	@if [ -z "$(SCENE)" ] || [ -z "$(FILE)" ]; then \
		echo "Usage: make preview SCENE=SceneName FILE=filename"; \
		echo "Example: make preview SCENE=ComplexProjectiveSpace FILE=twistor_visualization"; \
	else \
		manim -pql $(FILE).py $(SCENE); \
	fi

# Count total lines of code
stats:
	@echo "Project Statistics"
	@echo "=================="
	@echo "LaTeX files:"
	@wc -l *.tex
	@echo ""
	@echo "Python files:"
	@wc -l *_visualization.py
	@echo ""
	@echo "Documentation:"
	@wc -l *.md

# Validate Python syntax
validate:
	@echo "Validating Python syntax..."
	@python3 -m py_compile twistor_visualization.py
	@python3 -m py_compile spin_network_visualization.py
	@python3 -m py_compile combined_visualization.py
	@echo "✓ All Python files are syntactically correct"

# =====================================================================
# Quick Render Presets
# =====================================================================

# Render just the summary scenes
summaries:
	@echo "Rendering summary scenes..."
	manim -pqh twistor_visualization.py TwistorTheoryComplete
	manim -pqh spin_network_visualization.py SpinNetworkComplete
	manim -pqh combined_visualization.py FinalSynthesis
	@echo "Summary scenes complete!"

# Render just the 3D scenes
scenes-3d:
	@echo "Rendering 3D scenes..."
	manim -pqh twistor_visualization.py ComplexProjectiveSpace
	manim -pqh twistor_visualization.py AlphaBetaPlanes
	manim -pqh spin_network_visualization.py SixJSymbol
	manim -pqh spin_network_visualization.py TetrahedralNetwork
	manim -pqh combined_visualization.py GeometricInterpretation
	@echo "3D scenes complete!"

# Render educational sequence
educational:
	@echo "Rendering educational sequence..."
	manim -pqh twistor_visualization.py TwistorIntroduction
	manim -pqh twistor_visualization.py ComplexProjectiveSpace
	manim -pqh spin_network_visualization.py SpinNetworkIntroduction
	manim -pqh spin_network_visualization.py BasicSpinNetwork
	manim -pqh combined_visualization.py TwistorSpinComparison
	manim -pqh combined_visualization.py FinalSynthesis
	@echo "Educational sequence complete!"

# =====================================================================
# Environment Check
# =====================================================================

check-env:
	@echo "Environment Check"
	@echo "================="
	@echo "LaTeX:"
	@which pdflatex > /dev/null && pdflatex --version | head -n1 || echo "  Not found"
	@echo ""
	@echo "Python:"
	@which python3 > /dev/null && python3 --version || echo "  Not found"
	@echo ""
	@echo "Manim:"
	@which manim > /dev/null && manim --version || echo "  Not found"
	@echo ""
	@echo "FFmpeg:"
	@which ffmpeg > /dev/null && ffmpeg -version | head -n1 || echo "  Not found"
	@echo ""
	@echo "Required Python packages:"
	@pip show manim > /dev/null 2>&1 && echo "  ✓ manim" || echo "  ✗ manim"
	@pip show numpy > /dev/null 2>&1 && echo "  ✓ numpy" || echo "  ✗ numpy"
	@pip show scipy > /dev/null 2>&1 && echo "  ✓ scipy" || echo "  ✗ scipy"

# =====================================================================
# Info
# =====================================================================

info:
	@echo "Twistor Theory and Spin Networks Visualization"
	@echo "=============================================="
	@echo ""
	@echo "LaTeX Documents:"
	@ls -lh *.tex 2>/dev/null | awk '{print "  " $$9 " (" $$5 ")"}'
	@echo ""
	@echo "Python Scripts:"
	@ls -lh *_visualization.py 2>/dev/null | awk '{print "  " $$9 " (" $$5 ")"}'
	@echo ""
	@echo "Generated PDFs:"
	@ls -lh *.pdf 2>/dev/null | awk '{print "  " $$9 " (" $$5 ")"}' || echo "  None yet"
	@echo ""
	@echo "Rendered Videos:"
	@find media/videos -name "*.mp4" 2>/dev/null | wc -l | awk '{print "  " $$1 " videos"}' || echo "  None yet"
	@echo ""
	@echo "Run 'make help' for available commands"

.DEFAULT_GOAL := help
