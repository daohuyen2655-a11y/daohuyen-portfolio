import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add "View Website Demo" button
marker_end_debate_social = """                        ))}
                    </div>
                </div>

            </div>"""

new_debate_social_ending = """                        ))}
                    </div>
                </div>

                {/* View Website Button */}
                <div className="w-full flex justify-center mt-12 mb-8 relative z-30">
                    <a href="/assets/portfolio_assets/CC FTU/Chinese Debate 2026/WEBSITE/CUỘC THI TRANH BIỆN TIẾNG HOA 2026.html" target="_blank" rel="noopener noreferrer" className="relative group inline-flex items-center justify-center px-8 py-4 bg-[#0A1A40] text-cyan-400 font-['Fredoka'] font-bold text-2xl uppercase tracking-widest rounded-full overflow-hidden border-2 border-cyan-500 shadow-[0_0_20px_rgba(34,211,238,0.3)] hover:shadow-[0_0_40px_rgba(34,211,238,0.6)] transition-all duration-300 hover:scale-105 hover:-translate-y-1">
                        <span className="relative z-10 flex items-center gap-3 drop-shadow-md">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
                            View Website Demo
                        </span>
                        <div className="absolute inset-0 bg-gradient-to-r from-cyan-600/20 to-blue-600/20 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                    </a>
                </div>

            </div>"""
content = content.replace(marker_end_debate_social, new_debate_social_ending)

# 2. Remove Gradients Bridges
content = content.replace('{/* Smooth Transition to Chinese Debate 2026 */}\n        <div className="w-full h-[150px] bg-gradient-to-b from-[#FFD8B5] to-[#06112E]"></div>\n        \n', '')
content = content.replace('<div className="absolute top-0 left-0 w-full h-[100px] bg-gradient-to-b from-[#F6F4EB] to-[#FCFBF9] z-10 pointer-events-none"></div>\n', '')

# 3. Replace Gen 20 Recruitment section
gen20_start = "{/* ─── 03. GEN 20 RECRUITMENT ─── */}"
gen20_end = "</section>\n\n        {/* ─── 04. 19TH BIRTHDAY ─── */}"

start_idx = content.find(gen20_start)
end_idx = content.find(gen20_end, start_idx)

if start_idx != -1 and end_idx != -1:
    new_gen20 = """{/* ─── 03. GEN 20 RECRUITMENT ─── */}
        <section id="gen-20-recruit" className="relative w-full py-24 bg-gradient-to-b from-[#EAF2E3] to-[#D9EBCB] overflow-hidden">
           <div className="max-w-[1400px] mx-auto px-6 sm:px-10 relative z-20 flex flex-col">
              
              {/* 1. SECTION HEADER */}
              <div className="flex flex-col items-center mb-20 text-center">
                  <div className="px-6 py-2 border-[4px] border-white text-[#3B5B35] rounded-full text-sm font-bold mb-6 tracking-widest uppercase bg-white/50 backdrop-blur-sm shadow-md rotate-[-2deg]">
                      Campaign Design
                  </div>
                  <h2 className="font-['Fredoka'] text-[70px] md:text-[100px] font-black text-white leading-none mb-6 rotate-[1deg]" style={{ textShadow: '-3px -3px 0 #FFF, 3px -3px 0 #FFF, -3px 3px 0 #FFF, 3px 3px 0 #FFF, 8px 8px 0px rgba(59,91,53,0.3)' }}>
                      Phong Hải<br/>Trường Chinh
                  </h2>
                  <p className="max-w-2xl text-lg text-[#3B5B35]/80 font-['Quicksand'] font-bold leading-relaxed">
                      Creative identity for the Gen 20th Recruitment campaign. Emphasizing a natural, organic, and resilient theme.
                  </p>
              </div>

              {/* 2. KEY VISUAL */}
              <div className="w-full mb-32 flex flex-col items-center">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#3B5B35] mb-10 tracking-wide">
                      Key Visual
                  </h3>
                  <div className="relative w-full max-w-5xl rounded-[32px] overflow-hidden border-[8px] border-white shadow-[0_20px_50px_rgba(59,91,53,0.2)] rotate-[-1deg] group">
                      <img src="/assets/portfolio_assets/CC FTU/CC FTU Gen 20 Recruitment/KEY VISUAL/cover tuyển gen.png" alt="Gen 20 Key Visual" className="w-full h-auto block group-hover:scale-105 transition-transform duration-700" />
                  </div>
                  
                  {/* Avatar Badge */}
                  <div className="relative -mt-20 w-32 h-32 md:w-44 md:h-44 rounded-full p-2 bg-white shadow-xl z-10 group hover:-translate-y-2 transition-transform duration-300 rotate-[3deg]">
                      <div className="w-full h-full rounded-full overflow-hidden bg-[#D9EBCB]">
                          <img src="/assets/portfolio_assets/CC FTU/CC FTU Gen 20 Recruitment/KEY VISUAL/avt tuyển gen.png" alt="Gen 20 Avatar" className="w-full h-full object-cover" />
                      </div>
                  </div>
              </div>

              {/* 3. EVENT APPLICATIONS */}
              <div className="w-full mb-32 flex flex-col items-center">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#3B5B35] mb-10 tracking-wide text-center">
                      Event Applications
                  </h3>
                  <div className="w-full max-w-5xl flex flex-col items-center gap-6">
                      <div className="relative group w-full rounded-[24px] overflow-hidden border-[6px] border-white shadow-[0_15px_40px_rgba(59,91,53,0.15)] hover:shadow-[0_25px_50px_rgba(59,91,53,0.25)] transition-all duration-500 rotate-[1deg]">
                          <img src="/assets/portfolio_assets/CC FTU/CC FTU Gen 20 Recruitment/Print & Event Applications/frame.png" alt="Avatar Frame" className="w-full h-auto block group-hover:scale-[1.02] transition-transform duration-700" />
                      </div>
                      <h4 className="font-['Quicksand'] font-bold text-xl text-[#3B5B35] tracking-wider uppercase mt-4">Avatar Frame</h4>
                  </div>
              </div>

              {/* 4. DIGITAL & SOCIAL (MASONRY LAYOUT) */}
              <div className="w-full mb-10">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#3B5B35] mb-10 tracking-wide text-center">
                      Digital & Social
                  </h3>
                  
                  <div className="columns-1 md:columns-2 gap-8 w-full max-w-5xl mx-auto">
                      {[
                          "Q&A.png", 
                          "THÔNG BÁO KẾT QUẢ.png", 
                          "VIRAL POST.png", 
                          "Đóng đơn đăng ký.png"
                      ].map((filename, idx) => (
                          <div key={idx} className={`relative rounded-[24px] overflow-hidden border-[6px] border-white group hover:border-[#89B66B] transition-colors duration-300 shadow-lg break-inside-avoid mb-8 inline-block w-full ${idx % 2 === 0 ? 'rotate-[-1deg]' : 'rotate-[1deg]'}`}>
                              <img src={`/assets/portfolio_assets/CC FTU/CC FTU Gen 20 Recruitment/SOCIAL POST/${filename}`} alt={filename.replace('.png', '')} className="w-full h-auto block group-hover:scale-105 transition-transform duration-500" />
                          </div>
                      ))}
                  </div>
              </div>

           </div>
        </section>
"""
    content = content[:start_idx] + new_gen20 + content[end_idx:]

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("SUCCESS")
