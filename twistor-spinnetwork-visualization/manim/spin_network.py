"""
Spin Networks - Manim Animations
================================
Comprehensive visualization of Spin Network concepts.

Run with: manim -pql spin_network.py SpinNetworkBasics
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
INTERTWINER = "#E91E63"


class SpinNetworkBasics(Scene):
    """
    Introduction to Spin Networks and their basic structure.
    """

    def construct(self):
        # Title
        title = Text("Spin Networks", font_size=72, color=NODE_COLOR)
        subtitle = Text("Quantum States of Geometry", font_size=36, color=EDGE_COLOR)
        subtitle.next_to(title, DOWN)

        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP))
        self.wait()
        self.play(FadeOut(title), FadeOut(subtitle))

        # Definition
        def_title = Text("Definition", font_size=48, color=NODE_COLOR)
        def_title.to_edge(UP)

        definition = VGroup(
            Text("A spin network consists of:", font_size=28),
            VGroup(
                Text("1. ", font_size=24),
                Text("A graph ", font_size=24, color=EDGE_COLOR),
                MathTex(r"\Gamma = (V, E)", font_size=28)
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("2. ", font_size=24),
                Text("Spin labels ", font_size=24, color=SPIN_RED),
                MathTex(r"j_e \in \{0, \frac{1}{2}, 1, \frac{3}{2}, ...\}", font_size=28)
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("3. ", font_size=24),
                Text("Intertwiners ", font_size=24, color=INTERTWINER),
                MathTex(r"i_v", font_size=28)
            ).arrange(RIGHT, buff=0.1)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        definition.next_to(def_title, DOWN, buff=0.5)

        self.play(Write(def_title))
        for item in definition:
            self.play(FadeIn(item, shift=RIGHT))
            self.wait(0.3)
        self.wait()

        self.play(FadeOut(definition), FadeOut(def_title))

        # Visual example
        example_title = Text("Example Spin Network", font_size=40)
        example_title.to_edge(UP)
        self.play(Write(example_title))

        # Create vertices
        v1 = Dot(LEFT * 3, radius=0.25, color=NODE_COLOR)
        v2 = Dot(UP * 2, radius=0.25, color=NODE_COLOR)
        v3 = Dot(RIGHT * 3, radius=0.25, color=NODE_COLOR)
        v4 = Dot(DOWN * 2, radius=0.25, color=NODE_COLOR)
        v5 = Dot(ORIGIN, radius=0.25, color=NODE_COLOR)

        vertices = VGroup(v1, v2, v3, v4, v5)

        # Create edges with different thicknesses representing spins
        e1 = Line(v1.get_center(), v2.get_center(), stroke_width=4, color=EDGE_COLOR)
        e2 = Line(v2.get_center(), v3.get_center(), stroke_width=6, color=EDGE_COLOR)
        e3 = Line(v3.get_center(), v4.get_center(), stroke_width=4, color=EDGE_COLOR)
        e4 = Line(v4.get_center(), v1.get_center(), stroke_width=3, color=EDGE_COLOR)
        e5 = Line(v1.get_center(), v5.get_center(), stroke_width=3, color=EDGE_COLOR)
        e6 = Line(v2.get_center(), v5.get_center(), stroke_width=4, color=EDGE_COLOR)
        e7 = Line(v3.get_center(), v5.get_center(), stroke_width=6, color=EDGE_COLOR)
        e8 = Line(v4.get_center(), v5.get_center(), stroke_width=4, color=EDGE_COLOR)

        edges = VGroup(e1, e2, e3, e4, e5, e6, e7, e8)

        # Spin labels
        l1 = MathTex(r"j=1", font_size=24).next_to(e1, LEFT)
        l2 = MathTex(r"j=\frac{3}{2}", font_size=24).next_to(e2, UP)
        l3 = MathTex(r"j=1", font_size=24).next_to(e3, RIGHT)
        l4 = MathTex(r"j=\frac{1}{2}", font_size=24).next_to(e4, DOWN)

        labels = VGroup(l1, l2, l3, l4)

        # Animate creation
        self.play(LaggedStart(*[Create(e) for e in edges], lag_ratio=0.1))
        self.play(LaggedStart(*[GrowFromCenter(v) for v in vertices], lag_ratio=0.1))
        self.play(LaggedStart(*[FadeIn(l) for l in labels], lag_ratio=0.2))

        self.wait()

        # Highlight intertwiner at central vertex
        highlight = Circle(radius=0.4, color=INTERTWINER, stroke_width=3)
        highlight.move_to(v5)
        int_label = Text("Intertwiner", font_size=20, color=INTERTWINER)
        int_label.next_to(highlight, DOWN, buff=0.5)

        self.play(Create(highlight), Write(int_label))
        self.wait(2)


class SU2RepresentationScene(Scene):
    """
    Visualization of SU(2) representations.
    """

    def construct(self):
        title = Text("SU(2) Representations", font_size=48, color=SPIN_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))

        # Show representations for j = 0, 1/2, 1, 3/2, 2
        representations = []

        for i, (j, color) in enumerate([
            (0, NODE_COLOR),
            (0.5, SPIN_RED),
            (1, SPIN_GREEN),
            (1.5, SPIN_PURPLE),
            (2, TWISTOR_BLUE)
        ]):
            dim = int(2 * j + 1)
            j_label = MathTex(f"j = {j if j != int(j) else int(j)}" if j != 0.5 else r"j = \frac{1}{2}",
                            font_size=28)
            if j == 1.5:
                j_label = MathTex(r"j = \frac{3}{2}", font_size=28)

            dim_label = Text(f"dim = {dim}", font_size=20)

            # Create dots for basis states
            dots = VGroup(*[
                Dot(radius=0.1, color=color)
                for _ in range(dim)
            ]).arrange(RIGHT, buff=0.2)

            # Line connecting dots
            if dim > 1:
                line = Line(
                    dots[0].get_center(),
                    dots[-1].get_center(),
                    stroke_width=3,
                    color=EDGE_COLOR
                )
                rep_group = VGroup(line, dots, j_label, dim_label)
            else:
                rep_group = VGroup(dots, j_label, dim_label)

            j_label.next_to(dots, DOWN, buff=0.3)
            dim_label.next_to(j_label, DOWN, buff=0.1)

            representations.append(rep_group)

        reps = VGroup(*representations).arrange(RIGHT, buff=1.2)
        reps.next_to(title, DOWN, buff=1)

        for rep in representations:
            self.play(FadeIn(rep), run_time=0.5)
            self.wait(0.3)

        self.wait()

        # Dimension formula
        formula = MathTex(
            r"\dim(V_j) = 2j + 1",
            font_size=48
        )
        formula.to_edge(DOWN, buff=1)
        box = SurroundingRectangle(formula, color=SPIN_PURPLE, buff=0.2)

        self.play(Write(formula), Create(box))
        self.wait(2)


class ClebschGordanScene(Scene):
    """
    Visualization of Clebsch-Gordan decomposition.
    """

    def construct(self):
        title = Text("Clebsch-Gordan Decomposition", font_size=44, color=SPIN_GREEN)
        title.to_edge(UP)
        self.play(Write(title))

        # Formula
        formula = MathTex(
            r"V_{j_1} \otimes V_{j_2} = \bigoplus_{j=|j_1-j_2|}^{j_1+j_2} V_j",
            font_size=48
        )
        formula.next_to(title, DOWN, buff=0.5)
        self.play(Write(formula))
        self.wait()

        # Example: 1 ⊗ 1/2 = 3/2 ⊕ 1/2
        self.play(formula.animate.scale(0.7).to_corner(UL).shift(DOWN * 0.5))

        example_title = Text("Example: j₁ = 1, j₂ = 1/2", font_size=32)
        example_title.next_to(formula, DOWN, buff=0.5).shift(RIGHT * 2)
        self.play(Write(example_title))

        # Visual representation
        # j = 1 representation (3 dots)
        j1_dots = VGroup(*[Dot(radius=0.12, color=SPIN_GREEN) for _ in range(3)])
        j1_dots.arrange(RIGHT, buff=0.25)
        j1_line = Line(j1_dots[0].get_center(), j1_dots[-1].get_center(),
                       stroke_width=4, color=EDGE_COLOR)
        j1_label = MathTex(r"j_1 = 1", font_size=28, color=SPIN_GREEN)
        j1_group = VGroup(j1_line, j1_dots, j1_label)
        j1_label.next_to(j1_dots, DOWN, buff=0.2)

        # j = 1/2 representation (2 dots)
        j2_dots = VGroup(*[Dot(radius=0.12, color=SPIN_RED) for _ in range(2)])
        j2_dots.arrange(RIGHT, buff=0.25)
        j2_line = Line(j2_dots[0].get_center(), j2_dots[-1].get_center(),
                       stroke_width=3, color=EDGE_COLOR)
        j2_label = MathTex(r"j_2 = \frac{1}{2}", font_size=28, color=SPIN_RED)
        j2_group = VGroup(j2_line, j2_dots, j2_label)
        j2_label.next_to(j2_dots, DOWN, buff=0.2)

        tensor = MathTex(r"\otimes", font_size=48)

        lhs = VGroup(j1_group, tensor, j2_group).arrange(RIGHT, buff=0.5)
        lhs.move_to(LEFT * 3)

        equals = MathTex(r"=", font_size=48)
        equals.next_to(lhs, RIGHT, buff=0.3)

        # Result: j = 3/2 (4 dots) ⊕ j = 1/2 (2 dots)
        j32_dots = VGroup(*[Dot(radius=0.12, color=SPIN_PURPLE) for _ in range(4)])
        j32_dots.arrange(RIGHT, buff=0.2)
        j32_line = Line(j32_dots[0].get_center(), j32_dots[-1].get_center(),
                        stroke_width=5, color=EDGE_COLOR)
        j32_label = MathTex(r"j = \frac{3}{2}", font_size=28, color=SPIN_PURPLE)
        j32_group = VGroup(j32_line, j32_dots, j32_label)
        j32_label.next_to(j32_dots, DOWN, buff=0.2)

        oplus = MathTex(r"\oplus", font_size=48)

        j12_dots = VGroup(*[Dot(radius=0.12, color=SPIN_RED) for _ in range(2)])
        j12_dots.arrange(RIGHT, buff=0.25)
        j12_line = Line(j12_dots[0].get_center(), j12_dots[-1].get_center(),
                        stroke_width=3, color=EDGE_COLOR)
        j12_label = MathTex(r"j = \frac{1}{2}", font_size=28, color=SPIN_RED)
        j12_group = VGroup(j12_line, j12_dots, j12_label)
        j12_label.next_to(j12_dots, DOWN, buff=0.2)

        rhs = VGroup(j32_group, oplus, j12_group).arrange(RIGHT, buff=0.5)
        rhs.next_to(equals, RIGHT, buff=0.3)

        # Animate
        self.play(FadeIn(lhs))
        self.wait(0.5)
        self.play(Write(equals))
        self.play(FadeIn(rhs))
        self.wait()

        # Triangle inequality
        triangle = VGroup(
            Text("Triangle Inequality:", font_size=28, weight=BOLD),
            MathTex(r"|j_1 - j_2| \leq j \leq j_1 + j_2", font_size=36)
        ).arrange(DOWN, buff=0.2)
        triangle.to_edge(DOWN, buff=1)

        box = SurroundingRectangle(triangle, color=TWISTOR_GOLD, buff=0.2)
        self.play(FadeIn(triangle), Create(box))
        self.wait(2)


class IntertwinerScene(Scene):
    """
    Visualization of intertwiners at vertices.
    """

    def construct(self):
        title = Text("Intertwiners", font_size=56, color=INTERTWINER)
        title.to_edge(UP)
        self.play(Write(title))

        # Definition
        definition = MathTex(
            r"i_v \in \mathrm{Inv}_{SU(2)}(V_{j_1} \otimes \cdots \otimes V_{j_n})",
            font_size=36
        )
        definition.next_to(title, DOWN, buff=0.5)
        self.play(Write(definition))
        self.wait()
        self.play(definition.animate.scale(0.8).to_corner(UL).shift(DOWN * 0.8))

        # Show different valence vertices
        # 3-valent
        v3_center = LEFT * 4
        v3 = Dot(v3_center, radius=0.3, color=NODE_COLOR)
        e3_1 = Line(v3_center, v3_center + UP * 1.5 + LEFT * 0.5,
                    stroke_width=4, color=EDGE_COLOR)
        e3_2 = Line(v3_center, v3_center + UP * 1.5 + RIGHT * 0.5,
                    stroke_width=3, color=EDGE_COLOR)
        e3_3 = Line(v3_center, v3_center + DOWN * 1.5,
                    stroke_width=5, color=EDGE_COLOR)

        l3_1 = MathTex(r"j_1", font_size=24).next_to(e3_1, LEFT)
        l3_2 = MathTex(r"j_2", font_size=24).next_to(e3_2, RIGHT)
        l3_3 = MathTex(r"j_3", font_size=24).next_to(e3_3, RIGHT)

        v3_group = VGroup(e3_1, e3_2, e3_3, v3, l3_1, l3_2, l3_3)

        v3_label = Text("3-valent", font_size=24)
        v3_label.next_to(v3_group, DOWN, buff=0.5)
        v3_dim = MathTex(r"\dim \leq 1", font_size=20)
        v3_dim.next_to(v3_label, DOWN, buff=0.1)

        # 4-valent
        v4_center = ORIGIN
        v4 = Dot(v4_center, radius=0.3, color=INTERTWINER)
        e4_1 = Line(v4_center, v4_center + UP * 1.3 + LEFT * 0.8,
                    stroke_width=4, color=EDGE_COLOR)
        e4_2 = Line(v4_center, v4_center + UP * 1.3 + RIGHT * 0.8,
                    stroke_width=4, color=EDGE_COLOR)
        e4_3 = Line(v4_center, v4_center + DOWN * 1.3 + RIGHT * 0.8,
                    stroke_width=3, color=EDGE_COLOR)
        e4_4 = Line(v4_center, v4_center + DOWN * 1.3 + LEFT * 0.8,
                    stroke_width=3, color=EDGE_COLOR)

        v4_group = VGroup(e4_1, e4_2, e4_3, e4_4, v4)

        v4_label = Text("4-valent", font_size=24)
        v4_label.next_to(v4_group, DOWN, buff=0.5)
        v4_dim = MathTex(r"\dim \geq 1", font_size=20)
        v4_dim.next_to(v4_label, DOWN, buff=0.1)

        # n-valent
        v_n_center = RIGHT * 4
        v_n = Dot(v_n_center, radius=0.35, color=SPIN_PURPLE)
        n_label_inside = MathTex("n", font_size=24, color=WHITE)
        n_label_inside.move_to(v_n_center)

        edges_n = VGroup(*[
            Line(v_n_center, v_n_center + 1.3 * np.array([
                np.cos(angle), np.sin(angle), 0
            ]), stroke_width=3, color=EDGE_COLOR)
            for angle in np.linspace(0, TAU, 8, endpoint=False)
        ])

        vn_group = VGroup(edges_n, v_n, n_label_inside)

        vn_label = Text("n-valent", font_size=24)
        vn_label.next_to(vn_group, DOWN, buff=0.5)
        vn_dim = Text("Higher dim.", font_size=20)
        vn_dim.next_to(vn_label, DOWN, buff=0.1)

        # Animate all
        self.play(FadeIn(v3_group), Write(v3_label), Write(v3_dim))
        self.wait(0.5)
        self.play(FadeIn(v4_group), Write(v4_label), Write(v4_dim))
        self.wait(0.5)
        self.play(FadeIn(vn_group), Write(vn_label), Write(vn_dim))
        self.wait()

        # Invariance condition
        inv_text = VGroup(
            Text("Invariant under SU(2):", font_size=24, weight=BOLD),
            MathTex(r"g \cdot i_v = i_v \quad \forall g \in SU(2)", font_size=32)
        ).arrange(DOWN, buff=0.2)
        inv_text.to_edge(DOWN, buff=0.8)

        box = SurroundingRectangle(inv_text, color=INTERTWINER, buff=0.2)
        self.play(FadeIn(inv_text), Create(box))
        self.wait(2)


class AreaQuantizationScene(Scene):
    """
    Visualization of area quantization in Loop Quantum Gravity.
    """

    def construct(self):
        title = Text("Area Quantization", font_size=48, color=TWISTOR_GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        # Area operator eigenvalue
        formula = MathTex(
            r"\hat{A}_S |\mathcal{S}\rangle = 8\pi\gamma\ell_P^2 \sum_{e \cap S} \sqrt{j_e(j_e+1)} |\mathcal{S}\rangle",
            font_size=36
        )
        formula.next_to(title, DOWN, buff=0.5)
        self.play(Write(formula))
        self.wait()

        self.play(formula.animate.scale(0.75).to_corner(UR).shift(DOWN * 0.5))

        # Visual: surface intersecting spin network
        # Surface
        surface = Polygon(
            LEFT * 3 + DOWN * 1.5,
            RIGHT * 3 + DOWN * 1.5,
            RIGHT * 3.5 + UP * 1.5,
            LEFT * 2.5 + UP * 1.5,
            fill_color=SPIN_PURPLE,
            fill_opacity=0.3,
            stroke_color=SPIN_PURPLE,
            stroke_width=2
        )
        surface_label = Text("Surface S", font_size=24, color=SPIN_PURPLE)
        surface_label.next_to(surface, RIGHT)

        self.play(FadeIn(surface), Write(surface_label))

        # Spin network edges crossing the surface
        v1 = Dot(LEFT * 2 + DOWN * 2.5, radius=0.2, color=NODE_COLOR)
        v2 = Dot(LEFT * 1 + UP * 2.5, radius=0.2, color=NODE_COLOR)
        e1 = Line(v1.get_center(), v2.get_center(), stroke_width=5, color=EDGE_COLOR)

        v3 = Dot(RIGHT * 0.5 + DOWN * 2.5, radius=0.2, color=NODE_COLOR)
        v4 = Dot(RIGHT * 1.5 + UP * 2.5, radius=0.2, color=NODE_COLOR)
        e2 = Line(v3.get_center(), v4.get_center(), stroke_width=4, color=EDGE_COLOR)

        v5 = Dot(RIGHT * 3 + DOWN * 2.5, radius=0.2, color=NODE_COLOR)
        v6 = Dot(RIGHT * 2.5 + UP * 2.5, radius=0.2, color=NODE_COLOR)
        e3 = Line(v5.get_center(), v6.get_center(), stroke_width=3, color=EDGE_COLOR)

        edges = VGroup(e1, e2, e3)
        vertices = VGroup(v1, v2, v3, v4, v5, v6)

        self.play(Create(edges))
        self.play(FadeIn(vertices))

        # Intersection points
        int1 = Dot(LEFT * 1.5 + UP * 0.1, radius=0.15, color=LIGHT_RAY)
        int2 = Dot(RIGHT * 1 + UP * 0.3, radius=0.15, color=LIGHT_RAY)
        int3 = Dot(RIGHT * 2.7 + UP * 0.8, radius=0.15, color=LIGHT_RAY)

        intersections = VGroup(int1, int2, int3)

        self.play(LaggedStart(*[GrowFromCenter(i) for i in intersections], lag_ratio=0.2))

        # Labels for spins
        j1_label = MathTex(r"j_1 = \frac{3}{2}", font_size=24, color=LIGHT_RAY)
        j1_label.next_to(int1, LEFT)
        j2_label = MathTex(r"j_2 = 1", font_size=24, color=LIGHT_RAY)
        j2_label.next_to(int2, RIGHT)
        j3_label = MathTex(r"j_3 = \frac{1}{2}", font_size=24, color=LIGHT_RAY)
        j3_label.next_to(int3, RIGHT)

        self.play(Write(j1_label), Write(j2_label), Write(j3_label))
        self.wait()

        # Calculation
        calc = VGroup(
            MathTex(r"A_S = 8\pi\gamma\ell_P^2 \left(", font_size=28),
            MathTex(r"\sqrt{\frac{3}{2}\cdot\frac{5}{2}}", font_size=28, color=LIGHT_RAY),
            MathTex(r"+", font_size=28),
            MathTex(r"\sqrt{1 \cdot 2}", font_size=28, color=LIGHT_RAY),
            MathTex(r"+", font_size=28),
            MathTex(r"\sqrt{\frac{1}{2}\cdot\frac{3}{2}}", font_size=28, color=LIGHT_RAY),
            MathTex(r"\right)", font_size=28)
        ).arrange(RIGHT, buff=0.1)
        calc.to_edge(DOWN, buff=1)

        self.play(Write(calc))
        self.wait(2)


class SpinNetworkEvaluation(Scene):
    """
    Visualization of spin network evaluation (theta network).
    """

    def construct(self):
        title = Text("Spin Network Evaluation", font_size=48, color=EDGE_COLOR)
        title.to_edge(UP)
        self.play(Write(title))

        # Theta network
        subtitle = Text("The Theta Network", font_size=32)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(subtitle))

        # Create theta network
        left_vertex = Dot(LEFT * 2, radius=0.3, color=NODE_COLOR)
        right_vertex = Dot(RIGHT * 2, radius=0.3, color=NODE_COLOR)

        # Three edges connecting them
        top_edge = ArcBetweenPoints(
            LEFT * 2, RIGHT * 2,
            angle=-PI / 3,
            stroke_width=5,
            color=EDGE_COLOR
        )
        middle_edge = Line(
            LEFT * 2, RIGHT * 2,
            stroke_width=4,
            color=EDGE_COLOR
        )
        bottom_edge = ArcBetweenPoints(
            LEFT * 2, RIGHT * 2,
            angle=PI / 3,
            stroke_width=3,
            color=EDGE_COLOR
        )

        # Labels
        j1_label = MathTex(r"j_1", font_size=32).next_to(top_edge, UP)
        j2_label = MathTex(r"j_2", font_size=32).next_to(middle_edge, UP)
        j3_label = MathTex(r"j_3", font_size=32).next_to(bottom_edge, DOWN)

        theta_network = VGroup(
            top_edge, middle_edge, bottom_edge,
            left_vertex, right_vertex,
            j1_label, j2_label, j3_label
        )
        theta_network.shift(LEFT * 2)

        self.play(
            Create(top_edge),
            Create(middle_edge),
            Create(bottom_edge)
        )
        self.play(
            GrowFromCenter(left_vertex),
            GrowFromCenter(right_vertex)
        )
        self.play(Write(j1_label), Write(j2_label), Write(j3_label))
        self.wait()

        # Equals sign
        equals = MathTex(r"=", font_size=48)
        equals.next_to(theta_network, RIGHT, buff=0.5)
        self.play(Write(equals))

        # Result: theta coefficient
        result = MathTex(
            r"\Delta(j_1, j_2, j_3)",
            font_size=48
        )
        result.next_to(equals, RIGHT, buff=0.5)
        result_box = SurroundingRectangle(result, color=TWISTOR_GOLD, buff=0.15)

        self.play(Write(result), Create(result_box))
        self.wait()

        # Formula for theta coefficient
        formula = MathTex(
            r"\Delta(j_1, j_2, j_3) = \sqrt{\frac{(j_1+j_2-j_3)!(j_1-j_2+j_3)!(-j_1+j_2+j_3)!}{(j_1+j_2+j_3+1)!}}",
            font_size=28
        )
        formula.to_edge(DOWN, buff=1)

        self.play(Write(formula))
        self.wait(2)


class VolumeOperatorScene(Scene):
    """
    Visualization of volume operator in LQG.
    """

    def construct(self):
        title = Text("Volume Quantization", font_size=48, color=SPIN_GREEN)
        title.to_edge(UP)
        self.play(Write(title))

        # Formula
        formula = MathTex(
            r"\hat{V}_v \sim \ell_P^3 \sqrt{\left| \hat{J}_1 \cdot (\hat{J}_2 \times \hat{J}_3) \right|}",
            font_size=40
        )
        formula.next_to(title, DOWN, buff=0.5)
        self.play(Write(formula))
        self.wait()

        # Visual: 4-valent vertex with volume
        vertex_center = ORIGIN + DOWN * 0.5
        vertex = Circle(radius=0.6, color=NODE_COLOR, fill_opacity=0.8, fill_color=NODE_COLOR)
        vertex.move_to(vertex_center)
        volume_label = MathTex("V", font_size=36, color=WHITE)
        volume_label.move_to(vertex_center)

        # Four edges
        angles = [45, 135, 225, 315]
        edges = VGroup(*[
            Line(
                vertex_center,
                vertex_center + 2 * np.array([np.cos(a * DEGREES), np.sin(a * DEGREES), 0]),
                stroke_width=4 + i,
                color=EDGE_COLOR
            )
            for i, a in enumerate(angles)
        ])

        # Spin labels
        j_labels = VGroup(
            MathTex(r"j_1", font_size=28).next_to(edges[0], UR, buff=0.1),
            MathTex(r"j_2", font_size=28).next_to(edges[1], UL, buff=0.1),
            MathTex(r"j_3", font_size=28).next_to(edges[2], DL, buff=0.1),
            MathTex(r"j_4", font_size=28).next_to(edges[3], DR, buff=0.1)
        )

        self.play(Create(edges))
        self.play(FadeIn(vertex), Write(volume_label))
        self.play(Write(j_labels))
        self.wait()

        # Interpretation
        interpretation = VGroup(
            Text("Physical Interpretation:", font_size=28, weight=BOLD),
            Text("Vertices = quanta of volume", font_size=24),
            Text("Edges = quanta of area", font_size=24),
            MathTex(r"V \sim \ell_P^3 \sqrt{j_1 j_2 j_3 j_4}", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        interpretation.to_edge(DOWN, buff=0.8)

        box = SurroundingRectangle(interpretation, color=SPIN_GREEN, buff=0.2)
        self.play(FadeIn(interpretation), Create(box))
        self.wait(2)


class SpinNetworkEvolution(Scene):
    """
    Visualization of spin network evolution (spin foam vertex).
    """

    def construct(self):
        title = Text("Spin Foam: Spacetime from Spin Networks", font_size=40, color=SPIN_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))

        explanation = Text(
            "Spin networks evolve in 'time' through spin foam amplitudes",
            font_size=24
        )
        explanation.next_to(title, DOWN, buff=0.3)
        self.play(Write(explanation))

        # Initial spin network (bottom)
        v1 = Dot(LEFT * 2 + DOWN * 2, radius=0.2, color=NODE_COLOR)
        v2 = Dot(RIGHT * 2 + DOWN * 2, radius=0.2, color=NODE_COLOR)
        e_bottom = Line(v1.get_center(), v2.get_center(), stroke_width=4, color=EDGE_COLOR)
        j_bottom = MathTex(r"j", font_size=24).next_to(e_bottom, DOWN)

        initial = VGroup(e_bottom, v1, v2, j_bottom)

        # Final spin network (top) - more complex
        v3 = Dot(LEFT * 2.5 + UP * 2, radius=0.2, color=NODE_COLOR)
        v4 = Dot(ORIGIN + UP * 2.5, radius=0.2, color=NODE_COLOR)
        v5 = Dot(RIGHT * 2.5 + UP * 2, radius=0.2, color=NODE_COLOR)

        e_top1 = Line(v3.get_center(), v4.get_center(), stroke_width=4, color=EDGE_COLOR)
        e_top2 = Line(v4.get_center(), v5.get_center(), stroke_width=4, color=EDGE_COLOR)

        final = VGroup(e_top1, e_top2, v3, v4, v5)

        # Time arrow
        time_arrow = Arrow(
            LEFT * 4 + DOWN * 2,
            LEFT * 4 + UP * 2,
            color=TWISTOR_GOLD,
            stroke_width=3
        )
        time_label = Text("time", font_size=20, color=TWISTOR_GOLD)
        time_label.next_to(time_arrow, LEFT)

        self.play(FadeIn(initial))
        self.play(GrowArrow(time_arrow), Write(time_label))
        self.wait()

        # Evolution (intermediate foam)
        foam_lines = VGroup(
            DashedLine(v1.get_center(), v3.get_center(), color=SPIN_PURPLE, stroke_width=2),
            DashedLine(v1.get_center(), v4.get_center(), color=SPIN_PURPLE, stroke_width=2),
            DashedLine(v2.get_center(), v4.get_center(), color=SPIN_PURPLE, stroke_width=2),
            DashedLine(v2.get_center(), v5.get_center(), color=SPIN_PURPLE, stroke_width=2)
        )

        self.play(Create(foam_lines))
        self.play(FadeIn(final))

        # Vertex amplitude label
        vertex_point = ORIGIN + UP * 0.5
        vertex_circle = Circle(radius=0.3, color=INTERTWINER, stroke_width=3)
        vertex_circle.move_to(vertex_point)
        amp_label = MathTex(r"A_v", font_size=24, color=INTERTWINER)
        amp_label.next_to(vertex_circle, RIGHT)

        self.play(Create(vertex_circle), Write(amp_label))
        self.wait()

        # Amplitude formula
        amp_formula = MathTex(
            r"Z = \sum_{\{j_f\}} \prod_f A_f \prod_e A_e \prod_v A_v",
            font_size=36
        )
        amp_formula.to_edge(DOWN, buff=0.8)

        box = SurroundingRectangle(amp_formula, color=SPIN_PURPLE, buff=0.2)
        self.play(Write(amp_formula), Create(box))
        self.wait(2)


# Main execution
if __name__ == "__main__":
    scenes = [
        SpinNetworkBasics,
        SU2RepresentationScene,
        ClebschGordanScene,
        IntertwinerScene,
        AreaQuantizationScene,
        SpinNetworkEvaluation,
        VolumeOperatorScene,
        SpinNetworkEvolution
    ]
    print("Available scenes:")
    for s in scenes:
        print(f"  - {s.__name__}")
