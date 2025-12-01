"""
Advanced Visualizations for Twistor Theory and Spin Networks
=============================================================
More sophisticated animations showcasing deeper concepts.

Run with: manim -pql advanced_visualizations.py SpinFoamVertex
"""

from manim import *
import numpy as np

# Color scheme
TWISTOR_BLUE = "#2962FF"
TWISTOR_GOLD = "#FFC107"
SPIN_RED = "#F44336"
SPIN_GREEN = "#4CAF50"
SPIN_PURPLE = "#9C27B0"
NODE_COLOR = "#009688"
EDGE_COLOR = "#673AB7"
INTERTWINER = "#E91E63"


class SpinFoamVertex(ThreeDScene):
    """
    3D visualization of a spin foam vertex (4-simplex).
    """

    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)

        # Title
        title = Text("Spin Foam Vertex (4-Simplex)", font_size=36, color=SPIN_PURPLE)
        title.to_corner(UL)
        self.add_fixed_in_frame_mobjects(title)

        # Create 4-simplex (5 vertices, 10 edges)
        # Vertices of a 4-simplex projected to 3D
        vertices = [
            np.array([0, 0, 1.5]),
            np.array([1.2, 0, -0.5]),
            np.array([-0.6, 1, -0.5]),
            np.array([-0.6, -1, -0.5]),
            np.array([0, 0, -0.3])  # Central vertex
        ]

        # Create spheres for vertices
        spheres = VGroup(*[
            Sphere(radius=0.12, color=NODE_COLOR).move_to(v)
            for v in vertices
        ])

        # Create edges (all pairs)
        edges = VGroup()
        for i in range(5):
            for j in range(i + 1, 5):
                # Different thickness based on edge
                width = 0.03 if (i == 4 or j == 4) else 0.05
                edge = Line3D(
                    start=vertices[i],
                    end=vertices[j],
                    color=EDGE_COLOR,
                    thickness=width
                )
                edges.add(edge)

        self.play(Create(edges), run_time=2)
        self.play(Create(spheres))

        # Labels for spin labels on faces
        face_label = Text("Faces carry spin labels jf", font_size=24)
        face_label.to_corner(DR)
        self.add_fixed_in_frame_mobjects(face_label)
        self.play(Write(face_label))

        # Rotate to show 3D structure
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(5)
        self.stop_ambient_camera_rotation()

        # Show amplitude formula
        amplitude = MathTex(
            r"A_v = \{15j\}",
            font_size=32
        )
        amplitude.to_corner(DL)
        self.add_fixed_in_frame_mobjects(amplitude)
        self.play(Write(amplitude))
        self.wait(2)


class TwistorCorrespondence3D(ThreeDScene):
    """
    3D visualization of the twistor correspondence.
    """

    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)

        # Create Minkowski-like space on left
        axes = ThreeDAxes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            z_range=[-2, 2, 1],
            x_length=4,
            y_length=4,
            z_length=4
        ).shift(LEFT * 3)

        # Light cone
        cone = Surface(
            lambda u, v: np.array([
                v * np.cos(u) - 3,
                v * np.sin(u),
                v
            ]),
            u_range=[0, TAU],
            v_range=[0, 1.5],
            resolution=(24, 8),
            fill_opacity=0.3,
            stroke_width=1,
            stroke_color=TWISTOR_GOLD,
            fill_color=TWISTOR_GOLD
        )

        # Point in spacetime
        point = Sphere(radius=0.15, color=SPIN_RED).move_to(LEFT * 3 + UP * 0.5)

        # Twistor space representation (sphere)
        twistor_space = Surface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.sin(v) + 3,
                1.5 * np.sin(u) * np.sin(v),
                1.5 * np.cos(v)
            ]),
            u_range=[0, TAU],
            v_range=[0, PI],
            resolution=(24, 12),
            fill_opacity=0.3,
            stroke_width=0.5,
            stroke_color=TWISTOR_BLUE,
            fill_color=TWISTOR_BLUE
        )

        # Line in twistor space (corresponding to point)
        line = Line3D(
            start=np.array([3, -1.3, 0.5]),
            end=np.array([3, 1.3, -0.5]),
            color=SPIN_RED,
            thickness=0.08
        )

        self.play(Create(axes))
        self.play(Create(cone), Create(point))
        self.wait()
        self.play(Create(twistor_space), Create(line))

        # Label
        title = Text("Twistor Correspondence", font_size=32, color=TWISTOR_BLUE)
        title.to_corner(UL)
        self.add_fixed_in_frame_mobjects(title)

        correspondence = Text(
            "Point ↔ Line",
            font_size=24
        )
        correspondence.to_corner(UR)
        self.add_fixed_in_frame_mobjects(correspondence)

        self.play(Write(title), Write(correspondence))

        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(5)
        self.stop_ambient_camera_rotation()


