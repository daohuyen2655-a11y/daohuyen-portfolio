import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add useRef to react imports
content = content.replace(
    "import React, { useState, useEffect } from 'react';",
    "import React, { useState, useEffect, useRef } from 'react';"
)

# 2. Inject the hook after setEntered if not already there
hook_str = """  const [entered, setEntered] = useState(false);

  const gen20CarouselRef = useRef<HTMLDivElement>(null);
  useEffect(() => {
    const interval = setInterval(() => {
       if (gen20CarouselRef.current) {
           const { scrollLeft, scrollWidth, clientWidth } = gen20CarouselRef.current;
           if (scrollLeft + clientWidth >= scrollWidth - 10) {
               gen20CarouselRef.current.scrollTo({ left: 0, behavior: 'smooth' });
           } else {
               gen20CarouselRef.current.scrollBy({ left: clientWidth * 0.7, behavior: 'smooth' });
           }
       }
    }, 3000);
    return () => clearInterval(interval);
  }, []);"""

if "const gen20CarouselRef" not in content:
    content = content.replace("  const [entered, setEntered] = useState(false);", hook_str)

# 3. Replace the Gen 20 Section
start_marker = "{/* ─── 03. GEN 20 RECRUITMENT ─── */}"
end_marker = "</section>\n\n        {/* ─── 04. 19TH BIRTHDAY ─── */}"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    new_gen20 = """{/* ─── 03. GEN 20 RECRUITMENT ─── */}
        <section id="gen-20-recruit" className="relative w-full py-24 bg-gradient-to-b from-[#EAF2E3] to-[#D9EBCB] overflow-hidden">
           <div className="max-w-[1400px] mx-auto px-6 sm:px-10 relative z-20 flex flex-col">
              
              {/* 1. SECTION HEADER */}
              <div className="flex flex-col items-center mb-20 text-center">
                  <div className="px-6 py-2 border-[4px] border-white text-[#3B5B35] rounded-full text-sm font-bold mb-6 tracking-widest uppercase bg-white/50 backdrop-blur-sm shadow-md rotate-[-2deg]">
                      Campaign Design
                  </div>
                  <h2 className="font-['Fredoka'] text-[50px] md:text-[80px] font-black text-[#2C4424] leading-none mb-6 rotate-[1deg]" style={{ textShadow: '4px 4px 0px rgba(255,255,255,0.8)' }}>
                      Gen 20th Recruitment
                  </h2>
                  <p className="max-w-2xl text-lg text-[#3B5B35] font-['Quicksand'] font-bold leading-relaxed">
                      Chiến dịch tuyển thành viên thường niên lớn nhất của Câu lạc bộ Tiếng Trung - Trường Đại học Ngoại thương (CC FTU).
                  </p>
              </div>

              {/* 2. KEY VISUAL */}
              <div className="w-full mb-32 flex flex-col items-center">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#3B5B35] mb-10 tracking-wide">
                      Key Visual
                  </h3>
                  <div className="relative w-full max-w-5xl rounded-[32px] overflow-hidden border-[8px] border-white shadow-[0_20px_50px_rgba(59,91,53,0.2)] rotate-[-1deg] group">
                      <img src="/assets/portfolio_assets/CC FTU/CC FTU Gen 20 Recruitment/KEY VISUAL/cover tuyển gen.png" alt="Gen 20 Key Visual" className="w-full h-auto block group-hover:scale-105 transition-transform duration-700" />
                  </div>
                  
                  {/* Avatar Badge */}
                  <div className="relative -mt-20 w-32 h-32 md:w-44 md:h-44 rounded-full p-2 bg-white shadow-xl z-10 group hover:-translate-y-2 transition-transform duration-300 rotate-[3deg]">
                      <div className="w-full h-full rounded-full overflow-hidden bg-[#D9EBCB]">
                          <img src="/assets/portfolio_assets/CC FTU/CC FTU Gen 20 Recruitment/KEY VISUAL/avt tuyển gen.png" alt="Gen 20 Avatar" className="w-full h-full object-cover" />
                      </div>
                  </div>
              </div>

              {/* 3. EVENT APPLICATIONS */}
              <div className="w-full mb-32 flex flex-col items-center">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#3B5B35] mb-10 tracking-wide text-center">
                      Event Applications
                  </h3>
                  <div className="w-full max-w-lg flex flex-col items-center gap-6">
                      <div className="relative group w-full rounded-[24px] overflow-hidden border-[6px] border-white shadow-[0_15px_40px_rgba(59,91,53,0.15)] hover:shadow-[0_25px_50px_rgba(59,91,53,0.25)] transition-all duration-500 rotate-[1deg]">
                          <img src="/assets/portfolio_assets/CC FTU/CC FTU Gen 20 Recruitment/Print & Event Applications/frame.png" alt="Avatar Frame" className="w-full h-auto block group-hover:scale-[1.02] transition-transform duration-700" />
                      </div>
                      <h4 className="font-['Quicksand'] font-bold text-xl text-[#3B5B35] tracking-wider uppercase mt-4">Avatar Frame</h4>
                  </div>
              </div>

              {/* 4. DIGITAL & SOCIAL (AUTO-SCROLL CAROUSEL) */}
              <div className="w-full mb-10 overflow-hidden">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#3B5B35] mb-10 tracking-wide text-center">
                      Digital & Social
                  </h3>
                  
                  <div className="relative w-full max-w-6xl mx-auto group">
                      {/* Carousel Container */}
                      <div 
                          ref={gen20CarouselRef}
                          className="flex overflow-x-auto gap-6 snap-x snap-mandatory scroll-smooth pb-8"
                          style={{ scrollbarWidth: 'none', msOverflowStyle: 'none' }}
                      >
                          {[
                              "Q&A.png", 
                              "THÔNG BÁO KẾT QUẢ.png", 
                              "VIRAL POST.png", 
                              "Đóng đơn đăng ký.png"
                          ].map((filename, idx) => (
                              <div key={idx} className="flex-none w-[85%] md:w-[60%] lg:w-[45%] snap-center relative rounded-[24px] overflow-hidden border-[6px] border-white shadow-lg transition-transform duration-500 hover:scale-[1.02]">
                                  <img src={`/assets/portfolio_assets/CC FTU/CC FTU Gen 20 Recruitment/SOCIAL POST/${filename}`} alt={filename.replace('.png', '')} className="w-full h-auto block" />
                              </div>
                          ))}
                      </div>
                      
                      {/* Fade Indicators for ends */}
                      <div className="absolute top-0 bottom-0 left-0 w-16 bg-gradient-to-r from-[#EAF2E3] to-transparent pointer-events-none"></div>
                      <div className="absolute top-0 bottom-0 right-0 w-16 bg-gradient-to-l from-[#EAF2E3] to-transparent pointer-events-none"></div>
                  </div>
              </div>

           </div>
        </section>
"""
    content = content[:start_idx] + new_gen20 + content[end_idx:]
    with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS")
else:
    print("FAILED TO FIND MARKERS")

