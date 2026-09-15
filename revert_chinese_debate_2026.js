const fs = require('fs');
const file = 'src/app/page.tsx';
let code = fs.readFileSync(file, 'utf8');

const oldStr = `<section id="chinese-debate-2026" className="relative w-full pt-12 pb-24 bg-gradient-to-b from-[#06112E] via-[#0B2154] to-[#113B82] text-white overflow-hidden">`;
const newStr = `<section id="chinese-debate-2026" className="relative w-full pt-12 pb-24 bg-gradient-to-b from-[#06112E] to-[#0B1F4D] text-white overflow-hidden">
    {/* Decorative Tech Grid Background */}
    <div className="absolute inset-0 bg-[linear-gradient(rgba(34,211,238,0.03)_1px,transparent_1px),linear-gradient(90deg,rgba(34,211,238,0.03)_1px,transparent_1px)] bg-[size:40px_40px] pointer-events-none"></div>`;

if (code.includes(oldStr)) {
    code = code.replace(oldStr, newStr);
    fs.writeFileSync(file, code);
}
