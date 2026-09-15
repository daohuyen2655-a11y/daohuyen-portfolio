import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Gen 20 Title
old_gen20 = """<h2 className="font-['Fredoka'] text-[50px] md:text-[80px] font-black text-[#2C4424] leading-none mb-6 " style={{ textShadow: '4px 4px 0px rgba(255,255,255,0.8)' }}>"""
new_gen20 = """<h2 className="font-['Fredoka'] text-[50px] md:text-[80px] font-black text-transparent bg-clip-text bg-gradient-to-b from-[#A1C97A] to-[#2C4424] leading-none mb-6 pb-2" style={{ WebkitTextStroke: '2px #FFF', filter: 'drop-shadow(4px 4px 0px rgba(44,68,36,0.3))' }}>"""
content = content.replace(old_gen20, new_gen20)

# Replace 19th Title
old_19th = """<h2 className="font-['Fredoka'] text-[60px] md:text-[90px] font-black text-[#6B4AA6] leading-none mb-6" style={{ textShadow: '4px 4px 0px rgba(255,255,255,0.9)' }}>"""
new_19th = """<h2 className="font-['Fredoka'] text-[60px] md:text-[90px] font-black text-transparent bg-clip-text bg-gradient-to-b from-[#D1B3FF] to-[#6B4AA6] leading-none mb-6 pb-2" style={{ WebkitTextStroke: '2px #FFF', filter: 'drop-shadow(4px 4px 0px rgba(107,74,166,0.3))' }}>"""
content = content.replace(old_19th, new_19th)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS")
