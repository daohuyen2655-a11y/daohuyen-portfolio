import re

with open('src/app/globals.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the incredibly heavy mix-blend-mode
content = content.replace('mix-blend-mode: multiply;', '/* mix-blend-mode: multiply; removed for scroll performance */')

with open('src/app/globals.css', 'w', encoding='utf-8') as f:
    f.write(content)
print("SUCCESS")
