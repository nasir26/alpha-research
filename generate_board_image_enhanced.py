#!/usr/bin/env python3
"""
Generate a handwritten-style board image of the quantum computing map
Enhanced version with better handwritten effects
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import math

# Board dimensions
WIDTH = 2400
HEIGHT = 3600
MARGIN = 100

# Colors
BOARD_COLOR = (250, 250, 248)  # Off-white whiteboard
TEXT_COLOR = (25, 25, 25)  # Dark gray/black
ACCENT_COLOR = (40, 90, 180)  # Blue for headings
BULLET_COLOR = (60, 60, 60)

def draw_text_with_handwritten_effect(draw, text, position, font, color, 
                                     char_offset=1.5, word_offset=2.0):
    """Draw text with character-level handwritten variations"""
    x, y = position
    current_x = x
    
    words = text.split(' ')
    for word_idx, word in enumerate(words):
        word_x = current_x
        
        # Add word-level offset
        word_offset_x = random.uniform(-word_offset, word_offset)
        word_offset_y = random.uniform(-word_offset * 0.5, word_offset * 0.5)
        
        # Draw each character with slight variations
        for char in word:
            # Character-level offset
            char_offset_x = random.uniform(-char_offset, char_offset)
            char_offset_y = random.uniform(-char_offset * 0.7, char_offset * 0.7)
            
            # Draw character with offset
            char_x = word_x + word_offset_x + char_offset_x
            char_y = y + word_offset_y + char_offset_y
            
            draw.text((char_x, char_y), char, fill=color, font=font)
            
            # Get character width
            bbox = draw.textbbox((0, 0), char, font=font)
            word_x += (bbox[2] - bbox[0]) * 0.95  # Slight compression
            
        # Add space
        word_x += font.size * 0.3
        current_x = word_x
    
    return current_x

def create_board_image():
    """Create the board image with handwritten-style text"""
    
    # Create board background
    img = Image.new('RGB', (WIDTH, HEIGHT), BOARD_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Try to load fonts
    try:
        font_paths = [
            '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
            '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
            '/System/Library/Fonts/Helvetica.ttc',
        ]
        title_font = None
        heading_font = None
        body_font = None
        
        for path in font_paths:
            try:
                title_font = ImageFont.truetype(path, 56)
                heading_font = ImageFont.truetype(path, 36)
                body_font = ImageFont.truetype(path, 30)
                break
            except:
                continue
        
        if title_font is None:
            # Fallback to default
            title_font = ImageFont.load_default()
            heading_font = ImageFont.load_default()
            body_font = ImageFont.load_default()
    except:
        title_font = ImageFont.load_default()
        heading_font = ImageFont.load_default()
        body_font = ImageFont.load_default()
    
    # Structured content
    sections = [
        {
            'title': 'MAP OF QUANTUM COMPUTING',
            'type': 'main_title'
        },
        {
            'title': '1. CORE CONCEPTS',
            'items': [
                '• Qubits (vs classical bits)',
                '  - Superposition: |0⟩ + |1⟩',
                '  - Entanglement: Bell states',
                '  - Measurement: collapses state',
                '• Quantum Gates',
                '  - Pauli gates (X, Y, Z)',
                '  - Hadamard (H)',
                '  - CNOT (entanglement)',
                '• Quantum Circuits',
                '  - Unitary operations',
                '  - Reversibility',
            ]
        },
        {
            'title': '2. HARDWARE ARCHITECTURES',
            'items': [
                'Superconducting (IBM, Google)',
                '├─ Transmon qubits',
                '├─ Microwave control',
                '└─ Cryogenic temps (~20mK)',
                '',
                'Trapped Ions (IonQ, Honeywell)',
                '├─ Yb+, Ca+ ions',
                '├─ Laser control',
                '└─ Long coherence times',
                '',
                'Photonic (Xanadu, PsiQuantum)',
                '├─ Quantum optics',
                '└─ Room temp operation',
            ]
        },
        {
            'title': '3. KEY ALGORITHMS',
            'items': [
                "Shor's Algorithm",
                '└─ Factoring → breaks RSA',
                '   O(log³ N) vs O(e^N)',
                '',
                "Grover's Algorithm",
                '└─ Unstructured search',
                '   O(√N) vs O(N)',
                '',
                'QAOA & VQE',
                '└─ Optimization & Chemistry',
            ]
        },
        {
            'title': '4. APPLICATIONS',
            'items': [
                '• Cryptography (breaking & building)',
                '• Drug Discovery',
                '• Financial Modeling',
                '• Material Science',
                '• AI/ML',
            ]
        },
        {
            'title': '5. ERROR CORRECTION',
            'items': [
                'Challenges:',
                '• Decoherence (T1, T2)',
                '• Gate errors (~0.1-1%)',
                '• Measurement errors',
                '',
                'Solutions:',
                '• Surface codes',
                '• Stabilizer codes',
                '• Fault-tolerant thresholds',
            ]
        },
        {
            'title': '6. QUANTUM SUPREMACY',
            'items': [
                'Google (2019): Sycamore',
                '└─ 53 qubits',
                '   "200s vs 10,000 years"',
                '',
                'Current: NISQ era',
                '• ~100-1000 qubits',
                '• Limited coherence',
                '• No practical advantage yet',
            ]
        },
        {
            'title': '7. MAJOR PLAYERS',
            'items': [
                'Big Tech:',
                '• IBM (Qiskit)',
                '• Google (Cirq, Sycamore)',
                '• Microsoft (Azure Quantum)',
                '• Amazon (Braket)',
                '',
                'Startups:',
                '• IonQ, Rigetti',
                '• Xanadu, PsiQuantum',
                '• Quantinuum',
            ]
        },
        {
            'title': '8. SOFTWARE STACK',
            'items': [
                'Languages:',
                '• Qiskit (Python, IBM)',
                '• Cirq (Python, Google)',
                '• Q# (Microsoft)',
                '• PennyLane (Xanadu)',
                '',
                'Cloud: IBM Quantum, AWS, Azure',
            ]
        },
        {
            'title': '9. TIMELINE',
            'items': [
                'Past:',
                '• 1980s: Feynman, Deutsch',
                '• 1994: Shor\'s algorithm',
                '• 2019: Quantum supremacy',
                '',
                'Present (NISQ):',
                '• 50-1000 qubits',
                '• High error rates',
                '',
                'Future:',
                '• 2025-2030: 1000-10000 qubits',
                '• Error correction working',
            ]
        },
        {
            'title': '10. CHALLENGES',
            'items': [
                'Technical:',
                '• Scaling qubit count',
                '• Reducing errors',
                '• Better connectivity',
                '',
                'Practical:',
                '• Cost (millions)',
                '• Expertise gap',
            ]
        },
        {
            'title': 'KEY TAKEAWAY:',
            'items': [
                'Quantum computing = exponential speedup',
                'for SPECIFIC problems',
                'NOT a replacement for classical computing',
                '',
                'Still early days, but progress accelerating!',
                '"The quantum winter is over" 🌱',
            ],
            'type': 'highlight'
        }
    ]
    
    # Draw content
    y_pos = MARGIN
    
    for section in sections:
        # Draw title
        title = section['title']
        if section.get('type') == 'main_title':
            # Center the main title
            bbox = draw.textbbox((0, 0), title, font=title_font)
            text_width = bbox[2] - bbox[0]
            x_pos = (WIDTH - text_width) // 2
            # Add handwritten effect to title
            offset_x = random.uniform(-2, 2)
            offset_y = random.uniform(-2, 2)
            draw_text_with_handwritten_effect(draw, title, 
                                            (x_pos + offset_x, y_pos + offset_y),
                                            title_font, ACCENT_COLOR,
                                            char_offset=2, word_offset=3)
            y_pos += int(title_font.size * 2)
        else:
            # Section heading
            x_pos = MARGIN
            offset_x = random.uniform(-1.5, 1.5)
            offset_y = random.uniform(-1.5, 1.5)
            color = ACCENT_COLOR if section.get('type') != 'highlight' else (200, 50, 50)
            font_to_use = heading_font if section.get('type') != 'highlight' else title_font
            draw_text_with_handwritten_effect(draw, title,
                                            (x_pos + offset_x, y_pos + offset_y),
                                            font_to_use, color,
                                            char_offset=1.5, word_offset=2)
            y_pos += int(font_to_use.size * 1.8)
        
        # Draw items
        if 'items' in section:
            for item in section['items']:
                if item.strip():
                    # Determine indentation
                    if item.strip().startswith(('•', '-', '├', '└')):
                        x_offset = MARGIN + 50
                    elif item.strip()[0].isupper() and ':' in item:
                        x_offset = MARGIN + 30
                    else:
                        x_offset = MARGIN + 60
                    
                    # Add handwritten effect
                    offset_x = random.uniform(-1, 1)
                    offset_y = random.uniform(-1, 1)
                    
                    # Determine color
                    if item.strip().startswith('•'):
                        item_color = BULLET_COLOR
                    else:
                        item_color = TEXT_COLOR
                    
                    draw_text_with_handwritten_effect(draw, item,
                                                    (x_offset + offset_x, y_pos + offset_y),
                                                    body_font, item_color,
                                                    char_offset=1.2, word_offset=1.8)
                    
                    # Calculate line height
                    bbox = draw.textbbox((0, 0), item, font=body_font)
                    y_pos += int((bbox[3] - bbox[1]) * 1.25)
                else:
                    y_pos += int(body_font.size * 0.5)
        
        y_pos += 25  # Space between sections
    
    # Add board texture/imperfections for realism
    for _ in range(100):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        radius = random.randint(1, 4)
        # Slight color variation
        color_variation = random.randint(-8, 8)
        color = tuple(max(240, min(255, c + color_variation)) for c in BOARD_COLOR)
        draw.ellipse([x-radius, y-radius, x+radius, y+radius], fill=color)
    
    # Add subtle grid lines (like a whiteboard)
    for i in range(5):
        y_line = MARGIN + i * (HEIGHT - 2*MARGIN) // 4
        for x in range(0, WIDTH, 2):
            if random.random() > 0.98:  # Sparse dots
                draw.ellipse([x-1, y_line-1, x+1, y_line+1], 
                           fill=(230, 230, 230))
    
    # Add border/frame
    border_width = 4
    draw.rectangle([border_width, border_width, WIDTH-border_width, HEIGHT-border_width],
                  outline=(180, 180, 180), width=border_width)
    
    # Add some smudges/eraser marks
    for _ in range(20):
        x = random.randint(MARGIN, WIDTH - MARGIN)
        y = random.randint(MARGIN, HEIGHT - MARGIN)
        radius = random.randint(3, 8)
        # Semi-transparent white smudge
        smudge = Image.new('RGBA', (radius*2, radius*2), (255, 255, 255, 30))
        img.paste(smudge, (x-radius, y-radius), smudge)
    
    return img

if __name__ == '__main__':
    print("Generating enhanced board image...")
    random.seed(42)  # For reproducibility
    img = create_board_image()
    output_path = 'quantum_computing_map_board.png'
    img.save(output_path, 'PNG', quality=95, optimize=True)
    print(f"Image saved to {output_path}")
    print(f"Image size: {img.size[0]}x{img.size[1]} pixels")
