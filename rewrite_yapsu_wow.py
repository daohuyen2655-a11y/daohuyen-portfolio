import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

new_yapsu = """
        {/* ─── 01. YAPSU AI (THE "WOW" FACTOR - ULTRA POLISHED) ─── */}
        <section id="yapsu-ai" className="relative w-full py-32 bg-[#FAF9F6] text-[#1E293B] overflow-hidden font-sans">
           
           <style dangerouslySetInnerHTML={{__html: `
              @keyframes float-hero {
                 0%, 100% { transform: translateY(0px) rotate(10deg); }
                 50% { transform: translateY(-15px) rotate(11deg); }
              }
              @keyframes float-hero-front {
                 0%, 100% { transform: translateY(0px) rotate(-5deg); }
                 50% { transform: translateY(-20px) rotate(-4deg); }
              }
              @keyframes float-iso {
                 0%, 100% { transform: translateY(0px); }
                 50% { transform: translateY(-15px); }
              }
              .reflect-glass {
                 -webkit-box-reflect: below 4px linear-gradient(transparent 60%, rgba(255,255,255,0.4));
              }
           `}} />

           {/* Ethereal Glowing Background Orbs (Yapsu Amber/Orange) */}
           <div className="absolute top-0 right-0 w-[800px] h-[800px] bg-gradient-to-br from-orange-400/20 to-amber-300/10 rounded-full blur-[150px] pointer-events-none"></div>
           <div className="absolute top-[40%] left-[-10%] w-[600px] h-[600px] bg-gradient-to-tr from-blue-400/15 to-cyan-300/10 rounded-full blur-[120px] pointer-events-none"></div>
           
           <div className="max-w-[1400px] mx-auto px-6 relative z-20 flex flex-col">
              
              {/* 1. PRODUCT BRIEF (HERO) */}
              <div className="flex flex-col lg:flex-row items-center justify-between mb-48 gap-12 w-full">
                 {/* Left Text & Icon */}
                 <div className="w-full lg:w-[45%] flex flex-col items-start pt-10">
                    <h2 className="font-['Fredoka'] text-[70px] md:text-[95px] font-black leading-tight mb-6 text-transparent bg-clip-text bg-gradient-to-r from-orange-500 via-amber-500 to-yellow-500 drop-shadow-sm tracking-tight">
                       Yapsu AI.
                    </h2>
                    
                    <div className="px-8 py-2 border-[2px] border-orange-500 text-orange-600 rounded-full text-lg font-bold mb-10 bg-orange-50/80 shadow-[0_0_20px_rgba(249,115,22,0.15)] uppercase tracking-widest">
                       App Design
                    </div>
                    
                    <p className="text-2xl text-gray-600 leading-relaxed font-normal mb-12 max-w-lg">
                       Master languages naturally. Yapsu AI connects you with friendly AI tutors for seamless, real-time roleplay conversations.
                    </p>
                    
                    {/* Floating Premium Mascot Icon */}
                    <div className="w-[180px] h-[180px] rounded-[45px] shadow-[0_30px_60px_rgba(249,115,22,0.2)] shrink-0 overflow-hidden bg-white border border-white hover:scale-105 transition-transform duration-500 relative group">
                       <div className="absolute inset-0 bg-gradient-to-tr from-orange-400/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 z-10"></div>
                       <img src="/assets/portfolio_assets/Yapsu AI/yapsu_icon_premium.png" className="w-full h-full object-cover relative z-0" />
                    </div>
                 </div>
                 
                 {/* Right 2 Overlapping Floating Phones (Hyper-realistic) */}
                 <div className="w-full lg:w-[55%] h-[750px] relative flex justify-center items-center perspective-[2000px]">
                    
                    {/* Back Phone */}
                    <div className="absolute top-[80px] right-[80px] w-[300px] h-[630px] rounded-[60px] p-[10px] shadow-[0_40px_80px_rgba(0,0,0,0.15)] bg-gradient-to-br from-gray-100 to-gray-300 border border-white" 
                         style={{ animation: 'float-hero 8s ease-in-out infinite' }}>
                       <div className="w-full h-full bg-black rounded-[50px] overflow-hidden relative border-[6px] border-black shadow-[inset_0_0_15px_rgba(0,0,0,0.5)]">
                          <div className="absolute top-[14px] left-1/2 -translate-x-1/2 w-[90px] h-[28px] bg-black rounded-full z-20"></div>
                          <img src="/assets/portfolio_assets/Yapsu AI/snapshots/roadmap_07.jpg" className="w-full h-full object-cover" />
                       </div>
                    </div>

                    {/* Front Phone */}
                    <div className="absolute top-[180px] left-[60px] w-[320px] h-[670px] rounded-[60px] p-[10px] shadow-[[-30px_50px_100px_rgba(0,0,0,0.25)]] bg-gradient-to-br from-white to-gray-200 border border-white z-10" 
                         style={{ animation: 'float-hero-front 7s ease-in-out infinite' }}>
                       <div className="w-full h-full bg-black rounded-[50px] overflow-hidden relative border-[6px] border-black shadow-[inset_0_0_15px_rgba(0,0,0,0.5)]">
                          <div className="absolute top-[15px] left-1/2 -translate-x-1/2 w-[95px] h-[30px] bg-black rounded-full z-20"></div>
                          {/* Stunning subtle glass glare */}
                          <div className="absolute -top-[50%] -left-[50%] w-[200%] h-[200%] bg-gradient-to-tr from-transparent to-white/10 rotate-[35deg] pointer-events-none z-10"></div>
                          <img src="/assets/portfolio_assets/Yapsu AI/snapshots/onboard_15.jpg" className="w-full h-full object-cover" />
                       </div>
                    </div>
                 </div>
              </div>

              {/* 2. VÀI SCREEN UI TRẢI DỌC TRONG MOCKUP (ISOMETRIC FLOW) */}
              <div className="w-full flex flex-col items-center mb-48">
                 <h3 className="font-['Fredoka'] text-[55px] font-bold text-[#1A202C] text-center mb-10 tracking-tight">Experience Flow</h3>
                 
                 <div className="relative w-full h-[750px] flex justify-center items-center overflow-visible z-20 pointer-events-none">
                    <div className="absolute w-[1200px] h-[1200px] flex justify-center items-center perspective-[2500px] pointer-events-auto">
                       <div className="flex gap-[60px] transform rotate-x-[55deg] rotate-z-[-35deg] scale-[1.1]">
                          
                          {/* Left Column (Lower) */}
                          <div className="flex flex-col gap-[60px] translate-y-[80px]" style={{ animation: 'float-iso 6s ease-in-out infinite' }}>
                             {["onboard_04.jpg", "roadmap_07.jpg"].map((src, i) => (
                                <div key={`iso1-${i}`} className="relative w-[300px] h-[640px] rounded-[55px] p-[8px] bg-gradient-to-br from-white to-gray-200 border border-white transition-transform duration-500 hover:-translate-y-8" style={{ boxShadow: '-25px 35px 60px rgba(0,0,0,0.15)' }}>
                                   <div className="w-full h-full bg-black rounded-[46px] overflow-hidden relative border-[4px] border-black">
                                      <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[90px] h-[28px] bg-black rounded-full z-20"></div>
                                      <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                                   </div>
                                </div>
                             ))}
                          </div>
                          
                          {/* Middle Column (Higher - Hero Column) */}
                          <div className="flex flex-col gap-[60px] -translate-y-[100px]" style={{ animation: 'float-iso 7s ease-in-out infinite 0.5s' }}>
                             {["roleplay_10.jpg", "onboard_09.jpg", "roadmap_15.jpg"].map((src, i) => (
                                <div key={`iso2-${i}`} className="relative w-[300px] h-[640px] rounded-[55px] p-[8px] bg-gradient-to-br from-white to-gray-200 border border-white transition-transform duration-500 hover:-translate-y-8" style={{ boxShadow: '-25px 35px 60px rgba(0,0,0,0.15)' }}>
                                   <div className="w-full h-full bg-black rounded-[46px] overflow-hidden relative border-[4px] border-black">
                                      <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[90px] h-[28px] bg-black rounded-full z-20"></div>
                                      <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                                   </div>
                                </div>
                             ))}
                          </div>

                          {/* Right Column (Lower) */}
                          <div className="flex flex-col gap-[60px] translate-y-[40px]" style={{ animation: 'float-iso 6.5s ease-in-out infinite 1s' }}>
                             {["roleplay_18.jpg", "roadmap_05.jpg"].map((src, i) => (
                                <div key={`iso3-${i}`} className="relative w-[300px] h-[640px] rounded-[55px] p-[8px] bg-gradient-to-br from-white to-gray-200 border border-white transition-transform duration-500 hover:-translate-y-8" style={{ boxShadow: '-25px 35px 60px rgba(0,0,0,0.15)' }}>
                                   <div className="w-full h-full bg-black rounded-[46px] overflow-hidden relative border-[4px] border-black">
                                      <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[90px] h-[28px] bg-black rounded-full z-20"></div>
                                      <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                                   </div>
                                </div>
                             ))}
                          </div>

                       </div>
                    </div>
                 </div>
              </div>

              {/* 3. TOÀN BỘ SCREEN LÀM APP DESIGN (RAW FLAT GRID WITH MASONRY FEEL) */}
              <div className="w-full flex flex-col items-center mb-48">
                 <div className="w-full max-w-[800px] text-center mb-16">
                    <h3 className="font-['Fredoka'] text-[55px] font-bold text-[#1A202C] tracking-tight mb-4">Complete Interface</h3>
                    <p className="text-xl text-gray-500">A comprehensive view of the meticulously crafted screens and components.</p>
                 </div>
                 
                 {/* Super tight gap for that premium Dribbble/Figma showcase feel */}
                 <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4 w-full px-2">
                    {[
                       "onboard_04.jpg", "onboard_09.jpg", "onboard_15.jpg", "onboard_20.jpg",
                       "roleplay_05.jpg", "roleplay_10.jpg", "roleplay_15.jpg", "roleplay_18.jpg",
                       "roadmap_05.jpg", "roadmap_07.jpg", "roadmap_10.jpg", "roadmap_15.jpg"
                    ].map((src, i) => (
                       <div key={`flat-${i}`} className="w-full aspect-[9/19] rounded-[24px] overflow-hidden shadow-md bg-gray-100 hover:shadow-2xl hover:scale-[1.03] transition-all duration-300 cursor-pointer border border-gray-200/50">
                          <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                       </div>
                    ))}
                 </div>
              </div>

              {/* 4. INTERACTIVE PROTOTYPES (FUNCTIONAL VIDEOS WITH REFLECTIONS) */}
              <div className="w-full relative z-20 pb-32">
                 <h3 className="font-['Fredoka'] text-[55px] font-bold text-[#1A202C] text-center mb-24 tracking-tight">Live Prototypes</h3>
                 <div className="flex flex-col lg:flex-row justify-center items-center gap-20 w-full">
                    
                    {[
                       { title: "Onboarding", src: "Onboarding Feature.MP4" },
                       { title: "Roleplay", src: "Roleplay Feature.MP4" },
                       { title: "Roadmap", src: "Roadmap + Drill Feature.mov" }
                    ].map((vid, idx) => (
                       <div key={idx} className="flex flex-col items-center group">
                          {/* Hyper-realistic iPhone 15 Pro Light Mockup */}
                          <div className="relative w-[320px] h-[670px] bg-gradient-to-b from-[#ffffff] to-[#e5e5e5] rounded-[60px] p-[10px] shadow-[0_40px_80px_rgba(0,0,0,0.15)] border border-white reflect-glass transition-transform duration-500 hover:-translate-y-6">
                             <div className="w-full h-full bg-black rounded-[50px] border-[6px] border-black overflow-hidden relative shadow-[inset_0_0_15px_rgba(0,0,0,0.5)]">
                                <div className="absolute top-[15px] left-1/2 -translate-x-1/2 w-[95px] h-[30px] bg-black rounded-full z-20"></div>
                                <video src={`/assets/portfolio_assets/Yapsu AI/${vid.src}`} autoPlay muted loop playsInline className="w-full h-full object-cover" />
                             </div>
                          </div>
                          
                          <h4 className="font-['Fredoka'] text-2xl mt-12 text-[#1A202C] font-bold tracking-wide">{vid.title}</h4>
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
