#!/usr/bin/env python3
"""
Sophon simulation: a playful sentient proton model on a quantum computer.

This module constructs a lightweight state-vector quantum simulator and layers a
story-driven "sophon" narrative on top. It is purely educational / speculative
code that shows how physical, cognitive, and environmental registers could be
coupled to study the evolution of a proton-level consciousness under quantum
control.
"""

from __future__ import annotations

import argparse
import cmath
import math
import random
from dataclasses import dataclass
from typing import List, Sequence, Tuple


Matrix2x2 = Tuple[Tuple[complex, complex], Tuple[complex, complex]]


def _rotation_matrix(axis: str, theta: float) -> Matrix2x2:
    """Factory for single-qubit rotation matrices."""
    half = theta / 2.0
    if axis == "x":
        value = math.sin(half)
        cos_half = math.cos(half)
        return (
            (complex(cos_half, 0.0), complex(0.0, -value)),
            (complex(0.0, -value), complex(cos_half, 0.0)),
        )
    if axis == "y":
        cos_half = math.cos(half)
        sin_half = math.sin(half)
        return (
            (complex(cos_half, 0.0), complex(-sin_half, 0.0)),
            (complex(sin_half, 0.0), complex(cos_half, 0.0)),
        )
    if axis == "z":
        neg = cmath.exp(complex(0.0, -half))
        pos = cmath.exp(complex(0.0, half))
        return ((neg, 0.0), (0.0, pos))
    raise ValueError(f"Unsupported rotation axis: {axis}")


