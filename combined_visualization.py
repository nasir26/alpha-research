"""
Combined Twistor-Spin Network Visualization
=============================================
This module connects twistor theory with spin networks,
showing their relationships and unified framework.

Author: Generated Framework
Date: 2025
"""

from manim import *
import numpy as np

# ==================== COLOR SCHEME ====================
TWISTOR_COLOR = "#00CED1"
SPIN_COLOR = "#FF6B9D"
UNIFIED_COLOR = "#FFD700"  # Gold
CONNECTION_COLOR = "#9B59B6"  # Purple


# ==================== SCENE 1: COMPARISON ====================
class TwistorSpinComparison(Scene):
    """Side-by-side comparison of twistor theory and spin networks"""
    
    def construct(self):
        # Title
        title = Text(
            "Twistor Theory vs Spin Networks",
            font_size=56,
            color=UNIFIED_COLOR
        )
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Create two columns
        divider = Line(UP * 3.5, DOWN * 3.5, color=WHITE, stroke_width=2)
        
        # Column headers
        twistor_header = Text("Twistor Theory", font_size=36, color=TWISTOR_COLOR)
        twistor_header.move_to(LEFT * 3.5 + UP * 2.5)
        
        spin_header = Text("Spin Networks", font_size=36, color=SPIN_COLOR)
        spin_header.move_to(RIGHT * 3.5 + UP * 2.5)
        
        self.play(
            Create(divider),
            Write(twistor_header),
            Write(spin_header)
        )
        
        # Twistor properties
        twistor_props = VGroup(
            Text("• Complex geometry", font_size=24),
            Text("• ℂP³ space", font_size=24),
            Text("• SL(2,ℂ) group", font_size=24),
            Text("• Continuous", font_size=24),
            Text("• Classical+QFT", font_size=24),
            Text("• Null rays", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        twistor_props.next_to(twistor_header, DOWN, buff=0.5).shift(LEFT * 0.5)
        
        # Spin network properties
        spin_props = VGroup(
            Text("• Graph theory", font_size=24),
            Text("• Labeled graphs", font_size=24),
            Text("• SU(2) group", font_size=24),
            Text("• Discrete", font_size=24),
            Text("• Quantum gravity", font_size=24),
            Text("• Area quanta", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        spin_props.next_to(spin_header, DOWN, buff=0.5).shift(LEFT * 0.5)
        
        # Animate properties
        for tw_prop, sp_prop in zip(twistor_props, spin_props):
            self.play(
                FadeIn(tw_prop, shift=RIGHT),
                FadeIn(sp_prop, shift=LEFT),
                run_time=0.7
            )
        
        self.wait(2)
        
        # Common ground
        common_box = Rectangle(
            height=1.5,
            width=6,
            color=UNIFIED_COLOR,
            stroke_width=3
        ).to_edge(DOWN).shift(UP * 0.5)
        
        common_text = VGroup(
            Text("Common Ground:", font_size=28, color=UNIFIED_COLOR, weight=BOLD),
            Text("• Both reformulate spacetime geometry", font_size=22),
            Text("• Both use spinor representations", font_size=22),
            Text("• Both describe quantum structure", font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        common_text.move_to(common_box.get_center())
        
        self.play(Create(common_box))
        self.play(Write(common_text), run_time=2)
        
        self.wait(3)


# ==================== SCENE 2: SPINOR BRIDGE ====================
class SpinorBridge(Scene):
    """Show how spinors connect both frameworks"""
    
    def construct(self):
        # Title
        title = Text("Spinors: The Bridge", font_size=56, color=CONNECTION_COLOR)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # SU(2) and SL(2,C) relationship
        su2_circle = Circle(radius=1.5, color=SPIN_COLOR).shift(LEFT * 3.5)
        su2_label = MathTex(r"\text{SU}(2)", font_size=40, color=SPIN_COLOR)
        su2_label.move_to(su2_circle.get_center())
        
        sl2c_circle = Circle(radius=1.5, color=TWISTOR_COLOR).shift(RIGHT * 3.5)
        sl2c_label = MathTex(r"\text{SL}(2,\mathbb{C})", font_size=40, color=TWISTOR_COLOR)
        sl2c_label.move_to(sl2c_circle.get_center())
        
        self.play(Create(su2_circle), Write(su2_label))
        self.play(Create(sl2c_circle), Write(sl2c_label))
        
        # Connection arrow
        connection = Arrow(
            su2_circle.get_right(),
            sl2c_circle.get_left(),
            color=CONNECTION_COLOR,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        
        connection_label = Text(
            "Complexification",
            font_size=28,
            color=CONNECTION_COLOR
        ).next_to(connection, UP)
        
        self.play(GrowArrow(connection))
        self.play(Write(connection_label))
        
        # Spinor representations
        spinor_box = Rectangle(
            height=2.5,
            width=10,
            color=UNIFIED_COLOR,
            stroke_width=2
        ).shift(DOWN * 2)
        
        spinor_content = VGroup(
            MathTex(
                r"\text{SU}(2): \quad \psi^A, \quad A=0,1",
                font_size=32,
                color=SPIN_COLOR
            ),
            MathTex(
                r"\text{SL}(2,\mathbb{C}): \quad \omega^A, \pi_{A'}, \quad A,A'=0,1",
                font_size=32,
                color=TWISTOR_COLOR
            ),
            MathTex(
                r"\text{Both:} \quad \text{2-component spinors}",
                font_size=32,
                color=UNIFIED_COLOR
            ),
        ).arrange(DOWN, buff=0.4)
        spinor_content.move_to(spinor_box.get_center())
        
        self.play(Create(spinor_box))
        self.play(Write(spinor_content), run_time=2)
        
        self.wait(3)


# ==================== SCENE 3: GEOMETRIC INTERPRETATION ====================
class GeometricInterpretation(ThreeDScene):
    """3D visualization showing geometric aspects"""
    
    def construct(self):
        # Set camera
        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)
        
        # Title
        title = Text("Geometric Interpretation", font_size=48)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        
        # Create axes
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            z_length=6,
        )
        self.play(Create(axes))
        
        # Spin network embedded in space
        vertices = [
            np.array([1, 1, 1]),
            np.array([-1, 1, -1]),
            np.array([1, -1, -1]),
            np.array([-1, -1, 1]),
        ]
        
        dots = VGroup(*[
            Sphere(radius=0.1, resolution=(8, 8)).move_to(v).set_color(SPIN_COLOR)
            for v in vertices
        ])
        
        self.play(FadeIn(dots, scale=0.5))
        
        # Connect with edges
        edges = VGroup()
        for i in range(len(vertices)):
            for j in range(i+1, len(vertices)):
                line = Line3D(
                    vertices[i],
                    vertices[j],
                    color=SPIN_COLOR,
                    stroke_width=3
                )
                edges.add(line)
        
        self.play(Create(edges), run_time=2)
        
        # Add twistor lines
        twistor_lines = VGroup()
        for vertex in vertices:
            # Create line through vertex
            direction = vertex / np.linalg.norm(vertex)
            start = vertex - 1.5 * direction
            end = vertex + 1.5 * direction
            
            line = Line3D(
                start,
                end,
                color=TWISTOR_COLOR,
                stroke_width=2,
                stroke_opacity=0.6
            )
            twistor_lines.add(line)
        
        self.play(Create(twistor_lines), run_time=2)
        
        # Labels
        spin_label = Text("Spin Network", font_size=28, color=SPIN_COLOR)
        twist_label = Text("Twistor Lines", font_size=28, color=TWISTOR_COLOR)
        
        label_group = VGroup(spin_label, twist_label).arrange(DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(label_group)
        label_group.to_corner(DL)
        
        self.play(Write(label_group))
        
        # Rotate
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(6)
        self.stop_ambient_camera_rotation()
        
        self.wait(2)


# ==================== SCENE 4: QUANTUM GEOMETRY ====================
class QuantumGeometry(Scene):
    """Visualization of quantum geometry concepts"""
    
    def construct(self):
        # Title
        title = Text("Quantum Geometry", font_size=56, color=UNIFIED_COLOR)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Classical to quantum transition
        classical_text = Text("Classical Geometry", font_size=36, color=WHITE)
        classical_text.shift(UP * 2 + LEFT * 4)
        
        # Smooth manifold representation
        classical_surface = Circle(radius=1.2, color=WHITE, fill_opacity=0.2)
        classical_surface.next_to(classical_text, DOWN)
        
        self.play(Write(classical_text))
        self.play(Create(classical_surface))
        
        # Arrow
        arrow = Arrow(
            classical_surface.get_right() + RIGHT * 0.5,
            classical_surface.get_right() + RIGHT * 3,
            color=UNIFIED_COLOR,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        
        arrow_label = Text("Quantize", font_size=28, color=UNIFIED_COLOR)
        arrow_label.next_to(arrow, UP)
        
        self.play(GrowArrow(arrow), Write(arrow_label))
        
        # Quantum geometry
        quantum_text = Text("Quantum Geometry", font_size=36, color=UNIFIED_COLOR)
        quantum_text.shift(UP * 2 + RIGHT * 4)
        
        # Discrete network
        quantum_vertices = [
            RIGHT * 4 + UP * 0.8,
            RIGHT * 3.5 + DOWN * 0.5,
            RIGHT * 4.5 + DOWN * 0.5,
            RIGHT * 4 + DOWN * 1.3,
        ]
        
        quantum_dots = VGroup(*[
            Dot(v, color=SPIN_COLOR, radius=0.08)
            for v in quantum_vertices
        ])
        
        quantum_edges = VGroup()
        for i in range(len(quantum_vertices)):
            for j in range(i+1, len(quantum_vertices)):
                line = Line(
                    quantum_vertices[i],
                    quantum_vertices[j],
                    color=SPIN_COLOR,
                    stroke_width=2
                )
                quantum_edges.add(line)
        
        self.play(Write(quantum_text))
        self.play(Create(quantum_edges), FadeIn(quantum_dots))
        
        # Properties boxes
        classical_props = VGroup(
            Text("• Continuous", font_size=20),
            Text("• Differential", font_size=20),
            Text("• Smooth", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        classical_props.next_to(classical_surface, DOWN, buff=0.5)
        
        quantum_props = VGroup(
            Text("• Discrete", font_size=20, color=SPIN_COLOR),
            Text("• Combinatorial", font_size=20, color=SPIN_COLOR),
            Text("• Quantized", font_size=20, color=SPIN_COLOR),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        quantum_props.next_to(quantum_dots, DOWN, buff=0.8)
        
        self.play(Write(classical_props))
        self.play(Write(quantum_props))
        
        # Key formula
        formula = MathTex(
            r"[\hat{A}_S, \hat{V}_R] = i\hbar \, \text{(non-zero)}",
            font_size=36,
            color=UNIFIED_COLOR
        ).to_edge(DOWN)
        
        formula_label = Text(
            "Non-commutative geometry",
            font_size=24,
            color=UNIFIED_COLOR
        ).next_to(formula, UP)
        
        self.play(Write(formula_label))
        self.play(Write(formula))
        
        self.wait(3)


# ==================== SCENE 5: UNIFIED FRAMEWORK ====================
class UnifiedFramework(Scene):
    """Show the unified mathematical framework"""
    
    def construct(self):
        # Title
        title = Text(
            "Unified Mathematical Framework",
            font_size=52,
            color=UNIFIED_COLOR
        )
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Central concept
        center_box = Rectangle(
            height=1.5,
            width=4,
            color=UNIFIED_COLOR,
            stroke_width=3
        )
        center_text = Text(
            "Spinor Networks",
            font_size=36,
            color=UNIFIED_COLOR
        ).move_to(center_box.get_center())
        
        self.play(Create(center_box), Write(center_text))
        
        # Twistor branch
        twistor_box = Rectangle(
            height=1.2,
            width=3.5,
            color=TWISTOR_COLOR,
            stroke_width=2
        ).shift(LEFT * 4 + UP * 2)
        
        twistor_text = VGroup(
            Text("Twistor", font_size=28, color=TWISTOR_COLOR, weight=BOLD),
            Text("Diagrams", font_size=24, color=TWISTOR_COLOR),
        ).arrange(DOWN, buff=0.1)
        twistor_text.move_to(twistor_box.get_center())
        
        # Spin network branch
        spin_box = Rectangle(
            height=1.2,
            width=3.5,
            color=SPIN_COLOR,
            stroke_width=2
        ).shift(RIGHT * 4 + UP * 2)
        
        spin_text = VGroup(
            Text("Spin", font_size=28, color=SPIN_COLOR, weight=BOLD),
            Text("Networks", font_size=24, color=SPIN_COLOR),
        ).arrange(DOWN, buff=0.1)
        spin_text.move_to(spin_box.get_center())
        
        # Connect to center
        line_to_twistor = Line(
            center_box.get_top(),
            twistor_box.get_bottom(),
            color=CONNECTION_COLOR,
            stroke_width=3
        )
        
        line_to_spin = Line(
            center_box.get_top(),
            spin_box.get_bottom(),
            color=CONNECTION_COLOR,
            stroke_width=3
        )
        
        self.play(
            Create(line_to_twistor),
            Create(line_to_spin)
        )
        self.play(
            Create(twistor_box),
            Write(twistor_text),
            Create(spin_box),
            Write(spin_text)
        )
        
        # Properties
        properties = VGroup(
            VGroup(
                Dot(color=TWISTOR_COLOR, radius=0.08),
                Text("Complex geometry", font_size=24)
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Dot(color=SPIN_COLOR, radius=0.08),
                Text("Quantum states", font_size=24)
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Dot(color=UNIFIED_COLOR, radius=0.08),
                Text("Unified by spinors", font_size=24)
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        properties.shift(DOWN * 2)
        
        for prop in properties:
            self.play(FadeIn(prop, shift=UP))
            self.wait(0.5)
        
        self.wait(3)


# ==================== SCENE 6: FINAL SYNTHESIS ====================
class FinalSynthesis(Scene):
    """Final synthesis scene bringing everything together"""
    
    def construct(self):
        # Title
        title = Text(
            "Twistor Theory & Spin Networks",
            font_size=64,
            color=UNIFIED_COLOR,
            weight=BOLD
        )
        
        subtitle = Text(
            "Two Paths to Quantum Spacetime",
            font_size=36,
            color=WHITE
        ).next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP), run_time=1.5)
        self.wait(2)
        
        self.play(
            title.animate.scale(0.6).to_edge(UP),
            FadeOut(subtitle)
        )
        
        # Key results
        results_title = Text("Key Results", font_size=40, color=UNIFIED_COLOR)
        results_title.shift(UP * 2)
        self.play(Write(results_title))
        
        results = VGroup(
            Text("✓ Spacetime emerges from quantum networks", font_size=28),
            Text("✓ Area and volume are quantized", font_size=28),
            Text("✓ Complex geometry encodes physical fields", font_size=28),
            Text("✓ Spinors unify both frameworks", font_size=28),
            Text("✓ Discrete structures at Planck scale", font_size=28),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        results.shift(DOWN * 0.5)
        
        for result in results:
            self.play(FadeIn(result, shift=RIGHT))
            self.wait(0.6)
        
        self.wait(2)
        
        # Final equation
        final_eq = MathTex(
            r"\text{Quantum Geometry} = \text{Spinor Networks}",
            font_size=44,
            color=UNIFIED_COLOR
        ).to_edge(DOWN)
        
        box = SurroundingRectangle(final_eq, color=UNIFIED_COLOR, buff=0.3)
        
        self.play(Write(final_eq))
        self.play(Create(box))
        
        self.wait(3)
        
        # Fade to end
        self.play(
            FadeOut(results_title),
            FadeOut(results),
            FadeOut(final_eq),
            FadeOut(box),
            title.animate.move_to(ORIGIN).scale(1.5)
        )
        self.wait(2)


if __name__ == "__main__":
    """
    To render these scenes, use:
    
    manim -pql combined_visualization.py TwistorSpinComparison
    manim -pql combined_visualization.py SpinorBridge
    manim -pql combined_visualization.py GeometricInterpretation
    manim -pql combined_visualization.py QuantumGeometry
    manim -pql combined_visualization.py UnifiedFramework
    manim -pql combined_visualization.py FinalSynthesis
    
    For high quality: use -pqh instead of -pql
    """
    pass
