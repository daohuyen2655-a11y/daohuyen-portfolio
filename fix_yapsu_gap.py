import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Reduce TOC bottom padding
content = content.replace(
    'className="relative w-full pb-32 bg-[#F6F4EB]',
    'className="relative w-full pb-12 bg-[#F6F4EB]'
)

# 2. Reduce Yapsu AI top padding
content = content.replace(
    'className="relative w-full py-32 bg-gradient-to-b from-[#FCFBF9] via-[#FFF3E6]',
    'className="relative w-full pt-12 pb-32 bg-gradient-to-b from-[#FCFBF9] via-[#FFF3E6]'
)

# 3. Shorten the transition bridge so it doesn't overlap text, and fix the starting color to perfectly match TOC
content = content.replace(
    'className="absolute top-0 left-0 w-full h-[250px] bg-gradient-to-b from-[#F4F1EA] to-[#FCFBF9]',
    'className="absolute top-0 left-0 w-full h-[100px] bg-gradient-to-b from-[#F6F4EB] to-[#FCFBF9]'
)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("SUCCESS")
