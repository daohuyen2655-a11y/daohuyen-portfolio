import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Gen 20 Title
old_gen20 = """WebkitTextStroke: '2px #FFF', filter: 'drop-shadow(4px 4px 0px rgba(44,68,36,0.3))'"""
new_gen20 = """filter: 'drop-shadow(4px 4px 0px rgba(44,68,36,0.3))'"""
content = content.replace(old_gen20, new_gen20)

# Replace 19th Title
old_19th = """WebkitTextStroke: '2px #FFF', filter: 'drop-shadow(4px 4px 0px rgba(107,74,166,0.3))'"""
new_19th = """filter: 'drop-shadow(4px 4px 0px rgba(107,74,166,0.3))'"""
content = content.replace(old_19th, new_19th)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS")
