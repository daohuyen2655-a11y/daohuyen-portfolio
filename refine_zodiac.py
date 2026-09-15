import re
import os

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace the entire ZODIAC section again. 
# It starts at {/* ─── 07. ZODIAC ─── */} and ends at {/* ─── 08. PAINTASO ─── */}

start_marker = "{/* ─── 07. ZODIAC ─── */}"
end_marker = "{/* ─── 08. PAINTASO ─── */}"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

# I need the js_array_str again, but since it's already in the file, I can just generate the JSX part that loops over `zodiacCollections`.
# Wait, in the previous script, I directly injected the `js_array_str` into the mapping: `{[...].map(...) }`.
# Let's extract it or rebuild it. It's safer to just rebuild it so I don't rely on parsing the file.

import unicodedata

def contains_cu(path):
    norm = unicodedata.normalize('NFC', path).upper()
    return 'CŨ' in norm

base_dir = "public/assets/portfolio_assets/ZODIAC COLLECTIONS"
collections = [f for f in os.listdir(base_dir) if f.startswith('M') or f.startswith('m')]
def get_num(name):
    nums = re.findall(r'\d+', name)
    return int(nums[0]) if nums else 0
collections.sort(key=get_num)

zodiac_data = []
for coll in collections:
    coll_path = os.path.join(base_dir, coll)
    if not os.path.isdir(coll_path): continue
    images = []
    for root, dirs, files in os.walk(coll_path):
        for f in files:
            if f.lower().endswith(('.png', '.jpg', '.jpeg')):
                full_path = os.path.join(root, f)
                if contains_cu(full_path): continue
                rel_path = full_path.replace("public/", "/")
                images.append(rel_path)
    if images:
        images.sort()
        zodiac_data.append((coll, images))

js_array_str = "[\n"
for coll, imgs in zodiac_data:
    imgs_str = ", ".join([f'"{img}"' for img in imgs])
    js_array_str += f'    {{ title: "{coll.upper()}", images: [{imgs_str}] }},\n'
js_array_str += "  ]"

new_zodiac = f"""{{/* ─── 07. ZODIAC ─── */}}
        <section id="zodiac" className="relative w-full py-32 bg-gradient-to-b from-[#EAEBF2] to-[#D4D7EB] overflow-hidden">
           <div className="max-w-[1400px] mx-auto relative z-20 flex flex-col items-center">
              
              {{/* SECTION HEADER */}}
              <div className="flex flex-col items-center mb-10 text-center px-6">
                  <div className="bg-white/90 px-8 py-3 rounded-full font-bold text-[#2C3E50] border-[4px] border-white shadow-md rotate-[-1deg] text-xl mb-6 uppercase font-['Quicksand'] tracking-widest">
                      07. Zodiac Collections
                  </div>
                  <h2 className="font-['Fredoka'] text-[60px] md:text-[90px] text-[#2C3E50] leading-none mb-6 text-center" style={{{{ textShadow: '4px 4px 0px #FFF' }}}}>
                      ZODIAC
                  </h2>
                  <p className="max-w-2xl text-base text-[#546E7A] font-['Quicksand'] font-bold leading-relaxed bg-white/60 px-8 py-4 rounded-2xl shadow-sm">
                      A premium visual identity designed for Zodiac Collection. 
                      The signature circular emblem masterfully combines half sun and half moon, symbolizing the harmonious cycle of a full day.
                  </p>
              </div>

              {{/* INTERACTIVE PAPER STACK - ELEGANTE */}}
              <div className="relative w-full max-w-[1100px] h-[650px] md:h-[800px] mx-auto mt-4 perspective-[1200px]">
                  {{{js_array_str}.map((page, idx) => {{
                      let diff = idx - activeZodiacPage;
                      
                      let translateX = "0px";
                      let translateY = "0px";
                      let rotate = "0deg";
                      let opacity = 1;
                      let zIndex = 20 - idx;
                      let pointerEvents = "auto";
                      let scale = 1;
                      
                      if (diff < 0) {{
                          // Swiped away (top left)
                          translateX = "-120%";
                          translateY = "-80%";
                          rotate = "-20deg";
                          opacity = 0;
                          pointerEvents = "none";
                          scale = 0.8;
                      }} else if (diff === 0) {{
                          // Active Top Page
                          translateX = "0px";
                          translateY = "0px";
                          rotate = "0deg";
                          zIndex = 30;
                      }} else {{
                          // Stacked underneath (offset to bottom right)
                          translateX = `${{diff * 25}}px`;
                          translateY = `${{diff * 25}}px`;
                          rotate = `${{diff * 1.5}}deg`;
                          zIndex = 20 - diff;
                          scale = 1 - (diff * 0.02);
                          opacity = 1 - (diff * 0.05); 
                      }}

                      return (
                          <div 
                              key={{idx}}
                              className="absolute inset-0 bg-[#FAFAFA] rounded-[24px] border border-[#E0E0E0] p-8 md:p-14 transition-all duration-[800ms] ease-[cubic-bezier(0.25,1,0.5,1)] overflow-hidden flex flex-col shadow-[0_20px_50px_rgba(44,62,80,0.15)]"
                              style={{{{
                                  transform: `translate(${{translateX}}, ${{translateY}}) rotate(${{rotate}}) scale(${{scale}})`,
                                  opacity: opacity,
                                  zIndex: zIndex,
                                  pointerEvents: pointerEvents as any
                              }}}}
                          >
                              {{/* Elegant Header inside Card */}}
                              <div className="w-full flex justify-between items-end mb-8 border-b border-[#E0E0E0] pb-4 shrink-0">
                                  <h3 className="font-['Fredoka'] font-semibold text-3xl md:text-4xl text-[#2C3E50] tracking-wide">
                                      {{page.title}}
                                  </h3>
                                  <button 
                                      onClick={{() => setActiveZodiacPage(prev => (prev + 1) % 5)}}
                                      className="group flex items-center gap-2 font-['Quicksand'] font-bold text-[#546E7A] hover:text-[#2C3E50] transition-colors cursor-pointer text-sm md:text-base bg-[#F0F2F5] px-5 py-2 rounded-full"
                                  >
                                      Next Page 
                                      <span className="group-hover:translate-x-1 transition-transform">→</span>
                                  </button>
                              </div>
                              
                              {{/* Invisible Scrollbar Content */}}
                              <div className="flex-1 overflow-y-auto [&::-webkit-scrollbar]:hidden [-ms-overflow-style:none] [scrollbar-width:none] w-full">
                                  <div className="columns-1 sm:columns-2 md:columns-3 gap-8 pb-10">
                                      {{page.images.map((img, i) => (
                                          <div key={{i}} className="relative rounded-[16px] overflow-hidden border-[3px] border-white shadow-[0_8px_20px_rgba(0,0,0,0.06)] mb-8 break-inside-avoid bg-white group cursor-pointer hover:shadow-[0_15px_30px_rgba(0,0,0,0.12)] transition-shadow duration-500">
                                              <img src={{img}} alt="Zodiac Collection" className="w-full h-auto block group-hover:scale-[1.03] transition-transform duration-700" loading="lazy" />
                                          </div>
                                      ))}}
                                  </div>
                              </div>
                          </div>
                      );
                  }})}}
              </div>
           </div>
        </section>

        """

content = content[:start_idx] + new_zodiac + content[end_idx:]

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS")
