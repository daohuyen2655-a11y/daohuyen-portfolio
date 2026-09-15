import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

tag_to_remove = """<h4 className="font-['Quicksand'] font-bold text-lg text-[#4194B1] tracking-wider uppercase mt-4 bg-white/70 px-6 py-2 rounded-full shadow-sm">
                      Social Media Posts & Partners
                  </h4>"""

content = content.replace(tag_to_remove, "")

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS")
