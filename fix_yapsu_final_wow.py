import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

new_yapsu = """
        {/* ─── 01. YAPSU AI (THE ULTIMATE LIGHT PREMIUM WOW) ─── */}
        <section id="yapsu-ai" className="relative w-full py-32 bg-[#FCFAF8] text-[#1E293B] overflow-hidden font-sans">
           
           <style dangerouslySetInnerHTML={{__html: `
              @keyframes float-hero {
                 0%, 100% { transform: translateY(0px) rotate(12deg); }
                 50% { transform: translateY(-20px) rotate(12deg); }
              }
              @keyframes float-hero-front {
                 0%, 100% { transform: translateY(0px) rotate(-6deg); }
                 50% { transform: translateY(-25px) rotate(-6deg); }
              }
              @keyframes float-iso {
                 0%, 100% { transform: translateY(0px); }
                 50% { transform: translateY(-20px); }
              }
              .glass-mockup {
                 background: rgba(255, 255, 255, 0.6);
                 backdrop-filter: blur(20px);
                 -webkit-backdrop-filter: blur(20px);
                 border: 1.5px solid rgba(255, 255, 255, 0.9);
                 box-shadow: 0 40px 80px rgba(0,0,0,0.08), inset 0 0 20px rgba(255,255,255,0.8);
              }
              .reflect-glass {
                 -webkit-box-reflect: below 8px linear-gradient(transparent 60%, rgba(255,255,255,0.6));
              }
           `}} />

           {/* Ethereal Glowing Background Orbs (Yapsu Amber/Orange) - Bigger & Brighter */}
           <div className="absolute top-[-5%] right-[-5%] w-[1000px] h-[1000px] bg-gradient-to-br from-orange-400/25 to-amber-300/15 rounded-full blur-[160px] pointer-events-none z-0"></div>
           <div className="absolute top-[35%] left-[-15%] w-[800px] h-[800px] bg-gradient-to-tr from-blue-400/20 to-cyan-300/15 rounded-full blur-[140px] pointer-events-none z-0"></div>
           
           <div className="max-w-[1400px] mx-auto px-6 relative z-20 flex flex-col">
              
              {/* 1. PRODUCT BRIEF (HERO) */}
              <div className="flex flex-col lg:flex-row items-center justify-between mb-48 gap-12 w-full">
                 {/* Left Text & Icon */}
                 <div className="w-full lg:w-[45%] flex flex-col items-start pt-10 relative z-20">
                    <h2 className="font-['Fredoka'] text-[80px] md:text-[110px] font-black leading-[0.9] mb-8 text-transparent bg-clip-text bg-gradient-to-r from-orange-500 via-amber-500 to-yellow-500 drop-shadow-sm tracking-tight">
                       Yapsu AI.
                    </h2>
                    
                    <div className="px-8 py-2 border-[2px] border-orange-500 text-orange-600 rounded-full text-lg font-bold mb-10 bg-orange-50/80 shadow-[0_0_30px_rgba(249,115,22,0.2)] uppercase tracking-widest backdrop-blur-md">
                       App Design
                    </div>
                    
                    <p className="text-2xl text-gray-600 leading-relaxed font-normal mb-12 max-w-lg">
                       Master languages naturally. Yapsu AI connects you with friendly AI tutors for seamless, real-time roleplay conversations.
                    </p>
                    
                    {/* Clean & Vibrant Mascot Icon */}
                    <div className="w-[180px] h-[180px] rounded-[45px] shadow-[0_30px_60px_rgba(249,115,22,0.25)] shrink-0 overflow-hidden bg-white hover:scale-105 transition-transform duration-500 relative group z-10 border-[3px] border-white">
                       <img src="/assets/portfolio_assets/Yapsu AI/yapsu_icon_premium.png" className="w-full h-full object-cover relative z-0" />
                    </div>
                 </div>
                 
                 {/* Right 2 Overlapping Floating Phones (Roadmap & Amazing Drill) */}
                 <div className="w-full lg:w-[55%] h-[800px] relative flex justify-center items-center perspective-[2000px]">
                    
                    {/* Back Phone (Roadmap - highest visual complexity) */}
                    <div className="absolute top-[60px] right-[40px] w-[320px] h-[670px] rounded-[60px] p-[10px] glass-mockup" 
                         style={{ animation: 'float-hero 8s ease-in-out infinite' }}>
                       <div className="w-full h-full bg-white rounded-[50px] overflow-hidden relative border-[2px] border-gray-100 shadow-[inset_0_0_10px_rgba(0,0,0,0.05)]">
                          <div className="absolute top-[14px] left-1/2 -translate-x-1/2 w-[95px] h-[30px] bg-black/90 backdrop-blur-md rounded-full z-20 shadow-sm"></div>
                          <img src="/assets/portfolio_assets/Yapsu AI/snapshots/roadmap_04.jpg" className="w-full h-full object-cover" />
                       </div>
                    </div>

                    {/* Front Phone (Amazing Drill / Colorful Screen) */}
                    <div className="absolute top-[200px] left-[20px] w-[340px] h-[720px] rounded-[60px] p-[10px] glass-mockup shadow-[[-30px_50px_100px_rgba(0,0,0,0.15)]] z-10" 
                         style={{ animation: 'float-hero-front 7s ease-in-out infinite' }}>
                       <div className="w-full h-full bg-white rounded-[50px] overflow-hidden relative border-[2px] border-gray-100 shadow-[inset_0_0_10px_rgba(0,0,0,0.05)]">
                          <div className="absolute top-[15px] left-1/2 -translate-x-1/2 w-[100px] h-[32px] bg-black/90 backdrop-blur-md rounded-full z-20 shadow-sm"></div>
                          {/* Super subtle beautiful light glare */}
                          <div className="absolute -top-[50%] -left-[50%] w-[200%] h-[200%] bg-gradient-to-tr from-transparent via-transparent to-white/40 rotate-[35deg] pointer-events-none z-10"></div>
                          <img src="/assets/portfolio_assets/Yapsu AI/snapshots/onboard_09.jpg" className="w-full h-full object-cover" />
                       </div>
                    </div>
                 </div>
              </div>

              {/* 2. VÀI SCREEN UI TRẢI DỌC TRONG MOCKUP (ISOMETRIC FLOW) */}
              <div className="w-full flex flex-col items-center mb-48 pt-20">
                 <h3 className="font-['Fredoka'] text-[60px] font-black text-[#1A202C] text-center mb-4 tracking-tight z-30 relative">Experience Flow</h3>
                 <p className="text-2xl text-gray-500 mb-10 z-30 relative font-light">A seamless journey through language mastery.</p>
                 
                 <div className="relative w-full h-[800px] flex justify-center items-center overflow-visible z-20 pointer-events-none mt-10">
                    <div className="absolute w-[1200px] h-[1200px] flex justify-center items-center perspective-[2500px] pointer-events-auto">
                       <div className="flex gap-[70px] transform rotate-x-[55deg] rotate-z-[-35deg] scale-[1.15] translate-y-[80px]">
                          
                          {/* Left Column (Lower) */}
                          <div className="flex flex-col gap-[70px] translate-y-[100px]" style={{ animation: 'float-iso 6s ease-in-out infinite' }}>
                             {["roleplay_18.jpg", "roadmap_07.jpg"].map((src, i) => (
                                <div key={`iso1-${i}`} className="relative w-[320px] h-[680px] rounded-[60px] p-[10px] glass-mockup transition-transform duration-500 hover:-translate-y-8" style={{ boxShadow: '-25px 35px 60px rgba(0,0,0,0.1)' }}>
                                   <div className="w-full h-full bg-white rounded-[50px] overflow-hidden relative border border-gray-100">
                                      <div className="absolute top-[15px] left-1/2 -translate-x-1/2 w-[95px] h-[30px] bg-black/90 rounded-full z-20"></div>
                                      <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                                   </div>
                                </div>
                             ))}
                          </div>
                          
                          {/* Middle Column (Higher) */}
                          <div className="flex flex-col gap-[70px] -translate-y-[60px]" style={{ animation: 'float-iso 7s ease-in-out infinite 0.5s' }}>
                             {["onboard_10.jpg", "roleplay_19.jpg", "roadmap_15.jpg"].map((src, i) => (
                                <div key={`iso2-${i}`} className="relative w-[320px] h-[680px] rounded-[60px] p-[10px] glass-mockup transition-transform duration-500 hover:-translate-y-8" style={{ boxShadow: '-25px 35px 60px rgba(0,0,0,0.1)' }}>
                                   <div className="w-full h-full bg-white rounded-[50px] overflow-hidden relative border border-gray-100">
                                      <div className="absolute top-[15px] left-1/2 -translate-x-1/2 w-[95px] h-[30px] bg-black/90 rounded-full z-20"></div>
                                      <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                                   </div>
                                </div>
                             ))}
                          </div>

                          {/* Right Column (Lower) */}
                          <div className="flex flex-col gap-[70px] translate-y-[60px]" style={{ animation: 'float-iso 6.5s ease-in-out infinite 1s' }}>
                             {["onboard_05.jpg", "roleplay_03.jpg"].map((src, i) => (
                                <div key={`iso3-${i}`} className="relative w-[320px] h-[680px] rounded-[60px] p-[10px] glass-mockup transition-transform duration-500 hover:-translate-y-8" style={{ boxShadow: '-25px 35px 60px rgba(0,0,0,0.1)' }}>
                                   <div className="w-full h-full bg-white rounded-[50px] overflow-hidden relative border border-gray-100">
                                      <div className="absolute top-[15px] left-1/2 -translate-x-1/2 w-[95px] h-[30px] bg-black/90 rounded-full z-20"></div>
                                      <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                                   </div>
                                </div>
                             ))}
                          </div>

                       </div>
                    </div>
                 </div>
              </div>

              {/* 3. TOÀN BỘ SCREEN LÀM APP DESIGN (CURATED DISTINCT SCREENS) */}
              <div className="w-full flex flex-col items-center mb-48 pt-20">
                 <div className="w-full max-w-[800px] text-center mb-20">
                    <h3 className="font-['Fredoka'] text-[60px] font-black text-[#1A202C] tracking-tight mb-4">Complete Interface</h3>
                    <p className="text-2xl text-gray-500 font-light">A comprehensive view of the most distinct and colorful crafted screens.</p>
                 </div>
                 
                 <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-6 w-full px-4">
                    {[
                       "onboard_09.jpg",   // Massive blue vibrant screen
                       "roadmap_04.jpg",   // Clean white detailed roadmap
                       "roleplay_19.jpg",  // Chat interface dark/complex
                       "onboard_10.jpg",   // Bright blue boy holding bill
                       "onboard_05.jpg",   // Bright green mascot
                       "roleplay_03.jpg",  // Distinct UI modal
                       "roadmap_07.jpg",   // Achievement/drill screen
                       "onboard_21.jpg",   // Setup distinct
                       "roleplay_18.jpg",  // Chat with modal
                       "roadmap_15.jpg",   // Detailed list view
                       "onboard_27.jpg",   // Another highly distinct screen
                       "roleplay_15.jpg"   // Different chat state
                    ].map((src, i) => (
                       <div key={`flat-${i}`} className="w-full aspect-[9/19] rounded-[30px] overflow-hidden shadow-[0_15px_30px_rgba(0,0,0,0.06)] bg-white hover:shadow-[0_25px_50px_rgba(0,0,0,0.12)] hover:-translate-y-2 transition-all duration-300 cursor-pointer border border-gray-100">
                          <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                       </div>
                    ))}
                 </div>
              </div>

              {/* 4. INTERACTIVE PROTOTYPES (MASSIVE TITLES, CLEAR REFLECTIONS) */}
              <div className="w-full relative z-20 pb-48 pt-10">
                 <h3 className="font-['Fredoka'] text-[60px] font-black text-[#1A202C] text-center mb-24 tracking-tight">Live Prototypes</h3>
                 <div className="flex flex-col lg:flex-row justify-center items-center gap-20 w-full mt-10">
                    
                    {[
                       { title: "Onboarding", src: "Onboarding Feature.MP4" },
                       { title: "Roleplay", src: "Roleplay Feature.MP4" },
                       { title: "Roadmap", src: "Roadmap + Drill Feature.mov" }
                    ].map((vid, idx) => (
                       <div key={idx} className="flex flex-col items-center group">
                          
                          {/* Super Bold & Gradient Title so it pops massively */}
                          <div className="mb-12 px-8 py-3 bg-white/80 backdrop-blur-md rounded-full shadow-[0_10px_20px_rgba(0,0,0,0.05)] border border-gray-100">
                             <h4 className="font-['Fredoka'] text-3xl font-black text-transparent bg-clip-text bg-gradient-to-r from-orange-500 to-amber-500 tracking-wide uppercase">
                                {vid.title}
                             </h4>
                          </div>
                          
                          <div className="relative w-[340px] h-[720px] glass-mockup rounded-[65px] p-[12px] reflect-glass transition-transform duration-500 hover:-translate-y-4">
                             <div className="w-full h-full bg-white rounded-[55px] border-[2px] border-gray-100 overflow-hidden relative shadow-[inset_0_0_15px_rgba(0,0,0,0.05)]">
                                <div className="absolute top-[16px] left-1/2 -translate-x-1/2 w-[100px] h-[32px] bg-black/90 backdrop-blur-md rounded-full z-20 shadow-sm"></div>
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
