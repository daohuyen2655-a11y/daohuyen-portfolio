const fs = require('fs');
const file = 'src/app/page.tsx';
let code = fs.readFileSync(file, 'utf8');

const startIndex = code.indexOf('<section id="chinese-debate-2026"');
const endIndex = code.indexOf('</section>', startIndex) + '</section>'.length;

const newSection = `<section id="chinese-debate-2026" className="relative w-full pt-12 pb-24 bg-gradient-to-b from-[#E6F4F1] via-[#D6EEED] to-[#C1E6E7] text-[#1E293B] overflow-hidden font-sans">
    
    {/* Transition from Yapsu (Peach) to Chinese Debate (Light Teal) */}
    <div className="absolute top-0 left-0 w-full h-[100px] bg-gradient-to-b from-[#FFD8B5] to-[#E6F4F1] z-10 pointer-events-none"></div>

    <div className="max-w-[1400px] mx-auto px-6 sm:px-10 relative z-20 flex flex-col">
        
        {/* 1. SECTION HEADER */}
        <div className="flex flex-col items-center mb-24 text-center mt-12">
            <div className="px-6 py-2 border-[4px] border-white text-[#0B6E70] rounded-full text-sm font-bold mb-6 tracking-widest uppercase bg-white/50 backdrop-blur-sm shadow-md">
                Event Branding & Social Media
            </div>
            <h2 className="font-['Fredoka'] text-[60px] md:text-[90px] font-black text-transparent bg-clip-text bg-gradient-to-r from-[#0B6E70] to-[#1D4ED8] leading-tight drop-shadow-md mb-6">
                Chinese Debate '26
            </h2>
            <p className="max-w-2xl text-lg text-[#334155] font-['Quicksand'] font-medium leading-relaxed">
                A vibrant and futuristic visual identity designed for the Chinese Debate competition. Emphasizing a dynamic, high-energy cyber aesthetic to captivate a modern youth audience.
            </p>
        </div>

        {/* 2. KEY VISUAL */}
        <div className="w-full mb-32 flex flex-col items-center">
            <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#0B6E70] mb-10 tracking-wide drop-shadow-sm">
                Key Visual
            </h3>
            <div className="relative w-full max-w-5xl rounded-[24px] overflow-hidden border-[8px] border-white shadow-[0_15px_30px_rgba(11,110,112,0.15)]">
                <img src="/assets/portfolio_assets/CC FTU/Chinese Debate 2026/KEY VISUAL/cover tbth.png" alt="Chinese Debate Key Visual Cover" className="w-full h-auto block" />
            </div>
            
            {/* Avatar Badge */}
            <div className="relative -mt-16 w-32 h-32 md:w-40 md:h-40 rounded-full p-2 bg-white shadow-[0_10px_20px_rgba(11,110,112,0.2)] z-10 group hover:-translate-y-2 transition-transform duration-300">
                <div className="w-full h-full rounded-full overflow-hidden bg-[#E6F4F1]">
                    <img src="/assets/portfolio_assets/CC FTU/Chinese Debate 2026/KEY VISUAL/avatar-01.png" alt="Chinese Debate Avatar" className="w-full h-full object-cover" />
                </div>
            </div>
        </div>

        {/* 3. EVENT APPLICATIONS */}
        <div className="w-full mb-32 flex flex-col items-center">
            <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#0B6E70] mb-10 tracking-wide text-center drop-shadow-sm">
                Event Applications
            </h3>
            <div className="w-full max-w-5xl flex flex-col gap-16">
                {/* Backdrop */}
                <div className="flex flex-col items-center gap-5">
                    <div className="relative group w-full rounded-[24px] overflow-hidden border-[6px] border-white hover:border-[#0B6E70] transition-colors duration-500 shadow-[0_15px_30px_rgba(11,110,112,0.15)]">
                        <img src="/assets/portfolio_assets/CC FTU/Chinese Debate 2026/Print & Event Applications/Backdrop-01.png" alt="Backdrop Design" className="w-full h-auto block group-hover:scale-[1.02] transition-transform duration-700" />
                    </div>
                    <h4 className="font-['Quicksand'] font-bold text-xl text-[#0B6E70] tracking-wider uppercase drop-shadow-sm">Stage Backdrop</h4>
                </div>
                {/* Ticket */}
                <div className="flex flex-col items-center gap-5">
                    <div className="relative group w-full max-w-3xl mx-auto rounded-[24px] overflow-hidden border-[6px] border-white hover:border-[#0B6E70] transition-colors duration-500 shadow-[0_15px_30px_rgba(11,110,112,0.15)]">
                        <img src="/assets/portfolio_assets/CC FTU/Chinese Debate 2026/Print & Event Applications/TICKET.png" alt="Event Ticket" className="w-full h-auto block group-hover:scale-[1.02] transition-transform duration-700 drop-shadow-md" />
                    </div>
                    <h4 className="font-['Quicksand'] font-bold text-xl text-[#0B6E70] tracking-wider uppercase drop-shadow-sm">Event Ticket</h4>
                </div>
            </div>
        </div>

        {/* 4. DIGITAL & SOCIAL */}
        <div className="w-full mb-10">
            <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#0B6E70] mb-10 tracking-wide text-center drop-shadow-sm">
                Digital & Social
            </h3>
            
            {/* MASONRY LAYOUT FOR PERFECT PACKING */}
            <div className="columns-1 md:columns-2 lg:columns-3 gap-6 w-full max-w-7xl mx-auto">
                
                {/* Video Block */}
                <div className="relative rounded-[20px] overflow-hidden border-[6px] border-white group shadow-[0_10px_20px_rgba(11,110,112,0.1)] break-inside-avoid mb-6 inline-block w-full">
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
                    <div key={idx} className="relative rounded-[20px] overflow-hidden border-[6px] border-white group hover:border-[#0B6E70] transition-colors duration-300 shadow-[0_10px_20px_rgba(11,110,112,0.1)] break-inside-avoid mb-6 inline-block w-full">
                        <img src={\`/assets/portfolio_assets/CC FTU/Chinese Debate 2026/Social Posts/\${filename}\`} alt={filename.replace('.png', '')} className="w-full h-auto block group-hover:scale-105 transition-transform duration-500" />
                    </div>
                ))}
            </div>
        </div>

    </div>
</section>`;

code = code.substring(0, startIndex) + newSection + code.substring(endIndex);
fs.writeFileSync(file, code);
