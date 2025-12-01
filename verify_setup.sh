#!/bin/bash
# Verification script for Twistor Theory and Spin Networks Visualization
# ========================================================================

echo "=================================================="
echo "Twistor Theory & Spin Networks - Setup Verification"
echo "=================================================="
echo ""

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Counter for checks
PASSED=0
FAILED=0

# Function to check command
check_command() {
    if command -v "$1" &> /dev/null; then
        echo -e "${GREEN}✓${NC} $1 found: $(command -v $1)"
        ((PASSED++))
        return 0
    else
        echo -e "${RED}✗${NC} $1 not found"
        ((FAILED++))
        return 1
    fi
}

# Function to check file
check_file() {
    if [ -f "$1" ]; then
        SIZE=$(ls -lh "$1" | awk '{print $5}')
        echo -e "${GREEN}✓${NC} $1 (${SIZE})"
        ((PASSED++))
        return 0
    else
        echo -e "${RED}✗${NC} $1 not found"
        ((FAILED++))
        return 1
    fi
}

# Function to check Python package
check_python_package() {
    if python3 -c "import $1" &> /dev/null; then
        VERSION=$(python3 -c "import $1; print($1.__version__)" 2>/dev/null || echo "installed")
        echo -e "${GREEN}✓${NC} Python package '$1' ($VERSION)"
        ((PASSED++))
        return 0
    else
        echo -e "${RED}✗${NC} Python package '$1' not found"
        echo -e "    ${YELLOW}Install with: pip install $1${NC}"
        ((FAILED++))
        return 1
    fi
}

echo "1. Checking System Commands"
echo "----------------------------"
check_command "python3"
check_command "pip"
check_command "pdflatex"
check_command "make"
check_command "ffmpeg"
echo ""

echo "2. Checking Python Packages"
echo "----------------------------"
check_python_package "manim"
check_python_package "numpy"
check_python_package "scipy"
echo ""

echo "3. Checking LaTeX Files"
echo "-----------------------"
check_file "twister_spin_networks.tex"
check_file "mathematical_supplement.tex"
echo ""

echo "4. Checking Python Visualization Files"
echo "---------------------------------------"
check_file "twistor_visualization.py"
check_file "spin_network_visualization.py"
check_file "combined_visualization.py"
echo ""

echo "5. Checking Documentation Files"
echo "--------------------------------"
check_file "README_VISUALIZATION.md"
check_file "QUICKSTART.md"
check_file "PROJECT_OVERVIEW.md"
check_file "requirements.txt"
check_file "Makefile"
echo ""

echo "6. Checking Python Syntax"
echo "-------------------------"
if python3 -m py_compile twistor_visualization.py 2>/dev/null; then
    echo -e "${GREEN}✓${NC} twistor_visualization.py - valid syntax"
    ((PASSED++))
else
    echo -e "${RED}✗${NC} twistor_visualization.py - syntax error"
    ((FAILED++))
fi

if python3 -m py_compile spin_network_visualization.py 2>/dev/null; then
    echo -e "${GREEN}✓${NC} spin_network_visualization.py - valid syntax"
    ((PASSED++))
else
    echo -e "${RED}✗${NC} spin_network_visualization.py - syntax error"
    ((FAILED++))
fi

if python3 -m py_compile combined_visualization.py 2>/dev/null; then
    echo -e "${GREEN}✓${NC} combined_visualization.py - valid syntax"
    ((PASSED++))
else
    echo -e "${RED}✗${NC} combined_visualization.py - syntax error"
    ((FAILED++))
fi
echo ""

# Summary
echo "=================================================="
echo "Summary"
echo "=================================================="
echo -e "Passed: ${GREEN}${PASSED}${NC}"
echo -e "Failed: ${RED}${FAILED}${NC}"
echo ""

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}✓ All checks passed!${NC}"
    echo ""
    echo "You're ready to go! Try:"
    echo "  make latex          # Compile LaTeX documents"
    echo "  make manim-preview  # Render preview scenes"
    echo "  make help           # See all available commands"
    echo ""
    exit 0
else
    echo -e "${YELLOW}⚠ Some checks failed.${NC}"
    echo ""
    echo "Installation help:"
    if ! command -v pdflatex &> /dev/null; then
        echo "  LaTeX: sudo apt install texlive-full  (Ubuntu/Debian)"
        echo "         brew install --cask mactex      (macOS)"
    fi
    if ! python3 -c "import manim" &> /dev/null; then
        echo "  Manim: pip install -r requirements.txt"
    fi
    echo ""
    echo "See QUICKSTART.md for detailed installation instructions."
    echo ""
    exit 1
fi
