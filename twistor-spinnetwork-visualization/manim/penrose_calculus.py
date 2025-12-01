"""
Penrose Graphical Calculus - Manim Animations
=============================================
Visualization of Penrose's graphical notation for tensors.

Run with: manim -pql penrose_calculus.py PenroseBasics
"""

from manim import *
import numpy as np

# Custom color scheme
TWISTOR_BLUE = "#2962FF"
TWISTOR_GOLD = "#FFC107"
SPIN_RED = "#F44336"
SPIN_GREEN = "#4CAF50"
SPIN_PURPLE = "#9C27B0"
NODE_COLOR = "#009688"
EDGE_COLOR = "#673AB7"
INTERTWINER = "#E91E63"


class PenroseBasics(Scene):
    """
    Basic elements of Penrose graphical notation.
    """

    def construct(self):
        title = Text("Penrose Graphical Calculus", font_size=48, color=SPIN_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))

        subtitle = Text("A visual language for tensor algebra", font_size=28)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(subtitle, shift=UP))
        self.wait()

        self.play(FadeOut(subtitle))

        # Basic elements
        elements_title = Text("Basic Elements", font_size=36)
        elements_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(elements_title))

        # Vector (upward arrow)
        vector_group = self.create_vector_diagram()
        vector_group.shift(LEFT * 4.5 + DOWN * 0.5)

        # Covector (downward arrow)
        covector_group = self.create_covector_diagram()
        covector_group.shift(LEFT * 1.5 + DOWN * 0.5)

        # Tensor
        tensor_group = self.create_tensor_diagram()
        tensor_group.shift(RIGHT * 1.5 + DOWN * 0.5)

        # Metric
        metric_group = self.create_metric_diagram()
        metric_group.shift(RIGHT * 4.5 + DOWN * 0.5)

        # Animate all
        for group in [vector_group, covector_group, tensor_group, metric_group]:
            self.play(FadeIn(group))
            self.wait(0.3)

        self.wait()

        # Operations section
        self.play(
            FadeOut(elements_title),
            VGroup(vector_group, covector_group, tensor_group, metric_group).animate.shift(UP * 0.5).scale(0.8)
        )

        ops_title = Text("Operations", font_size=36)
        ops_title.move_to(DOWN * 0.5)
        self.play(Write(ops_title))

        # Contraction
        contraction = self.create_contraction_diagram()
        contraction.shift(LEFT * 3 + DOWN * 2.5)

        # Tensor product
        product = self.create_product_diagram()
        product.shift(DOWN * 2.5)

        # Trace
        trace = self.create_trace_diagram()
        trace.shift(RIGHT * 3 + DOWN * 2.5)

        self.play(FadeIn(contraction), FadeIn(product), FadeIn(trace))
        self.wait(2)

    def create_vector_diagram(self):
        line = Line(DOWN * 0.8, UP * 0.8, stroke_width=4, color=SPIN_RED)
        arrow = Triangle(fill_color=SPIN_RED, fill_opacity=1, stroke_width=0)
        arrow.scale(0.15).rotate(-PI / 2).move_to(line.get_end())
        label = MathTex(r"v^a", font_size=32, color=SPIN_RED)
        label.next_to(line, RIGHT)
        name = Text("Vector", font_size=20)
        name.next_to(line, DOWN, buff=0.5)
        return VGroup(line, arrow, label, name)

    def create_covector_diagram(self):
        line = Line(UP * 0.8, DOWN * 0.8, stroke_width=4, color=SPIN_GREEN)
        arrow = Triangle(fill_color=SPIN_GREEN, fill_opacity=1, stroke_width=0)
        arrow.scale(0.15).rotate(PI / 2).move_to(line.get_end())
        label = MathTex(r"w_a", font_size=32, color=SPIN_GREEN)
        label.next_to(line, RIGHT)
        name = Text("Covector", font_size=20)
        name.next_to(line, DOWN, buff=0.5)
        return VGroup(line, arrow, label, name)

    def create_tensor_diagram(self):
        box = Rectangle(width=0.8, height=0.8, fill_color=TWISTOR_BLUE,
                       fill_opacity=0.3, stroke_color=TWISTOR_BLUE)
        T_label = MathTex("T", font_size=28, color=TWISTOR_BLUE).move_to(box)

        up_line = Line(box.get_top(), box.get_top() + UP * 0.5,
                       stroke_width=3, color=SPIN_RED)
        down_line = Line(box.get_bottom(), box.get_bottom() + DOWN * 0.5,
                         stroke_width=3, color=SPIN_GREEN)

        label = MathTex(r"T^a{}_b", font_size=28)
        label.next_to(box, RIGHT, buff=0.3)
        name = Text("Tensor", font_size=20)
        name.next_to(down_line, DOWN, buff=0.3)

        return VGroup(up_line, down_line, box, T_label, label, name)

    def create_metric_diagram(self):
        arc1 = ArcBetweenPoints(
            LEFT * 0.4, RIGHT * 0.4,
            angle=-PI,
            stroke_width=4,
            color=SPIN_PURPLE
        )
        arc2 = ArcBetweenPoints(
            LEFT * 0.4 + DOWN * 0.8, RIGHT * 0.4 + DOWN * 0.8,
            angle=PI,
            stroke_width=4,
            color=SPIN_PURPLE
        )
        label = MathTex(r"g_{ab}", font_size=28, color=SPIN_PURPLE)
        label.next_to(arc1, RIGHT, buff=0.5)
        name = Text("Metric", font_size=20)
        name.next_to(arc2, DOWN, buff=0.3)

        return VGroup(arc1, arc2, label, name)

    def create_contraction_diagram(self):
        line1 = Line(DOWN * 0.5, UP * 0.1, stroke_width=4, color=SPIN_RED)
        line2 = Line(UP * 0.1, UP * 0.7, stroke_width=4, color=SPIN_GREEN)
        dot = Dot(UP * 0.1, radius=0.1, color=BLACK)
        name = Text("Contraction", font_size=18)
        name.next_to(line1, DOWN, buff=0.3)
        return VGroup(line1, line2, dot, name)

    def create_product_diagram(self):
        line1 = Line(LEFT * 0.3 + DOWN * 0.5, LEFT * 0.3 + UP * 0.7,
                     stroke_width=4, color=SPIN_RED)
        line2 = Line(RIGHT * 0.3 + DOWN * 0.5, RIGHT * 0.3 + UP * 0.7,
                     stroke_width=4, color=SPIN_GREEN)
        name = Text("Tensor Product", font_size=18)
        name.next_to(VGroup(line1, line2), DOWN, buff=0.3)
        return VGroup(line1, line2, name)

    def create_trace_diagram(self):
        box = Rectangle(width=0.6, height=0.6, fill_color=TWISTOR_BLUE,
                       fill_opacity=0.3, stroke_color=TWISTOR_BLUE)
        T_label = MathTex("T", font_size=24, color=TWISTOR_BLUE).move_to(box)

        arc = ArcBetweenPoints(
            box.get_top() + LEFT * 0.15,
            box.get_top() + RIGHT * 0.15,
            angle=-PI,
            stroke_width=3,
            color=EDGE_COLOR
        )
        arc.shift(UP * 0.4)

        name = Text("Trace", font_size=18)
        name.next_to(box, DOWN, buff=0.3)

        return VGroup(box, T_label, arc, name)


