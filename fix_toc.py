import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the TOC Title
old_title = """<h2 className="text-[70px] md:text-[100px] font-['Fredoka'] font-black text-[#6C8558] rotate-[-2deg] transition-transform duration-500 group-hover:scale-105" style={{ textShadow: '-3px -3px 0 #FFF, 3px -3px 0 #FFF, -3px 3px 0 #FFF, 3px 3px 0 #FFF, 5px 5px 0px rgba(108,133,88,0.3)' }}>
                       Table of Contents
                    </h2>"""

new_title = """<h2 className="text-[70px] md:text-[100px] font-['Fredoka'] font-black text-[#E8704A] rotate-[-2deg] transition-transform duration-500 group-hover:scale-105" style={{ textShadow: '-4px -4px 0 #FFF, 4px -4px 0 #FFF, -4px 4px 0 #FFF, 4px 4px 0 #FFF, 8px 8px 0px rgba(232,112,74,0.2)' }}>
                       Table of Contents
                    </h2>"""

content = content.replace(old_title, new_title)

# 2. Update the TOC Cards Design
old_cards = """<a key={idx} href={`#${item.anchor}`} className="group relative w-full max-w-[280px]">
                       <div className="w-full aspect-[4/3] bg-white rounded-[24px] shadow-sm group-hover:shadow-[8px_8px_0px_rgba(0,0,0,0.1)] transition-all duration-300 border-[3px] border-white group-hover:-translate-y-2 flex flex-col p-6 relative z-10 overflow-hidden">
                          <div className="absolute top-0 left-1/2 -translate-x-1/2 w-12 h-3 opacity-80 rounded-b-md" style={{ backgroundColor: item.color }}></div>
                          <span className="font-['Fredoka'] font-black text-5xl opacity-20 mt-4 group-hover:opacity-40 transition-opacity" style={{ color: item.color }}>{item.id}</span>
                          <h3 className="font-['Fredoka'] font-bold text-2xl text-[#333] mt-auto leading-tight">{item.title}</h3>
                       </div>
                       <div className="absolute inset-0 bg-[#E0DCC8] rounded-[24px] translate-y-3 translate-x-3 z-0 group-hover:translate-y-4 group-hover:translate-x-4 transition-transform"></div>
                    </a>"""

new_cards = """<a key={idx} href={`#${item.anchor}`} className="group relative w-full max-w-[280px] h-[180px] block">
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

content = content.replace(old_cards, new_cards)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("SUCCESS")
