"""
Utility Functions and Common Components
=======================================
Shared utilities for Twistor and Spin Network visualizations.
"""

from manim import *
import numpy as np

# =============================================================================
# COLOR PALETTE
# =============================================================================

class Colors:
    """Consistent color scheme for all visualizations."""
    
    # Primary colors
    TWISTOR_BLUE = "#2962FF"
    TWISTOR_GOLD = "#FFC107"
    
    # Spinor colors
    SPIN_RED = "#F44336"      # Unprimed spinors, negative helicity
    SPIN_GREEN = "#4CAF50"    # Primed spinors, positive helicity
    SPIN_PURPLE = "#9C27B0"   # Combined/mixed
    
    # Spacetime colors
    SPACETIME_DARK = "#212121"
    NULL_CONE = "#FF9800"
    LIGHT_RAY = "#FFEB3B"
    
    # Spin network colors
    NODE_COLOR = "#009688"    # Teal for vertices
    EDGE_COLOR = "#673AB7"    # Purple for edges
    INTERTWINER = "#E91E63"   # Pink for intertwiners
    
    # Utility
    BACKGROUND = "#1a1a2e"
    ACCENT = "#16213e"


# =============================================================================
# COMMON MOBJECTS
# =============================================================================

class SpinNetworkVertex(VGroup):
    """A spin network vertex with optional label."""
    
    def __init__(self, position=ORIGIN, radius=0.25, color=Colors.NODE_COLOR, 
                 label=None, **kwargs):
        super().__init__(**kwargs)
        
        self.dot = Dot(position, radius=radius, color=color)
        self.add(self.dot)
        
        if label:
            self.label = MathTex(label, font_size=24, color=WHITE)
            self.label.move_to(position)
            self.add(self.label)
    
    def get_center(self):
        return self.dot.get_center()


class SpinNetworkEdge(VGroup):
    """A spin network edge with spin label."""
    
    def __init__(self, start, end, spin=1, show_label=True, **kwargs):
        super().__init__(**kwargs)
        
        # Edge width proportional to spin
        width = 2 + spin * 2
        
        self.line = Line(start, end, stroke_width=width, color=Colors.EDGE_COLOR)
        self.add(self.line)
        
        if show_label:
            midpoint = (np.array(start) + np.array(end)) / 2
            
            # Format spin label
            if spin == int(spin):
                label_text = f"j={int(spin)}"
            else:
                # Format as fraction
                if spin == 0.5:
                    label_text = r"j=\frac{1}{2}"
                elif spin == 1.5:
                    label_text = r"j=\frac{3}{2}"
                elif spin == 2.5:
                    label_text = r"j=\frac{5}{2}"
                else:
                    label_text = f"j={spin}"
            
            self.label = MathTex(label_text, font_size=20)
            
            # Position label perpendicular to edge
            direction = np.array(end) - np.array(start)
            perpendicular = np.array([-direction[1], direction[0], 0])
            perpendicular = perpendicular / np.linalg.norm(perpendicular) * 0.3
            
            self.label.move_to(midpoint + perpendicular)
            self.add(self.label)
    
    def get_start(self):
        return self.line.get_start()
    
    def get_end(self):
        return self.line.get_end()


class TwistorLine(VGroup):
    """A twistor line representation."""
    
    def __init__(self, start=DOWN, end=UP, is_dual=False, label=None, **kwargs):
        super().__init__(**kwargs)
        
        color = Colors.SPIN_RED if is_dual else Colors.TWISTOR_BLUE
        
        if is_dual:
            self.line = DashedLine(start, end, stroke_width=4, color=color)
        else:
            self.line = Line(start, end, stroke_width=4, color=color)
        
        self.add(self.line)
        
        # Add endpoints
        self.start_dot = Dot(start, radius=0.08, color=color)
        self.end_dot = Dot(end, radius=0.08, color=color)
        self.add(self.start_dot, self.end_dot)
        
        if label:
            self.label = MathTex(label, font_size=28, color=color)
            self.label.next_to(self.line, RIGHT, buff=0.2)
            self.add(self.label)


class LightCone2D(VGroup):
    """A 2D representation of a light cone."""
    
    def __init__(self, apex=ORIGIN, size=2, **kwargs):
        super().__init__(**kwargs)
        
        # Future cone
        future_left = Line(apex, apex + size * (UP + LEFT), 
                          stroke_width=3, color=Colors.NULL_CONE)
        future_right = Line(apex, apex + size * (UP + RIGHT), 
                           stroke_width=3, color=Colors.NULL_CONE)
        
        # Past cone
        past_left = Line(apex, apex + size * (DOWN + LEFT), 
                        stroke_width=3, color=Colors.NULL_CONE)
        past_right = Line(apex, apex + size * (DOWN + RIGHT), 
                         stroke_width=3, color=Colors.NULL_CONE)
        
        # Fill
        future_fill = Polygon(
            apex, apex + size * (UP + LEFT), apex + size * (UP + RIGHT),
            fill_color=Colors.NULL_CONE, fill_opacity=0.2, stroke_width=0
        )
        past_fill = Polygon(
            apex, apex + size * (DOWN + LEFT), apex + size * (DOWN + RIGHT),
            fill_color=Colors.NULL_CONE, fill_opacity=0.2, stroke_width=0
        )
        
        self.add(future_fill, past_fill)
        self.add(future_left, future_right, past_left, past_right)
        
        # Apex point
        self.apex = Dot(apex, radius=0.1, color=Colors.TWISTOR_GOLD)
        self.add(self.apex)


