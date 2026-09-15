import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the start of the first project section
match = re.search(r'\{\/\*\s*───\s*01\.\s*.*?\s*───\s*\*\/\}', content)
if match:
    header = content[:match.start()]
    with open('page_header_tmp.txt', 'w', encoding='utf-8') as f:
        f.write(header)
    print("Extracted header.")
else:
    print("Could not find section comment.")
