const fs = require('fs');
const file = 'src/app/page.tsx';
let code = fs.readFileSync(file, 'utf8');

// Key Visual
code = code.replace(
    `className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#4194B1] mb-10 tracking-wide drop-shadow-[0_0_10px_rgba(255,255,255,1)]">
                      Key Visual`,
    `className="font-['Fredoka'] text-3xl md:text-4xl font-black text-transparent bg-clip-text bg-gradient-to-b from-[#8DD1E8] to-[#4194B1] mb-10 tracking-wide" style={{ filter: 'drop-shadow(0px 0px 8px rgba(255,255,255,0.9))' }}>
                      Key Visual`
);

// Digital & Social
code = code.replace(
    `className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#4194B1] mb-10 tracking-wide drop-shadow-[0_0_10px_rgba(255,255,255,1)] text-center">
                      Digital & Social`,
    `className="font-['Fredoka'] text-3xl md:text-4xl font-black text-transparent bg-clip-text bg-gradient-to-b from-[#8DD1E8] to-[#4194B1] mb-10 tracking-wide text-center" style={{ filter: 'drop-shadow(0px 0px 8px rgba(255,255,255,0.9))' }}>
                      Digital & Social`
);

fs.writeFileSync(file, code);