class InvariantTensor(VGroup):
    """Visualization of an invariant tensor (epsilon or intertwiner)."""
    
    def __init__(self, position=ORIGIN, n_legs=3, **kwargs):
        super().__init__(**kwargs)
        
        # Central node
        self.node = Dot(position, radius=0.2, color=Colors.INTERTWINER)
        self.add(self.node)
        
        # Legs
        self.legs = VGroup()
        for i in range(n_legs):
            angle = TAU * i / n_legs - PI/2
            end = position + 1.2 * np.array([np.cos(angle), np.sin(angle), 0])
            leg = Line(position, end, stroke_width=3, color=Colors.EDGE_COLOR)
            self.legs.add(leg)
        
        self.add(self.legs)


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def create_spin_network_graph(vertices, edges, spins):
    """
    Create a complete spin network from vertex positions and edge connections.
    
    Args:
        vertices: List of (x, y) positions
        edges: List of (i, j) pairs indexing vertices
        spins: List of spin values for each edge
    
    Returns:
        VGroup containing the complete spin network
    """
    network = VGroup()
    
    # Create edges first (so vertices appear on top)
    for (i, j), spin in zip(edges, spins):
        start = np.array([*vertices[i], 0])
        end = np.array([*vertices[j], 0])
        edge = SpinNetworkEdge(start, end, spin=spin)
        network.add(edge)
    
    # Create vertices
    for pos in vertices:
        vertex = SpinNetworkVertex(np.array([*pos, 0]))
        network.add(vertex)
    
    return network


def create_theta_network(position=ORIGIN, spins=(1, 0.5, 1.5)):
    """
    Create a theta network (two vertices connected by three edges).
    
    Args:
        position: Center position
        spins: Tuple of three spin values
    
    Returns:
        VGroup containing the theta network
    """
    network = VGroup()
    
    left = position + LEFT * 1.5
    right = position + RIGHT * 1.5
    
    # Three curved edges
    angles = [PI/3, 0, -PI/3]
    for spin, angle in zip(spins, angles):
        if angle == 0:
            edge = Line(left, right, stroke_width=2 + spin * 2, color=Colors.EDGE_COLOR)
        else:
            edge = ArcBetweenPoints(left, right, angle=angle, 
                                    stroke_width=2 + spin * 2, color=Colors.EDGE_COLOR)
        network.add(edge)
    
    # Vertices
    v1 = SpinNetworkVertex(left)
    v2 = SpinNetworkVertex(right)
    network.add(v1, v2)
    
    return network


def area_eigenvalue(spins):
    """
    Calculate the area eigenvalue for a list of spins.
    
    Args:
        spins: List of spin values
    
    Returns:
        Sum of sqrt(j(j+1)) for each spin
    """
    return sum(np.sqrt(j * (j + 1)) for j in spins)


def format_spin_label(j):
    """
    Format a spin value as a LaTeX string.
    
    Args:
        j: Spin value (integer or half-integer)
    
    Returns:
        LaTeX string representation
    """
    if j == int(j):
        return str(int(j))
    else:
        numerator = int(2 * j)
        return rf"\frac{{{numerator}}}{{2}}"


# =============================================================================
# ANIMATION HELPERS
# =============================================================================

def highlight_pulse(mobject, color=Colors.TWISTOR_GOLD, scale=1.2):
    """
    Create a pulsing highlight animation.
    
    Args:
        mobject: Object to highlight
        color: Highlight color
        scale: Maximum scale factor
    
    Returns:
        Animation sequence
    """
    return Succession(
        mobject.animate.scale(scale).set_color(color),
        mobject.animate.scale(1/scale).set_color(mobject.get_color()),
        lag_ratio=0.5
    )


def draw_brace_label(start, end, label_text, direction=DOWN):
    """
    Create a brace with label between two points.
    
    Args:
        start: Start position
        end: End position
        label_text: Text for label
        direction: Direction for brace
    
    Returns:
        VGroup containing brace and label
    """
    brace = Brace(Line(start, end), direction)
    label = brace.get_tex(label_text)
    return VGroup(brace, label)


# =============================================================================
# MATH HELPERS
# =============================================================================

def wigner_3j_nonzero(j1, j2, j3):
    """
    Check if a Wigner 3j symbol is potentially nonzero (triangle inequality).
    
    Args:
        j1, j2, j3: Three spin values
    
    Returns:
        True if triangle inequality is satisfied
    """
    return (abs(j1 - j2) <= j3 <= j1 + j2 and 
            (j1 + j2 + j3) == int(j1 + j2 + j3))


def intertwiner_dimension(spins):
    """
    Estimate the dimension of the intertwiner space for given incident spins.
    
    For a 3-valent vertex: 0 or 1
    For higher valence: uses Clebsch-Gordan decomposition
    
    Args:
        spins: List of spin values
    
    Returns:
        Dimension of intertwiner space
    """
    if len(spins) < 3:
        return 0
    elif len(spins) == 3:
        j1, j2, j3 = spins
        if wigner_3j_nonzero(j1, j2, j3):
            return 1
        return 0
    else:
        # For higher valence, return a rough estimate
        return max(1, len(spins) - 2)


if __name__ == "__main__":
    print("Utility module for Twistor-SpinNetwork visualization")
    print("\nAvailable classes:")
    print("  - SpinNetworkVertex")
    print("  - SpinNetworkEdge")
    print("  - TwistorLine")
    print("  - LightCone2D")
    print("  - InvariantTensor")
    print("\nHelper functions:")
    print("  - create_spin_network_graph()")
    print("  - create_theta_network()")
    print("  - area_eigenvalue()")
    print("  - format_spin_label()")
