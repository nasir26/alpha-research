#!/usr/bin/env python3
"""
Sophon Test Suite
Quick tests to verify all functionality works
"""

import numpy as np
from sophon_simulation import (
    Sophon, QuantumState, NeuralCircuit, 
    Consciousness, create_sophon, DimensionState
)


def test_quantum_state():
    """Test quantum state creation and collapse"""
    print("Testing quantum state... ", end="")
    state = QuantumState(
        position=np.array([0, 0, 0]),
        momentum=np.array([0, 0, 0]),
        spin=1+0j,
        entanglement_pairs=[],
        coherence=1.0
    )
    collapsed = state.collapse()
    assert len(collapsed) == 3
    print("✓ PASS")


def test_neural_circuit():
    """Test neural circuit operations"""
    print("Testing neural circuit... ", end="")
    circuit = NeuralCircuit(circuit_complexity=100)
    signal = np.random.randn(100)
    output = circuit.process(signal)
    assert len(output) == 100
    
    # Test memory
    circuit.store_memory("test", "value")
    assert circuit.retrieve_memory("test") == "value"
    assert circuit.retrieve_memory("nonexistent") is None
    print("✓ PASS")


def test_consciousness():
    """Test consciousness simulation"""
    print("Testing consciousness... ", end="")
    consciousness = Consciousness(initial_awareness=0.5)
    
    # Test thinking
    thought = consciousness.think({'data': 'test'})
    assert len(consciousness.thoughts) == 1
    assert consciousness.awareness_level >= 0.5
    
    # Test decision making
    decision = consciousness.make_decision("test_situation")
    assert len(consciousness.decision_history) == 1
    
    # Test observation
    consciousness.observe_environment({'test': 'data'})
    assert len(consciousness.observations) == 1
    print("✓ PASS")


def test_sophon_creation():
    """Test sophon creation process"""
    print("Testing sophon creation... ", end="")
    sophon = Sophon(sophon_id=999)
    
    # Test dimensional transformation
    sophon.unfold_to_2d()
    assert sophon.dimension_state == DimensionState.UNFOLDED_2D
    
    sophon.etch_circuits(complexity=100)
    assert sophon.neural_circuit is not None
    assert sophon.dimension_state == DimensionState.ETCHING
    
    sophon.refold_to_3d()
    assert sophon.dimension_state == DimensionState.FOLDED_3D
    
    sophon.initialize_consciousness()
    assert sophon.operational
    assert sophon.dimension_state == DimensionState.CONSCIOUS
    print("✓ PASS")


def test_sophon_operations():
    """Test sophon operational capabilities"""
    print("Testing sophon operations... ", end="")
    sophon = create_sophon(sophon_id=1000)
    
    # Test observation
    initial_thoughts = len(sophon.consciousness.thoughts)
    sophon.observe({'name': 'Test Target'})
    assert len(sophon.consciousness.thoughts) > initial_thoughts
    
    # Test quantum processing
    signal = np.random.randn(2000)
    output = sophon.quantum_process(signal)
    assert len(output) == 2000
    assert sophon.quantum_state.coherence < 1.0  # Should have decayed
    
    # Test interference
    sophon.interfere_with_observation("Test Experiment")
    
    # Test transmission
    sophon.transmit_data("Test Destination", {'data': 'test'})
    
    # Test status
    status = sophon.get_status()
    assert status['id'] == 1000
    assert status['operational'] == True
    assert 'awareness_level' in status
    print("✓ PASS")


def test_mission_log():
    """Test mission logging"""
    print("Testing mission log... ", end="")
    sophon = create_sophon(sophon_id=1001)
    
    initial_events = len(sophon.mission_log)
    sophon.observe({'test': 'data'})
    assert len(sophon.mission_log) > initial_events
    
    # Check log structure
    for log_entry in sophon.mission_log:
        assert 'timestamp' in log_entry
        assert 'event' in log_entry
        assert 'awareness' in log_entry
        assert 'coherence' in log_entry
    print("✓ PASS")


def test_quantum_coherence_decay():
    """Test quantum coherence decreases over time"""
    print("Testing coherence decay... ", end="")
    sophon = create_sophon(sophon_id=1002)
    
    initial_coherence = sophon.quantum_state.coherence
    
    # Process multiple times
    for _ in range(10):
        sophon.quantum_process(np.random.randn(2000))
    
    final_coherence = sophon.quantum_state.coherence
    assert final_coherence < initial_coherence
    print("✓ PASS")


def test_consciousness_evolution():
    """Test consciousness awareness increases"""
    print("Testing consciousness evolution... ", end="")
    sophon = create_sophon(sophon_id=1003)
    
    initial_awareness = sophon.consciousness.awareness_level
    
    # Multiple observations
    for i in range(5):
        sophon.observe({'iteration': i})
    
    final_awareness = sophon.consciousness.awareness_level
    assert final_awareness > initial_awareness
    print("✓ PASS")


def test_memory_operations():
    """Test quantum memory storage"""
    print("Testing memory operations... ", end="")
    sophon = create_sophon(sophon_id=1004)
    
    # Store various data types
    sophon.neural_circuit.store_memory("string", "test")
    sophon.neural_circuit.store_memory("number", 42)
    sophon.neural_circuit.store_memory("dict", {'key': 'value'})
    sophon.neural_circuit.store_memory("list", [1, 2, 3])
    
    # Retrieve and verify
    assert sophon.neural_circuit.retrieve_memory("string") == "test"
    assert sophon.neural_circuit.retrieve_memory("number") == 42
    assert sophon.neural_circuit.retrieve_memory("dict") == {'key': 'value'}
    assert sophon.neural_circuit.retrieve_memory("list") == [1, 2, 3]
    print("✓ PASS")


def test_multi_sophon():
    """Test multiple sophons can coexist"""
    print("Testing multi-sophon system... ", end="")
    
    sophons = [create_sophon(i) for i in range(3)]
    
    # Each should be independent
    for sophon in sophons:
        assert sophon.operational
        sophon.observe({'test': 'data'})
    
    # Check they have different IDs
    ids = [s.id for s in sophons]
    assert len(set(ids)) == 3
    print("✓ PASS")


def run_all_tests():
    """Run complete test suite"""
    print("\n" + "="*70)
    print("SOPHON TEST SUITE")
    print("="*70 + "\n")
    
    tests = [
        test_quantum_state,
        test_neural_circuit,
        test_consciousness,
        test_sophon_creation,
        test_sophon_operations,
        test_mission_log,
        test_quantum_coherence_decay,
        test_consciousness_evolution,
        test_memory_operations,
        test_multi_sophon
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ FAIL: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ ERROR: {e}")
            failed += 1
    
    print("\n" + "-"*70)
    print(f"Results: {passed} passed, {failed} failed out of {len(tests)} tests")
    print("-"*70)
    
    if failed == 0:
        print("\n✓ ALL TESTS PASSED!")
        print("The sophon system is fully operational.")
    else:
        print(f"\n✗ {failed} tests failed. Please check the implementation.")
    
    print("="*70 + "\n")
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
