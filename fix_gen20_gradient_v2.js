const fs = require('fs');
const file = 'src/app/page.tsx';
let code = fs.readFileSync(file, 'utf8');

const regexTitle = /className="font-\['Fredoka'\] text-\[50px\] md:text-\[80px\] font-black text-transparent bg-clip-text bg-gradient-to-b from-\[#[A-F0-9]+\] to-\[#[A-F0-9]+\] leading-none mb-6 pb-2" style=\{\{ filter: 'drop-shadow\([^)]+\)' \}\}/g;

const newTitle = `className="font-['Fredoka'] text-[50px] md:text-[80px] font-black text-transparent bg-clip-text bg-gradient-to-b from-[#82BA5D] to-[#2A5212] leading-none mb-6 pb-2" style={{ filter: 'drop-shadow(0px 0px 10px rgba(255,255,255,1))' }}`;

code = code.replace(regexTitle, newTitle);

const regexSubheading = /className="font-\['Fredoka'\] text-3xl md:text-4xl font-black text-transparent bg-clip-text bg-gradient-to-b from-\[#[A-F0-9]+\] to-\[#[A-F0-9]+\] mb-10 tracking-wide( text-center)?" style=\{\{ filter: 'drop-shadow\([^)]+\)' \}\}/g;

code = code.replace(regexSubheading, (match, p1) => {
    let centerClass = p1 ? " text-center" : "";
    return `className="font-['Fredoka'] text-3xl md:text-4xl font-black text-transparent bg-clip-text bg-gradient-to-b from-[#82BA5D] to-[#2A5212] mb-10 tracking-wide${centerClass}" style={{ filter: 'drop-shadow(0px 0px 8px rgba(255,255,255,0.9))' }}`;
});


fs.writeFileSync(file, code);
