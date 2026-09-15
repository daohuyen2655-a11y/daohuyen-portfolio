import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

new_yapsu = """
        {/* ─── 01. YAPSU AI (FINAL PREMIUM LIGHT MODE) ─── */}
        <section id="yapsu-ai" className="relative w-full py-32 bg-[#FCFBF8] text-[#1E293B] overflow-hidden font-sans">
           
           {/* Abstract Soft Background Accents (Yapsu Brand Colors) */}
           <div className="absolute top-[-10%] right-[-5%] w-[800px] h-[800px] bg-orange-300/20 rounded-full blur-[120px] pointer-events-none"></div>
           <div className="absolute bottom-[20%] left-[-10%] w-[600px] h-[600px] bg-blue-300/20 rounded-full blur-[100px] pointer-events-none"></div>
           
           <div className="max-w-[1400px] mx-auto px-6 relative z-20 flex flex-col">
              
              {/* 1. PRODUCT BRIEF (HERO) */}
              <div className="flex flex-col lg:flex-row items-center justify-between mb-40 gap-12 w-full">
                 {/* Left Text & Icon */}
                 <div className="w-full lg:w-[45%] flex flex-col items-start pt-10">
                    <h2 className="font-['Fredoka'] text-[60px] md:text-[85px] font-bold leading-tight mb-6 text-[#1A202C] drop-shadow-sm">
                       1. Yapsu AI
                    </h2>
                    
                    <div className="px-8 py-2 border-[1.5px] border-orange-500 text-orange-600 rounded-[30px] text-lg font-medium mb-10 bg-orange-50/50">
                       App Design
                    </div>
                    
                    <p className="text-xl md:text-2xl text-gray-600 leading-relaxed font-light mb-12 max-w-lg">
                       This is an application interface design project. Yapsu AI is a modern language learning app designed for individuals seeking a natural way to practice conversations with friendly AI tutors.
                    </p>
                    
                    {/* Clean Mascot Icon */}
                    <div className="w-[180px] h-[180px] rounded-[40px] shadow-[0_20px_40px_rgba(0,0,0,0.08)] shrink-0 overflow-hidden bg-white border border-gray-100 hover:-translate-y-2 transition-transform duration-500">
                       <img src="/assets/portfolio_assets/Yapsu AI/yapsu_icon_premium.png" className="w-full h-full object-cover" />
                    </div>
                 </div>
                 
                 {/* Right 2 Overlapping Static Phones */}
                 <div className="w-full lg:w-[55%] h-[750px] relative flex justify-center items-center perspective-1000">
                    {/* Back Phone */}
                    <div className="absolute top-[80px] right-[80px] w-[290px] h-[620px] bg-white rounded-[50px] p-[8px] shadow-[0_30px_60px_rgba(0,0,0,0.15)] border border-gray-200 transition-transform duration-700 ease-out hover:-translate-y-4" 
                         style={{ transform: 'rotate(10deg)' }}>
                       <div className="w-full h-full bg-gray-50 rounded-[42px] overflow-hidden relative border border-gray-100">
                          <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[85px] h-[26px] bg-black rounded-full z-20"></div>
                          <img src="/assets/portfolio_assets/Yapsu AI/snapshots/roadmap_07.jpg" className="w-full h-full object-cover" />
                       </div>
                    </div>

                    {/* Front Phone */}
                    <div className="absolute top-[160px] left-[60px] w-[310px] h-[660px] bg-white/90 backdrop-blur-md rounded-[52px] p-[10px] shadow-[[-20px_40px_80px_rgba(0,0,0,0.2)]] border border-white transition-transform duration-700 ease-out hover:-translate-y-4 z-10" 
                         style={{ transform: 'rotate(-5deg)' }}>
                       <div className="w-full h-full bg-gray-50 rounded-[42px] overflow-hidden relative border border-gray-200">
                          <div className="absolute top-[14px] left-1/2 -translate-x-1/2 w-[90px] h-[28px] bg-black rounded-full z-20"></div>
                          <img src="/assets/portfolio_assets/Yapsu AI/snapshots/onboard_15.jpg" className="w-full h-full object-cover" />
                       </div>
                    </div>
                 </div>
              </div>

              {/* 2. VÀI SCREEN UI TRẢI DỌC TRONG MOCKUP (ISOMETRIC FLOW) */}
              <div className="w-full flex flex-col items-center mb-40">
                 <h3 className="font-['Fredoka'] text-[45px] font-bold text-[#1A202C] text-center mb-10 tracking-wide">Flow Overview</h3>
                 
                 <div className="relative w-full h-[700px] flex justify-center items-center overflow-hidden z-20 pointer-events-none">
                    <div className="absolute w-[1200px] h-[1200px] flex justify-center items-center perspective-[2000px] pointer-events-auto">
                       <div className="flex gap-[60px] transform rotate-x-[55deg] rotate-z-[-35deg] scale-[1.05]">
                          
                          {/* Column 1 */}
                          <div className="flex flex-col gap-[60px] -translate-y-[120px]">
                             {["onboard_04.jpg", "roadmap_07.jpg", "roleplay_15.jpg"].map((src, i) => (
                                <div key={`col1-${i}`} className="relative w-[280px] h-[600px] bg-white rounded-[45px] p-[8px] transition-transform duration-500 hover:-translate-y-8 border border-gray-100" style={{ boxShadow: '-20px 20px 40px rgba(0,0,0,0.08)' }}>
                                   <div className="w-full h-full bg-gray-50 rounded-[38px] overflow-hidden relative">
                                      <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[85px] h-[26px] bg-black rounded-full z-20"></div>
                                      <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                                   </div>
                                </div>
                             ))}
                          </div>
                          
                          {/* Column 2 */}
                          <div className="flex flex-col gap-[60px]">
                             {["roleplay_10.jpg", "onboard_09.jpg", "roadmap_15.jpg"].map((src, i) => (
                                <div key={`col2-${i}`} className="relative w-[280px] h-[600px] bg-white rounded-[45px] p-[8px] transition-transform duration-500 hover:-translate-y-8 border border-gray-100" style={{ boxShadow: '-20px 20px 40px rgba(0,0,0,0.08)' }}>
                                   <div className="w-full h-full bg-gray-50 rounded-[38px] overflow-hidden relative">
                                      <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[85px] h-[26px] bg-black rounded-full z-20"></div>
                                      <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                                   </div>
                                </div>
                             ))}
                          </div>

                       </div>
                    </div>
                 </div>
              </div>

              {/* 3. TOÀN BỘ SCREEN LÀM APP DESIGN (RAW FLAT GRID) */}
              <div className="w-full flex flex-col items-center mb-40">
                 <h3 className="font-['Fredoka'] text-[45px] font-bold text-[#1A202C] text-center mb-16 tracking-wide">App Design</h3>
                 
                 {/* Massive Flat Grid simulating Figma canvas */}
                 <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-6 w-full px-4">
                    {[
                       "onboard_04.jpg", "onboard_09.jpg", "onboard_15.jpg", "onboard_20.jpg",
                       "roleplay_05.jpg", "roleplay_10.jpg", "roleplay_15.jpg", "roleplay_18.jpg",
                       "roadmap_05.jpg", "roadmap_07.jpg", "roadmap_10.jpg", "roadmap_15.jpg"
                    ].map((src, i) => (
                       <div key={`flat-${i}`} className="w-full aspect-[9/19] rounded-2xl overflow-hidden shadow-lg border border-gray-200 bg-white hover:scale-105 transition-transform duration-300">
                          <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                       </div>
                    ))}
                 </div>
              </div>

              {/* 4. INTERACTIVE PROTOTYPES (FUNCTIONAL VIDEOS) */}
              <div className="w-full relative z-20">
                 <h3 className="font-['Fredoka'] text-[45px] font-bold text-[#1A202C] text-center mb-20 tracking-wide">Interactive Prototypes</h3>
                 <div className="flex flex-col lg:flex-row justify-center items-center gap-16 w-full">
                    
                    {[
                       { title: "Onboarding", src: "Onboarding Feature.MP4" },
                       { title: "Roleplay", src: "Roleplay Feature.MP4" },
                       { title: "Roadmap", src: "Roadmap + Drill Feature.mov" }
                    ].map((vid, idx) => (
                       <div key={idx} className="flex flex-col items-center group">
                          <h4 className="font-['Fredoka'] text-2xl mb-8 text-gray-700 font-medium tracking-wide">{vid.title}</h4>
                          
                          {/* Clean Light-Mode Prototype Mockup */}
                          <div className="relative w-[300px] h-[620px] bg-white rounded-[55px] p-[10px] shadow-[0_30px_60px_rgba(0,0,0,0.12)] border border-gray-200 transition-transform duration-500 hover:-translate-y-4">
                             <div className="w-full h-full bg-gray-50 rounded-[45px] border-[2px] border-gray-100 overflow-hidden relative">
                                <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[90px] h-[28px] bg-black rounded-full z-20"></div>
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
