import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

new_isometric = """
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
"""

# Find the block to replace
start_marker = '<div className="absolute w-[2200px] flex justify-center items-center perspective-[2500px]">'
end_marker = '</div>\n                 </div>\n              </div>\n\n              {/* 3. EXPERIENCE FLOW (WAS APP DESIGN)'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_isometric.strip() + '\n                 ' + content[end_idx:]
    with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS")
else:
    print("FAILED TO FIND MARKERS")
