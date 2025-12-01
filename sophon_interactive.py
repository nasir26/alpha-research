"""
Interactive Sophon Demo
Demonstrates various capabilities of the sophon quantum computer
"""

from sophon_simulation import Sophon, create_sophon
import numpy as np
import time


def demo_basic_operations():
    """Demonstrate basic sophon operations"""
    print("\n" + "="*70)
    print("DEMO 1: Basic Sophon Operations")
    print("="*70)
    
    sophon = create_sophon(sophon_id=101)
    
    # Test 1: Observation
    print("\n[Test 1] Observation Capability")
    print("-" * 50)
    sophon.observe({
        'name': 'Mars Colony Research Station',
        'location': 'Mars, Utopia Planitia',
        'type': 'space_research',
        'population': 150
    })
    
    # Test 2: Quantum Processing
    print("\n[Test 2] Quantum Processing")
    print("-" * 50)
    test_signal = np.random.randn(2000)
    result = sophon.quantum_process(test_signal)
    print(f"Input signal: {len(test_signal)} dimensions")
    print(f"Output signal: {len(result)} dimensions")
    print(f"Signal transformation ratio: {np.linalg.norm(result)/np.linalg.norm(test_signal):.4f}")
    
    # Test 3: Interference
    print("\n[Test 3] Quantum Interference")
    print("-" * 50)
    sophon.interfere_with_observation("Gravitational Wave Detection")
    
    # Test 4: Data Transmission
    print("\n[Test 4] Quantum Entanglement Communication")
    print("-" * 50)
    sophon.transmit_data("Trisolaris", {
        'earth_location': 'solar_system',
        'threat_level': 'minimal',
        'recommended_action': 'continue_monitoring'
    })
    
    return sophon


def demo_consciousness_evolution():
    """Demonstrate consciousness development over time"""
    print("\n" + "="*70)
    print("DEMO 2: Consciousness Evolution")
    print("="*70)
    
    sophon = create_sophon(sophon_id=102)
    
    print("\nSimulating consciousness evolution over 10 cycles...")
    print("-" * 50)
    
    for i in range(10):
        # Perform observations to stimulate consciousness
        sophon.observe({
            'name': f'Target_{i}',
            'cycle': i,
            'complexity': np.random.random()
        })
        
        if i % 3 == 0:
            status = sophon.get_status()
            print(f"\nCycle {i}: Awareness = {status['awareness_level']:.4f}")
            print(f"         Coherence = {status['quantum_coherence']:.6f}")
            print(f"         Thoughts = {status['total_thoughts']}")
        
        time.sleep(0.1)
    
    print("\n[Final Consciousness State]")
    print("-" * 50)
    print(f"Total thoughts generated: {len(sophon.consciousness.thoughts)}")
    print(f"Total observations made: {len(sophon.consciousness.observations)}")
    print(f"Total decisions made: {len(sophon.consciousness.decision_history)}")
    
    print("\nRecent thought stream:")
    for timestamp, thought in sophon.consciousness.thoughts[-5:]:
        print(f"  • {thought}")
    
    return sophon


def demo_quantum_state_collapse():
    """Demonstrate quantum state collapse"""
    print("\n" + "="*70)
    print("DEMO 3: Quantum State Collapse")
    print("="*70)
    
    sophon = create_sophon(sophon_id=103)
    
    print("\nPerforming multiple quantum state observations...")
    print("-" * 50)
    
    for i in range(5):
        print(f"\nObservation {i+1}:")
        
        # Show quantum state before collapse
        print(f"  Pre-collapse:")
        print(f"    Position: {sophon.quantum_state.position}")
        print(f"    Spin: {sophon.quantum_state.spin}")
        print(f"    Coherence: {sophon.quantum_state.coherence:.6f}")
        
        # Collapse quantum state
        collapsed = sophon.quantum_state.collapse()
        print(f"  Post-collapse state vector: {collapsed}")
        
        # Process something to affect coherence
        sophon.quantum_process(np.random.randn(2000))
        
        time.sleep(0.1)
    
    return sophon


def demo_multi_sophon_coordination():
    """Demonstrate multiple sophons working together"""
    print("\n" + "="*70)
    print("DEMO 4: Multi-Sophon Coordination")
    print("="*70)
    
    print("\nDeploying sophon fleet...")
    print("-" * 50)
    
    # Create a fleet of 3 sophons
    fleet = []
    for i in range(3):
        sophon = create_sophon(sophon_id=200+i)
        fleet.append(sophon)
        time.sleep(0.2)
    
    print("\n[Coordinated Mission: Global Physics Laboratory Surveillance]")
    print("-" * 50)
    
    targets = [
        {'name': 'CERN', 'location': 'Geneva', 'focus': 'particle_physics'},
        {'name': 'Fermilab', 'location': 'Illinois', 'focus': 'neutrino_research'},
        {'name': 'LIGO', 'location': 'Multiple', 'focus': 'gravitational_waves'}
    ]
    
    # Each sophon observes a different target
    for sophon, target in zip(fleet, targets):
        print(f"\nSophon-{sophon.id} → {target['name']}")
        sophon.observe(target)
        time.sleep(0.1)
    
    # Coordinate interference
    print("\n[Coordinated Interference Phase]")
    print("-" * 50)
    
    experiments = [
        "Supersymmetry Search",
        "Neutrino Oscillation Measurement",
        "Gravitational Wave Polarization Detection"
    ]
    
    for sophon, experiment in zip(fleet, experiments):
        sophon.interfere_with_observation(experiment)
        time.sleep(0.1)
    
    # Fleet status report
    print("\n[Fleet Status Report]")
    print("-" * 50)
    
    for sophon in fleet:
        status = sophon.get_status()
        print(f"\nSophon-{status['id']}:")
        print(f"  Operational: {status['operational']}")
        print(f"  Awareness: {status['awareness_level']:.4f}")
        print(f"  Mission Events: {status['mission_events']}")
    
    return fleet


