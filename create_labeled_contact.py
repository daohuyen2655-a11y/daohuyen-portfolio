import os
import glob
from PIL import Image, ImageDraw, ImageFont

# Get all snapshots
snapshots_dir = "public/assets/portfolio_assets/Yapsu AI/snapshots/"
files = glob.glob(os.path.join(snapshots_dir, "*.jpg"))
files.sort()

# Limit to 30 files for a reasonable grid
files = files[:30] 

# Dimensions for each thumbnail
thumb_w, thumb_h = 200, 430
cols = 6
rows = (len(files) + cols - 1) // cols

contact_sheet = Image.new('RGB', (cols * thumb_w, rows * thumb_h), (255, 255, 255))

for i, filepath in enumerate(files):
    filename = os.path.basename(filepath)
    try:
        img = Image.open(filepath)
        img.thumbnail((thumb_w, thumb_h - 30))  # Leave room for text
        
        col = i % cols
        row = i // cols
        
        x = col * thumb_w
        y = row * thumb_h
        
        # Paste image
        contact_sheet.paste(img, (x, y))
        
        # Draw filename
        draw = ImageDraw.Draw(contact_sheet)
        draw.text((x + 5, y + thumb_h - 25), filename, fill=(255, 0, 0))
    except Exception as e:
        print(f"Error processing {filename}: {e}")

contact_sheet.save("/tmp/labeled_snapshots.jpg")
print("Saved /tmp/labeled_snapshots.jpg")
