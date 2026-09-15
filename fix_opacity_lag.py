import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Add the opacity transition back, but with hardware acceleration and without pointer-events-none (since we have scroll lock)
old_wrapper = "className=\"\""
new_wrapper = "className={`transition-opacity duration-1000 ease-out transform-gpu will-change-[opacity] ${entered ? 'opacity-100' : 'opacity-0'}`}"

# If old_wrapper is not found exactly as "", we can search for `<div className="">`
content = content.replace('<div className="">', f'<div {new_wrapper}>')

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("SUCCESS")
