import re
import os
import shutil

with open('src/app/page.tsx', 'r') as f:
    content = f.read()

# Remove the symlink if it exists
symlink_path = 'public/assets/portfolio_assets'
if os.path.islink(symlink_path):
    os.remove(symlink_path)
    os.makedirs(symlink_path)
elif not os.path.exists(symlink_path):
    os.makedirs(symlink_path)

# Find all /assets/portfolio_assets/ paths
paths = re.findall(r'[\'"]/assets/portfolio_assets/([^\'"]+)[\'"]', content)
paths = list(set(paths))

source_base = "/Users/daohuyen/.gemini/antigravity/scratch/assets/portfolio_assets/PORTFOLIO ASSETS"
dest_base = "public/assets/portfolio_assets"

total_size = 0
for p in paths:
    src_file = os.path.join(source_base, p)
    dest_file = os.path.join(dest_base, p)
    
    if os.path.exists(src_file):
        os.makedirs(os.path.dirname(dest_file), exist_ok=True)
        shutil.copy2(src_file, dest_file)
        size = os.path.getsize(src_file)
        total_size += size
        print(f"Copied: {p} ({size/1024/1024:.2f} MB)")
    else:
        print(f"NOT FOUND: {src_file}")

print(f"Total size copied: {total_size/1024/1024:.2f} MB")
