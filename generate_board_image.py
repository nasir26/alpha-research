#!/usr/bin/env python3
"""
Generate a handwritten-style board image of the quantum computing map
"""

from PIL import Image, ImageDraw, ImageFont
import random
import math

# Board dimensions
WIDTH = 2400
HEIGHT = 3200
MARGIN = 80

# Colors
BOARD_COLOR = (248, 248, 245)  # Off-white whiteboard
TEXT_COLOR = (30, 30, 30)  # Dark gray/black
ACCENT_COLOR = (50, 100, 200)  # Blue for headings

def add_handwritten_effect(draw, text, position, font, color, max_offset=2):
    """Add slight randomness to simulate handwritten text"""
    x, y = position
    words = text.split(' ')
    current_x = x
    
    for word in words:
        # Add small random offset to each word
        offset_x = random.uniform(-max_offset, max_offset)
        offset_y = random.uniform(-max_offset, max_offset)
        
        word_with_space = word + ' '
        draw.text((current_x + offset_x, y + offset_y), word_with_space, 
                 fill=color, font=font)
        
        # Get text width
        bbox = draw.textbbox((0, 0), word_with_space, font=font)
        current_x += (bbox[2] - bbox[0])
    
    return current_x

def draw_text_multiline(draw, text, position, font, color, line_spacing=1.2, max_width=None):
    """Draw multiline text with handwritten effect"""
    x, y = position
    lines = text.split('\n')
    current_y = y
    
    for line in lines:
        if line.strip():
            # Add slight rotation and offset for handwritten feel
            offset_x = random.uniform(-1, 1)
            offset_y = random.uniform(-1, 1)
            add_handwritten_effect(draw, line, (x + offset_x, current_y + offset_y), 
                                 font, color, max_offset=1.5)
        current_y += int(font.size * line_spacing)
    
    return current_y

