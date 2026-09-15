import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = "{/* 3. EVENT APPLICATIONS (BENTO GRID) */}"
end_marker = "</div>\n        </section>"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    new_layout = """{/* 3. EVENT APPLICATIONS */}
                <div className="w-full mb-32 flex flex-col items-center">
                    <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-cyan-400 mb-10 tracking-wide text-center drop-shadow-[0_0_10px_rgba(34,211,238,0.5)]">
                        Event Applications
                    </h3>
                    <div className="w-full max-w-5xl flex flex-col gap-12">
                        {/* Backdrop */}
                        <div className="relative group w-full rounded-[24px] overflow-hidden border border-cyan-900/50 bg-[#0A1B45] p-2 shadow-[0_0_40px_rgba(34,211,238,0.08)]">
                            <img src="/assets/portfolio_assets/CC FTU/Chinese Debate 2026/Print & Event Applications/Backdrop-01.png" alt="Backdrop Design" className="w-full h-auto rounded-[18px] group-hover:scale-[1.02] transition-transform duration-500" />
                        </div>
                        {/* Ticket - Centered and constrained */}
                        <div className="relative group w-full max-w-2xl mx-auto rounded-[24px] overflow-hidden border border-cyan-900/50 bg-[#0A1B45] p-2 shadow-[0_0_40px_rgba(34,211,238,0.08)]">
                            <img src="/assets/portfolio_assets/CC FTU/Chinese Debate 2026/Print & Event Applications/TICKET.png" alt="Event Ticket" className="w-full h-auto rounded-[18px] group-hover:scale-[1.02] transition-transform duration-500 drop-shadow-xl" />
                        </div>
                    </div>
                </div>

                {/* 4. DIGITAL & SOCIAL (MASONRY LAYOUT) */}
                <div className="w-full mb-10">
                    <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-cyan-400 mb-10 tracking-wide text-center drop-shadow-[0_0_10px_rgba(34,211,238,0.5)]">
                        Digital & Social
                    </h3>
                    
                    <div className="columns-1 md:columns-2 lg:columns-3 gap-6 space-y-6">
                        {/* Video Block */}
                        <div className="relative rounded-[20px] overflow-hidden border border-cyan-500/50 bg-[#0A1A40] group shadow-[0_0_20px_rgba(34,211,238,0.2)] break-inside-avoid">
                            <video src="/assets/portfolio_assets/CC FTU/Chinese Debate 2026/VIDEO/Video công bố top 6 chung kết_.mp4" autoPlay muted loop playsInline className="w-full h-auto object-cover" />
                        </div>

                        {/* Map through Social Posts */}
                        {[
                            "Công bố quán quân.png", 
                            "Công bố Á quân.png", 
                            "GIA HẠN ĐƠN ĐĂNG KÝ.png", 
                            "Post giới thiệu đại sứ truyền thông.png", 
                            "Post mở đơn.png"
                        ].map((filename, idx) => (
                            <div key={idx} className="relative rounded-[20px] overflow-hidden border border-blue-900/60 bg-[#0A1A40] group hover:border-cyan-500/50 transition-colors duration-300 shadow-md break-inside-avoid">
                                <img src={`/assets/portfolio_assets/CC FTU/Chinese Debate 2026/Social Posts/${filename}`} alt={filename.replace('.png', '')} className="w-full h-auto block group-hover:scale-105 transition-transform duration-500" />
                            </div>
                        ))}
                    </div>
                </div>

            </div>
"""
    content = content[:start_idx] + new_layout + content[end_idx:]
    with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS")
else:
    print("FAILED TO FIND MARKERS")
