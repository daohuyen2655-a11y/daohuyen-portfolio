import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove "View Website" CTA from Chinese Debate 2026
cta_pattern = r'\{/\* View Website Button \*/\}.*?</svg>\s*View Website\s*</span>\s*<div className="absolute inset-0[^>]+></div>\s*</a>\s*</div>'
content = re.sub(cta_pattern, '', content, flags=re.DOTALL)

# 2. Build Chinese Debate 2025
start_marker = "{/* ─── 05. CHINESE DEBATE 2025 ─── */}"
end_marker = "{/* ─── 06. TALKSHOW ─── */}"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    new_2025 = """{/* ─── 05. CHINESE DEBATE 2025 ─── */}
        <section id="chinese-debate-25" className="relative w-full py-24 bg-gradient-to-b from-[#231710] to-[#3D2719] overflow-hidden">
           <div className="max-w-[1400px] mx-auto px-6 sm:px-10 relative z-20 flex flex-col">
              
              {/* 1. SECTION HEADER */}
              <div className="flex flex-col items-center mb-20 text-center">
                  <div className="px-6 py-2 border-2 border-[#D4AF37] text-[#FFF2B2] rounded-full text-sm font-bold mb-6 tracking-widest uppercase bg-[#231710]/50 backdrop-blur-sm shadow-[0_0_15px_rgba(212,175,55,0.3)]">
                      Event Identity
                  </div>
                  <h2 className="font-['Fredoka'] text-[60px] md:text-[90px] font-black text-transparent bg-clip-text bg-gradient-to-b from-[#FFF2B2] to-[#D4AF37] leading-none mb-6 pb-2" style={{ filter: 'drop-shadow(0px 0px 15px rgba(212,175,55,0.5))' }}>
                      Chinese Debate 2025
                  </h2>
                  <p className="max-w-2xl text-lg text-[#F3E5AB] font-['Quicksand'] font-bold leading-relaxed">
                      "BỨT PHÁ" - The prestigious academic debate competition hosted by the Chinese Club - Foreign Trade University.
                  </p>
              </div>

              {/* 2. KEY VISUAL */}
              <div className="w-full mb-32 flex flex-col items-center">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#D4AF37] mb-10 tracking-wide drop-shadow-[0_0_10px_rgba(212,175,55,0.4)]">
                      Key Visual
                  </h3>
                  <div className="relative w-full max-w-5xl rounded-[32px] overflow-hidden border-[4px] border-[#D4AF37] shadow-[0_0_40px_rgba(212,175,55,0.3)] group">
                      <img src="/assets/portfolio_assets/CC FTU/Chinese Debate 2025/KEY VISUAL/cover tbth1.png" alt="Debate 2025 Key Visual" className="w-full h-auto block group-hover:scale-105 transition-transform duration-700" />
                  </div>
                  
                  {/* Avatar Badge */}
                  <div className="relative -mt-20 w-32 h-32 md:w-44 md:h-44 rounded-full p-1 bg-[#D4AF37] shadow-[0_0_30px_rgba(212,175,55,0.4)] z-10 group hover:-translate-y-2 transition-transform duration-300">
                      <div className="w-full h-full rounded-full overflow-hidden bg-[#231710]">
                          <img src="/assets/portfolio_assets/CC FTU/Chinese Debate 2025/KEY VISUAL/AVATAR TBTH.png" alt="Debate Avatar" className="w-full h-full object-cover" />
                      </div>
                  </div>
              </div>

              {/* 3. DIGITAL & SOCIAL POSTS (MASONRY) */}
              <div className="w-full mb-24">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#D4AF37] mb-10 tracking-wide text-center drop-shadow-[0_0_10px_rgba(212,175,55,0.4)]">
                      Digital & Social
                  </h3>
                  
                  <div className="columns-2 md:columns-3 lg:columns-4 gap-6 w-full max-w-[1400px] mx-auto">
                      {[
                          "MỞ ĐƠN.png",
                          "THÔNG BÁO QUÁN QUÂN.png",
                          "THỂ LỆ VÒNG SƠ KHẢO.png",
                          "THÔNG BÁO CƠ CẤU GIẢI THƯỞNG.png",
                          "QUYỀN LỢI KHI THAM GIA CUỘC THI.png",
                          "TỪ KHOÁ VÒNG CHUNG KẾT CUỘC THI.png",
                          "GIỚI THIỆU BẢO TRỢ TRUYỀN THÔNG.png",
                          "GIỚI THIỆU ĐỐI TÁC TRUYỀN THÔNG.png",
                          "GIỚI THIỆU NTT-1.png",
                          "GIỚI THIỆU NTT-2.png"
                      ].map((filename, idx) => (
                          <div key={idx} className="relative rounded-[16px] overflow-hidden border-2 border-[#D4AF37]/50 group hover:border-[#D4AF37] transition-colors duration-300 shadow-[0_0_15px_rgba(212,175,55,0.1)] break-inside-avoid mb-6 inline-block w-full">
                              <img src={`/assets/portfolio_assets/CC FTU/Chinese Debate 2025/Social Posts/${filename}`} alt={filename.replace('.png', '')} className="w-full h-auto block group-hover:scale-105 transition-transform duration-500" loading="lazy" />
                          </div>
                      ))}
                  </div>
              </div>

              {/* 4. VIDEO PRODUCTION */}
              <div className="w-full mb-10 flex flex-col items-center">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#D4AF37] mb-10 tracking-wide text-center drop-shadow-[0_0_10px_rgba(212,175,55,0.4)]">
                      Video Production
                  </h3>
                  <div className="w-full max-w-4xl relative rounded-[24px] overflow-hidden border-[4px] border-[#D4AF37] shadow-[0_0_40px_rgba(212,175,55,0.3)] bg-black">
                      <video 
                          src="/assets/portfolio_assets/CC FTU/Chinese Debate 2025/Video/THỂ LỆ VÒNG CHUNG KẾT.mp4"
                          controls
                          muted
                          loop
                          className="w-full h-auto block"
                      />
                  </div>
                  <h4 className="font-['Quicksand'] font-bold text-lg text-[#FFF2B2] tracking-wider mt-6">
                      Final Round Rules & Trailer
                  </h4>
              </div>

           </div>
        </section>

        """
    content = content[:start_idx] + new_2025 + content[end_idx:]
    with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS")
else:
    print("FAILED TO FIND MARKERS")