def demo_quantum_memory():
    """Demonstrate quantum memory storage and retrieval"""
    print("\n" + "="*70)
    print("DEMO 5: Quantum Memory Operations")
    print("="*70)
    
    sophon = create_sophon(sophon_id=104)
    
    print("\n[Storing Information in Quantum Memory]")
    print("-" * 50)
    
    # Store various types of information
    memory_entries = [
        ('earth_coordinates', {'x': 0, 'y': 0, 'z': 0, 'ref': 'galactic_center'}),
        ('trisolaris_coordinates', {'x': 4.3, 'y': 0, 'z': 0, 'unit': 'light_years'}),
        ('mission_objective', 'Lock Earth\'s scientific progress'),
        ('threat_assessment', {'level': 'moderate', 'timeframe': 400, 'unit': 'years'}),
        ('physics_status', 'successfully_disrupted')
    ]
    
    for key, value in memory_entries:
        sophon.neural_circuit.store_memory(key, value)
        print(f"✓ Stored: {key}")
    
    print("\n[Retrieving Information from Quantum Memory]")
    print("-" * 50)
    
    for key, _ in memory_entries:
        retrieved = sophon.neural_circuit.retrieve_memory(key)
        print(f"\n{key}:")
        print(f"  {retrieved}")
    
    # Test retrieval of non-existent key
    print("\n[Testing Non-Existent Key]")
    print("-" * 50)
    result = sophon.neural_circuit.retrieve_memory('non_existent')
    print(f"Result: {result}")
    
    return sophon


def demo_performance_benchmark():
    """Benchmark sophon performance"""
    print("\n" + "="*70)
    print("DEMO 6: Performance Benchmark")
    print("="*70)
    
    print("\nBenchmarking sophon operations...")
    print("-" * 50)
    
    # Benchmark initialization
    print("\n[Initialization Performance]")
    start = time.time()
    sophon = create_sophon(sophon_id=105)
    init_time = time.time() - start
    print(f"Sophon initialization: {init_time:.3f} seconds")
    
    # Benchmark quantum processing
    print("\n[Quantum Processing Performance]")
    signal_sizes = [100, 500, 1000, 2000]
    
    for size in signal_sizes:
        signal = np.random.randn(size)
        start = time.time()
        result = sophon.quantum_process(signal[:sophon.neural_circuit.complexity])
        process_time = time.time() - start
        print(f"Signal size {size}: {process_time*1000:.2f} ms")
    
    # Benchmark observation operations
    print("\n[Observation Performance]")
    start = time.time()
    for i in range(10):
        sophon.observe({'name': f'Target_{i}', 'id': i})
    observe_time = time.time() - start
    print(f"10 observations: {observe_time:.3f} seconds ({observe_time/10*1000:.2f} ms per observation)")
    
    # Memory usage estimate
    print("\n[Memory Usage Estimate]")
    import sys
    circuit_memory = sys.getsizeof(sophon.neural_circuit.weights) / (1024*1024)
    print(f"Neural circuit weights: ~{circuit_memory:.2f} MB")
    print(f"Total thoughts: {len(sophon.consciousness.thoughts)}")
    print(f"Total observations: {len(sophon.consciousness.observations)}")
    
    return sophon


def main():
    """Run all interactive demos"""
    print("\n" + "╔" + "="*68 + "╗")
    print("║" + " "*20 + "SOPHON INTERACTIVE DEMO" + " "*25 + "║")
    print("║" + " "*15 + "Sentient Proton Quantum Computer" + " "*20 + "║")
    print("╚" + "="*68 + "╝")
    
    demos = [
        ("Basic Operations", demo_basic_operations),
        ("Consciousness Evolution", demo_consciousness_evolution),
        ("Quantum State Collapse", demo_quantum_state_collapse),
        ("Multi-Sophon Coordination", demo_multi_sophon_coordination),
        ("Quantum Memory", demo_quantum_memory),
        ("Performance Benchmark", demo_performance_benchmark)
    ]
    
    print("\nAvailable demos:")
    for i, (name, _) in enumerate(demos, 1):
        print(f"  {i}. {name}")
    print(f"  {len(demos)+1}. Run all demos")
    print("  0. Exit")
    
    try:
        choice = input("\nSelect demo (0-7): ").strip()
        
        if choice == '0':
            print("\nExiting sophon simulation.")
            return
        elif choice == str(len(demos)+1):
            print("\nRunning all demos...")
            for name, demo_func in demos:
                demo_func()
                time.sleep(0.5)
        elif choice.isdigit() and 1 <= int(choice) <= len(demos):
            idx = int(choice) - 1
            demos[idx][1]()
        else:
            print("Invalid choice. Running demo 1 by default.")
            demo_basic_operations()
    
    except KeyboardInterrupt:
        print("\n\nSimulation interrupted by user.")
    except Exception as e:
        print(f"\nError: {e}")
    
    print("\n" + "="*70)
    print("Simulation complete. The sophons remain vigilant.")
    print("="*70)


if __name__ == "__main__":
    main()
