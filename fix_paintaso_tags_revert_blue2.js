const fs = require('fs');
const file = 'src/app/page.tsx';
let code = fs.readFileSync(file, 'utf8');

const oldH3Grad = `from-[#74C6F0] to-[#358BBD]`;
const newH3Grad = `from-[#5EB8E6] to-[#2A7AA8]`;

code = code.replace(new RegExp(oldH3Grad.replace(/\[/g, '\\[').replace(/\]/g, '\\]'), 'g'), newH3Grad);

fs.writeFileSync(file, code);
