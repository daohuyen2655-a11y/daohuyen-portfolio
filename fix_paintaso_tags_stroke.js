const fs = require('fs');
const file = 'src/app/page.tsx';
let code = fs.readFileSync(file, 'utf8');

const oldH3Stroke = `h3 className="absolute inset-0 font-['Fredoka'] text-3xl md:text-4xl font-black tracking-wide pb-2" style={{ WebkitTextStroke: '6px #FFE885', color: '#FFE885' }}`;
const newH3Stroke = `h3 className="absolute inset-0 font-['Fredoka'] text-3xl md:text-4xl font-black tracking-wide pb-2" style={{ WebkitTextStroke: '4px #FFE885', color: '#FFE885' }}`;

code = code.replace(new RegExp(oldH3Stroke.replace(/\[/g, '\\[').replace(/\]/g, '\\]').replace(/\{/g, '\\{').replace(/\}/g, '\\}'), 'g'), newH3Stroke);

fs.writeFileSync(file, code);
