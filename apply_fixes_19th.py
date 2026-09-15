import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. White blur shadows for Titles
old_gen20 = """<h2 className="font-['Fredoka'] text-[50px] md:text-[80px] font-black text-transparent bg-clip-text bg-gradient-to-b from-[#A1C97A] to-[#2C4424] leading-none mb-6 pb-2" style={{ filter: 'drop-shadow(4px 4px 0px rgba(44,68,36,0.3))' }}>"""
new_gen20 = """<h2 className="font-['Fredoka'] text-[50px] md:text-[80px] font-black text-transparent bg-clip-text bg-gradient-to-b from-[#A1C97A] to-[#2C4424] leading-none mb-6 pb-2" style={{ filter: 'drop-shadow(0px 0px 10px rgba(255,255,255,1))' }}>"""
content = content.replace(old_gen20, new_gen20)

old_19th = """<h2 className="font-['Fredoka'] text-[60px] md:text-[90px] font-black text-transparent bg-clip-text bg-gradient-to-b from-[#D1B3FF] to-[#6B4AA6] leading-none mb-6 pb-2" style={{ filter: 'drop-shadow(4px 4px 0px rgba(107,74,166,0.3))' }}>"""
new_19th = """<h2 className="font-['Fredoka'] text-[60px] md:text-[90px] font-black text-transparent bg-clip-text bg-gradient-to-b from-[#D1B3FF] to-[#6B4AA6] leading-none mb-6 pb-2" style={{ filter: 'drop-shadow(0px 0px 12px rgba(255,255,255,1))' }}>"""
content = content.replace(old_19th, new_19th)

# 2. Translate subtext
old_sub = """"Vân Hạ Diệp Mộng" - Kỷ niệm 19 năm thành lập Câu lạc bộ Tiếng Trung Trường Đại học Ngoại thương (CC FTU)."""
new_sub = """"Vân Hạ Diệp Mộng" - Celebrating the 19th Anniversary of the Chinese Club - Foreign Trade University (CC FTU)."""
content = content.replace(old_sub, new_sub)

# 3. Update Event Applications (19th Birthday)
start_marker = """<div className="columns-1 md:columns-2 gap-8 w-full max-w-5xl mx-auto">\n                      {[\n                          "BACKDROP tím.png", \n                          "FRAME tím.png", \n                          "Social story.png", \n                          "cover mail tím.png"\n                      ].map((filename, idx) => (\n                          <div key={idx} className="relative rounded-[24px] overflow-hidden border-[6px] border-white group hover:border-[#8665C3] transition-colors duration-300 shadow-lg break-inside-avoid mb-8 inline-block w-full">\n                              <img src={`/assets/portfolio_assets/CC FTU/CC FTU 19th Anniversary/Print & Event Applications/${filename}`} alt={filename.replace('.png', '')} className="w-full h-auto block group-hover:scale-105 transition-transform duration-500" />\n                          </div>\n                      ))}\n                  </div>"""

new_event_apps = """<div className="columns-1 md:columns-2 gap-8 w-full max-w-5xl mx-auto">
                      {[
                          { file: "FRAME tím.png", name: "Avatar Frame" },
                          { file: "BACKDROP tím.png", name: "Event Backdrop" },
                          { file: "Social story.png", name: "Social Media Story" }
                      ].map((item, idx) => (
                          <div key={idx} className="break-inside-avoid mb-10 inline-block w-full flex flex-col items-center">
                              <div className="relative rounded-[24px] overflow-hidden border-[6px] border-white group hover:border-[#8665C3] transition-colors duration-300 shadow-lg w-full mb-4">
                                  <img src={`/assets/portfolio_assets/CC FTU/CC FTU 19th Anniversary/Print & Event Applications/${item.file}`} alt={item.name} className="w-full h-auto block group-hover:scale-105 transition-transform duration-500" />
                              </div>
                              <h4 className="font-['Quicksand'] font-bold text-lg text-[#8665C3] tracking-wider uppercase text-center bg-white/60 px-6 py-2 rounded-full shadow-sm">{item.name}</h4>
                          </div>
                      ))}
                  </div>"""
content = content.replace(start_marker, new_event_apps)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("SUCCESS")
