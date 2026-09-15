from PIL import Image
import numpy as np

# Load the image
img_path = 'public/assets/portfolio_assets/PAINTASO/KEY VISUAL/COVER.jpg'
img = Image.open(img_path).convert('RGB')
img_data = np.array(img)

# We are looking for yellow colors. Yellow in RGB has high Red and Green, and lower Blue.
# Let's filter pixels that are "yellow-ish"
pixels = img_data.reshape(-1, 3)
yellows = []
for p in pixels:
    r, g, b = p
    # Yellow criteria: R > 150, G > 150, B < 120 (approximate)
    if r > 180 and g > 150 and b < 140:
        yellows.append(p)

if len(yellows) > 0:
    # Find the most common/average yellow
    avg_yellow = np.median(yellows, axis=0).astype(int)
    print(f"Found yellow: #{avg_yellow[0]:02x}{avg_yellow[1]:02x}{avg_yellow[2]:02x}")
else:
    print("No yellow found.")
