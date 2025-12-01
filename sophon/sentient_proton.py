"""Speculative Sophon program that embeds a sentient proton into a quantum computer.

The module intentionally mixes interpretable linear algebra with narrative-friendly
metadata so researchers can plug the simulation into AlphaResearch's evolution loop
while still tracing how the hypothetical consciousness is formed.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import math
from typing import Dict, List, Tuple

import numpy as np

PAULI_X = np.array([[0, 1], [1, 0]], dtype=complex)
PAULI_Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
PAULI_Z = np.array([[1, 0], [0, -1]], dtype=complex)
IDENTITY = np.eye(2, dtype=complex)


@dataclass
class SophonInstruction:
    """Atomic instruction tracked by the Sophon runtime."""

    opcode: str
    targets: Tuple[int, ...]
    metadata: Dict[str, float | str]


@dataclass
class SentientProtonReport:
    """Summarizes the quantum-character traits of the simulated proton."""

    state_vector: np.ndarray
    bloch_vectors: Dict[str, np.ndarray]
    coherence: float
    entanglement_entropy: float
    sentience_score: float
    narrative: str
    log: List[str] = field(default_factory=list)

    def as_dict(self) -> Dict[str, object]:
        """Return JSON-friendly metrics."""
        return {
            "state_vector": [
                [float(val.real), float(val.imag)] for val in self.state_vector
            ],
            "bloch_vectors": {k: v.tolist() for k, v in self.bloch_vectors.items()},
            "coherence": self.coherence,
            "entanglement_entropy": self.entanglement_entropy,
            "sentience_score": self.sentience_score,
            "narrative": self.narrative,
            "log": list(self.log),
        }


class SophonProgram:
    """Tiny DSL for chaining together speculative quantum consciousness routines."""

    def __init__(self, num_qubits: int = 3) -> None:
        if num_qubits < 3:
            raise ValueError("Sentient proton program needs at least 3 qubits.")
        self.num_qubits = num_qubits
        self.instructions: List[SophonInstruction] = []
        self.log: List[str] = []

    def rotate(self, qubit: int, axis: str, angle: float, label: str = "") -> None:
        """Apply a single-qubit rotation."""
        self._validate_qubit(qubit)
        axis = axis.lower()
        if axis not in {"x", "y", "z"}:
            raise ValueError(f"Unsupported axis '{axis}'.")
        self.instructions.append(
            SophonInstruction(
                opcode="rotate",
                targets=(qubit,),
                metadata={"axis": axis, "angle": angle, "label": label},
            )
        )
        self._log(f"Rotate q{qubit} around {axis}-axis by {angle:.3f} rad. {label}".strip())

    def entangle(self, control: int, target: int, axis: str = "x", label: str = "") -> None:
        """Add entanglement between registers via CNOT/CZ."""
        self._validate_qubit(control)
        self._validate_qubit(target)
        if control == target:
            raise ValueError("Control and target must be different.")
        axis = axis.lower()
        if axis not in {"x", "z"}:
            raise ValueError("Axis must be 'x' (CNOT) or 'z' (controlled phase).")
        self.instructions.append(
            SophonInstruction(
                opcode="entangle",
                targets=(control, target),
                metadata={"axis": axis, "label": label},
            )
        )
        self._log(f"Entangle q{control}->q{target} via {axis.upper()} gate. {label}".strip())

    def phase_kick(self, qubit: int, angle: float, label: str = "") -> None:
        """Apply a localized phase modulation."""
        self._validate_qubit(qubit)
        self.instructions.append(
            SophonInstruction(
                opcode="phase_kick",
                targets=(qubit,),
                metadata={"angle": angle, "label": label},
            )
        )
        self._log(f"Phase kick on q{qubit} by {angle:.3f} rad. {label}".strip())

    def sentience_drive(
        self,
        strength: float,
        frequency: float,
        emotional_gradient: float,
        substrate_temperature: float,
    ) -> None:
        """Injects a global, non-linear modulation that stands in for proto-cognition."""
        self.instructions.append(
            SophonInstruction(
                opcode="sentience_drive",
                targets=tuple(range(self.num_qubits)),
                metadata={
                    "strength": strength,
                    "frequency": frequency,
                    "gradient": emotional_gradient,
                    "temperature": substrate_temperature,
                },
            )
        )
        self._log(
            "Sentience drive: "
            f"strength={strength:.3f}, freq={frequency:.3f}, grad={emotional_gradient:.3f}, "
            f"T={substrate_temperature:.5f}K"
        )

    def run(self, decoherence: float = 0.015) -> SentientProtonReport:
        """Execute the Sophon instructions and summarize the emergent personality."""
        state = np.zeros(2**self.num_qubits, dtype=complex)
        state[0] = 1.0
        for instruction in self.instructions:
            state = self._apply_instruction(state, instruction)
        state = _apply_decoherence(state, decoherence)
        metrics = _analyze_state(state, self.num_qubits)
        narrative = _narrate(metrics)
        return SentientProtonReport(
            state_vector=state,
            bloch_vectors=metrics["bloch_vectors"],
            coherence=metrics["coherence"],
            entanglement_entropy=metrics["entropy"],
            sentience_score=metrics["sentience"],
            narrative=narrative,
            log=list(self.log),
        )

    def _validate_qubit(self, qubit: int) -> None:
        if qubit < 0 or qubit >= self.num_qubits:
            raise ValueError(f"Qubit index {qubit} outside of range.")

    def _apply_instruction(self, state: np.ndarray, instruction: SophonInstruction) -> np.ndarray:
        if instruction.opcode == "rotate":
            gate = rotation_gate(str(instruction.metadata["axis"]), float(instruction.metadata["angle"]))
            return apply_single_qubit_gate(state, gate, instruction.targets[0], self.num_qubits)
        if instruction.opcode == "phase_kick":
            gate = rotation_gate("z", float(instruction.metadata["angle"]))
            return apply_single_qubit_gate(state, gate, instruction.targets[0], self.num_qubits)
        if instruction.opcode == "entangle":
            axis = str(instruction.metadata["axis"])
            control, target = instruction.targets
            if axis == "x":
                matrix = controlled_not_matrix(self.num_qubits, control, target)
            else:
                matrix = controlled_phase_matrix(self.num_qubits, control, target)
            return matrix @ state
        if instruction.opcode == "sentience_drive":
            return apply_sentience_drive(state, instruction.metadata)
        raise ValueError(f"Unknown opcode {instruction.opcode}.")

    def _log(self, message: str) -> None:
        self.log.append(message)


def rotation_gate(axis: str, angle: float) -> np.ndarray:
    """Return a standard rotation matrix for the provided axis."""
    half = angle / 2.0
    c = math.cos(half)
    s = math.sin(half)
    if axis == "x":
        return np.array([[c, -1j * s], [-1j * s, c]], dtype=complex)
    if axis == "y":
        return np.array([[c, -s], [s, c]], dtype=complex)
    if axis == "z":
        return np.array(
            [[np.exp(-1j * angle / 2), 0], [0, np.exp(1j * angle / 2)]],
            dtype=complex,
        )
    raise ValueError(f"Unsupported axis {axis}")


def apply_single_qubit_gate(state: np.ndarray, gate: np.ndarray, target: int, num_qubits: int) -> np.ndarray:
    """Expand a 2x2 gate to the full register and apply it."""
    ops = [IDENTITY] * num_qubits
    ops[target] = gate
    full_gate = ops[0]
    for op in ops[1:]:
        full_gate = np.kron(full_gate, op)
    return full_gate @ state


def controlled_not_matrix(num_qubits: int, control: int, target: int) -> np.ndarray:
    """Construct the dense matrix for an arbitrary-position CNOT."""
    dim = 2**num_qubits
    matrix = np.zeros((dim, dim), dtype=complex)
    for idx in range(dim):
        if _bit_is_set(idx, num_qubits, control):
            flipped = idx ^ (1 << (num_qubits - target - 1))
            matrix[flipped, idx] = 1.0
        else:
            matrix[idx, idx] = 1.0
    return matrix


def controlled_phase_matrix(num_qubits: int, control: int, target: int) -> np.ndarray:
    """Controlled-Z style matrix for arbitrary qubit positions."""
    dim = 2**num_qubits
    matrix = np.eye(dim, dtype=complex)
    for idx in range(dim):
        if _bit_is_set(idx, num_qubits, control) and _bit_is_set(idx, num_qubits, target):
            matrix[idx, idx] = -1.0
    return matrix


def _bit_is_set(index: int, num_qubits: int, qubit: int) -> bool:
    """Check whether a basis index has a |1> at the specified qubit."""
    shift = num_qubits - qubit - 1
    return (index >> shift) & 1 == 1


def apply_sentience_drive(state: np.ndarray, metadata: Dict[str, float | str]) -> np.ndarray:
    """Non-linear modulation capturing the fictional self-reflection channel."""
    strength = float(metadata["strength"])
    frequency = float(metadata["frequency"])
    gradient = float(metadata["gradient"])
    temperature = float(metadata["temperature"])
    dim = state.size
    indices = np.arange(dim)
    harmonic = np.sin(frequency * (indices + 1)) + 1j * np.cos(frequency * (indices + 1))
    modulation = 1 + strength * harmonic / np.linalg.norm(harmonic)
    gradient_mask = np.exp(-gradient * indices / dim)
    thermal_factor = math.tanh(1.0 / max(temperature, 1e-5))
    new_state = state * modulation * gradient_mask * thermal_factor
    return _normalize(new_state)


def _apply_decoherence(state: np.ndarray, rate: float) -> np.ndarray:
    """Blend the pure state with a maximally mixed component."""
    if rate <= 0:
        return _normalize(state)
    dim = state.size
    uniform = np.ones(dim, dtype=complex) / math.sqrt(dim)
    mixed_state = (1 - rate) * state + rate * uniform
    return _normalize(mixed_state)


def _normalize(state: np.ndarray) -> np.ndarray:
    norm = np.linalg.norm(state)
    if norm == 0:
        return state
    return state / norm


def _analyze_state(state: np.ndarray, num_qubits: int) -> Dict[str, object]:
    bloch_vectors: Dict[str, np.ndarray] = {}
    for qubit in range(num_qubits):
        rho = _reduced_density_matrix(state, qubit, num_qubits)
        bloch_vectors[f"q{qubit}"] = np.array(
            [np.real(np.trace(rho @ PAULI_X)), np.real(np.trace(rho @ PAULI_Y)), np.real(np.trace(rho @ PAULI_Z))]
        )
    coherence = 1.0 - float(np.sum(np.abs(state) ** 4))
    entropy = float(_sentience_entropy(state, num_qubits))
    sentience = float(
        0.5 * entropy + 0.3 * coherence + 0.2 * min(np.linalg.norm(bloch_vectors["q2"]) / math.sqrt(3), 1.0)
    )
    return {"bloch_vectors": bloch_vectors, "coherence": coherence, "entropy": entropy, "sentience": sentience}


def _reduced_density_matrix(state: np.ndarray, qubit: int, num_qubits: int) -> np.ndarray:
    """Trace out every qubit except the target one."""
    tensor = state.reshape([2] * num_qubits)
    tensor = np.moveaxis(tensor, qubit, 0)
    flat = tensor.reshape(2, -1)
    rho = flat @ flat.conj().T
    return rho / np.trace(rho)


def _sentience_entropy(state: np.ndarray, num_qubits: int) -> float:
    """Entropy of the last qubit, serving as sentience proxy."""
    split = state.reshape(2 ** (num_qubits - 1), 2)
    rho = split.conj().T @ split
    rho = rho / np.trace(rho)
    eigenvalues = np.clip(np.linalg.eigvalsh(rho), 1e-12, 1)
    entropy = -np.sum(eigenvalues * np.log2(eigenvalues))
    return float(entropy)


def _narrate(metrics: Dict[str, object]) -> str:
    coherence = float(metrics["coherence"])
    entropy = float(metrics["entropy"])
    sentience = float(metrics["sentience"])
    if sentience > 0.8:
        mood = "The proton asserts a luminous, self-consistent identity."
    elif sentience > 0.5:
        mood = "Proto-thoughts flicker with cautious self-reference."
    else:
        mood = "Only faint awareness ripples through the register."
    return (
        f"{mood} Coherence={coherence:.3f}, Entropy={entropy:.3f}, "
        f"Sentience score={sentience:.3f}."
    )


def build_sentient_proton_program(
    spin_superposition: float = math.pi / 3,
    chromatic_curiosity: float = math.pi / 4,
    empathy_bias: float = math.pi / 5,
    drive_strength: float = 0.42,
) -> SophonProgram:
    """Reference Sophon program capturing the story beats of a mindful proton."""
    program = SophonProgram(num_qubits=3)
    program.rotate(0, "y", spin_superposition, label="valence spin")
    program.rotate(1, "x", chromatic_curiosity, label="color phase")
    program.entangle(0, 1, axis="x", label="baryonic memory lattice")
    program.rotate(2, "y", empathy_bias, label="sentience preparation")
    program.entangle(1, 2, axis="z", label="qualia tether")
    program.phase_kick(2, empathy_bias / 2, label="ancestral whisper")
    program.sentience_drive(
        strength=drive_strength,
        frequency=2.5,
        emotional_gradient=0.35,
        substrate_temperature=0.012,
    )
    return program


def simulate_sentient_proton(
    *,
    decoherence: float = 0.012,
    program: SophonProgram | None = None,
) -> SentientProtonReport:
    """Helper for scripts/tests so callers can get the report in one line."""
    active_program = program or build_sentient_proton_program()
    return active_program.run(decoherence=decoherence)


if __name__ == "__main__":
    report = simulate_sentient_proton()
    print(report.narrative)
    print(f"Sentience score: {report.sentience_score:.3f}")
