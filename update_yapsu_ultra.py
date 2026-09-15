import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

new_yapsu = """
        {/* ─── 01. YAPSU AI (ULTRA PREMIUM SHOWCASE) ─── */}
        <section id="yapsu-ai" className="relative w-full py-32 overflow-hidden font-sans">
           
           {/* Deep Radial Glowing Background */}
           <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_30%_50%,_#1B3B90_0%,_#0B2070_40%,_#040B28_100%)] z-0"></div>
           
           {/* Complex Elegant Wavy Lines (Bottom Left) */}
           <div className="absolute bottom-[-10%] left-[-10%] w-[120%] h-[700px] z-0 pointer-events-none mix-blend-screen opacity-70">
              <svg width="100%" height="100%" viewBox="0 0 1440 600" fill="none" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
                 <path d="M-200,500 C100,650 400,250 900,400 C1300,550 1400,200 1600,250" stroke="url(#waveGrad)" strokeWidth="1.5" />
                 <path d="M-200,520 C120,670 420,270 920,420 C1320,570 1420,220 1620,270" stroke="url(#waveGrad)" strokeWidth="1.2" opacity="0.8"/>
                 <path d="M-200,540 C140,690 440,290 940,440 C1340,590 1440,240 1640,290" stroke="url(#waveGrad)" strokeWidth="0.9" opacity="0.6"/>
                 <path d="M-200,560 C160,710 460,310 960,460 C1360,610 1460,260 1660,310" stroke="url(#waveGrad)" strokeWidth="0.6" opacity="0.4"/>
                 <path d="M-200,580 C180,730 480,330 980,480 C1380,630 1480,280 1680,330" stroke="url(#waveGrad)" strokeWidth="0.3" opacity="0.2"/>
                 <defs>
                    <linearGradient id="waveGrad" x1="0" y1="0" x2="1440" y2="600" gradientUnits="userSpaceOnUse">
                       <stop stopColor="#ffffff" stopOpacity="0.1" />
                       <stop offset="0.3" stopColor="#ffffff" stopOpacity="0.8" />
                       <stop offset="0.7" stopColor="#ffffff" stopOpacity="0.6" />
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
                    <h2 className="font-['Fredoka'] text-[60px] md:text-[85px] font-bold leading-tight mb-6 tracking-wide drop-shadow-[0_0_20px_rgba(255,255,255,0.3)]">
                       1. Yapsu AI
                    </h2>
                    
                    <div className="px-10 py-3 border-[2px] border-white rounded-[40px] text-xl font-medium mb-10 hover:bg-white hover:text-[#0B2070] transition-colors cursor-pointer shadow-[0_0_15px_rgba(255,255,255,0.2)]">
                       App Design
                    </div>
                    
                    <p className="text-xl md:text-2xl text-blue-50 leading-relaxed font-light mb-16 max-w-lg drop-shadow-md">
                       This is an application interface design project. Yapsu AI is a modern language learning app designed for individuals seeking a natural way to practice conversations with friendly AI tutors.
                    </p>
                    
                    {/* Glowing Mascot Icon */}
                    <div className="flex flex-col items-center">
                       <div className="w-[200px] h-[200px] rounded-[50px] shadow-[0_30px_60px_rgba(0,0,0,0.6),_0_0_80px_rgba(255,160,0,0.5)] shrink-0 overflow-hidden border-[2px] border-white/20 hover:scale-105 transition-transform duration-500 bg-white">
                          <img src="/assets/portfolio_assets/Yapsu AI/yapsu_icon_premium.png" className="w-full h-full object-cover scale-[1.02]" />
                       </div>
                       <h3 className="font-['Fredoka'] text-3xl font-black text-transparent bg-clip-text bg-gradient-to-b from-white to-gray-400 mt-8 tracking-widest drop-shadow-[0_4px_4px_rgba(0,0,0,0.5)]">
                          YAPSU AI
                       </h3>
                    </div>
                 </div>
                 
                 {/* Right 3D Floating Videos - Highly Realistic Silver iPhones */}
                 <div className="w-full lg:w-[55%] h-[800px] relative perspective-[1500px]">
                    
                    {/* Phone 1 (Back) */}
                    <div className="absolute top-[80px] right-[40px] w-[320px] h-[660px] rounded-[60px] p-[12px] shadow-[0_50px_100px_rgba(0,0,0,0.8)] transition-transform duration-700 ease-out hover:-translate-y-6" 
                         style={{ background: 'linear-gradient(135deg, #f5f7fa 0%, #b8c6db 100%)', transform: 'rotateY(-25deg) rotateX(12deg) rotateZ(-8deg)' }}>
                       {/* Hardware buttons */}
                       <div className="absolute top-[130px] -left-[3px] w-[4px] h-[30px] bg-[#a0aabf] rounded-l-md"></div>
                       <div className="absolute top-[180px] -left-[3px] w-[4px] h-[55px] bg-[#a0aabf] rounded-l-md"></div>
                       <div className="absolute top-[250px] -left-[3px] w-[4px] h-[55px] bg-[#a0aabf] rounded-l-md"></div>
                       <div className="absolute top-[190px] -right-[3px] w-[4px] h-[80px] bg-[#a0aabf] rounded-r-md"></div>
                       
                       <div className="w-full h-full bg-black rounded-[48px] overflow-hidden relative border-[5px] border-black shadow-[inset_0_0_20px_rgba(0,0,0,0.8)]">
                          <div className="absolute top-[14px] left-1/2 -translate-x-1/2 w-[100px] h-[30px] bg-black rounded-full z-20 shadow-[inset_0_-2px_4px_rgba(255,255,255,0.15)]"></div>
                          {/* Apple-style Sharp Diagonal Glare */}
                          <div className="absolute -top-[50%] -left-[50%] w-[200%] h-[200%] bg-gradient-to-tr from-transparent via-transparent to-white/30 rotate-[35deg] pointer-events-none z-10 mix-blend-overlay"></div>
                          <video src="/assets/portfolio_assets/Yapsu AI/Onboarding Feature.MP4" autoPlay muted loop playsInline className="w-full h-full object-cover opacity-90" />
                       </div>
                    </div>

                    {/* Phone 2 (Front) */}
                    <div className="absolute top-[220px] left-[50px] w-[340px] h-[700px] rounded-[60px] p-[12px] shadow-[[-40px_60px_100px_rgba(0,0,0,0.9)]] transition-transform duration-700 ease-out hover:-translate-y-6 z-10" 
                         style={{ background: 'linear-gradient(135deg, #ffffff 0%, #c3cfe2 100%)', transform: 'rotateY(-15deg) rotateX(8deg) rotateZ(-4deg)' }}>
                       {/* Hardware buttons */}
                       <div className="absolute top-[140px] -left-[3px] w-[4px] h-[32px] bg-[#b1bace] rounded-l-md"></div>
                       <div className="absolute top-[190px] -left-[3px] w-[4px] h-[60px] bg-[#b1bace] rounded-l-md"></div>
                       <div className="absolute top-[265px] -left-[3px] w-[4px] h-[60px] bg-[#b1bace] rounded-l-md"></div>
                       <div className="absolute top-[200px] -right-[3px] w-[4px] h-[85px] bg-[#b1bace] rounded-r-md"></div>

                       <div className="w-full h-full bg-black rounded-[50px] overflow-hidden relative border-[6px] border-black shadow-[inset_0_0_20px_rgba(0,0,0,0.8)]">
                          <div className="absolute top-[15px] left-1/2 -translate-x-1/2 w-[105px] h-[32px] bg-black rounded-full z-20 shadow-[inset_0_-2px_4px_rgba(255,255,255,0.2)]"></div>
                          {/* Apple-style Sharp Diagonal Glare */}
                          <div className="absolute -top-[50%] -left-[50%] w-[200%] h-[200%] bg-gradient-to-tr from-transparent via-transparent to-white/40 rotate-[30deg] pointer-events-none z-10 mix-blend-overlay"></div>
                          <video src="/assets/portfolio_assets/Yapsu AI/Roleplay Feature.MP4" autoPlay muted loop playsInline className="w-full h-full object-cover" />
                       </div>
                    </div>
                 </div>
              </div>

              {/* ISOMETRIC SNAPSHOTS GRID */}
              <div className="w-full flex flex-col items-center mb-10">
                 <h3 className="font-['Fredoka'] text-[45px] font-bold text-white text-center mb-10 tracking-wide z-30 drop-shadow-md">Screen Flow</h3>
                 
                 <div className="relative w-full h-[650px] flex justify-center items-center overflow-hidden z-20 pointer-events-none">
                    <div className="absolute w-[1200px] h-[1200px] flex justify-center items-center perspective-[2500px] pointer-events-auto">
                       <div className="flex gap-[50px] transform rotate-x-[55deg] rotate-z-[-40deg] scale-[1.15]">
                          
                          {/* Column 1 */}
                          <div className="flex flex-col gap-[50px] -translate-y-[100px]">
                             {["onboard_04.jpg", "roleplay_18.jpg", "roadmap_07.jpg", "onboard_15.jpg"].map((src, i) => (
                                <div key={`col1-${i}`} className="relative w-[260px] h-[560px] rounded-[50px] p-[8px] transition-transform duration-500 hover:-translate-y-8" style={{ background: 'linear-gradient(135deg, #e2e8f0 0%, #94a3b8 100%)', boxShadow: '-12px 12px 0px #091221, -30px 30px 60px rgba(0,0,0,0.9)' }}>
                                   <div className="w-full h-full bg-black rounded-[42px] overflow-hidden relative">
                                      <div className="absolute top-[10px] left-1/2 -translate-x-1/2 w-[80px] h-[24px] bg-black rounded-full z-20"></div>
                                      <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                                      <div className="absolute inset-0 bg-gradient-to-tr from-transparent to-white/10 z-10 pointer-events-none mix-blend-overlay"></div>
                                   </div>
                                </div>
                             ))}
                          </div>
                          
                          {/* Column 2 */}
                          <div className="flex flex-col gap-[50px]">
                             {["roleplay_10.jpg", "roadmap_05.jpg", "onboard_09.jpg", "roleplay_05.jpg"].map((src, i) => (
                                <div key={`col2-${i}`} className="relative w-[260px] h-[560px] rounded-[50px] p-[8px] transition-transform duration-500 hover:-translate-y-8" style={{ background: 'linear-gradient(135deg, #e2e8f0 0%, #94a3b8 100%)', boxShadow: '-12px 12px 0px #091221, -30px 30px 60px rgba(0,0,0,0.9)' }}>
                                   <div className="w-full h-full bg-black rounded-[42px] overflow-hidden relative">
                                      <div className="absolute top-[10px] left-1/2 -translate-x-1/2 w-[80px] h-[24px] bg-black rounded-full z-20"></div>
                                      <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                                      <div className="absolute inset-0 bg-gradient-to-tr from-transparent to-white/10 z-10 pointer-events-none mix-blend-overlay"></div>
                                   </div>
                                </div>
                             ))}
                          </div>
                          
                          {/* Column 3 */}
                          <div className="flex flex-col gap-[50px] translate-y-[100px]">
                             {["roadmap_15.jpg", "roleplay_15.jpg", "onboard_20.jpg", "roadmap_10.jpg"].map((src, i) => (
                                <div key={`col3-${i}`} className="relative w-[260px] h-[560px] rounded-[50px] p-[8px] transition-transform duration-500 hover:-translate-y-8" style={{ background: 'linear-gradient(135deg, #e2e8f0 0%, #94a3b8 100%)', boxShadow: '-12px 12px 0px #091221, -30px 30px 60px rgba(0,0,0,0.9)' }}>
                                   <div className="w-full h-full bg-black rounded-[42px] overflow-hidden relative">
                                      <div className="absolute top-[10px] left-1/2 -translate-x-1/2 w-[80px] h-[24px] bg-black rounded-full z-20"></div>
                                      <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                                      <div className="absolute inset-0 bg-gradient-to-tr from-transparent to-white/10 z-10 pointer-events-none mix-blend-overlay"></div>
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
                 <h3 className="font-['Fredoka'] text-[45px] font-bold text-white text-center mb-20 tracking-wide drop-shadow-md">Interactive Prototypes</h3>
                 <div className="flex flex-col lg:flex-row justify-center items-center gap-16 w-full">
                    
                    {[
                       { title: "Onboarding", src: "Onboarding Feature.MP4" },
                       { title: "Roleplay", src: "Roleplay Feature.MP4" },
                       { title: "Roadmap", src: "Roadmap + Drill Feature.mov" }
                    ].map((vid, idx) => (
                       <div key={idx} className="flex flex-col items-center group">
                          <h4 className="font-['Fredoka'] text-2xl mb-8 text-white/90 tracking-wide">{vid.title}</h4>
                          
                          {/* Ultra Premium Silver iPhone Mockup Frame */}
                          <div className="relative w-[300px] h-[620px] rounded-[60px] p-[10px] shadow-[0_40px_80px_rgba(0,0,0,0.7)] border border-gray-100 transition-transform duration-500 hover:-translate-y-6" 
                               style={{ background: 'linear-gradient(135deg, #ffffff 0%, #b8c6db 100%)' }}>
                             
                             {/* Hardware Buttons */}
                             <div className="absolute top-[120px] -left-[3px] w-[4px] h-[28px] bg-[#9ca3af] rounded-l-md"></div>
                             <div className="absolute top-[170px] -left-[3px] w-[4px] h-[55px] bg-[#9ca3af] rounded-l-md"></div>
                             <div className="absolute top-[240px] -left-[3px] w-[4px] h-[55px] bg-[#9ca3af] rounded-l-md"></div>
                             <div className="absolute top-[180px] -right-[3px] w-[4px] h-[80px] bg-[#9ca3af] rounded-r-md"></div>

                             <div className="w-full h-full bg-black rounded-[50px] border-[5px] border-black overflow-hidden relative shadow-[inset_0_0_15px_rgba(0,0,0,0.8)]">
                                <div className="absolute top-[14px] left-1/2 -translate-x-1/2 w-[95px] h-[30px] bg-black rounded-full z-20 shadow-[inset_0_-2px_4px_rgba(255,255,255,0.2)]"></div>
                                {/* Apple-style Sharp Diagonal Glare */}
                                <div className="absolute -top-[50%] -left-[50%] w-[200%] h-[200%] bg-gradient-to-tr from-transparent via-transparent to-white/30 rotate-[35deg] pointer-events-none z-10 mix-blend-overlay"></div>
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
