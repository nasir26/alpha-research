#!/bin/bash

# Script to render all Twistor Theory and Spin Networks visualizations
# Usage: ./render_all_scenes.sh [quality]
# Quality options: l (low), m (medium), h (high), s (4K)
# Default: l (low quality for fast preview)

QUALITY=${1:-l}
QUALITY_FLAG="-pq${QUALITY}"

echo "=========================================="
echo "Rendering Twistor Theory & Spin Networks"
echo "Quality: $QUALITY_FLAG"
echo "=========================================="
echo ""

# Base scenes
SCENES=(
    "TwistorSpace"
    "SpinNetwork"
    "PenroseDiagram"
    "TwistorSpinNetworkConnection"
    "QuantumGeometry"
    "TwistorEquation"
    "SpinNetworkEvolution"
    "ComprehensiveVisualization"
)

# Enhanced scenes
ENHANCED_SCENES=(
    "TwistorSpaceDetailed"
    "SpinNetworkDetailed"
    "PenroseDiagramDetailed"
    "TwistorSpinNetworkConnectionDetailed"
    "QuantumGeometryDetailed"
    "MathematicalFormulations"
    "SpinFoamEvolution"
)

# Function to render scenes from a file
render_scenes() {
    local file=$1
    shift
    local scenes=("$@")
    
    echo "Rendering from $file..."
    for scene in "${scenes[@]}"; do
        echo "  - Rendering $scene..."
        manim $QUALITY_FLAG "$file" "$scene" || echo "    Warning: Failed to render $scene"
    done
    echo ""
}

# Render base scenes
echo "=== Base Scenes ==="
render_scenes "twistor_spin_networks.py" "${SCENES[@]}"

# Render enhanced scenes
echo "=== Enhanced Scenes ==="
render_scenes "twistor_spin_networks_enhanced.py" "${ENHANCED_SCENES[@]}"

echo "=========================================="
echo "Rendering complete!"
echo "Videos saved in: media/videos/"
echo "=========================================="
