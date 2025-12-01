# Quick Start Guide: Twistor Theory & Spin Networks Visualization

## Installation

```bash
# Install Manim
pip install manim

# Or use requirements file
pip install -r manim_requirements.txt
```

## Quick Render

### Single Scene (Fast Preview)
```bash
manim -pql twistor_spin_networks.py TwistorSpace
```

### All Scenes
```bash
chmod +x render_all_scenes.sh
./render_all_scenes.sh l    # Low quality (fast)
./render_all_scenes.sh m    # Medium quality
./render_all_scenes.sh h    # High quality
./render_all_scenes.sh s    # 4K quality
```

## Available Scenes

### Base Scenes (`twistor_spin_networks.py`)
1. **TwistorSpace** - 3D twistor space visualization
2. **SpinNetwork** - Basic spin network structure
3. **PenroseDiagram** - Conformal compactification
4. **TwistorSpinNetworkConnection** - Relationship between concepts
5. **QuantumGeometry** - 3D quantum geometry
6. **TwistorEquation** - Mathematical formulations
7. **SpinNetworkEvolution** - Network evolution over time
8. **ComprehensiveVisualization** - Overview of all concepts

### Enhanced Scenes (`twistor_spin_networks_enhanced.py`)
1. **TwistorSpaceDetailed** - Detailed twistor space with equations
2. **SpinNetworkDetailed** - Complex spin network structures
3. **PenroseDiagramDetailed** - Detailed Penrose diagram
4. **TwistorSpinNetworkConnectionDetailed** - Detailed connection visualization
5. **QuantumGeometryDetailed** - Detailed quantum geometry with formulas
6. **MathematicalFormulations** - All key equations
7. **SpinFoamEvolution** - Spin foam evolution

## Output Location

Rendered videos are saved in:
```
media/videos/twistor_spin_networks/<quality>/<SceneName>.mp4
```

## Compile LaTeX Document

```bash
pdflatex twistor_spin_networks_theory.tex
```

## Customization

Edit the Python files to:
- Change colors
- Modify animation speeds
- Add new equations
- Create custom visualizations

## Troubleshooting

**LaTeX not rendering?**
```bash
sudo apt-get install texlive-full  # Linux
```

**FFmpeg missing?**
```bash
sudo apt-get install ffmpeg  # Linux
brew install ffmpeg  # macOS
```

**Import errors?**
```bash
pip install --upgrade manim numpy scipy matplotlib
```
