import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = "{/* ─── 06. TALKSHOW ─── */}"
end_marker = "{/* ─── 07. ZODIAC ─── */}"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    new_talkshow = """{/* ─── 06. TALKSHOW ─── */}
        <section id="talkshow" className="relative w-full py-24 bg-gradient-to-b from-[#E8F4F8] to-[#CDE6EF] overflow-hidden">
           <div className="max-w-[1400px] mx-auto px-6 sm:px-10 relative z-20 flex flex-col">
              
              {/* 1. SECTION HEADER */}
              <div className="flex flex-col items-center mb-20 text-center">
                  <div className="px-6 py-2 border-[3px] border-[#58B3D3] text-[#4194B1] rounded-full text-sm font-bold mb-6 tracking-widest uppercase bg-white/60 backdrop-blur-sm shadow-[0_0_15px_rgba(88,179,211,0.2)]">
                      Event Identity
                  </div>
                  <h2 className="font-['Fredoka'] text-[60px] md:text-[90px] font-black text-transparent bg-clip-text bg-gradient-to-b from-[#8DD1E8] to-[#4194B1] leading-none mb-6 pb-2" style={{ filter: 'drop-shadow(0px 0px 10px rgba(255,255,255,1))' }}>
                      Talkshow Livestream
                  </h2>
                  <p className="max-w-2xl text-lg text-[#58B3D3] font-['Quicksand'] font-bold leading-relaxed">
                      "Từ Trung Quốc đến Việt Nam: Livestream đã cách mạng hóa ngành bán lẻ như thế nào?" - A modern and engaging talkshow exploring the e-commerce livestream revolution.
                  </p>
              </div>

              {/* 2. KEY VISUAL */}
              <div className="w-full mb-24 flex flex-col items-center">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#4194B1] mb-10 tracking-wide drop-shadow-[0_0_10px_rgba(255,255,255,1)]">
                      Key Visual
                  </h3>
                  <div className="relative w-full max-w-5xl rounded-[32px] overflow-hidden border-[4px] border-white shadow-[0_20px_50px_rgba(88,179,211,0.2)] group">
                      <img src="/assets/portfolio_assets/CC FTU/Talkshow/KEY VISUAL/cover nè 22.04.05.png" alt="Talkshow Key Visual" className="w-full h-auto block group-hover:scale-105 transition-transform duration-700" />
                  </div>
                  
                  {/* Avatar Badge */}
                  <div className="relative -mt-20 w-32 h-32 md:w-44 md:h-44 rounded-full p-1 bg-white shadow-[0_15px_40px_rgba(88,179,211,0.3)] z-10 group hover:-translate-y-2 transition-transform duration-300">
                      <div className="w-full h-full rounded-full overflow-hidden bg-[#E8F4F8]">
                          <img src="/assets/portfolio_assets/CC FTU/Talkshow/KEY VISUAL/avatar.jpg" alt="Talkshow Avatar" className="w-full h-full object-cover" />
                      </div>
                  </div>
              </div>

              {/* 3. DIGITAL & SOCIAL */}
              <div className="w-full mb-10 flex flex-col items-center">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#4194B1] mb-10 tracking-wide drop-shadow-[0_0_10px_rgba(255,255,255,1)] text-center">
                      Digital & Social
                  </h3>
                  <div className="relative max-w-2xl w-full rounded-[24px] overflow-hidden border-[4px] border-white shadow-[0_20px_50px_rgba(88,179,211,0.2)] group hover:border-[#8DD1E8] transition-colors duration-500">
                      <img src="/assets/portfolio_assets/CC FTU/Talkshow/SOCIAL POST/Thông báo danh sách nhận ĐRL.png" alt="Social Post" className="w-full h-auto block group-hover:scale-[1.02] transition-transform duration-700" />
                  </div>
                  <h4 className="font-['Quicksand'] font-bold text-lg text-[#4194B1] tracking-wider uppercase mt-8 bg-white/70 px-6 py-2 rounded-full shadow-sm">
                      Social Media Post
                  </h4>
              </div>

           </div>
        </section>

        """
    content = content[:start_idx] + new_talkshow + content[end_idx:]
    with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS")
else:
    print("FAILED TO FIND MARKERS")