class PachnerMoves(Scene):
    """
    Visualization of Pachner moves on triangulations.
    """

    def construct(self):
        title = Text("Pachner Moves", font_size=48, color=NODE_COLOR)
        title.to_edge(UP)
        self.play(Write(title))

        subtitle = Text(
            "Local moves that preserve triangulation equivalence",
            font_size=24
        )
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))

        # 2-2 Move (in 3D, but shown as 2D projection)
        move_22_title = Text("2-2 Move", font_size=28, color=SPIN_GREEN)
        move_22_title.shift(LEFT * 3.5 + UP * 1)
        self.play(Write(move_22_title))

        # Initial configuration: two triangles sharing an edge
        t1 = Polygon(
            LEFT * 1 + UP * 1,
            RIGHT * 1 + UP * 1,
            ORIGIN + DOWN * 0.5,
            stroke_width=3,
            stroke_color=EDGE_COLOR,
            fill_color=EDGE_COLOR,
            fill_opacity=0.2
        )
        t2 = Polygon(
            LEFT * 1 + UP * 1,
            RIGHT * 1 + UP * 1,
            ORIGIN + UP * 2.5,
            stroke_width=3,
            stroke_color=EDGE_COLOR,
            fill_color=EDGE_COLOR,
            fill_opacity=0.2
        )
        initial = VGroup(t1, t2).shift(LEFT * 3.5 + DOWN * 1)

        self.play(Create(initial))
        self.wait()

        # Arrow
        arrow = Arrow(LEFT * 1, RIGHT * 1, color=TWISTOR_GOLD)
        arrow.shift(DOWN * 0.5)
        self.play(GrowArrow(arrow))

        # Final configuration: same vertices, different diagonal
        t3 = Polygon(
            LEFT * 1 + UP * 1,
            ORIGIN + DOWN * 0.5,
            ORIGIN + UP * 2.5,
            stroke_width=3,
            stroke_color=EDGE_COLOR,
            fill_color=SPIN_GREEN,
            fill_opacity=0.2
        )
        t4 = Polygon(
            RIGHT * 1 + UP * 1,
            ORIGIN + DOWN * 0.5,
            ORIGIN + UP * 2.5,
            stroke_width=3,
            stroke_color=EDGE_COLOR,
            fill_color=SPIN_GREEN,
            fill_opacity=0.2
        )
        final = VGroup(t3, t4).shift(RIGHT * 3.5 + DOWN * 1)

        self.play(Create(final))
        self.wait()

        # Connection to spin networks
        note = VGroup(
            Text("In LQG:", font_size=24, weight=BOLD),
            Text("Pachner moves correspond to", font_size=20),
            Text("spin foam vertex amplitudes", font_size=20)
        ).arrange(DOWN, buff=0.15)
        note.to_edge(DOWN, buff=0.8)

        box = SurroundingRectangle(note, color=SPIN_PURPLE, buff=0.15)
        self.play(FadeIn(note), Create(box))
        self.wait(2)


