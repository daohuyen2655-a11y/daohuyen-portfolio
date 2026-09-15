import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace border-[8px] for Key Visual in Gen 20 (line ~962)
old_gen20_kv = """<div className="relative w-full max-w-5xl rounded-[32px] overflow-hidden border-[8px] border-white shadow-[0_20px_50px_rgba(59,91,53,0.2)] group">"""
new_gen20_kv = """<div className="relative w-full max-w-5xl rounded-[32px] overflow-hidden border-[4px] border-white shadow-[0_20px_50px_rgba(59,91,53,0.2)] group">"""
content = content.replace(old_gen20_kv, new_gen20_kv)

# Replace border-[8px] for Key Visual in 19th Anniversary (line ~1088)
old_19th_kv = """<div className="relative w-full max-w-5xl rounded-[32px] overflow-hidden border-[8px] border-white shadow-[0_20px_50px_rgba(134,101,195,0.2)] group">"""
new_19th_kv = """<div className="relative w-full max-w-5xl rounded-[32px] overflow-hidden border-[4px] border-white shadow-[0_20px_50px_rgba(134,101,195,0.2)] group">"""
content = content.replace(old_19th_kv, new_19th_kv)

# Replace avatar badges p-2 -> p-1
old_gen20_avt = """<div className="relative -mt-20 w-32 h-32 md:w-44 md:h-44 rounded-full p-2 bg-white shadow-xl z-10 group hover:-translate-y-2 transition-transform duration-300 ">"""
new_gen20_avt = """<div className="relative -mt-20 w-32 h-32 md:w-44 md:h-44 rounded-full p-1 bg-white shadow-xl z-10 group hover:-translate-y-2 transition-transform duration-300 ">"""
content = content.replace(old_gen20_avt, new_gen20_avt)

old_19th_avt = """<div className="relative -mt-20 w-32 h-32 md:w-44 md:h-44 rounded-full p-2 bg-white shadow-xl z-10 group hover:-translate-y-2 transition-transform duration-300">"""
new_19th_avt = """<div className="relative -mt-20 w-32 h-32 md:w-44 md:h-44 rounded-full p-1 bg-white shadow-xl z-10 group hover:-translate-y-2 transition-transform duration-300">"""
content = content.replace(old_19th_avt, new_19th_avt)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS")