def create_board_image():
    """Create the board image with handwritten-style text"""
    
    # Create board background
    img = Image.new('RGB', (WIDTH, HEIGHT), BOARD_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Try to load a handwritten font, fallback to default
    try:
        # Try common handwritten fonts
        font_paths = [
            '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
            '/System/Library/Fonts/Helvetica.ttc',
            'arial.ttf',
        ]
        title_font = None
        body_font = None
        
        for path in font_paths:
            try:
                title_font = ImageFont.truetype(path, 48)
                body_font = ImageFont.truetype(path, 28)
                break
            except:
                continue
        
        if title_font is None:
            title_font = ImageFont.load_default()
            body_font = ImageFont.load_default()
    except:
        title_font = ImageFont.load_default()
        body_font = ImageFont.load_default()
    
    # Content sections
    content = """
MAP OF QUANTUM COMPUTING

1. CORE CONCEPTS
   • Qubits (vs classical bits)
     - Superposition: |0⟩ + |1⟩
     - Entanglement: Bell states
     - Measurement: collapses state
   • Quantum Gates
     - Pauli gates (X, Y, Z)
     - Hadamard (H)
     - CNOT (entanglement)
   • Quantum Circuits
     - Unitary operations
     - Reversibility

2. HARDWARE ARCHITECTURES
   Superconducting (IBM, Google)
   ├─ Transmon qubits
   ├─ Microwave control
   └─ Cryogenic temps (~20mK)
   
   Trapped Ions (IonQ, Honeywell)
   ├─ Yb+, Ca+ ions
   ├─ Laser control
   └─ Long coherence times
   
   Photonic (Xanadu, PsiQuantum)
   ├─ Quantum optics
   └─ Room temp operation

3. KEY ALGORITHMS
   Shor's Algorithm
   └─ Factoring → breaks RSA
      O(log³ N) vs O(e^N)
   
   Grover's Algorithm
   └─ Unstructured search
      O(√N) vs O(N)
   
   QAOA & VQE
   └─ Optimization & Chemistry

4. APPLICATIONS
   • Cryptography (breaking & building)
   • Drug Discovery
   • Financial Modeling
   • Material Science
   • AI/ML

5. ERROR CORRECTION
   Challenges:
   • Decoherence (T1, T2)
   • Gate errors (~0.1-1%)
   • Measurement errors
   
   Solutions:
   • Surface codes
   • Stabilizer codes
   • Fault-tolerant thresholds

6. QUANTUM SUPREMACY
   Google (2019): Sycamore
   └─ 53 qubits
      "200s vs 10,000 years"
   
   Current: NISQ era
   • ~100-1000 qubits
   • Limited coherence
   • No practical advantage yet

7. MAJOR PLAYERS
   Big Tech:
   • IBM (Qiskit)
   • Google (Cirq, Sycamore)
   • Microsoft (Azure Quantum)
   • Amazon (Braket)
   
   Startups:
   • IonQ, Rigetti
   • Xanadu, PsiQuantum
   • Quantinuum

8. SOFTWARE STACK
   Languages:
   • Qiskit (Python, IBM)
   • Cirq (Python, Google)
   • Q# (Microsoft)
   • PennyLane (Xanadu)
   
   Cloud: IBM Quantum, AWS, Azure

9. TIMELINE
   Past:
   • 1980s: Feynman, Deutsch
   • 1994: Shor's algorithm
   • 2019: Quantum supremacy
   
   Present (NISQ):
   • 50-1000 qubits
   • High error rates
   
   Future:
   • 2025-2030: 1000-10000 qubits
   • Error correction working

10. CHALLENGES
    Technical:
    • Scaling qubit count
    • Reducing errors
    • Better connectivity
    
    Practical:
    • Cost (millions)
    • Expertise gap

KEY TAKEAWAY:
Quantum computing = exponential speedup
for SPECIFIC problems
NOT a replacement for classical computing

Still early days, but progress accelerating!
"The quantum winter is over" 🌱
"""
    
    # Draw title
    y_pos = MARGIN
    title_lines = ["MAP OF QUANTUM COMPUTING", ""]
    for line in title_lines:
        if line:
            bbox = draw.textbbox((0, 0), line, font=title_font)
            text_width = bbox[2] - bbox[0]
            x_pos = (WIDTH - text_width) // 2 + random.uniform(-3, 3)
            draw.text((x_pos, y_pos), line, fill=ACCENT_COLOR, font=title_font)
        y_pos += int(title_font.size * 1.5)
    
    y_pos += 20
    
    # Draw content sections
    sections = content.split('\n\n')
    for section in sections:
        if section.strip():
            # Draw section with slight variations
            lines = section.strip().split('\n')
            for line in lines:
                if line.strip():
                    # Indent based on line content
                    if line.strip().startswith(('•', '-', '├', '└')):
                        x_offset = MARGIN + 40
                    elif line.strip()[0].isdigit() and '.' in line[:3]:
                        x_offset = MARGIN
                        # Make section headers slightly larger and colored
                        font_to_use = title_font if len(line) < 30 else body_font
                        color_to_use = ACCENT_COLOR if len(line) < 30 else TEXT_COLOR
                    else:
                        x_offset = MARGIN + 20
                        font_to_use = body_font
                        color_to_use = TEXT_COLOR
                    
                    # Add handwritten effect
                    offset_x = random.uniform(-1.5, 1.5)
                    offset_y = random.uniform(-1.5, 1.5)
                    
                    draw.text((x_offset + offset_x, y_pos + offset_y), 
                            line, fill=color_to_use, font=font_to_use)
                    
                    # Calculate next line position
                    bbox = draw.textbbox((0, 0), line, font=body_font)
                    y_pos += int((bbox[3] - bbox[1]) * 1.2)
            
            y_pos += 15  # Space between sections
    
    # Add some board texture/imperfections
    for _ in range(50):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        radius = random.randint(1, 3)
        color = tuple(min(255, c + random.randint(-5, 5)) for c in BOARD_COLOR)
        draw.ellipse([x-radius, y-radius, x+radius, y+radius], fill=color)
    
    # Add a subtle border/frame effect
    border_width = 3
    draw.rectangle([border_width, border_width, WIDTH-border_width, HEIGHT-border_width], 
                  outline=(200, 200, 200), width=border_width)
    
    return img

if __name__ == '__main__':
    print("Generating board image...")
    img = create_board_image()
    output_path = 'quantum_computing_map_board.png'
    img.save(output_path, 'PNG', quality=95)
    print(f"Image saved to {output_path}")
