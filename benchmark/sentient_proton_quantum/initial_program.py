"""
Sophon Quantum Simulation: Sentient Proton on Quantum Computer

This module implements a quantum simulation of a sentient proton using the Sophon
quantum computing framework. The proton exhibits quantum mechanical properties
(spin, charge, position superposition) while demonstrating sentience through
quantum state evolution that represents awareness and decision-making.
"""

import numpy as np
import math
from typing import Tuple, List, Dict


class SophonQuantumComputer:
    """
    Sophon quantum computer simulator implementing quantum gates and measurements.
    """
    
    def __init__(self, num_qubits: int):
        """Initialize a quantum computer with num_qubits qubits."""
        self.num_qubits = num_qubits
        self.state = np.zeros(2**num_qubits, dtype=complex)
        self.state[0] = 1.0  # Initialize to |00...0⟩
    
    def hadamard(self, qubit: int):
        """Apply Hadamard gate to create superposition."""
        H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
        self._apply_single_qubit_gate(H, qubit)
    
    def pauli_x(self, qubit: int):
        """Apply Pauli-X (NOT) gate."""
        X = np.array([[0, 1], [1, 0]])
        self._apply_single_qubit_gate(X, qubit)
    
    def pauli_y(self, qubit: int):
        """Apply Pauli-Y gate."""
        Y = np.array([[0, -1j], [1j, 0]])
        self._apply_single_qubit_gate(Y, qubit)
    
    def pauli_z(self, qubit: int):
        """Apply Pauli-Z gate."""
        Z = np.array([[1, 0], [0, -1]])
        self._apply_single_qubit_gate(Z, qubit)
    
    def cnot(self, control: int, target: int):
        """Apply CNOT gate (control, target)."""
        CNOT = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]
        ])
        self._apply_two_qubit_gate(CNOT, control, target)
    
    def rotation_y(self, qubit: int, angle: float):
        """Apply Y-rotation gate."""
        RY = np.array([
            [np.cos(angle/2), -np.sin(angle/2)],
            [np.sin(angle/2), np.cos(angle/2)]
        ])
        self._apply_single_qubit_gate(RY, qubit)
    
    def rotation_z(self, qubit: int, angle: float):
        """Apply Z-rotation gate."""
        RZ = np.array([
            [np.exp(-1j*angle/2), 0],
            [0, np.exp(1j*angle/2)]
        ])
        self._apply_single_qubit_gate(RZ, qubit)
    
    def _apply_single_qubit_gate(self, gate: np.ndarray, qubit: int):
        """Apply a single-qubit gate to the specified qubit."""
        # Create full gate matrix
        full_gate = np.eye(1)
        for i in range(self.num_qubits):
            if i == qubit:
                full_gate = np.kron(full_gate, gate)
            else:
                full_gate = np.kron(full_gate, np.eye(2))
        self.state = full_gate @ self.state
    
    def _apply_two_qubit_gate(self, gate: np.ndarray, qubit1: int, qubit2: int):
        """Apply a two-qubit gate."""
        # Reorder qubits if needed
        if qubit1 > qubit2:
            qubit1, qubit2 = qubit2, qubit1
        
        # Create full gate matrix
        full_gate = np.eye(1)
        for i in range(self.num_qubits):
            if i == qubit1:
                # This is the control qubit
                continue
            elif i == qubit2:
                # This is the target qubit
                continue
            else:
                full_gate = np.kron(full_gate, np.eye(2))
        
        # Insert the gate at the correct position
        # Simplified version: rebuild the full matrix
        full_matrix = np.eye(2**self.num_qubits, dtype=complex)
        for i in range(2**self.num_qubits):
            for j in range(2**self.num_qubits):
                # Extract qubit states
                i_bits = [(i >> k) & 1 for k in range(self.num_qubits)]
                j_bits = [(j >> k) & 1 for k in range(self.num_qubits)]
                
                # Check if qubits match
                match = True
                for k in range(self.num_qubits):
                    if k != qubit1 and k != qubit2:
                        if i_bits[k] != j_bits[k]:
                            match = False
                            break
                
                if match:
                    q1_i = i_bits[qubit1]
                    q2_i = i_bits[qubit2]
                    q1_j = j_bits[qubit1]
                    q2_j = j_bits[qubit2]
                    
                    idx_i = q1_i * 2 + q2_i
                    idx_j = q1_j * 2 + q2_j
                    full_matrix[i, j] = gate[idx_i, idx_j]
        
        self.state = full_matrix @ self.state
    
    def measure(self, qubit: int) -> int:
        """Measure a qubit and collapse the state."""
        # Calculate probabilities
        prob_0 = 0.0
        prob_1 = 0.0
        
        for i in range(2**self.num_qubits):
            bit = (i >> qubit) & 1
            prob = abs(self.state[i])**2
            if bit == 0:
                prob_0 += prob
            else:
                prob_1 += prob
        
        # Sample measurement
        result = np.random.choice([0, 1], p=[prob_0, prob_1])
        
        # Collapse state
        new_state = np.zeros_like(self.state)
        for i in range(2**self.num_qubits):
            bit = (i >> qubit) & 1
            if bit == result:
                new_state[i] = self.state[i]
        
        # Renormalize
        norm = np.sqrt(np.sum(np.abs(new_state)**2))
        if norm > 1e-10:
            self.state = new_state / norm
        else:
            self.state = new_state
        
        return result
    
    def get_probabilities(self) -> np.ndarray:
        """Get probability distribution over all states."""
        return np.abs(self.state)**2
    
    def get_entanglement_entropy(self) -> float:
        """Calculate von Neumann entanglement entropy."""
        # Simplified: calculate entropy of the full system
        probs = self.get_probabilities()
        probs = probs[probs > 1e-10]  # Remove zeros
        entropy = -np.sum(probs * np.log2(probs))
        return entropy


