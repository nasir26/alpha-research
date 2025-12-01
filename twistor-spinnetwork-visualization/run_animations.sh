#!/bin/bash
# =============================================================================
# Twistor Theory and Spin Networks - Animation Runner
# =============================================================================
# This script renders all Manim animations for the project.
#
# Usage:
#   ./run_animations.sh [quality]
#
# Quality options:
#   low    - Low quality (480p), fast render
#   medium - Medium quality (720p)
#   high   - High quality (1080p), slow render
#
# =============================================================================

set -e

# Default quality
QUALITY="${1:-low}"

# Set quality flag
case $QUALITY in
    low)
        FLAG="-pql"
        echo "Rendering in LOW quality (480p)"
        ;;
    medium)
        FLAG="-pqm"
        echo "Rendering in MEDIUM quality (720p)"
        ;;
    high)
        FLAG="-pqh"
        echo "Rendering in HIGH quality (1080p)"
        ;;
    *)
        echo "Unknown quality: $QUALITY"
        echo "Usage: $0 [low|medium|high]"
        exit 1
        ;;
esac

cd "$(dirname "$0")/manim"

echo ""
echo "=============================================="
echo "Twistor Theory Animations"
echo "=============================================="

TWISTOR_SCENES=(
    "TwistorSpaceScene"
    "IncidenceRelationScene"
    "NullTwistorScene"
    "PenroseCorrespondence"
)

for scene in "${TWISTOR_SCENES[@]}"; do
    echo "Rendering: $scene"
    manim $FLAG twistor_intro.py $scene || echo "  Warning: $scene may have failed"
done

echo ""
echo "=============================================="
echo "Spin Network Animations"
echo "=============================================="

SPIN_SCENES=(
    "SpinNetworkBasics"
    "SU2RepresentationScene"
    "ClebschGordanScene"
    "IntertwinerScene"
    "AreaQuantizationScene"
    "SpinNetworkEvaluation"
)

for scene in "${SPIN_SCENES[@]}"; do
    echo "Rendering: $scene"
    manim $FLAG spin_network.py $scene || echo "  Warning: $scene may have failed"
done

echo ""
echo "=============================================="
echo "Penrose Calculus Animations"
echo "=============================================="

PENROSE_SCENES=(
    "PenroseBasics"
    "SpinorNotation"
    "TwistorDiagrams"
    "WignerSymbols"
)

for scene in "${PENROSE_SCENES[@]}"; do
    echo "Rendering: $scene"
    manim $FLAG penrose_calculus.py $scene || echo "  Warning: $scene may have failed"
done

echo ""
echo "=============================================="
echo "Unified View Animations"
echo "=============================================="

UNIFIED_SCENES=(
    "TwistorSpinNetworkConnection"
    "QuantumGeometryBridge"
    "HistoricalTimeline"
)

for scene in "${UNIFIED_SCENES[@]}"; do
    echo "Rendering: $scene"
    manim $FLAG unified_view.py $scene || echo "  Warning: $scene may have failed"
done

echo ""
echo "=============================================="
echo "Advanced Visualizations"
echo "=============================================="

ADVANCED_SCENES=(
    "PachnerMoves"
    "CoherentStates"
    "HolonomyFlux"
)

for scene in "${ADVANCED_SCENES[@]}"; do
    echo "Rendering: $scene"
    manim $FLAG advanced_visualizations.py $scene || echo "  Warning: $scene may have failed"
done

echo ""
echo "=============================================="
echo "All animations complete!"
echo "Output files are in: media/videos/"
echo "=============================================="