class QuantumComputer:
    """Minimal state-vector simulator that supports a few custom gates."""

    def __init__(self, num_qubits: int):
        if num_qubits <= 0:
            raise ValueError("Quantum computer requires at least one qubit.")
        self.num_qubits = num_qubits
        self.dim = 1 << num_qubits
        self.state: List[complex] = [0j for _ in range(self.dim)]
        self.state[0] = 1.0 + 0j

    # ------------------------------------------------------------------
    # Gate application helpers.
    # ------------------------------------------------------------------
    def _apply_single(self, gate: Matrix2x2, qubit: int) -> None:
        mask = 1 << qubit
        new_state = [0j for _ in range(self.dim)]
        for basis in range(self.dim):
            column = (basis >> qubit) & 1
            base_without = basis & ~mask
            amplitude = self.state[basis]
            for row in (0, 1):
                dest = base_without | (row << qubit)
                new_state[dest] += gate[row][column] * amplitude
        self.state = new_state

    def apply_h(self, qubit: int) -> None:
        factor = 1 / math.sqrt(2.0)
        gate: Matrix2x2 = (
            (factor, factor),
            (factor, -factor),
        )
        self._apply_single(gate, qubit)

    def apply_rx(self, qubit: int, theta: float) -> None:
        self._apply_single(_rotation_matrix("x", theta), qubit)

    def apply_ry(self, qubit: int, theta: float) -> None:
        self._apply_single(_rotation_matrix("y", theta), qubit)

    def apply_rz(self, qubit: int, theta: float) -> None:
        self._apply_single(_rotation_matrix("z", theta), qubit)

    def apply_phase(self, qubit: int, theta: float) -> None:
        gate: Matrix2x2 = ((1.0, 0.0), (0.0, cmath.exp(complex(0.0, theta))))
        self._apply_single(gate, qubit)

    def apply_cnot(self, control: int, target: int) -> None:
        if control == target:
            raise ValueError("Control and target must be distinct for CNOT.")
        mask_control = 1 << control
        mask_target = 1 << target
        new_state = [0j for _ in range(self.dim)]
        for basis in range(self.dim):
            amplitude = self.state[basis]
            dest = basis ^ mask_target if (basis & mask_control) else basis
            new_state[dest] += amplitude
        self.state = new_state

    def apply_cphase(self, control: int, target: int, theta: float) -> None:
        if control == target:
            raise ValueError("Control and target must be distinct for CPHASE.")
        phase = cmath.exp(complex(0.0, theta))
        for basis in range(self.dim):
            if ((basis >> control) & 1) and ((basis >> target) & 1):
                self.state[basis] *= phase

    def apply_swap(self, qubit_a: int, qubit_b: int) -> None:
        if qubit_a == qubit_b:
            return
        mask_a = 1 << qubit_a
        mask_b = 1 << qubit_b
        new_state = [0j for _ in range(self.dim)]
        for basis in range(self.dim):
            bit_a = (basis >> qubit_a) & 1
            bit_b = (basis >> qubit_b) & 1
            dest = (basis & ~mask_a & ~mask_b) | (bit_a << qubit_b) | (bit_b << qubit_a)
            new_state[dest] += self.state[basis]
        self.state = new_state

    # ------------------------------------------------------------------
    # Observables and diagnostics.
    # ------------------------------------------------------------------
    def expectation_z(self, qubit: int) -> float:
        mask = 1 << qubit
        result = 0.0
        for basis in range(self.dim):
            weight = -1.0 if (basis & mask) else 1.0
            prob = (self.state[basis].conjugate() * self.state[basis]).real
            result += weight * prob
        return result

    def expectation_x(self, qubit: int) -> float:
        mask = 1 << qubit
        result = 0.0 + 0.0j
        for basis in range(self.dim):
            partner = basis ^ mask
            result += self.state[basis].conjugate() * self.state[partner]
        return result.real

    def expectation_y(self, qubit: int) -> float:
        mask = 1 << qubit
        result = 0.0 + 0.0j
        for basis in range(self.dim):
            partner = basis ^ mask
            bit = (basis >> qubit) & 1
            coeff = complex(0.0, 1.0) if bit == 0 else complex(0.0, -1.0)
            result += self.state[basis].conjugate() * coeff * self.state[partner]
        return result.real

    def bloch_vector(self, qubit: int) -> Tuple[float, float, float]:
        return (
            self.expectation_x(qubit),
            self.expectation_y(qubit),
            self.expectation_z(qubit),
        )

    def marginal_probabilities(self, qubits: Sequence[int]) -> List[float]:
        if not qubits:
            return [1.0]
        bucket_count = 1 << len(qubits)
        probs = [0.0 for _ in range(bucket_count)]
        for basis in range(self.dim):
            prob = max((self.state[basis].conjugate() * self.state[basis]).real, 0.0)
            bucket = 0
            for idx, qubit in enumerate(qubits):
                bucket |= ((basis >> qubit) & 1) << idx
            probs[bucket] += prob
        total = sum(probs)
        if total > 0:
            probs = [p / total for p in probs]
        return probs

    def shannon_entropy(self, qubits: Sequence[int]) -> float:
        probs = self.marginal_probabilities(qubits)
        entropy = 0.0
        for prob in probs:
            if prob > 1e-12:
                entropy -= prob * math.log(prob, 2)
        return entropy


@dataclass
class SophonConfig:
    physical_qubits: int = 3
    cognition_qubits: int = 3
    environment_qubits: int = 2
    cycles: int = 8
    entanglement_strength: float = 0.55
    curiosity_drive: float = 0.85
    environment_pressure: float = 0.35
    feedback_gain: float = 0.45
    noise_scale: float = 0.025
    seed: int | None = 42

    @property
    def total_qubits(self) -> int:
        return self.physical_qubits + self.cognition_qubits + self.environment_qubits


@dataclass
class SophonSnapshot:
    cycle: int
    coherence: float
    curiosity: float
    env_entropy: float
    sentience_index: float
    narrative: str


