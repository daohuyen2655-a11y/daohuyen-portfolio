import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

new_yapsu = """
        {/* ─── 01. YAPSU AI (PURE UI - DRIBBBLE STYLE) ─── */}
        <section id="yapsu-ai" className="relative w-full py-32 bg-[#FCFBF9] text-[#334155] font-sans overflow-hidden">
           
           <div className="max-w-[1300px] mx-auto px-6 relative z-20 flex flex-col">
              
              {/* 1. PRODUCT BRIEF (HERO) */}
              <div className="flex flex-col lg:flex-row items-center justify-between mb-40 gap-16 w-full">
                 {/* Left Text & Icon */}
                 <div className="w-full lg:w-[45%] flex flex-col items-start pt-10">
                    <h2 className="font-['Fredoka'] text-[70px] md:text-[85px] font-semibold leading-[1.1] mb-6 text-[#0F172A] tracking-tight">
                       Yapsu AI
                    </h2>
                    
                    <div className="px-6 py-2 border border-orange-200 text-orange-500 rounded-full text-base font-semibold mb-8 bg-orange-50 uppercase tracking-widest">
                       App Design
                    </div>
                    
                    <p className="text-xl text-[#475569] leading-relaxed font-normal mb-12 max-w-lg">
                       This is an application interface design project. Yapsu AI is a modern language learning app designed for individuals seeking a natural way to practice conversations with friendly AI tutors.
                    </p>
                    
                    {/* Clean Mascot Icon */}
                    <div className="w-[150px] h-[150px] rounded-[32px] shadow-[0_10px_30px_rgba(0,0,0,0.05)] shrink-0 overflow-hidden bg-white border border-gray-100">
                       <img src="/assets/portfolio_assets/Yapsu AI/yapsu_icon_premium.png" className="w-full h-full object-cover" />
                    </div>
                 </div>
                 
                 {/* Right 2 Overlapping Phones - Ultra Sleek */}
                 <div className="w-full lg:w-[55%] h-[700px] relative flex justify-center items-center perspective-[2000px]">
                    
                    {/* Phone 1: Roadmap (Back) */}
                    <div className="absolute top-[60px] right-[50px] w-[290px] h-[620px] rounded-[48px] p-[6px] bg-[#E2E8F0] shadow-[0_20px_50px_-12px_rgba(0,0,0,0.15)]" 
                         style={{ transform: 'rotate(8deg)' }}>
                       <div className="w-full h-full bg-white rounded-[42px] overflow-hidden relative border border-gray-100 shadow-[inset_0_0_10px_rgba(0,0,0,0.05)]">
                          <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[90px] h-[28px] bg-black rounded-full z-20"></div>
                          <img src="/assets/portfolio_assets/Yapsu AI/snapshots/roadmap_04.jpg" className="w-full h-full object-cover" />
                       </div>
                    </div>

                    {/* Phone 2: Drill (Front) */}
                    <div className="absolute top-[140px] left-[50px] w-[310px] h-[660px] rounded-[50px] p-[6px] bg-[#F1F5F9] shadow-[[-20px_30px_60px_rgba(0,0,0,0.2)]] z-10" 
                         style={{ transform: 'rotate(-4deg)' }}>
                       <div className="w-full h-full bg-white rounded-[44px] overflow-hidden relative border border-gray-100 shadow-[inset_0_0_10px_rgba(0,0,0,0.05)]">
                          <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[95px] h-[30px] bg-black rounded-full z-20"></div>
                          <img src="/assets/portfolio_assets/Yapsu AI/snapshots/roadmap_07.jpg" className="w-full h-full object-cover" />
                       </div>
                    </div>
                 </div>
              </div>

              {/* 2. EXPERIENCE FLOW (ISOMETRIC - NO CLUNKY FRAMES, JUST RAW UI) */}
              <div className="w-full flex flex-col items-center mb-48 pt-10">
                 <h3 className="font-['Fredoka'] text-[45px] font-semibold text-[#0F172A] text-center mb-16 tracking-wide z-30 relative">
                    Experience Flow
                 </h3>
                 
                 {/* Pushed down to completely prevent overlap */}
                 <div className="relative w-full h-[650px] flex justify-center items-center overflow-visible z-20 pointer-events-none mt-20">
                    <div className="absolute w-[1200px] h-[1200px] flex justify-center items-center perspective-[2500px] pointer-events-auto">
                       <div className="flex gap-[40px] transform rotate-x-[55deg] rotate-z-[-35deg] scale-[1.0] translate-y-[100px]">
                          
                          {/* Column 1 */}
                          <div className="flex flex-col gap-[40px] translate-y-[80px]">
                             {["onboard_04.jpg", "roadmap_10.jpg"].map((src, i) => (
                                <div key={`iso1-${i}`} className="relative w-[280px] h-[600px] rounded-[32px] overflow-hidden transition-transform duration-500 hover:-translate-y-6" style={{ boxShadow: '-15px 25px 40px rgba(0,0,0,0.12)' }}>
                                   <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                                </div>
                             ))}
                          </div>
                          
                          {/* Column 2 */}
                          <div className="flex flex-col gap-[40px] -translate-y-[20px]">
                             {["roleplay_15.jpg", "onboard_09.jpg", "roadmap_15.jpg"].map((src, i) => (
                                <div key={`iso2-${i}`} className="relative w-[280px] h-[600px] rounded-[32px] overflow-hidden transition-transform duration-500 hover:-translate-y-6" style={{ boxShadow: '-15px 25px 40px rgba(0,0,0,0.12)' }}>
                                   <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                                </div>
                             ))}
                          </div>

                          {/* Column 3 */}
                          <div className="flex flex-col gap-[40px] translate-y-[40px]">
                             {["roleplay_03.jpg", "roleplay_18.jpg"].map((src, i) => (
                                <div key={`iso3-${i}`} className="relative w-[280px] h-[600px] rounded-[32px] overflow-hidden transition-transform duration-500 hover:-translate-y-6" style={{ boxShadow: '-15px 25px 40px rgba(0,0,0,0.12)' }}>
                                   <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                                </div>
                             ))}
                          </div>

                       </div>
                    </div>
                 </div>
              </div>

              {/* 3. APP DESIGN (COMPLETE INTERFACE - TIGHT FIGMA GRID) */}
              <div className="w-full flex flex-col items-center mb-48 pt-10">
                 <h3 className="font-['Fredoka'] text-[45px] font-semibold text-[#0F172A] text-center mb-16 tracking-wide">
                    App Design
                 </h3>
                 
                 <div className="grid grid-cols-2 md:grid-cols-4 gap-4 w-full px-4 max-w-[1100px]">
                    {[
                       "onboard_05.jpg", "onboard_10.jpg", "roleplay_19.jpg", "roadmap_04.jpg",
                       "roleplay_03.jpg", "roadmap_07.jpg", "onboard_21.jpg", "roleplay_18.jpg",
                       "roadmap_15.jpg", "onboard_27.jpg", "roleplay_15.jpg", "onboard_09.jpg"
                    ].map((src, i) => (
                       <div key={`flat-${i}`} className="w-full aspect-[9/19] rounded-[20px] overflow-hidden border border-gray-200/60 bg-white shadow-sm hover:shadow-xl transition-shadow duration-300">
                          <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                       </div>
                    ))}
                 </div>
              </div>

              {/* 4. LIVE PROTOTYPES */}
              <div className="w-full relative z-20 pb-48 pt-10">
                 <h3 className="font-['Fredoka'] text-[45px] font-semibold text-[#0F172A] text-center mb-24 tracking-wide">
                    Live Prototypes
                 </h3>
                 <div className="flex flex-col lg:flex-row justify-center items-center gap-16 w-full mt-10">
                    
                    {[
                       { title: "Onboarding", src: "Onboarding Feature.MP4" },
                       { title: "Roleplay", src: "Roleplay Feature.MP4" },
                       { title: "Roadmap", src: "Roadmap + Drill Feature.mov" }
                    ].map((vid, idx) => (
                       <div key={idx} className="flex flex-col items-center">
                          
                          <h4 className="font-['Fredoka'] text-[28px] mb-10 text-[#334155] font-semibold tracking-wide">
                             {vid.title}
                          </h4>
                          
                          <div className="relative w-[300px] h-[640px] rounded-[50px] p-[8px] bg-[#F1F5F9] shadow-[0_25px_50px_-12px_rgba(0,0,0,0.15)]" style={{ WebkitBoxReflect: "below 8px linear-gradient(transparent 60%, rgba(255,255,255,0.3))" }}>
                             <div className="w-full h-full bg-white rounded-[42px] overflow-hidden relative border border-gray-100 shadow-[inset_0_0_10px_rgba(0,0,0,0.05)]">
                                <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[95px] h-[30px] bg-black rounded-full z-20"></div>
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
