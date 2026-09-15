import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new TOC section
new_toc = """
        {/* ─── TABLE OF CONTENTS ─── */}
        <section id="toc" className="relative w-full pb-32 bg-[#F6F4EB] overflow-hidden pt-16 md:pt-20">
           {/* Background Textures */}
           <div className="absolute inset-0 noise-overlay opacity-[0.15] pointer-events-none z-0"></div>
           <div className="absolute inset-0 bg-halftone-large opacity-[0.03] pointer-events-none z-0"></div>
           
           <div className="max-w-[1200px] mx-auto px-6 relative z-20">
              
              <div className="flex flex-col items-center mb-24">
                 <div className="relative group">
                    <h2 className="text-[70px] md:text-[100px] font-['Fredoka'] font-black text-[#6C8558] rotate-[-2deg] transition-transform duration-500 group-hover:scale-105" style={{ textShadow: '-3px -3px 0 #FFF, 3px -3px 0 #FFF, -3px 3px 0 #FFF, 3px 3px 0 #FFF, 5px 5px 0px rgba(108,133,88,0.3)' }}>
                       Table of Contents
                    </h2>
                 </div>
              </div>

              {/* Grid 4 Columns */}
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-10 w-full justify-items-center">
                 {[
                    { id: "01", title: "Yapsu AI", link: "yapsu-ai", color: "group-hover:text-[#6BA5D7]", border: "group-hover:border-[#6BA5D7]", tapeColor: "bg-[#6BA5D7]", shadow: "rgba(107,165,215,0.5)" },
                    { id: "02", title: "Chinese\nDebate '26", link: "chinese-debate-26", color: "group-hover:text-[#00C2CC]", border: "group-hover:border-[#00C2CC]", tapeColor: "bg-[#00C2CC]", shadow: "rgba(0,194,204,0.5)" },
                    { id: "03", title: "Gen 20th\nRecruit", link: "gen-20-recruit", color: "group-hover:text-[#3B5B35]", border: "group-hover:border-[#3B5B35]", tapeColor: "bg-[#3B5B35]", shadow: "rgba(59,91,53,0.5)" },
                    { id: "04", title: "19th\nBirthday", link: "19th-birthday", color: "group-hover:text-[#A890D8]", border: "group-hover:border-[#A890D8]", tapeColor: "bg-[#A890D8]", shadow: "rgba(168,144,216,0.5)" },
                    { id: "05", title: "Chinese\nDebate '25", link: "chinese-debate-25", color: "group-hover:text-[#D4AF37]", border: "group-hover:border-[#D4AF37]", tapeColor: "bg-[#D4AF37]", shadow: "rgba(212,175,55,0.5)" },
                    { id: "06", title: "Talkshow", link: "talkshow", color: "group-hover:text-[#58B3D3]", border: "group-hover:border-[#58B3D3]", tapeColor: "bg-[#58B3D3]", shadow: "rgba(88,179,211,0.5)" },
                    { id: "07", title: "Zodiac", link: "zodiac", color: "group-hover:text-[#2C3E50]", border: "group-hover:border-[#2C3E50]", tapeColor: "bg-[#2C3E50]", shadow: "rgba(44,62,80,0.5)" },
                    { id: "08", title: "Paintaso", link: "paintaso", color: "group-hover:text-[#E53935]", border: "group-hover:border-[#E53935]", tapeColor: "bg-[#E53935]", shadow: "rgba(229,57,53,0.5)" }
                 ].map((item, i) => (
                    <a href={`#${item.link}`} key={item.id} className={`relative group cursor-pointer block transition-all duration-300 hover:-translate-y-4 hover:scale-105 z-10 hover:z-20 w-full max-w-[260px]`} style={{ transform: `rotate(${i%2==0 ? 2 : -2}deg)` }}>
                       <div className={`w-full aspect-square bg-[#FDFBF7] rounded-[24px] border-[6px] border-white shadow-[8px_8px_0px_rgba(92,74,61,0.15)] group-hover:shadow-[14px_14px_0px_rgba(92,74,61,0.25)] ${item.border} p-8 flex flex-col justify-between transition-all duration-300`}>
                          <div className="absolute inset-0 noise-overlay opacity-10 rounded-[18px]"></div>
                          <span className={`font-['Fredoka'] text-6xl font-black text-[#E8E2D5] transition-colors ${item.color}`}>{item.id}</span>
                          <h3 className={`font-['Fredoka'] text-3xl font-bold text-[#5C4A3D] leading-tight group-hover:text-[#333] whitespace-pre-line`}>
                             {item.title}
                          </h3>
                       </div>
                       
                       {/* Tape/Sticker */}
                       <div className={`absolute top-[-15px] left-1/2 -translate-x-1/2 w-[60px] h-[25px] ${item.tapeColor} border-[3px] border-white rotate-[${i%2==0 ? -4 : 4}deg] shadow-[4px_4px_0px_${item.shadow}] rounded-sm z-10 transition-transform duration-300 group-hover:rotate-[${i%2==0 ? 4 : -4}deg]`}></div>
                    </a>
                 ))}
              </div>
           </div>
        </section>"""

# We need to replace everything from <section id="toc" to the end of </section> before {/* ─── 01. YAPSU AI ─── */}
pattern = re.compile(r'<section id="toc".*?</section>', re.DOTALL)
content = re.sub(pattern, new_toc, content)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
