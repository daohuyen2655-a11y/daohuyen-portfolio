import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

new_yapsu = """
        {/* ─── 01. YAPSU AI (PRO SHOWCASE) ─── */}
        <section id="yapsu-ai" className="relative w-full py-32 bg-gradient-to-br from-[#08122B] via-[#102352] to-[#142F73] overflow-hidden font-sans">
           
           {/* SVG Wavy Background (Matches AuraFlow Vibe) */}
           <div className="absolute inset-0 z-0 opacity-30 pointer-events-none flex items-center justify-center">
              <svg width="100%" height="100%" viewBox="0 0 1440 800" fill="none" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
                 <path d="M-100,600 C200,400 400,800 800,500 C1200,200 1400,400 1600,300" stroke="url(#paint0_linear)" strokeWidth="1.5" />
                 <path d="M-100,620 C220,420 420,820 820,520 C1220,220 1420,420 1620,320" stroke="url(#paint0_linear)" strokeWidth="1" opacity="0.7"/>
                 <path d="M-100,640 C240,440 440,840 840,540 C1240,240 1440,440 1640,340" stroke="url(#paint0_linear)" strokeWidth="0.5" opacity="0.4"/>
                 <defs>
                    <linearGradient id="paint0_linear" x1="0" y1="0" x2="1440" y2="800" gradientUnits="userSpaceOnUse">
                       <stop stopColor="#ffffff" stopOpacity="0" />
                       <stop offset="0.5" stopColor="#ffffff" stopOpacity="0.8" />
                       <stop offset="1" stopColor="#ffffff" stopOpacity="0" />
                    </linearGradient>
                 </defs>
              </svg>
           </div>
           
           <div className="max-w-[1400px] mx-auto px-6 relative z-20">
              
              {/* HERO SECTION */}
              <div className="flex flex-col lg:flex-row items-center justify-between mb-48 gap-16">
                 {/* Left Text */}
                 <div className="w-full lg:w-1/2 flex flex-col items-start text-white">
                    <h2 className="font-['Fredoka'] text-[60px] md:text-[90px] font-bold leading-tight mb-6 tracking-wide drop-shadow-md">
                       1. Yapsu AI
                    </h2>
                    
                    <div className="px-8 py-2 border-[1.5px] border-white/80 rounded-[30px] text-lg font-medium mb-10 hover:bg-white hover:text-[#102352] transition-colors cursor-pointer tracking-wider">
                       App Design
                    </div>
                    
                    <div className="flex items-start gap-8 mb-8">
                       {/* App Icon Mockup */}
                       <div className="w-[120px] h-[120px] rounded-[28px] shadow-[0_20px_40px_rgba(0,0,0,0.5)] bg-gradient-to-tr from-[#FF8C00] to-[#FFD700] p-[4px] shrink-0 border border-white/20">
                          <div className="w-full h-full bg-[#FFB020] rounded-[24px] flex flex-col justify-center items-center overflow-hidden relative">
                             {/* Mascot placeholder shape */}
                             <div className="w-[60px] h-[40px] bg-[#D45A00] rounded-full absolute bottom-4"></div>
                             <div className="w-[12px] h-[12px] bg-white rounded-full absolute top-[40%] left-[30%]"></div>
                             <div className="w-[12px] h-[12px] bg-white rounded-full absolute top-[40%] right-[30%]"></div>
                             <h4 className="font-['Fredoka'] font-black text-white text-xl absolute bottom-1">Yapsu</h4>
                          </div>
                       </div>
                       
                       <p className="text-lg md:text-xl text-blue-100/90 leading-relaxed font-light mt-2 max-w-md">
                          This is an application interface design project. Yapsu AI is a modern language learning app designed for individuals seeking a natural way to practice conversations with friendly AI tutors.
                       </p>
                    </div>
                 </div>
                 
                 {/* Right 3D Floating Video - Highly Realistic Phone */}
                 <div className="w-full lg:w-1/2 flex justify-center perspective-1000">
                    <div className="relative w-[300px] h-[620px] bg-[#1A1F35] rounded-[55px] p-[10px] shadow-[30px_40px_80px_rgba(0,0,0,0.7)] border border-white/20 transition-transform duration-700 ease-out hover:rotate-y-[-10deg] hover:rotate-x-[5deg]" style={{ transform: 'rotateY(-25deg) rotateX(12deg) rotateZ(-6deg)', boxShadow: 'inset -2px 2px 10px rgba(255,255,255,0.4), inset 5px -5px 15px rgba(0,0,0,0.8), 30px 40px 80px rgba(0,0,0,0.7)' }}>
                       {/* Inner screen border */}
                       <div className="w-full h-full bg-black rounded-[45px] overflow-hidden relative border-[4px] border-black">
                          {/* Dynamic Island */}
                          <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[90px] h-[28px] bg-black rounded-full z-20 shadow-[inset_0_-2px_4px_rgba(255,255,255,0.1)]"></div>
                          {/* Screen Glare */}
                          <div className="absolute inset-0 bg-gradient-to-tr from-transparent via-white/5 to-white/20 z-10 pointer-events-none"></div>
                          <video src="/assets/portfolio_assets/Yapsu AI/Roleplay Feature.MP4" autoPlay muted loop playsInline className="w-full h-full object-cover" />
                       </div>
                    </div>
                 </div>
              </div>

              {/* ISOMETRIC SNAPSHOTS GRID (With 3D Extrusion) */}
              <div className="w-full mb-48 relative">
                 <h3 className="font-['Fredoka'] text-[45px] font-bold text-white text-center mb-20 tracking-wide">Screen Flow</h3>
                 
                 <div className="w-full overflow-visible flex justify-center items-center perspective-[2000px]">
                    <div className="flex gap-[40px] transform rotate-x-[55deg] rotate-z-[-40deg] scale-[1.1] translate-y-10">
                       
                       {/* Column 1 */}
                       <div className="flex flex-col gap-[40px] -translate-y-[80px]">
                          {[
                             "/assets/portfolio_assets/Yapsu AI/snapshots/onboard_04.jpg",
                             "/assets/portfolio_assets/Yapsu AI/snapshots/roleplay_18.jpg",
                             "/assets/portfolio_assets/Yapsu AI/snapshots/roadmap_07.jpg"
                          ].map((src, i) => (
                             <div key={`col1-${i}`} className="relative w-[240px] h-[520px] bg-[#111A2C] rounded-[45px] p-[8px] transition-transform duration-500 hover:-translate-y-8" style={{ boxShadow: '-12px 12px 0px #091221, -25px 25px 50px rgba(0,0,0,0.8)' }}>
                                <div className="w-full h-full bg-black rounded-[38px] overflow-hidden">
                                   <div className="absolute top-[8px] left-1/2 -translate-x-1/2 w-[70px] h-[20px] bg-black rounded-b-[12px] z-20"></div>
                                   <img src={src} className="w-full h-full object-cover" />
                                </div>
                             </div>
                          ))}
                       </div>
                       
                       {/* Column 2 */}
                       <div className="flex flex-col gap-[40px]">
                          {[
                             "/assets/portfolio_assets/Yapsu AI/snapshots/roleplay_10.jpg",
                             "/assets/portfolio_assets/Yapsu AI/snapshots/roadmap_05.jpg",
                             "/assets/portfolio_assets/Yapsu AI/snapshots/onboard_09.jpg"
                          ].map((src, i) => (
                             <div key={`col2-${i}`} className="relative w-[240px] h-[520px] bg-[#111A2C] rounded-[45px] p-[8px] transition-transform duration-500 hover:-translate-y-8" style={{ boxShadow: '-12px 12px 0px #091221, -25px 25px 50px rgba(0,0,0,0.8)' }}>
                                <div className="w-full h-full bg-black rounded-[38px] overflow-hidden">
                                   <div className="absolute top-[8px] left-1/2 -translate-x-1/2 w-[70px] h-[20px] bg-black rounded-b-[12px] z-20"></div>
                                   <img src={src} className="w-full h-full object-cover" />
                                </div>
                             </div>
                          ))}
                       </div>
                       
                       {/* Column 3 */}
                       <div className="flex flex-col gap-[40px] translate-y-[80px]">
                          {[
                             "/assets/portfolio_assets/Yapsu AI/snapshots/roadmap_15.jpg",
                             "/assets/portfolio_assets/Yapsu AI/snapshots/onboard_15.jpg",
                             "/assets/portfolio_assets/Yapsu AI/snapshots/roleplay_15.jpg"
                          ].map((src, i) => (
                             <div key={`col3-${i}`} className="relative w-[240px] h-[520px] bg-[#111A2C] rounded-[45px] p-[8px] transition-transform duration-500 hover:-translate-y-8" style={{ boxShadow: '-12px 12px 0px #091221, -25px 25px 50px rgba(0,0,0,0.8)' }}>
                                <div className="w-full h-full bg-black rounded-[38px] overflow-hidden">
                                   <div className="absolute top-[8px] left-1/2 -translate-x-1/2 w-[70px] h-[20px] bg-black rounded-b-[12px] z-20"></div>
                                   <img src={src} className="w-full h-full object-cover" />
                                </div>
                             </div>
                          ))}
                       </div>
                    </div>
                 </div>
              </div>

              {/* FUNCTIONAL VIDEO MOCKUPS */}
              <div className="w-full relative z-20 pt-20">
                 <h3 className="font-['Fredoka'] text-[45px] font-bold text-white text-center mb-20 tracking-wide">Interactive Prototypes</h3>
                 <div className="flex flex-col lg:flex-row justify-center items-center gap-14 w-full">
                    
                    {/* Video 1 */}
                    <div className="flex flex-col items-center group">
                       <h4 className="font-['Fredoka'] text-2xl mb-8 text-white/90 tracking-wide">Onboarding</h4>
                       <div className="relative w-[300px] h-[620px] bg-[#E2E8F0] rounded-[55px] p-[3px] shadow-[0_30px_60px_rgba(0,0,0,0.4)] transition-transform duration-500 hover:-translate-y-4" style={{ boxShadow: 'inset 0 0 10px rgba(255,255,255,0.8), 0 30px 60px rgba(0,0,0,0.6)' }}>
                          <div className="w-full h-full bg-black rounded-[52px] border-[6px] border-black overflow-hidden relative">
                             <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[90px] h-[28px] bg-black rounded-full z-20"></div>
                             <div className="absolute inset-0 bg-gradient-to-tr from-transparent to-white/10 z-10 pointer-events-none"></div>
                             <video src="/assets/portfolio_assets/Yapsu AI/Onboarding Feature.MP4" autoPlay muted loop playsInline className="w-full h-full object-cover" />
                          </div>
                       </div>
                    </div>

                    {/* Video 2 */}
                    <div className="flex flex-col items-center group">
                       <h4 className="font-['Fredoka'] text-2xl mb-8 text-white/90 tracking-wide">Roleplay</h4>
                       <div className="relative w-[300px] h-[620px] bg-[#E2E8F0] rounded-[55px] p-[3px] shadow-[0_30px_60px_rgba(0,0,0,0.4)] transition-transform duration-500 hover:-translate-y-4" style={{ boxShadow: 'inset 0 0 10px rgba(255,255,255,0.8), 0 30px 60px rgba(0,0,0,0.6)' }}>
                          <div className="w-full h-full bg-black rounded-[52px] border-[6px] border-black overflow-hidden relative">
                             <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[90px] h-[28px] bg-black rounded-full z-20"></div>
                             <div className="absolute inset-0 bg-gradient-to-tr from-transparent to-white/10 z-10 pointer-events-none"></div>
                             <video src="/assets/portfolio_assets/Yapsu AI/Roleplay Feature.MP4" autoPlay muted loop playsInline className="w-full h-full object-cover" />
                          </div>
                       </div>
                    </div>

                    {/* Video 3 */}
                    <div className="flex flex-col items-center group">
                       <h4 className="font-['Fredoka'] text-2xl mb-8 text-white/90 tracking-wide">Roadmap</h4>
                       <div className="relative w-[300px] h-[620px] bg-[#E2E8F0] rounded-[55px] p-[3px] shadow-[0_30px_60px_rgba(0,0,0,0.4)] transition-transform duration-500 hover:-translate-y-4" style={{ boxShadow: 'inset 0 0 10px rgba(255,255,255,0.8), 0 30px 60px rgba(0,0,0,0.6)' }}>
                          <div className="w-full h-full bg-black rounded-[52px] border-[6px] border-black overflow-hidden relative">
                             <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[90px] h-[28px] bg-black rounded-full z-20"></div>
                             <div className="absolute inset-0 bg-gradient-to-tr from-transparent to-white/10 z-10 pointer-events-none"></div>
                             <video src="/assets/portfolio_assets/Yapsu AI/Roadmap + Drill Feature.mov" autoPlay muted loop playsInline className="w-full h-full object-cover" />
                          </div>
                       </div>
                    </div>

                 </div>
              </div>

           </div>
        </section>"""

pattern = re.compile(r'<section id="yapsu-ai".*?</section>', re.DOTALL)
content = re.sub(pattern, new_yapsu.strip(), content)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
