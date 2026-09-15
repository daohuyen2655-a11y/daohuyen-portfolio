import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the memory-heavy VRAM wrapper
content = content.replace(
    'className={`transition-opacity duration-1000 ease-out transform-gpu will-change-[opacity] ${entered ? \'opacity-100\' : \'opacity-0\'}`}',
    'className=""'
)

# Instead, add a simple cover div right after the interactive intro to act as the fade.
intro_marker = "</div>\n\n      <div className=\"\">\n        \n        {/* ─── HERO SECTION ─── */}"

new_intro = """</div>

      {/* Crossfade Cover - Fades out to reveal page, infinitely faster than fading the page in */}
      <div className={`fixed inset-0 z-[90] bg-[#FAF4E1] transition-opacity duration-1000 ease-in-out pointer-events-none ${entered ? 'opacity-0' : 'opacity-100'}`}></div>

      <div className="">
        
        {/* ─── HERO SECTION ─── */}"""

content = content.replace(intro_marker, new_intro)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("SUCCESS")
