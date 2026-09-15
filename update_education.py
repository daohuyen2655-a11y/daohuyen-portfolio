import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the specific education date line
old_date = '<p className="font-[\'Quicksand\'] font-bold text-lg mb-1 opacity-80">Sep 2024 – Apr 2028</p>'
new_date = '<p className="font-[\'Quicksand\'] font-bold text-lg mb-1 opacity-80">Sep 2024 – Present</p>'

content = content.replace(old_date, new_date)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS")