class SpinorNotation(Scene):
    """
    Penrose's spinor notation using graphical calculus.
    """

    def construct(self):
        title = Text("Spinor Graphical Notation", font_size=48, color=TWISTOR_BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        # Unprimed spinor
        unprimed = VGroup(
            Line(DOWN * 1, UP * 1, stroke_width=5, color=SPIN_RED),
            MathTex(r"\xi^A", font_size=36, color=SPIN_RED).shift(RIGHT * 0.8)
        )
        unprimed.shift(LEFT * 4)

        unprimed_label = Text("Unprimed\nSpinor", font_size=20, color=SPIN_RED)
        unprimed_label.next_to(unprimed, DOWN, buff=0.5)

        # Primed (dotted) spinor
        primed_line = DashedLine(DOWN * 1, UP * 1, stroke_width=5, color=SPIN_GREEN)
        primed = VGroup(
            primed_line,
            MathTex(r"\bar{\eta}^{A'}", font_size=36, color=SPIN_GREEN).shift(RIGHT * 0.8)
        )
        primed.shift(LEFT * 1)

        primed_label = Text("Primed\nSpinor", font_size=20, color=SPIN_GREEN)
        primed_label.next_to(primed, DOWN, buff=0.5)

        # Epsilon tensor
        eps_center = RIGHT * 2
        eps = VGroup(
            Line(eps_center + UP * 0.8, eps_center, stroke_width=4, color=SPIN_RED),
            Line(eps_center + UP * 0.8 + RIGHT * 0.6, eps_center,
                 stroke_width=4, color=SPIN_RED),
            Dot(eps_center, radius=0.12, color=TWISTOR_GOLD),
            MathTex(r"\epsilon_{AB}", font_size=32).shift(RIGHT * 3.5)
        )

        eps_label = Text("Epsilon\nTensor", font_size=20)
        eps_label.next_to(eps, DOWN, buff=0.5)

        self.play(FadeIn(unprimed), Write(unprimed_label))
        self.wait(0.5)
        self.play(FadeIn(primed), Write(primed_label))
        self.wait(0.5)
        self.play(FadeIn(eps), Write(eps_label))
        self.wait()

        # Raising and lowering indices
        self.play(
            VGroup(unprimed, unprimed_label, primed, primed_label, eps, eps_label).animate.shift(UP * 0.5).scale(0.8)
        )

        index_title = Text("Raising and Lowering Indices", font_size=32)
        index_title.move_to(DOWN * 0.5)
        self.play(Write(index_title))

        # Show contraction with epsilon
        formula = MathTex(
            r"\xi_A = \epsilon_{AB} \xi^B",
            font_size=40
        )
        formula.move_to(DOWN * 1.5)

        # Graphical version
        graph_eps = VGroup(
            Line(DOWN * 0.5 + LEFT * 0.3, UP * 0.3 + LEFT * 0.3,
                 stroke_width=4, color=SPIN_RED),
            ArcBetweenPoints(
                UP * 0.3 + LEFT * 0.3, UP * 0.3 + RIGHT * 0.3,
                angle=PI,
                stroke_width=4,
                color=TWISTOR_GOLD
            ),
            Line(UP * 0.3 + RIGHT * 0.3, UP * 1.1 + RIGHT * 0.3,
                 stroke_width=4, color=SPIN_RED)
        )
        graph_eps.shift(RIGHT * 3 + DOWN * 1.5)

        self.play(Write(formula))
        self.play(Create(graph_eps))
        self.wait(2)


class TwistorDiagrams(Scene):
    """
    Twistor diagrams in Penrose notation.
    """

    def construct(self):
        title = Text("Twistor Diagrams", font_size=48, color=SPIN_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))

        # Twistor line
        twistor = VGroup(
            Line(DOWN * 1.2, UP * 1.2, stroke_width=5, color=TWISTOR_BLUE),
            Dot(DOWN * 1.2, radius=0.1, color=TWISTOR_BLUE),
            Dot(UP * 1.2, radius=0.1, color=TWISTOR_BLUE)
        )
        twistor.shift(LEFT * 4)
        twistor_label = MathTex(r"Z^\alpha", font_size=32, color=TWISTOR_BLUE)
        twistor_label.next_to(twistor, RIGHT)
        twistor_name = Text("Twistor", font_size=24)
        twistor_name.next_to(twistor, DOWN, buff=0.5)

        # Dual twistor (dashed)
        dual = VGroup(
            DashedLine(DOWN * 1.2, UP * 1.2, stroke_width=5, color=SPIN_RED),
            Dot(DOWN * 1.2, radius=0.1, color=SPIN_RED),
            Dot(UP * 1.2, radius=0.1, color=SPIN_RED)
        )
        dual.shift(LEFT * 1)
        dual_label = MathTex(r"W_\alpha", font_size=32, color=SPIN_RED)
        dual_label.next_to(dual, RIGHT)
        dual_name = Text("Dual Twistor", font_size=24)
        dual_name.next_to(dual, DOWN, buff=0.5)

        # Contraction
        contraction = VGroup(
            Line(DOWN * 0.8, ORIGIN, stroke_width=5, color=TWISTOR_BLUE),
            DashedLine(ORIGIN, UP * 0.8, stroke_width=5, color=SPIN_RED),
            Dot(ORIGIN, radius=0.15, color=SPIN_PURPLE)
        )
        contraction.shift(RIGHT * 2)
        contraction_label = MathTex(r"Z^\alpha W_\alpha", font_size=28)
        contraction_label.next_to(contraction, RIGHT, buff=0.3)
        contraction_name = Text("Contraction", font_size=24)
        contraction_name.next_to(contraction, DOWN, buff=0.5)

        # 3-vertex
        vertex_center = RIGHT * 5
        vertex = VGroup(
            Line(vertex_center, vertex_center + UP * 1 + LEFT * 0.5,
                 stroke_width=5, color=TWISTOR_BLUE),
            Line(vertex_center, vertex_center + UP * 1 + RIGHT * 0.5,
                 stroke_width=5, color=TWISTOR_BLUE),
            DashedLine(vertex_center, vertex_center + DOWN * 1,
                       stroke_width=5, color=SPIN_RED),
            Dot(vertex_center, radius=0.15, color=NODE_COLOR)
        )
        vertex_name = Text("3-Vertex", font_size=24)
        vertex_name.next_to(vertex, DOWN, buff=0.5)

        # Animate
        self.play(
            FadeIn(twistor), Write(twistor_label), Write(twistor_name)
        )
        self.wait(0.3)
        self.play(
            FadeIn(dual), Write(dual_label), Write(dual_name)
        )
        self.wait(0.3)
        self.play(
            FadeIn(contraction), Write(contraction_label), Write(contraction_name)
        )
        self.wait(0.3)
        self.play(
            FadeIn(vertex), Write(vertex_name)
        )
        self.wait(2)


