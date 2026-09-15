import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = "{/* ─── 07. ZODIAC ─── */}"
end_marker = "{/* ─── 08. PAINTASO ─── */}"
start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    zodiac_section = content[start_idx:end_idx]
    
    # 1. Update Subtitle
    zodiac_section = zodiac_section.replace(
        "font-['Quicksand'] tracking-[0.2em] font-bold",
        "font-serif italic tracking-[0.3em] font-normal"
    )
    
    # 2. Update Main Title "ZODIAC"
    zodiac_section = zodiac_section.replace(
        "font-['Fredoka'] text-[60px] md:text-[90px] text-[#4A4238] leading-none mb-6 text-center font-medium",
        "font-serif text-[60px] md:text-[100px] text-[#2C2822] leading-none mb-8 text-center font-light tracking-[0.1em]"
    )
    
    # 3. Update Description
    zodiac_section = zodiac_section.replace(
        "font-['Quicksand'] font-medium leading-relaxed px-4",
        "font-serif italic font-normal leading-loose px-4"
    )
    
    # 4. Update Card Inner Header "MÁC X"
    zodiac_section = zodiac_section.replace(
        "font-['Fredoka'] font-medium text-3xl md:text-4xl text-[#4A4238] tracking-wide",
        "font-serif italic text-3xl md:text-5xl text-[#2C2822] tracking-widest"
    )
    
    # 5. Update "NEXT" Button
    zodiac_section = zodiac_section.replace(
        "font-['Quicksand'] font-semibold text-[#8C8377] hover:text-[#4A4238] transition-colors cursor-pointer text-sm md:text-base px-4 py-2",
        "font-sans font-light tracking-widest text-[#8C8377] hover:text-[#2C2822] transition-colors cursor-pointer text-xs md:text-sm px-4 py-2 uppercase"
    )

    content = content[:start_idx] + zodiac_section + content[end_idx:]
    with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS")
else:
    print("FAILED")
