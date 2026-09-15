const fs = require('fs');
const file = 'src/app/page.tsx';
let code = fs.readFileSync(file, 'utf8');

const regex = /className="font-\['Fredoka'\] text-3xl md:text-4xl font-bold text-\[#D4AF37\] mb-10 tracking-wide text-center drop-shadow-\[0_0_10px_rgba\(212,175,55,0\.4\)\]">\s*Video Production/g;

const newStr = `className="font-['Fredoka'] text-3xl md:text-4xl font-black text-transparent bg-clip-text bg-gradient-to-b from-[#FFF2B2] to-[#D4AF37] mb-10 tracking-wide text-center" style={{ filter: 'drop-shadow(0px 0px 8px rgba(212,175,55,0.4))' }}>
                      Video Production`;

code = code.replace(regex, newStr);

fs.writeFileSync(file, code);
