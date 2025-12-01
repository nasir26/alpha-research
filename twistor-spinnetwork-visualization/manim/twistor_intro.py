"""
Twistor Theory Introduction - Manim Animations
===============================================
Comprehensive visualization of Twistor Theory fundamentals.

Run with: manim -pql twistor_intro.py TwistorSpaceScene
"""

from manim import *
import numpy as np

# Custom color scheme
TWISTOR_BLUE = "#2962FF"
TWISTOR_GOLD = "#FFC107"
SPIN_RED = "#F44336"
SPIN_GREEN = "#4CAF50"
SPIN_PURPLE = "#9C27B0"
SPACETIME_DARK = "#212121"
NULL_CONE = "#FF9800"
LIGHT_RAY = "#FFEB3B"
NODE_COLOR = "#009688"
EDGE_COLOR = "#673AB7"


class TwistorSpaceScene(ThreeDScene):
    """
    Introduction to Twistor Space.
    Visualizes the structure of CP³ and its relationship to C⁴.
    """

    def construct(self):
        # Title
        title = Text("Twistor Space", font_size=72, color=TWISTOR_BLUE)
        subtitle = MathTex(r"\mathbb{T} = \mathbb{C}^4", font_size=48)
        subtitle.next_to(title, DOWN)

        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP))
        self.wait()
        self.play(FadeOut(title), FadeOut(subtitle))

        # Twistor components
        twistor_def = MathTex(
            r"Z^\alpha = (\omega^A, \pi_{A'})",
            font_size=56
        )
        twistor_def.to_edge(UP)

        omega_label = MathTex(r"\omega^A", color=SPIN_RED, font_size=40)
        pi_label = MathTex(r"\pi_{A'}", color=SPIN_GREEN, font_size=40)
        omega_desc = Text("Spinor", font_size=24, color=SPIN_RED)
        pi_desc = Text("Dual Spinor", font_size=24, color=SPIN_GREEN)

        omega_group = VGroup(omega_label, omega_desc).arrange(DOWN, buff=0.2)
        pi_group = VGroup(pi_label, pi_desc).arrange(DOWN, buff=0.2)

        components = VGroup(omega_group, pi_group).arrange(RIGHT, buff=2)
        components.next_to(twistor_def, DOWN, buff=1)

        self.play(Write(twistor_def))
        self.wait(0.5)
        self.play(
            FadeIn(omega_group, shift=RIGHT),
            FadeIn(pi_group, shift=LEFT)
        )
        self.wait()

        # Show C⁴ structure
        c4_structure = VGroup(
            MathTex(r"\mathbb{C}^4 = \{", font_size=36),
            MathTex(r"(\omega^0, \omega^1,", color=SPIN_RED, font_size=36),
            MathTex(r"\pi_{0'}, \pi_{1'})", color=SPIN_GREEN, font_size=36),
            MathTex(r"\}", font_size=36)
        ).arrange(RIGHT, buff=0.1)
        c4_structure.next_to(components, DOWN, buff=1)

        self.play(Write(c4_structure))
        self.wait()

        # Transition to projective space
        self.play(
            FadeOut(twistor_def),
            FadeOut(components),
            c4_structure.animate.to_edge(UP)
        )

        proj_arrow = Arrow(LEFT * 2, RIGHT * 2, color=TWISTOR_GOLD)
        proj_label = Text("Projectivize", font_size=32, color=TWISTOR_GOLD)
        proj_label.next_to(proj_arrow, UP)

        cp3 = MathTex(r"\mathbb{PT} = \mathbb{CP}^3", font_size=56, color=TWISTOR_BLUE)
        cp3.next_to(proj_arrow, DOWN, buff=1)

        dim_label = MathTex(
            r"\dim_\mathbb{C} = 3",
            font_size=36
        )
        dim_label.next_to(cp3, DOWN)

        self.play(GrowArrow(proj_arrow), Write(proj_label))
        self.play(Write(cp3), Write(dim_label))
        self.wait()

        # Clear and show 3D representation
        self.play(FadeOut(Group(*self.mobjects)))

        # 3D visualization of projective space concept
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # Create a sphere to represent CP³ (schematically)
        sphere = Surface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u) * np.sin(v),
                1.5 * np.cos(v)
            ]),
            u_range=[0, TAU],
            v_range=[0, PI],
            resolution=(32, 16),
            fill_opacity=0.3,
            stroke_width=0.5,
            stroke_color=TWISTOR_BLUE,
            fill_color=TWISTOR_BLUE
        )

        title_3d = Text("Projective Twistor Space CP³", font_size=36, color=TWISTOR_BLUE)
        title_3d.to_corner(UL)
        self.add_fixed_in_frame_mobjects(title_3d)

        self.play(Create(sphere), Write(title_3d))
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(4)
        self.stop_ambient_camera_rotation()


