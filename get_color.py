from PIL import Image
import sys

img_path = "/Users/daohuyen/.gemini/antigravity/brain/036f841b-d9bb-4ba8-b57c-44e9a3dd7a43/.user_uploaded/media_1789455609275.png"
try:
    img = Image.open(img_path)
    img = img.convert('RGB')
    
    # Get a few sample points on the folder front
    # The folder front is the large beige area
    w, h = img.size
    samples = [
        img.getpixel((w//2, h//2)), # center
        img.getpixel((w//4, h//2)), # mid left
        img.getpixel((3*w//4, h//2)) # mid right
    ]
    
    for i, rgb in enumerate(samples):
        hex_color = '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])
        print(f"Sample {i+1}: {hex_color} (RGB: {rgb})")
        
except Exception as e:
    print("Error:", e)