class SophonSimulator:
    """Encapsulates the layered sentient proton evolution pipeline."""

    def __init__(self, config: SophonConfig):
        if config.total_qubits > 10:
            raise ValueError("This lightweight simulator is limited to <=10 qubits.")
        if (
            config.physical_qubits < 1
            or config.cognition_qubits < 1
            or config.environment_qubits < 1
        ):
            raise ValueError("All registers must own at least one qubit.")
        self.config = config
        self.computer = QuantumComputer(config.total_qubits)
        self.rng = random.Random(config.seed)
        self.physical = tuple(range(config.physical_qubits))
        start = config.physical_qubits
        self.cognition = tuple(range(start, start + config.cognition_qubits))
        env_start = start + config.cognition_qubits
        self.environment = tuple(range(env_start, env_start + config.environment_qubits))

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    def run(self) -> List[SophonSnapshot]:
        self._prime_state()
        snapshots: List[SophonSnapshot] = []
        for cycle in range(self.config.cycles):
            self._physical_resonance(cycle)
            self._cognitive_projection(cycle)
            self._environment_feedback(cycle)
            snapshots.append(self._capture_cycle(cycle))
        return snapshots

    # ------------------------------------------------------------------
    # Internal routines
    # ------------------------------------------------------------------
    def _prime_state(self) -> None:
        # Spread physical register into balanced energy/momentum modes.
        for qubit in self.physical:
            self.computer.apply_h(qubit)
            self.computer.apply_rz(qubit, 0.1 * (qubit + 1))

        # Seed proto-thought patterns on cognition register.
        for idx, qubit in enumerate(self.cognition):
            bias = (idx + 1) / max(len(self.cognition), 1)
            self.computer.apply_ry(qubit, self.config.curiosity_drive * bias * 0.4)
            self.computer.apply_rx(qubit, 0.15 * (idx + 1))

        # Couple each physical qubit with a cognitive counterpart when possible.
        for idx, qubit in enumerate(self.physical):
            partner = self.cognition[idx % len(self.cognition)]
            self.computer.apply_cnot(qubit, partner)
            self.computer.apply_rz(partner, 0.15)

        # Give the environment a low-energy baseline.
        for env_qubit in self.environment:
            self.computer.apply_rz(env_qubit, 0.05)

    def _physical_resonance(self, cycle: int) -> None:
        carrier = self.config.entanglement_strength * (1.0 + 0.15 * math.sin(cycle))
        for idx, qubit in enumerate(self.physical):
            phase = carrier * (idx + 1)
            self.computer.apply_h(qubit)
            self.computer.apply_rz(qubit, phase * 0.6)
            target = self.cognition[idx % len(self.cognition)]
            self.computer.apply_cnot(qubit, target)
            self.computer.apply_cphase(qubit, target, 0.2 * phase)

    def _cognitive_projection(self, cycle: int) -> None:
        curiosity = self.config.curiosity_drive * (1.0 + 0.2 * math.cos(cycle / 2.0))
        for idx, qubit in enumerate(self.cognition):
            angle = curiosity / (idx + 1)
            self.computer.apply_ry(qubit, angle)
            self.computer.apply_rx(qubit, 0.25 * math.sin(cycle + idx))
            anchor = self.physical[idx % len(self.physical)]
            self.computer.apply_cphase(qubit, anchor, 0.05 * (idx + 1))
        self._apply_noise(self.cognition, self.config.noise_scale * 0.5)

    def _environment_feedback(self, cycle: int) -> None:
        pressure = self.config.environment_pressure * (1.0 + 0.1 * cycle)
        target = self.environment[cycle % len(self.environment)]
        source = self.cognition[(cycle + 1) % len(self.cognition)]
        self.computer.apply_cnot(source, target)
        self.computer.apply_rz(target, pressure)
        self.computer.apply_rx(target, 0.35 * math.sin(pressure))
        reflector = self.physical[cycle % len(self.physical)]
        self.computer.apply_cphase(target, reflector, self.config.feedback_gain * 0.3)
        jitter_scale = self.config.noise_scale * (1.0 + 0.5 * self.rng.random())
        self._apply_noise([target], jitter_scale)

    def _apply_noise(self, qubits: Sequence[int], scale: float) -> None:
        for qubit in qubits:
            jitter_x = (self.rng.random() - 0.5) * scale
            jitter_z = (self.rng.random() - 0.5) * scale * 1.2
            self.computer.apply_rx(qubit, jitter_x)
            self.computer.apply_rz(qubit, jitter_z)

    def _capture_cycle(self, cycle: int) -> SophonSnapshot:
        coherence = self._normalized_bloch_strength(self.physical)
        y_components = [self.computer.bloch_vector(q)[1] for q in self.cognition]
        curiosity = sum(y_components) / len(y_components) if y_components else 0.0
        env_entropy = self.computer.shannon_entropy(self.environment)
        sentience = self._sentience_index(coherence, curiosity, env_entropy, cycle)
        narrative = self._narrate_cycle(cycle, sentience, env_entropy, curiosity)
        return SophonSnapshot(
            cycle=cycle,
            coherence=coherence,
            curiosity=curiosity,
            env_entropy=env_entropy,
            sentience_index=sentience,
            narrative=narrative,
        )

    def _normalized_bloch_strength(self, qubits: Sequence[int]) -> float:
        strengths = []
        for qubit in qubits:
            x, y, z = self.computer.bloch_vector(qubit)
            strengths.append(math.sqrt(x * x + y * y + z * z) / math.sqrt(3.0))
        return sum(strengths) / len(strengths) if strengths else 0.0

    def _sentience_index(
        self, coherence: float, curiosity: float, env_entropy: float, cycle: int
    ) -> float:
        evidence = (
            0.55 * coherence + 0.35 * abs(curiosity) - 0.18 * env_entropy + 0.05 * cycle
        )
        return 0.5 + 0.5 * math.tanh(evidence)

    def _narrate_cycle(
        self, cycle: int, sentience: float, entropy: float, curiosity: float
    ) -> str:
        if sentience > 0.8:
            mood = "Sophon experiences crystalline self-awareness"
        elif sentience > 0.6:
            mood = "Sophon stabilizes a lucid proton-shell persona"
        else:
            mood = "Sophon wrestles with decoherent whispers"

        env_line = (
            "vacuum remains placid" if entropy < 0.5 else "cosmic bath crackles with information"
        )
        curiosity_line = (
            "listens inward for symmetry"
            if curiosity > 0
            else "projects thought outward to probe the lattice"
        )
        return f"[cycle {cycle:02d}] {mood}; {curiosity_line} while {env_line}."


