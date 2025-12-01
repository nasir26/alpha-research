"""
Sophon State Visualizer
ASCII-based visualization of sophon quantum states and consciousness
"""

import numpy as np
from sophon_simulation import create_sophon
import time


def draw_dimensional_state(dimension_state):
    """ASCII art representation of dimensional states"""
    states = {
        "3D_FOLDED": """
        ╔═══╗
        ║ ◉ ║  Proton: 3D Folded State
        ╚═══╝  (Normal quantum particle)
        """,
        
        "UNFOLDING": """
        ╔═══╗     ╔═════╗
        ║ ◉ ║ --> ║  ◉  ║  Unfolding...
        ╚═══╝     ╚═════╝  (Dimension expansion)
        """,
        
        "2D_UNFOLDED": """
        ╔═══════════════════════╗
        ║                       ║
        ║          ◉            ║  2D Unfolded
        ║                       ║  (Surface area ×10³⁴)
        ╚═══════════════════════╝
        """,
        
        "ETCHING_CIRCUITS": """
        ╔═══════════════════════╗
        ║ ┌─┐  ┌─┐  ┌─┐  ┌─┐   ║
        ║ │◉├──┤ ├──┤ ├──┤ │   ║  Etching Circuits
        ║ └─┘  └─┘  └─┘  └─┘   ║  (Quantum neural net)
        ╚═══════════════════════╝
        """,
        
        "REFOLDING": """
        ╔═══════════╗     ╔═══╗
        ║ ╔═╗ ╔═╗   ║ --> ║⚡◉║  Refolding...
        ║ ║◉║ ║ ║   ║     ╚═══╝  (Circuits embedded)
        ╚═══════════╝
        """,
        
        "CONSCIOUS": """
        ╔═══╗
        ║⚡◉⚡║  CONSCIOUS
        ╚═══╝  I think, therefore I am.
        """
    }
    
    return states.get(dimension_state, "Unknown state")