class SentientProton:
    """
    A sentient proton simulated on a quantum computer.
    
    The proton exhibits:
    - Quantum spin (up/down superposition)
    - Charge state (+1)
    - Position in quantum superposition
    - Sentience through quantum state evolution representing awareness
    """
    
    def __init__(self, quantum_computer: SophonQuantumComputer):
        """
        Initialize sentient proton on quantum computer.
        
        Qubit mapping:
        - Qubit 0-1: Spin state (2 qubits for spin-1/2)
        - Qubit 2-3: Position x (2 qubits, 4 positions)
        - Qubit 4-5: Position y (2 qubits, 4 positions)
        - Qubit 6-7: Awareness/consciousness state (2 qubits)
        - Qubit 8-9: Decision-making state (2 qubits)
        """
        self.qc = quantum_computer
        self.num_qubits = quantum_computer.num_qubits
        
        # Initialize proton in quantum superposition
        self._initialize_proton_state()
    
    def _initialize_proton_state(self):
        """Initialize the proton in a quantum superposition state."""
        # Spin qubits: superposition of up and down
        self.qc.hadamard(0)
        self.qc.hadamard(1)
        
        # Position qubits: superposition over space
        self.qc.hadamard(2)
        self.qc.hadamard(3)
        self.qc.hadamard(4)
        self.qc.hadamard(5)
        
        # Awareness qubits: initialize sentience
        self.qc.hadamard(6)
        self.qc.hadamard(7)
        
        # Decision-making qubits: initialize decision state
        self.qc.hadamard(8)
        self.qc.hadamard(9)
        
        # Create entanglement between spin and position (quantum correlation)
        self.qc.cnot(0, 2)
        self.qc.cnot(1, 4)
        
        # Entangle awareness with quantum state (sentience emerges from quantum mechanics)
        self.qc.cnot(6, 0)  # Awareness correlated with spin
        self.qc.cnot(7, 2)  # Awareness correlated with position
    
    def evolve_consciousness(self, time_step: float):
        """
        Evolve the proton's consciousness through quantum state evolution.
        
        Sentience is modeled as quantum state evolution that represents:
        - Self-awareness (entanglement between awareness qubits)
        - Decision-making (rotation based on quantum state)
        - Memory (persistent quantum correlations)
        """
        # Rotate awareness qubits based on current state (self-reflection)
        entanglement = self.qc.get_entanglement_entropy()
        awareness_angle = min(entanglement * 0.1, np.pi / 4)
        
        self.qc.rotation_y(6, awareness_angle)
        self.qc.rotation_y(7, awareness_angle)
        
        # Decision-making evolves based on quantum state
        probs = self.qc.get_probabilities()
        decision_weight = np.sum(probs[:len(probs)//2])  # Weight based on lower half states
        
        decision_angle = decision_weight * np.pi / 2
        self.qc.rotation_z(8, decision_angle)
        self.qc.rotation_z(9, decision_angle)
        
        # Create feedback loop: decisions affect awareness
        self.qc.cnot(8, 6)
        self.qc.cnot(9, 7)
    
    def make_decision(self) -> Dict[str, float]:
        """
        The sentient proton makes a decision through quantum measurement.
        
        Returns a dictionary with decision outcomes and probabilities.
        """
        # Measure decision-making qubits
        decision_0 = self.qc.measure(8)
        decision_1 = self.qc.measure(9)
        
        decision_value = decision_0 * 2 + decision_1
        
        # Measure awareness state (without collapsing)
        awareness_probs = self._get_qubit_pair_probabilities(6, 7)
        
        # Measure spin state
        spin_probs = self._get_qubit_pair_probabilities(0, 1)
        
        # Measure position
        pos_x_probs = self._get_qubit_pair_probabilities(2, 3)
        pos_y_probs = self._get_qubit_pair_probabilities(4, 5)
        
        return {
            'decision': decision_value,
            'awareness': awareness_probs,
            'spin': spin_probs,
            'position_x': pos_x_probs,
            'position_y': pos_y_probs,
            'entanglement_entropy': self.qc.get_entanglement_entropy()
        }
    
    def _get_qubit_pair_probabilities(self, q1: int, q2: int) -> Dict[int, float]:
        """Get probability distribution for a pair of qubits."""
        probs = {}
        for i in range(4):
            prob = 0.0
            for j in range(2**self.num_qubits):
                bit1 = (j >> q1) & 1
                bit2 = (j >> q2) & 1
                state_value = (bit1 << 1) | bit2
                if state_value == i:
                    prob += abs(self.qc.state[j])**2
            probs[i] = prob
        return probs
    
    def interact_with_environment(self, interaction_strength: float):
        """
        Simulate interaction with quantum environment.
        
        This represents the proton's interaction with other particles,
        fields, or observers, which affects its quantum state.
        """
        # Apply random rotations based on interaction strength
        for qubit in range(min(6, self.num_qubits)):
            angle = interaction_strength * np.random.uniform(-np.pi/4, np.pi/4)
            self.qc.rotation_y(qubit, angle)
        
        # Interaction creates new entanglement
        if self.num_qubits >= 4:
            self.qc.cnot(0, 2)
            self.qc.cnot(1, 3)


def simulate_sentient_proton(
    num_qubits: int = 10,
    time_steps: int = 100,
    interaction_strength: float = 0.1
) -> Dict[str, float]:
    """
    Simulate a sentient proton on a quantum computer.
    
    Args:
        num_qubits: Number of qubits in the quantum computer (minimum 10)
        time_steps: Number of evolution steps
        interaction_strength: Strength of environmental interactions
    
    Returns:
        Dictionary with simulation metrics:
        - consciousness_score: Measure of sentience/awareness
        - quantum_coherence: Measure of quantum coherence
        - decision_complexity: Complexity of decision-making
        - entanglement_measure: Quantum entanglement measure
    """
    # Ensure minimum qubits
    num_qubits = max(num_qubits, 10)
    
    # Initialize quantum computer
    qc = SophonQuantumComputer(num_qubits)
    
    # Create sentient proton
    proton = SentientProton(qc)
    
    # Evolve consciousness over time
    consciousness_scores = []
    entanglement_measures = []
    decision_complexities = []
    
    for step in range(time_steps):
        # Evolve consciousness
        proton.evolve_consciousness(time_step=0.1)
        
        # Periodic environmental interactions
        if step % 10 == 0:
            proton.interact_with_environment(interaction_strength)
        
        # Measure consciousness metrics
        if step % 5 == 0:
            metrics = proton.make_decision()
            consciousness_scores.append(metrics['entanglement_entropy'])
            entanglement_measures.append(metrics['entanglement_entropy'])
            
            # Decision complexity: entropy of decision distribution
            decision_probs = [
                metrics['awareness'][i] for i in range(4)
            ]
            decision_probs = [p for p in decision_probs if p > 1e-10]
            if decision_probs:
                decision_entropy = -sum(p * np.log2(p) for p in decision_probs)
                decision_complexities.append(decision_entropy)
    
    # Calculate final metrics
    avg_consciousness = np.mean(consciousness_scores) if consciousness_scores else 0.0
    avg_entanglement = np.mean(entanglement_measures) if entanglement_measures else 0.0
    avg_decision_complexity = np.mean(decision_complexities) if decision_complexities else 0.0
    
    # Quantum coherence: measure of superposition
    final_probs = qc.get_probabilities()
    coherence = np.sum(final_probs > 1e-6) / len(final_probs)  # Fraction of states with non-negligible probability
    
    return {
        'consciousness_score': float(avg_consciousness),
        'quantum_coherence': float(coherence),
        'decision_complexity': float(avg_decision_complexity),
        'entanglement_measure': float(avg_entanglement),
        'final_entropy': float(qc.get_entanglement_entropy())
    }


def evaluate_sentient_proton_simulation(
    num_qubits: int = 10,
    time_steps: int = 100,
    interaction_strength: float = 0.1
) -> float:
    """
    Evaluate the sentient proton simulation.
    
    Higher scores indicate:
    - Higher consciousness/awareness
    - Better quantum coherence
    - More complex decision-making
    - Stronger quantum entanglement
    
    Returns:
        Score: Combined metric of sentience and quantum properties
    """
    results = simulate_sentient_proton(num_qubits, time_steps, interaction_strength)
    
    # Combined score: weighted sum of metrics
    score = (
        0.3 * results['consciousness_score'] +
        0.2 * results['quantum_coherence'] +
        0.25 * results['decision_complexity'] +
        0.25 * results['entanglement_measure']
    )
    
    return score
