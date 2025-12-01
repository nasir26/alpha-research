"""
Twistor Theory Visualization using Manim
==========================================
This module provides comprehensive visualizations of twistor theory concepts
using the Manim mathematical animation library.

Author: Generated Framework
Date: 2025
"""

from manim import *
import numpy as np

# ==================== COLOR SCHEME ====================
TWISTOR_COLOR = "#00CED1"  # Dark turquoise
SPACETIME_COLOR = "#FF6B6B"  # Coral red
SPINOR_COLOR = "#4ECDC4"  # Turquoise
CORRESPONDENCE_COLOR = "#FFE66D"  # Yellow
COMPLEX_COLOR = "#A8E6CF"  # Mint green


# ==================== SCENE 1: INTRODUCTION ====================
class TwistorIntroduction(Scene):
    """Introduction to twistor theory concepts"""
    
    def construct(self):
        # Title
        title = Text("Twistor Theory", font_size=72, color=TWISTOR_COLOR)
        subtitle = Text(
            "A Geometric Approach to Spacetime",
            font_size=36,
            color=WHITE
        ).next_to(title, DOWN)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Key concepts
        concepts = VGroup(
            Text("• Complex Projective Space CP³", font_size=32),
            Text("• Spacetime ↔ Twistor Correspondence", font_size=32),
            Text("• Spinor Formulation", font_size=32),
            Text("• Penrose Transform", font_size=32),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        for concept in concepts:
            self.play(FadeIn(concept, shift=RIGHT))
            self.wait(0.5)
        
        self.wait(2)
        self.play(FadeOut(concepts))


# ==================== SCENE 2: COMPLEX PROJECTIVE SPACE ====================
class ComplexProjectiveSpace(ThreeDScene):
    """Visualization of CP³ as twistor space"""
    
    def construct(self):
        # Set up 3D scene
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Title
        title = Text("Complex Projective Space CP³", font_size=48)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        
        # Create coordinate axes
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            z_length=6,
        )
        
        # Labels
        x_label = MathTex(r"\omega^0", color=RED).next_to(axes.x_axis, RIGHT)
        y_label = MathTex(r"\omega^1", color=GREEN).next_to(axes.y_axis, UP)
        z_label = MathTex(r"\pi_{0'}", color=BLUE).next_to(axes.z_axis, OUT)
        
        self.play(Create(axes))
        self.add_fixed_in_frame_mobjects(x_label, y_label, z_label)
        self.play(Write(x_label), Write(y_label), Write(z_label))
        
        # Create projective lines (representing spacetime points)
        lines = VGroup()
        for i in range(8):
            angle = i * TAU / 8
            start = np.array([
                2 * np.cos(angle),
                2 * np.sin(angle),
                -2
            ])
            end = np.array([
                2 * np.cos(angle),
                2 * np.sin(angle),
                2
            ])
            line = Line3D(start, end, color=TWISTOR_COLOR, stroke_width=2)
            lines.add(line)
        
        self.play(Create(lines), run_time=2)
        
        # Rotate camera
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        
        # Formula
        formula = MathTex(
            r"Z^\alpha = \begin{pmatrix} \omega^A \\ \pi_{A'} \end{pmatrix}",
            font_size=40,
            color=TWISTOR_COLOR
        )
        self.add_fixed_in_frame_mobjects(formula)
        formula.to_edge(DOWN)
        self.play(Write(formula))
        
        self.wait(3)


