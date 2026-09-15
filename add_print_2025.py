import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Background Color and Text
old_header = """<section id="chinese-debate-25" className="relative w-full py-24 bg-gradient-to-b from-[#231710] to-[#3D2719] overflow-hidden">
           <div className="max-w-[1400px] mx-auto px-6 sm:px-10 relative z-20 flex flex-col">
              
              {/* 1. SECTION HEADER */}
              <div className="flex flex-col items-center mb-20 text-center">
                  <div className="px-6 py-2 border-2 border-[#D4AF37] text-[#FFF2B2] rounded-full text-sm font-bold mb-6 tracking-widest uppercase bg-[#231710]/50 backdrop-blur-sm shadow-[0_0_15px_rgba(212,175,55,0.3)]">
                      Event Identity
                  </div>
                  <h2 className="font-['Fredoka'] text-[60px] md:text-[90px] font-black text-transparent bg-clip-text bg-gradient-to-b from-[#FFF2B2] to-[#D4AF37] leading-none mb-6 pb-2" style={{ filter: 'drop-shadow(0px 0px 15px rgba(212,175,55,0.5))' }}>
                      Chinese Debate 2025
                  </h2>
                  <p className="max-w-2xl text-lg text-[#F3E5AB] font-['Quicksand'] font-bold leading-relaxed">
                      "BỨT PHÁ" - The prestigious academic debate competition hosted by the Chinese Club - Foreign Trade University.
                  </p>
              </div>"""

new_header = """<section id="chinese-debate-25" className="relative w-full py-24 bg-gradient-to-b from-[#4A2C11] to-[#2E1A09] overflow-hidden">
           <div className="max-w-[1400px] mx-auto px-6 sm:px-10 relative z-20 flex flex-col">
              
              {/* 1. SECTION HEADER */}
              <div className="flex flex-col items-center mb-20 text-center">
                  <div className="px-6 py-2 border-2 border-[#D4AF37] text-[#FFF2B2] rounded-full text-sm font-bold mb-6 tracking-widest uppercase bg-[#4A2C11]/50 backdrop-blur-sm shadow-[0_0_15px_rgba(212,175,55,0.3)]">
                      Event Identity
                  </div>
                  <h2 className="font-['Fredoka'] text-[60px] md:text-[90px] font-black text-transparent bg-clip-text bg-gradient-to-b from-[#FFF2B2] to-[#D4AF37] leading-none mb-6 pb-2" style={{ filter: 'drop-shadow(0px 0px 15px rgba(212,175,55,0.5))' }}>
                      Chinese Debate 2025
                  </h2>
                  <p className="max-w-2xl text-lg text-[#F3E5AB] font-['Quicksand'] font-bold leading-relaxed">
                      "BỨT PHÁ" - The explosive academic debate arena with a fierce, burning, and breakthrough spirit hosted by the Chinese Club - Foreign Trade University (CC FTU).
                  </p>
              </div>"""
content = content.replace(old_header, new_header)

# 2. Insert Event Applications
old_digital = """{/* 3. DIGITAL & SOCIAL POSTS (MASONRY) */}"""
new_event_apps = """{/* 2.5 PRINT & EVENT APPLICATIONS */}
              <div className="w-full mb-32 flex flex-col items-center">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#D4AF37] mb-10 tracking-wide drop-shadow-[0_0_10px_rgba(212,175,55,0.4)] text-center">
                      Event Applications
                  </h3>
                  
                  <div className="w-full max-w-5xl flex flex-col gap-16">
                      <div className="flex flex-col items-center gap-5">
                          <div className="relative group w-full rounded-[24px] overflow-hidden border-2 border-[#D4AF37] shadow-[0_0_20px_rgba(212,175,55,0.2)] hover:border-[#F3E5AB] transition-colors duration-500">
                              <img src="/assets/portfolio_assets/CC FTU/Chinese Debate 2025/Print & Event Applications/BACKDROP.png" alt="Event Backdrop" className="w-full h-auto block group-hover:scale-[1.02] transition-transform duration-700" />
                          </div>
                          <h4 className="font-['Quicksand'] font-bold text-xl text-[#FFF2B2] tracking-wider uppercase drop-shadow-md">Stage Backdrop</h4>
                      </div>
                      
                      <div className="columns-1 md:columns-3 gap-8 w-full">
                          {[
                              { file: "phướn_1.png", name: "Vertical Banner 1" },
                              { file: "phướn_Huyen.png", name: "Vertical Banner 2" },
                              { file: "phướn_Thu.png", name: "Vertical Banner 3" }
                          ].map((item, idx) => (
                              <div key={idx} className="flex flex-col items-center gap-5 mb-8 break-inside-avoid">
                                  <div className="relative group w-full rounded-[24px] overflow-hidden border-2 border-[#D4AF37] shadow-[0_0_20px_rgba(212,175,55,0.2)] hover:border-[#F3E5AB] transition-colors duration-500">
                                      <img src={`/assets/portfolio_assets/CC FTU/Chinese Debate 2025/Print & Event Applications/${item.file}`} alt={item.name} className="w-full h-auto block group-hover:scale-[1.02] transition-transform duration-700" />
                                  </div>
                                  <h4 className="font-['Quicksand'] font-bold text-lg text-[#FFF2B2] tracking-wider uppercase drop-shadow-md text-center">{item.name}</h4>
                              </div>
                          ))}
                      </div>
                  </div>
              </div>

              {/* 3. DIGITAL & SOCIAL POSTS (MASONRY) */}"""
content = content.replace(old_digital, new_event_apps)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS")
