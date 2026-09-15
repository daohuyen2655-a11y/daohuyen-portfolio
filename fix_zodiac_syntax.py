import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

bad_style = "style={ filter: 'drop-shadow(0px 0px 10px rgba(255,255,255,1))' }"
good_style = "style={{ filter: 'drop-shadow(0px 0px 10px rgba(255,255,255,1))' }}"

content = content.replace(bad_style, good_style)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS")
