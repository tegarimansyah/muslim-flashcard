#!/usr/bin/env python3
"""
Generate PWA icons from SVG source
Requires: cairosvg, pillow
Install: pip install cairosvg pillow
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_simple_icon(size):
    """Create a simple geometric Islamic-style icon"""
    # Create image with transparent background
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Colors
    bg_color = (5, 150, 105, 255)  # #059669
    bg_color_light = (4, 120, 87, 255)  # #047857
    white = (255, 255, 255, 255)
    
    # Draw main circle background
    center = size // 2
    radius = int(size * 0.47)
    
    # Draw gradient-like circle
    for i in range(radius):
        alpha = int(255 * (1 - i / radius))
        color = (
            int(bg_color[0] + (bg_color_light[0] - bg_color[0]) * (i / radius)),
            int(bg_color[1] + (bg_color_light[1] - bg_color[1]) * (i / radius)),
            int(bg_color[2] + (bg_color_light[2] - bg_color[2]) * (i / radius)),
            alpha
        )
        draw.ellipse([center - radius + i, center - radius + i, 
                     center + radius - i, center + radius - i], fill=color)
    
    # Draw decorative circles
    if size >= 96:
        draw.ellipse([center - int(size * 0.39), center - int(size * 0.39),
                     center + int(size * 0.39), center + int(size * 0.39)], 
                    outline=white, width=2)
    
    if size >= 128:
        draw.ellipse([center - int(size * 0.31), center - int(size * 0.31),
                     center + int(size * 0.31), center + int(size * 0.31)], 
                    outline=white, width=2)
    
    # Draw book/reading symbol
    book_width = int(size * 0.08)
    book_height = int(size * 0.31)
    page_width = int(size * 0.19)
    
    # Book spine
    draw.rectangle([center - book_width // 2, center - book_height // 2,
                   center + book_width // 2, center + book_height // 2], 
                  fill=white)
    
    # Left page (curved)
    left_page = [
        (center - book_width // 2 - 2, center - book_height // 2 + 2),
        (center - int(size * 0.2), center - int(size * 0.12)),
        (center - int(size * 0.2), center + int(size * 0.12)),
        (center - book_width // 2 - 2, center + book_height // 2 - 2),
        (center - book_width // 2, center + book_height // 2 - 2),
        (center - book_width // 2, center - book_height // 2 + 2)
    ]
    draw.polygon(left_page, fill=white)
    
    # Right page (curved)
    right_page = [
        (center + book_width // 2 + 2, center - book_height // 2 + 2),
        (center + int(size * 0.2), center - int(size * 0.12)),
        (center + int(size * 0.2), center + int(size * 0.12)),
        (center + book_width // 2 + 2, center + book_height // 2 - 2),
        (center + book_width // 2, center + book_height // 2 - 2),
        (center + book_width // 2, center - book_height // 2 + 2)
    ]
    draw.polygon(right_page, fill=white)
    
    # Add decorative dots if size allows
    if size >= 96:
        dot_radius = max(2, int(size * 0.01))
        dot_offset = int(size * 0.12)
        
        # Left side dots
        draw.ellipse([center - dot_offset - dot_radius, center - int(size * 0.06) - dot_radius,
                     center - dot_offset + dot_radius, center - int(size * 0.06) + dot_radius],
                    fill=bg_color)
        draw.ellipse([center - dot_offset - dot_radius, center + int(size * 0.06) - dot_radius,
                     center - dot_offset + dot_radius, center + int(size * 0.06) + dot_radius],
                    fill=bg_color)
        
        # Right side dots
        draw.ellipse([center + dot_offset - dot_radius, center - int(size * 0.06) - dot_radius,
                     center + dot_offset + dot_radius, center - int(size * 0.06) + dot_radius],
                    fill=bg_color)
        draw.ellipse([center + dot_offset - dot_radius, center + int(size * 0.06) - dot_radius,
                     center + dot_offset + dot_radius, center + int(size * 0.06) + dot_radius],
                    fill=bg_color)
    
    # Add Arabic letter "Dz" (ذ) at bottom if size allows
    if size >= 128:
        try:
            # Try to use a system font, fallback to default
            font_size = int(size * 0.19)
            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except:
                font = ImageFont.load_default()
            
            text = "ذ"
            text_bbox = draw.textbbox((0, 0), text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            
            text_x = center - text_width // 2
            text_y = center + int(size * 0.25) - text_height // 2
            
            draw.text((text_x, text_y), text, font=font, fill=white)
        except Exception as e:
            # If font loading fails, just skip the text
            pass
    
    return img

def generate_all_icons():
    """Generate all required PWA icon sizes"""
    sizes = [72, 96, 128, 144, 152, 192, 384, 512]
    icons_dir = "static/icons"
    
    # Ensure icons directory exists
    os.makedirs(icons_dir, exist_ok=True)
    
    print("Generating PWA icons...")
    for size in sizes:
        icon = create_simple_icon(size)
        filename = f"icon-{size}x{size}.png"
        filepath = os.path.join(icons_dir, filename)
        icon.save(filepath, "PNG")
        print(f"  Generated: {filename} ({size}x{size})")
    
    # Also generate favicon.ico (16x16, 32x32)
    print("\nGenerating favicon.ico...")
    favicon_sizes = [16, 32]
    favicon_images = []
    for size in favicon_sizes:
        favicon_images.append(create_simple_icon(size))
    
    favicon_path = os.path.join("static", "favicon.ico")
    favicon_images[0].save(favicon_path, format='ICO', sizes=[(16, 16), (32, 32)])
    print(f"  Generated: favicon.ico")
    
    # Generate apple-touch-icon
    print("\nGenerating apple-touch-icon.png...")
    apple_icon = create_simple_icon(180)
    apple_path = os.path.join("static", "apple-touch-icon.png")
    apple_icon.save(apple_path, "PNG")
    print(f"  Generated: apple-touch-icon.png (180x180)")
    
    print("\n✅ All icons generated successfully!")

if __name__ == "__main__":
    generate_all_icons()