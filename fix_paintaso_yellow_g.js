const fs = require('fs');
const file = 'src/app/page.tsx';
let code = fs.readFileSync(file, 'utf8');

// Replace #FFCA28 with #FFE066
code = code.replace(/#FFCA28/g, '#FFE066');

// Fix 'g' clipping on Title: add pb-4 to the h2
const oldTitleStroke = `h2 className="absolute inset-0 font-['Fredoka'] text-[60px] md:text-[90px] font-black leading-none"`;
const newTitleStroke = `h2 className="absolute inset-0 font-['Fredoka'] text-[60px] md:text-[90px] font-black leading-none pb-4"`;
code = code.replace(oldTitleStroke, newTitleStroke);

const oldTitleGrad = `h2 className="relative font-['Fredoka'] text-[60px] md:text-[90px] font-black text-transparent bg-clip-text bg-gradient-to-b from-[#5AB4E5] to-[#1A5E8A] leading-none z-10"`;
const newTitleGrad = `h2 className="relative font-['Fredoka'] text-[60px] md:text-[90px] font-black text-transparent bg-clip-text bg-gradient-to-b from-[#5AB4E5] to-[#1A5E8A] leading-none pb-4 z-10"`;
code = code.replace(oldTitleGrad, newTitleGrad);

// For subheadings, they might also clip 'p' or 'g' or 'y'. Add pb-2 to h3 tags.
const oldH3Stroke = `h3 className="absolute inset-0 font-['Fredoka'] text-3xl md:text-4xl font-black tracking-wide"`;
const newH3Stroke = `h3 className="absolute inset-0 font-['Fredoka'] text-3xl md:text-4xl font-black tracking-wide pb-2"`;
code = code.replace(new RegExp(oldH3Stroke.replace(/\[/g, '\\[').replace(/\]/g, '\\]'), 'g'), newH3Stroke);

const oldH3Grad = `h3 className="relative font-['Fredoka'] text-3xl md:text-4xl font-black tracking-wide text-transparent bg-clip-text bg-gradient-to-b from-[#5AB4E5] to-[#1A5E8A] z-10"`;
const newH3Grad = `h3 className="relative font-['Fredoka'] text-3xl md:text-4xl font-black tracking-wide text-transparent bg-clip-text bg-gradient-to-b from-[#5AB4E5] to-[#1A5E8A] pb-2 z-10"`;
code = code.replace(new RegExp(oldH3Grad.replace(/\[/g, '\\[').replace(/\]/g, '\\]'), 'g'), newH3Grad);

fs.writeFileSync(file, code);
