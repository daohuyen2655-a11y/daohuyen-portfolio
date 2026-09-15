import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Make the Yapsu AI gradient much more visible (using a deeper soft orange #FFEDD5)
content = content.replace('bg-gradient-to-b from-[#FCFBF9] to-[#FFF3E6]', 'bg-gradient-to-b from-[#FCFBF9] via-[#FFF3E6] to-[#FFD8B5]')

# Update the bridge to match the new bottom color
content = content.replace('from-[#FFF3E6] to-[#06112E]', 'from-[#FFD8B5] to-[#06112E]')

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("SUCCESS")
