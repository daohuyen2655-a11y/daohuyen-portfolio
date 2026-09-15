import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add useEffect for scroll locking
old_useeffect = "useEffect(() => { setMounted(true); }, []);"
new_useeffect = """useEffect(() => { setMounted(true); }, []);
  useEffect(() => {
    if (mounted) {
      if (!entered) {
        document.body.style.overflow = 'hidden';
      } else {
        document.body.style.overflow = '';
      }
    }
  }, [entered, mounted]);"""
content = content.replace(old_useeffect, new_useeffect)

# 2. Remove the layout-shifting classes from the main wrapper
old_wrapper = "className={`transition-opacity duration-1000 delay-300 ${entered ? 'opacity-100' : 'opacity-0 h-screen overflow-hidden'}`}"
new_wrapper = "className={`transition-opacity duration-1000 delay-300 ${entered ? 'opacity-100' : 'opacity-0 pointer-events-none'}`}"
content = content.replace(old_wrapper, new_wrapper)

# 3. Shrink Gap
content = content.replace(
    'className="w-full h-[300px] bg-gradient-to-b from-[#FFD8B5] to-[#06112E]"',
    'className="w-full h-[150px] bg-gradient-to-b from-[#FFD8B5] to-[#06112E]"'
)
content = content.replace(
    'id="chinese-debate-2026" className="relative w-full py-24',
    'id="chinese-debate-2026" className="relative w-full pt-12 pb-24'
)

# 4. Fix Cropping (object-cover -> object-contain) in Chinese Debate 2026
content = content.replace(
    'alt="Chinese Debate Key Visual Cover" className="w-full h-full object-cover"',
    'alt="Chinese Debate Key Visual Cover" className="w-full h-full object-contain p-2"'
)
content = content.replace(
    'alt="Backdrop Design" className="w-full h-full object-cover group-hover:scale-105',
    'alt="Backdrop Design" className="w-full h-full object-contain p-4 group-hover:scale-105'
)

# Fix social posts cropping
content = content.replace(
    'alt={filename.replace(\'.png\', \'\')} className="w-full h-full object-cover group-hover:scale-105',
    'alt={filename.replace(\'.png\', \'\')} className="w-full h-full object-contain p-4 group-hover:scale-105'
)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("SUCCESS")
