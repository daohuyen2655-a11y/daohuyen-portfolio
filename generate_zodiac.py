import os
import re

base_dir = "public/assets/portfolio_assets/ZODIAC COLLECTIONS"
collections = [f for f in os.listdir(base_dir) if f.startswith('M') or f.startswith('m')]
collections.sort() 

jsx_blocks = []

for coll in collections:
    coll_path = os.path.join(base_dir, coll)
    if not os.path.isdir(coll_path):
        continue
    
    images = []
    for root, dirs, files in os.walk(coll_path):
        for f in files:
            if f.lower().endswith(('.png', '.jpg', '.jpeg')):
                full_path = os.path.join(root, f)
                rel_path = full_path.replace("public/", "/")
                images.append(rel_path)
    
    if not images:
        continue
        
    images.sort()
    
    images_jsx = ""
    for img in images:
        images_jsx += f"""
                          <div className="relative rounded-[16px] overflow-hidden border-[4px] border-white shadow-lg group hover:border-[#2C3E50] transition-colors duration-300 break-inside-avoid mb-6 inline-block w-full">
                              <img src="{img}" alt="Zodiac Collection" className="w-full h-auto block group-hover:scale-105 transition-transform duration-500" loading="lazy" />
                          </div>"""
    
    block = f"""
              {{/* {coll.upper()} */}}
              <div className="w-full mb-20 flex flex-col items-center">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#2C3E50] mb-10 tracking-wide bg-white/70 px-8 py-2 rounded-full shadow-sm uppercase">
                      {coll}
                  </h3>
                  <div className="columns-2 md:columns-3 lg:columns-4 gap-6 w-full max-w-[1400px] mx-auto">
                      {images_jsx}
                  </div>
              </div>"""
    jsx_blocks.append(block)

full_zodiac_jsx = "\n".join(jsx_blocks)

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = "{/* ─── 07. ZODIAC ─── */}"
end_marker = "{/* ─── 08. PAINTASO ─── */}"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

new_zodiac = f"""{{/* ─── 07. ZODIAC ─── */}}
        <section id="zodiac" className="relative w-full py-24 bg-gradient-to-b from-[#EAEBF2] to-[#D4D7EB] overflow-hidden">
           <div className="max-w-[1400px] mx-auto px-6 sm:px-10 relative z-20 flex flex-col">
              
              {{/* SECTION HEADER */}}
              <div className="flex flex-col items-center mb-20 text-center">
                  <div className="px-6 py-2 border-[3px] border-[#2C3E50] text-[#2C3E50] rounded-full text-sm font-bold mb-6 tracking-widest uppercase bg-white/60 backdrop-blur-sm shadow-[0_0_15px_rgba(44,62,80,0.1)]">
                      Art & Merchandise
                  </div>
                  <h2 className="font-['Fredoka'] text-[60px] md:text-[90px] font-black text-transparent bg-clip-text bg-gradient-to-b from-[#7F8C8D] to-[#2C3E50] leading-none mb-6 pb-2" style={{ filter: 'drop-shadow(0px 0px 10px rgba(255,255,255,1))' }}>
                      Zodiac Collections
                  </h2>
                  <p className="max-w-2xl text-lg text-[#34495E] font-['Quicksand'] font-bold leading-relaxed">
                      A unique artistic exploration combining the twelve zodiac signs with striking visual elements, featuring both classic and modernized logo adaptations.
                  </p>
              </div>

              {full_zodiac_jsx}
              
           </div>
        </section>

        """

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_zodiac + content[end_idx:]
    with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS")
else:
    print("FAILED TO FIND MARKERS")
