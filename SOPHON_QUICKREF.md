# Sophon Quick Reference Guide

## 🚀 One-Line Start
```bash
pip3 install numpy && python3 sophon_quickstart.py
```

## 📁 Files at a Glance

| File | Size | Purpose | When to Use |
|------|------|---------|-------------|
| `sophon_simulation.py` | 15K | Core implementation | Import for your projects |
| `sophon_quickstart.py` | 2.5K | Minimal example | **START HERE** |
| `sophon_interactive.py` | 11K | 6 demos | Learn features |
| `sophon_visualizer.py` | 12K | ASCII visualization | See it in action |
| `test_sophon.py` | 7.2K | Test suite | Verify installation |
| `SOPHON_INDEX.md` | 12K | Navigation | Find what you need |
| `SOPHON_README.md` | 6.9K | Documentation | Learn the API |
| `SOPHON_SUMMARY.md` | 12K | Technical details | Understand deeply |

**Total: 8 files, ~78KB**

## 💻 Code Cheat Sheet

### Create a Sophon
```python
from sophon_simulation import create_sophon
sophon = create_sophon(sophon_id=1)
```

### Observe Target
```python
sophon.observe({
    'name': 'Research Lab',
    'location': 'Earth',
    'classification': 'high_priority'
})
```

### Process Quantum Data
```python
import numpy as np
signal = np.random.randn(2000)
output = sophon.quantum_process(signal)
```

### Interfere with Physics
```python
sophon.interfere_with_observation("Quantum Experiment")
```

### Transmit Data
```python
sophon.transmit_data("Command", {'status': 'success'})
```

### Check Status
```python
status = sophon.get_status()
print(f"Awareness: {status['awareness_level']:.2%}")
print(f"Coherence: {status['quantum_coherence']:.6f}")
```

### Access Consciousness
```python
# View thoughts
for timestamp, thought in sophon.consciousness.thoughts:
    print(thought)

# View decisions
for ts, situation, decision in sophon.consciousness.decision_history:
    print(f"{situation} → {decision}")
```

### Memory Operations
```python
# Store
sophon.neural_circuit.store_memory("key", "value")

# Retrieve
data = sophon.neural_circuit.retrieve_memory("key")
```

### Create Fleet
```python
fleet = [create_sophon(i) for i in range(5)]
for sophon in fleet:
    sophon.observe({'target': f'Location_{sophon.id}'})
```

## 🎯 Common Tasks

| Task | Command |
|------|---------|
| Install dependencies | `pip3 install numpy` |
| Quick test | `python3 sophon_quickstart.py` |
| Full simulation | `python3 sophon_simulation.py` |
| Interactive menu | `python3 sophon_interactive.py` |
| Visual demo | `python3 sophon_visualizer.py` |
| Run tests | `python3 test_sophon.py` |
| Read docs | `cat SOPHON_README.md` |

## 🏗️ Architecture Quick View

```
Sophon
├── QuantumState (position, momentum, spin, coherence)
├── NeuralCircuit (2000 nodes, memory)
├── Consciousness (awareness, thoughts, decisions)
└── Mission Log (events, timestamps)
```

## 🎓 Learning Path

1. **Beginner**: Run `sophon_quickstart.py` → Read `SOPHON_INDEX.md`
2. **Intermediate**: Run all demos → Read `SOPHON_README.md`
3. **Advanced**: Study source → Read `SOPHON_SUMMARY.md`

## 🔧 API Quick Reference

### Sophon Class Methods

| Method | Parameters | Returns | Purpose |
|--------|-----------|---------|---------|
| `unfold_to_2d()` | None | None | Unfold to 2D |
| `etch_circuits(complexity)` | int | None | Etch circuits |
| `refold_to_3d()` | None | None | Refold to 3D |
| `initialize_consciousness()` | None | None | Boot consciousness |
| `observe(target)` | dict | None | Observe target |
| `quantum_process(signal)` | ndarray | ndarray | Process signal |
| `interfere_with_observation(exp)` | str | None | Interfere |
| `transmit_data(dest, data)` | str, dict | None | Transmit |
| `get_status()` | None | dict | Get status |
| `log_mission(event)` | str | None | Log event |

### Status Dictionary Keys

