"""
Spin Network Visualization using Manim
========================================
This module provides comprehensive visualizations of spin network concepts
and their role in loop quantum gravity using the Manim library.

Author: Generated Framework
Date: 2025
"""

from manim import *
import numpy as np
from itertools import combinations

# ==================== COLOR SCHEME ====================
SPIN_COLOR_1 = "#FF6B9D"  # Pink
SPIN_COLOR_2 = "#C44569"  # Dark pink
SPIN_COLOR_3 = "#FFA07A"  # Light salmon
NODE_COLOR = "#4A90E2"  # Blue
EDGE_COLOR = "#50E3C2"  # Teal
INTERTWINER_COLOR = "#F5A623"  # Orange
QUANTUM_COLOR = "#B8E986"  # Light green


# ==================== SCENE 1: INTRODUCTION ====================
class SpinNetworkIntroduction(Scene):
    """Introduction to spin networks"""
    
    def construct(self):
        # Title
        title = Text("Spin Networks", font_size=72, color=SPIN_COLOR_1)
        subtitle = Text(
            "Quantum States of Geometry",
            font_size=36,
            color=WHITE
        ).next_to(title, DOWN)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Key concepts
        concepts = VGroup(
            Text("• Graph with labeled edges and vertices", font_size=32),
            Text("• Edges: spin-j representations of SU(2)", font_size=32),
            Text("• Vertices: intertwiners", font_size=32),
            Text("• Quantum states of 3D geometry", font_size=32),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        for concept in concepts:
            self.play(FadeIn(concept, shift=RIGHT))
            self.wait(0.5)
        
        self.wait(2)
        self.play(FadeOut(concepts))


# ==================== SCENE 2: BASIC SPIN NETWORK ====================
class BasicSpinNetwork(Scene):
    """Visualization of a basic spin network structure"""
    
    def construct(self):
        # Title
        title = Text("Basic Spin Network Structure", font_size=48, color=NODE_COLOR)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Create vertices
        v1 = Dot(LEFT * 3, color=NODE_COLOR, radius=0.15)
        v2 = Dot(RIGHT * 3, color=NODE_COLOR, radius=0.15)
        v3 = Dot(UP * 2, color=NODE_COLOR, radius=0.15)
        v4 = Dot(DOWN * 2, color=NODE_COLOR, radius=0.15)
        
        vertices = VGroup(v1, v2, v3, v4)
        
        # Create edges with spin labels
        edges = VGroup()
        
        # Edge data: (start, end, spin, color)
        edge_data = [
            (v1, v2, "1/2", SPIN_COLOR_1),
            (v1, v3, "1", SPIN_COLOR_2),
            (v1, v4, "1/2", SPIN_COLOR_1),
            (v2, v3, "3/2", SPIN_COLOR_3),
            (v2, v4, "1", SPIN_COLOR_2),
        ]
        
        edge_objects = []
        for start, end, spin, color in edge_data:
            edge = Arrow(
                start.get_center(),
                end.get_center(),
                buff=0.15,
                color=color,
                stroke_width=6,
                max_tip_length_to_length_ratio=0.15
            )
            edges.add(edge)
            edge_objects.append((edge, spin, color))
        
        # Animate creation
        self.play(FadeIn(vertices, scale=0.5))
        self.play(Create(edges), run_time=2)
        
        # Add spin labels
        labels = VGroup()
        for edge, spin, color in edge_objects:
            label = MathTex(f"j={spin}", font_size=28, color=color)
            label.move_to(edge.get_center())
            label.shift(UP * 0.3)
            labels.add(label)
        
        self.play(Write(labels))
        
        # Add vertex labels
        vertex_labels = VGroup(
            MathTex(r"\iota_1", font_size=32).next_to(v1, LEFT),
            MathTex(r"\iota_2", font_size=32).next_to(v2, RIGHT),
            MathTex(r"\iota_3", font_size=32).next_to(v3, UP),
            MathTex(r"\iota_4", font_size=32).next_to(v4, DOWN),
        )
        
        self.play(Write(vertex_labels))
        
        # Formula
        formula = MathTex(
            r"|\Gamma, \{j_e\}, \{\iota_v\}\rangle",
            font_size=40,
            color=QUANTUM_COLOR
        ).to_edge(DOWN)
        
        box = SurroundingRectangle(formula, color=QUANTUM_COLOR, buff=0.2)
        
        self.play(Write(formula))
        self.play(Create(box))
        
        self.wait(3)


# ==================== SCENE 3: SU(2) REPRESENTATIONS ====================
class SU2Representations(Scene):
    """Visualization of SU(2) representations on edges"""
    
    def construct(self):
        # Title
        title = Text("SU(2) Representations", font_size=52, color=EDGE_COLOR)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Representation table
        table_data = [
            ["Spin j", "Dimension", "Physical Meaning"],
            ["0", "1", "Trivial (no area)"],
            ["1/2", "2", "Minimal area"],
            ["1", "3", "Elementary excitation"],
            ["3/2", "4", "Higher excitation"],
        ]
        
        table = Table(
            table_data,
            include_outer_lines=True,
            line_config={"stroke_width": 2, "color": WHITE}
        ).scale(0.6).shift(UP * 1)
        
        # Color code the spins
        table.get_entries((2, 1)).set_color(YELLOW)
        table.get_entries((3, 1)).set_color(SPIN_COLOR_1)
        table.get_entries((4, 1)).set_color(SPIN_COLOR_2)
        table.get_entries((5, 1)).set_color(SPIN_COLOR_3)
        
        self.play(Create(table))
        self.wait(2)
        
        # Area formula
        area_formula = MathTex(
            r"A = 8\pi\gamma\ell_P^2\sqrt{j(j+1)}",
            font_size=44,
            color=QUANTUM_COLOR
        ).shift(DOWN * 2)
        
        area_label = Text(
            "Area eigenvalue for spin-j edge",
            font_size=28,
            color=WHITE
        ).next_to(area_formula, DOWN)
        
        self.play(Write(area_formula))
        self.play(FadeIn(area_label, shift=UP))
        
        # Highlight formula
        box = SurroundingRectangle(area_formula, color=QUANTUM_COLOR, buff=0.2)
        self.play(Create(box))
        
        self.wait(3)


# ==================== SCENE 4: INTERTWINER AT VERTEX ====================
class IntertwinerVertex(Scene):
    """Detailed view of intertwiner at a vertex"""
    
    def construct(self):
        # Title
        title = Text("Intertwiner at Vertex", font_size=52, color=INTERTWINER_COLOR)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Central vertex
        center = Dot(ORIGIN, color=NODE_COLOR, radius=0.2)
        center_label = MathTex(r"\iota", font_size=48, color=INTERTWINER_COLOR)
        center_label.next_to(center, DOWN, buff=0.3)
        
        self.play(FadeIn(center, scale=0.5))
        self.play(Write(center_label))
        
        # Four edges with different spins
        num_edges = 4
        angles = [i * TAU / num_edges for i in range(num_edges)]
        spins = ["1/2", "1", "1/2", "1"]
        colors = [SPIN_COLOR_1, SPIN_COLOR_2, SPIN_COLOR_1, SPIN_COLOR_2]
        
        edges = VGroup()
        edge_labels = VGroup()
        hilbert_labels = VGroup()
        
        for i, (angle, spin, color) in enumerate(zip(angles, spins, colors)):
            # Edge endpoint
            end_point = 2.5 * np.array([np.cos(angle), np.sin(angle), 0])
            
            # Arrow
            arrow = Arrow(
                center.get_center(),
                end_point,
                buff=0.2,
                color=color,
                stroke_width=6,
                max_tip_length_to_length_ratio=0.15
            )
            edges.add(arrow)
            
            # Spin label
            mid_point = 1.5 * np.array([np.cos(angle), np.sin(angle), 0])
            label = MathTex(f"j_{i+1}={spin}", font_size=28, color=color)
            label.move_to(mid_point)
            edge_labels.add(label)
            
            # Hilbert space label
            outer_point = 3 * np.array([np.cos(angle), np.sin(angle), 0])
            dim = int(2 * eval(spin) + 1)
            hilbert = MathTex(rf"\mathcal{{H}}_{{{dim}}}", font_size=24, color=color)
            hilbert.move_to(outer_point)
            hilbert_labels.add(hilbert)
        
        self.play(Create(edges), run_time=2)
        self.play(Write(edge_labels))
        self.wait(1)
        self.play(Write(hilbert_labels))
        
        # Intertwiner definition
        intertwiner_def = MathTex(
            r"\iota \in \text{Inv}\left(\bigotimes_{i=1}^4 V_{j_i}\right)",
            font_size=36
        ).to_edge(DOWN).shift(UP * 0.5)
        
        invariant_text = Text(
            "SU(2)-invariant map",
            font_size=28,
            color=INTERTWINER_COLOR
        ).next_to(intertwiner_def, DOWN)
        
        self.play(Write(intertwiner_def))
        self.play(Write(invariant_text))
        
        self.wait(3)


# ==================== SCENE 5: 6J-SYMBOL ====================
class SixJSymbol(ThreeDScene):
    """Visualization of 6j-symbol as tetrahedral graph"""
    
    def construct(self):
        # Set camera
        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)
        
        # Title
        title = Text("Wigner 6j-Symbol", font_size=48, color=GOLD)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        
        # Tetrahedron vertices
        vertices_3d = [
            np.array([0, 0, 0]),
            np.array([2, 0, 0]),
            np.array([1, np.sqrt(3), 0]),
            np.array([1, np.sqrt(3)/3, 2*np.sqrt(2/3)])
        ]
        
        # Create dots
        dots = VGroup(*[
            Dot3D(point=v, color=NODE_COLOR, radius=0.1)
            for v in vertices_3d
        ])
        
        self.play(FadeIn(dots, scale=0.5))
        
        # Create edges
        edges_3d = VGroup()
        edge_labels_3d = []
        
        spins = ["j₁", "j₂", "j₃", "j₄", "j₅", "j₆"]
        colors = [RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE]
        
        edge_index = 0
        for i in range(len(vertices_3d)):
            for j in range(i+1, len(vertices_3d)):
                start = vertices_3d[i]
                end = vertices_3d[j]
                
                edge = Line3D(
                    start=start,
                    end=end,
                    color=colors[edge_index],
                    stroke_width=4
                )
                edges_3d.add(edge)
                
                # Label
                mid = (start + end) / 2
                label_text = spins[edge_index]
                edge_labels_3d.append((mid, label_text, colors[edge_index]))
                
                edge_index += 1
        
        self.play(Create(edges_3d), run_time=2)
        
        # Add labels (fixed to camera frame)
        label_group = VGroup()
        for mid, text, color in edge_labels_3d:
            label = MathTex(text, color=color, font_size=32)
            # Position relative to screen
            label.move_to(self.camera.frame_center + 
                         0.3 * (mid - self.camera.frame_center))
            label_group.add(label)
        
        self.add_fixed_in_frame_mobjects(label_group)
        self.play(Write(label_group))
        
        # Rotate
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        
        # 6j-symbol formula
        sixj_formula = MathTex(
            r"\begin{Bmatrix} j_1 & j_2 & j_3 \\ j_4 & j_5 & j_6 \end{Bmatrix}",
            font_size=40,
            color=GOLD
        )
        self.add_fixed_in_frame_mobjects(sixj_formula)
        sixj_formula.to_edge(DOWN)
        
        self.play(Write(sixj_formula))
        self.wait(3)


