import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Spacing: Increase padding-top of the TOC section to push it away from the marquee
content = content.replace(
    '''<section id="toc" className="relative w-full pb-32 bg-[#F6F4EB] overflow-hidden pt-16 md:pt-0">''',
    '''<section id="toc" className="relative w-full pb-32 bg-[#F6F4EB] overflow-hidden pt-32 md:pt-24">'''
)

# 2. Title: Change from Orange to Black (#222) to match the "PRODUCT DESIGN" banner text
old_title = """<h2 className="text-[70px] md:text-[100px] font-['Fredoka'] font-black text-[#E8704A] rotate-[-2deg] transition-transform duration-500 group-hover:scale-105" style={{ textShadow: '-4px -4px 0 #FFF, 4px -4px 0 #FFF, -4px 4px 0 #FFF, 4px 4px 0 #FFF, 8px 8px 0px rgba(232,112,74,0.2)' }}>
                       Table of Contents
                    </h2>"""

new_title = """<h2 className="text-[70px] md:text-[100px] font-['Fredoka'] font-black text-[#222] rotate-[-2deg] transition-transform duration-500 group-hover:scale-105" style={{ textShadow: '-4px -4px 0 #FFF, 4px -4px 0 #FFF, -4px 4px 0 #FFF, 4px 4px 0 #FFF, 8px 8px 0px rgba(34,34,34,0.15)' }}>
                       Table of Contents
                    </h2>"""
content = content.replace(old_title, new_title)

# 3. Cards: Fix the cut-off number and change hover colors to match the banner (Yellow/Orange #F9B658 and Black #222)
old_cards = """<a key={idx} href={`#${item.anchor}`} className="group relative w-full max-w-[280px] h-[180px] block">
                       {/* Shadow / Base layer - solid color matching hero */}
                       <div className="absolute inset-0 bg-[#E8704A] rounded-[28px] translate-y-2 translate-x-2 opacity-0 group-hover:opacity-100 group-hover:translate-y-3 group-hover:translate-x-3 transition-all duration-300"></div>
                       
                       {/* Top Card layer */}
                       <div className="absolute inset-0 bg-white rounded-[28px] border-[3px] border-[#E8E6DD] group-hover:border-[#E8704A] transition-colors duration-300 flex flex-col justify-between p-6 overflow-hidden z-10">
                          
                          {/* Number Watermark */}
                          <div className="absolute -right-2 -bottom-5 text-[90px] font-['Fredoka'] font-black text-[#F4F1EA] group-hover:text-[#F9B658] transition-colors duration-300 z-0">
                             {item.id}
                          </div>

                          {/* Top Accent Pill (Unifying the top bar to a single brand color style) */}
                          <div className="w-10 h-2 bg-[#E8E6DD] group-hover:bg-[#89B66B] rounded-full transition-colors duration-300 z-10"></div>
                          
                          {/* Title */}
                          <h3 className="font-['Fredoka'] font-bold text-2xl text-[#475569] group-hover:text-[#E8704A] leading-tight z-10 w-[80%] relative">
                             {item.title}
                          </h3>
                       </div>
                    </a>"""

new_cards = """<a key={idx} href={`#${item.anchor}`} className="group relative w-full max-w-[280px] h-[180px] block">
                       {/* Shadow / Base layer - solid color matching banner */}
                       <div className="absolute inset-0 bg-[#F9B658] rounded-[28px] translate-y-2 translate-x-2 opacity-0 group-hover:opacity-100 group-hover:translate-y-3 group-hover:translate-x-3 transition-all duration-300 border-[3px] border-[#222]"></div>
                       
                       {/* Top Card layer */}
                       <div className="absolute inset-0 bg-white rounded-[28px] border-[3px] border-[#E8E6DD] group-hover:border-[#222] transition-colors duration-300 flex flex-col justify-between p-6 overflow-hidden z-10">
                          
                          {/* Number Watermark (Fixed position to avoid cut-off) */}
                          <div className="absolute right-4 bottom-2 text-[65px] font-['Fredoka'] font-black text-[#F0EFE6] group-hover:text-[#F9B658] transition-colors duration-300 z-0 leading-none">
                             {item.id}
                          </div>

                          {/* Top Accent Pill */}
                          <div className="w-10 h-2 bg-[#E8E6DD] group-hover:bg-[#222] rounded-full transition-colors duration-300 z-10"></div>
                          
                          {/* Title */}
                          <h3 className="font-['Fredoka'] font-bold text-2xl text-[#475569] group-hover:text-[#222] leading-tight z-10 w-[80%] relative">
                             {item.title}
                          </h3>
                       </div>
                    </a>"""
content = content.replace(old_cards, new_cards)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("SUCCESS")
