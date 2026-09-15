import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Subtext
old_subtext = """A majestic and adventurous visual identity designed for the Chinese Debate competition. Emphasizing a grand, journey-driven aesthetic of conquering new peaks to inspire and captivate a young audience."""
new_subtext = """A fierce and explosive visual identity designed for the Chinese Debate competition. Emphasizing a dynamic, fiery golden dragon aesthetic to ignite passion and captivate a modern youth audience."""
content = content.replace(old_subtext, new_subtext)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS")
