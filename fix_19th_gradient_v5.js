const fs = require('fs');
const file = 'src/app/page.tsx';
let code = fs.readFileSync(file, 'utf8');

code = code.replace(/from-\[#D1B3FF\] to-\[#8665C3\]/g, 'from-[#B48CF5] to-[#6A3CC9]');

fs.writeFileSync(file, code);
