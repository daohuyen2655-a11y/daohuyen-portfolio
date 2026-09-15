const fs = require('fs');
const file = 'src/app/page.tsx';
let code = fs.readFileSync(file, 'utf8');

// Key Visual
code = code.replace(
    `className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#D4AF37] mb-10 tracking-wide drop-shadow-[0_0_10px_rgba(212,175,55,0.4)]">
                      Key Visual`,
    `className="font-['Fredoka'] text-3xl md:text-4xl font-black text-transparent bg-clip-text bg-gradient-to-b from-[#FFF2B2] to-[#D4AF37] mb-10 tracking-wide" style={{ filter: 'drop-shadow(0px 0px 15px rgba(212,175,55,0.5))' }}>
                      Key Visual`
);

// Event Applications
code = code.replace(
    `className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#D4AF37] mb-10 tracking-wide drop-shadow-[0_0_10px_rgba(212,175,55,0.4)] text-center">
                      Event Applications`,
    `className="font-['Fredoka'] text-3xl md:text-4xl font-black text-transparent bg-clip-text bg-gradient-to-b from-[#FFF2B2] to-[#D4AF37] mb-10 tracking-wide text-center" style={{ filter: 'drop-shadow(0px 0px 15px rgba(212,175,55,0.5))' }}>
                      Event Applications`
);

// Digital & Social
code = code.replace(
    `className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#D4AF37] mb-10 tracking-wide text-center drop-shadow-[0_0_10px_rgba(212,175,55,0.4)]">
                      Digital & Social`,
    `className="font-['Fredoka'] text-3xl md:text-4xl font-black text-transparent bg-clip-text bg-gradient-to-b from-[#FFF2B2] to-[#D4AF37] mb-10 tracking-wide text-center" style={{ filter: 'drop-shadow(0px 0px 15px rgba(212,175,55,0.5))' }}>
                      Digital & Social`
);

fs.writeFileSync(file, code);
