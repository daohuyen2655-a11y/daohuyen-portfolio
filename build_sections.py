with open('page_header_tmp.txt', 'r', encoding='utf-8') as f:
    header = f.read()

sections = """
        {/* ─── 01. YAPSU AI ─── */}
        <section id="yapsu-ai" className="relative w-full py-32 bg-[#F5F5F7] overflow-hidden">
           <div className="absolute inset-0 noise-overlay opacity-10 pointer-events-none"></div>
           <div className="max-w-[1400px] mx-auto px-6 relative z-20 flex flex-col items-center">
              <div className="bg-white/90 px-8 py-3 rounded-full font-bold text-[#6BA5D7] border-[6px] border-white shadow-lg rotate-[-1deg] text-2xl mb-8">
                 01. Yapsu AI
              </div>
              <h2 className="font-['Fredoka'] text-[80px] md:text-[130px] text-white leading-none mb-24 text-center rotate-[1deg]" style={{ textShadow: '-3px -3px 0 #FFF, 3px -3px 0 #FFF, -3px 3px 0 #FFF, 3px 3px 0 #FFF, 8px 8px 0px #6BA5D7' }}>
                 Yapsu AI
              </h2>
              <div className="flex flex-wrap justify-center items-center gap-12 w-full">
                 <div className="w-full max-w-[400px] bg-white p-4 rounded-[2rem] shadow-[15px_15px_0px_#6BA5D7] border-[6px] border-[#6BA5D7] rotate-[1deg]">
                    <h3 className="font-['Fredoka'] text-2xl text-center mb-4 text-[#6BA5D7]">Onboarding</h3>
                    <video src="/assets/portfolio_assets/Yapsu AI/Onboarding Feature.MP4" autoPlay muted loop controls playsInline className="w-full h-auto object-contain rounded-[16px]" />
                 </div>
                 <div className="w-full max-w-[400px] bg-white p-4 rounded-[2rem] shadow-[15px_15px_0px_#6BA5D7] border-[6px] border-[#6BA5D7] rotate-[-2deg]">
                    <h3 className="font-['Fredoka'] text-2xl text-center mb-4 text-[#6BA5D7]">Roleplay</h3>
                    <video src="/assets/portfolio_assets/Yapsu AI/Roleplay Feature.MP4" autoPlay muted loop controls playsInline className="w-full h-auto object-contain rounded-[16px]" />
                 </div>
                 <div className="w-full max-w-[400px] bg-white p-4 rounded-[2rem] shadow-[15px_15px_0px_#6BA5D7] border-[6px] border-[#6BA5D7] rotate-[2deg]">
                    <h3 className="font-['Fredoka'] text-2xl text-center mb-4 text-[#6BA5D7]">Roadmap</h3>
                    <video src="/assets/portfolio_assets/Yapsu AI/Roadmap + Drill Feature.mov" autoPlay muted loop controls playsInline className="w-full h-auto object-contain rounded-[16px]" />
                 </div>
              </div>
           </div>
        </section>

        {/* ─── 02. CHINESE DEBATE 2026 ─── */}
        <section id="chinese-debate-26" className="relative w-full py-32 bg-[#06112E] overflow-hidden">
           <div className="absolute inset-0 noise-overlay opacity-15 pointer-events-none"></div>
           <div className="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] opacity-20"></div>
           <div className="max-w-[1400px] mx-auto px-6 relative z-20 flex flex-col items-center">
              <div className="bg-[#00F0FF]/10 px-8 py-3 rounded-full font-bold text-[#00F0FF] border-[6px] border-[#00F0FF] shadow-[6px_6px_0px_#00F0FF] rotate-[2deg] text-2xl mb-8 backdrop-blur-sm">
                 02. Chinese Debate 2026
              </div>
              <h2 className="font-['Fredoka'] text-[60px] md:text-[100px] text-transparent bg-clip-text bg-gradient-to-r from-[#00F0FF] to-[#0066FF] leading-none mb-24 text-center rotate-[-1deg]" style={{ WebkitTextStroke: '2px #00F0FF', filter: 'drop-shadow(0px 0px 10px rgba(0,240,255,0.8))' }}>
                 CÔNG NGHỆ
              </h2>
              <div className="w-full flex justify-center items-center mb-16 relative">
                 <img src="/assets/portfolio_assets/CC FTU/Chinese Debate 2026/KEY VISUAL/cover tbth.png" className="w-full max-w-4xl h-auto object-contain border-[8px] border-[#00F0FF] rounded-[24px] shadow-[0_0_40px_rgba(0,240,255,0.4)] rotate-[1deg]" />
              </div>
           </div>
        </section>

        {/* ─── 03. GEN 20 RECRUITMENT ─── */}
        <section id="gen-20-recruit" className="relative w-full py-32 bg-[#EAF2E3] overflow-hidden">
           <div className="absolute inset-0 noise-overlay opacity-10 pointer-events-none"></div>
           <div className="max-w-[1400px] mx-auto px-6 relative z-20 flex flex-col items-center">
              <div className="bg-white/90 px-8 py-3 rounded-full font-bold text-[#3B5B35] border-[6px] border-white shadow-lg rotate-[-2deg] text-2xl mb-8">
                 03. Gen 20th Recruit
              </div>
              <h2 className="font-['Fredoka'] text-[70px] md:text-[110px] text-white leading-none mb-24 text-center rotate-[1deg]" style={{ textShadow: '-3px -3px 0 #FFF, 3px -3px 0 #FFF, -3px 3px 0 #FFF, 3px 3px 0 #FFF, 8px 8px 0px #3B5B35' }}>
                 PHONG HẢI<br/>TRƯỜNG CHINH
              </h2>
              <div className="w-full flex justify-center items-center mb-16 relative">
                 <img src="/assets/portfolio_assets/CC FTU/CC FTU Gen 20 Recruitment/KEY VISUAL/cover tuyển gen.png" className="w-full max-w-4xl h-auto object-contain border-[8px] border-white rounded-[24px] shadow-2xl rotate-[-1deg]" />
              </div>
           </div>
        </section>

        {/* ─── 04. 19TH BIRTHDAY ─── */}
        <section id="19th-birthday" className="relative w-full py-32 bg-[#F4EEF7] overflow-hidden">
           <div className="absolute inset-0 noise-overlay opacity-10 pointer-events-none"></div>
           <div className="max-w-[1400px] mx-auto px-6 relative z-20 flex flex-col items-center">
              <div className="bg-white/90 px-8 py-3 rounded-full font-bold text-[#A890D8] border-[6px] border-white shadow-lg rotate-[2deg] text-2xl mb-8">
                 04. 19th Birthday
              </div>
              <h2 className="font-['Fredoka'] text-[70px] md:text-[110px] text-white leading-none mb-24 text-center rotate-[-1deg]" style={{ textShadow: '-3px -3px 0 #FFF, 3px -3px 0 #FFF, -3px 3px 0 #FFF, 3px 3px 0 #FFF, 8px 8px 0px #A890D8' }}>
                 Vân Hạ Diệp Mộng
              </h2>
              <div className="w-full flex justify-center items-center mb-16 relative">
                 <img src="/assets/portfolio_assets/CC FTU/CC FTU 19th Anniversary/KEY VISUAL/cover tím.png" className="w-full max-w-4xl h-auto object-contain border-[8px] border-white rounded-[24px] shadow-[0_20px_50px_rgba(168,144,216,0.4)] rotate-[2deg]" />
              </div>
           </div>
        </section>

        {/* ─── 05. CHINESE DEBATE 2025 ─── */}
        <section id="chinese-debate-25" className="relative w-full py-32 bg-[#231710] overflow-hidden">
           <div className="absolute inset-0 noise-overlay opacity-20 pointer-events-none"></div>
           <div className="max-w-[1400px] mx-auto px-6 relative z-20 flex flex-col items-center">
              <div className="bg-gradient-to-r from-[#D4AF37] to-[#F3E5AB] px-8 py-3 rounded-full font-bold text-[#231710] border-[6px] border-[#D4AF37] shadow-[6px_6px_0px_#B8860B] rotate-[-2deg] text-2xl mb-8">
                 05. Chinese Debate 2025
              </div>
              <h2 className="font-['Fredoka'] text-[80px] md:text-[130px] text-transparent bg-clip-text bg-gradient-to-b from-[#FFF2B2] to-[#D4AF37] leading-none mb-24 text-center rotate-[1deg]" style={{ WebkitTextStroke: '2px #B8860B', filter: 'drop-shadow(0px 10px 15px rgba(212,175,55,0.5))' }}>
                 BỨT PHÁ
              </h2>
              <div className="w-full flex justify-center items-center mb-16 relative">
                 <img src="/assets/portfolio_assets/CC FTU/Chinese Debate 2025/KEY VISUAL/cover tbth1.png" className="w-full max-w-4xl h-auto object-contain border-[8px] border-[#D4AF37] rounded-[24px] shadow-[0_0_50px_rgba(212,175,55,0.3)] rotate-[-1deg]" />
              </div>
           </div>
        </section>

        {/* ─── 06. TALKSHOW ─── */}
        <section id="talkshow" className="relative w-full py-32 bg-[#E8F4F8] overflow-hidden">
           <div className="absolute inset-0 noise-overlay opacity-10 pointer-events-none"></div>
           <div className="max-w-[1400px] mx-auto px-6 relative z-20 flex flex-col items-center">
              <div className="bg-white/90 px-8 py-3 rounded-full font-bold text-[#58B3D3] border-[6px] border-white shadow-lg rotate-[2deg] text-2xl mb-8">
                 06. Talkshow
              </div>
              <h2 className="font-['Fredoka'] text-[60px] md:text-[90px] text-white leading-none mb-24 text-center rotate-[-1deg]" style={{ textShadow: '-3px -3px 0 #FFF, 3px -3px 0 #FFF, -3px 3px 0 #FFF, 3px 3px 0 #FFF, 8px 8px 0px #58B3D3' }}>
                 LIVESTREAM
              </h2>
              <div className="w-full flex justify-center items-center mb-16 relative">
                 <img src="/assets/portfolio_assets/CC FTU/Talkshow/KEY VISUAL/cover nè 22.04.05.png" className="w-full max-w-4xl h-auto object-contain border-[8px] border-white rounded-[24px] shadow-2xl rotate-[1deg]" />
              </div>
           </div>
        </section>

        {/* ─── 07. ZODIAC ─── */}
        <section id="zodiac" className="relative w-full py-32 bg-[#EAEBF2] overflow-hidden">
           <div className="absolute inset-0 noise-overlay opacity-10 pointer-events-none"></div>
           <div className="max-w-[1400px] mx-auto px-6 relative z-20 flex flex-col items-center">
              <div className="bg-white/90 px-8 py-3 rounded-full font-bold text-[#2C3E50] border-[6px] border-white shadow-lg rotate-[-2deg] text-2xl mb-8">
                 07. Zodiac Collections
              </div>
              <h2 className="font-['Fredoka'] text-[80px] md:text-[130px] text-white leading-none mb-24 text-center rotate-[1deg]" style={{ textShadow: '-3px -3px 0 #FFF, 3px -3px 0 #FFF, -3px 3px 0 #FFF, 3px 3px 0 #FFF, 8px 8px 0px #2C3E50' }}>
                 Zodiac
              </h2>
           </div>
        </section>

        {/* ─── 08. PAINTASO ─── */}
        <section id="paintaso" className="relative w-full py-32 bg-[#FDF2F5] overflow-hidden">
           <div className="absolute inset-0 noise-overlay opacity-10 pointer-events-none"></div>
           <div className="max-w-[1400px] mx-auto px-6 relative z-20 flex flex-col items-center">
              <div className="bg-white/90 px-8 py-3 rounded-full font-bold text-[#E53935] border-[6px] border-white shadow-lg rotate-[2deg] text-2xl mb-8">
                 08. Paintaso Workshop
              </div>
              <h2 className="font-['Fredoka'] text-[70px] md:text-[110px] text-white leading-none mb-24 text-center rotate-[-1deg]" style={{ textShadow: '-3px -3px 0 #FFF, 3px -3px 0 #FFF, -3px 3px 0 #FFF, 3px 3px 0 #FFF, 8px 8px 0px #E53935' }}>
                 Tô Bình Yên
              </h2>
              <div className="w-full flex justify-center items-center mb-16 relative">
                 <img src="/assets/portfolio_assets/PAINTASO/KEY VISUAL/COVER.jpg" className="w-full max-w-4xl h-auto object-contain border-[8px] border-white rounded-[24px] shadow-2xl rotate-[-2deg]" />
              </div>
           </div>
        </section>

        {/* ─── FOOTER ─── */}
        <footer className="w-full py-24 bg-[#89B66B] text-center text-white relative overflow-hidden">
           <div className="absolute inset-0 noise-overlay opacity-15 pointer-events-none"></div>
           <div className="relative z-20 flex flex-col items-center">
              <h2 className="font-['Fredoka'] text-[60px] md:text-[90px] mb-8 font-black" style={{ textShadow: '-3px -3px 0 #FFF, 3px -3px 0 #FFF, -3px 3px 0 #FFF, 3px 3px 0 #FFF, 6px 6px 0px #709955' }}>
                 Thanks for watching!
              </h2>
              <div className="bg-white px-8 py-3 rounded-full text-[#89B66B] font-bold text-2xl border-[4px] border-white shadow-[6px_6px_0px_#709955] rotate-[-2deg]">
                 Huyen Dao © 2026
              </div>
           </div>
        </footer>
      </div>
    </main>
  );
}
"""

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(header + sections)
