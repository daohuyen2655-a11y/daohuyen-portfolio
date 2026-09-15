import os
import re
import unicodedata

def contains_cu(path):
    norm = unicodedata.normalize('NFC', path).upper()
    return 'CŨ' in norm

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
                
                # Exclude old logos ("CŨ")
                if contains_cu(full_path):
                    continue
                    
                rel_path = full_path.replace("public/", "/")
                name = f.replace('.png', '').replace('.jpg', '').replace('.jpeg', '').upper()
                images.append((rel_path, name))
    
    if not images:
        continue
        
    images.sort(key=lambda x: x[0])
    
    images_jsx = ""
    for img_path, img_name in images:
        images_jsx += f"""
                          <div className="snap-center shrink-0 w-[85vw] md:w-[45vw] lg:w-[35vw] flex flex-col items-center group">
                              <div className="w-full aspect-square md:aspect-[4/5] flex items-center justify-center bg-[#111111] border border-[#333333] p-8 md:p-12 overflow-hidden relative">
                                  {{/* Subtle background glow */}}
                                  <div className="absolute inset-0 bg-gradient-to-tr from-transparent via-[#222222] to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-1000"></div>
                                  <img src="{img_path}" alt="{img_name}" className="max-w-full max-h-full object-contain filter brightness-90 group-hover:brightness-110 group-hover:scale-105 transition-all duration-1000 ease-out relative z-10 drop-shadow-2xl" loading="lazy" />
                              </div>
                              <div className="w-full flex justify-between items-center mt-6 px-2">
                                  <p className="font-serif italic text-[#888888] text-sm tracking-[0.2em]">{coll.upper()}</p>
                                  <p className="font-sans text-[#DDDDDD] text-xs tracking-widest uppercase">{img_name}</p>
                              </div>
                          </div>"""
    
    block = f"""
              {{/* {coll.upper()} */}}
              <div className="w-full mb-32 flex flex-col">
                  <div className="flex items-center gap-6 mb-16 px-6 sm:px-10">
                      <h3 className="font-serif italic tracking-[0.3em] text-2xl md:text-3xl text-[#E5E0D8] uppercase">
                          {coll}
                      </h3>
                      <div className="h-[1px] bg-[#333333] flex-grow"></div>
                  </div>
                  
                  {{/* Horizontal Scroll Lookbook */}}
                  <div className="flex overflow-x-auto gap-8 md:gap-16 pb-12 px-6 sm:px-10 snap-x snap-mandatory [&::-webkit-scrollbar]:hidden [-ms-overflow-style:none] [scrollbar-width:none] items-center cursor-grab active:cursor-grabbing">
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
        <section id="zodiac" className="relative w-full py-32 bg-[#050505] overflow-hidden">
           
           {{/* Subtle Noise for Luxury Texture - VERY low opacity to avoid lag */}}
           <div className="absolute inset-0 opacity-[0.02] pointer-events-none" style={{{{ backgroundImage: 'url("data:image/svg+xml,%3Csvg viewBox=\\'0 0 200 200\\' xmlns=\\'http://www.w3.org/2000/svg\\'%3E%3Cfilter id=\\'noiseFilter\\'%3E%3CfeTurbulence type=\\'fractalNoise\\' baseFrequency=\\'0.9\\' numOctaves=\\'3\\' stitchTiles=\\'stitch\\'/%3E%3C/filter%3E%3Crect width=\\'100%25\\' height=\\'100%25\\' filter=\\'url(%23noiseFilter)\\'/%3E%3C/svg%3E")' }}}}></div>

           <div className="max-w-[1600px] mx-auto relative z-20 flex flex-col">
              
              {{/* SECTION HEADER - FASHION EDITORIAL STYLE */}}
              <div className="flex flex-col items-center mb-32 text-center px-6">
                  <p className="font-sans text-[#888888] text-xs md:text-sm tracking-[0.4em] mb-8 uppercase">
                      Fashion & Brand Identity
                  </p>
                  <h2 className="font-serif text-[50px] md:text-[100px] lg:text-[140px] text-[#E5E0D8] leading-none mb-8 tracking-[-0.02em] font-light">
                      ZODIAC
                  </h2>
                  <p className="max-w-2xl text-base md:text-lg text-[#999999] font-serif italic leading-relaxed tracking-wide">
                      A premium visual identity designed for Zodiac Collection. 
                      The signature circular emblem masterfully combines half sun and half moon, symbolizing the harmonious cycle of a full day.
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
