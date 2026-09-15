import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = "{/* ─── 07. ZODIAC ─── */}"
end_marker = "{/* ─── 08. PAINTASO ─── */}"
start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    zodiac_section = content[start_idx:end_idx]
    
    # We replace the entire Invisible Scrollbar Content block
    block_start = zodiac_section.find("{/* UNIFIED SMALL LAYOUT FOR ALL TAGS */}")
    
    if block_start == -1:
        # Fallback if I named it differently in the last script
        block_start = zodiac_section.find("{/* Invisible Scrollbar Content")

    # Find the end of the return statement div
    # It looks like: 
    #       </div>
    #   );
    # }})}
    
    # Let's just do a string replacement of the inner content of the card.
    old_content_block = """{/* UNIFIED SMALL LAYOUT FOR ALL TAGS */}
                              <div className="flex-1 overflow-y-auto [&::-webkit-scrollbar]:hidden [-ms-overflow-style:none] [scrollbar-width:none] w-full px-2">
                                  <div className="w-full max-w-[850px] mx-auto flex flex-wrap justify-center gap-6 md:gap-10 pb-10">
                                      {page.images.map((img, i) => (
                                          <div key={i} className="relative rounded-[12px] overflow-hidden border border-[#F2EFEA] shadow-[0_4px_15px_rgba(0,0,0,0.03)] bg-white w-full sm:w-[calc(50%-12px)] md:w-[calc(33.333%-27px)]">
                                              <img src={img} alt="Zodiac Collection" className="w-full h-auto block" loading="lazy" />
                                          </div>
                                      ))}
                                  </div>
                              </div>"""
                              
    new_content_block = """{/* PRECISE USER LAYOUT */}
                              <div className="flex-1 w-full px-2">
                                  {(page.title === "MÁC 1" || page.title === "MÁC 3") ? (
                                      {/* Mác 1 & 3: 2 Rows, Left-Aligned, Fully Visible (Small size) */}
                                      <div className="w-full flex flex-wrap justify-start gap-4 md:gap-8 pb-4">
                                          {page.images.map((img, i) => (
                                              <div key={i} className="relative rounded-[8px] overflow-hidden border border-[#F2EFEA] shadow-sm bg-white w-[140px] md:w-[220px]">
                                                  <img src={img} alt="Zodiac Collection" className="w-full h-auto block" loading="lazy" />
                                              </div>
                                          ))}
                                      </div>
                                  ) : (
                                      {/* Mác 2, 4, 5: Small size, Horizontal Scroll */}
                                      <div className="w-full flex flex-nowrap overflow-x-auto gap-6 md:gap-10 pb-6 [&::-webkit-scrollbar]:hidden [-ms-overflow-style:none] [scrollbar-width:none] pt-4">
                                          {page.images.map((img, i) => (
                                              <div key={i} className="relative rounded-[8px] overflow-hidden border border-[#F2EFEA] shadow-sm bg-white shrink-0 w-[220px] md:w-[320px]">
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
