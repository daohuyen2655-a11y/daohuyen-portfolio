import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

target = '<section id="yapsu-ai" className="relative w-full pt-12 pb-32 bg-gradient-to-b from-[#FCFBF9] via-[#FFF3E6] to-[#FFD8B5] text-[#334155] font-sans">\n           \n           {/* Transition from TOC (Beige) to Yapsu (Light) */}'

replacement = '<section id="yapsu-ai" className="relative w-full pt-12 pb-32 bg-gradient-to-b from-[#FCFBF9] via-[#FFF3E6] to-[#FFD8B5] text-[#334155] font-sans">\n           \n           {/* Transition from TOC (Beige) to Yapsu (Light) */}\n           <div className="absolute top-0 left-0 w-full h-[100px] bg-gradient-to-b from-[#F6F4EB] to-[#FCFBF9] z-10 pointer-events-none"></div>'

if target in content:
    content = content.replace(target, replacement)
    with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS")
else:
    print("TARGET NOT FOUND")
