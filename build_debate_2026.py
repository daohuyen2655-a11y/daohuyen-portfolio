import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the old skeleton block exactly as it appears
old_skeleton = """        {/* Skeleton for Chinese Debate 2026 to ensure the gradient blends perfectly */}
        <section id="chinese-debate-2026" className="relative w-full py-20 bg-gradient-to-b from-[#06112E] to-[#0B1F4D] text-white">
            <div className="max-w-[1400px] mx-auto px-6 text-center">
                <h2 className="font-['Fredoka'] text-[60px] font-bold text-cyan-400 drop-shadow-[0_0_15px_rgba(34,211,238,0.6)]">
                    02. Chinese Debate 2026
                </h2>
            </div>
        </section>"""

# Define the new massive structure
new_structure = """        {/* ─── 02. CHINESE DEBATE 2026 ─── */}
        <section id="chinese-debate-2026" className="relative w-full py-24 bg-gradient-to-b from-[#06112E] to-[#0B1F4D] text-white overflow-hidden">
            {/* Decorative Tech Grid Background */}
            <div className="absolute inset-0 bg-[linear-gradient(rgba(34,211,238,0.03)_1px,transparent_1px),linear-gradient(90deg,rgba(34,211,238,0.03)_1px,transparent_1px)] bg-[size:40px_40px] pointer-events-none"></div>

            <div className="max-w-[1400px] mx-auto px-6 sm:px-10 relative z-20 flex flex-col">
                
                {/* 1. SECTION HEADER */}
                <div className="flex flex-col items-center mb-24 text-center">
                    <div className="px-6 py-2 border border-cyan-500/30 text-cyan-400 rounded-full text-sm font-bold mb-6 tracking-widest uppercase bg-cyan-950/30 backdrop-blur-sm shadow-[0_0_15px_rgba(34,211,238,0.2)]">
                        Event Branding & Social Media
                    </div>
                    <h2 className="font-['Fredoka'] text-[60px] md:text-[90px] font-black text-transparent bg-clip-text bg-gradient-to-r from-cyan-300 to-blue-500 leading-tight drop-shadow-[0_0_25px_rgba(34,211,238,0.4)] mb-6">
                        Chinese Debate '26
                    </h2>
                    <p className="max-w-2xl text-lg text-blue-200/80 font-['Quicksand'] font-medium leading-relaxed">
                        A vibrant and futuristic visual identity designed for the Chinese Debate competition. Emphasizing a dynamic, high-energy cyber aesthetic to captivate a modern youth audience.
                    </p>
                </div>

                {/* 2. KEY VISUAL */}
                <div className="w-full mb-32 flex flex-col items-center">
                    <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-cyan-400 mb-10 tracking-wide drop-shadow-[0_0_10px_rgba(34,211,238,0.5)]">
                        Key Visual
                    </h3>
                    <div className="relative w-full max-w-5xl rounded-[32px] p-2 bg-gradient-to-br from-cyan-500/30 to-blue-900/40 shadow-[0_0_40px_rgba(34,211,238,0.15)] backdrop-blur-md">
                        <div className="w-full aspect-[16/9] rounded-[24px] overflow-hidden bg-[#0A1B45] relative">
                            <img src="/assets/portfolio_assets/CC FTU/Chinese Debate 2026/KEY VISUAL/cover tbth.png" alt="Chinese Debate Key Visual Cover" className="w-full h-full object-cover" />
                        </div>
                    </div>
                    
                    {/* Avatar Badge */}
                    <div className="relative -mt-16 w-32 h-32 md:w-40 md:h-40 rounded-full p-1.5 bg-gradient-to-br from-cyan-400 to-blue-600 shadow-[0_0_30px_rgba(34,211,238,0.4)] z-10 group hover:-translate-y-2 transition-transform duration-300">
                        <div className="w-full h-full rounded-full overflow-hidden bg-[#06112E]">
                            <img src="/assets/portfolio_assets/CC FTU/Chinese Debate 2026/KEY VISUAL/avatar-01.png" alt="Chinese Debate Avatar" className="w-full h-full object-cover" />
                        </div>
                    </div>
                </div>

                {/* 3. EVENT APPLICATIONS (BENTO GRID) */}
                <div className="w-full mb-32">
                    <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-cyan-400 mb-10 tracking-wide text-center drop-shadow-[0_0_10px_rgba(34,211,238,0.5)]">
                        Event Applications
                    </h3>
                    <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                        {/* Backdrop (Spans 2 columns) */}
                        <div className="col-span-1 lg:col-span-2 relative group rounded-[24px] overflow-hidden border border-cyan-900/50 bg-[#0A1A40] shadow-[0_10px_30px_rgba(0,0,0,0.5)] hover:shadow-[0_0_30px_rgba(34,211,238,0.2)] transition-all duration-500">
                            <div className="w-full aspect-video">
                                <img src="/assets/portfolio_assets/CC FTU/Chinese Debate 2026/Print & Event Applications/Backdrop-01.png" alt="Backdrop Design" className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
                            </div>
                            <div className="absolute bottom-0 left-0 w-full p-6 bg-gradient-to-t from-[#06112E] to-transparent">
                                <h4 className="font-bold text-xl text-cyan-300 drop-shadow-md">Stage Backdrop</h4>
                            </div>
                        </div>
                        {/* Ticket (Spans 1 column) */}
                        <div className="col-span-1 relative group rounded-[24px] overflow-hidden border border-cyan-900/50 bg-[#0A1A40] shadow-[0_10px_30px_rgba(0,0,0,0.5)] hover:shadow-[0_0_30px_rgba(34,211,238,0.2)] transition-all duration-500 flex flex-col">
                            <div className="w-full flex-1 min-h-[250px] p-8 flex justify-center items-center">
                                <img src="/assets/portfolio_assets/CC FTU/Chinese Debate 2026/Print & Event Applications/TICKET.png" alt="Event Ticket" className="w-full h-auto max-h-full object-contain group-hover:-translate-y-2 transition-transform duration-500 drop-shadow-2xl" />
                            </div>
                            <div className="w-full p-6 bg-gradient-to-t from-[#06112E] to-transparent mt-auto">
                                <h4 className="font-bold text-xl text-cyan-300 drop-shadow-md">Event Ticket</h4>
                            </div>
                        </div>
                    </div>
                </div>

                {/* 4. SOCIAL MEDIA & VIDEO */}
                <div className="w-full mb-10">
                    <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-cyan-400 mb-10 tracking-wide text-center drop-shadow-[0_0_10px_rgba(34,211,238,0.5)]">
                        Digital & Social
                    </h3>
                    
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        {/* Map through Social Posts */}
                        {[
                            "Công bố quán quân.png", 
                            "Công bố Á quân.png", 
                            "GIA HẠN ĐƠN ĐĂNG KÝ.png", 
                            "Post giới thiệu đại sứ truyền thông.png", 
                            "Post mở đơn.png"
                        ].map((filename, idx) => (
                            <div key={idx} className="relative aspect-square rounded-[20px] overflow-hidden border border-blue-900/60 bg-[#0A1A40] group hover:border-cyan-500/50 transition-colors duration-300 shadow-md">
                                <img src={`/assets/portfolio_assets/CC FTU/Chinese Debate 2026/Social Posts/${filename}`} alt={filename.replace('.png', '')} className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
                            </div>
                        ))}
                        
                        {/* Video Block taking up the 6th slot for symmetry */}
                        <div className="relative aspect-square rounded-[20px] overflow-hidden border border-cyan-500/50 bg-[#0A1A40] group shadow-[0_0_20px_rgba(34,211,238,0.2)] p-2">
                            <div className="w-full h-full rounded-[16px] overflow-hidden relative">
                                 <video src="/assets/portfolio_assets/CC FTU/Chinese Debate 2026/VIDEO/Video công bố top 6 chung kết_.mp4" autoPlay muted loop playsInline className="w-full h-full object-cover" />
                                 <div className="absolute inset-0 bg-cyan-900/20 pointer-events-none mix-blend-overlay"></div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </section>"""

# Perform string replacement safely
if old_skeleton in content:
    content = content.replace(old_skeleton, new_structure)
    with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS")
else:
    print("FAILED: Skeleton not found exactly as requested. Needs regex or manual match.")
