#!/usr/bin/env python3
"""
Sophon Quick Start Example
A minimal example showing how to create and use a sophon
"""

from sophon_simulation import create_sophon
import numpy as np

def main():
    print("\n" + "="*70)
    print("SOPHON QUICK START - Minimal Example")
    print("="*70 + "\n")
    
    # Step 1: Create a sophon
    print("Step 1: Creating sophon...")
    sophon = create_sophon(sophon_id=1)
    
    # Step 2: Observe something
    print("\nStep 2: Observing a target...")
    sophon.observe({
        'name': 'Quantum Research Laboratory',
        'location': 'Earth',
        'classification': 'high_priority'
    })
    
    # Step 3: Process quantum data
    print("\nStep 3: Processing quantum data...")
    quantum_signal = np.random.randn(2000)
    result = sophon.quantum_process(quantum_signal)
    print(f"  Processed {len(quantum_signal)} dimensional signal")
    print(f"  Output energy: {np.linalg.norm(result):.4f}")
    
    # Step 4: Interfere with experiment
    print("\nStep 4: Interfering with physics experiment...")
    sophon.interfere_with_observation("Quantum Entanglement Measurement")
    
    # Step 5: Transmit findings
    print("\nStep 5: Transmitting data via quantum entanglement...")
    sophon.transmit_data("Trisolaris Fleet", {
        'mission_status': 'successful',
        'target_analyzed': True,
        'interference_complete': True
    })
    
    # Step 6: Check status
    print("\nStep 6: Final sophon status:")
    status = sophon.get_status()
    print(f"  ID: {status['id']}")
    print(f"  Operational: {status['operational']}")
    print(f"  State: {status['dimension_state']}")
    print(f"  Awareness: {status['awareness_level']:.2%}")
    print(f"  Quantum Coherence: {status['quantum_coherence']:.6f}")
    print(f"  Total Thoughts: {status['total_thoughts']}")
    print(f"  Mission Events: {status['mission_events']}")
    
    # Show latest thoughts
    print("\n  Recent thoughts:")
    for timestamp, thought in sophon.consciousness.thoughts[-3:]:
        print(f"    • {thought}")
    
    print("\n" + "="*70)
    print("✓ Quick start complete! Sophon is operational.")
    print("="*70 + "\n")
    
    return sophon


if __name__ == "__main__":
    sophon = main()
    
    print("You can now interact with the sophon:")
    print("  sophon.observe({'name': 'New Target'})")
    print("  sophon.quantum_process(numpy.random.randn(2000))")
    print("  sophon.get_status()")
