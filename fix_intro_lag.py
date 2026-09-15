import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the heavy wrapper div with just an empty wrapper or nothing.
old_wrapper = "className={`transition-opacity duration-1000 delay-300 ${entered ? 'opacity-100' : 'opacity-0 pointer-events-none'}`}"
new_wrapper = "className=\"\""
content = content.replace(old_wrapper, new_wrapper)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("SUCCESS")
