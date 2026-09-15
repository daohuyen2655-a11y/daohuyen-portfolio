const fs = require('fs');
const file = 'src/app/page.tsx';
let code = fs.readFileSync(file, 'utf8');

const regexTitle = /className="font-\['Fredoka'\] text-\[60px\] md:text-\[90px\] font-black text-transparent bg-clip-text bg-gradient-to-b from-\[#[A-F0-9]+\] to-\[#[A-F0-9]+\] leading-none mb-6 pb-2" style=\{\{ filter: 'drop-shadow\([^)]+\)' \}\}/g;

const newTitle = `className="font-['Fredoka'] text-[60px] md:text-[90px] font-black text-transparent bg-clip-text bg-gradient-to-b from-[#A374F5] to-[#4B2299] leading-none mb-6 pb-2" style={{ filter: 'drop-shadow(0px 0px 10px rgba(255,255,255,1))' }}`;

code = code.replace(regexTitle, newTitle);

// Subheading: Key Visual
code = code.replace(
    `className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#8665C3] mb-10 tracking-wide">
                      Key Visual`,
    `className="font-['Fredoka'] text-3xl md:text-4xl font-black text-transparent bg-clip-text bg-gradient-to-b from-[#A374F5] to-[#4B2299] mb-10 tracking-wide" style={{ filter: 'drop-shadow(0px 0px 8px rgba(255,255,255,0.9))' }}>
                      Key Visual`
);

// Subheading: Event Applications
code = code.replace(
    `className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#8665C3] mb-10 tracking-wide text-center">
                      Event Applications`,
    `className="font-['Fredoka'] text-3xl md:text-4xl font-black text-transparent bg-clip-text bg-gradient-to-b from-[#A374F5] to-[#4B2299] mb-10 tracking-wide text-center" style={{ filter: 'drop-shadow(0px 0px 8px rgba(255,255,255,0.9))' }}>
                      Event Applications`
);

fs.writeFileSync(file, code);
