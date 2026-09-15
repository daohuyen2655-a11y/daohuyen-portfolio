import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

old_toc_array_pattern = r"const tocItems = \[.*?\];"
new_toc_array = """const tocItems = [
    { id: '01', title: "Yapsu AI", color: 'bg-[#E8F0F8]', hoverBorder: 'group-hover:border-[#6BA5D7]', textColor: 'text-[#5C4A3D]', tapeShape: 'star', tapeColor: 'bg-[#6BA5D7]', anchor: '#yapsu-ai' },
    { id: '02', title: "Chinese\\nDebate '26", color: 'bg-[#E6F7FF]', hoverBorder: 'group-hover:border-[#00C2CC]', textColor: 'text-[#5C4A3D]', tapeShape: 'clover', tapeColor: 'bg-[#00C2CC]', anchor: '#chinese-debate-26' },
    { id: '03', title: "Gen 20th\\nRecruit", color: 'bg-[#EDF5E8]', hoverBorder: 'group-hover:border-[#3B5B35]', textColor: 'text-[#5C4A3D]', tapeShape: 'flower', tapeColor: 'bg-[#3B5B35]', anchor: '#gen-20-recruit' },
    { id: '04', title: "19th\\nBirthday", color: 'bg-[#F4EEF7]', hoverBorder: 'group-hover:border-[#A890D8]', textColor: 'text-[#5C4A3D]', tapeShape: 'heart', tapeColor: 'bg-[#A890D8]', anchor: '#19th-birthday' },
    { id: '05', title: "Chinese\\nDebate '25", color: 'bg-[#FDF8E7]', hoverBorder: 'group-hover:border-[#D4AF37]', textColor: 'text-[#5C4A3D]', tapeShape: 'star', tapeColor: 'bg-[#D4AF37]', anchor: '#chinese-debate-25' },
    { id: '06', title: "Talkshow", color: 'bg-[#E8F4F8]', hoverBorder: 'group-hover:border-[#58B3D3]', textColor: 'text-[#5C4A3D]', tapeShape: 'clover', tapeColor: 'bg-[#58B3D3]', anchor: '#talkshow' },
    { id: '07', title: "Zodiac", color: 'bg-[#EAEBF2]', hoverBorder: 'group-hover:border-[#2C3E50]', textColor: 'text-[#5C4A3D]', tapeShape: 'flower', tapeColor: 'bg-[#2C3E50]', anchor: '#zodiac' },
    { id: '08', title: "Paintaso", color: 'bg-[#FDF2F5]', hoverBorder: 'group-hover:border-[#E53935]', textColor: 'text-[#5C4A3D]', tapeShape: 'heart', tapeColor: 'bg-[#E53935]', anchor: '#paintaso' },
  ];"""

# Replace the array
content = re.sub(old_toc_array_pattern, new_toc_array, content, flags=re.DOTALL)

# Fix the bottom row mapping
old_slice = "tocItems.slice(4, 7).map("
new_slice = "tocItems.slice(4, 8).map("
content = content.replace(old_slice, new_slice)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("TOC reordered to exactly 8 items (4-4 layout).")

