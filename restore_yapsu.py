import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Grab everything up to TOC grid start
toc_header = '<div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-10 w-full justify-items-center">'
top_part = content[:content.find(toc_header) + len(toc_header)]

# 2. Grab everything after Yapsu Live Prototypes (which starts at chinese-debate-2026)
bottom_part = content[content.find('{/* Smooth Transition to Chinese Debate 2026 */}'):]

middle_part = """
                 {[
                    { id: "01", title: "Yapsu AI", color: "#F1934B", anchor: "yapsu-ai" },
                    { id: "02", title: "Chinese Debate '26", color: "#4EC4E1", anchor: "chinese-debate-2026" },
                    { id: "03", title: "Gen 20th Recruit", color: "#89B66B", anchor: "gen-20-recruit" },
                    { id: "04", title: "19th Birthday", color: "#A890D8", anchor: "19th-birthday" },
                    { id: "05", title: "Chinese Debate '25", color: "#D4AF37", anchor: "chinese-debate-25" },
                    { id: "06", title: "Talkshow", color: "#58B3D3", anchor: "talkshow" },
                    { id: "07", title: "Zodiac", color: "#2C3E50", anchor: "zodiac" },
                    { id: "08", title: "Paintaso", color: "#E53935", anchor: "paintaso" }
                 ].map((item, idx) => (
                    <a key={idx} href={`#${item.anchor}`} className="group relative w-full max-w-[280px]">
                       <div className="w-full aspect-[4/3] bg-white rounded-[24px] shadow-sm group-hover:shadow-[8px_8px_0px_rgba(0,0,0,0.1)] transition-all duration-300 border-[3px] border-white group-hover:-translate-y-2 flex flex-col p-6 relative z-10 overflow-hidden">
                          <div className="absolute top-0 left-1/2 -translate-x-1/2 w-12 h-3 opacity-80 rounded-b-md" style={{ backgroundColor: item.color }}></div>
                          <span className="font-['Fredoka'] font-black text-5xl opacity-20 mt-4 group-hover:opacity-40 transition-opacity" style={{ color: item.color }}>{item.id}</span>
                          <h3 className="font-['Fredoka'] font-bold text-2xl text-[#333] mt-auto leading-tight">{item.title}</h3>
                       </div>
                       <div className="absolute inset-0 bg-[#E0DCC8] rounded-[24px] translate-y-3 translate-x-3 z-0 group-hover:translate-y-4 group-hover:translate-x-4 transition-transform"></div>
                    </a>
                 ))}
              </div>
           </div>
        </section>

        {/* ─── 01. YAPSU AI ─── */}
        <section id="yapsu-ai" className="relative w-full py-32 bg-[#FCFBF9] text-[#334155] font-sans">
           
           {/* Transition from TOC (Beige) to Yapsu (Light) */}
           <div className="absolute top-0 left-0 w-full h-[250px] bg-gradient-to-b from-[#F4F1EA] to-[#FCFBF9] z-10 pointer-events-none"></div>

           <div className="max-w-[1600px] mx-auto px-4 sm:px-8 relative z-20 flex flex-col">
              
              {/* 1. PRODUCT BRIEF (HERO) */}
              <div className="flex flex-col lg:flex-row items-center justify-between mb-32 gap-16 w-full max-w-[1400px] mx-auto pt-10">
                 <div className="w-full lg:w-[45%] flex flex-col items-start pt-10">
                    <h2 className="font-['Fredoka'] text-[70px] md:text-[85px] font-bold leading-tight mb-6 text-transparent bg-clip-text bg-gradient-to-r from-orange-500 to-amber-400 drop-shadow-sm tracking-tight">
                       Yapsu AI
                    </h2>
                    
                    <div className="px-6 py-2 border border-orange-200 text-orange-500 rounded-full text-base font-semibold mb-8 bg-orange-50 uppercase tracking-widest shadow-sm">
                       Product Design
                    </div>
                    
                    <p className="text-xl text-[#475569] leading-relaxed font-normal mb-12 max-w-lg">
                       Yapsu AI is a modern language learning app designed for individuals seeking a natural way to practice conversations with friendly AI tutors.
                    </p>
                    
                    <div className="w-[160px] h-[160px] rounded-[36px] shadow-[0_15px_40px_rgba(0,0,0,0.08)] shrink-0 overflow-hidden bg-white border border-gray-100 hover:-translate-y-2 transition-transform duration-500">
                       <img src="/assets/portfolio_assets/Yapsu AI/yapsu_icon_premium.png" className="w-full h-full object-cover" />
                    </div>
                 </div>
                 
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

              {/* 2. APP DESIGN - ISOMETRIC */}
              <div className="w-full flex flex-col items-center mt-20 relative max-w-[1400px] mx-auto">
                 <h3 className="font-['Fredoka'] text-[50px] font-bold text-transparent bg-clip-text bg-gradient-to-r from-orange-500 to-amber-400 text-center mb-10 tracking-wide z-30 drop-shadow-sm">
                    App Design
                 </h3>
                 
                 <div className="relative w-[100vw] max-w-[100vw] h-[1000px] flex justify-center items-center overflow-hidden z-20 pointer-events-none" 
                      style={{ WebkitMaskImage: 'linear-gradient(to bottom, transparent 0%, black 15%, black 85%, transparent 100%)', maskImage: 'linear-gradient(to bottom, transparent 0%, black 15%, black 85%, transparent 100%)' }}>
                    
                    <div className="absolute w-[2200px] flex justify-center items-center perspective-[2500px]">
                       <div className="flex gap-[50px] transform rotate-x-[55deg] rotate-z-[-35deg] scale-[0.8] translate-y-[100px]">
                          
                          {/* Column 1 */}
                          <div className="flex flex-col gap-[50px] translate-y-[150px]">
                             {["19_dark_ui.jpg", "onboard_27.jpg", "09_drill_fill.jpg", "13_roleplay_gradient.jpg"].map((src, i) => (
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
                             {["03_onboard_aha.jpg", "18_boy_bill.jpg", "10_drill_matching.jpg", "14_roleplay_hint.jpg"].map((src, i) => (
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
                             {["z_green_reminders.jpg", "05_roadmap_map.jpg", "11_drill_repeat.jpg", "15_roleplay_feedback.jpg"].map((src, i) => (
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
                             {["onboard_09.jpg", "roadmap_04.jpg", "z_orange_amazing.jpg", "16_roleplay_transcript.jpg"].map((src, i) => (
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

              {/* 3. EXPERIENCE FLOW - FLAT GRID */}
              <div className="w-full flex flex-col items-center mt-32 mb-48 pt-10">
                 <h3 className="font-['Fredoka'] text-[50px] font-bold text-transparent bg-clip-text bg-gradient-to-r from-orange-500 to-amber-400 text-center mb-16 tracking-wide drop-shadow-sm">
                    Experience Flow
                 </h3>
                 
                 <div className="grid grid-cols-2 md:grid-cols-4 xl:grid-cols-8 gap-4 w-full">
                    {[
                       // ---------------- ROW 1 (8 images) ----------------
                       // 6 ONBOARDING (Post-login)
                       "19_dark_ui.jpg",           // Dark UI (Imagine)
                       "03_onboard_aha.jpg",       // Japanese level
                       "z_green_reminders.jpg",    // Green reminders
                       "onboard_09.jpg",           // Blue tutor
                       "onboard_27.jpg",           // Pink cherry blossom
                       "18_boy_bill.jpg",          // Orange boy with bill
                       
                       // 2 ROADMAP
                       "05_roadmap_map.jpg",       // Map path
                       "roadmap_04.jpg",           // Vocab table
                       
                       // ---------------- ROW 2 (8 images) ----------------
                       // 4 DRILL
                       "09_drill_fill.jpg",        // Fill in blank
                       "10_drill_matching.jpg",    // Matching
                       "11_drill_repeat.jpg",      // Repeat after
                       "z_orange_amazing.jpg",     // Orange amazing
                       
                       // 4 ROLEPLAY
                       "13_roleplay_gradient.jpg", // Gradient
                       "14_roleplay_hint.jpg",     // Hint
                       "15_roleplay_feedback.jpg", // Feedback
                       "16_roleplay_transcript.jpg"// Transcript
                    ].map((src, i) => (
                       <div key={`flat-${i}`} className="w-full aspect-[9/19] rounded-[24px] overflow-hidden shadow-sm border border-gray-200 bg-white hover:shadow-xl transition-shadow duration-300">
                          <img src={`/assets/portfolio_assets/Yapsu AI/snapshots/${src}`} className="w-full h-full object-cover" />
                       </div>
                    ))}
                 </div>
              </div>

              {/* 4. LIVE PROTOTYPES */}
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
"""

new_content = top_part + middle_part + bottom_part
with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(new_content)