# ==================== SCENE 3: INCIDENCE RELATION ====================
class IncidenceRelation(Scene):
    """Visualization of the incidence relation between spacetime and twistor space"""
    
    def construct(self):
        # Title
        title = Text("Incidence Relation", font_size=56, color=CORRESPONDENCE_COLOR)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Create two spaces side by side
        spacetime_label = Text("Spacetime", font_size=36, color=SPACETIME_COLOR)
        spacetime_label.move_to(LEFT * 4 + UP * 2)
        
        twistor_label = Text("Twistor Space", font_size=36, color=TWISTOR_COLOR)
        twistor_label.move_to(RIGHT * 4 + UP * 2)
        
        self.play(Write(spacetime_label), Write(twistor_label))
        
        # Spacetime point
        spacetime_circle = Circle(radius=2, color=SPACETIME_COLOR).shift(LEFT * 4)
        spacetime_point = Dot(spacetime_circle.get_center(), color=YELLOW, radius=0.1)
        spacetime_text = MathTex(r"x^{AA'}", color=YELLOW).next_to(spacetime_point, DOWN)
        
        self.play(Create(spacetime_circle))
        self.play(FadeIn(spacetime_point, scale=0.5))
        self.play(Write(spacetime_text))
        
        # Twistor space representation
        twistor_circle = Circle(radius=2, color=TWISTOR_COLOR).shift(RIGHT * 4)
        
        # Create multiple lines representing CP¹
        twistor_lines = VGroup()
        for i in range(6):
            angle = i * TAU / 6
            start = twistor_circle.get_center() + 0.5 * np.array([np.cos(angle), np.sin(angle), 0])
            end = twistor_circle.get_center() + 1.5 * np.array([np.cos(angle), np.sin(angle), 0])
            line = Line(start, end, color=TWISTOR_COLOR, stroke_width=3)
            twistor_lines.add(line)
        
        self.play(Create(twistor_circle))
        self.play(Create(twistor_lines), run_time=2)
        
        twistor_text = MathTex(r"\mathbb{CP}^1 \subset \mathbb{CP}^3", 
                               color=TWISTOR_COLOR, font_size=36)
        twistor_text.next_to(twistor_circle, DOWN)
        self.play(Write(twistor_text))
        
        # Show correspondence with arrow
        arrow = Arrow(
            spacetime_point.get_right() + RIGHT * 0.5,
            twistor_circle.get_left() + LEFT * 0.5,
            color=CORRESPONDENCE_COLOR,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(GrowArrow(arrow))
        
        # Display incidence relation formula
        formula = MathTex(
            r"\omega^A = ix^{AA'}\pi_{A'}",
            font_size=48,
            color=CORRESPONDENCE_COLOR
        ).to_edge(DOWN)
        
        box = SurroundingRectangle(formula, color=YELLOW, buff=0.2)
        
        self.play(Write(formula))
        self.play(Create(box))
        
        self.wait(3)


# ==================== SCENE 4: SPINOR DECOMPOSITION ====================
class SpinorDecomposition(Scene):
    """Visualization of spinor decomposition of spacetime vectors"""
    
    def construct(self):
        # Title
        title = Text("Spinor Decomposition", font_size=56, color=SPINOR_COLOR)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Spacetime vector
        vector_eq = MathTex(
            r"x^\mu = (t, x, y, z)",
            font_size=40
        ).shift(UP * 2)
        self.play(Write(vector_eq))
        
        # Arrow down
        arrow1 = Arrow(vector_eq.get_bottom(), vector_eq.get_bottom() + DOWN, 
                       color=YELLOW)
        self.play(GrowArrow(arrow1))
        
        # Spinor matrix form
        spinor_matrix = MathTex(
            r"x^{AA'} = \begin{pmatrix} t+z & x-iy \\ x+iy & t-z \end{pmatrix}",
            font_size=40,
            color=SPINOR_COLOR
        ).next_to(arrow1, DOWN)
        
        self.play(Write(spinor_matrix))
        self.wait(1)
        
        # Show decomposition
        arrow2 = Arrow(spinor_matrix.get_bottom(), spinor_matrix.get_bottom() + DOWN,
                       color=YELLOW)
        self.play(GrowArrow(arrow2))
        
        # Left and right handed spinors
        decomposition = VGroup(
            MathTex(r"\omega^0", color=RED, font_size=48),
            MathTex(r"\omega^1", color=RED, font_size=48),
            MathTex(r"\pi_{0'}", color=BLUE, font_size=48),
            MathTex(r"\pi_{1'}", color=BLUE, font_size=48),
        ).arrange(RIGHT, buff=0.8).next_to(arrow2, DOWN)
        
        # Labels
        left_label = Text("Left-handed", font_size=24, color=RED).next_to(
            VGroup(decomposition[0], decomposition[1]), UP
        )
        right_label = Text("Right-handed", font_size=24, color=BLUE).next_to(
            VGroup(decomposition[2], decomposition[3]), UP
        )
        
        self.play(FadeIn(decomposition, shift=UP))
        self.play(Write(left_label), Write(right_label))
        
        # Group representation
        group_text = MathTex(
            r"\text{SL}(2,\mathbb{C}) = \text{Spin}(3,1)",
            font_size=36,
            color=GREEN
        ).to_edge(DOWN)
        
        box = SurroundingRectangle(group_text, color=GREEN, buff=0.2)
        
        self.play(Write(group_text))
        self.play(Create(box))
        
        self.wait(3)


# ==================== SCENE 5: PENROSE TRANSFORM ====================
class PenroseTransform(Scene):
    """Visualization of the Penrose transform"""
    
    def construct(self):
        # Title
        title = Text("The Penrose Transform", font_size=56, color=GOLD)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Two domains
        left_box = Rectangle(height=4, width=4, color=TWISTOR_COLOR).shift(LEFT * 3.5)
        left_title = Text("Twistor Space", font_size=28, color=TWISTOR_COLOR)
        left_title.next_to(left_box, UP)
        
        right_box = Rectangle(height=4, width=4, color=SPACETIME_COLOR).shift(RIGHT * 3.5)
        right_title = Text("Spacetime", font_size=28, color=SPACETIME_COLOR)
        right_title.next_to(right_box, UP)
        
        self.play(Create(left_box), Create(right_box))
        self.play(Write(left_title), Write(right_title))
        
        # Cohomology group
        cohomology = MathTex(
            r"H^1(\mathbb{PT}, \mathcal{O}(-n-2))",
            font_size=32,
            color=TWISTOR_COLOR
        ).move_to(left_box.get_center())
        
        # Physical field
        field = MathTex(
            r"\phi_{\alpha_1...\alpha_n}(x)",
            font_size=32,
            color=SPACETIME_COLOR
        ).move_to(right_box.get_center())
        
        # Helicity label
        helicity_text = Text(
            "helicity n/2",
            font_size=24,
            color=YELLOW
        ).next_to(field, DOWN)
        
        self.play(Write(cohomology))
        self.play(Write(field), Write(helicity_text))
        
        # Bidirectional arrow
        arrow = DoubleArrow(
            left_box.get_right(),
            right_box.get_left(),
            color=CORRESPONDENCE_COLOR,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.1
        )
        
        transform_label = Text(
            "Penrose Transform",
            font_size=24,
            color=CORRESPONDENCE_COLOR
        ).next_to(arrow, UP)
        
        self.play(GrowArrow(arrow))
        self.play(Write(transform_label))
        
        # Examples
        examples = VGroup(
            MathTex(r"n=0: \text{ scalar field}", font_size=28),
            MathTex(r"n=2: \text{ Maxwell field}", font_size=28),
            MathTex(r"n=4: \text{ graviton}", font_size=28),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(DOWN)
        
        for example in examples:
            self.play(FadeIn(example, shift=UP))
            self.wait(0.5)
        
        self.wait(3)


# ==================== SCENE 6: ALPHA AND BETA PLANES ====================
class AlphaBetaPlanes(ThreeDScene):
    """Visualization of α-planes and β-planes in twistor space"""
    
    def construct(self):
        # Set camera
        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)
        
        # Title
        title = Text("α-planes and β-planes", font_size=48)
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
        
        # α-plane (represents a point in spacetime)
        alpha_plane = Surface(
            lambda u, v: axes.c2p(u, v, 0.5 * u + 0.3 * v),
            u_range=[-2, 2],
            v_range=[-2, 2],
            fill_color=BLUE,
            fill_opacity=0.5,
            stroke_color=BLUE
        )
        
        alpha_label = MathTex(r"\alpha\text{-plane}", color=BLUE, font_size=36)
        self.add_fixed_in_frame_mobjects(alpha_label)
        alpha_label.to_corner(UL).shift(DOWN)
        
        self.play(Create(alpha_plane), Write(alpha_label))
        self.wait(1)
        
        # β-plane (represents a null ray)
        beta_plane = Surface(
            lambda u, v: axes.c2p(0.3 * u + v, u, 0.7 * u + 0.2 * v),
            u_range=[-2, 2],
            v_range=[-2, 2],
            fill_color=RED,
            fill_opacity=0.4,
            stroke_color=RED
        )
        
        beta_label = MathTex(r"\beta\text{-plane}", color=RED, font_size=36)
        self.add_fixed_in_frame_mobjects(beta_label)
        beta_label.to_corner(UR).shift(DOWN)
        
        self.play(Create(beta_plane), Write(beta_label))
        
        # Correspondence text
        corr_text1 = MathTex(
            r"\alpha\text{-plane} \leftrightarrow \text{point in spacetime}",
            font_size=28,
            color=BLUE
        )
        corr_text2 = MathTex(
            r"\beta\text{-plane} \leftrightarrow \text{null ray}",
            font_size=28,
            color=RED
        )
        
        corr_group = VGroup(corr_text1, corr_text2).arrange(DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(corr_group)
        corr_group.to_edge(DOWN)
        
        self.play(Write(corr_text1))
        self.wait(1)
        self.play(Write(corr_text2))
        
        # Rotate camera
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(6)
        self.stop_ambient_camera_rotation()
        
        self.wait(2)


# ==================== SCENE 7: NULL TWISTORS ====================
class NullTwistors(Scene):
    """Visualization of null twistors and light cones"""
    
    def construct(self):
        # Title
        title = Text("Null Twistors and Light Cones", font_size=52, color=YELLOW)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        
        # Null condition
        null_condition = MathTex(
            r"Z^\alpha Z_\alpha = 0",
            font_size=48,
            color=YELLOW
        ).shift(UP * 2)
        
        self.play(Write(null_condition))
        
        # Expanded form
        expanded = MathTex(
            r"\omega^A \pi_A + \pi_{A'}\omega^{A'} = 0",
            font_size=40
        ).next_to(null_condition, DOWN)
        
        self.play(Write(expanded))
        self.wait(1)
        
        # Light cone visualization
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
        )
        axes.shift(DOWN * 1.5)
        
        # Create light cone
        light_cone_future = VGroup()
        light_cone_past = VGroup()
        
        for angle in np.linspace(0, TAU, 32):
            radius = 2
            # Future cone
            line_future = Line(
                axes.c2p(0, 0),
                axes.c2p(radius * np.cos(angle), radius * np.sin(angle)),
                color=YELLOW,
                stroke_width=2
            )
            light_cone_future.add(line_future)
            
            # Past cone  
            line_past = Line(
                axes.c2p(0, 0),
                axes.c2p(-radius * np.cos(angle), -radius * np.sin(angle)),
                color=ORANGE,
                stroke_width=2
            )
            light_cone_past.add(line_past)
        
        labels = VGroup(
            MathTex(r"t", font_size=36).next_to(axes.y_axis, UP),
            MathTex(r"x", font_size=36).next_to(axes.x_axis, RIGHT),
        )
        
        self.play(Create(axes), Write(labels))
        self.play(Create(light_cone_future), Create(light_cone_past), run_time=2)
        
        # Label regions
        future_label = Text("Future", font_size=24, color=YELLOW).move_to(
            axes.c2p(0, 1.5)
        )
        past_label = Text("Past", font_size=24, color=ORANGE).move_to(
            axes.c2p(0, -1.5)
        )
        
        self.play(Write(future_label), Write(past_label))
        
        self.wait(3)


# ==================== MAIN COMPILATION SCENE ====================
class TwistorTheoryComplete(Scene):
    """Master scene that combines all concepts"""
    
    def construct(self):
        # Title sequence
        main_title = Text(
            "Twistor Theory",
            font_size=84,
            color=TWISTOR_COLOR,
            weight=BOLD
        )
        
        subtitle = Text(
            "From Spacetime to Complex Geometry",
            font_size=42,
            color=WHITE
        ).next_to(main_title, DOWN, buff=0.5)
        
        author = Text(
            "Penrose (1967)",
            font_size=28,
            color=GRAY,
            slant=ITALIC
        ).next_to(subtitle, DOWN, buff=1)
        
        self.play(
            Write(main_title),
            run_time=2
        )
        self.play(
            FadeIn(subtitle, shift=UP),
            run_time=1.5
        )
        self.play(
            Write(author),
            run_time=1
        )
        self.wait(2)
        
        self.play(
            FadeOut(main_title),
            FadeOut(subtitle),
            FadeOut(author)
        )
        
        # Summary slide
        summary_title = Text("Key Concepts", font_size=56, color=GOLD)
        summary_title.to_edge(UP)
        self.play(Write(summary_title))
        
        concepts = VGroup(
            VGroup(
                Dot(color=TWISTOR_COLOR, radius=0.1),
                Text("Twistor space: ℂP³", font_size=32)
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Dot(color=SPACETIME_COLOR, radius=0.1),
                Text("Incidence relation: ω = ix·π", font_size=32)
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Dot(color=SPINOR_COLOR, radius=0.1),
                Text("Spinor formulation: SL(2,ℂ)", font_size=32)
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Dot(color=CORRESPONDENCE_COLOR, radius=0.1),
                Text("Penrose transform: cohomology ↔ fields", font_size=32)
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Dot(color=YELLOW, radius=0.1),
                Text("α-planes and β-planes", font_size=32)
            ).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).shift(DOWN * 0.5)
        
        for concept in concepts:
            self.play(FadeIn(concept, shift=RIGHT))
            self.wait(0.5)
        
        self.wait(3)
        self.play(FadeOut(summary_title), FadeOut(concepts))


if __name__ == "__main__":
    """
    To render these scenes, use:
    
    manim -pql twistor_visualization.py TwistorIntroduction
    manim -pql twistor_visualization.py ComplexProjectiveSpace
    manim -pql twistor_visualization.py IncidenceRelation
    manim -pql twistor_visualization.py SpinorDecomposition
    manim -pql twistor_visualization.py PenroseTransform
    manim -pql twistor_visualization.py AlphaBetaPlanes
    manim -pql twistor_visualization.py NullTwistors
    manim -pql twistor_visualization.py TwistorTheoryComplete
    
    For high quality: use -pqh instead of -pql
    """
    pass
