import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = "{/* Carousel Container */}"
end_marker = "</div>\n              </div>\n\n           </div>\n        </section>"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    new_carousel = """{/* Carousel Container */}
                      <div className="relative w-full h-[400px] sm:h-[450px] md:h-[550px] flex justify-center items-center overflow-hidden">
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
                              
                              let translateX = "0%";
                              let scale = 1;
                              let opacity = 1;
                              let zIndex = 30;
                              let blur = "0px";

                              if (diff === 0) {
                                  // Active
                                  translateX = "0%";
                                  scale = 1;
                                  opacity = 1;
                                  zIndex = 30;
                                  blur = "0px";
                              } else if (diff === 1) {
                                  // Right
                                  translateX = "110%";
                                  scale = 0.85;
                                  opacity = 0.3;
                                  zIndex = 20;
                                  blur = "3px";
                              } else if (diff === -1) {
                                  // Left
                                  translateX = "-110%";
                                  scale = 0.85;
                                  opacity = 0.3;
                                  zIndex = 20;
                                  blur = "3px";
                              } else {
                                  // Hidden
                                  translateX = "0%";
                                  scale = 0.5;
                                  opacity = 0;
                                  zIndex = 10;
                                  blur = "10px";
                              }

                              return (
                                  <div 
                                      key={idx} 
                                      onClick={() => setActiveGen20Idx(idx)}
                                      className="absolute top-1/2 left-1/2 cursor-pointer transition-all duration-700 ease-[cubic-bezier(0.25,1,0.5,1)] rounded-[24px] overflow-hidden border-[6px] border-white shadow-[0_15px_40px_rgba(59,91,53,0.3)] hover:opacity-80"
                                      style={{ 
                                          transform: `translate(-50%, -50%) translateX(${translateX}) scale(${scale})`,
                                          zIndex: zIndex,
                                          opacity: opacity,
                                          filter: `blur(${blur})`
                                      }}
                                  >
                                      <img src={`/assets/portfolio_assets/CC FTU/CC FTU Gen 20 Recruitment/SOCIAL POST/${filename}`} alt={filename.replace('.png', '')} className="h-[280px] sm:h-[350px] md:h-[420px] w-auto max-w-none block object-contain" />
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