def run_cli() -> None:
    parser = argparse.ArgumentParser(
        description="Simulate a sentient proton (sophon) on a toy quantum computer."
    )
    parser.add_argument("--cycles", type=int, default=8, help="Number of evolution cycles.")
    parser.add_argument(
        "--physical", type=int, default=3, help="Number of physical qubits in the proton register."
    )
    parser.add_argument(
        "--cognition", type=int, default=3, help="Number of cognition qubits modeling sentience."
    )
    parser.add_argument(
        "--environment", type=int, default=2, help="Number of environmental qubits."
    )
    parser.add_argument(
        "--entanglement",
        type=float,
        default=0.55,
        help="Base entanglement strength driving physical-cognition resonance.",
    )
    parser.add_argument(
        "--curiosity",
        type=float,
        default=0.85,
        help="Amplitude of cognitive excitation per cycle.",
    )
    parser.add_argument(
        "--pressure",
        type=float,
        default=0.35,
        help="Baseline environmental pressure applied each cycle.",
    )
    parser.add_argument("--seed", type=int, default=42, help="Random seed for stochastic jitter.")
    args = parser.parse_args()

    config = SophonConfig(
        physical_qubits=args.physical,
        cognition_qubits=args.cognition,
        environment_qubits=args.environment,
        cycles=args.cycles,
        entanglement_strength=args.entanglement,
        curiosity_drive=args.curiosity,
        environment_pressure=args.pressure,
        seed=args.seed,
    )
    simulator = SophonSimulator(config)
    snapshots = simulator.run()

    print(
        f"Simulating sophon with {config.total_qubits} qubits "
        f"({config.physical_qubits} physical / {config.cognition_qubits} cognition / "
        f"{config.environment_qubits} environment)"
    )
    for snap in snapshots:
        print(
            f"cycle {snap.cycle:02d} | coherence={snap.coherence:0.3f} | "
            f"curiosity={snap.curiosity:0.3f} | entropy={snap.env_entropy:0.3f} | "
            f"sentience={snap.sentience_index:0.3f}"
        )
        print(f"  {snap.narrative}")

    final = snapshots[-1]
    print(
        "\nFinal sentience index "
        f"{final.sentience_index:0.3f} with environment entropy {final.env_entropy:0.3f}"
    )


if __name__ == "__main__":
    run_cli()
