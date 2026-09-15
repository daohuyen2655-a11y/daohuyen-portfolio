const fs = require('fs');
const file = 'src/app/page.tsx';
let code = fs.readFileSync(file, 'utf8');

// Replace Blue Gradient from-[#74C6F0] to-[#358BBD] -> from-[#5EB8E6] to-[#2A7AA8]
code = code.replace(/from-\[#74C6F0\] to-\[#358BBD\]/g, 'from-[#5EB8E6] to-[#2A7AA8]');

fs.writeFileSync(file, code);
