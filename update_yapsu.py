import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

new_yapsu = """
        {/* ─── 01. YAPSU AI ─── */}
        <section id="yapsu-ai" className="relative w-full py-32 bg-[#F5F5F7] overflow-hidden">
           <div className="absolute inset-0 noise-overlay opacity-10 pointer-events-none"></div>
           
           <div className="max-w-[1400px] mx-auto px-6 relative z-20 flex flex-col items-center">
              {/* Badge */}
              <div className="bg-white/90 px-8 py-3 rounded-full font-bold text-[#6BA5D7] border-[4px] border-white shadow-lg rotate-[-2deg] text-xl mb-8 flex items-center gap-2">
                 <span className="w-3 h-3 rounded-full bg-[#6BA5D7] animate-pulse"></span> App Showcase
              </div>
              
              <h2 className="font-['Fredoka'] text-[60px] md:text-[100px] text-transparent bg-clip-text bg-gradient-to-r from-[#6BA5D7] to-[#8FAFE6] leading-none mb-6 text-center" style={{ filter: 'drop-shadow(0px 10px 15px rgba(107,165,215,0.2))' }}>
                 Yapsu AI
              </h2>
              
              <p className="text-xl md:text-2xl text-[#8E8E93] text-center max-w-2xl mb-24 font-medium">
                 An intelligent language learning application powered by AI, featuring interactive roleplay and personalized roadmaps.
              </p>
              
              {/* Phone Mockups Container */}
              <div className="flex flex-col lg:flex-row justify-center items-center gap-12 w-full perspective-1000">
                 
                 {/* Phone 1 */}
                 <div className="flex flex-col items-center group">
                    <h3 className="font-['Fredoka'] text-2xl mb-6 text-[#6BA5D7] bg-[#E8F0F8] px-6 py-2 rounded-full border-[3px] border-white shadow-sm transition-transform duration-300 group-hover:-translate-y-2">Onboarding</h3>
                    <div className="relative w-[280px] h-[580px] bg-black rounded-[45px] border-[12px] border-black shadow-[0_20px_50px_rgba(107,165,215,0.3)] overflow-hidden transition-transform duration-500 hover:scale-105">
                       {/* Notch */}
                       <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[100px] h-[25px] bg-black rounded-b-[18px] z-20"></div>
                       <video src="/assets/portfolio_assets/Yapsu AI/Onboarding Feature.MP4" autoPlay muted loop playsInline className="w-full h-full object-cover rounded-[32px] bg-white" />
                    </div>
                 </div>

                 {/* Phone 2 */}
                 <div className="flex flex-col items-center group lg:-translate-y-12">
                    <h3 className="font-['Fredoka'] text-2xl mb-6 text-[#6BA5D7] bg-[#E8F0F8] px-6 py-2 rounded-full border-[3px] border-white shadow-sm transition-transform duration-300 group-hover:-translate-y-2">Roleplay</h3>
                    <div className="relative w-[280px] h-[580px] bg-black rounded-[45px] border-[12px] border-black shadow-[0_30px_60px_rgba(107,165,215,0.4)] overflow-hidden transition-transform duration-500 hover:scale-105">
                       {/* Notch */}
                       <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[100px] h-[25px] bg-black rounded-b-[18px] z-20"></div>
                       <video src="/assets/portfolio_assets/Yapsu AI/Roleplay Feature.MP4" autoPlay muted loop playsInline className="w-full h-full object-cover rounded-[32px] bg-white" />
                    </div>
                 </div>

                 {/* Phone 3 */}
                 <div className="flex flex-col items-center group">
                    <h3 className="font-['Fredoka'] text-2xl mb-6 text-[#6BA5D7] bg-[#E8F0F8] px-6 py-2 rounded-full border-[3px] border-white shadow-sm transition-transform duration-300 group-hover:-translate-y-2">Roadmap</h3>
                    <div className="relative w-[280px] h-[580px] bg-black rounded-[45px] border-[12px] border-black shadow-[0_20px_50px_rgba(107,165,215,0.3)] overflow-hidden transition-transform duration-500 hover:scale-105">
                       {/* Notch */}
                       <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[100px] h-[25px] bg-black rounded-b-[18px] z-20"></div>
                       <video src="/assets/portfolio_assets/Yapsu AI/Roadmap + Drill Feature.mov" autoPlay muted loop playsInline className="w-full h-full object-cover rounded-[32px] bg-white" />
                    </div>
                 </div>

              </div>
           </div>
        </section>"""

pattern = re.compile(r'<section id="yapsu-ai".*?</section>', re.DOTALL)
content = re.sub(pattern, new_yapsu.strip(), content)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
