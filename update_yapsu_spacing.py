import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the icon
old_icon_pattern = r"\{/\* App Icon Mockup \*/\}.*?<p className=\"text-lg md:text-xl text-blue-100/90 leading-relaxed font-light mt-2 max-w-md\">"
new_icon = """{/* App Icon Mockup */}
                       <div className="w-[120px] h-[120px] rounded-[28px] shadow-[0_20px_40px_rgba(0,0,0,0.5)] bg-transparent shrink-0 overflow-hidden border border-white/10">
                          <img src="/assets/portfolio_assets/Yapsu AI/yapsu_icon.png" className="w-full h-full object-cover" />
                       </div>
                       
                       <p className="text-lg md:text-xl text-blue-100/90 leading-relaxed font-light mt-2 max-w-md">"""
content = re.sub(old_icon_pattern, new_icon, content, flags=re.DOTALL)

# Reduce huge margins causing white space
content = content.replace("mb-48 gap-16", "mb-10 gap-16")
content = content.replace("mb-48 relative", "mb-16 relative")
content = content.replace("pt-20", "pt-0")
content = content.replace("translate-y-10", "translate-y-0")

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