class CoherentStates(Scene):
    """
    Visualization of coherent spin network states.
    """

    def construct(self):
        title = Text("Coherent Spin Network States", font_size=44, color=TWISTOR_BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        # Explanation
        explanation = VGroup(
            Text("Coherent states interpolate between", font_size=24),
            Text("quantum spin networks and classical geometry", font_size=24)
        ).arrange(DOWN, buff=0.2)
        explanation.next_to(title, DOWN, buff=0.3)
        self.play(Write(explanation))

        # Quantum side: discrete spin network
        quantum_label = Text("Quantum", font_size=28, color=SPIN_RED)
        quantum_label.shift(LEFT * 4 + UP * 0.5)

        # Simple spin network
        qv1 = Dot(LEFT * 5, radius=0.2, color=NODE_COLOR)
        qv2 = Dot(LEFT * 3, radius=0.2, color=NODE_COLOR)
        qe = Line(qv1.get_center(), qv2.get_center(), stroke_width=4, color=EDGE_COLOR)
        j_label = MathTex(r"j=2", font_size=24).next_to(qe, UP)

        quantum = VGroup(qe, qv1, qv2, j_label).shift(DOWN * 1)

        self.play(Write(quantum_label), FadeIn(quantum))

        # Classical side: smooth geometry
        classical_label = Text("Classical", font_size=28, color=SPIN_GREEN)
        classical_label.shift(RIGHT * 4 + UP * 0.5)

        # Smooth curve representing classical geometry
        curve = ParametricFunction(
            lambda t: np.array([t + 3, 0.3 * np.sin(2 * t) - 1, 0]),
            t_range=[-1.5, 1.5],
            color=SPIN_GREEN,
            stroke_width=4
        )

        classical = VGroup(curve)

        self.play(Write(classical_label), Create(classical))
        self.wait()

        # Coherent state in the middle
        coherent_label = Text("Coherent State", font_size=28, color=SPIN_PURPLE)
        coherent_label.shift(DOWN * 2.5)

        # Blurred/superposed version
        coherent = VGroup()
        for offset in np.linspace(-0.1, 0.1, 5):
            cv1 = Dot(LEFT * 0.5 + UP * offset, radius=0.15, 
                     color=NODE_COLOR, fill_opacity=0.4)
            cv2 = Dot(RIGHT * 0.5 + DOWN * offset, radius=0.15, 
                     color=NODE_COLOR, fill_opacity=0.4)
            ce = Line(cv1.get_center(), cv2.get_center(), 
                     stroke_width=3, color=EDGE_COLOR, stroke_opacity=0.4)
            coherent.add(ce, cv1, cv2)

        coherent.shift(DOWN * 1)

        self.play(Write(coherent_label), FadeIn(coherent))
        self.wait()

        # Formula
        formula = MathTex(
            r"|j, \vec{n}\rangle = e^{i j \vec{n} \cdot \vec{J}} |j, j\rangle",
            font_size=36
        )
        formula.to_edge(DOWN, buff=0.5)
        self.play(Write(formula))
        self.wait(2)


class HolonomyFlux(Scene):
    """
    Visualization of holonomy-flux algebra.
    """

    def construct(self):
        title = Text("Holonomy-Flux Algebra", font_size=48, color=EDGE_COLOR)
        title.to_edge(UP)
        self.play(Write(title))

        # Loop/holonomy
        loop_label = Text("Holonomy", font_size=28, color=TWISTOR_BLUE)
        loop_label.shift(LEFT * 3.5 + UP * 1.5)

        # Draw a loop
        loop = Circle(radius=1, color=TWISTOR_BLUE, stroke_width=4)
        loop.shift(LEFT * 3.5)
        arrow_on_loop = Arrow(
            LEFT * 3.5 + UP * 1,
            LEFT * 3.5 + UP * 1 + RIGHT * 0.3,
            color=TWISTOR_BLUE
        )

        hol_formula = MathTex(
            r"h_\gamma = \mathcal{P} \exp\left(\int_\gamma A\right)",
            font_size=28
        )
        hol_formula.next_to(loop, DOWN, buff=0.3)

        self.play(Write(loop_label), Create(loop), GrowArrow(arrow_on_loop))
        self.play(Write(hol_formula))

        # Surface/flux
        flux_label = Text("Flux", font_size=28, color=SPIN_GREEN)
        flux_label.shift(RIGHT * 3.5 + UP * 1.5)

        # Draw a surface
        surface = Polygon(
            RIGHT * 2.5 + UP * 0.8,
            RIGHT * 4.5 + UP * 0.8,
            RIGHT * 4.5 + DOWN * 0.8,
            RIGHT * 2.5 + DOWN * 0.8,
            fill_color=SPIN_GREEN,
            fill_opacity=0.3,
            stroke_color=SPIN_GREEN,
            stroke_width=2
        )

        # Normal vector
        normal = Arrow(
            RIGHT * 3.5,
            RIGHT * 3.5 + OUT * 1.5 + UP * 0.5,
            color=SPIN_GREEN
        )

        flux_formula = MathTex(
            r"E_S^i = \int_S E^i",
            font_size=28
        )
        flux_formula.next_to(surface, DOWN, buff=0.3)

        self.play(Write(flux_label), Create(surface))
        self.play(Write(flux_formula))
        self.wait()

        # Commutation relation
        commutator = MathTex(
            r"[E_S^i, h_\gamma] = i\hbar \, (\text{intersection}) \, \tau^i h_\gamma",
            font_size=32
        )
        commutator.to_edge(DOWN, buff=1)

        box = SurroundingRectangle(commutator, color=SPIN_PURPLE, buff=0.2)

        self.play(Write(commutator), Create(box))
        self.wait()

        # Show intersection
        intersection = Dot(
            LEFT * 3.5 + RIGHT * 3.5 * 0.3,  # Approximate intersection point
            radius=0.15,
            color=INTERTWINER
        )
        int_label = Text("intersection!", font_size=20, color=INTERTWINER)
        int_label.next_to(intersection, UP)

        self.play(GrowFromCenter(intersection), Write(int_label))
        self.wait(2)


class QuantumTetrahedron(ThreeDScene):
    """
    3D visualization of a quantum tetrahedron.
    """

    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=-30 * DEGREES)

        title = Text("Quantum Tetrahedron", font_size=36, color=NODE_COLOR)
        title.to_corner(UL)
        self.add_fixed_in_frame_mobjects(title)

        # Tetrahedron vertices
        vertices = [
            np.array([0, 0, 1.5]),
            np.array([1.2, 0, -0.5]),
            np.array([-0.6, 1, -0.5]),
            np.array([-0.6, -1, -0.5])
        ]

        # Edges
        edges = VGroup()
        edge_pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3), (3, 1)]

        for i, j in edge_pairs:
            edge = Line3D(
                start=vertices[i],
                end=vertices[j],
                color=EDGE_COLOR,
                thickness=0.04
            )
            edges.add(edge)

        # Vertices as spheres
        spheres = VGroup(*[
            Sphere(radius=0.1, color=NODE_COLOR).move_to(v)
            for v in vertices
        ])

        # Faces (with slight transparency)
        faces = VGroup()
        face_indices = [(0, 1, 2), (0, 2, 3), (0, 3, 1), (1, 3, 2)]
        colors = [SPIN_RED, SPIN_GREEN, TWISTOR_BLUE, SPIN_PURPLE]

        for indices, color in zip(face_indices, colors):
            face = Polygon(
                *[vertices[i] for i in indices],
                fill_color=color,
                fill_opacity=0.3,
                stroke_width=0
            )
            faces.add(face)

        self.play(Create(edges))
        self.play(Create(spheres))
        self.play(FadeIn(faces))

        # Area labels for faces
        face_label = Text("Each face: area = √j(j+1)", font_size=24)
        face_label.to_corner(DR)
        self.add_fixed_in_frame_mobjects(face_label)
        self.play(Write(face_label))

        # Closure constraint
        closure = MathTex(
            r"\sum_{f=1}^{4} \vec{J}_f = 0",
            font_size=32
        )
        closure.to_corner(DL)
        self.add_fixed_in_frame_mobjects(closure)
        self.play(Write(closure))

        # Rotate
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(5)
        self.stop_ambient_camera_rotation()


# Main execution
if __name__ == "__main__":
    scenes = [
        SpinFoamVertex,
        TwistorCorrespondence3D,
        PachnerMoves,
        CoherentStates,
        HolonomyFlux,
        QuantumTetrahedron
    ]
    print("Available advanced scenes:")
    for s in scenes:
        print(f"  - {s.__name__}")
