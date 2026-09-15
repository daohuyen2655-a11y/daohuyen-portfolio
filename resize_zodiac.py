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
        <section id="zodiac" className="relative w-full py-32 bg-[#F9F7F3] overflow-hidden">
           
           {{/* Subtle Paper Texture */}}
           <div className="absolute inset-0 opacity-[0.04] pointer-events-none" style={{{{ backgroundImage: 'url("data:image/svg+xml,%3Csvg viewBox=\\'0 0 200 200\\' xmlns=\\'http://www.w3.org/2000/svg\\'%3E%3Cfilter id=\\'noiseFilter\\'%3E%3CfeTurbulence type=\\'fractalNoise\\' baseFrequency=\\'0.85\\' numOctaves=\\'3\\' stitchTiles=\\'stitch\\'/%3E%3C/filter%3E%3Crect width=\\'100%25\\' height=\\'100%25\\' filter=\\'url(%23noiseFilter)\\'/%3E%3C/svg%3E")' }}}}></div>

           <div className="max-w-[1400px] mx-auto relative z-20 flex flex-col items-center">
              
              {{/* SECTION HEADER */}}
              <div className="flex flex-col items-center mb-12 text-center px-6">
                  {{/* Standardized Branding Pill */}}
                  <div className="px-8 py-2 border-[3px] border-[#8C8377] text-[#8C8377] rounded-full text-sm font-bold mb-6 tracking-widest uppercase bg-transparent shadow-[0_0_15px_rgba(140,131,119,0.1)] font-['Quicksand']">
                      Branding
                  </div>
                  
                  {{/* Elegant Typography */}}
                  <h2 className="font-serif text-[60px] md:text-[90px] text-[#2C2822] leading-none mb-6 text-center font-light tracking-[0.1em]">
                      ZODIAC
                  </h2>
                  
                  {{/* Controlled 2-Line Subtext */}}
                  <p className="max-w-4xl text-base md:text-lg text-[#736B60] font-serif italic font-normal leading-loose px-4">
                      A premium visual identity designed for Zodiac Collections.<br className="hidden md:block" /> 
                      The signature circular emblem masterfully combines half sun and half moon, symbolizing the harmonious cycle of a full day.
                  </p>
              </div>

              {{/* INTERACTIVE PAPER STACK - COMPACT SIZE */}}
              <div className="relative w-full max-w-[850px] h-[550px] md:h-[600px] mx-auto mt-4 perspective-[1200px]">
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
                          rotate = "-15deg";
                          opacity = 0;
                          pointerEvents = "none";
                          scale = 0.85;
                      }} else if (diff === 0) {{
                          // Active Top Page
                          translateX = "0px";
                          translateY = "0px";
                          rotate = "0deg";
                          zIndex = 30;
                      }} else {{
                          // Stacked underneath (offset to bottom right, much tighter now)
                          translateX = `${{diff * 12}}px`;
                          translateY = `${{diff * 12}}px`;
                          rotate = `${{diff * 1}}deg`;
                          zIndex = 20 - diff;
                          scale = 1 - (diff * 0.02);
                          opacity = 1 - (diff * 0.08); 
                      }}

                      return (
                          <div 
                              key={{idx}}
                              className="absolute inset-0 bg-[#FDFCF9] rounded-[20px] border border-[#EBE6DD] p-6 md:p-10 transition-all duration-[900ms] ease-[cubic-bezier(0.25,1,0.5,1)] overflow-hidden flex flex-col shadow-[0_15px_40px_rgba(90,80,70,0.06)]"
                              style={{{{
                                  transform: `translate(${{translateX}}, ${{translateY}}) rotate(${{rotate}}) scale(${{scale}})`,
                                  opacity: opacity,
                                  zIndex: zIndex,
                                  pointerEvents: pointerEvents as any
                              }}}}
                          >
                              {{/* Elegant Header inside Card */}}
                              <div className="w-full flex justify-between items-center mb-6 border-b border-[#EBE6DD] pb-4 shrink-0">
                                  <h3 className="font-serif italic text-2xl md:text-3xl text-[#2C2822] tracking-widest">
                                      {{page.title}}
                                  </h3>
                                  <button 
                                      onClick={{() => setActiveZodiacPage(prev => (prev + 1) % 5)}}
                                      className="group flex items-center gap-2 font-sans font-light tracking-widest text-[#8C8377] hover:text-[#2C2822] transition-colors cursor-pointer text-xs md:text-sm px-4 py-2 uppercase"
                                  >
                                      NEXT <span className="group-hover:translate-x-1 transition-transform">➔</span>
                                  </button>
                              </div>
                              
                              {{/* Invisible Scrollbar Content */}}
                              <div className="flex-1 overflow-y-auto [&::-webkit-scrollbar]:hidden [-ms-overflow-style:none] [scrollbar-width:none] w-full px-2">
                                  <div className="columns-1 sm:columns-2 gap-6 pb-6">
                                      {{page.images.map((img, i) => (
                                          <div key={{i}} className="relative rounded-[12px] overflow-hidden border border-[#F2EFEA] shadow-[0_4px_15px_rgba(0,0,0,0.03)] mb-6 break-inside-avoid bg-white">
                                              <img src={{img}} alt="Zodiac Collection" className="w-full h-auto block" loading="lazy" />
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
