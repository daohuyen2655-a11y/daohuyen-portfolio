import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = "{/* ─── 07. ZODIAC ─── */}"
end_marker = "{/* ─── 08. PAINTASO ─── */}"
start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    zodiac_section = content[start_idx:end_idx]
    
    old_content_block = """{/* Invisible Scrollbar Content - GRID INSTEAD OF COLUMNS FOR STRICT ROWS */}
                              <div className="flex-1 overflow-y-auto [&::-webkit-scrollbar]:hidden [-ms-overflow-style:none] [scrollbar-width:none] w-full flex justify-center">
                                  <div className="w-full max-w-4xl flex flex-wrap justify-center gap-6 md:gap-10 pb-10">
                                      {page.images.map((img, i) => (
                                          <div key={i} className="relative rounded-[8px] overflow-hidden border border-[#F2EFEA] shadow-[0_4px_15px_rgba(0,0,0,0.04)] bg-white w-full sm:w-[calc(50%-12px)] md:w-[calc(33.333%-27px)]">
                                              <img src={img} alt="Zodiac Collection" className="w-full h-auto block" loading="lazy" />
                                          </div>
                                      ))}
                                  </div>
                              </div>"""

    new_content_block = """{/* Invisible Scrollbar Content */}
                              <div className="flex-1 overflow-y-auto [&::-webkit-scrollbar]:hidden [-ms-overflow-style:none] [scrollbar-width:none] w-full px-2">
                                  {(page.title === "MÁC 1" || page.title === "MÁC 3") ? (
                                      <div className="w-full max-w-4xl mx-auto flex flex-wrap justify-center gap-6 md:gap-10 pb-10">
                                          {page.images.map((img, i) => (
                                              <div key={i} className="relative rounded-[12px] overflow-hidden border border-[#F2EFEA] shadow-[0_4px_15px_rgba(0,0,0,0.03)] bg-white w-full sm:w-[calc(50%-12px)] md:w-[calc(33.333%-27px)]">
                                                  <img src={img} alt="Zodiac Collection" className="w-full h-auto block" loading="lazy" />
                                              </div>
                                          ))}
                                      </div>
                                  ) : (
                                      <div className="columns-1 sm:columns-2 md:columns-3 gap-8 pb-10">
                                          {page.images.map((img, i) => (
                                              <div key={i} className="relative rounded-[12px] overflow-hidden border border-[#F2EFEA] shadow-[0_4px_15px_rgba(0,0,0,0.03)] mb-8 break-inside-avoid bg-white">
                                                  <img src={img} alt="Zodiac Collection" className="w-full h-auto block" loading="lazy" />
                                              </div>
                                          ))}
                                      </div>
                                  )}
                              </div>"""
                              
    if old_content_block in zodiac_section:
        zodiac_section = zodiac_section.replace(old_content_block, new_content_block)
        content = content[:start_idx] + zodiac_section + content[end_idx:]
        with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
            f.write(content)
        print("SUCCESS")
    else:
        print("FAILED: old block not found")
else:
    print("FAILED: markers not found")
