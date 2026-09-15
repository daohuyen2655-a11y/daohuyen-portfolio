const fs = require('fs');
const file = 'src/app/page.tsx';
let code = fs.readFileSync(file, 'utf8');

// The tags are h3. We'll specifically replace the gradient on h3 elements.
const oldH3Grad = `h3 className="relative font-['Fredoka'] text-3xl md:text-4xl font-black tracking-wide text-transparent bg-clip-text bg-gradient-to-b from-[#5EB8E6] to-[#2A7AA8] pb-2 z-10"`;
const newH3Grad = `h3 className="relative font-['Fredoka'] text-3xl md:text-4xl font-black tracking-wide text-transparent bg-clip-text bg-gradient-to-b from-[#3C9DD6] to-[#1A5780] pb-2 z-10"`;

code = code.replace(new RegExp(oldH3Grad.replace(/\[/g, '\\[').replace(/\]/g, '\\]'), 'g'), newH3Grad);

fs.writeFileSync(file, code);
