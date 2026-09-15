import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

new_yapsu = """
        {/* ─── 01. YAPSU AI (ELEGANT, CLEAN, PIXEL-PERFECT) ─── */}
        <section id="yapsu-ai" className="relative w-full py-32 bg-[#FCFBF9] text-[#334155] font-sans">
           
           <style dangerouslySetInnerHTML={{__html: `
              .reflect-glass {
                 -webkit-box-reflect: below 12px linear-gradient(transparent 60%, rgba(255,255,255,0.3));
              }
              .clean-shadow {
                 box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.08);
              }
           `}} />

           {/* Pure minimal background, no noisy glowing orbs */}
           
           <div className="max-w-[1300px] mx-auto px-6 relative z-20 flex flex-col">
              
              {/* 1. PRODUCT BRIEF (HERO) */}
              <div className="flex flex-col lg:flex-row items-center justify-between mb-40 gap-16 w-full">
                 {/* Left Text & Icon */}
                 <div className="w-full lg:w-[45%] flex flex-col items-start pt-10">
                    <h2 className="font-['Fredoka'] text-[60px] md:text-[80px] font-semibold leading-tight mb-6 text-[#1E293B]">
                       1. Yapsu AI
                    </h2>
                    
                    <div className="px-6 py-2 border border-orange-200 text-orange-500 rounded-full text-base font-medium mb-8 bg-orange-50/50 uppercase tracking-wide">
                       App Design
                    </div>
                    
                    <p className="text-xl text-[#64748B] leading-relaxed font-light mb-12 max-w-lg">
                       This is an application interface design project. Yapsu AI is a modern language learning app designed for individuals seeking a natural way to practice conversations with friendly AI tutors.
                    </p>
                    
                    {/* Clean Mascot Icon */}
                    <div className="w-[160px] h-[160px] rounded-[36px] shadow-sm shrink-0 overflow-hidden bg-white border border-gray-100">
                       <img src="/assets/portfolio_assets/Yapsu AI/yapsu_icon_premium.png" className="w-full h-full object-cover" />
                    </div>
                 </div>
                 
                 {/* Right 2 Overlapping Phones - Clean & Elegant */}
                 <div className="w-full lg:w-[55%] h-[700px] relative flex justify-center items-center perspective-[2000px]">
                    
                    {/* Phone 1: Roadmap (Back) */}
                    <div className="absolute top-[60px] right-[40px] w-[290px] h-[620px] bg-white rounded-[50px] p-[8px] clean-shadow border border-gray-200" 
                         style={{ transform: 'rotate(8deg) scale(0.95)' }}>
                       <div className="w-full h-full bg-gray-50 rounded-[42px] overflow-hidden relative border border-gray-100">
                          <div className="absolute top-[14px] left-1/2 -translate-x-1/2 w-[100px] h-[30px] bg-black rounded-full z-20"></div>
                          <img src="/assets/portfolio_assets/Yapsu AI/snapshots/roadmap_04.jpg" className="w-full h-full object-cover" />
                       </div>
                    </div>

                    {/* Phone 2: Drill (Front) */}
                    <div className="absolute top-[140px] left-[40px] w-[310px] h-[660px] bg-white/95 backdrop-blur-sm rounded-[54px] p-[10px] shadow-[[-20px_30px_60px_rgba(0,0,0,0.12)]] border border-gray-100 z-10" 
                         style={{ transform: 'rotate(-4deg)' }}>
                       <div className="w-full h-full bg-gray-50 rounded-[44px] overflow-hidden relative border border-gray-200">
                          <div className="absolute top-[14px] left-1/2 -translate-x-1/2 w-[110px] h-[32px] bg-black rounded-full z-20"></div>
                          <img src="/assets/portfolio_assets/Yapsu AI/snapshots/roadmap_07.jpg" className="w-full h-full object-cover" />
                       </div>
                    </div>
                 </div>
              </div>

              {/* 2. EXPERIENCE FLOW (ISOMETRIC) */}
              <div className="w-full flex flex-col items-center mb-48 pt-10">
                 <h3 className="font-['Fredoka'] text-[45px] font-semibold text-[#1E293B] text-center mb-24 tracking-wide z-30 relative">
                    Experience Flow
                 </h3>
                 
                 {/* Massive gap added via mt-10 and scale reduction to guarantee NO OVERLAP */}
                 <div className="relative w-full h-[700px] flex justify-center items-center overflow-visible z-20 pointer-events-none mt-10">
                    <div className="absolute w-[1200px] h-[1200px] flex justify-center items-center perspective-[2500px] pointer-events-auto">
                       <div className="flex gap-[60px] transform rotate-x-[55deg] rotate-z-[-35deg] scale-[0.95] translate-y-[80px]">
                          
                          {/* Column 1 */}
                          <div className="flex flex-col gap-[60px] translate-y-[80px]">
                             {["onboard_04.jpg", "roadmap_10.jpg"].map((src, i) => (
                                <div key={`iso1-${i}`} className="relative w-[300px] h-[640px] bg-white rounded-[50px] p-[8px] clean-shadow border border-gray-200">
                                   <div className="w-full h-full bg-gray-50 rounded-[42px] overflow-hidden relative">
                                      <div className="absolute top-[14px] left-1/2 -translate-x-1/2 w-[110px] h-[32px] bg-black rounded-full z-20"></div>
                                      <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                                   </div>
                                </div>
                             ))}
                          </div>
                          
                          {/* Column 2 */}
                          <div className="flex flex-col gap-[60px] -translate-y-[20px]">
                             {["roleplay_15.jpg", "onboard_09.jpg", "roadmap_15.jpg"].map((src, i) => (
                                <div key={`iso2-${i}`} className="relative w-[300px] h-[640px] bg-white rounded-[50px] p-[8px] clean-shadow border border-gray-200">
                                   <div className="w-full h-full bg-gray-50 rounded-[42px] overflow-hidden relative">
                                      <div className="absolute top-[14px] left-1/2 -translate-x-1/2 w-[110px] h-[32px] bg-black rounded-full z-20"></div>
                                      <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                                   </div>
                                </div>
                             ))}
                          </div>

                          {/* Column 3 */}
                          <div className="flex flex-col gap-[60px] translate-y-[40px]">
                             {["roleplay_03.jpg", "roleplay_18.jpg"].map((src, i) => (
                                <div key={`iso3-${i}`} className="relative w-[300px] h-[640px] bg-white rounded-[50px] p-[8px] clean-shadow border border-gray-200">
                                   <div className="w-full h-full bg-gray-50 rounded-[42px] overflow-hidden relative">
                                      <div className="absolute top-[14px] left-1/2 -translate-x-1/2 w-[110px] h-[32px] bg-black rounded-full z-20"></div>
                                      <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                                   </div>
                                </div>
                             ))}
                          </div>

                       </div>
                    </div>
                 </div>
              </div>

              {/* 3. APP DESIGN (COMPLETE INTERFACE) */}
              <div className="w-full flex flex-col items-center mb-48 pt-10">
                 <h3 className="font-['Fredoka'] text-[45px] font-semibold text-[#1E293B] text-center mb-16 tracking-wide">
                    App Design
                 </h3>
                 
                 <div className="grid grid-cols-2 md:grid-cols-4 gap-8 w-full px-4 max-w-[1100px]">
                    {[
                       "onboard_05.jpg",   // Green Mascot
                       "onboard_10.jpg",   // Blue / Boy
                       "roleplay_19.jpg",  // Detailed Chat
                       "roadmap_04.jpg",   // Clean White Roadmap
                       "roleplay_03.jpg",  // Select Tutor Modal
                       "roadmap_07.jpg",   // Drill Completion
                       "onboard_21.jpg",   // Orange Header
                       "roleplay_18.jpg"   // Light Chat
                    ].map((src, i) => (
                       <div key={`flat-${i}`} className="w-full aspect-[9/19] rounded-[28px] overflow-hidden shadow-sm border border-gray-200 bg-white hover:shadow-lg transition-shadow duration-300">
                          <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                       </div>
                    ))}
                 </div>
              </div>

              {/* 4. LIVE PROTOTYPES */}
              <div className="w-full relative z-20 pb-48 pt-10">
                 <h3 className="font-['Fredoka'] text-[45px] font-semibold text-[#1E293B] text-center mb-24 tracking-wide">
                    Live Prototypes
                 </h3>
                 <div className="flex flex-col lg:flex-row justify-center items-center gap-16 w-full mt-10">
                    
                    {[
                       { title: "Onboarding", src: "Onboarding Feature.MP4" },
                       { title: "Roleplay", src: "Roleplay Feature.MP4" },
                       { title: "Roadmap", src: "Roadmap + Drill Feature.mov" }
                    ].map((vid, idx) => (
                       <div key={idx} className="flex flex-col items-center">
                          
                          {/* Elegant, medium-weight text positioned safely above the phone */}
                          <h4 className="font-['Fredoka'] text-[28px] mb-12 text-[#334155] font-medium tracking-wide">
                             {vid.title}
                          </h4>
                          
                          <div className="relative w-[310px] h-[660px] bg-white rounded-[54px] p-[10px] clean-shadow border border-gray-200 reflect-glass">
                             <div className="w-full h-full bg-gray-50 rounded-[44px] overflow-hidden relative border border-gray-100">
                                <div className="absolute top-[14px] left-1/2 -translate-x-1/2 w-[110px] h-[32px] bg-black rounded-full z-20"></div>
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
