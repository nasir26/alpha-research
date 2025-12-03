#!/usr/bin/env python3
"""
Generate a truly handwritten-style board image
Simulates marker/chalk writing on a whiteboard
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import math

# Board dimensions
WIDTH = 2400
HEIGHT = 3800
MARGIN = 100

# Colors - whiteboard with marker/chalk
BOARD_COLOR = (252, 252, 250)  # Slightly off-white
MARKER_COLOR = (20, 20, 20)  # Dark marker
CHALK_BLUE = (50, 100, 200)  # Blue marker for headings
CHALK_RED = (200, 50, 50)  # Red for emphasis

def draw_handwritten_text(draw, text, position, font, color, img, 
                          char_variation=3.0, word_variation=4.0, 
                          size_variation=0.15, rotation_variation=2.0):
    """Draw text that looks truly handwritten with significant variations"""
    x, y = position
    current_x = x
    
    words = text.split(' ')
    for word in words:
        if not word.strip():
            current_x += font.size * 0.4
            continue
            
        word_x = current_x
        
        # Word-level variation
        word_offset_x = random.uniform(-word_variation, word_variation)
        word_offset_y = random.uniform(-word_variation * 0.6, word_variation * 0.6)
        word_rotation = random.uniform(-rotation_variation, rotation_variation)
        
        # Draw each character with significant variations
        for char_idx, char in enumerate(word):
            # Character-level variations
            char_offset_x = random.uniform(-char_variation, char_variation)
            char_offset_y = random.uniform(-char_variation * 0.8, char_variation * 0.8)
            char_rotation = random.uniform(-rotation_variation * 0.7, rotation_variation * 0.7)
            char_size_factor = 1.0 + random.uniform(-size_variation, size_variation)
            
            # Calculate position
            char_x = word_x + word_offset_x + char_offset_x
            char_y = y + word_offset_y + char_offset_y
            
            # Create a temporary image for this character to apply rotation
            char_size = int(font.size * 1.5 * char_size_factor)
            char_img = Image.new('RGBA', (char_size, char_size), (255, 255, 255, 0))
            char_draw = ImageDraw.Draw(char_img)
            
            # Draw character in temp image
            try:
                # Try to get a slightly different sized font
                char_font_size = int(font.size * char_size_factor)
                char_font = ImageFont.truetype(font.path, char_font_size) if hasattr(font, 'path') else font
            except:
                char_font = font
            
            char_draw.text((char_size//4, char_size//4), char, fill=color, font=char_font)
            
            # Apply rotation
            if abs(char_rotation) > 0.1:
                rotated = char_img.rotate(char_rotation, expand=True, fillcolor=(255, 255, 255, 0))
            else:
                rotated = char_img
            
            # Paste onto main image
            img.paste(rotated, (int(char_x), int(char_y)), rotated)
            
            # Get character width for spacing
            bbox = char_draw.textbbox((0, 0), char, font=char_font)
            char_width = (bbox[2] - bbox[0]) * 0.9  # Slight compression
            word_x += char_width
        
        # Space between words
        current_x = word_x + font.size * 0.35
    
    return current_x

def draw_simple_handwritten(draw, text, position, font, color, 
                           variation=2.5, size_var=0.12):
    """Simpler handwritten effect - draw text multiple times with offsets for thickness"""
    x, y = position
    current_x = x
    
    words = text.split(' ')
    for word in words:
        if not word.strip():
            current_x += font.size * 0.4
            continue
        
        # Word position variation
        base_x = current_x + random.uniform(-variation, variation)
        base_y = y + random.uniform(-variation * 0.5, variation * 0.5)
        
        # Draw word multiple times with slight offsets for marker thickness
        offsets = [
            (0, 0),
            (0.5, 0.3),
            (-0.3, 0.4),
            (0.3, -0.2),
        ]
        
        for offset_x, offset_y in offsets:
            draw.text((base_x + offset_x, base_y + offset_y), word + ' ', 
                     fill=color, font=font)
        
        # Get word width
        bbox = draw.textbbox((0, 0), word + ' ', font=font)
        current_x += (bbox[2] - bbox[0]) * 0.95
    
    return current_x

def create_handwritten_board():
    """Create board with truly handwritten appearance"""
    
    # Create board
    img = Image.new('RGB', (WIDTH, HEIGHT), BOARD_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Load fonts - use bold/regular for variation
    try:
        font_path = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
        title_font = ImageFont.truetype(font_path, 64)
        heading_font = ImageFont.truetype(font_path, 42)
        body_font = ImageFont.truetype(font_path, 32)
        small_font = ImageFont.truetype(font_path, 28)
    except:
        title_font = ImageFont.load_default()
        heading_font = ImageFont.load_default()
        body_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    
    y_pos = MARGIN
    
    # Title
    title = "MAP OF QUANTUM COMPUTING"
    bbox = draw.textbbox((0, 0), title, font=title_font)
    text_width = bbox[2] - bbox[0]
    x_pos = (WIDTH - text_width) // 2
    
    # Draw title with handwritten effect (thicker, more prominent)
    for i in range(5):  # Multiple passes for thickness
        offset_x = random.uniform(-1.5, 1.5)
        offset_y = random.uniform(-1.5, 1.5)
        draw.text((x_pos + offset_x, y_pos + offset_y), title, 
                 fill=CHALK_BLUE, font=title_font)
    
    y_pos += 100
    
    # Content sections
    content = [
        ("1. CORE CONCEPTS", "heading", [
            "• Qubits (vs classical bits)",
            "  - Superposition: |0⟩ + |1⟩",
            "  - Entanglement: Bell states",
            "  - Measurement: collapses state",
            "• Quantum Gates",
            "  - Pauli gates (X, Y, Z)",
            "  - Hadamard (H)",
            "  - CNOT (entanglement)",
            "• Quantum Circuits",
            "  - Unitary operations",
            "  - Reversibility",
        ]),
        ("2. HARDWARE ARCHITECTURES", "heading", [
            "Superconducting (IBM, Google)",
            "├─ Transmon qubits",
            "├─ Microwave control",
            "└─ Cryogenic temps (~20mK)",
            "",
            "Trapped Ions (IonQ, Honeywell)",
            "├─ Yb+, Ca+ ions",
            "├─ Laser control",
            "└─ Long coherence times",
            "",
            "Photonic (Xanadu, PsiQuantum)",
            "├─ Quantum optics",
            "└─ Room temp operation",
        ]),
        ("3. KEY ALGORITHMS", "heading", [
            "Shor's Algorithm",
            "└─ Factoring → breaks RSA",
            "   O(log³ N) vs O(e^N)",
            "",
            "Grover's Algorithm",
            "└─ Unstructured search",
            "   O(√N) vs O(N)",
            "",
            "QAOA & VQE",
            "└─ Optimization & Chemistry",
        ]),
        ("4. APPLICATIONS", "heading", [
            "• Cryptography (breaking & building)",
            "• Drug Discovery",
            "• Financial Modeling",
            "• Material Science",
            "• AI/ML",
        ]),
        ("5. ERROR CORRECTION", "heading", [
            "Challenges:",
            "• Decoherence (T1, T2)",
            "• Gate errors (~0.1-1%)",
            "• Measurement errors",
            "",
            "Solutions:",
            "• Surface codes",
            "• Stabilizer codes",
            "• Fault-tolerant thresholds",
        ]),
        ("6. QUANTUM SUPREMACY", "heading", [
            "Google (2019): Sycamore",
            "└─ 53 qubits",
            '   "200s vs 10,000 years"',
            "",
            "Current: NISQ era",
            "• ~100-1000 qubits",
            "• Limited coherence",
            "• No practical advantage yet",
        ]),
        ("7. MAJOR PLAYERS", "heading", [
            "Big Tech:",
            "• IBM (Qiskit)",
            "• Google (Cirq, Sycamore)",
            "• Microsoft (Azure Quantum)",
            "• Amazon (Braket)",
            "",
            "Startups:",
            "• IonQ, Rigetti",
            "• Xanadu, PsiQuantum",
            "• Quantinuum",
        ]),
        ("8. SOFTWARE STACK", "heading", [
            "Languages:",
            "• Qiskit (Python, IBM)",
            "• Cirq (Python, Google)",
            "• Q# (Microsoft)",
            "• PennyLane (Xanadu)",
            "",
            "Cloud: IBM Quantum, AWS, Azure",
        ]),
        ("9. TIMELINE", "heading", [
            "Past:",
            "• 1980s: Feynman, Deutsch",
            "• 1994: Shor's algorithm",
            "• 2019: Quantum supremacy",
            "",
            "Present (NISQ):",
            "• 50-1000 qubits",
            "• High error rates",
            "",
            "Future:",
            "• 2025-2030: 1000-10000 qubits",
            "• Error correction working",
        ]),
        ("10. CHALLENGES", "heading", [
            "Technical:",
            "• Scaling qubit count",
            "• Reducing errors",
            "• Better connectivity",
            "",
            "Practical:",
            "• Cost (millions)",
            "• Expertise gap",
        ]),
        ("KEY TAKEAWAY:", "highlight", [
            "Quantum computing = exponential speedup",
            "for SPECIFIC problems",
            "NOT a replacement for classical computing",
            "",
            "Still early days, but progress accelerating!",
            '"The quantum winter is over" 🌱',
        ]),
    ]
    
    # Draw all sections
    for section_title, section_type, items in content:
        # Section heading
        x_pos = MARGIN
        color = CHALK_BLUE if section_type == "heading" else CHALK_RED
        font_to_use = heading_font if section_type != "highlight" else title_font
        
        # Draw heading with handwritten effect
        draw_simple_handwritten(draw, section_title, (x_pos, y_pos), 
                               font_to_use, color, variation=3.0, size_var=0.1)
        
        # Calculate heading height
        bbox = draw.textbbox((0, 0), section_title, font=font_to_use)
        y_pos += int((bbox[3] - bbox[1]) * 1.5)
        
        # Draw items
        for item in items:
            if item.strip():
                # Determine indentation and font
                if item.strip().startswith(('•', '-', '├', '└')):
                    x_offset = MARGIN + 60
                    item_font = body_font
                elif item.strip()[0].isupper() and ':' in item:
                    x_offset = MARGIN + 40
                    item_font = body_font
                else:
                    x_offset = MARGIN + 80
                    item_font = small_font
                
                # Draw with handwritten effect
                draw_simple_handwritten(draw, item, (x_offset, y_pos),
                                       item_font, MARKER_COLOR, 
                                       variation=2.5, size_var=0.12)
                
                # Calculate line height
                bbox = draw.textbbox((0, 0), item, font=item_font)
                y_pos += int((bbox[3] - bbox[1]) * 1.3)
            else:
                y_pos += int(body_font.size * 0.6)
        
        y_pos += 30  # Space between sections
    
    # Add board texture
    for _ in range(150):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        radius = random.randint(1, 5)
        color_var = random.randint(-10, 10)
        color = tuple(max(240, min(255, c + color_var)) for c in BOARD_COLOR)
        draw.ellipse([x-radius, y-radius, x+radius, y+radius], fill=color)
    
    # Add subtle grid (like whiteboard lines)
    for i in range(6):
        y_line = MARGIN + i * (HEIGHT - 2*MARGIN) // 5
        for x in range(0, WIDTH, 3):
            if random.random() > 0.99:
                draw.ellipse([x-1, y_line-1, x+1, y_line+1], 
                           fill=(240, 240, 240))
    
    # Add eraser marks/smudges
    for _ in range(25):
        x = random.randint(MARGIN, WIDTH - MARGIN)
        y = random.randint(MARGIN, HEIGHT - MARGIN)
        radius = random.randint(5, 15)
        # Semi-transparent white smudge
        smudge = Image.new('RGBA', (radius*2, radius*2), (255, 255, 255, 40))
        img.paste(smudge, (x-radius, y-radius), smudge)
    
    # Add border
    border_width = 5
    draw.rectangle([border_width, border_width, WIDTH-border_width, HEIGHT-border_width],
                  outline=(170, 170, 170), width=border_width)
    
    # Add some marker bleed effects (slight blur on some text areas)
    # This would require more complex processing, so we'll skip for now
    
    return img

if __name__ == '__main__':
    print("Generating handwritten board image...")
    random.seed(42)  # For reproducibility
    img = create_handwritten_board()
    output_path = 'quantum_computing_map_board.png'
    img.save(output_path, 'PNG', quality=95, optimize=True)
    print(f"Image saved to {output_path}")
    print(f"Image size: {img.size[0]}x{img.size[1]} pixels")