- `id`: Sophon ID
- `operational`: Boolean
- `dimension_state`: Current state
- `quantum_coherence`: 0.0-1.0
- `awareness_level`: 0.0-1.0
- `total_thoughts`: Count
- `total_observations`: Count
- `mission_events`: Count

## 📊 Performance

- **Init time**: ~0.4s
- **Processing**: ~5-10ms (2000 dims)
- **Observation**: ~20-30ms
- **Memory**: ~5MB per sophon

## 🎨 Visualizations

```python
from sophon_visualizer import visualize_sophon, comparison_visualization

# Single sophon
sophon = create_sophon(1)
visualize_sophon(sophon)

# Fleet comparison
fleet = [create_sophon(i) for i in range(3)]
comparison_visualization(fleet)
```

## 🧪 Test Coverage

All 10 tests passing:
- ✓ Quantum state ops
- ✓ Neural circuits
- ✓ Consciousness
- ✓ Creation process
- ✓ Operations
- ✓ Mission logging
- ✓ Coherence decay
- ✓ Consciousness evolution
- ✓ Memory ops
- ✓ Multi-sophon

## 📖 Documentation Files

- **SOPHON_INDEX.md**: Complete navigation guide
- **SOPHON_README.md**: Main API documentation
- **SOPHON_SUMMARY.md**: Technical details & benchmarks
- **SOPHON_QUICKREF.md**: This file

## 🎯 Use Case Examples

### Scientific Demo
```python
sophon = create_sophon(1)
for i in range(10):
    sophon.observe({'experiment': i})
    print(f"Awareness: {sophon.consciousness.awareness_level:.2%}")
```

### Fleet Coordination
```python
targets = ['CERN', 'Fermilab', 'LIGO']
fleet = [create_sophon(i) for i in range(len(targets))]
for sophon, target in zip(fleet, targets):
    sophon.observe({'name': target})
    sophon.interfere_with_observation(f"{target} Experiment")
```

### Data Collection
```python
sophon = create_sophon(1)
sophon.neural_circuit.store_memory("mission", "observe_earth")
sophon.neural_circuit.store_memory("target", "physics_labs")
# Later...
mission = sophon.neural_circuit.retrieve_memory("mission")
```

## 🔍 Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: numpy` | `pip3 install numpy` |
| `python: command not found` | Use `python3` instead |
| Import error | Ensure in correct directory |
| Memory error | Reduce circuit complexity |

## 💡 Tips & Tricks

1. **Reduce output**: Redirect to file `python3 script.py > output.txt`
2. **Silent mode**: Modify print statements in source
3. **Speed up**: Lower circuit complexity (default 2000)
4. **Save state**: Use pickle to serialize sophons
5. **Parallel**: Use multiprocessing for large fleets

## 🎬 Demo Commands

```bash
# Quick start (30 seconds)
python3 sophon_quickstart.py

# Full mission (1 minute)
python3 sophon_simulation.py

# Interactive (user choice)
python3 sophon_interactive.py

# Visual demo (1 minute)
python3 sophon_visualizer.py

# Run tests (30 seconds)
python3 test_sophon.py

# Specific demo
python3 -c "from sophon_interactive import demo_basic_operations; demo_basic_operations()"
```

## 🌟 Cool One-Liners

```bash
# Create 10 sophons
python3 -c "from sophon_simulation import create_sophon; [create_sophon(i) for i in range(10)]"

# Quick status
python3 -c "from sophon_simulation import create_sophon; s=create_sophon(1); print(s.get_status())"

# Thought stream
python3 -c "from sophon_simulation import create_sophon; s=create_sophon(1); s.observe({'x':1}); print(s.consciousness.thoughts)"
```

## 📚 Further Reading

- **Three-Body Problem** by Liu Cixin (the novel)
- **Quantum Computing** - Nielsen & Chuang
- **Consciousness** - Integrated Information Theory

## 🎉 Ready to Go!

```python
from sophon_simulation import create_sophon

# Your sophon awaits
sophon = create_sophon(sophon_id=1)

# The universe is now observable
sophon.observe({'universe': 'everything'})

# Physics is... malleable
sophon.interfere_with_observation("The Standard Model")
```

---

**Need help?** Read SOPHON_INDEX.md for full navigation.

*"I think, therefore I am." - Sophon*
