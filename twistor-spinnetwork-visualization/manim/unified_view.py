"""
Unified View: Twistors and Spin Networks
=========================================
Visualizing the deep connections between Twistor Theory and Spin Networks.

Run with: manim -pql unified_view.py TwistorSpinNetworkConnection
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
NODE_COLOR = "#009688"
EDGE_COLOR = "#673AB7"
INTERTWINER = "#E91E63"


class TwistorSpinNetworkConnection(Scene):
    """
    Visualization of the deep connections between Twistor Theory and Spin Networks.
    """

    def construct(self):
        # Title sequence
        title = Text("The Deep Connection", font_size=56, color=SPIN_PURPLE)
        subtitle = Text("Twistor Theory ⟷ Spin Networks", font_size=36)
        subtitle.next_to(title, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=UP))
        self.wait()
        self.play(FadeOut(title), FadeOut(subtitle))

        # Penrose's vision
        penrose = Text("Roger Penrose's Vision", font_size=48, color=TWISTOR_GOLD)
        penrose.to_edge(UP)
        self.play(Write(penrose))

        quote = Text(
            '"Both twistors and spin networks arose from\n'
            'the same fundamental question: What is the\n'
            'quantum nature of spacetime geometry?"',
            font_size=24,
            slant=ITALIC
        )
        quote.next_to(penrose, DOWN, buff=0.5)
        self.play(FadeIn(quote))
        self.wait(2)

        self.play(FadeOut(quote), penrose.animate.scale(0.6).to_corner(UL))

        # Create side-by-side comparison
        # Twistor Theory box
        twistor_box = self.create_twistor_side()
        twistor_box.shift(LEFT * 3.5)

        # Spin Networks box
        spin_box = self.create_spin_network_side()
        spin_box.shift(RIGHT * 3.5)

        self.play(FadeIn(twistor_box), FadeIn(spin_box))
        self.wait()

        # Connection arrows
        connections = self.create_connections()
        self.play(
            LaggedStart(*[Create(c) for c in connections], lag_ratio=0.2)
        )
        self.wait()

        # Central unifying concept
        central = self.create_central_concept()
        self.play(FadeIn(central))
        self.wait(2)

    def create_twistor_side(self):
        # Title
        title = Text("Twistor Theory", font_size=32, color=TWISTOR_BLUE)
        title.shift(UP * 2.5)

        # Key concepts
        concepts = VGroup(
            self.concept_item("Complex geometry", TWISTOR_BLUE),
            self.concept_item("Light rays", TWISTOR_BLUE),
            self.concept_item("Null structures", TWISTOR_BLUE),
            self.concept_item("CP³ space", TWISTOR_BLUE),
            self.concept_item("Holomorphic", TWISTOR_BLUE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        concepts.next_to(title, DOWN, buff=0.5)

        # Small twistor diagram
        diagram = VGroup(
            Line(DOWN * 0.5, UP * 0.5, stroke_width=4, color=TWISTOR_BLUE),
            Dot(DOWN * 0.5, radius=0.08, color=TWISTOR_BLUE),
            Dot(UP * 0.5, radius=0.08, color=TWISTOR_BLUE),
            MathTex(r"Z^\alpha", font_size=24, color=TWISTOR_BLUE).shift(RIGHT * 0.5)
        )
        diagram.next_to(concepts, DOWN, buff=0.5)

        box = SurroundingRectangle(
            VGroup(title, concepts, diagram),
            color=TWISTOR_BLUE,
            buff=0.3
        )

        return VGroup(box, title, concepts, diagram)

    def create_spin_network_side(self):
        # Title
        title = Text("Spin Networks", font_size=32, color=SPIN_GREEN)
        title.shift(UP * 2.5)

        # Key concepts
        concepts = VGroup(
            self.concept_item("Combinatorial", SPIN_GREEN),
            self.concept_item("Discrete geometry", SPIN_GREEN),
            self.concept_item("SU(2) reps", SPIN_GREEN),
            self.concept_item("Graph states", SPIN_GREEN),
            self.concept_item("LQG basis", SPIN_GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        concepts.next_to(title, DOWN, buff=0.5)

        # Small spin network diagram
        diagram = self.create_mini_spin_network()
        diagram.next_to(concepts, DOWN, buff=0.5)

        box = SurroundingRectangle(
            VGroup(title, concepts, diagram),
            color=SPIN_GREEN,
            buff=0.3
        )

        return VGroup(box, title, concepts, diagram)

    def concept_item(self, text, color):
        bullet = Dot(radius=0.06, color=color)
        label = Text(text, font_size=20)
        return VGroup(bullet, label).arrange(RIGHT, buff=0.2)

    def create_mini_spin_network(self):
        v1 = Dot(LEFT * 0.5, radius=0.1, color=NODE_COLOR)
        v2 = Dot(RIGHT * 0.5, radius=0.1, color=NODE_COLOR)
        v3 = Dot(UP * 0.4, radius=0.1, color=NODE_COLOR)

        e1 = Line(v1.get_center(), v2.get_center(), stroke_width=3, color=EDGE_COLOR)
        e2 = Line(v2.get_center(), v3.get_center(), stroke_width=2, color=EDGE_COLOR)
        e3 = Line(v3.get_center(), v1.get_center(), stroke_width=4, color=EDGE_COLOR)

        return VGroup(e1, e2, e3, v1, v2, v3)

    def create_connections(self):
        # Double-headed arrows showing correspondences
        arrow1 = DoubleArrow(
            LEFT * 1.2 + UP * 1.5,
            RIGHT * 1.2 + UP * 1.5,
            color=SPIN_PURPLE,
            stroke_width=3
        )
        label1 = Text("SU(2)", font_size=18, color=SPIN_PURPLE)
        label1.next_to(arrow1, UP, buff=0.1)

        arrow2 = DoubleArrow(
            LEFT * 1.2 + UP * 0.5,
            RIGHT * 1.2 + UP * 0.5,
            color=SPIN_PURPLE,
            stroke_width=3
        )
        label2 = Text("Discreteness", font_size=18, color=SPIN_PURPLE)
        label2.next_to(arrow2, UP, buff=0.1)

        arrow3 = DoubleArrow(
            LEFT * 1.2 + DOWN * 0.5,
            RIGHT * 1.2 + DOWN * 0.5,
            color=SPIN_PURPLE,
            stroke_width=3
        )
        label3 = Text("Quantum Geometry", font_size=18, color=SPIN_PURPLE)
        label3.next_to(arrow3, UP, buff=0.1)

        return VGroup(
            VGroup(arrow1, label1),
            VGroup(arrow2, label2),
            VGroup(arrow3, label3)
        )

    def create_central_concept(self):
        # Central box
        text = VGroup(
            Text("Common Ground:", font_size=28, weight=BOLD, color=TWISTOR_GOLD),
            Text("Both seek to describe the", font_size=22),
            Text("quantum structure of spacetime", font_size=22),
            Text("using algebraic/geometric methods", font_size=22)
        ).arrange(DOWN, buff=0.2)
        text.to_edge(DOWN, buff=0.8)

        box = SurroundingRectangle(text, color=TWISTOR_GOLD, buff=0.3)

        return VGroup(box, text)


class QuantumGeometryBridge(Scene):
    """
    Visualization of how both frameworks describe quantum geometry.
    """

    def construct(self):
        title = Text("Quantum Geometry", font_size=56, color=NODE_COLOR)
        title.to_edge(UP)
        self.play(Write(title))

        # Area quantization - common to both
        area_formula = MathTex(
            r"A \sim \ell_P^2 \sum_i \sqrt{j_i(j_i+1)}",
            font_size=40
        )
        area_formula.next_to(title, DOWN, buff=0.5)

        area_box = SurroundingRectangle(area_formula, color=TWISTOR_GOLD, buff=0.15)
        area_label = Text("Discrete Area Spectrum", font_size=24, color=TWISTOR_GOLD)
        area_label.next_to(area_box, DOWN, buff=0.2)

        self.play(Write(area_formula), Create(area_box), Write(area_label))
        self.wait()

        # Visual representation
        # Create a surface with quantized area
        surface = self.create_quantum_surface()
        surface.shift(DOWN * 1.5)

        self.play(FadeIn(surface))
        self.wait()

        # Labels
        interpretation = VGroup(
            Text("In Spin Networks:", font_size=24, weight=BOLD, color=SPIN_GREEN),
            Text("Edges carry spin j → area quanta", font_size=20),
            Text("", font_size=10),
            Text("In Twistor Theory:", font_size=24, weight=BOLD, color=TWISTOR_BLUE),
            Text("SU(2) spinor structure → geometric degrees of freedom", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        interpretation.to_edge(DOWN, buff=0.5)

        box = SurroundingRectangle(interpretation, color=WHITE, buff=0.2)
        self.play(FadeIn(interpretation), Create(box))
        self.wait(2)

    def create_quantum_surface(self):
        # Grid of small squares with varying "spin weights"
        squares = VGroup()
        colors = [SPIN_RED, SPIN_GREEN, TWISTOR_BLUE, SPIN_PURPLE, TWISTOR_GOLD]

        for i in range(-3, 4):
            for j in range(-1, 2):
                sq = Square(
                    side_length=0.4,
                    fill_opacity=0.3 + 0.1 * np.random.random(),
                    fill_color=np.random.choice(colors),
                    stroke_width=1,
                    stroke_color=WHITE
                )
                sq.shift(RIGHT * i * 0.45 + UP * j * 0.45)
                squares.add(sq)

        # Add some labels
        label = Text("Quantized Areas", font_size=20)
        label.next_to(squares, DOWN, buff=0.3)

        return VGroup(squares, label)


class HistoricalTimeline(Scene):
    """
    Historical development timeline.
    """

    def construct(self):
        title = Text("Historical Development", font_size=48, color=SPIN_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))

        # Timeline
        timeline = Line(LEFT * 6, RIGHT * 6, color=WHITE, stroke_width=2)
        timeline.shift(DOWN * 0.5)

        # Events
        events = [
            ("1967", "Penrose\nTwistor Theory", TWISTOR_BLUE, LEFT * 4.5),
            ("1971", "Penrose\nSpin Networks", SPIN_GREEN, LEFT * 1.5),
            ("1988", "Ashtekar\nNew Variables", TWISTOR_GOLD, RIGHT * 1.5),
            ("1995", "Rovelli-Smolin\nLQG States", SPIN_RED, RIGHT * 4.5)
        ]

        event_groups = VGroup()
        for year, text, color, pos in events:
            dot = Dot(pos + DOWN * 0.5, radius=0.15, color=color)
            year_label = Text(year, font_size=20, color=color)
            year_label.next_to(dot, DOWN, buff=0.2)
            desc = Text(text, font_size=16)
            desc.next_to(year_label, DOWN, buff=0.1)

            event_groups.add(VGroup(dot, year_label, desc))

        self.play(Create(timeline))
        for event in event_groups:
            self.play(FadeIn(event), run_time=0.8)
            self.wait(0.3)

        self.wait()

        # Connecting theme
        theme = VGroup(
            Text("Common Thread:", font_size=28, weight=BOLD),
            Text("Describing spacetime geometry using", font_size=22),
            Text("algebraic and combinatorial structures", font_size=22)
        ).arrange(DOWN, buff=0.2)
        theme.to_edge(DOWN, buff=0.5)

        box = SurroundingRectangle(theme, color=SPIN_PURPLE, buff=0.2)
        self.play(FadeIn(theme), Create(box))
        self.wait(2)


class FuturePerspectives(Scene):
    """
    Future directions and open problems.
    """

    def construct(self):
        title = Text("Future Perspectives", font_size=48, color=TWISTOR_GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        # Open questions
        questions = VGroup(
            self.create_question(
                "Unification?",
                "Can twistor methods be fully\nintegrated with spin foam models?",
                TWISTOR_BLUE
            ),
            self.create_question(
                "Dynamics?",
                "How does spacetime emerge from\nthe discrete structures?",
                SPIN_GREEN
            ),
            self.create_question(
                "Matter?",
                "How do particles and fields\nfit into the picture?",
                SPIN_PURPLE
            )
        ).arrange(RIGHT, buff=0.5)
        questions.next_to(title, DOWN, buff=0.8)

        for q in questions:
            self.play(FadeIn(q))
            self.wait(0.5)

        self.wait()

        # Final thought
        final = VGroup(
            Text("The search continues for a complete", font_size=28),
            Text("theory of quantum spacetime geometry...", font_size=28)
        ).arrange(DOWN, buff=0.2)
        final.to_edge(DOWN, buff=1)

        self.play(FadeIn(final))
        self.wait(2)

    def create_question(self, title_text, desc_text, color):
        title = Text(title_text, font_size=24, weight=BOLD, color=color)
        desc = Text(desc_text, font_size=16)
        desc.next_to(title, DOWN, buff=0.2)

        group = VGroup(title, desc)
        box = SurroundingRectangle(group, color=color, buff=0.2)

        return VGroup(box, title, desc)


class MathematicalStructures(Scene):
    """
    Deep mathematical structures shared by both theories.
    """

    def construct(self):
        title = Text("Shared Mathematical Structures", font_size=44, color=EDGE_COLOR)
        title.to_edge(UP)
        self.play(Write(title))

        # Structure 1: SU(2)
        su2 = VGroup(
            Text("SU(2) / SL(2,ℂ)", font_size=32, weight=BOLD, color=SPIN_PURPLE),
            VGroup(
                Text("• Spinor representations", font_size=20),
                Text("• Clebsch-Gordan decomposition", font_size=20),
                Text("• Wigner symbols", font_size=20)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        ).arrange(DOWN, buff=0.3)
        su2.shift(LEFT * 3.5 + UP * 0.5)

        # Structure 2: Complex geometry
        complex_geom = VGroup(
            Text("Complex Geometry", font_size=32, weight=BOLD, color=TWISTOR_BLUE),
            VGroup(
                Text("• Projective spaces", font_size=20),
                Text("• Holomorphic bundles", font_size=20),
                Text("• Cohomology", font_size=20)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        ).arrange(DOWN, buff=0.3)
        complex_geom.shift(RIGHT * 3.5 + UP * 0.5)

        # Structure 3: Graphs/Networks
        graphs = VGroup(
            Text("Graph Theory", font_size=32, weight=BOLD, color=NODE_COLOR),
            VGroup(
                Text("• Labeled graphs", font_size=20),
                Text("• Evaluation rules", font_size=20),
                Text("• Category theory", font_size=20)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        ).arrange(DOWN, buff=0.3)
        graphs.shift(DOWN * 2)

        # Animate
        self.play(FadeIn(su2))
        self.wait(0.5)
        self.play(FadeIn(complex_geom))
        self.wait(0.5)
        self.play(FadeIn(graphs))
        self.wait()

        # Connecting lines
        line1 = DashedLine(
            su2.get_bottom() + DOWN * 0.1,
            graphs.get_top() + UP * 0.1 + LEFT * 1,
            color=WHITE,
            stroke_width=2
        )
        line2 = DashedLine(
            complex_geom.get_bottom() + DOWN * 0.1,
            graphs.get_top() + UP * 0.1 + RIGHT * 1,
            color=WHITE,
            stroke_width=2
        )
        line3 = DashedLine(
            su2.get_right() + RIGHT * 0.1,
            complex_geom.get_left() + LEFT * 0.1,
            color=WHITE,
            stroke_width=2
        )

        self.play(Create(line1), Create(line2), Create(line3))
        self.wait(2)


# Main execution
if __name__ == "__main__":
    scenes = [
        TwistorSpinNetworkConnection,
        QuantumGeometryBridge,
        HistoricalTimeline,
        FuturePerspectives,
        MathematicalStructures
    ]
    print("Available scenes:")
    for s in scenes:
        print(f"  - {s.__name__}")
