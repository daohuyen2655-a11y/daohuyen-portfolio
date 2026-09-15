const fs = require('fs');
const file = 'src/app/page.tsx';
let code = fs.readFileSync(file, 'utf8');

// Title
code = code.replace(
    `className="font-['Fredoka'] text-[50px] md:text-[80px] font-black text-[#2C4424] leading-none mb-6 pb-2 drop-shadow-[4px_4px_0_white]">`,
    `className="font-['Fredoka'] text-[50px] md:text-[80px] font-black text-transparent bg-clip-text bg-gradient-to-b from-[#55823E] to-[#16290C] leading-none mb-6 pb-2" style={{ filter: 'drop-shadow(3px 3px 0px white)' }}>`
);

// Key Visual
code = code.replace(
    `className="font-['Fredoka'] text-3xl md:text-4xl font-black text-[#2C4424] mb-10 tracking-wide drop-shadow-[2px_2px_0_white]">
                      Key Visual`,
    `className="font-['Fredoka'] text-3xl md:text-4xl font-black text-transparent bg-clip-text bg-gradient-to-b from-[#55823E] to-[#16290C] mb-10 tracking-wide" style={{ filter: 'drop-shadow(2px 2px 0px white)' }}>
                      Key Visual`
);

// Event Applications
code = code.replace(
    `className="font-['Fredoka'] text-3xl md:text-4xl font-black text-[#2C4424] mb-10 tracking-wide text-center drop-shadow-[2px_2px_0_white]">
                      Event Applications`,
    `className="font-['Fredoka'] text-3xl md:text-4xl font-black text-transparent bg-clip-text bg-gradient-to-b from-[#55823E] to-[#16290C] mb-10 tracking-wide text-center" style={{ filter: 'drop-shadow(2px 2px 0px white)' }}>
                      Event Applications`
);

// Digital & Social
code = code.replace(
    `className="font-['Fredoka'] text-3xl md:text-4xl font-black text-[#2C4424] mb-10 tracking-wide text-center drop-shadow-[2px_2px_0_white]">
                      Digital & Social`,
    `className="font-['Fredoka'] text-3xl md:text-4xl font-black text-transparent bg-clip-text bg-gradient-to-b from-[#55823E] to-[#16290C] mb-10 tracking-wide text-center" style={{ filter: 'drop-shadow(2px 2px 0px white)' }}>
                      Digital & Social`
);

fs.writeFileSync(file, code);
