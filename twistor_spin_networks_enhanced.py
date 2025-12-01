"""
Enhanced Twistor Theory and Spin Networks Visualization

This enhanced version includes:
- More detailed mathematical formulations
- Advanced geometric visualizations
- Interactive transformations
- Comprehensive LaTeX documentation
- Extended spin network structures
"""

from manim import *
import numpy as np
from typing import List, Tuple, Optional
import math


class TwistorSpaceDetailed(ThreeDScene):
    """
    Detailed visualization of Twistor Space with mathematical foundations
    
    Twistor space T is a 4-dimensional complex vector space.
    Points in twistor space correspond to null geodesics in Minkowski space.
    """
    
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        
        # Title with LaTeX
        title = MathTex(
            r"\text{Twistor Space } \mathbb{T} = \mathbb{C}^4",
            font_size=48,
            color=BLUE
        )
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.wait(1)
        
        # Create coordinate system
        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-4, 4, 1],
            axis_config={"color": GRAY, "stroke_width": 2}
        )
        axes_labels = axes.get_axis_labels(
            MathTex("\\text{Re}(Z^0)"),
            MathTex("\\text{Im}(Z^1)"),
            MathTex("\\text{Re}(Z^2)")
        )
        self.add(axes, axes_labels)
        
        # Twistor coordinates explanation
        coords = MathTex(
            r"Z^\alpha = \begin{pmatrix} Z^0 \\ Z^1 \\ Z^2 \\ Z^3 \end{pmatrix} = \begin{pmatrix} \omega^0 \\ \omega^1 \\ \pi_{0'} \\ \pi_{1'} \end{pmatrix}",
            font_size=32
        )
        coords.to_corner(UL)
        self.add_fixed_in_frame_mobjects(coords)
        self.wait(2)
        
        # Null twistor condition
        null_condition = MathTex(
            r"Z^\alpha \bar{Z}_\alpha = |Z^0|^2 + |Z^1|^2 - |Z^2|^2 - |Z^3|^2 = 0",
            font_size=28,
            color=YELLOW
        )
        null_condition.next_to(coords, DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(null_condition)
        self.wait(2)
        
        # Create null twistor surface
        null_surface = self.create_null_twistor_surface()
        self.play(Create(null_surface), run_time=3)
        self.wait(2)
        
        # Show twistor incidence relation
        incidence = MathTex(
            r"\omega^A = i x^{AA'} \pi_{A'}",
            font_size=32,
            color=GREEN
        )
        incidence.to_corner(UR)
        self.add_fixed_in_frame_mobjects(incidence)
        self.wait(2)
        
        # Animate rotation
        self.play(
            Rotate(null_surface, PI, axis=UP),
            run_time=4
        )
        self.wait(2)
    
    def create_null_twistor_surface(self) -> ParametricSurface:
        """Create surface representing null twistors"""
        return ParametricSurface(
            lambda u, v: np.array([
                2 * np.cos(u) * np.cos(v),
                2 * np.sin(u) * np.cos(v),
                2 * np.sin(v) * np.cos(u)
            ]),
            u_range=[0, 2 * PI],
            v_range=[-PI/2, PI/2],
            fill_opacity=0.4,
            fill_color=BLUE,
            checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(30, 30)
        )


class SpinNetworkDetailed(Scene):
    """
    Detailed Spin Network visualization with mathematical structure
    
    A spin network is a graph where:
    - Vertices represent quantum geometry
    - Edges are labeled by SU(2) representations (spins)
    - The network is gauge invariant
    """
    
    def construct(self):
        # Title
        title = MathTex(
            r"\text{Spin Network } \Gamma = (V, E, j)",
            font_size=48,
            color=YELLOW
        )
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Create complex spin network
        network = self.create_complex_network()
        self.play(Create(network), run_time=3)
        self.wait(1)
        
        # Add spin labels with mathematical notation
        spin_labels = self.add_detailed_spin_labels()
        self.play(*[Write(label) for label in spin_labels], run_time=2)
        self.wait(1)
        
        # Show gauge invariance
        gauge_inv = MathTex(
            r"\text{Gauge Invariant: } A(\Gamma) = A(g \cdot \Gamma)",
            font_size=28,
            color=GREEN
        )
        gauge_inv.to_edge(DOWN)
        self.play(Write(gauge_inv))
        self.wait(2)
        
        # Show spin network amplitude
        amplitude = MathTex(
            r"A(\Gamma) = \prod_{e \in E} (2j_e + 1) \prod_{v \in V} \begin{Bmatrix} j_1 & j_2 & j_3 \\ j_4 & j_5 & j_6 \end{Bmatrix}",
            font_size=24
        )
        amplitude.next_to(gauge_inv, UP, buff=0.5)
        self.play(Write(amplitude), run_time=3)
        self.wait(2)
        
        # Animate gauge transformation
        self.animate_detailed_gauge_transformation(network)
        self.wait(2)
    
    def create_complex_network(self) -> VGroup:
        """Create a more complex spin network"""
        # Central node
        center = Circle(radius=0.25, color=WHITE, fill_opacity=1)
        center.move_to(ORIGIN)
        
        # Surrounding nodes
        num_nodes = 6
        nodes = [center]
        angles = [k * 2 * PI / num_nodes for k in range(num_nodes)]
        
        for angle in angles:
            node = Circle(radius=0.2, color=WHITE, fill_opacity=1)
            pos = 1.5 * (np.cos(angle) * RIGHT + np.sin(angle) * UP)
            node.move_to(pos)
            nodes.append(node)
        
        # Edges from center to outer nodes
        edges = []
        for i in range(1, len(nodes)):
            edge = Line(
                center.get_center(),
                nodes[i].get_center(),
                color=BLUE,
                stroke_width=4
            )
            edges.append(edge)
        
        # Additional edges between outer nodes
        for i in range(1, len(nodes)):
            j = (i % num_nodes) + 1
            edge = Line(
                nodes[i].get_center(),
                nodes[j].get_center(),
                color=BLUE_D,
                stroke_width=2
            )
            edges.append(edge)
        
        return VGroup(*nodes, *edges)
    
    def add_detailed_spin_labels(self) -> List[MathTex]:
        """Add detailed spin labels"""
        labels = []
        spins = ["1/2", "1", "3/2", "1", "1/2", "1"]
        
        # Position labels on edges
        positions = [
            1.5 * (np.cos(k * 2 * PI / 6) * RIGHT + np.sin(k * 2 * PI / 6) * UP)
            for k in range(6)
        ]
        
        for i, (pos, spin) in enumerate(zip(positions, spins)):
            label = MathTex(f"j={spin}", font_size=24)
            label.move_to(0.7 * pos)
            labels.append(label)
        
        return labels
    
    def animate_detailed_gauge_transformation(self, network: VGroup):
        """Animate a detailed gauge transformation"""
        # Rotate the network
        self.play(
            Rotate(network, PI/3),
            run_time=2
        )


class PenroseDiagramDetailed(Scene):
    """
    Detailed Penrose Diagram with conformal compactification
    
    Penrose diagrams represent the conformal compactification of spacetime,
    showing causal structure and infinity.
    """
    
    def construct(self):
        title = MathTex(
            r"\text{Penrose Diagram: Conformal Compactification}",
            font_size=42,
            color=ORANGE
        )
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Create detailed Penrose diagram
        diagram = self.create_detailed_penrose_diagram()
        self.play(Create(diagram), run_time=3)
        self.wait(1)
        
        # Add detailed labels
        labels = self.add_detailed_penrose_labels()
        self.play(*[Write(label) for label in labels], run_time=2)
        self.wait(1)
        
        # Show conformal factor
        conformal = MathTex(
            r"\tilde{g}_{\mu\nu} = \Omega^2 g_{\mu\nu}",
            font_size=32,
            color=YELLOW
        )
        conformal.to_edge(DOWN)
        self.play(Write(conformal))
        self.wait(2)
        
        # Show null geodesics
        null_geodesics = self.show_null_geodesics()
        self.play(Create(null_geodesics), run_time=2)
        self.wait(2)
    
    def create_detailed_penrose_diagram(self) -> VGroup:
        """Create detailed Penrose diagram"""
        # Main diamond
        diamond = Polygon(
            np.array([0, 2, 0]),
            np.array([2, 0, 0]),
            np.array([0, -2, 0]),
            np.array([-2, 0, 0]),
            color=WHITE,
            stroke_width=3
        )
        
        # Light cones from center
        light_cone_up = Polygon(
            np.array([0, 0, 0]),
            np.array([1, 1, 0]),
            np.array([0, 2, 0]),
            np.array([-1, 1, 0]),
            color=YELLOW,
            fill_opacity=0.3
        )
        
        light_cone_down = Polygon(
            np.array([0, 0, 0]),
            np.array([1, -1, 0]),
            np.array([0, -2, 0]),
            np.array([-1, -1, 0]),
            color=YELLOW,
            fill_opacity=0.3
        )
        
        # Spacelike surfaces
        spacelike = Polygon(
            np.array([-1.5, 0, 0]),
            np.array([1.5, 0, 0]),
            np.array([1.5, -0.3, 0]),
            np.array([-1.5, -0.3, 0]),
            color=BLUE,
            fill_opacity=0.2
        )
        
        return VGroup(diamond, light_cone_up, light_cone_down, spacelike)
    
    def add_detailed_penrose_labels(self) -> List[MathTex]:
        """Add detailed Penrose diagram labels"""
        labels = [
            MathTex("i^0", font_size=28).move_to(np.array([0, 0, 0])),
            MathTex("i^+", font_size=28, color=RED).move_to(np.array([0, 2, 0])),
            MathTex("i^-", font_size=28, color=RED).move_to(np.array([0, -2, 0])),
            MathTex(r"\mathscr{I}^+", font_size=28, color=GREEN).move_to(np.array([2, 0, 0])),
            MathTex(r"\mathscr{I}^-", font_size=28, color=GREEN).move_to(np.array([-2, 0, 0]))
        ]
        return labels
    
    def show_null_geodesics(self) -> VGroup:
        """Show null geodesics"""
        # Null geodesics at 45 degrees
        geodesic1 = Line(
            np.array([-1.5, -1.5, 0]),
            np.array([1.5, 1.5, 0]),
            color=RED,
            stroke_width=2
        )
        geodesic2 = Line(
            np.array([-1.5, 1.5, 0]),
            np.array([1.5, -1.5, 0]),
            color=RED,
            stroke_width=2
        )
        return VGroup(geodesic1, geodesic2)


class TwistorSpinNetworkConnectionDetailed(Scene):
    """
    Detailed connection between Twistor Theory and Spin Networks
    
    Shows how twistors quantize to spin networks in Loop Quantum Gravity.
    """
    
    def construct(self):
        title = MathTex(
            r"\text{Twistor Theory } \longleftrightarrow \text{ Spin Networks}",
            font_size=42,
            color=PURPLE
        )
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Left side: Twistor
        twistor_group = self.create_detailed_twistor()
        twistor_group.shift(LEFT * 4)
        
        # Right side: Spin Network
        spin_group = self.create_detailed_spin_network()
        spin_group.shift(RIGHT * 4)
        
        # Connection
        arrow = DoubleArrow(
            twistor_group.get_right(),
            spin_group.get_left(),
            color=GREEN,
            stroke_width=5,
            buff=0.5
        )
        
        # Quantization label
        quantize = MathTex(
            r"\text{Quantization}",
            font_size=32,
            color=YELLOW
        )
        quantize.next_to(arrow, UP, buff=0.3)
        
        self.play(
            Create(twistor_group),
            Create(spin_group),
            run_time=2
        )
        self.play(Create(arrow), Write(quantize), run_time=2)
        self.wait(1)
        
        # Mathematical relationship
        relation = MathTex(
            r"Z^\alpha \in \mathbb{T} \quad \rightarrow \quad \Gamma_{spin} \in \mathcal{H}_{LQG}",
            font_size=28
        )
        relation.to_edge(DOWN)
        self.play(Write(relation), run_time=3)
        self.wait(2)
        
        # Show quantization formula
        quant_formula = MathTex(
            r"\hat{A}_S = 8\pi \gamma \ell_P^2 \sum_{p \in S} \sqrt{\hat{j}_p(\hat{j}_p + 1)}",
            font_size=24
        )
        quant_formula.next_to(relation, UP, buff=0.5)
        self.play(Write(quant_formula), run_time=3)
        self.wait(3)
    
    def create_detailed_twistor(self) -> VGroup:
        """Create detailed twistor representation"""
        # Twistor as complex plane
        circle = Circle(radius=1, color=BLUE, stroke_width=3)
        
        # Twistor coordinates
        coords = MathTex(
            r"Z^\alpha = \begin{pmatrix} \omega^A \\ \pi_{A'} \end{pmatrix}",
            font_size=24
        )
        coords.next_to(circle, DOWN, buff=0.3)
        
        # Null condition
        null = MathTex(
            r"Z^\alpha \bar{Z}_\alpha = 0",
            font_size=20,
            color=YELLOW
        )
        null.next_to(coords, DOWN, buff=0.2)
        
        return VGroup(circle, coords, null)
    
    def create_detailed_spin_network(self) -> VGroup:
        """Create detailed spin network representation"""
        # Simple network
        node1 = Dot(color=WHITE, radius=0.15).shift(UP * 0.5)
        node2 = Dot(color=WHITE, radius=0.15).shift(DOWN * 0.5)
        edge = Line(
            node1.get_center(),
            node2.get_center(),
            color=BLUE,
            stroke_width=4
        )
        
        # Spin label
        spin_label = MathTex("j", font_size=24)
        spin_label.next_to(edge, RIGHT, buff=0.2)
        
        # Network label
        network_label = MathTex(r"\Gamma", font_size=24)
        network_label.next_to(edge, DOWN, buff=0.5)
        
        return VGroup(node1, node2, edge, spin_label, network_label)


class QuantumGeometryDetailed(ThreeDScene):
    """
    Detailed Quantum Geometry from Spin Networks
    
    Shows how spin networks give rise to discrete quantum geometry.
    """
    
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)
        
        title = MathTex(
            r"\text{Quantum Geometry from Spin Networks}",
            font_size=42,
            color=GREEN
        )
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.wait(1)
        
        # Create 3D tetrahedral network
        tetrahedron = self.create_tetrahedral_network()
        self.play(Create(tetrahedron), run_time=3)
        self.wait(1)
        
        # Area quantization
        area_formula = MathTex(
            r"A_S = 8\pi \gamma \ell_P^2 \sum_{p \in S} \sqrt{j_p(j_p + 1)}",
            font_size=28,
            color=YELLOW
        )
        area_formula.to_corner(UL)
        self.add_fixed_in_frame_mobjects(area_formula)
        self.wait(2)
        
        # Volume quantization
        volume_formula = MathTex(
            r"V = \left( \frac{8\pi \gamma}{3} \right)^{3/2} \ell_P^3 \sum_v \sqrt{|\det(\vec{j}_v)|}",
            font_size=24
        )
        volume_formula.next_to(area_formula, DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(volume_formula)
        self.wait(2)
        
        # Animate rotation
        self.play(
            Rotate(tetrahedron, 2 * PI / 3, axis=UP),
            run_time=3
        )
        self.wait(2)
    
    def create_tetrahedral_network(self) -> VGroup:
        """Create 3D tetrahedral spin network"""
        # Tetrahedron vertices
        vertices = [
            np.array([1, 1, 1]),
            np.array([-1, -1, 1]),
            np.array([1, -1, -1]),
            np.array([-1, 1, -1])
        ]
        
        # Nodes
        nodes = []
        for v in vertices:
            node = Sphere(radius=0.2, color=WHITE, fill_opacity=1)
            node.move_to(v)
            nodes.append(node)
        
        # Edges
        edges = []
        for i in range(len(vertices)):
            for j in range(i + 1, len(vertices)):
                edge = Line3D(
                    vertices[i],
                    vertices[j],
                    color=BLUE,
                    stroke_width=5
                )
                edges.append(edge)
        
        return VGroup(*nodes, *edges)


class MathematicalFormulations(Scene):
    """
    Comprehensive mathematical formulations
    
    All key equations in twistor theory and spin networks.
    """
    
    def construct(self):
        title = MathTex(
            r"\text{Mathematical Formulations}",
            font_size=48,
            color=TEAL
        )
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Create scrollable list of equations
        equations = self.create_equation_list()
        
        # Animate equations appearing
        for i, eq in enumerate(equations):
            self.play(Write(eq), run_time=2)
            if i < len(equations) - 1:
                self.wait(1)
        
        self.wait(3)
    
    def create_equation_list(self) -> List[MathTex]:
        """Create list of key equations"""
        equations = [
            # Twistor equation
            MathTex(
                r"\nabla_{AA'} \omega^B = -i \epsilon_A^B \pi_{A'}",
                font_size=36
            ),
            
            # Null twistor
            MathTex(
                r"Z^\alpha \bar{Z}_\alpha = \omega^A \bar{\pi}_A + \pi_{A'} \bar{\omega}^{A'} = 0",
                font_size=32
            ),
            
            # Twistor incidence
            MathTex(
                r"\omega^A = i x^{AA'} \pi_{A'}",
                font_size=36
            ),
            
            # Spin network amplitude
            MathTex(
                r"A(\Gamma) = \prod_{e \in E} (2j_e + 1) \prod_{v \in V} \begin{Bmatrix} j_1 & j_2 & j_3 \\ j_4 & j_5 & j_6 \end{Bmatrix}",
                font_size=28
            ),
            
            # Area quantization
            MathTex(
                r"A_S = 8\pi \gamma \ell_P^2 \sum_{p \in S} \sqrt{j_p(j_p + 1)}",
                font_size=32
            ),
            
            # Volume quantization
            MathTex(
                r"V = \left( \frac{8\pi \gamma}{3} \right)^{3/2} \ell_P^3 \sum_v \sqrt{|\det(\vec{j}_v)|}",
                font_size=28
            ),
            
            # Hamiltonian constraint
            MathTex(
                r"\hat{H} |\Gamma\rangle = 0",
                font_size=36
            )
        ]
        
        # Arrange vertically
        equations[0].shift(UP * 2.5)
        for i in range(1, len(equations)):
            equations[i].next_to(equations[i-1], DOWN, buff=0.4)
        
        return equations


class SpinFoamEvolution(Scene):
    """
    Spin Foam Evolution
    
    Shows how spin networks evolve into spin foams.
    """
    
    def construct(self):
        title = MathTex(
            r"\text{Spin Foam Evolution}",
            font_size=48,
            color=RED
        )
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Initial network
        network1 = self.create_network_1()
        network1.shift(LEFT * 3)
        
        # Intermediate
        network2 = self.create_network_2()
        
        # Final foam
        network3 = self.create_network_3()
        network3.shift(RIGHT * 3)
        
        # Evolution arrows
        arrow1 = Arrow(
            network1.get_right(),
            network2.get_left(),
            color=YELLOW,
            stroke_width=4
        )
        arrow2 = Arrow(
            network2.get_right(),
            network3.get_left(),
            color=YELLOW,
            stroke_width=4
        )
        
        # Labels
        label1 = MathTex(r"\Gamma_1", font_size=24).next_to(network1, DOWN)
        label2 = MathTex(r"\Gamma_2", font_size=24).next_to(network2, DOWN)
        label3 = MathTex(r"\text{Spin Foam}", font_size=24).next_to(network3, DOWN)
        
        self.play(
            Create(network1),
            Write(label1),
            run_time=1
        )
        self.play(Create(arrow1), run_time=1)
        self.play(
            Create(network2),
            Write(label2),
            run_time=1
        )
        self.play(Create(arrow2), run_time=1)
        self.play(
            Create(network3),
            Write(label3),
            run_time=1
        )
        self.wait(2)
        
        # Foam amplitude
        foam_amp = MathTex(
            r"A(\text{foam}) = \sum_{j_f, i_v} \prod_f (2j_f + 1) \prod_v A_v(j_f, i_v)",
            font_size=24
        )
        foam_amp.to_edge(DOWN)
        self.play(Write(foam_amp), run_time=3)
        self.wait(2)
    
    def create_network_1(self) -> VGroup:
        """Initial network"""
        node = Dot(color=WHITE, radius=0.2)
        return VGroup(node)
    
    def create_network_2(self) -> VGroup:
        """Intermediate network"""
        node1 = Dot(color=WHITE, radius=0.15).shift(UP * 0.3)
        node2 = Dot(color=WHITE, radius=0.15).shift(DOWN * 0.3)
        edge = Line(node1.get_center(), node2.get_center(), color=BLUE)
        return VGroup(node1, node2, edge)
    
    def create_network_3(self) -> VGroup:
        """Spin foam representation"""
        # More complex structure
        nodes = [
            Dot(color=WHITE, radius=0.12).shift(UP * 0.4 + LEFT * 0.3),
            Dot(color=WHITE, radius=0.12).shift(UP * 0.4 + RIGHT * 0.3),
            Dot(color=WHITE, radius=0.12).shift(DOWN * 0.4)
        ]
        edges = [
            Line(nodes[0].get_center(), nodes[2].get_center(), color=BLUE),
            Line(nodes[1].get_center(), nodes[2].get_center(), color=BLUE),
            Line(nodes[0].get_center(), nodes[1].get_center(), color=BLUE)
        ]
        return VGroup(*nodes, *edges)


# Main execution
if __name__ == "__main__":
    """
    Enhanced visualization scenes for Twistor Theory and Spin Networks.
    
    Render commands:
    manim -pql twistor_spin_networks_enhanced.py TwistorSpaceDetailed
    manim -pql twistor_spin_networks_enhanced.py SpinNetworkDetailed
    manim -pql twistor_spin_networks_enhanced.py PenroseDiagramDetailed
    manim -pql twistor_spin_networks_enhanced.py TwistorSpinNetworkConnectionDetailed
    manim -pql twistor_spin_networks_enhanced.py QuantumGeometryDetailed
    manim -pql twistor_spin_networks_enhanced.py MathematicalFormulations
    manim -pql twistor_spin_networks_enhanced.py SpinFoamEvolution
    """
