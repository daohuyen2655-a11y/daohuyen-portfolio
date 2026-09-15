import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = "{/* 2. KEY VISUAL */}"
end_marker = "</div>\n        </section>"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    new_content = """{/* 2. KEY VISUAL */}
                <div className="w-full mb-32 flex flex-col items-center">
                    <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-cyan-400 mb-10 tracking-wide drop-shadow-[0_0_10px_rgba(34,211,238,0.5)]">
                        Key Visual
                    </h3>
                    <div className="relative w-full max-w-5xl rounded-[24px] overflow-hidden border-2 border-cyan-500/50 shadow-[0_0_40px_rgba(34,211,238,0.2)]">
                        <img src="/assets/portfolio_assets/CC FTU/Chinese Debate 2026/KEY VISUAL/cover tbth.png" alt="Chinese Debate Key Visual Cover" className="w-full h-auto block" />
                    </div>
                    
                    {/* Avatar Badge */}
                    <div className="relative -mt-16 w-32 h-32 md:w-40 md:h-40 rounded-full p-1 bg-gradient-to-br from-cyan-400 to-blue-600 shadow-[0_0_30px_rgba(34,211,238,0.5)] z-10 group hover:-translate-y-2 transition-transform duration-300">
                        <div className="w-full h-full rounded-full overflow-hidden bg-[#06112E]">
                            <img src="/assets/portfolio_assets/CC FTU/Chinese Debate 2026/KEY VISUAL/avatar-01.png" alt="Chinese Debate Avatar" className="w-full h-full object-cover" />
                        </div>
                    </div>
                </div>

                {/* 3. EVENT APPLICATIONS */}
                <div className="w-full mb-32 flex flex-col items-center">
                    <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-cyan-400 mb-10 tracking-wide text-center drop-shadow-[0_0_10px_rgba(34,211,238,0.5)]">
                        Event Applications
                    </h3>
                    <div className="w-full max-w-5xl flex flex-col gap-16">
                        {/* Backdrop */}
                        <div className="flex flex-col items-center gap-5">
                            <div className="relative group w-full rounded-[24px] overflow-hidden border-2 border-cyan-900/60 hover:border-cyan-400/80 transition-colors duration-500 shadow-[0_0_30px_rgba(34,211,238,0.1)]">
                                <img src="/assets/portfolio_assets/CC FTU/Chinese Debate 2026/Print & Event Applications/Backdrop-01.png" alt="Backdrop Design" className="w-full h-auto block group-hover:scale-[1.02] transition-transform duration-700" />
                            </div>
                            <h4 className="font-['Quicksand'] font-bold text-xl text-cyan-300 tracking-wider uppercase drop-shadow-md">Stage Backdrop</h4>
                        </div>
                        {/* Ticket */}
                        <div className="flex flex-col items-center gap-5">
                            <div className="relative group w-full max-w-3xl mx-auto rounded-[24px] overflow-hidden border-2 border-cyan-900/60 hover:border-cyan-400/80 transition-colors duration-500 shadow-[0_0_30px_rgba(34,211,238,0.1)]">
                                <img src="/assets/portfolio_assets/CC FTU/Chinese Debate 2026/Print & Event Applications/TICKET.png" alt="Event Ticket" className="w-full h-auto block group-hover:scale-[1.02] transition-transform duration-700 drop-shadow-xl" />
                            </div>
                            <h4 className="font-['Quicksand'] font-bold text-xl text-cyan-300 tracking-wider uppercase drop-shadow-md">Event Ticket</h4>
                        </div>
                    </div>
                </div>

                {/* 4. DIGITAL & SOCIAL */}
                <div className="w-full mb-10">
                    <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-cyan-400 mb-10 tracking-wide text-center drop-shadow-[0_0_10px_rgba(34,211,238,0.5)]">
                        Digital & Social
                    </h3>
                    
                    {/* Switch back to a robust 2-row x 3-column Grid for perfectly balanced layout of 6 items */}
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 items-start">
                        {/* Video Block */}
                        <div className="relative rounded-[20px] overflow-hidden border-2 border-cyan-500/50 group shadow-[0_0_20px_rgba(34,211,238,0.2)]">
                            <video src="/assets/portfolio_assets/CC FTU/Chinese Debate 2026/VIDEO/Video công bố top 6 chung kết_.mp4" autoPlay muted loop playsInline className="w-full h-auto block" />
                        </div>

                        {/* Social Posts */}
                        {[
                            "Công bố quán quân.png", 
                            "Công bố Á quân.png", 
                            "GIA HẠN ĐƠN ĐĂNG KÝ.png", 
                            "Post giới thiệu đại sứ truyền thông.png", 
                            "Post mở đơn.png"
                        ].map((filename, idx) => (
                            <div key={idx} className="relative rounded-[20px] overflow-hidden border-2 border-blue-900/60 group hover:border-cyan-400/80 transition-colors duration-300 shadow-md">
                                <img src={`/assets/portfolio_assets/CC FTU/Chinese Debate 2026/Social Posts/${filename}`} alt={filename.replace('.png', '')} className="w-full h-auto block group-hover:scale-105 transition-transform duration-500" />
                            </div>
                        ))}
                    </div>
                </div>

            </div>
"""
    content = content[:start_idx] + new_content + content[end_idx:]
    with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS")
else:
    print("FAILED TO FIND MARKERS")
