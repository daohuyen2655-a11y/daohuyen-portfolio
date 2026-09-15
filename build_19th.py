import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = "{/* ─── 04. 19TH BIRTHDAY ─── */}"
end_marker = "{/* ─── 05. CHINESE DEBATE 2025 ─── */}"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    new_19th = """{/* ─── 04. 19TH ANNIVERSARY ─── */}
        <section id="19th-birthday" className="relative w-full py-24 bg-gradient-to-b from-[#F4EEF7] to-[#E3D5F2] overflow-hidden">
           <div className="max-w-[1400px] mx-auto px-6 sm:px-10 relative z-20 flex flex-col">
              
              {/* 1. SECTION HEADER */}
              <div className="flex flex-col items-center mb-20 text-center">
                  <div className="px-6 py-2 border-[4px] border-white text-[#8665C3] rounded-full text-sm font-bold mb-6 tracking-widest uppercase bg-white/50 backdrop-blur-sm shadow-md">
                      Event Identity
                  </div>
                  <h2 className="font-['Fredoka'] text-[60px] md:text-[90px] font-black text-[#6B4AA6] leading-none mb-6" style={{ textShadow: '4px 4px 0px rgba(255,255,255,0.9)' }}>
                      19th Anniversary
                  </h2>
                  <p className="max-w-2xl text-lg text-[#6B4AA6]/90 font-['Quicksand'] font-bold leading-relaxed">
                      "Vân Hạ Diệp Mộng" - Kỷ niệm 19 năm thành lập Câu lạc bộ Tiếng Trung Trường Đại học Ngoại thương (CC FTU).
                  </p>
              </div>

              {/* 2. KEY VISUAL */}
              <div className="w-full mb-32 flex flex-col items-center">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#8665C3] mb-10 tracking-wide">
                      Key Visual
                  </h3>
                  <div className="relative w-full max-w-5xl rounded-[32px] overflow-hidden border-[8px] border-white shadow-[0_20px_50px_rgba(134,101,195,0.2)] group">
                      <img src="/assets/portfolio_assets/CC FTU/CC FTU 19th Anniversary/Key Visual/cover tím.png" alt="19th Anniversary Key Visual" className="w-full h-auto block group-hover:scale-105 transition-transform duration-700" />
                  </div>
                  
                  {/* Avatar Badge */}
                  <div className="relative -mt-20 w-32 h-32 md:w-44 md:h-44 rounded-full p-2 bg-white shadow-xl z-10 group hover:-translate-y-2 transition-transform duration-300">
                      <div className="w-full h-full rounded-full overflow-hidden bg-[#E3D5F2]">
                          <img src="/assets/portfolio_assets/CC FTU/CC FTU 19th Anniversary/Key Visual/AVT tím.png" alt="19th Avatar" className="w-full h-full object-cover" />
                      </div>
                  </div>
              </div>

              {/* 3. EVENT APPLICATIONS (MASONRY) */}
              <div className="w-full mb-10">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#8665C3] mb-10 tracking-wide text-center">
                      Event Applications
                  </h3>
                  
                  <div className="columns-1 md:columns-2 gap-8 w-full max-w-5xl mx-auto">
                      {[
                          "BACKDROP tím.png", 
                          "FRAME tím.png", 
                          "Social story.png", 
                          "cover mail tím.png"
                      ].map((filename, idx) => (
                          <div key={idx} className="relative rounded-[24px] overflow-hidden border-[6px] border-white group hover:border-[#8665C3] transition-colors duration-300 shadow-lg break-inside-avoid mb-8 inline-block w-full">
                              <img src={`/assets/portfolio_assets/CC FTU/CC FTU 19th Anniversary/Print & Event Applications/${filename}`} alt={filename.replace('.png', '')} className="w-full h-auto block group-hover:scale-105 transition-transform duration-500" />
                          </div>
                      ))}
                  </div>
              </div>

           </div>
        </section>

        """
    content = content[:start_idx] + new_19th + content[end_idx:]
    with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS")
else:
    print("FAILED TO FIND MARKERS")

