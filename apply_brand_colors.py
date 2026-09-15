import re
import os
import unicodedata

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = "{/* ─── 07. ZODIAC ─── */}"
end_marker = "{/* ─── 08. PAINTASO ─── */}"
start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

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
        <section id="zodiac" className="relative w-full py-32 bg-gradient-to-b from-[#FEF5F5] to-[#E6E6E6] overflow-hidden">
           
           {{/* Subtle Grain for Premium Feel */}}
           <div className="absolute inset-0 opacity-[0.03] pointer-events-none" style={{{{ backgroundImage: 'url("data:image/svg+xml,%3Csvg viewBox=\\'0 0 200 200\\' xmlns=\\'http://www.w3.org/2000/svg\\'%3E%3Cfilter id=\\'noiseFilter\\'%3E%3CfeTurbulence type=\\'fractalNoise\\' baseFrequency=\\'0.8\\' numOctaves=\\'3\\' stitchTiles=\\'stitch\\'/%3E%3C/filter%3E%3Crect width=\\'100%25\\' height=\\'100%25\\' filter=\\'url(%23noiseFilter)\\'/%3E%3C/svg%3E")' }}}}></div>

           <div className="max-w-[1400px] mx-auto relative z-20 flex flex-col items-center">
              
              {{/* SECTION HEADER */}}
              <div className="flex flex-col items-center mb-16 text-center px-6">
                  <div className="bg-[#0B0B0B] px-8 py-2 rounded-full font-bold text-[#FEF5F5] shadow-xl text-sm md:text-base mb-6 uppercase font-['Quicksand'] tracking-[0.3em]">
                      07. Zodiac Collections
                  </div>
                  
                  {{/* Pure Brand Typography */}}
                  <h2 className="font-['Fredoka'] text-[70px] md:text-[110px] text-[#0B0B0B] leading-none mb-8 text-center" 
                      style={{{{ filter: 'drop-shadow(3px 3px 0px rgba(255,255,255,1)) drop-shadow(8px 8px 15px rgba(0,0,0,0.1))' }}}}>
                      ZODIAC
                  </h2>
                  
                  <p className="max-w-2xl text-base md:text-lg text-[#333333] font-['Quicksand'] font-semibold leading-relaxed px-4">
                      A premium visual identity designed for Zodiac Collection. 
                      The signature circular emblem masterfully combines half sun and half moon, symbolizing the harmonious cycle of a full day.
                  </p>
              </div>

              {{/* INTERACTIVE PAPER STACK - LUXURY JET BLACK BOARDS */}}
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
                          translateX = `${{diff * 20}}px`;
                          translateY = `${{diff * 20}}px`;
                          rotate = `${{diff * 1.5}}deg`;
                          zIndex = 20 - diff;
                          scale = 1 - (diff * 0.02);
                          opacity = 1 - (diff * 0.05); 
                      }}

                      return (
                          <div 
                              key={{idx}}
                              className="absolute inset-0 bg-[#0B0B0B] rounded-[32px] border border-[#222222] p-8 md:p-12 transition-all duration-[800ms] ease-[cubic-bezier(0.25,1,0.5,1)] overflow-hidden flex flex-col shadow-[0_30px_60px_rgba(0,0,0,0.4)]"
                              style={{{{
                                  transform: `translate(${{translateX}}, ${{translateY}}) rotate(${{rotate}}) scale(${{scale}})`,
                                  opacity: opacity,
                                  zIndex: zIndex,
                                  pointerEvents: pointerEvents as any
                              }}}}
                          >
                              {{/* Elegant Header inside Card */}}
                              <div className="w-full flex justify-between items-center mb-8 border-b border-white/10 pb-6 shrink-0">
                                  <h3 className="font-['Fredoka'] font-semibold text-3xl md:text-5xl text-[#FEF5F5] tracking-wider drop-shadow-md">
                                      {{page.title}}
                                  </h3>
                                  <button 
                                      onClick={{() => setActiveZodiacPage(prev => (prev + 1) % 5)}}
                                      className="group flex items-center gap-3 font-['Quicksand'] font-bold text-[#0B0B0B] bg-[#FEF5F5] hover:bg-white transition-colors cursor-pointer text-sm md:text-base px-6 py-3 rounded-full shadow-lg"
                                  >
                                      NEXT <span className="group-hover:translate-x-1 transition-transform">➔</span>
                                  </button>
                              </div>
                              
                              {{/* Invisible Scrollbar Content */}}
                              <div className="flex-1 overflow-y-auto [&::-webkit-scrollbar]:hidden [-ms-overflow-style:none] [scrollbar-width:none] w-full px-2">
                                  <div className="columns-1 sm:columns-2 md:columns-3 gap-8 pb-10">
                                      {{page.images.map((img, i) => (
                                          <div key={{i}} className="relative rounded-[16px] overflow-hidden border border-white/10 shadow-[0_10px_30px_rgba(0,0,0,0.6)] mb-8 break-inside-avoid bg-white group cursor-pointer hover:shadow-[0_20px_50px_rgba(255,255,255,0.1)] transition-shadow duration-500 hover:-translate-y-1">
                                              <img src={{img}} alt="Zodiac Collection" className="w-full h-auto block group-hover:scale-105 transition-transform duration-700" loading="lazy" />
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
