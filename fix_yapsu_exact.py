import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

new_yapsu = """
        {/* ─── 01. YAPSU AI (CLEAN PREMIUM - BUGS FIXED EXACTLY) ─── */}
        <section id="yapsu-ai" className="relative w-full py-32 bg-[#FCFAF8] text-[#1E293B] overflow-hidden font-sans">
           
           <style dangerouslySetInnerHTML={{__html: `
              .reflect-glass {
                 -webkit-box-reflect: below 8px linear-gradient(transparent 70%, rgba(255,255,255,0.4));
              }
           `}} />

           {/* Abstract Soft Background Accents (Kept very subtle) */}
           <div className="absolute top-[-10%] right-[-5%] w-[800px] h-[800px] bg-orange-300/10 rounded-full blur-[120px] pointer-events-none z-0"></div>
           <div className="absolute bottom-[20%] left-[-10%] w-[600px] h-[600px] bg-blue-300/10 rounded-full blur-[100px] pointer-events-none z-0"></div>
           
           <div className="max-w-[1400px] mx-auto px-6 relative z-20 flex flex-col">
              
              {/* 1. PRODUCT BRIEF (HERO) */}
              <div className="flex flex-col lg:flex-row items-center justify-between mb-48 gap-12 w-full">
                 {/* Left Text & Icon */}
                 <div className="w-full lg:w-[45%] flex flex-col items-start pt-10 relative z-20">
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
                    
                    {/* Phone 1: ROADMAP */}
                    <div className="absolute top-[80px] right-[80px] w-[290px] h-[620px] bg-white rounded-[50px] p-[8px] shadow-[0_30px_60px_rgba(0,0,0,0.15)] border border-gray-200 transition-transform duration-700 ease-out hover:-translate-y-4" 
                         style={{ transform: 'rotate(10deg)' }}>
                       <div className="w-full h-full bg-gray-50 rounded-[42px] overflow-hidden relative border border-gray-100">
                          <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[85px] h-[26px] bg-black rounded-full z-20"></div>
                          <img src="/assets/portfolio_assets/Yapsu AI/snapshots/roadmap_04.jpg" className="w-full h-full object-cover" />
                       </div>
                    </div>

                    {/* Phone 2: AMAZING DRILL */}
                    <div className="absolute top-[160px] left-[60px] w-[310px] h-[660px] bg-white rounded-[52px] p-[10px] shadow-[[-20px_40px_80px_rgba(0,0,0,0.2)]] border border-gray-100 transition-transform duration-700 ease-out hover:-translate-y-4 z-10" 
                         style={{ transform: 'rotate(-5deg)' }}>
                       <div className="w-full h-full bg-gray-50 rounded-[42px] overflow-hidden relative border border-gray-200">
                          <div className="absolute top-[14px] left-1/2 -translate-x-1/2 w-[90px] h-[28px] bg-black rounded-full z-20"></div>
                          <img src="/assets/portfolio_assets/Yapsu AI/snapshots/roadmap_07.jpg" className="w-full h-full object-cover" />
                       </div>
                    </div>
                 </div>
              </div>

              {/* 2. FLOW OVERVIEW (TEXT KHÔNG BỊ CHE KHUẤT) */}
              <div className="w-full flex flex-col items-center mb-48 pt-20">
                 {/* Text is pushed up and grid is pushed down to guarantee no overlap */}
                 <h3 className="font-['Fredoka'] text-[45px] font-bold text-[#1A202C] text-center mb-4 tracking-wide z-30 relative">Experience Flow</h3>
                 
                 <div className="relative w-full h-[750px] flex justify-center items-center overflow-visible z-20 pointer-events-none mt-24">
                    <div className="absolute w-[1200px] h-[1200px] flex justify-center items-center perspective-[2000px] pointer-events-auto">
                       <div className="flex gap-[60px] transform rotate-x-[55deg] rotate-z-[-35deg] scale-[1.05] translate-y-[60px]">
                          
                          {/* Column 1 */}
                          <div className="flex flex-col gap-[60px] translate-y-[80px]">
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
                          <div className="flex flex-col gap-[60px] -translate-y-[20px]">
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

              {/* 3. TOÀN BỘ SCREEN LÀM APP DESIGN (ĐA DẠNG MÀU SẮC NHẤT) */}
              <div className="w-full flex flex-col items-center mb-40 pt-10">
                 <h3 className="font-['Fredoka'] text-[45px] font-bold text-[#1A202C] text-center mb-16 tracking-wide">App Design</h3>
                 
                 <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-6 w-full px-4">
                    {[
                       "onboard_05.jpg",   // Brilliant Green Mascot
                       "onboard_10.jpg",   // Boy with bill / Money
                       "roleplay_19.jpg",  // Detailed Chat Interface
                       "roadmap_04.jpg",   // Clean White Roadmap
                       "roleplay_03.jpg",  // Select Tutor List
                       "roadmap_07.jpg",   // Achievement/Amazing Drill
                       "onboard_21.jpg",   // Orange header setup
                       "roleplay_18.jpg",  // Light Chat
                       "roadmap_15.jpg",   // Detailed Lesson View
                       "onboard_27.jpg",   // Settings/Options
                       "roleplay_15.jpg",  // Feedback Modal
                       "onboard_09.jpg"    // Vibrant Blue Setup
                    ].map((src, i) => (
                       <div key={`flat-${i}`} className="w-full aspect-[9/19] rounded-2xl overflow-hidden shadow-lg border border-gray-200 bg-white hover:scale-105 transition-transform duration-300">
                          <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                       </div>
                    ))}
                 </div>
              </div>

              {/* 4. INTERACTIVE PROTOTYPES (CHỮ RÕ RÀNG, KHÔNG BỊ CHÌM) */}
              <div className="w-full relative z-20 pb-48 pt-10">
                 <h3 className="font-['Fredoka'] text-[45px] font-bold text-[#1A202C] text-center mb-20 tracking-wide">Live Prototypes</h3>
                 <div className="flex flex-col lg:flex-row justify-center items-center gap-16 w-full mt-10">
                    
                    {[
                       { title: "Onboarding", src: "Onboarding Feature.MP4" },
                       { title: "Roleplay", src: "Roleplay Feature.MP4" },
                       { title: "Roadmap", src: "Roadmap + Drill Feature.mov" }
                    ].map((vid, idx) => (
                       <div key={idx} className="flex flex-col items-center group">
                          
                          {/* 1. Moved text to TOP and made it bolder & larger so it's impossible to sink */}
                          <h4 className="font-['Fredoka'] text-3xl mb-8 text-[#1A202C] font-extrabold tracking-wide drop-shadow-sm">
                             {vid.title}
                          </h4>
                          
                          <div className="relative w-[300px] h-[620px] bg-white rounded-[55px] p-[10px] shadow-[0_30px_60px_rgba(0,0,0,0.12)] border border-gray-200 transition-transform duration-500 hover:-translate-y-4 reflect-glass">
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
