import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

new_yapsu = """
        {/* ─── 01. YAPSU AI ─── */}
        <section id="yapsu-ai" className="relative w-full py-32 bg-gradient-to-br from-[#0A1930] via-[#102B5A] to-[#1E439B] overflow-hidden font-sans">
           {/* Abstract wavy lines in background (CSS implementation) */}
           <div className="absolute inset-0 opacity-20 pointer-events-none" style={{ backgroundImage: 'radial-gradient(circle at 50% 50%, rgba(255,255,255,0.1) 0%, transparent 60%)' }}></div>
           
           <div className="max-w-[1400px] mx-auto px-6 relative z-20">
              
              {/* HERO SECTION */}
              <div className="flex flex-col lg:flex-row items-center justify-between mb-40 gap-16">
                 {/* Left Text */}
                 <div className="w-full lg:w-1/2 flex flex-col items-start text-white">
                    <h2 className="font-['Fredoka'] text-[60px] md:text-[90px] font-bold leading-tight mb-6">
                       1. Yapsu AI
                    </h2>
                    <div className="px-6 py-2 border-2 border-white rounded-full text-lg font-semibold mb-8 hover:bg-white hover:text-[#102B5A] transition-colors cursor-pointer">
                       App Design
                    </div>
                    <p className="text-lg md:text-xl text-blue-100 leading-relaxed font-light max-w-xl">
                       This is an application interface design project. Yapsu AI is a modern application designed for modern people—those seeking to improve their language skills with intelligent roleplay, personalized roadmaps, and seamless daily practice.
                    </p>
                 </div>
                 
                 {/* Right 3D Floating Video */}
                 <div className="w-full lg:w-1/2 flex justify-center perspective-1000">
                    <div className="relative w-[280px] h-[580px] bg-black rounded-[40px] border-[8px] border-[#2A4365] shadow-[30px_30px_60px_rgba(0,0,0,0.6)] overflow-hidden" style={{ transform: 'rotateY(-20deg) rotateX(10deg) rotateZ(-5deg)' }}>
                       <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[100px] h-[25px] bg-black rounded-b-[18px] z-20"></div>
                       <video src="/assets/portfolio_assets/Yapsu AI/Roleplay Feature.MP4" autoPlay muted loop playsInline className="w-full h-full object-cover rounded-[32px] bg-white opacity-90" />
                       <div className="absolute inset-0 bg-gradient-to-tr from-blue-500/20 to-transparent pointer-events-none mix-blend-overlay"></div>
                    </div>
                 </div>
              </div>

              {/* ISOMETRIC SNAPSHOTS GRID */}
              <div className="w-full mb-40">
                 <h3 className="font-['Fredoka'] text-[50px] text-white text-center mb-16">Screen Flow</h3>
                 {/* CSS Isometric Grid */}
                 <div className="relative w-full h-[600px] overflow-hidden flex justify-center items-center perspective-1000">
                    <div className="absolute flex gap-8 transform rotate-x-[60deg] rotate-z-[-30deg] scale-125">
                       
                       {/* Column 1 */}
                       <div className="flex flex-col gap-8 -translate-y-24">
                          <img src="/assets/portfolio_assets/Yapsu AI/snapshots/onboard_04.jpg" className="w-[200px] h-auto rounded-[20px] shadow-[15px_15px_30px_rgba(0,0,0,0.5)] border-4 border-[#3A5385] object-cover" />
                          <img src="/assets/portfolio_assets/Yapsu AI/snapshots/onboard_09.jpg" className="w-[200px] h-auto rounded-[20px] shadow-[15px_15px_30px_rgba(0,0,0,0.5)] border-4 border-[#3A5385] object-cover" />
                          <img src="/assets/portfolio_assets/Yapsu AI/snapshots/roleplay_05.jpg" className="w-[200px] h-auto rounded-[20px] shadow-[15px_15px_30px_rgba(0,0,0,0.5)] border-4 border-[#3A5385] object-cover" />
                       </div>
                       
                       {/* Column 2 */}
                       <div className="flex flex-col gap-8">
                          <img src="/assets/portfolio_assets/Yapsu AI/snapshots/roleplay_10.jpg" className="w-[200px] h-auto rounded-[20px] shadow-[15px_15px_30px_rgba(0,0,0,0.5)] border-4 border-[#3A5385] object-cover" />
                          <img src="/assets/portfolio_assets/Yapsu AI/snapshots/roadmap_05.jpg" className="w-[200px] h-auto rounded-[20px] shadow-[15px_15px_30px_rgba(0,0,0,0.5)] border-4 border-[#3A5385] object-cover" />
                          <img src="/assets/portfolio_assets/Yapsu AI/snapshots/roadmap_10.jpg" className="w-[200px] h-auto rounded-[20px] shadow-[15px_15px_30px_rgba(0,0,0,0.5)] border-4 border-[#3A5385] object-cover" />
                       </div>
                       
                       {/* Column 3 */}
                       <div className="flex flex-col gap-8 translate-y-24">
                          <img src="/assets/portfolio_assets/Yapsu AI/snapshots/onboard_15.jpg" className="w-[200px] h-auto rounded-[20px] shadow-[15px_15px_30px_rgba(0,0,0,0.5)] border-4 border-[#3A5385] object-cover" />
                          <img src="/assets/portfolio_assets/Yapsu AI/snapshots/roleplay_15.jpg" className="w-[200px] h-auto rounded-[20px] shadow-[15px_15px_30px_rgba(0,0,0,0.5)] border-4 border-[#3A5385] object-cover" />
                          <img src="/assets/portfolio_assets/Yapsu AI/snapshots/roadmap_15.jpg" className="w-[200px] h-auto rounded-[20px] shadow-[15px_15px_30px_rgba(0,0,0,0.5)] border-4 border-[#3A5385] object-cover" />
                       </div>

                    </div>
                 </div>
              </div>

              {/* FUNCTIONAL VIDEO MOCKUPS */}
              <div className="w-full">
                 <h3 className="font-['Fredoka'] text-[50px] text-white text-center mb-16">Interactive Prototypes</h3>
                 <div className="flex flex-col lg:flex-row justify-center items-center gap-12 w-full">
                    {/* Phone 1 */}
                    <div className="flex flex-col items-center group">
                       <h4 className="font-['Fredoka'] text-2xl mb-6 text-blue-200">Onboarding</h4>
                       <div className="relative w-[280px] h-[580px] bg-[#0A1930] rounded-[45px] border-[6px] border-[#3A5385] shadow-2xl overflow-hidden">
                          <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[100px] h-[25px] bg-[#0A1930] rounded-b-[18px] z-20"></div>
                          <video src="/assets/portfolio_assets/Yapsu AI/Onboarding Feature.MP4" autoPlay muted loop playsInline className="w-full h-full object-cover rounded-[38px] bg-white" />
                       </div>
                    </div>

                    {/* Phone 2 */}
                    <div className="flex flex-col items-center group">
                       <h4 className="font-['Fredoka'] text-2xl mb-6 text-blue-200">Roleplay</h4>
                       <div className="relative w-[280px] h-[580px] bg-[#0A1930] rounded-[45px] border-[6px] border-[#3A5385] shadow-2xl overflow-hidden">
                          <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[100px] h-[25px] bg-[#0A1930] rounded-b-[18px] z-20"></div>
                          <video src="/assets/portfolio_assets/Yapsu AI/Roleplay Feature.MP4" autoPlay muted loop playsInline className="w-full h-full object-cover rounded-[38px] bg-white" />
                       </div>
                    </div>

                    {/* Phone 3 */}
                    <div className="flex flex-col items-center group">
                       <h4 className="font-['Fredoka'] text-2xl mb-6 text-blue-200">Roadmap</h4>
                       <div className="relative w-[280px] h-[580px] bg-[#0A1930] rounded-[45px] border-[6px] border-[#3A5385] shadow-2xl overflow-hidden">
                          <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[100px] h-[25px] bg-[#0A1930] rounded-b-[18px] z-20"></div>
                          <video src="/assets/portfolio_assets/Yapsu AI/Roadmap + Drill Feature.mov" autoPlay muted loop playsInline className="w-full h-full object-cover rounded-[38px] bg-white" />
                       </div>
                    </div>
                 </div>
              </div>

           </div>
        </section>"""

pattern = re.compile(r'<section id="yapsu-ai".*?</section>', re.DOTALL)
content = re.sub(pattern, new_yapsu.strip(), content)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
