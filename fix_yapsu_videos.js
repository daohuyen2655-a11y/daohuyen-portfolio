const fs = require('fs');
const file = 'src/app/page.tsx';
let code = fs.readFileSync(file, 'utf8');

code = code.replace(
    '{ title: "Onboarding", src: "Onboarding Feature.MP4" }',
    '{ title: "Onboarding", src: "onboarding-feature.mp4" }'
);
code = code.replace(
    '{ title: "Roleplay", src: "Roleplay Feature.MP4" }',
    '{ title: "Roleplay", src: "roleplay-feature.mp4" }'
);
code = code.replace(
    '{ title: "Roadmap", src: "Roadmap + Drill Feature.mov" }',
    '{ title: "Roadmap", src: "roadmap-drill-feature.mov" }'
);

code = code.replace(
    '`/assets/portfolio_assets/Yapsu AI/${vid.src}`',
    '`/assets/yapsu-ai/${vid.src}`'
);

fs.writeFileSync(file, code);
