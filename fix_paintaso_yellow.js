const fs = require('fs');
const file = 'src/app/page.tsx';
let code = fs.readFileSync(file, 'utf8');

// Replace all #FDEECA with #FFCA28 (warm golden yellow) in the Paintaso section.
code = code.replace(/#FDEECA/g, '#FFCA28');

fs.writeFileSync(file, code);
