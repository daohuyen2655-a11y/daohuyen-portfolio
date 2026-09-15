import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

old_block = """<div className="columns-2 md:columns-3 lg:columns-3 gap-6 w-full max-w-[1200px] mx-auto">
                      {[
                          "Thông báo danh sách nhận ĐRL.png",
                          "NTT-01.png",
                          "NTT-02.png",
                          "NTT-03.png",
                          "NTT-04.png"
                      ].map((filename, idx) => (
                          <div key={idx} className="relative rounded-[16px] overflow-hidden border-[4px] border-white shadow-[0_15px_30px_rgba(88,179,211,0.15)] group hover:border-[#8DD1E8] transition-colors duration-300 break-inside-avoid mb-6 inline-block w-full">"""

new_block = """<div className="flex flex-wrap justify-center gap-6 w-full max-w-[1200px] mx-auto">
                      {[
                          "NTT-04.png",
                          "NTT-01.png",
                          "NTT-02.png",
                          "NTT-03.png",
                          "Thông báo danh sách nhận ĐRL.png"
                      ].map((filename, idx) => (
                          <div key={idx} className="relative rounded-[16px] overflow-hidden border-[4px] border-white shadow-[0_15px_30px_rgba(88,179,211,0.15)] group hover:border-[#8DD1E8] transition-colors duration-300 w-full sm:w-[calc(50%-12px)] lg:w-[calc(33.333%-16px)] flex-shrink-0">"""

content = content.replace(old_block, new_block)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS")