# ==================== SCENE 6: WILSON LOOP ====================
class WilsonLoop(Scene):
    """Visualization of Wilson loop in spin network"""
    
    def construct(self):
        # Title
        title = Text("Wilson Loop", font_size=52, color=PURPLE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Create loop
        loop_radius = 2
        circle = Circle(radius=loop_radius, color=EDGE_COLOR, stroke_width=8)
        
        self.play(Create(circle))
        
        # Add arrow to show orientation
        arrow_angle = PI / 4
        arrow_start = loop_radius * np.array([np.cos(arrow_angle), np.sin(arrow_angle), 0])
        tangent = np.array([-np.sin(arrow_angle), np.cos(arrow_angle), 0])
        arrow_end = arrow_start + 0.5 * tangent
        
        orientation_arrow = Arrow(
            arrow_start,
            arrow_end,
            color=YELLOW,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.3
        )
        
        self.play(GrowArrow(orientation_arrow))
        
        # Spin label
        spin_label = MathTex(r"j = 1", font_size=40, color=EDGE_COLOR)
        spin_label.move_to(circle.get_center() + RIGHT * 2.8)
        self.play(Write(spin_label))
        
        # Add trace points on loop
        num_points = 8
        points = VGroup()
        for i in range(num_points):
            angle = i * TAU / num_points
            point = Dot(
                loop_radius * np.array([np.cos(angle), np.sin(angle), 0]),
                color=YELLOW,
                radius=0.06
            )
            points.add(point)
        
        self.play(FadeIn(points, lag_ratio=0.1))
        
        # Wilson loop operator formula
        formula = MathTex(
            r"W_\gamma[A] = \text{Tr}\left[\mathcal{P}\exp\left(\oint_\gamma A\right)\right]",
            font_size=36
        ).to_edge(DOWN).shift(UP * 0.5)
        
        interpretation = Text(
            "Holonomy around closed loop",
            font_size=28,
            color=PURPLE
        ).next_to(formula, DOWN)
        
        self.play(Write(formula))
        self.play(Write(interpretation))
        
        # Animate flow around loop
        tracer = Dot(color=RED, radius=0.12)
        tracer.move_to(loop_radius * RIGHT)
        
        self.play(FadeIn(tracer, scale=0.5))
        self.play(
            MoveAlongPath(tracer, circle),
            run_time=3,
            rate_func=linear
        )
        self.play(FadeOut(tracer))
        
        self.wait(2)


# ==================== SCENE 7: THETA GRAPH ====================
class ThetaGraph(Scene):
    """Visualization of theta graph evaluation"""
    
    def construct(self):
        # Title
        title = Text("Theta Graph", font_size=52, color=QUANTUM_COLOR)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Two vertices
        left_vertex = Dot(LEFT * 3, color=NODE_COLOR, radius=0.15)
        right_vertex = Dot(RIGHT * 3, color=NODE_COLOR, radius=0.15)
        
        vertices = VGroup(left_vertex, right_vertex)
        self.play(FadeIn(vertices, scale=0.5))
        
        # Three parallel edges
        edge1 = CurvedArrow(
            left_vertex.get_center(),
            right_vertex.get_center(),
            angle=TAU/6,
            color=SPIN_COLOR_1,
            stroke_width=6
        )
        
        edge2 = Arrow(
            left_vertex.get_center(),
            right_vertex.get_center(),
            color=SPIN_COLOR_2,
            stroke_width=6,
            buff=0.15,
            max_tip_length_to_length_ratio=0.15
        )
        
        edge3 = CurvedArrow(
            left_vertex.get_center(),
            right_vertex.get_center(),
            angle=-TAU/6,
            color=SPIN_COLOR_3,
            stroke_width=6
        )
        
        edges = VGroup(edge1, edge2, edge3)
        self.play(Create(edges), run_time=2)
        
        # Labels
        label1 = MathTex(r"j_1=\frac{1}{2}", font_size=32, color=SPIN_COLOR_1)
        label1.next_to(edge1, UP)
        
        label2 = MathTex(r"j_2=1", font_size=32, color=SPIN_COLOR_2)
        label2.next_to(edge2, DOWN, buff=0.2)
        
        label3 = MathTex(r"j_3=\frac{1}{2}", font_size=32, color=SPIN_COLOR_3)
        label3.next_to(edge3, DOWN)
        
        labels = VGroup(label1, label2, label3)
        self.play(Write(labels))
        
        # Evaluation formula
        evaluation = MathTex(
            r"\langle\Gamma_\theta\rangle = \sum_{m_1,m_2,m_3} C^{j_1 j_2 j_3}_{m_1 m_2 m_3} C^{j_1 j_2 j_3}_{m_1 m_2 m_3}",
            font_size=32
        ).to_edge(DOWN).shift(UP)
        
        cg_text = Text(
            "Clebsch-Gordan coefficients",
            font_size=24,
            color=QUANTUM_COLOR
        ).next_to(evaluation, DOWN)
        
        self.play(Write(evaluation))
        self.play(Write(cg_text))
        
        self.wait(3)


# ==================== SCENE 8: AREA QUANTIZATION ====================
class AreaQuantization(Scene):
    """Visualization of quantized area spectrum"""
    
    def construct(self):
        # Title
        title = Text("Quantized Area Spectrum", font_size=52, color=QUANTUM_COLOR)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Create axes for spectrum
        axes = Axes(
            x_range=[0, 3, 0.5],
            y_range=[0, 8, 1],
            x_length=10,
            y_length=5,
            axis_config={"include_numbers": False},
            tips=False
        ).shift(DOWN * 0.5)
        
        x_label = MathTex(r"j", font_size=36).next_to(axes.x_axis, RIGHT)
        y_label = MathTex(r"A/\ell_P^2", font_size=36).next_to(axes.y_axis, UP)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        
        # Plot discrete spectrum
        spins = [0, 0.5, 1, 1.5, 2, 2.5]
        colors = [YELLOW, SPIN_COLOR_1, SPIN_COLOR_2, SPIN_COLOR_3, BLUE, PURPLE]
        
        dots = VGroup()
        lines = VGroup()
        area_labels = VGroup()
        
        for j, color in zip(spins, colors):
            area_value = 8 * np.pi * 0.2 * np.sqrt(j * (j + 1))  # Scaled for visualization
            
            x_coord = axes.c2p(j, 0)[0]
            y_coord = axes.c2p(0, area_value)[1]
            point = np.array([x_coord, y_coord, 0])
            
            # Vertical line
            line = DashedLine(
                axes.c2p(j, 0),
                point,
                color=color,
                stroke_width=2
            )
            lines.add(line)
            
            # Dot
            dot = Dot(point, color=color, radius=0.1)
            dots.add(dot)
            
            # Spin label
            spin_text = MathTex(f"j={j}", font_size=24, color=color)
            spin_text.next_to(axes.c2p(j, 0), DOWN, buff=0.2)
            area_labels.add(spin_text)
        
        self.play(Create(lines), run_time=2)
        self.play(FadeIn(dots, lag_ratio=0.1))
        self.play(Write(area_labels))
        
        # Area formula
        area_formula = MathTex(
            r"A_j = 8\pi\gamma\ell_P^2\sqrt{j(j+1)}",
            font_size=40,
            color=QUANTUM_COLOR
        ).to_corner(UR)
        
        box = SurroundingRectangle(area_formula, color=QUANTUM_COLOR, buff=0.15)
        
        self.play(Write(area_formula))
        self.play(Create(box))
        
        # Add "discrete" annotation
        discrete_text = Text(
            "Discrete spectrum!",
            font_size=32,
            color=RED
        ).to_corner(UL).shift(DOWN * 2)
        
        self.play(Write(discrete_text))
        
        self.wait(3)


# ==================== SCENE 9: TETRAHEDRAL NETWORK ====================
class TetrahedralNetwork(ThreeDScene):
    """Visualization of tetrahedral spin network"""
    
    def construct(self):
        # Set camera
        self.set_camera_orientation(phi=65 * DEGREES, theta=40 * DEGREES)
        
        # Title
        title = Text("Tetrahedral Spin Network", font_size=48)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        
        # Tetrahedron vertices
        sqrt3 = np.sqrt(3)
        sqrt6 = np.sqrt(6)
        vertices_3d = [
            np.array([0, 0, 0]),
            np.array([2, 0, 0]),
            np.array([1, sqrt3, 0]),
            np.array([1, sqrt3/3, 2*np.sqrt(2/3)])
        ]
        
        # Create vertices
        dots = VGroup(*[
            Sphere(radius=0.1, resolution=(10, 10)).move_to(v).set_color(NODE_COLOR)
            for v in vertices_3d
        ])
        
        self.play(FadeIn(dots, scale=0.5))
        
        # Create edges with spins
        edges_3d = VGroup()
        spins = [1/2, 1/2, 1, 1/2, 1, 1]
        colors = [SPIN_COLOR_1, SPIN_COLOR_1, SPIN_COLOR_2, 
                 SPIN_COLOR_1, SPIN_COLOR_2, SPIN_COLOR_2]
        
        edge_index = 0
        edge_data = []
        
        for i in range(len(vertices_3d)):
            for j in range(i+1, len(vertices_3d)):
                start = vertices_3d[i]
                end = vertices_3d[j]
                
                # Create cylinder for edge
                edge_vector = end - start
                edge_length = np.linalg.norm(edge_vector)
                edge_center = (start + end) / 2
                
                cylinder = Cylinder(
                    radius=0.03,
                    height=edge_length,
                    direction=edge_vector / edge_length,
                    color=colors[edge_index]
                ).move_to(edge_center)
                
                edges_3d.add(cylinder)
                edge_data.append((edge_center, spins[edge_index], colors[edge_index]))
                edge_index += 1
        
        self.play(Create(edges_3d), run_time=2)
        
        # Rotate to show structure
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(6)
        self.stop_ambient_camera_rotation()
        
        # Add description
        description = VGroup(
            Text("4 vertices (nodes)", font_size=28),
            Text("6 edges (spins)", font_size=28),
            Text("4 faces (triangles)", font_size=28),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        self.add_fixed_in_frame_mobjects(description)
        description.to_corner(DL)
        
        for line in description:
            self.play(FadeIn(line, shift=RIGHT))
            self.wait(0.5)
        
        self.wait(2)


# ==================== SCENE 10: COMPLETE SUMMARY ====================
class SpinNetworkComplete(Scene):
    """Master scene summarizing spin network concepts"""
    
    def construct(self):
        # Title sequence
        main_title = Text(
            "Spin Networks",
            font_size=84,
            color=SPIN_COLOR_1,
            weight=BOLD
        )
        
        subtitle = Text(
            "Discrete Quantum Geometry",
            font_size=42,
            color=WHITE
        ).next_to(main_title, DOWN, buff=0.5)
        
        author = Text(
            "Rovelli & Smolin (1995)",
            font_size=28,
            color=GRAY,
            slant=ITALIC
        ).next_to(subtitle, DOWN, buff=1)
        
        self.play(Write(main_title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP), run_time=1.5)
        self.play(Write(author), run_time=1)
        self.wait(2)
        
        self.play(
            FadeOut(main_title),
            FadeOut(subtitle),
            FadeOut(author)
        )
        
        # Summary
        summary_title = Text("Key Concepts", font_size=56, color=GOLD)
        summary_title.to_edge(UP)
        self.play(Write(summary_title))
        
        concepts = VGroup(
            VGroup(
                Dot(color=NODE_COLOR, radius=0.1),
                Text("Graph Γ = (V, E)", font_size=32)
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Dot(color=EDGE_COLOR, radius=0.1),
                Text("Edges: spin-j ∈ {0, 1/2, 1, 3/2, ...}", font_size=32)
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Dot(color=INTERTWINER_COLOR, radius=0.1),
                Text("Vertices: intertwiners ι", font_size=32)
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Dot(color=QUANTUM_COLOR, radius=0.1),
                Text("Quantized area: A ∝ √(j(j+1))", font_size=32)
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Dot(color=GOLD, radius=0.1),
                Text("Recoupling: 6j-symbols", font_size=32)
            ).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).shift(DOWN * 0.5)
        
        for concept in concepts:
            self.play(FadeIn(concept, shift=RIGHT))
            self.wait(0.5)
        
        self.wait(3)
        self.play(FadeOut(summary_title), FadeOut(concepts))
        
        # Final message
        final_message = Text(
            "Foundation of Loop Quantum Gravity",
            font_size=48,
            color=QUANTUM_COLOR
        )
        
        self.play(Write(final_message))
        self.wait(3)
        self.play(FadeOut(final_message))


if __name__ == "__main__":
    """
    To render these scenes, use:
    
    manim -pql spin_network_visualization.py SpinNetworkIntroduction
    manim -pql spin_network_visualization.py BasicSpinNetwork
    manim -pql spin_network_visualization.py SU2Representations
    manim -pql spin_network_visualization.py IntertwinerVertex
    manim -pql spin_network_visualization.py SixJSymbol
    manim -pql spin_network_visualization.py WilsonLoop
    manim -pql spin_network_visualization.py ThetaGraph
    manim -pql spin_network_visualization.py AreaQuantization
    manim -pql spin_network_visualization.py TetrahedralNetwork
    manim -pql spin_network_visualization.py SpinNetworkComplete
    
    For high quality: use -pqh instead of -pql
    """
    pass
