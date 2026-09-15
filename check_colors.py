import os
from PIL import Image

base_dir = "public/assets/portfolio_assets/ZODIAC COLLECTIONS"
sample_images = []
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.lower().endswith('.png'):
            sample_images.append(os.path.join(root, f))
            if len(sample_images) > 5:
                break
    if len(sample_images) > 5:
        break

for img_path in sample_images:
    try:
        with Image.open(img_path) as img:
            img = img.convert('RGB')
            # resize to 1x1 to get average color
            avg_color = img.resize((1, 1)).getpixel((0, 0))
            print(f"{os.path.basename(img_path)}: {avg_color}")
    except Exception as e:
        print(f"Error on {img_path}: {e}")