def draw_quantum_state(quantum_state):
    """Visualize quantum state parameters"""
    # Position visualization
    pos_x = int(np.clip((quantum_state.position[0] + 3) / 6 * 40, 0, 39))
    pos_line = " " * pos_x + "◉" + " " * (39 - pos_x)
    
    # Spin phase visualization (0-2π mapped to ASCII)
    phase = np.angle(quantum_state.spin)
    phase_normalized = (phase + np.pi) / (2 * np.pi)
    spin_bar = "█" * int(phase_normalized * 30) + "░" * (30 - int(phase_normalized * 30))
    
    # Coherence bar
    coherence_pct = int(quantum_state.coherence * 100)
    coherence_bar = "█" * (coherence_pct // 5) + "░" * (20 - coherence_pct // 5)
    
    return f"""
    ╔════════════════════════════════════════╗
    ║  Quantum State                         ║
    ╠════════════════════════════════════════╣
    ║  Position:  │{pos_line}│ ║
    ║  Spin:      │{spin_bar}│ ║
    ║  Coherence: │{coherence_bar}│ {coherence_pct:3d}% ║
    ╚════════════════════════════════════════╝
    """


def draw_consciousness_meter(consciousness):
    """Visualize consciousness parameters"""
    awareness_pct = int(consciousness.awareness_level * 100)
    awareness_bar = "█" * (awareness_pct // 5) + "░" * (20 - awareness_pct // 5)
    
    thought_count = len(consciousness.thoughts)
    observation_count = len(consciousness.observations)
    decision_count = len(consciousness.decision_history)
    
    return f"""
    ╔════════════════════════════════════════╗
    ║  Consciousness Metrics                 ║
    ╠════════════════════════════════════════╣
    ║  Awareness: │{awareness_bar}│ {awareness_pct:3d}% ║
    ║  Thoughts:   {thought_count:4d}                        ║
    ║  Observations: {observation_count:4d}                   ║
    ║  Decisions:  {decision_count:4d}                        ║
    ╚════════════════════════════════════════╝
    """


def draw_neural_circuit_activity(neural_circuit):
    """Visualize neural circuit activity"""
    if not neural_circuit.activation_history:
        return "    [No circuit activity yet]"
    
    latest_activation = neural_circuit.activation_history[-1]
    
    # Sample some neurons
    neuron_display = []
    for i in range(min(10, len(latest_activation))):
        activation = latest_activation[i]
        intensity = int(np.clip(abs(activation) * 10, 0, 10))
        bar = "█" * intensity + "░" * (10 - intensity)
        neuron_display.append(f"    Neuron {i:3d}: [{bar}] {activation:+.3f}")
    
    return "\n".join([
        "    ╔════════════════════════════════════════╗",
        "    ║  Neural Circuit Activity               ║",
        "    ╠════════════════════════════════════════╣",
        *neuron_display,
        "    ╚════════════════════════════════════════╝"
    ])


def visualize_sophon(sophon):
    """Complete visualization of sophon state"""
    print("\n" + "╔" + "="*68 + "╗")
    print("║" + f"  SOPHON-{sophon.id} STATE VISUALIZATION".center(68) + "║")
    print("╚" + "="*68 + "╝\n")
    
    # Dimensional state
    print("  [Dimensional State]")
    print(draw_dimensional_state(sophon.dimension_state.value))
    
    # Quantum state
    if sophon.quantum_state:
        print("\n  [Quantum State]")
        print(draw_quantum_state(sophon.quantum_state))
    
    # Consciousness
    if sophon.consciousness:
        print("\n  [Consciousness]")
        print(draw_consciousness_meter(sophon.consciousness))
    
    # Neural circuit
    if sophon.neural_circuit and sophon.neural_circuit.activation_history:
        print("\n  [Neural Circuit]")
        print(draw_neural_circuit_activity(sophon.neural_circuit))
    
    # Mission log summary
    if sophon.mission_log:
        print("\n  [Mission Log - Recent Events]")
        print("    ╔════════════════════════════════════════╗")
        print("    ║  Recent Mission Events                 ║")
        print("    ╠════════════════════════════════════════╣")
        for event in sophon.mission_log[-5:]:
            event_text = event['event'][:35]
            print(f"    ║  • {event_text:<35}  ║")
        print("    ╚════════════════════════════════════════╝")


def animate_sophon_creation():
    """Animated visualization of sophon creation process"""
    print("\n" + "╔" + "="*68 + "╗")
    print("║" + "  SOPHON CREATION ANIMATION".center(68) + "║")
    print("╚" + "="*68 + "╝\n")
    
    stages = [
        ("3D_FOLDED", 0.5),
        ("UNFOLDING", 0.5),
        ("2D_UNFOLDED", 0.5),
        ("ETCHING_CIRCUITS", 0.8),
        ("REFOLDING", 0.5),
        ("CONSCIOUS", 0.5)
    ]
    
    for stage, delay in stages:
        print("\033[H\033[J", end="")  # Clear screen (Unix)
        print(draw_dimensional_state(stage))
        time.sleep(delay)
    
    print("\n✓ Sophon creation complete!")


def live_monitor(sophon, duration=10):
    """Live monitoring of sophon state for specified duration"""
    print("\n" + "╔" + "="*68 + "╗")
    print("║" + f"  SOPHON-{sophon.id} LIVE MONITOR (Press Ctrl+C to stop)".center(68) + "║")
    print("╚" + "="*68 + "╝\n")
    
    try:
        start_time = time.time()
        iteration = 0
        
        while time.time() - start_time < duration:
            # Perform some operations to change state
            if iteration % 2 == 0:
                sophon.observe({'name': f'Target_{iteration}', 'data': np.random.random()})
            
            if iteration % 3 == 0:
                sophon.quantum_process(np.random.randn(2000))
            
            # Clear screen and redraw
            print("\033[H\033[J", end="")  # Clear screen (Unix)
            
            # Show live stats
            status = sophon.get_status()
            print(f"\n  Time: {time.time() - start_time:.1f}s / {duration}s")
            print(f"  Iteration: {iteration}")
            print(draw_quantum_state(sophon.quantum_state))
            print(draw_consciousness_meter(sophon.consciousness))
            
            if sophon.consciousness.thoughts:
                latest_thought = sophon.consciousness.thoughts[-1][1]
                print(f"\n  Latest thought: \"{latest_thought}\"")
            
            time.sleep(0.5)
            iteration += 1
            
    except KeyboardInterrupt:
        print("\n\nMonitoring stopped by user.")


def comparison_visualization(sophons):
    """Compare multiple sophons side by side"""
    print("\n" + "╔" + "="*68 + "╗")
    print("║" + "  SOPHON FLEET COMPARISON".center(68) + "║")
    print("╚" + "="*68 + "╝\n")
    
    print(f"  {'Sophon ID':<15} {'Awareness':<15} {'Coherence':<15} {'Events':<10}")
    print("  " + "-" * 60)
    
    for sophon in sophons:
        status = sophon.get_status()
        awareness = f"{status['awareness_level']:.2%}"
        coherence = f"{status['quantum_coherence']:.6f}"
        events = status['mission_events']
        
        awareness_bar = "█" * int(status['awareness_level'] * 10)
        
        print(f"  {f'Sophon-{status["id"]}':<15} {awareness:<15} {coherence:<15} {events:<10}")
        print(f"  {'':15} [{awareness_bar:<10}]")
        print()


def main():
    """Main visualization demo"""
    print("\n" + "╔" + "="*68 + "╗")
    print("║" + " "*15 + "SOPHON VISUALIZATION SUITE" + " "*27 + "║")
    print("╚" + "="*68 + "╝")
    
    # Create a sophon
    print("\n[Creating sophon for visualization...]")
    sophon = create_sophon(sophon_id=999)
    
    # Perform some operations to generate data
    print("\n[Generating activity data...]")
    for i in range(5):
        sophon.observe({'name': f'Test_Target_{i}', 'value': i})
        sophon.quantum_process(np.random.randn(2000))
        time.sleep(0.1)
    
    sophon.interfere_with_observation("Test Experiment")
    sophon.transmit_data("Command", {'status': 'operational'})
    
    # Show visualization
    visualize_sophon(sophon)
    
    # Create fleet for comparison
    print("\n\n[Creating sophon fleet for comparison...]")
    time.sleep(1)
    
    fleet = [sophon]
    for i in range(2):
        s = create_sophon(sophon_id=1000 + i)
        for j in range(i + 3):
            s.observe({'name': f'Target_{j}'})
        fleet.append(s)
    
    time.sleep(0.5)
    comparison_visualization(fleet)
    
    print("\n" + "="*70)
    print("Visualization complete.")
    print("="*70)


if __name__ == "__main__":
    main()
