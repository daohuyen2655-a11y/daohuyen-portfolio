import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add state and effect for activeDebateIdx
state_insert_marker = "const [activeGen20Idx, setActiveGen20Idx] = useState(0);"
if "const [activeDebateIdx, setActiveDebateIdx] = useState(0);" not in content:
    new_state = state_insert_marker + "\n  const [activeDebateIdx, setActiveDebateIdx] = useState(0);"
    content = content.replace(state_insert_marker, new_state)

effect_insert_marker = """setActiveGen20Idx(prev => (prev + 1) % 4);
    }, 5000);
    return () => clearInterval(interval);
  }, []);"""

if "setActiveDebateIdx" not in effect_insert_marker and "setActiveDebateIdx(prev => (prev + 1) % 10);" not in content:
    new_effect = effect_insert_marker + """\n\n  useEffect(() => {\n    const interval = setInterval(() => {\n      setActiveDebateIdx(prev => (prev + 1) % 10);\n    }, 5000);\n    return () => clearInterval(interval);\n  }, []);"""
    content = content.replace(effect_insert_marker, new_effect)

# 2. Replace Masonry Grid with Carousel
masonry_pattern = r'\{/\* 3\. DIGITAL & SOCIAL POSTS \(MASONRY\) \*/\}.*?<div className="columns-2 md:columns-3 lg:columns-4 gap-6 w-full max-w-\[1400px\] mx-auto">.*?</div>\n              </div>'

new_carousel = """{/* 3. DIGITAL & SOCIAL POSTS (CAROUSEL) */}
              <div className="w-full mb-24 overflow-hidden">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#D4AF37] mb-10 tracking-wide text-center drop-shadow-[0_0_10px_rgba(212,175,55,0.4)]">
                      Digital & Social
                  </h3>
                  
                  <div className="relative w-full h-[400px] sm:h-[450px] md:h-[550px] flex justify-center items-center">
                      {[
                          "MỞ ĐƠN.png",
                          "THÔNG BÁO QUÁN QUÂN.png",
                          "THỂ LỆ VÒNG SƠ KHẢO.png",
                          "THÔNG BÁO CƠ CẤU GIẢI THƯỞNG.png",
                          "QUYỀN LỢI KHI THAM GIA CUỘC THI.png",
                          "TỪ KHOÁ VÒNG CHUNG KẾT CUỘC THI.png",
                          "GIỚI THIỆU BẢO TRỢ TRUYỀN THÔNG.png",
                          "GIỚI THIỆU ĐỐI TÁC TRUYỀN THÔNG.png",
                          "GIỚI THIỆU NTT-1.png",
                          "GIỚI THIỆU NTT-2.png"
                      ].map((filename, idx) => {
                          let diff = idx - activeDebateIdx;
                          if (diff > 5) diff -= 10;
                          if (diff < -4) diff += 10;
                          
                          let translateX = "0%";
                          let scale = 1;
                          let opacity = 1;
                          let zIndex = 30;
                          let blur = "0px";
                          let pointerEvents = "auto";

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
                              opacity = 0.4;
                              zIndex = 20;
                              blur = "3px";
                          } else if (diff === -1) {
                              // Left
                              translateX = "-110%";
                              scale = 0.85;
                              opacity = 0.4;
                              zIndex = 20;
                              blur = "3px";
                          } else {
                              // Hidden
                              translateX = "0%";
                              scale = 0.5;
                              opacity = 0;
                              zIndex = 10;
                              blur = "10px";
                              pointerEvents = "none";
                          }

                          return (
                              <div 
                                  key={idx} 
                                  onClick={() => setActiveDebateIdx(idx)}
                                  className="absolute top-1/2 left-1/2 cursor-pointer transition-all duration-700 ease-[cubic-bezier(0.25,1,0.5,1)] rounded-[24px] overflow-hidden border-[4px] border-[#D4AF37] shadow-[0_15px_40px_rgba(212,175,55,0.3)] hover:opacity-80"
                                  style={{ 
                                      transform: `translate(-50%, -50%) translateX(${translateX}) scale(${scale})`,
                                      zIndex: zIndex,
                                      opacity: opacity,
                                      filter: `blur(${blur})`,
                                      pointerEvents: pointerEvents as any
                                  }}
                              >
                                  <img src={`/assets/portfolio_assets/CC FTU/Chinese Debate 2025/Social Posts/${filename}`} alt={filename.replace('.png', '')} className="h-[280px] sm:h-[350px] md:h-[420px] w-auto max-w-none block object-contain" />
                              </div>
                          );
                      })}
                  </div>
              </div>"""

content = re.sub(masonry_pattern, new_carousel, content, flags=re.DOTALL)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS")
