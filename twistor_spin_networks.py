"""
Twistor Theory and Spin Networks Visualization using Manim

This script provides comprehensive visualizations of:
1. Twistor space geometry
2. Spin networks and their evolution
3. Penrose diagrams
4. Quantum geometry representations
5. Mathematical relationships between twistors and spin networks

Author: Generated for educational purposes
"""

from manim import *
import numpy as np
from typing import List, Tuple, Optional


class TwistorSpace(ThreeDScene):
    """Visualization of Twistor Space Geometry"""
    
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        
        # Title
        title = Text("Twistor Space", font_size=48)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.wait(1)
        
        # Create twistor space axes
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-3, 3, 1],
            axis_config={"color": GRAY}
        )
        self.add(axes)
        
        # Twistor as a complex 2-plane in CP^3
        # Represented as a surface
        twistor_surface = ParametricSurface(
            lambda u, v: np.array([
                2 * np.cos(u) * np.cos(v),
                2 * np.sin(u) * np.cos(v),
                2 * np.sin(v)
            ]),
            u_range=[0, 2 * PI],
            v_range=[-PI/2, PI/2],
            fill_opacity=0.3,
            fill_color=BLUE,
            checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(20, 20)
        )
        self.play(Create(twistor_surface), run_time=2)
        
        # Add twistor coordinates
        twistor_label = MathTex(
            r"Z^\alpha = (\omega^A, \pi_{A'})",
            font_size=36
        )
        twistor_label.to_corner(UL)
        self.add_fixed_in_frame_mobjects(twistor_label)
        self.wait(2)
        
        # Show null twistor condition
        null_condition = MathTex(
            r"Z^\alpha \bar{Z}_\alpha = 0",
            font_size=32
        )
        null_condition.next_to(twistor_label, DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(null_condition)
        self.wait(2)
        
        # Animate twistor evolution
        self.play(
            Rotate(twistor_surface, PI/2, axis=UP),
            run_time=3
        )
        self.wait(2)


class SpinNetwork(Scene):
    """Visualization of Spin Networks"""
    
    def construct(self):
        # Title
        title = Text("Spin Networks", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Create a simple spin network
        nodes = self.create_spin_network_nodes()
        edges = self.create_spin_network_edges(nodes)
        
        # Animate creation
        self.play(*[Create(node) for node in nodes], run_time=2)
        self.play(*[Create(edge) for edge in edges], run_time=2)
        
        # Add spin labels
        spin_labels = self.add_spin_labels(nodes, edges)
        self.play(*[Write(label) for label in spin_labels], run_time=2)
        
        # Show gauge invariance
        gauge_text = Text("Gauge Invariant", font_size=32, color=GREEN)
        gauge_text.to_edge(DOWN)
        self.play(Write(gauge_text))
        self.wait(2)
        
        # Animate network transformation
        self.animate_network_transformation(nodes, edges)
        self.wait(2)
    
    def create_spin_network_nodes(self) -> List[Circle]:
        """Create nodes for spin network"""
        positions = [
            np.array([-2, 1, 0]),
            np.array([2, 1, 0]),
            np.array([0, -1, 0]),
            np.array([-1, 0.5, 0]),
            np.array([1, 0.5, 0])
        ]
        
        nodes = []
        for pos in positions:
            node = Circle(radius=0.2, color=WHITE, fill_opacity=1)
            node.move_to(pos)
            nodes.append(node)
        
        return nodes
    
    def create_spin_network_edges(self, nodes: List[Circle]) -> List[Line]:
        """Create edges connecting nodes"""
        connections = [
            (0, 3), (3, 2), (2, 4), (4, 1),
            (0, 2), (1, 2)
        ]
        
        edges = []
        for i, j in connections:
            edge = Line(
                nodes[i].get_center(),
                nodes[j].get_center(),
                color=BLUE,
                stroke_width=3
            )
            edges.append(edge)
        
        return edges
    
    def add_spin_labels(self, nodes: List[Circle], edges: List[Line]) -> List[MathTex]:
        """Add spin labels to edges"""
        labels = []
        spins = ["1/2", "1", "1/2", "1", "1", "1/2"]
        
        for i, edge in enumerate(edges):
            midpoint = edge.get_center()
            label = MathTex(f"j={spins[i]}", font_size=20)
            label.move_to(midpoint + 0.3 * UP)
            labels.append(label)
        
        return labels
    
    def animate_network_transformation(self, nodes: List[Circle], edges: List[Line]):
        """Animate a gauge transformation"""
        # Create new positions
        new_positions = [
            np.array([-1.5, 1.2, 0]),
            np.array([1.5, 1.2, 0]),
            np.array([0, -0.8, 0]),
            np.array([-0.8, 0.6, 0]),
            np.array([0.8, 0.6, 0])
        ]
        
        animations = []
        for node, new_pos in zip(nodes, new_positions):
            animations.append(node.animate.move_to(new_pos))
        
        # Update edges
        connections = [
            (0, 3), (3, 2), (2, 4), (4, 1),
            (0, 2), (1, 2)
        ]
        
        edge_animations = []
        for edge, (i, j) in zip(edges, connections):
            new_edge = Line(
                nodes[i].get_center(),
                nodes[j].get_center(),
                color=BLUE,
                stroke_width=3
            )
            edge_animations.append(Transform(edge, new_edge))
        
        self.play(*animations, *edge_animations, run_time=2)


class PenroseDiagram(Scene):
    """Penrose Diagram Visualization"""
    
    def construct(self):
        title = Text("Penrose Diagram", font_size=48, color=ORANGE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Create conformal compactification
        diagram = self.create_penrose_diagram()
        self.play(Create(diagram), run_time=2)
        
        # Add labels
        labels = self.add_penrose_labels()
        self.play(*[Write(label) for label in labels], run_time=2)
        
        # Show null infinity
        null_infinity = self.show_null_infinity()
        self.play(Create(null_infinity), run_time=2)
        self.wait(2)
    
    def create_penrose_diagram(self) -> VGroup:
        """Create Penrose diagram structure"""
        # Diamond shape representing conformal compactification
        diamond = Polygon(
            np.array([0, 2, 0]),
            np.array([2, 0, 0]),
            np.array([0, -2, 0]),
            np.array([-2, 0, 0]),
            color=WHITE,
            stroke_width=2
        )
        
        # Light cones
        light_cone_1 = Polygon(
            np.array([0, 0, 0]),
            np.array([1, 1, 0]),
            np.array([0, 2, 0]),
            np.array([-1, 1, 0]),
            color=YELLOW,
            fill_opacity=0.2
        )
        
        light_cone_2 = Polygon(
            np.array([0, 0, 0]),
            np.array([1, -1, 0]),
            np.array([0, -2, 0]),
            np.array([-1, -1, 0]),
            color=YELLOW,
            fill_opacity=0.2
        )
        
        return VGroup(diamond, light_cone_1, light_cone_2)
    
    def add_penrose_labels(self) -> List[Text]:
        """Add labels to Penrose diagram"""
        labels = [
            Text("i⁰", font_size=24).move_to(np.array([0, 0, 0])),
            Text("i⁺", font_size=24).move_to(np.array([0, 2, 0])),
            Text("i⁻", font_size=24).move_to(np.array([0, -2, 0])),
            Text("ℐ⁺", font_size=24).move_to(np.array([2, 0, 0])),
            Text("ℐ⁻", font_size=24).move_to(np.array([-2, 0, 0]))
        ]
        return labels
    
    def show_null_infinity(self) -> VGroup:
        """Show null infinity boundaries"""
        null_plus = Arc(
            radius=2,
            angle=PI,
            start_angle=0,
            color=RED,
            stroke_width=3
        )
        null_minus = Arc(
            radius=2,
            angle=PI,
            start_angle=PI,
            color=RED,
            stroke_width=3
        )
        return VGroup(null_plus, null_minus)


class TwistorSpinNetworkConnection(Scene):
    """Connection between Twistor Theory and Spin Networks"""
    
    def construct(self):
        title = Text(
            "Twistor Theory ↔ Spin Networks",
            font_size=42,
            color=PURPLE
        )
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Show twistor on left
        twistor_side = self.create_twistor_representation()
        twistor_side.shift(LEFT * 3)
        
        # Show spin network on right
        spin_side = self.create_spin_network_representation()
        spin_side.shift(RIGHT * 3)
        
        # Create connection arrow
        arrow = DoubleArrow(
            twistor_side.get_right(),
            spin_side.get_left(),
            color=GREEN,
            stroke_width=4
        )
        
        # Mathematical relationship
        relation = MathTex(
            r"Z^\alpha \leftrightarrow \Gamma_{spin}",
            font_size=32
        )
        relation.next_to(arrow, UP, buff=0.3)
        
        self.play(
            Create(twistor_side),
            Create(spin_side),
            run_time=2
        )
        self.play(Create(arrow), Write(relation), run_time=2)
        self.wait(2)
        
        # Show quantization
        quantize_text = Text(
            "Quantization: Twistor → Spin Network",
            font_size=28,
            color=YELLOW
        )
        quantize_text.to_edge(DOWN)
        self.play(Write(quantize_text))
        self.wait(2)
    
    def create_twistor_representation(self) -> VGroup:
        """Create twistor visualization"""
        circle = Circle(radius=1, color=BLUE)
        center = Dot(color=BLUE)
        label = MathTex("Z^\\alpha", font_size=24)
        label.next_to(circle, DOWN, buff=0.2)
        return VGroup(circle, center, label)
    
    def create_spin_network_representation(self) -> VGroup:
        """Create spin network visualization"""
        # Simple network
        node1 = Dot(color=WHITE).shift(UP * 0.5)
        node2 = Dot(color=WHITE).shift(DOWN * 0.5)
        edge = Line(node1.get_center(), node2.get_center(), color=BLUE)
        label = MathTex("\\Gamma", font_size=24)
        label.next_to(edge, DOWN, buff=0.2)
        return VGroup(node1, node2, edge, label)


class QuantumGeometry(ThreeDScene):
    """Quantum Geometry from Spin Networks"""
    
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)
        
        title = Text("Quantum Geometry", font_size=48, color=GREEN)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.wait(1)
        
        # Create 3D spin network
        network_3d = self.create_3d_spin_network()
        self.play(Create(network_3d), run_time=3)
        
        # Show area quantization
        area_text = MathTex(
            r"A = 8\pi \gamma \ell_P^2 \sqrt{j(j+1)}",
            font_size=32
        )
        area_text.to_corner(UL)
        self.add_fixed_in_frame_mobjects(area_text)
        self.wait(2)
        
        # Animate network evolution
        self.play(
            Rotate(network_3d, PI/3, axis=UP),
            run_time=3
        )
        self.wait(2)
    
    def create_3d_spin_network(self) -> VGroup:
        """Create 3D spin network structure"""
        # Tetrahedral structure
        vertices = [
            np.array([1, 1, 1]),
            np.array([-1, -1, 1]),
            np.array([1, -1, -1]),
            np.array([-1, 1, -1])
        ]
        
        nodes = [Sphere(radius=0.15, color=WHITE).move_to(v) for v in vertices]
        
        edges = []
        for i in range(len(vertices)):
            for j in range(i + 1, len(vertices)):
                edge = Line3D(
                    vertices[i],
                    vertices[j],
                    color=BLUE,
                    stroke_width=4
                )
                edges.append(edge)
        
        return VGroup(*nodes, *edges)


class TwistorEquation(Scene):
    """Mathematical Formulation of Twistor Theory"""
    
    def construct(self):
        title = Text("Twistor Equations", font_size=48, color=TEAL)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Twistor equation
        twistor_eq = MathTex(
            r"\nabla_{AA'} \omega^B = -i \epsilon_A^B \pi_{A'}",
            font_size=40
        )
        twistor_eq.shift(UP * 1.5)
        self.play(Write(twistor_eq))
        self.wait(2)
        
        # Null twistor condition
        null_eq = MathTex(
            r"Z^\alpha \bar{Z}_\alpha = \omega^A \bar{\pi}_A + \pi_{A'} \bar{\omega}^{A'} = 0",
            font_size=32
        )
        null_eq.next_to(twistor_eq, DOWN, buff=1)
        self.play(Write(null_eq))
        self.wait(2)
        
        # Spin network amplitude
        amplitude = MathTex(
            r"A(\Gamma) = \prod_{edges} (2j_e + 1) \prod_{vertices} \{6j\}",
            font_size=32
        )
        amplitude.next_to(null_eq, DOWN, buff=1)
        self.play(Write(amplitude))
        self.wait(2)
        
        # Connection formula
        connection = MathTex(
            r"Z^\alpha \rightarrow \text{Spin Network Vertex}",
            font_size=28
        )
        connection.to_edge(DOWN)
        self.play(Write(connection))
        self.wait(3)


class SpinNetworkEvolution(Scene):
    """Evolution of Spin Networks"""
    
    def construct(self):
        title = Text("Spin Network Evolution", font_size=48, color=RED)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Create initial network
        network1 = self.create_network_stage_1()
        network1.shift(LEFT * 2.5)
        
        # Create intermediate network
        network2 = self.create_network_stage_2()
        
        # Create final network
        network3 = self.create_network_stage_3()
        network3.shift(RIGHT * 2.5)
        
        # Arrows showing evolution
        arrow1 = Arrow(
            network1.get_right(),
            network2.get_left(),
            color=YELLOW,
            stroke_width=3
        )
        arrow2 = Arrow(
            network2.get_right(),
            network3.get_left(),
            color=YELLOW,
            stroke_width=3
        )
        
        # Labels
        label1 = Text("t₁", font_size=24).next_to(network1, DOWN)
        label2 = Text("t₂", font_size=24).next_to(network2, DOWN)
        label3 = Text("t₃", font_size=24).next_to(network3, DOWN)
        
        self.play(Create(network1), Write(label1), run_time=1)
        self.wait(1)
        self.play(Create(arrow1), run_time=1)
        self.play(Create(network2), Write(label2), run_time=1)
        self.wait(1)
        self.play(Create(arrow2), run_time=1)
        self.play(Create(network3), Write(label3), run_time=1)
        self.wait(2)
    
    def create_network_stage_1(self) -> VGroup:
        """Initial network state"""
        node = Dot(color=WHITE)
        return VGroup(node)
    
    def create_network_stage_2(self) -> VGroup:
        """Intermediate network state"""
        node1 = Dot(color=WHITE).shift(UP * 0.3)
        node2 = Dot(color=WHITE).shift(DOWN * 0.3)
        edge = Line(node1.get_center(), node2.get_center(), color=BLUE)
        return VGroup(node1, node2, edge)
    
    def create_network_stage_3(self) -> VGroup:
        """Final network state"""
        nodes = [
            Dot(color=WHITE).shift(UP * 0.5 + LEFT * 0.3),
            Dot(color=WHITE).shift(UP * 0.5 + RIGHT * 0.3),
            Dot(color=WHITE).shift(DOWN * 0.5)
        ]
        edges = [
            Line(nodes[0].get_center(), nodes[2].get_center(), color=BLUE),
            Line(nodes[1].get_center(), nodes[2].get_center(), color=BLUE),
            Line(nodes[0].get_center(), nodes[1].get_center(), color=BLUE)
        ]
        return VGroup(*nodes, *edges)


class ComprehensiveVisualization(Scene):
    """Comprehensive visualization combining all concepts"""
    
    def construct(self):
        # Main title
        main_title = Text(
            "Twistor Theory & Spin Networks",
            font_size=56,
            color=GOLD
        )
        main_title.to_edge(UP)
        self.play(Write(main_title))
        self.wait(2)
        
        # Create overview diagram
        overview = self.create_overview_diagram()
        self.play(Create(overview), run_time=3)
        self.wait(2)
        
        # Key concepts
        concepts = VGroup(
            Text("• Twistor Space: CP³", font_size=28, color=BLUE),
            Text("• Spin Networks: Graph with spins", font_size=28, color=GREEN),
            Text("• Quantum Geometry: Discrete area/volume", font_size=28, color=YELLOW),
            Text("• Loop Quantum Gravity: Spin foam", font_size=28, color=RED)
        )
        concepts.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        concepts.next_to(overview, DOWN, buff=1)
        
        self.play(Write(concepts), run_time=3)
        self.wait(3)
    
    def create_overview_diagram(self) -> VGroup:
        """Create overview diagram"""
        # Central circle representing quantum geometry
        center = Circle(radius=1.5, color=GOLD, stroke_width=3)
        
        # Surrounding elements
        twistor = Circle(radius=0.5, color=BLUE).shift(UP * 2.5)
        spin = Circle(radius=0.5, color=GREEN).shift(DOWN * 2.5)
        penrose = Circle(radius=0.5, color=ORANGE).shift(LEFT * 2.5)
        quantum = Circle(radius=0.5, color=RED).shift(RIGHT * 2.5)
        
        # Connections
        connections = [
            Line(center.get_top(), twistor.get_bottom(), color=GRAY),
            Line(center.get_bottom(), spin.get_top(), color=GRAY),
            Line(center.get_left(), penrose.get_right(), color=GRAY),
            Line(center.get_right(), quantum.get_left(), color=GRAY)
        ]
        
        # Labels
        labels = VGroup(
            Text("Twistor", font_size=20).next_to(twistor, UP),
            Text("Spin Net", font_size=20).next_to(spin, DOWN),
            Text("Penrose", font_size=20).next_to(penrose, LEFT),
            Text("Quantum", font_size=20).next_to(quantum, RIGHT)
        )
        
        return VGroup(center, twistor, spin, penrose, quantum, *connections, labels)


# Main execution
if __name__ == "__main__":
    """
    To render individual scenes:
    
    manim -pql twistor_spin_networks.py TwistorSpace
    manim -pql twistor_spin_networks.py SpinNetwork
    manim -pql twistor_spin_networks.py PenroseDiagram
    manim -pql twistor_spin_networks.py TwistorSpinNetworkConnection
    manim -pql twistor_spin_networks.py QuantumGeometry
    manim -pql twistor_spin_networks.py TwistorEquation
    manim -pql twistor_spin_networks.py SpinNetworkEvolution
    manim -pql twistor_spin_networks.py ComprehensiveVisualization
    
    To render all scenes in sequence:
    manim -pql twistor_spin_networks.py ComprehensiveVisualization
    
    Quality options:
    -pql: preview, low quality
    -pqm: preview, medium quality
    -pqh: preview, high quality
    -pqs: preview, 4K quality
    """
