const fs = require('fs');
const file = 'src/app/page.tsx';
let code = fs.readFileSync(file, 'utf8');

// 1. Extend the Zodiac section padding
const oldZodiacClass = `className="relative w-full py-32 bg-gradient-to-b from-[#F9F7F3] via-[#F4F0E8] to-[#EBE4D5] overflow-hidden"`;
const newZodiacClass = `className="relative w-full pt-32 pb-[200px] md:pb-[250px] bg-gradient-to-b from-[#F9F7F3] via-[#F4F0E8] to-[#EBE4D5] overflow-hidden"`;
code = code.replace(oldZodiacClass, newZodiacClass);

// 2. Add the wavy divider at the end of Zodiac section
const oldZodiacEnd = `              </div>
           </div>
        </section>`;
        
const newZodiacEnd = `              </div>
           </div>
           
           {/* Wavy Divider Transition to Paintaso */}
           <div className="absolute bottom-0 left-0 w-full overflow-hidden leading-[0] z-0">
               <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320" className="w-full h-16 sm:h-24 md:h-32 block" preserveAspectRatio="none">
                   <path fill="#EEF8FF" fillOpacity="1" d="M0,224L48,213.3C96,203,192,181,288,186.7C384,192,480,224,576,213.3C672,203,768,149,864,138.7C960,128,1056,160,1152,176C1248,192,1344,192,1392,192L1440,192L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path>
               </svg>
           </div>
        </section>`;

// Replace only the FIRST matching oldZodiacEnd (which should be the Zodiac one, since Paintaso already got replaced)
// Wait, Paintaso's end is:
/*
           {/* Wavy Divider Transition to Footer *\/}
           <div className="absolute bottom-0 left-0 w-full overflow-hidden leading-[0] z-0">
               <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320" className="w-full h-16 sm:h-24 md:h-32 block" preserveAspectRatio="none">
*/
// So oldZodiacEnd is unique to Zodiac.

code = code.replace(oldZodiacEnd, newZodiacEnd);

fs.writeFileSync(file, code);