class IncidenceRelationScene(Scene):
    """
    Visualizes the incidence relation: ω^A = i x^{AA'} π_{A'}
    """

    def construct(self):
        title = Text("The Incidence Relation", font_size=56, color=TWISTOR_BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        # The fundamental equation
        incidence = MathTex(
            r"\omega^A = i \, x^{AA'} \pi_{A'}",
            font_size=64
        )
        incidence.set_color_by_tex(r"\omega", SPIN_RED)
        incidence.set_color_by_tex(r"\pi", SPIN_GREEN)
        incidence.set_color_by_tex("x", TWISTOR_GOLD)

        box = SurroundingRectangle(incidence, color=TWISTOR_BLUE, buff=0.3)

        self.play(Write(incidence))
        self.play(Create(box))
        self.wait()

        # Explanation
        explanation = VGroup(
            MathTex(r"x^{AA'}", color=TWISTOR_GOLD),
            Text("= spacetime point", font_size=28)
        ).arrange(RIGHT, buff=0.3)

        explanation2 = VGroup(
            MathTex(r"Z^\alpha = (\omega^A, \pi_{A'})", font_size=36),
            Text("= twistor incident with x", font_size=28)
        ).arrange(RIGHT, buff=0.3)

        explanations = VGroup(explanation, explanation2).arrange(DOWN, buff=0.5)
        explanations.next_to(box, DOWN, buff=1)

        self.play(FadeIn(explanations, shift=UP))
        self.wait()

        # Show the correspondence visually
        self.play(
            FadeOut(incidence),
            FadeOut(box),
            FadeOut(explanations),
            title.animate.scale(0.7).to_corner(UL)
        )

        # Create visual representation
        # Minkowski space on left
        mink_box = Square(side_length=3, color=SPACETIME_DARK, fill_opacity=0.2)
        mink_box.shift(LEFT * 3.5)
        mink_label = Text("Minkowski Space", font_size=24)
        mink_label.next_to(mink_box, UP)

        # Point in Minkowski
        point = Dot(LEFT * 3.5, radius=0.15, color=TWISTOR_GOLD)
        point_label = MathTex("x", color=TWISTOR_GOLD, font_size=36)
        point_label.next_to(point, UR, buff=0.1)

        self.play(
            Create(mink_box),
            Write(mink_label),
            Create(point),
            Write(point_label)
        )

        # Twistor space on right
        twist_circle = Circle(radius=1.5, color=TWISTOR_BLUE, fill_opacity=0.2)
        twist_circle.shift(RIGHT * 3.5)
        twist_label = Text("Twistor Space", font_size=24, color=TWISTOR_BLUE)
        twist_label.next_to(twist_circle, UP)

        self.play(Create(twist_circle), Write(twist_label))

        # Line in twistor space corresponding to point
        line_in_twist = Line(
            RIGHT * 3.5 + UP * 1.2 + LEFT * 1,
            RIGHT * 3.5 + DOWN * 1.2 + RIGHT * 1,
            color=TWISTOR_GOLD,
            stroke_width=4
        )
        line_label = MathTex(r"L_x", color=TWISTOR_GOLD, font_size=36)
        line_label.next_to(line_in_twist, RIGHT)

        # Arrow showing correspondence
        arrow = CurvedArrow(
            LEFT * 2.5, RIGHT * 1.8,
            angle=-TAU / 6,
            color=SPIN_PURPLE
        )
        arrow_label = Text("corresponds to", font_size=20, color=SPIN_PURPLE)
        arrow_label.next_to(arrow, UP, buff=0.1)

        self.play(
            GrowArrow(arrow),
            Write(arrow_label)
        )
        self.play(Create(line_in_twist), Write(line_label))
        self.wait()

        # Summary text
        summary = VGroup(
            Text("Point in spacetime", font_size=24, color=TWISTOR_GOLD),
            MathTex(r"\longleftrightarrow", font_size=36),
            Text("Line in twistor space", font_size=24, color=TWISTOR_BLUE)
        ).arrange(RIGHT, buff=0.3)
        summary.to_edge(DOWN)

        self.play(FadeIn(summary))
        self.wait(2)


class NullTwistorScene(Scene):
    """
    Visualization of null twistors and light rays.
    """

    def construct(self):
        title = Text("Null Twistors", font_size=56, color=NULL_CONE)
        title.to_edge(UP)
        self.play(Write(title))

        # Definition
        null_def = MathTex(
            r"Z^\alpha \bar{Z}_\alpha = ",
            r"\omega^A \bar{\omega}_A + \bar{\pi}_{A'} \pi^{A'} = 0",
            font_size=40
        )
        null_def.next_to(title, DOWN, buff=0.5)
        self.play(Write(null_def))
        self.wait()

        # Create regions visualization
        self.play(
            null_def.animate.scale(0.7).to_corner(UL).shift(DOWN * 0.5)
        )

        # Twistor space regions
        # PT+ region
        pt_plus = Rectangle(
            width=3, height=4,
            fill_color=SPIN_GREEN,
            fill_opacity=0.3,
            stroke_color=SPIN_GREEN
        )
        pt_plus.shift(LEFT * 2.5)
        pt_plus_label = MathTex(r"\mathbb{PT}^+", color=SPIN_GREEN, font_size=48)
        pt_plus_label.move_to(pt_plus)
        pt_plus_desc = Text("Z·Z̄ > 0", font_size=20, color=SPIN_GREEN)
        pt_plus_desc.next_to(pt_plus_label, DOWN)

        # Null region
        null_line = Line(UP * 2, DOWN * 2, color=NULL_CONE, stroke_width=6)
        null_label = MathTex(r"\mathbf{N}", color=NULL_CONE, font_size=48)
        null_label.next_to(null_line, UP)
        null_desc = Text("Z·Z̄ = 0", font_size=20, color=NULL_CONE)
        null_desc.next_to(null_label, DOWN, buff=0.1)

        # PT- region
        pt_minus = Rectangle(
            width=3, height=4,
            fill_color=SPIN_RED,
            fill_opacity=0.3,
            stroke_color=SPIN_RED
        )
        pt_minus.shift(RIGHT * 2.5)
        pt_minus_label = MathTex(r"\mathbb{PT}^-", color=SPIN_RED, font_size=48)
        pt_minus_label.move_to(pt_minus)
        pt_minus_desc = Text("Z·Z̄ < 0", font_size=20, color=SPIN_RED)
        pt_minus_desc.next_to(pt_minus_label, DOWN)

        self.play(
            FadeIn(pt_plus),
            Write(pt_plus_label),
            Write(pt_plus_desc)
        )
        self.play(
            Create(null_line),
            Write(null_label),
            Write(null_desc)
        )
        self.play(
            FadeIn(pt_minus),
            Write(pt_minus_label),
            Write(pt_minus_desc)
        )
        self.wait()

        # Add dots on null line representing light rays
        dots = VGroup(*[
            Dot(UP * y, color=LIGHT_RAY, radius=0.1)
            for y in np.linspace(-1.5, 1.5, 7)
        ])

        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.1)
        )

        # Helicity interpretation
        helicity_box = VGroup(
            Text("Physical Interpretation:", font_size=24, weight=BOLD),
            VGroup(
                MathTex(r"\mathbb{PT}^+", color=SPIN_GREEN, font_size=28),
                Text(": positive helicity states", font_size=20)
            ).arrange(RIGHT),
            VGroup(
                MathTex(r"\mathbf{N}", color=NULL_CONE, font_size=28),
                Text(": light rays in spacetime", font_size=20)
            ).arrange(RIGHT),
            VGroup(
                MathTex(r"\mathbb{PT}^-", color=SPIN_RED, font_size=28),
                Text(": negative helicity states", font_size=20)
            ).arrange(RIGHT)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        helicity_box.to_edge(DOWN)

        box_rect = SurroundingRectangle(helicity_box, color=WHITE, buff=0.2)

        self.play(
            FadeIn(helicity_box),
            Create(box_rect)
        )
        self.wait(2)


class PenroseCorrespondence(Scene):
    """
    Full visualization of the Penrose correspondence.
    """

    def construct(self):
        title = Text("The Penrose Correspondence", font_size=48, color=SPIN_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))

        # Two side-by-side frames
        mink_frame = Rectangle(width=5, height=4, color=SPACETIME_DARK)
        mink_frame.shift(LEFT * 3.5)
        mink_title = Text("Minkowski Space M", font_size=24)
        mink_title.next_to(mink_frame, UP)

        twist_frame = Rectangle(width=5, height=4, color=TWISTOR_BLUE)
        twist_frame.shift(RIGHT * 3.5)
        twist_title = Text("Twistor Space PT", font_size=24, color=TWISTOR_BLUE)
        twist_title.next_to(twist_frame, UP)

        self.play(
            Create(mink_frame),
            Create(twist_frame),
            Write(mink_title),
            Write(twist_title)
        )

        # Point to Line
        point = Dot(LEFT * 3.5, radius=0.15, color=TWISTOR_GOLD)
        point_label = MathTex("p", color=TWISTOR_GOLD).next_to(point, UR, buff=0.1)

        self.play(GrowFromCenter(point), Write(point_label))

        # Animate line appearing in twistor space
        line = Line(
            RIGHT * 2.5 + UP * 1.5,
            RIGHT * 4.5 + DOWN * 1.5,
            color=TWISTOR_GOLD,
            stroke_width=4
        )
        line_label = MathTex(r"L_p", color=TWISTOR_GOLD)
        line_label.next_to(line, RIGHT)

        arrow1 = Arrow(LEFT * 1.5, RIGHT * 1.5, color=SPIN_PURPLE)

        self.play(GrowArrow(arrow1))
        self.play(Create(line), Write(line_label))
        self.wait()

        # Clear for reverse correspondence
        self.play(
            FadeOut(point),
            FadeOut(point_label),
            FadeOut(line),
            FadeOut(line_label),
            FadeOut(arrow1)
        )

        # Point in twistor space to light ray
        twist_point = Dot(RIGHT * 3.5, radius=0.15, color=TWISTOR_BLUE)
        twist_point_label = MathTex("Z", color=TWISTOR_BLUE)
        twist_point_label.next_to(twist_point, UR, buff=0.1)

        self.play(GrowFromCenter(twist_point), Write(twist_point_label))

        # Light ray in Minkowski space
        light_ray = Line(
            LEFT * 5 + DOWN * 1.5,
            LEFT * 2 + UP * 1.5,
            color=LIGHT_RAY,
            stroke_width=4
        )
        ray_label = Text("Light Ray", font_size=20, color=LIGHT_RAY)
        ray_label.next_to(light_ray, LEFT)

        arrow2 = Arrow(RIGHT * 1.5, LEFT * 1.5, color=SPIN_PURPLE)

        self.play(GrowArrow(arrow2))
        self.play(Create(light_ray), Write(ray_label))
        self.wait()

        # Summary
        summary = VGroup(
            MathTex(r"\text{Point } p \in \mathbb{M}", font_size=32),
            MathTex(r"\longleftrightarrow", font_size=32),
            MathTex(r"\text{Line } L_p \subset \mathbb{PT}", font_size=32)
        ).arrange(RIGHT, buff=0.3)

        summary2 = VGroup(
            MathTex(r"\text{Point } Z \in \mathbb{PT}", font_size=32),
            MathTex(r"\longleftrightarrow", font_size=32),
            MathTex(r"\text{Light ray in } \mathbb{M}", font_size=32)
        ).arrange(RIGHT, buff=0.3)

        summaries = VGroup(summary, summary2).arrange(DOWN, buff=0.4)
        summaries.to_edge(DOWN)

        box = SurroundingRectangle(summaries, color=SPIN_PURPLE, buff=0.2)

        self.play(
            FadeIn(summaries),
            Create(box)
        )
        self.wait(2)


