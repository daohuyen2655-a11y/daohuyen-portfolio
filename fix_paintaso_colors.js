const fs = require('fs');
const file = 'src/app/page.tsx';
let code = fs.readFileSync(file, 'utf8');

// Replace Yellow outline #FFE066 -> #FFE885
code = code.replace(/#FFE066/g, '#FFE885');

// Replace Blue Gradient
code = code.replace(/from-\[#5AB4E5\] to-\[#1A5E8A\]/g, 'from-[#74C6F0] to-[#358BBD]');

fs.writeFileSync(file, code);
