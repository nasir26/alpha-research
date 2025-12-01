# Twistor Theory and Spin Networks: A Visual Exploration

<p align="center">
  <img src="figures/banner.png" alt="Twistor-SpinNetwork Visualization" width="800">
</p>

## 📖 Overview

This project provides a comprehensive visual exploration of two fundamental structures in mathematical physics:

- **Twistor Theory** - Roger Penrose's elegant reformulation of spacetime geometry using complex geometry
- **Spin Networks** - Combinatorial structures that form the basis of Loop Quantum Gravity

The project includes:
- 📄 A detailed **LaTeX document** with embedded TikZ diagrams
- 🎬 **Manim animations** for dynamic visualization
- 📐 **Mathematical formulations** with clear explanations

## 🏗️ Project Structure

```
twistor-spinnetwork-visualization/
├── latex/
│   └── main.tex              # Comprehensive LaTeX document
├── manim/
│   ├── twistor_intro.py      # Twistor space visualizations
│   ├── spin_network.py       # Spin network animations
│   ├── penrose_calculus.py   # Graphical calculus visualizations
│   └── unified_view.py       # Connections between theories
├── figures/
│   └── (generated figures)
├── output/
│   └── (rendered videos)
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### Prerequisites

1. **Python 3.8+**
2. **LaTeX distribution** (for document compilation and Manim)
   - Ubuntu/Debian: `sudo apt-get install texlive-full`
   - macOS: `brew install --cask mactex`
   - Windows: [MiKTeX](https://miktex.org/)

3. **FFmpeg** (for video rendering)
   - Ubuntu/Debian: `sudo apt-get install ffmpeg`
   - macOS: `brew install ffmpeg`

### Installation

```bash
# Clone or navigate to the project
cd twistor-spinnetwork-visualization

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### Compiling the LaTeX Document

```bash
cd latex
pdflatex main.tex
pdflatex main.tex  # Run twice for references
```

### Running Manim Animations

```bash
cd manim

# Low quality preview (fast)
manim -pql twistor_intro.py TwistorSpaceScene

# High quality render
manim -pqh spin_network.py SpinNetworkBasics

# All scenes in a file
manim -pql penrose_calculus.py
```

## 📚 Content Overview

### Part I: Twistor Theory

1. **Introduction to Twistor Space**
   - Minkowski space and spinor notation
   - Definition of twistors: $Z^{\alpha} = (\omega^A, \pi_{A'})$
   - Projective twistor space $\mathbb{PT} = \mathbb{CP}^3$

2. **The Incidence Relation**
   - Fundamental equation: $\omega^A = i x^{AA'} \pi_{A'}$
   - Point-line correspondence
   - Null twistors and light rays

3. **The Penrose Transform**
   - Cohomology and massless fields
   - Sheaf-theoretic formulation

### Part II: Spin Networks

1. **Foundations**
   - SU(2) representation theory
   - Definition of spin networks: $\mathcal{S} = (\Gamma, \{j_e\}, \{i_v\})$
   - Intertwiners and recoupling

2. **Penrose Graphical Calculus**
   - Tensor notation
   - Wigner 3j and 6j symbols
   - Evaluation rules

3. **Loop Quantum Gravity**
   - Kinematical Hilbert space
   - Area operator spectrum: $A = 8\pi\gamma\ell_P^2 \sum_e \sqrt{j_e(j_e+1)}$
   - Volume quantization

### Part III: Connections

- Shared SU(2) structure
- Quantum geometry perspectives
- Historical development

## 🎬 Animation Scenes

| Scene | File | Description |
|-------|------|-------------|
| `TwistorSpaceScene` | `twistor_intro.py` | 3D visualization of twistor space |
| `IncidenceRelationScene` | `twistor_intro.py` | The fundamental incidence relation |
| `NullTwistorScene` | `twistor_intro.py` | Null twistors and PT±/N decomposition |
| `PenroseCorrespondence` | `twistor_intro.py` | Point-line correspondence |
| `SpinNetworkBasics` | `spin_network.py` | Basic spin network structure |
| `SU2RepresentationScene` | `spin_network.py` | SU(2) representations |
| `ClebschGordanScene` | `spin_network.py` | Tensor product decomposition |
| `AreaQuantizationScene` | `spin_network.py` | LQG area spectrum |
| `PenroseBasics` | `penrose_calculus.py` | Graphical calculus elements |
| `WignerSymbols` | `penrose_calculus.py` | 3j and 6j symbols |
| `TwistorSpinNetworkConnection` | `unified_view.py` | Deep connections |

## 📐 Key Mathematical Formulas

### Twistor Theory

**Incidence Relation:**
$$\omega^A = i x^{AA'} \pi_{A'}$$

**Null Condition:**
$$Z^{\alpha}\bar{Z}_{\alpha} = \omega^A\bar{\omega}_A + \bar{\pi}_{A'}\pi^{A'} = 0$$

### Spin Networks

**Area Spectrum:**
$$A_S = 8\pi\gamma\ell_P^2 \sum_{e \cap S} \sqrt{j_e(j_e+1)}$$

**Clebsch-Gordan Decomposition:**
$$V_{j_1} \otimes V_{j_2} = \bigoplus_{j=|j_1-j_2|}^{j_1+j_2} V_j$$

## 🎨 Color Scheme

The visualizations use a consistent color scheme:

| Color | Hex | Usage |
|-------|-----|-------|
| Twistor Blue | `#2962FF` | Twistor space elements |
| Spin Red | `#F44336` | Unprimed spinors, $\mathbb{PT}^-$ |
| Spin Green | `#4CAF50` | Primed spinors, $\mathbb{PT}^+$ |
| Node Teal | `#009688` | Spin network vertices |
| Edge Purple | `#673AB7` | Spin network edges |
| Gold | `#FFC107` | Spacetime points, highlights |

## 📖 References

1. R. Penrose, "Twistor algebra", J. Math. Phys. **8**, 345 (1967)
2. R. Penrose and W. Rindler, *Spinors and Space-Time*, Cambridge University Press (1984)
3. R. Penrose, "Angular momentum: an approach to combinatorial space-time" (1971)
4. C. Rovelli and L. Smolin, "Spin networks and quantum gravity", Phys. Rev. D **52**, 5743 (1995)
5. C. Rovelli, *Quantum Gravity*, Cambridge University Press (2004)
6. T. Thiemann, *Modern Canonical Quantum General Relativity*, Cambridge University Press (2007)

## 📄 License

This project is for educational purposes. Feel free to use and modify with attribution.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests for:
- Additional animations
- Improved mathematical explanations
- Bug fixes
- Documentation improvements

---

<p align="center">
  <i>Exploring the quantum geometry of spacetime through visualization</i>
</p>
