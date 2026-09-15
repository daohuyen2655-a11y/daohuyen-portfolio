import os
import re
import unicodedata

def contains_cu(path):
    norm = unicodedata.normalize('NFC', path).upper()
    return 'CŨ' in norm

base_dir = "public/assets/portfolio_assets/ZODIAC COLLECTIONS"
collections = [f for f in os.listdir(base_dir) if f.startswith('M') or f.startswith('m')]

# Sort correctly by extracting the number
def get_num(name):
    nums = re.findall(r'\d+', name)
    return int(nums[0]) if nums else 0

collections.sort(key=get_num)

zodiac_data = []

for coll in collections:
    coll_path = os.path.join(base_dir, coll)
    if not os.path.isdir(coll_path):
        continue
    
    images = []
    for root, dirs, files in os.walk(coll_path):
        for f in files:
            if f.lower().endswith(('.png', '.jpg', '.jpeg')):
                full_path = os.path.join(root, f)
                if contains_cu(full_path):
                    continue
                rel_path = full_path.replace("public/", "/")
                images.append(rel_path)
    
    if not images:
        continue
        
    images.sort()
    zodiac_data.append((coll, images))

# Create the JS array string
js_array_str = "[\n"
for coll, imgs in zodiac_data:
    imgs_str = ", ".join([f'"{img}"' for img in imgs])
    js_array_str += f'    {{ title: "{coll.upper()}", images: [{imgs_str}] }},\n'
js_array_str += "  ]"


with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Add the state if it doesn't exist
state_marker = "const [activeDebateIdx, setActiveDebateIdx] = useState(0);"
if "const [activeZodiacPage, setActiveZodiacPage] = useState(0);" not in content:
    new_state = state_marker + "\n  const [activeZodiacPage, setActiveZodiacPage] = useState(0);"
    content = content.replace(state_marker, new_state)

start_marker = "{/* ─── 07. ZODIAC ─── */}"
end_marker = "{/* ─── 08. PAINTASO ─── */}"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

new_zodiac = f"""{{/* ─── 07. ZODIAC ─── */}}
        <section id="zodiac" className="relative w-full py-32 bg-gradient-to-b from-[#EAEBF2] to-[#D4D7EB] overflow-hidden">
           <div className="max-w-[1400px] mx-auto relative z-20 flex flex-col items-center">
              
              {{/* SECTION HEADER */}}
              <div className="flex flex-col items-center mb-16 text-center px-6">
                  <div className="bg-white/90 px-8 py-3 rounded-full font-bold text-[#2C3E50] border-[6px] border-white shadow-lg rotate-[-2deg] text-2xl mb-8 uppercase font-['Quicksand']">
                      07. Zodiac Collections
                  </div>
                  <h2 className="font-['Fredoka'] text-[70px] md:text-[110px] text-white leading-none mb-8 text-center rotate-[1deg]" style={{{{ textShadow: '-3px -3px 0 #FFF, 3px -3px 0 #FFF, -3px 3px 0 #FFF, 3px 3px 0 #FFF, 8px 8px 0px #2C3E50' }}}}>
                      ZODIAC
                  </h2>
                  <p className="max-w-2xl text-lg text-[#34495E] font-['Quicksand'] font-bold leading-relaxed bg-white/50 p-6 rounded-2xl border-4 border-white shadow-sm">
                      A premium visual identity designed for Zodiac Collection. 
                      The signature circular emblem masterfully combines half sun and half moon, symbolizing the harmonious cycle of a full day.
                  </p>
              </div>

              {{/* INTERACTIVE PAPER STACK */}}
              <div className="relative w-full max-w-[1000px] h-[700px] md:h-[900px] mx-auto mt-10 perspective-[1000px]">
                  <div className="absolute top-[-50px] right-0 z-50 animate-bounce">
                      <div className="bg-[#E53935] text-white font-['Fredoka'] font-bold px-6 py-3 rounded-full border-4 border-white shadow-lg cursor-pointer hover:scale-110 transition-transform flex items-center gap-2"
                           onClick={{() => setActiveZodiacPage(prev => (prev + 1) % 5)}}>
                          <span>Click to Flip Page</span>
                          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
                      </div>
                  </div>

                  {{{js_array_str}.map((page, idx) => {{
                      let diff = idx - activeZodiacPage;
                      
                      // Paper Stack Logic
                      let translateX = "0px";
                      let translateY = "0px";
                      let rotate = "0deg";
                      let opacity = 1;
                      let zIndex = 20 - idx;
                      let pointerEvents = "auto";
                      
                      if (diff < 0) {{
                          // Swiped away (top left)
                          translateX = "-150%";
                          translateY = "-100%";
                          rotate = "-15deg";
                          opacity = 0;
                          pointerEvents = "none";
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
                          rotate = `${{diff * 2}}deg`;
                          zIndex = 20 - diff;
                          // Optional: slightly dim pages underneath
                          opacity = 1 - (diff * 0.1); 
                      }}

                      return (
                          <div 
                              key={{idx}}
                              className="absolute inset-0 bg-[#F9F9F9] rounded-[32px] border-[8px] border-white p-8 md:p-12 transition-all duration-700 ease-[cubic-bezier(0.34,1.56,0.64,1)] overflow-hidden"
                              style={{{{
                                  transform: `translate(${{translateX}}, ${{translateY}}) rotate(${{rotate}})`,
                                  opacity: opacity,
                                  zIndex: zIndex,
                                  pointerEvents: pointerEvents as any,
                                  boxShadow: diff >= 0 ? '15px 15px 40px rgba(44, 62, 80, 0.2)' : 'none'
                              }}}}
                          >
                              <div className="w-full h-full flex flex-col">
                                  <h3 className="font-['Fredoka'] font-black text-4xl text-[#2C3E50] mb-8 border-b-4 border-[#2C3E50]/10 pb-4">
                                      {{page.title}}
                                  </h3>
                                  <div className="flex-1 overflow-y-auto pr-4 custom-scrollbar">
                                      <div className="columns-1 sm:columns-2 md:columns-3 gap-6">
                                          {{page.images.map((img, i) => (
                                              <div key={{i}} className="relative rounded-[16px] overflow-hidden border-[4px] border-white shadow-md mb-6 break-inside-avoid bg-white">
                                                  <img src={{img}} alt="Zodiac Collection" className="w-full h-auto block hover:scale-105 transition-transform duration-500" loading="lazy" />
                                              </div>
                                          ))}}
                                      </div>
                                  </div>
                              </div>
                          </div>
                      );
                  }})}}
              </div>
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
