const fs = require('fs');
const file = 'src/app/page.tsx';
let code = fs.readFileSync(file, 'utf8');

// Replace Yellow outline #FFE885 -> #FFE066
code = code.replace(/#FFE885/g, '#FFE066');

fs.writeFileSync(file, code);
