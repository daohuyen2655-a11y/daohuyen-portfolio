import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

new_yapsu = """
        {/* ─── 01. YAPSU AI (CLEAN PREMIUM) ─── */}
        <section id="yapsu-ai" className="relative w-full py-32 overflow-hidden font-sans">
           
           {/* Deep Radial Glowing Background */}
           <div className="absolute inset-0 bg-[radial-gradient(circle_at_30%_40%,_#1E3B8A_0%,_#0B1B42_50%,_#050B1F_100%)] z-0"></div>
           
           {/* Subtle Elegant Wavy Lines */}
           <div className="absolute bottom-0 left-0 w-full h-[500px] z-0 pointer-events-none mix-blend-screen opacity-40">
              <svg width="100%" height="100%" viewBox="0 0 1440 500" fill="none" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
                 <path d="M-100,400 C200,500 400,100 800,200 C1200,300 1300,50 1500,100" stroke="url(#waveGradClean)" strokeWidth="1" />
                 <path d="M-100,420 C220,520 420,120 820,220 C1220,320 1320,70 1520,120" stroke="url(#waveGradClean)" strokeWidth="0.8" opacity="0.6"/>
                 <path d="M-100,440 C240,540 440,140 840,240 C1240,340 1340,90 1540,140" stroke="url(#waveGradClean)" strokeWidth="0.5" opacity="0.3"/>
                 <defs>
                    <linearGradient id="waveGradClean" x1="0" y1="0" x2="1440" y2="500" gradientUnits="userSpaceOnUse">
                       <stop stopColor="#ffffff" stopOpacity="0.1" />
                       <stop offset="0.5" stopColor="#ffffff" stopOpacity="0.5" />
                       <stop offset="1" stopColor="#ffffff" stopOpacity="0" />
                    </linearGradient>
                 </defs>
              </svg>
           </div>
           
           <div className="max-w-[1400px] mx-auto px-6 relative z-20 flex flex-col">
              
              {/* HERO SECTION */}
              <div className="flex flex-col lg:flex-row items-center justify-between mb-32 gap-12 w-full">
                 
                 {/* Left Text & Icon */}
                 <div className="w-full lg:w-[45%] flex flex-col items-start text-white pt-10">
                    <h2 className="font-['Fredoka'] text-[60px] md:text-[85px] font-bold leading-tight mb-6 tracking-wide drop-shadow-[0_4px_10px_rgba(0,0,0,0.5)]">
                       1. Yapsu AI
                    </h2>
                    
                    <div className="px-8 py-2 border border-white/60 rounded-[30px] text-lg font-medium mb-10 hover:bg-white hover:text-[#0B2070] transition-colors cursor-pointer">
                       App Design
                    </div>
                    
                    <p className="text-xl md:text-2xl text-blue-50/80 leading-relaxed font-light mb-12 max-w-lg drop-shadow-sm">
                       This is an application interface design project. Yapsu AI is a modern language learning app designed for individuals seeking a natural way to practice conversations with friendly AI tutors.
                    </p>
                    
                    {/* Clean Mascot Icon */}
                    <div className="w-[160px] h-[160px] rounded-[36px] shadow-[0_20px_40px_rgba(0,0,0,0.5)] shrink-0 overflow-hidden hover:-translate-y-2 transition-transform duration-500">
                       <img src="/assets/portfolio_assets/Yapsu AI/yapsu_icon_premium.png" className="w-full h-full object-cover" />
                    </div>
                 </div>
                 
                 {/* Right 3D Floating Images - Sleek & Clean Overlap */}
                 <div className="w-full lg:w-[55%] h-[750px] relative perspective-1000 flex justify-center items-center">
                    
                    {/* Phone 1 (Back - Roadmap) */}
                    <div className="absolute top-[80px] right-[80px] w-[280px] h-[600px] bg-[#1a233a] rounded-[45px] p-[6px] shadow-[0_30px_60px_rgba(0,0,0,0.7)] border border-[#3b4768] transition-transform duration-700 ease-out hover:-translate-y-4" 
                         style={{ transform: 'rotate(12deg) rotateY(-10deg)' }}>
                       <div className="w-full h-full bg-[#111] rounded-[40px] overflow-hidden relative border-[2px] border-black">
                          <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[80px] h-[24px] bg-black rounded-full z-20"></div>
                          <img src="/assets/portfolio_assets/Yapsu AI/snapshots/roadmap_07.jpg" className="w-full h-full object-cover" />
                       </div>
                    </div>

                    {/* Phone 2 (Front - Onboarding) */}
                    <div className="absolute top-[180px] left-[60px] w-[300px] h-[640px] bg-[#1a233a] rounded-[48px] p-[8px] shadow-[[-20px_30px_60px_rgba(0,0,0,0.8)]] border border-[#4a5c88] transition-transform duration-700 ease-out hover:-translate-y-4 z-10" 
                         style={{ transform: 'rotate(10deg) rotateY(-5deg)' }}>
                       <div className="w-full h-full bg-[#111] rounded-[42px] overflow-hidden relative border-[2px] border-black">
                          <div className="absolute top-[14px] left-1/2 -translate-x-1/2 w-[85px] h-[26px] bg-black rounded-full z-20"></div>
                          <img src="/assets/portfolio_assets/Yapsu AI/snapshots/onboard_15.jpg" className="w-full h-full object-cover" />
                       </div>
                    </div>
                 </div>
              </div>

              {/* ISOMETRIC SNAPSHOTS GRID (Clean minimal bezels) */}
              <div className="w-full flex flex-col items-center mb-10">
                 <h3 className="font-['Fredoka'] text-[45px] font-bold text-white text-center mb-6 tracking-wide z-30 drop-shadow-md">Screen Flow</h3>
                 
                 <div className="relative w-full h-[650px] flex justify-center items-center overflow-hidden z-20 pointer-events-none rounded-[40px] bg-white/[0.02] border border-white/5">
                    <div className="absolute w-[1200px] h-[1200px] flex justify-center items-center perspective-[2500px] pointer-events-auto">
                       <div className="flex gap-[40px] transform rotate-x-[55deg] rotate-z-[-40deg] scale-[1.1]">
                          
                          {/* Column 1 */}
                          <div className="flex flex-col gap-[40px] -translate-y-[100px]">
                             {["onboard_04.jpg", "roleplay_18.jpg", "roadmap_07.jpg", "onboard_15.jpg"].map((src, i) => (
                                <div key={`col1-${i}`} className="relative w-[260px] h-[560px] bg-[#0c1222] rounded-[45px] p-[6px] border border-[#2a3654] transition-transform duration-500 hover:-translate-y-8" style={{ boxShadow: '-15px 15px 40px rgba(0,0,0,0.8)' }}>
                                   <div className="w-full h-full bg-[#111] rounded-[40px] overflow-hidden relative">
                                      <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[80px] h-[24px] bg-black rounded-full z-20"></div>
                                      <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover opacity-90" />
                                   </div>
                                </div>
                             ))}
                          </div>
                          
                          {/* Column 2 */}
                          <div className="flex flex-col gap-[40px]">
                             {["roleplay_10.jpg", "roadmap_05.jpg", "onboard_09.jpg", "roleplay_05.jpg"].map((src, i) => (
                                <div key={`col2-${i}`} className="relative w-[260px] h-[560px] bg-[#0c1222] rounded-[45px] p-[6px] border border-[#2a3654] transition-transform duration-500 hover:-translate-y-8" style={{ boxShadow: '-15px 15px 40px rgba(0,0,0,0.8)' }}>
                                   <div className="w-full h-full bg-[#111] rounded-[40px] overflow-hidden relative">
                                      <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[80px] h-[24px] bg-black rounded-full z-20"></div>
                                      <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover opacity-90" />
                                   </div>
                                </div>
                             ))}
                          </div>
                          
                          {/* Column 3 */}
                          <div className="flex flex-col gap-[40px] translate-y-[100px]">
                             {["roadmap_15.jpg", "roleplay_15.jpg", "onboard_20.jpg", "roadmap_10.jpg"].map((src, i) => (
                                <div key={`col3-${i}`} className="relative w-[260px] h-[560px] bg-[#0c1222] rounded-[45px] p-[6px] border border-[#2a3654] transition-transform duration-500 hover:-translate-y-8" style={{ boxShadow: '-15px 15px 40px rgba(0,0,0,0.8)' }}>
                                   <div className="w-full h-full bg-[#111] rounded-[40px] overflow-hidden relative">
                                      <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[80px] h-[24px] bg-black rounded-full z-20"></div>
                                      <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover opacity-90" />
                                   </div>
                                </div>
                             ))}
                          </div>

                       </div>
                    </div>
                 </div>
              </div>

              {/* FUNCTIONAL VIDEO MOCKUPS */}
              <div className="w-full relative z-20 pt-16">
                 <h3 className="font-['Fredoka'] text-[45px] font-bold text-white text-center mb-16 tracking-wide drop-shadow-md">Interactive Prototypes</h3>
                 <div className="flex flex-col lg:flex-row justify-center items-center gap-12 w-full">
                    
                    {[
                       { title: "Onboarding", src: "Onboarding Feature.MP4" },
                       { title: "Roleplay", src: "Roleplay Feature.MP4" },
                       { title: "Roadmap", src: "Roadmap + Drill Feature.mov" }
                    ].map((vid, idx) => (
                       <div key={idx} className="flex flex-col items-center group">
                          <h4 className="font-['Fredoka'] text-2xl mb-8 text-white/90 tracking-wide">{vid.title}</h4>
                          
                          {/* Clean Dark Mockup Frame */}
                          <div className="relative w-[280px] h-[590px] bg-[#1a233a] rounded-[48px] p-[6px] shadow-[0_20px_50px_rgba(0,0,0,0.6)] border border-[#3b4768] transition-transform duration-500 hover:-translate-y-4">
                             <div className="w-full h-full bg-black rounded-[42px] border-[2px] border-black overflow-hidden relative">
                                <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[80px] h-[24px] bg-black rounded-full z-20"></div>
                                <video src={`/assets/portfolio_assets/Yapsu AI/${vid.src}`} autoPlay muted loop playsInline className="w-full h-full object-cover" />
                             </div>
                          </div>
                       </div>
                    ))}

                 </div>
              </div>

           </div>
        </section>"""

pattern = re.compile(r'<section id="yapsu-ai".*?</section>', re.DOTALL)
content = re.sub(pattern, new_yapsu.strip(), content)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
