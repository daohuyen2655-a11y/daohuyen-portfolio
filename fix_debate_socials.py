import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = "{/* Switch back to a robust 2-row x 3-column Grid for perfectly balanced layout of 6 items */}"
end_marker = "</div>\n                </div>\n\n            </div>"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    new_content = """{/* MASONRY LAYOUT FOR PERFECT PACKING */}
                    <div className="columns-1 md:columns-2 lg:columns-3 gap-6 w-full max-w-7xl mx-auto">
                        
                        {/* Video Block */}
                        <div className="relative rounded-[20px] overflow-hidden border-2 border-cyan-500/50 group shadow-[0_0_20px_rgba(34,211,238,0.2)] break-inside-avoid mb-6 inline-block w-full">
                            <video src="/assets/portfolio_assets/CC FTU/Chinese Debate 2026/VIDEO/Video công bố top 6 chung kết_.mp4" autoPlay muted loop playsInline className="w-full h-auto block" />
                        </div>

                        {/* Social Posts */}
                        {[
                            "Công bố quán quân.png", 
                            "GIA HẠN ĐƠN ĐĂNG KÝ.png", 
                            "Công bố Á quân.png", 
                            "Post giới thiệu đại sứ truyền thông.png", 
                            "Post mở đơn.png"
                        ].map((filename, idx) => (
                            <div key={idx} className="relative rounded-[20px] overflow-hidden border-2 border-blue-900/60 group hover:border-cyan-400/80 transition-colors duration-300 shadow-md break-inside-avoid mb-6 inline-block w-full">
                                <img src={`/assets/portfolio_assets/CC FTU/Chinese Debate 2026/Social Posts/${filename}`} alt={filename.replace('.png', '')} className="w-full h-auto block group-hover:scale-105 transition-transform duration-500" />
                            </div>
                        ))}
                    """
    content = content[:start_idx] + new_content + content[end_idx:]
    with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS")
else:
    print("FAILED TO FIND MARKERS")
