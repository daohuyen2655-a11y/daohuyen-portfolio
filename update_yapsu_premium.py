import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

new_yapsu = """
        {/* ─── 01. YAPSU AI (PREMIUM SHOWCASE) ─── */}
        <section id="yapsu-ai" className="relative w-full py-24 bg-gradient-to-br from-[#0B1736] via-[#10245C] to-[#1C3A8A] overflow-hidden font-sans">
           
           {/* Ref-like abstract wave background */}
           <div className="absolute inset-0 z-0 opacity-40 pointer-events-none flex items-center justify-center mix-blend-screen">
              <svg width="100%" height="100%" viewBox="0 0 1440 800" fill="none" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
                 <path d="M-100,700 C300,500 500,800 900,600 C1300,400 1500,500 1600,450" stroke="rgba(255,255,255,0.15)" strokeWidth="2" />
                 <path d="M-100,720 C320,520 520,820 920,620 C1320,420 1520,520 1620,470" stroke="rgba(255,255,255,0.1)" strokeWidth="1"/>
                 <path d="M-100,740 C340,540 540,840 940,640 C1340,440 1540,540 1640,490" stroke="rgba(255,255,255,0.05)" strokeWidth="0.5"/>
              </svg>
           </div>
           
           <div className="max-w-[1400px] mx-auto px-6 relative z-20 flex flex-col">
              
              {/* HERO SECTION */}
              <div className="flex flex-col lg:flex-row items-start justify-between mb-24 gap-12 w-full">
                 
                 {/* Left Text */}
                 <div className="w-full lg:w-1/2 flex flex-col items-start text-white pt-10">
                    <h2 className="font-['Fredoka'] text-[60px] md:text-[90px] font-bold leading-tight mb-6 tracking-wide drop-shadow-md">
                       1. Yapsu AI
                    </h2>
                    
                    <div className="px-8 py-2 border-[1.5px] border-white/80 rounded-[30px] text-lg font-medium mb-10 hover:bg-white hover:text-[#102352] transition-colors cursor-pointer tracking-wider">
                       App Design
                    </div>
                    
                    <p className="text-xl text-blue-100/90 leading-relaxed font-light mb-16 max-w-lg">
                       This is an application interface design project. Yapsu AI is a modern language learning app designed for individuals seeking a natural way to practice conversations with friendly AI tutors.
                    </p>
                    
                    {/* App Icon Uploaded by User */}
                    <div className="w-[180px] h-[180px] rounded-[40px] shadow-[0_20px_40px_rgba(0,0,0,0.5)] shrink-0 overflow-hidden border-[2px] border-white/10 hover:scale-105 transition-transform duration-500">
                       <img src="/assets/portfolio_assets/Yapsu AI/yapsu_icon_premium.png" className="w-full h-full object-cover" />
                    </div>
                 </div>
                 
                 {/* Right 3D Floating Videos - Dual Overlapping Phones like Ref 1 */}
                 <div className="w-full lg:w-1/2 h-[750px] relative perspective-1000">
                    {/* Phone 1 (Back) */}
                    <div className="absolute top-10 right-20 w-[290px] h-[600px] bg-[#1a2133] rounded-[55px] p-[10px] shadow-[0_40px_80px_rgba(0,0,0,0.8)] border border-white/20 transition-transform duration-700 ease-out hover:-translate-y-4" style={{ transform: 'rotateY(-20deg) rotateX(10deg) rotateZ(-5deg)' }}>
                       <div className="w-full h-full bg-black rounded-[45px] overflow-hidden relative border-[4px] border-black">
                          <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[90px] h-[28px] bg-black rounded-full z-20"></div>
                          <div className="absolute inset-0 bg-gradient-to-tr from-transparent via-white/5 to-white/10 z-10 pointer-events-none"></div>
                          <video src="/assets/portfolio_assets/Yapsu AI/Onboarding Feature.MP4" autoPlay muted loop playsInline className="w-full h-full object-cover opacity-80" />
                       </div>
                    </div>

                    {/* Phone 2 (Front) */}
                    <div className="absolute top-32 left-10 w-[310px] h-[640px] bg-[#1a2133] rounded-[55px] p-[10px] shadow-[[-30px_40px_80px_rgba(0,0,0,0.9)]] border border-[#405482] transition-transform duration-700 ease-out hover:-translate-y-4 z-10" style={{ transform: 'rotateY(-15deg) rotateX(5deg) rotateZ(-2deg)' }}>
                       <div className="w-full h-full bg-black rounded-[45px] overflow-hidden relative border-[4px] border-black">
                          <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[90px] h-[28px] bg-black rounded-full z-20 shadow-[inset_0_-2px_4px_rgba(255,255,255,0.1)]"></div>
                          <div className="absolute inset-0 bg-gradient-to-tr from-transparent via-white/5 to-white/20 z-10 pointer-events-none"></div>
                          <video src="/assets/portfolio_assets/Yapsu AI/Roleplay Feature.MP4" autoPlay muted loop playsInline className="w-full h-full object-cover" />
                       </div>
                    </div>
                 </div>
              </div>

              {/* ISOMETRIC SNAPSHOTS GRID (Fixed Spacing & Depth) */}
              <div className="w-full flex flex-col items-center mb-10">
                 <h3 className="font-['Fredoka'] text-[45px] font-bold text-white text-center mb-6 tracking-wide z-30">Screen Flow</h3>
                 
                 {/* Fixed Height Container to prevent massive DOM gaps */}
                 <div className="relative w-full h-[650px] flex justify-center items-center overflow-hidden z-20 pointer-events-none rounded-[40px] bg-white/5 border border-white/10 backdrop-blur-sm">
                    {/* Absolute positioned 3D Grid */}
                    <div className="absolute w-[1200px] h-[1200px] flex justify-center items-center perspective-[2000px] pointer-events-auto">
                       <div className="flex gap-[40px] transform rotate-x-[55deg] rotate-z-[-40deg] scale-[1.15]">
                          
                          {/* Column 1 */}
                          <div className="flex flex-col gap-[40px] -translate-y-[100px]">
                             {["onboard_04.jpg", "roleplay_18.jpg", "roadmap_07.jpg", "onboard_15.jpg"].map((src, i) => (
                                <div key={`col1-${i}`} className="relative w-[240px] h-[520px] bg-[#111A2C] rounded-[45px] p-[8px] transition-transform duration-500 hover:-translate-y-8" style={{ boxShadow: '-12px 12px 0px #091221, -25px 25px 50px rgba(0,0,0,0.8)' }}>
                                   <div className="w-full h-full bg-black rounded-[38px] overflow-hidden">
                                      <div className="absolute top-[8px] left-1/2 -translate-x-1/2 w-[70px] h-[20px] bg-black rounded-b-[12px] z-20"></div>
                                      <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                                   </div>
                                </div>
                             ))}
                          </div>
                          
                          {/* Column 2 */}
                          <div className="flex flex-col gap-[40px]">
                             {["roleplay_10.jpg", "roadmap_05.jpg", "onboard_09.jpg", "roleplay_05.jpg"].map((src, i) => (
                                <div key={`col2-${i}`} className="relative w-[240px] h-[520px] bg-[#111A2C] rounded-[45px] p-[8px] transition-transform duration-500 hover:-translate-y-8" style={{ boxShadow: '-12px 12px 0px #091221, -25px 25px 50px rgba(0,0,0,0.8)' }}>
                                   <div className="w-full h-full bg-black rounded-[38px] overflow-hidden">
                                      <div className="absolute top-[8px] left-1/2 -translate-x-1/2 w-[70px] h-[20px] bg-black rounded-b-[12px] z-20"></div>
                                      <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                                   </div>
                                </div>
                             ))}
                          </div>
                          
                          {/* Column 3 */}
                          <div className="flex flex-col gap-[40px] translate-y-[100px]">
                             {["roadmap_15.jpg", "roleplay_15.jpg", "onboard_20.jpg", "roadmap_10.jpg"].map((src, i) => (
                                <div key={`col3-${i}`} className="relative w-[240px] h-[520px] bg-[#111A2C] rounded-[45px] p-[8px] transition-transform duration-500 hover:-translate-y-8" style={{ boxShadow: '-12px 12px 0px #091221, -25px 25px 50px rgba(0,0,0,0.8)' }}>
                                   <div className="w-full h-full bg-black rounded-[38px] overflow-hidden">
                                      <div className="absolute top-[8px] left-1/2 -translate-x-1/2 w-[70px] h-[20px] bg-black rounded-b-[12px] z-20"></div>
                                      <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
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
                 <h3 className="font-['Fredoka'] text-[45px] font-bold text-white text-center mb-16 tracking-wide">Interactive Prototypes</h3>
                 <div className="flex flex-col lg:flex-row justify-center items-center gap-14 w-full">
                    
                    {[
                       { title: "Onboarding", src: "Onboarding Feature.MP4" },
                       { title: "Roleplay", src: "Roleplay Feature.MP4" },
                       { title: "Roadmap", src: "Roadmap + Drill Feature.mov" }
                    ].map((vid, idx) => (
                       <div key={idx} className="flex flex-col items-center group">
                          <h4 className="font-['Fredoka'] text-2xl mb-8 text-white/90 tracking-wide">{vid.title}</h4>
                          
                          {/* Premium Hardware Mockup Frame */}
                          <div className="relative w-[280px] h-[590px] bg-[#1F2942] rounded-[55px] p-[8px] shadow-[0_30px_60px_rgba(0,0,0,0.5)] border border-[#3A4A70] transition-transform duration-500 hover:-translate-y-4" style={{ boxShadow: 'inset 0 0 10px rgba(255,255,255,0.1), 0 30px 60px rgba(0,0,0,0.5)' }}>
                             
                             {/* Hardware Buttons */}
                             <div className="absolute top-[110px] -left-[2px] w-[3px] h-[25px] bg-[#3A4A70] rounded-l-md"></div>
                             <div className="absolute top-[150px] -left-[2px] w-[3px] h-[50px] bg-[#3A4A70] rounded-l-md"></div>
                             <div className="absolute top-[210px] -left-[2px] w-[3px] h-[50px] bg-[#3A4A70] rounded-l-md"></div>
                             <div className="absolute top-[160px] -right-[2px] w-[3px] h-[75px] bg-[#3A4A70] rounded-r-md"></div>

                             <div className="w-full h-full bg-black rounded-[48px] border-[5px] border-black overflow-hidden relative">
                                <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[85px] h-[26px] bg-black rounded-full z-20"></div>
                                <div className="absolute inset-0 bg-gradient-to-tr from-transparent via-white/5 to-white/10 z-10 pointer-events-none"></div>
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
