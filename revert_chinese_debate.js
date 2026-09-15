const fs = require('fs');
const file = 'src/app/page.tsx';
let code = fs.readFileSync(file, 'utf8');

const startIndex = code.indexOf('<section id="chinese-debate-2026"');
const endIndex = code.indexOf('</section>', startIndex) + '</section>'.length;

const oldSection = `<section id="chinese-debate-2026" className="relative w-full pt-12 pb-24 bg-gradient-to-b from-[#06112E] to-[#0B1F4D] text-white overflow-hidden">
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
            
            {/* MASONRY LAYOUT FOR PERFECT PACKING */}
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
                        <img src={\`/assets/portfolio_assets/CC FTU/Chinese Debate 2026/Social Posts/\${filename}\`} alt={filename.replace('.png', '')} className="w-full h-auto block group-hover:scale-105 transition-transform duration-500" />
                    </div>
                ))}
            </div>
        </div>

    </div>
</section>`;

code = code.substring(0, startIndex) + oldSection + code.substring(endIndex);
fs.writeFileSync(file, code);