class WignerSymbols(Scene):
    """
    Visualization of Wigner 3j and 6j symbols.
    """

    def construct(self):
        title = Text("Wigner Symbols", font_size=48, color=NODE_COLOR)
        title.to_edge(UP)
        self.play(Write(title))

        # 3j symbol
        symbol_3j = Text("Wigner 3j-Symbol", font_size=32, color=SPIN_GREEN)
        symbol_3j.shift(LEFT * 3 + UP * 2)

        # Triangle for 3j
        triangle_center = LEFT * 3 + DOWN * 0.5
        triangle = Polygon(
            triangle_center + UP * 1,
            triangle_center + DOWN * 0.5 + LEFT * 1,
            triangle_center + DOWN * 0.5 + RIGHT * 1,
            stroke_width=4,
            stroke_color=EDGE_COLOR,
            fill_opacity=0
        )

        vertices_3j = VGroup(*[
            Dot(p, radius=0.15, color=NODE_COLOR)
            for p in [
                triangle_center + UP * 1,
                triangle_center + DOWN * 0.5 + LEFT * 1,
                triangle_center + DOWN * 0.5 + RIGHT * 1
            ]
        ])

        j_labels_3j = VGroup(
            MathTex(r"j_1", font_size=24).next_to(triangle, LEFT),
            MathTex(r"j_2", font_size=24).next_to(triangle, RIGHT),
            MathTex(r"j_3", font_size=24).next_to(triangle, DOWN)
        )

        formula_3j = MathTex(
            r"\begin{pmatrix} j_1 & j_2 & j_3 \\ m_1 & m_2 & m_3 \end{pmatrix}",
            font_size=28
        )
        formula_3j.next_to(triangle, DOWN, buff=1)

        # 6j symbol
        symbol_6j = Text("Wigner 6j-Symbol", font_size=32, color=SPIN_PURPLE)
        symbol_6j.shift(RIGHT * 3 + UP * 2)

        # Tetrahedron for 6j
        tet_center = RIGHT * 3 + DOWN * 0.5

        # Tetrahedron vertices
        v1 = tet_center + UP * 0.8
        v2 = tet_center + DOWN * 0.5 + LEFT * 1
        v3 = tet_center + DOWN * 0.5 + RIGHT * 1
        v4 = tet_center + DOWN * 0.1

        tetrahedron = VGroup(
            Line(v1, v2, stroke_width=3, color=EDGE_COLOR),
            Line(v2, v3, stroke_width=3, color=EDGE_COLOR),
            Line(v3, v1, stroke_width=3, color=EDGE_COLOR),
            DashedLine(v1, v4, stroke_width=2, color=EDGE_COLOR),
            DashedLine(v2, v4, stroke_width=2, color=EDGE_COLOR),
            DashedLine(v3, v4, stroke_width=2, color=EDGE_COLOR)
        )

        vertices_6j = VGroup(*[
            Dot(v, radius=0.12, color=NODE_COLOR)
            for v in [v1, v2, v3, v4]
        ])

        formula_6j = MathTex(
            r"\begin{Bmatrix} j_1 & j_2 & j_{12} \\ j_3 & j & j_{23} \end{Bmatrix}",
            font_size=28
        )
        formula_6j.next_to(tetrahedron, DOWN, buff=1)

        # Animate
        self.play(Write(symbol_3j))
        self.play(Create(triangle), FadeIn(vertices_3j), Write(j_labels_3j))
        self.play(Write(formula_3j))
        self.wait()

        self.play(Write(symbol_6j))
        self.play(Create(tetrahedron), FadeIn(vertices_6j))
        self.play(Write(formula_6j))
        self.wait()

        # Connection to spin networks
        connection = VGroup(
            Text("These symbols appear in:", font_size=24, weight=BOLD),
            Text("• Spin network evaluation", font_size=20),
            Text("• Recoupling theory", font_size=20),
            Text("• LQG vertex amplitudes", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        connection.to_edge(DOWN, buff=0.5)

        box = SurroundingRectangle(connection, color=TWISTOR_GOLD, buff=0.2)
        self.play(FadeIn(connection), Create(box))
        self.wait(2)


class RecouplingTheory(Scene):
    """
    Visualization of recoupling in spin networks.
    """

    def construct(self):
        title = Text("Recoupling Theory", font_size=48, color=EDGE_COLOR)
        title.to_edge(UP)
        self.play(Write(title))

        subtitle = Text("Changing the coupling scheme", font_size=28)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(subtitle))

        # Initial coupling: ((j1 ⊗ j2) ⊗ j3)
        initial_center = LEFT * 3 + DOWN * 0.5

        # Draw initial tree
        i_v1 = Dot(initial_center + UP * 1.5 + LEFT * 1, radius=0.15, color=NODE_COLOR)
        i_v2 = Dot(initial_center + UP * 1.5, radius=0.15, color=NODE_COLOR)
        i_v3 = Dot(initial_center + UP * 1.5 + RIGHT * 1, radius=0.15, color=NODE_COLOR)
        i_v4 = Dot(initial_center + UP * 0.5 + LEFT * 0.5, radius=0.2, color=INTERTWINER)
        i_v5 = Dot(initial_center + DOWN * 0.5, radius=0.2, color=INTERTWINER)

        i_edges = VGroup(
            Line(i_v1.get_center(), i_v4.get_center(), stroke_width=4, color=EDGE_COLOR),
            Line(i_v2.get_center(), i_v4.get_center(), stroke_width=4, color=EDGE_COLOR),
            Line(i_v4.get_center(), i_v5.get_center(), stroke_width=4, color=EDGE_COLOR),
            Line(i_v3.get_center(), i_v5.get_center(), stroke_width=4, color=EDGE_COLOR),
            Line(i_v5.get_center(), initial_center + DOWN * 1.5, stroke_width=4, color=EDGE_COLOR)
        )

        i_labels = VGroup(
            MathTex(r"j_1", font_size=20).next_to(i_v1, UP),
            MathTex(r"j_2", font_size=20).next_to(i_v2, UP),
            MathTex(r"j_3", font_size=20).next_to(i_v3, UP),
            MathTex(r"j_{12}", font_size=18).next_to(i_edges[2], LEFT)
        )

        initial = VGroup(i_edges, i_v1, i_v2, i_v3, i_v4, i_v5, i_labels)

        initial_name = Text("((j₁ ⊗ j₂) ⊗ j₃)", font_size=24)
        initial_name.next_to(initial, DOWN, buff=0.3)

        # Arrow
        arrow = Arrow(LEFT * 0.5, RIGHT * 0.5, color=TWISTOR_GOLD, stroke_width=4)
        arrow.shift(DOWN * 0.5)
        arrow_label = MathTex(r"\{6j\}", font_size=28, color=TWISTOR_GOLD)
        arrow_label.next_to(arrow, UP)

        # Final coupling: (j1 ⊗ (j2 ⊗ j3))
        final_center = RIGHT * 3 + DOWN * 0.5

        f_v1 = Dot(final_center + UP * 1.5 + LEFT * 1, radius=0.15, color=NODE_COLOR)
        f_v2 = Dot(final_center + UP * 1.5, radius=0.15, color=NODE_COLOR)
        f_v3 = Dot(final_center + UP * 1.5 + RIGHT * 1, radius=0.15, color=NODE_COLOR)
        f_v4 = Dot(final_center + UP * 0.5 + RIGHT * 0.5, radius=0.2, color=INTERTWINER)
        f_v5 = Dot(final_center + DOWN * 0.5, radius=0.2, color=INTERTWINER)

        f_edges = VGroup(
            Line(f_v2.get_center(), f_v4.get_center(), stroke_width=4, color=EDGE_COLOR),
            Line(f_v3.get_center(), f_v4.get_center(), stroke_width=4, color=EDGE_COLOR),
            Line(f_v4.get_center(), f_v5.get_center(), stroke_width=4, color=EDGE_COLOR),
            Line(f_v1.get_center(), f_v5.get_center(), stroke_width=4, color=EDGE_COLOR),
            Line(f_v5.get_center(), final_center + DOWN * 1.5, stroke_width=4, color=EDGE_COLOR)
        )

        f_labels = VGroup(
            MathTex(r"j_1", font_size=20).next_to(f_v1, UP),
            MathTex(r"j_2", font_size=20).next_to(f_v2, UP),
            MathTex(r"j_3", font_size=20).next_to(f_v3, UP),
            MathTex(r"j_{23}", font_size=18).next_to(f_edges[2], RIGHT)
        )

        final = VGroup(f_edges, f_v1, f_v2, f_v3, f_v4, f_v5, f_labels)

        final_name = Text("(j₁ ⊗ (j₂ ⊗ j₃))", font_size=24)
        final_name.next_to(final, DOWN, buff=0.3)

        # Animate
        self.play(FadeIn(initial), Write(initial_name))
        self.wait()
        self.play(GrowArrow(arrow), Write(arrow_label))
        self.play(FadeIn(final), Write(final_name))
        self.wait()

        # Formula
        formula = MathTex(
            r"\sum_{j_{12}} [j_{12}] [j_{23}] \begin{Bmatrix} j_1 & j_2 & j_{12} \\ j_3 & j & j_{23} \end{Bmatrix}",
            font_size=32
        )
        formula.to_edge(DOWN, buff=0.8)

        self.play(Write(formula))
        self.wait(2)


# Main execution
if __name__ == "__main__":
    scenes = [
        PenroseBasics,
        SpinorNotation,
        TwistorDiagrams,
        WignerSymbols,
        RecouplingTheory
    ]
    print("Available scenes:")
    for s in scenes:
        print(f"  - {s.__name__}")
