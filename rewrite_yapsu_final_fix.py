import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

new_yapsu = """
        {/* ─── 01. YAPSU AI (FINAL FIX: GRADIENT FADE + 8-COLUMN GRID) ─── */}
        <section id="yapsu-ai" className="relative w-full py-32 bg-[#FCFBF9] text-[#334155] font-sans">
           
           <div className="max-w-[1600px] mx-auto px-4 sm:px-8 relative z-20 flex flex-col">
              
              {/* 1. PRODUCT BRIEF (HERO) */}
              <div className="flex flex-col lg:flex-row items-center justify-between mb-32 gap-16 w-full max-w-[1400px] mx-auto">
                 {/* Left Text & Icon */}
                 <div className="w-full lg:w-[45%] flex flex-col items-start pt-10">
                    <h2 className="font-['Fredoka'] text-[70px] md:text-[85px] font-bold leading-tight mb-6 text-transparent bg-clip-text bg-gradient-to-r from-orange-500 to-amber-400 drop-shadow-sm tracking-tight">
                       Yapsu AI
                    </h2>
                    
                    <div className="px-6 py-2 border border-orange-200 text-orange-500 rounded-full text-base font-semibold mb-8 bg-orange-50 uppercase tracking-widest shadow-sm">
                       App Design
                    </div>
                    
                    <p className="text-xl text-[#475569] leading-relaxed font-normal mb-12 max-w-lg">
                       This is an application interface design project. Yapsu AI is a modern language learning app designed for individuals seeking a natural way to practice conversations with friendly AI tutors.
                    </p>
                    
                    {/* Clean Mascot Icon */}
                    <div className="w-[160px] h-[160px] rounded-[36px] shadow-[0_15px_40px_rgba(0,0,0,0.08)] shrink-0 overflow-hidden bg-white border border-gray-100 hover:-translate-y-2 transition-transform duration-500">
                       <img src="/assets/portfolio_assets/Yapsu AI/yapsu_icon_premium.png" className="w-full h-full object-cover" />
                    </div>
                 </div>
                 
                 {/* Right 2 Overlapping Phones */}
                 <div className="w-full lg:w-[55%] h-[700px] relative flex justify-center items-center perspective-[2000px]">
                    <div className="absolute top-[60px] right-[50px] w-[290px] h-[620px] rounded-[48px] p-[6px] bg-white border border-gray-200 shadow-[0_20px_50px_-12px_rgba(0,0,0,0.15)]" style={{ transform: 'rotate(8deg)' }}>
                       <div className="w-full h-full bg-gray-50 rounded-[42px] overflow-hidden relative border border-gray-100">
                          <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[90px] h-[28px] bg-black rounded-full z-20"></div>
                          <img src="/assets/portfolio_assets/Yapsu AI/snapshots/roadmap_04.jpg" className="w-full h-full object-cover" />
                       </div>
                    </div>
                    <div className="absolute top-[140px] left-[50px] w-[310px] h-[660px] rounded-[50px] p-[6px] bg-white border border-gray-200 shadow-[[-20px_30px_60px_rgba(0,0,0,0.15)]] z-10" style={{ transform: 'rotate(-4deg)' }}>
                       <div className="w-full h-full bg-gray-50 rounded-[44px] overflow-hidden relative border border-gray-100">
                          <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[95px] h-[30px] bg-black rounded-full z-20"></div>
                          <img src="/assets/portfolio_assets/Yapsu AI/snapshots/roadmap_07.jpg" className="w-full h-full object-cover" />
                       </div>
                    </div>
                 </div>
              </div>

              {/* 2. EXPERIENCE FLOW (FADE MASK - NO RECTANGLE SLICE, NO OVERLAP) */}
              <div className="w-full flex flex-col items-center mt-20 relative max-w-[1400px] mx-auto">
                 <h3 className="font-['Fredoka'] text-[50px] font-bold text-transparent bg-clip-text bg-gradient-to-r from-orange-500 to-amber-400 text-center mb-10 tracking-wide z-30 drop-shadow-sm">
                    Experience Flow
                 </h3>
                 
                 {/* The gradient mask makes the top and bottom fade into transparency, so it never looks like a harsh cut, while overflow-hidden prevents bleeding! */}
                 <div className="relative w-[100vw] max-w-[100vw] h-[1000px] flex justify-center items-center overflow-hidden z-20 pointer-events-none" 
                      style={{ WebkitMaskImage: 'linear-gradient(to bottom, transparent 0%, black 15%, black 85%, transparent 100%)', maskImage: 'linear-gradient(to bottom, transparent 0%, black 15%, black 85%, transparent 100%)' }}>
                    
                    <div className="absolute w-[2200px] flex justify-center items-center perspective-[2500px]">
                       <div className="flex gap-[50px] transform rotate-x-[55deg] rotate-z-[-35deg] scale-[0.8] translate-y-[100px]">
                          
                          {/* Column 1 */}
                          <div className="flex flex-col gap-[50px] translate-y-[150px]">
                             {["onboard_04.jpg", "roadmap_10.jpg", "roleplay_03.jpg", "onboard_21.jpg"].map((src, i) => (
                                <div key={`iso1-${i}`} className="relative w-[280px] h-[600px] rounded-[45px] p-[6px] bg-white border border-gray-200 shadow-[0_20px_40px_rgba(0,0,0,0.1)] transition-transform duration-500 hover:-translate-y-8">
                                   <div className="w-full h-full bg-gray-50 rounded-[40px] overflow-hidden relative border border-gray-100">
                                      <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[85px] h-[26px] bg-black rounded-full z-20"></div>
                                      <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                                   </div>
                                </div>
                             ))}
                          </div>
                          
                          {/* Column 2 */}
                          <div className="flex flex-col gap-[50px] -translate-y-[50px]">
                             {["roleplay_15.jpg", "onboard_09.jpg", "roadmap_15.jpg", "roleplay_19.jpg"].map((src, i) => (
                                <div key={`iso2-${i}`} className="relative w-[280px] h-[600px] rounded-[45px] p-[6px] bg-white border border-gray-200 shadow-[0_20px_40px_rgba(0,0,0,0.1)] transition-transform duration-500 hover:-translate-y-8">
                                   <div className="w-full h-full bg-gray-50 rounded-[40px] overflow-hidden relative border border-gray-100">
                                      <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[85px] h-[26px] bg-black rounded-full z-20"></div>
                                      <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                                   </div>
                                </div>
                             ))}
                          </div>

                          {/* Column 3 */}
                          <div className="flex flex-col gap-[50px] translate-y-[100px]">
                             {["roadmap_07.jpg", "roleplay_18.jpg", "onboard_05.jpg", "onboard_10.jpg"].map((src, i) => (
                                <div key={`iso3-${i}`} className="relative w-[280px] h-[600px] rounded-[45px] p-[6px] bg-white border border-gray-200 shadow-[0_20px_40px_rgba(0,0,0,0.1)] transition-transform duration-500 hover:-translate-y-8">
                                   <div className="w-full h-full bg-gray-50 rounded-[40px] overflow-hidden relative border border-gray-100">
                                      <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[85px] h-[26px] bg-black rounded-full z-20"></div>
                                      <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                                   </div>
                                </div>
                             ))}
                          </div>

                          {/* Column 4 */}
                          <div className="flex flex-col gap-[50px] -translate-y-[20px]">
                             {["onboard_27.jpg", "roadmap_04.jpg", "roleplay_09.jpg", "roadmap_20.jpg"].map((src, i) => (
                                <div key={`iso4-${i}`} className="relative w-[280px] h-[600px] rounded-[45px] p-[6px] bg-white border border-gray-200 shadow-[0_20px_40px_rgba(0,0,0,0.1)] transition-transform duration-500 hover:-translate-y-8">
                                   <div className="w-full h-full bg-gray-50 rounded-[40px] overflow-hidden relative border border-gray-100">
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

              {/* 3. APP DESIGN (2 ROWS X 8 COLUMNS = 16 COMPLETELY DISTINCT SCREENS) */}
              <div className="w-full flex flex-col items-center mt-32 mb-48 pt-10">
                 <h3 className="font-['Fredoka'] text-[50px] font-bold text-transparent bg-clip-text bg-gradient-to-r from-orange-500 to-amber-400 text-center mb-16 tracking-wide drop-shadow-sm">
                    App Design
                 </h3>
                 
                 <div className="grid grid-cols-2 md:grid-cols-4 xl:grid-cols-8 gap-4 w-full">
                    {[
                       // Row 1 (8 completely distinct screens)
                       "onboard_15.jpg",   // Green Splash
                       "roleplay_19.jpg",  // Dark Chat Dense
                       "onboard_09.jpg",   // Blue boy
                       "roadmap_04.jpg",   // White clean map
                       "roleplay_03.jpg",  // Avatar selection cards
                       "onboard_10.jpg",   // Orange bill boy
                       "roadmap_07.jpg",   // Drill completion (green accents)
                       "onboard_21.jpg",   // Orange header setup
                       
                       // Row 2 (8 completely distinct screens)
                       "onboard_05.jpg",   // Green mascot greeting
                       "roleplay_15.jpg",  // Feedback modal
                       "roadmap_20.jpg",   // Map alt
                       "roleplay_05.jpg",  // Tutor list
                       "onboard_27.jpg",   // Settings options
                       "roleplay_18.jpg",  // Light chat
                       "roadmap_15.jpg",   // Detailed list
                       "onboard_04.jpg"    // Clean white list
                    ].map((src, i) => (
                       <div key={`flat-${i}`} className="w-full aspect-[9/19] rounded-[24px] overflow-hidden shadow-sm border border-gray-200 bg-white hover:shadow-xl transition-shadow duration-300">
                          <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                       </div>
                    ))}
                 </div>
              </div>

              {/* 4. LIVE PROTOTYPES (TYPOGRAPHY IN BOXES AS REQUESTED) */}
              <div className="w-full relative z-20 pb-48 pt-10 max-w-[1400px] mx-auto">
                 <h3 className="font-['Fredoka'] text-[50px] font-bold text-transparent bg-clip-text bg-gradient-to-r from-orange-500 to-amber-400 text-center mb-24 tracking-wide drop-shadow-sm">
                    Live Prototypes
                 </h3>
                 
                 <div className="flex flex-col lg:flex-row justify-center items-center gap-16 w-full mt-10">
                    
                    {[
                       { title: "Onboarding", src: "Onboarding Feature.MP4" },
                       { title: "Roleplay", src: "Roleplay Feature.MP4" },
                       { title: "Roadmap", src: "Roadmap + Drill Feature.mov" }
                    ].map((vid, idx) => (
                       <div key={idx} className="flex flex-col items-center">
                          
                          {/* Typography in a flexible box instead of raw gradient text */}
                          <div className="mb-10 px-8 py-3 bg-white rounded-2xl shadow-sm border border-gray-200 flex items-center justify-center">
                             <h4 className="font-['Fredoka'] text-[24px] font-bold text-[#334155] tracking-wide">
                                {vid.title}
                             </h4>
                          </div>
                          
                          <div className="relative w-[310px] h-[660px] rounded-[52px] p-[8px] bg-white border border-gray-200 shadow-[0_25px_50px_-12px_rgba(0,0,0,0.15)]" style={{ WebkitBoxReflect: "below 12px linear-gradient(transparent 60%, rgba(255,255,255,0.4))" }}>
                             <div className="w-full h-full bg-gray-50 rounded-[44px] overflow-hidden relative border border-gray-100 shadow-[inset_0_0_10px_rgba(0,0,0,0.05)]">
                                <div className="absolute top-[14px] left-1/2 -translate-x-1/2 w-[100px] h-[30px] bg-black rounded-full z-20"></div>
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
