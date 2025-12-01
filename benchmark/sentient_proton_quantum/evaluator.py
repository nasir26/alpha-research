"""
Evaluator for Sentient Proton Quantum Simulation

This evaluator tests the quantum simulation of a sentient proton,
measuring consciousness, quantum coherence, and decision-making capabilities.
"""

import numpy as np
import importlib.util
import sys


def verify_quantum_simulation(results: dict) -> bool:
    """
    Verify that the quantum simulation results are valid.
    
    Args:
        results: Dictionary with simulation metrics
    
    Returns:
        bool: True if results are valid, False otherwise
    """
    required_keys = [
        'consciousness_score',
        'quantum_coherence',
        'decision_complexity',
        'entanglement_measure'
    ]
    
    # Check all required keys are present
    if not all(key in results for key in required_keys):
        return False
    
    # Check values are valid numbers
    for key in required_keys:
        value = results[key]
        if not isinstance(value, (int, float)):
            return False
        if np.isnan(value) or np.isinf(value):
            return False
        if value < 0:  # Some metrics should be non-negative
            return False
    
    # Check quantum coherence is in valid range [0, 1]
    if not (0 <= results['quantum_coherence'] <= 1):
        return False
    
    return True


def evaluate(program_path: str = "results/initial_program.py"):
    """
    Evaluate the sentient proton quantum simulation from the given program file.
    
    Args:
        program_path: Path to the Python program file
    
    Returns:
        dict: Evaluation results with score and metrics
    """
    import importlib.util
    import sys
    
    # Load the module from the given path
    spec = importlib.util.spec_from_file_location("program", program_path)
    program = importlib.util.module_from_spec(spec)
    sys.modules["program"] = program
    spec.loader.exec_module(program)
    
    # Test the simulation function
    try:
        # Test with different configurations
        results_10 = program.simulate_sentient_proton(
            num_qubits=10,
            time_steps=50,
            interaction_strength=0.1
        )
        
        results_12 = program.simulate_sentient_proton(
            num_qubits=12,
            time_steps=100,
            interaction_strength=0.15
        )
        
        results_14 = program.simulate_sentient_proton(
            num_qubits=14,
            time_steps=150,
            interaction_strength=0.2
        )
        
    except Exception as e:
        return {"error": str(e), "score": -10.0}
    
    # Validate results
    valid_10 = verify_quantum_simulation(results_10)
    valid_12 = verify_quantum_simulation(results_12)
    valid_14 = verify_quantum_simulation(results_14)
    
    if not all([valid_10, valid_12, valid_14]):
        return {"error": "Invalid simulation results", "score": -1.0}
    
    # Calculate scores for each configuration
    score_10 = program.evaluate_sentient_proton_simulation(
        num_qubits=10,
        time_steps=50,
        interaction_strength=0.1
    )
    
    score_12 = program.evaluate_sentient_proton_simulation(
        num_qubits=12,
        time_steps=100,
        interaction_strength=0.15
    )
    
    score_14 = program.evaluate_sentient_proton_simulation(
        num_qubits=14,
        time_steps=150,
        interaction_strength=0.2
    )
    
    # Combined score: weighted average
    total_score = score_10 + score_12 + score_14
    
    return {
        "score": float(total_score),
        "result_10_qubits": float(score_10),
        "result_12_qubits": float(score_12),
        "result_14_qubits": float(score_14),
        "metrics_10": results_10,
        "metrics_12": results_12,
        "metrics_14": results_14
    }


if __name__ == "__main__":
    # Test evaluation
    result = evaluate("/workspace/benchmark/sentient_proton_quantum/initial_program.py")
    print(result)
