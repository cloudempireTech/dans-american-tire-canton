import urllib.request
import os
from PIL import Image

output_dir = r"C:\Users\dasan\.gemini\antigravity\scratch\dans-american-tire-canton\assets\images"
os.makedirs(output_dir, exist_ok=True)

# Curated high-res Unsplash IDs for tire shop, wheel alignment, brakes, fleet auto service
assets = [
    ("tire-tread-display.jpg", "photo-1578844251758-2f71da64c96f"),
    ("wheel-alignment-laser.jpg", "photo-1619642751034-765dfdf7c58e"),
    ("brake-rotor-caliper.jpg", "photo-1486006920555-c77dce18193b"),
    ("mechanic-suspension-lift.jpg", "photo-1617814076367-b759c7d7e738"),
    ("tire-mounting-balancer.jpg", "photo-1549399542-7e3f8b79c341"),
    ("commercial-fleet-vans.jpg", "photo-1519003722824-194d4455a60c"),
    ("oil-change-inspection.jpg", "photo-1503376780353-7e6692767b70"),
    ("canton-shop-exterior.jpg", "photo-1580273916550-e323be2ae537"),
    ("towing-roadside-truck.jpg", "photo-1563720223185-11003d516935"),
    ("satisfied-driver-keys.jpg", "photo-1560250097-0b93528c311a")
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

for filename, photo_id in assets:
    target_path = os.path.join(output_dir, filename)
    url = f"https://images.unsplash.com/{photo_id}?auto=format&fit=crop&w=1200&q=80"
    print(f"Downloading {filename}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        tmp_path = target_path + ".tmp"
        with urllib.request.urlopen(req) as resp, open(tmp_path, 'wb') as f:
            f.write(resp.read())
        
        img = Image.open(tmp_path)
        img = img.convert('RGB')
        img.save(target_path, 'JPEG', quality=85, optimize=True)
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        size_kb = os.path.getsize(target_path) / 1024
        print(f"  Saved {filename} ({size_kb:.1f} KB)")
    except Exception as e:
        print(f"  Error downloading {filename}: {e}")

print("Image download and optimization complete!")
