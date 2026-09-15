import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = "{/* Carousel Container */}"
end_marker = "{/* Fade Indicators for ends */}"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    new_carousel = """{/* Carousel Container */}
                      <div className="relative w-full h-[350px] sm:h-[450px] md:h-[550px] lg:h-[650px] flex justify-center items-center">
                          {[
                              "Q&A.png", 
                              "THÔNG BÁO KẾT QUẢ.png", 
                              "VIRAL POST.png", 
                              "Đóng đơn đăng ký.png"
                          ].map((filename, idx) => {
                              let diff = idx - activeGen20Idx;
                              if (diff === 3) diff = -1;
                              if (diff === -3) diff = 1;
                              if (diff === -2) diff = 2;
                              
                              let leftStyle = "50%";
                              let transformStyle = "translate(-50%, -50%) scale(1)";
                              let opacityClass = "opacity-100";
                              let zIndexClass = "z-30";
                              let blurClass = "blur-0";

                              if (diff === 0) {
                                  // Active (Center)
                                  leftStyle = "50%";
                                  transformStyle = "translate(-50%, -50%) scale(1)";
                                  opacityClass = "opacity-100";
                                  zIndexClass = "z-30";
                                  blurClass = "blur-0";
                              } else if (diff === 1) {
                                  // Right
                                  leftStyle = "80%";
                                  transformStyle = "translate(-50%, -50%) scale(0.85)";
                                  opacityClass = "opacity-40 hover:opacity-70";
                                  zIndexClass = "z-20";
                                  blurClass = "blur-[3px] hover:blur-[1px]";
                              } else if (diff === -1) {
                                  // Left
                                  leftStyle = "20%";
                                  transformStyle = "translate(-50%, -50%) scale(0.85)";
                                  opacityClass = "opacity-40 hover:opacity-70";
                                  zIndexClass = "z-20";
                                  blurClass = "blur-[3px] hover:blur-[1px]";
                              } else {
                                  // Hidden (Back)
                                  leftStyle = "50%";
                                  transformStyle = "translate(-50%, -50%) scale(0.5)";
                                  opacityClass = "opacity-0 pointer-events-none";
                                  zIndexClass = "z-10";
                                  blurClass = "blur-[10px]";
                              }

                              return (
                                  <div 
                                      key={idx} 
                                      onClick={() => setActiveGen20Idx(idx)}
                                      className={`absolute top-[50%] w-fit h-fit cursor-pointer transition-all duration-700 ease-[cubic-bezier(0.25,1,0.5,1)] rounded-[24px] overflow-hidden border-[6px] border-white shadow-[0_15px_40px_rgba(59,91,53,0.3)] ${opacityClass} ${zIndexClass} ${blurClass}`}
                                      style={{ left: leftStyle, transform: transformStyle }}
                                  >
                                      <img src={`/assets/portfolio_assets/CC FTU/CC FTU Gen 20 Recruitment/SOCIAL POST/${filename}`} alt={filename.replace('.png', '')} className="h-[250px] sm:h-[350px] md:h-[450px] lg:h-[550px] w-auto block object-contain" />
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
