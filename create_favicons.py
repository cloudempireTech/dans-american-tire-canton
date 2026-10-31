import os
from PIL import Image, ImageDraw

base_dir = r"C:\Users\dasan\.gemini\antigravity\scratch\dans-american-tire-canton\assets\images"
os.makedirs(base_dir, exist_ok=True)

# 1. Create SVG Logo & Favicon
svg_logo = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <defs>
    <linearGradient id="redGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF4B4B"/>
      <stop offset="100%" stop-color="#D90429"/>
    </linearGradient>
    <radialGradient id="darkBg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#162035"/>
      <stop offset="100%" stop-color="#0a0f1d"/>
    </radialGradient>
  </defs>
  <rect width="512" height="512" rx="110" fill="url(#darkBg)"/>
  
  <!-- Outer Tire Tread Ring -->
  <circle cx="256" cy="256" r="215" fill="none" stroke="#334155" stroke-width="26" stroke-dasharray="16 10"/>
  <circle cx="256" cy="256" r="190" fill="none" stroke="url(#redGrad)" stroke-width="8"/>
  
  <!-- Rim / Alloy Spoke Core -->
  <circle cx="256" cy="256" r="140" fill="#0f172a" stroke="#ffffff" stroke-width="6"/>
  <circle cx="256" cy="256" r="48" fill="url(#redGrad)"/>
  
  <!-- Stylized D Star Hub -->
  <polygon points="256,120 274,175 332,175 285,208 303,264 256,230 209,264 227,208 180,175 238,175" fill="#FFB703"/>
  <text x="256" y="380" font-family="'Outfit', sans-serif" font-size="70" font-weight="900" fill="#FFFFFF" text-anchor="middle" letter-spacing="4">DAN'S</text>
</svg>'''

with open(os.path.join(base_dir, "logo.svg"), "w", encoding="utf-8") as f:
    f.write(svg_logo)

with open(os.path.join(base_dir, "favicon.svg"), "w", encoding="utf-8") as f:
    f.write(svg_logo)

# 2. Render PNG 512x512
size = 512
img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Background
draw.rounded_rectangle([16, 16, 496, 496], radius=110, fill=(10, 15, 29, 255))

# Tread ring
draw.ellipse([36, 36, 476, 476], outline=(51, 65, 85, 255), width=24)
draw.ellipse([64, 64, 448, 448], outline=(230, 57, 70, 255), width=8)

# Rim circle
draw.ellipse([110, 110, 402, 402], fill=(15, 23, 42, 255), outline=(255, 255, 255, 255), width=6)
# Hub
draw.ellipse([208, 208, 304, 304], fill=(230, 57, 70, 255))

# Star
star_pts = [(256, 130), (270, 175), (318, 175), (280, 202), (294, 246), (256, 218), (218, 246), (232, 202), (194, 175), (242, 175)]
draw.polygon(star_pts, fill=(255, 183, 3, 255))

# Letter D / American Tire banner
draw.rounded_rectangle([180, 310, 332, 360], radius=8, fill=(230, 57, 70, 255))
draw.line([(200, 335), (312, 335)], fill=(255, 255, 255, 255), width=6)

logo_512_path = os.path.join(base_dir, "logo-512.png")
img.save(logo_512_path, "PNG")

# 3. Apple touch icon 180x180
apple_icon = img.resize((180, 180), Image.Resampling.LANCZOS)
apple_icon.save(os.path.join(base_dir, "apple-touch-icon.png"), "PNG")

# 4. Favicon 32x32
fav_32 = img.resize((32, 32), Image.Resampling.LANCZOS)
fav_32.save(os.path.join(base_dir, "favicon-32x32.png"), "PNG")

# 5. Favicon ico
img.resize((32, 32), Image.Resampling.LANCZOS).save(os.path.join(base_dir, "favicon.ico"), format="ICO")

print("All Dan's American Tire favicons successfully generated!")
