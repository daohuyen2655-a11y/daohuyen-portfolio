const fs = require('fs');
const file = 'src/app/page.tsx';
let code = fs.readFileSync(file, 'utf8');

const regexTitleGlow = /className="font-\['Fredoka'\] text-\[60px\] md:text-\[90px\] font-black text-transparent bg-clip-text bg-gradient-to-b from-\[#FFF2B2\] to-\[#D4AF37\] leading-none mb-6 pb-2" style=\{\{ filter: 'drop-shadow\(0px 0px 15px rgba\(212,175,55,0\.5\)\)' \}\}/g;
const newTitleGlow = `className="font-['Fredoka'] text-[60px] md:text-[90px] font-black text-transparent bg-clip-text bg-gradient-to-b from-[#FFF2B2] to-[#D4AF37] leading-none mb-6 pb-2" style={{ filter: 'drop-shadow(0px 0px 8px rgba(212,175,55,0.4))' }}`;

code = code.replace(regexTitleGlow, newTitleGlow);


const regexTagGlow = /style=\{\{ filter: 'drop-shadow\(0px 0px 15px rgba\(212,175,55,0\.5\)\)' \}\}/g;
const newTagGlow = `style={{ filter: 'drop-shadow(0px 0px 8px rgba(212,175,55,0.4))' }}`;

// Apply to the remaining (the subheadings)
code = code.replace(regexTagGlow, newTagGlow);

fs.writeFileSync(file, code);
