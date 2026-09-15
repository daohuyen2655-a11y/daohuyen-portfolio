const fs = require('fs');
const file = 'src/app/page.tsx';
let code = fs.readFileSync(file, 'utf8');

// Replace Yellow outline #FFE066 -> #FFE885
code = code.replace(/#FFE066/g, '#FFE885');

fs.writeFileSync(file, code);
