const fs = require('fs');
const file = 'src/app/page.tsx';
let code = fs.readFileSync(file, 'utf8');

// Title
code = code.replace(
    `className="font-['Fredoka'] text-[50px] md:text-[80px] font-black text-transparent bg-clip-text bg-gradient-to-b from-[#A1C97A] to-[#2C4424] leading-none mb-6 pb-2" style={{ filter: 'drop-shadow(0px 0px 10px rgba(255,255,255,1))' }}>`,
    `className="font-['Fredoka'] text-[50px] md:text-[80px] font-black text-[#2C4424] leading-none mb-6 pb-2 drop-shadow-[4px_4px_0_white]">`
);

// Key Visual
code = code.replace(
    `className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#3B5B35] mb-10 tracking-wide">
                      Key Visual`,
    `className="font-['Fredoka'] text-3xl md:text-4xl font-black text-[#2C4424] mb-10 tracking-wide drop-shadow-[2px_2px_0_white]">
                      Key Visual`
);

// Event Applications
code = code.replace(
    `className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#3B5B35] mb-10 tracking-wide text-center">
                      Event Applications`,
    `className="font-['Fredoka'] text-3xl md:text-4xl font-black text-[#2C4424] mb-10 tracking-wide text-center drop-shadow-[2px_2px_0_white]">
                      Event Applications`
);

// Digital & Social
code = code.replace(
    `className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#3B5B35] mb-10 tracking-wide text-center">
                      Digital & Social`,
    `className="font-['Fredoka'] text-3xl md:text-4xl font-black text-[#2C4424] mb-10 tracking-wide text-center drop-shadow-[2px_2px_0_white]">
                      Digital & Social`
);

fs.writeFileSync(file, code);