class LightConeTwistor(ThreeDScene):
    """
    3D visualization of light cones and their twistor correspondence.
    """

    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)

        title = Text("Light Cone in Minkowski Space", font_size=36)
        title.to_corner(UL)
        self.add_fixed_in_frame_mobjects(title)

        # Create light cone
        future_cone = Surface(
            lambda u, v: np.array([
                v * np.cos(u),
                v * np.sin(u),
                v
            ]),
            u_range=[0, TAU],
            v_range=[0, 2],
            resolution=(32, 8),
            fill_opacity=0.4,
            stroke_width=1,
            stroke_color=NULL_CONE,
            fill_color=NULL_CONE
        )

        past_cone = Surface(
            lambda u, v: np.array([
                v * np.cos(u),
                v * np.sin(u),
                -v
            ]),
            u_range=[0, TAU],
            v_range=[0, 2],
            resolution=(32, 8),
            fill_opacity=0.4,
            stroke_width=1,
            stroke_color=NULL_CONE,
            fill_color=NULL_CONE
        )

        # Origin point
        origin = Sphere(radius=0.1, color=TWISTOR_GOLD)

        # Axes
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            z_length=6
        )

        t_label = Text("t", font_size=24)
        t_label.next_to(axes.z_axis, UP)
        self.add_fixed_orientation_mobjects(t_label)

        self.play(Create(axes))
        self.play(Create(future_cone), Create(past_cone))
        self.play(Create(origin))
        self.add(t_label)

        # Light ray
        light_ray = Line3D(
            start=np.array([-2, 0, -2]),
            end=np.array([2, 0, 2]),
            color=LIGHT_RAY,
            thickness=0.05
        )

        self.play(Create(light_ray))

        # Rotate camera
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(5)
        self.stop_ambient_camera_rotation()


# Scene list for rendering
if __name__ == "__main__":
    scenes = [
        TwistorSpaceScene,
        IncidenceRelationScene,
        NullTwistorScene,
        PenroseCorrespondence,
        LightConeTwistor
    ]
    print("Available scenes:")
    for s in scenes:
        print(f"  - {s.__name__}")
