import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the old scroll container with the new 3D Infinite Loop Coverflow
start_marker = "{/* Carousel Container */}"
end_marker = "{/* Fade Indicators for ends */}"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    new_carousel = """{/* Carousel Container */}
                      <div className="relative w-full h-[400px] sm:h-[500px] md:h-[650px] flex justify-center items-center perspective-1000">
                          {[
                              "Q&A.png", 
                              "THÔNG BÁO KẾT QUẢ.png", 
                              "VIRAL POST.png", 
                              "Đóng đơn đăng ký.png"
                          ].map((filename, idx) => {
                              // Calculate infinite loop relative positions
                              let diff = idx - activeGen20Idx;
                              if (diff === 3) diff = -1;
                              if (diff === -3) diff = 1;
                              if (diff === -2) diff = 2;
                              
                              let transformStyle = "translateX(0) scale(1)";
                              let opacityClass = "opacity-100";
                              let zIndexClass = "z-30";
                              let blurClass = "blur-0";

                              if (diff === 0) {
                                  // Active (Center)
                                  transformStyle = "translateX(0%) scale(1)";
                                  opacityClass = "opacity-100";
                                  zIndexClass = "z-30";
                                  blurClass = "blur-0";
                              } else if (diff === 1) {
                                  // Right
                                  transformStyle = "translateX(65%) scale(0.8)";
                                  opacityClass = "opacity-40 hover:opacity-70";
                                  zIndexClass = "z-20";
                                  blurClass = "blur-[4px] hover:blur-[2px]";
                              } else if (diff === -1) {
                                  // Left
                                  transformStyle = "translateX(-65%) scale(0.8)";
                                  opacityClass = "opacity-40 hover:opacity-70";
                                  zIndexClass = "z-20";
                                  blurClass = "blur-[4px] hover:blur-[2px]";
                              } else {
                                  // Hidden (Back)
                                  transformStyle = "translateX(0%) scale(0.5)";
                                  opacityClass = "opacity-0 pointer-events-none";
                                  zIndexClass = "z-10";
                                  blurClass = "blur-[10px]";
                              }

                              return (
                                  <div 
                                      key={idx} 
                                      onClick={() => setActiveGen20Idx(idx)}
                                      className={`absolute w-[75%] md:w-[45%] lg:w-[35%] cursor-pointer transition-all duration-700 ease-[cubic-bezier(0.25,1,0.5,1)] rounded-[24px] overflow-hidden border-[6px] border-white shadow-[0_15px_40px_rgba(59,91,53,0.4)] ${opacityClass} ${zIndexClass} ${blurClass}`}
                                      style={{ transform: transformStyle }}
                                  >
                                      <img src={`/assets/portfolio_assets/CC FTU/CC FTU Gen 20 Recruitment/SOCIAL POST/${filename}`} alt={filename.replace('.png', '')} className="w-full h-auto block" />
                                      {diff !== 0 && (
                                          <div className="absolute inset-0 bg-[#EAF2E3]/20 backdrop-blur-[1px]"></div>
                                      )}
                                  </div>
                              );
                          })}
                      </div>
                      
                      """
    content = content[:start_idx] + new_carousel + content[end_idx:]
    with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS")
else:
    print("FAILED TO FIND MARKERS")

