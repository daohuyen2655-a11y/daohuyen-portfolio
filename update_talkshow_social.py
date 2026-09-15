import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Target the existing Digital & Social block in Talkshow
old_block = """{/* 3. DIGITAL & SOCIAL */}
              <div className="w-full mb-10 flex flex-col items-center">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#4194B1] mb-10 tracking-wide drop-shadow-[0_0_10px_rgba(255,255,255,1)] text-center">
                      Digital & Social
                  </h3>
                  <div className="relative max-w-2xl w-full rounded-[24px] overflow-hidden border-[4px] border-white shadow-[0_20px_50px_rgba(88,179,211,0.2)] group hover:border-[#8DD1E8] transition-colors duration-500">
                      <img src="/assets/portfolio_assets/CC FTU/Talkshow/SOCIAL POST/Thông báo danh sách nhận ĐRL.png" alt="Social Post" className="w-full h-auto block group-hover:scale-[1.02] transition-transform duration-700" />
                  </div>
                  <h4 className="font-['Quicksand'] font-bold text-lg text-[#4194B1] tracking-wider uppercase mt-8 bg-white/70 px-6 py-2 rounded-full shadow-sm">
                      Social Media Post
                  </h4>
              </div>"""

new_block = """{/* 3. DIGITAL & SOCIAL */}
              <div className="w-full mb-10 flex flex-col items-center">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#4194B1] mb-10 tracking-wide drop-shadow-[0_0_10px_rgba(255,255,255,1)] text-center">
                      Digital & Social
                  </h3>
                  
                  <div className="columns-2 md:columns-3 lg:columns-3 gap-6 w-full max-w-[1200px] mx-auto">
                      {[
                          "Thông báo danh sách nhận ĐRL.png",
                          "NTT-01.png",
                          "NTT-02.png",
                          "NTT-03.png",
                          "NTT-04.png"
                      ].map((filename, idx) => (
                          <div key={idx} className="relative rounded-[16px] overflow-hidden border-[4px] border-white shadow-[0_15px_30px_rgba(88,179,211,0.15)] group hover:border-[#8DD1E8] transition-colors duration-300 break-inside-avoid mb-6 inline-block w-full">
                              <img src={`/assets/portfolio_assets/CC FTU/Talkshow/SOCIAL POST/${filename}`} alt={filename.replace('.png', '')} className="w-full h-auto block group-hover:scale-105 transition-transform duration-500" loading="lazy" />
                          </div>
                      ))}
                  </div>
                  <h4 className="font-['Quicksand'] font-bold text-lg text-[#4194B1] tracking-wider uppercase mt-4 bg-white/70 px-6 py-2 rounded-full shadow-sm">
                      Social Media Posts & Partners
                  </h4>
              </div>"""

content = content.replace(old_block, new_block)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS")
