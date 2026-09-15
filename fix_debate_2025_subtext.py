import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Subtext
old_subtext = """A vibrant, futuristic visual identity tailored for the Chinese Debate competition, featuring a dynamic, high-energy cyber aesthetic designed to captivate a modern youth audience."""
new_subtext = """A majestic and adventurous visual identity designed for the Chinese Debate competition. Emphasizing a grand, journey-driven aesthetic of conquering new peaks to inspire and captivate a young audience."""
content = content.replace(old_subtext, new_subtext)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS")
