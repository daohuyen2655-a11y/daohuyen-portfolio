import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove all noise overlays
content = re.sub(r'<div className="absolute inset-0 noise-overlay.*?</div>\s*', '', content)

# 2. Add introVisible state
old_state = "const [entered, setEntered] = useState(false);"
new_state = "const [entered, setEntered] = useState(false);\n  const [introVisible, setIntroVisible] = useState(true);\n  useEffect(() => { if (entered) setTimeout(() => setIntroVisible(false), 1000); }, [entered]);"
content = content.replace(old_state, new_state)

# 3. Conditionally render the intro block
old_intro = """{/* ─── INTERACTIVE INTRO ─── */}
      <div className={`fixed inset-0 z-[100] bg-[#FDFCEE] flex flex-col items-center justify-center transition-transform duration-1000 ease-[cubic-bezier(0.76,0,0.24,1)] ${entered ? '-translate-y-full' : 'translate-y-0'}`}>"""
new_intro = """{/* ─── INTERACTIVE INTRO ─── */}
      {introVisible && (
        <div className={`fixed inset-0 z-[100] bg-[#FDFCEE] flex flex-col items-center justify-center transition-transform duration-1000 ease-[cubic-bezier(0.76,0,0.24,1)] ${entered ? '-translate-y-full' : 'translate-y-0'}`}>"""
content = content.replace(old_intro, new_intro)

# Close the div
old_intro_close = """</div>
      </div>

      {/* Crossfade Cover - Fades out to reveal page, infinitely faster than fading the page in */}
      <div className={`fixed inset-0 z-[90] bg-[#FAF4E1] transition-opacity duration-1000 ease-in-out pointer-events-none ${entered ? 'opacity-0' : 'opacity-100'}`}></div>"""

new_intro_close = """</div>
        </div>
      )}

      {/* Crossfade Cover - Fades out to reveal page, infinitely faster than fading the page in */}
      {introVisible && (
        <div className={`fixed inset-0 z-[90] bg-[#FAF4E1] transition-opacity duration-1000 ease-in-out pointer-events-none ${entered ? 'opacity-0' : 'opacity-100'}`}></div>
      )}"""
content = content.replace(old_intro_close, new_intro_close)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS")
