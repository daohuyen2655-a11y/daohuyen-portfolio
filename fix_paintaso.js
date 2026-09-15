const fs = require('fs');
const file = 'src/app/page.tsx';
let code = fs.readFileSync(file, 'utf8');

// Title
const oldTitle = `<h2 className="font-['Fredoka'] text-[60px] md:text-[90px] font-black text-transparent bg-clip-text bg-gradient-to-b from-[#5AB4E5] to-[#1A5E8A] leading-none mb-6 pb-2" style={{ filter: 'drop-shadow(0px 0px 12px rgba(255,255,255,1))' }}>
                      Tô Bình Yên
                  </h2>`;

const newTitle = `<div className="relative inline-block mb-6 pb-2">
                      {/* Outline Layer */}
                      <h2 className="absolute inset-0 font-['Fredoka'] text-[60px] md:text-[90px] font-black leading-none" style={{ WebkitTextStroke: '10px #FDEECA', color: '#FDEECA' }} aria-hidden="true">
                          Healing Workshop
                      </h2>
                      {/* Gradient Fill Layer */}
                      <h2 className="relative font-['Fredoka'] text-[60px] md:text-[90px] font-black text-transparent bg-clip-text bg-gradient-to-b from-[#5AB4E5] to-[#1A5E8A] leading-none z-10">
                          Healing Workshop
                      </h2>
                  </div>`;
code = code.replace(oldTitle, newTitle);

// Subheading: Key Visual
const oldKeyVisual = `<h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#3A7FB5] mb-10 tracking-wide">
                      Key Visual
                  </h3>`;
const newKeyVisual = `<div className="relative inline-block mb-10">
                      <h3 className="absolute inset-0 font-['Fredoka'] text-3xl md:text-4xl font-black tracking-wide" style={{ WebkitTextStroke: '6px #FDEECA', color: '#FDEECA' }} aria-hidden="true">
                          Key Visual
                      </h3>
                      <h3 className="relative font-['Fredoka'] text-3xl md:text-4xl font-black tracking-wide text-transparent bg-clip-text bg-gradient-to-b from-[#5AB4E5] to-[#1A5E8A] z-10">
                          Key Visual
                      </h3>
                  </div>`;
code = code.replace(oldKeyVisual, newKeyVisual);

// Subheading: Print & Event Applications
const oldPrintApps = `<h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#3A7FB5] mb-10 tracking-wide text-center">
                      Print &amp; Event Applications
                  </h3>`;
const newPrintApps = `<div className="relative inline-block mb-10 text-center w-full flex justify-center">
                      <div className="relative inline-block">
                          <h3 className="absolute inset-0 font-['Fredoka'] text-3xl md:text-4xl font-black tracking-wide" style={{ WebkitTextStroke: '6px #FDEECA', color: '#FDEECA' }} aria-hidden="true">
                              Print &amp; Event Applications
                          </h3>
                          <h3 className="relative font-['Fredoka'] text-3xl md:text-4xl font-black tracking-wide text-transparent bg-clip-text bg-gradient-to-b from-[#5AB4E5] to-[#1A5E8A] z-10">
                              Print &amp; Event Applications
                          </h3>
                      </div>
                  </div>`;
code = code.replace(oldPrintApps, newPrintApps);

// Subheading: Social Media Posts
const oldSocial = `<h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-[#3A7FB5] mb-10 tracking-wide text-center">
                      Social Media Posts
                  </h3>`;
const newSocial = `<div className="relative inline-block mb-10 text-center w-full flex justify-center">
                      <div className="relative inline-block">
                          <h3 className="absolute inset-0 font-['Fredoka'] text-3xl md:text-4xl font-black tracking-wide" style={{ WebkitTextStroke: '6px #FDEECA', color: '#FDEECA' }} aria-hidden="true">
                              Social Media Posts
                          </h3>
                          <h3 className="relative font-['Fredoka'] text-3xl md:text-4xl font-black tracking-wide text-transparent bg-clip-text bg-gradient-to-b from-[#5AB4E5] to-[#1A5E8A] z-10">
                              Social Media Posts
                          </h3>
                      </div>
                  </div>`;
code = code.replace(oldSocial, newSocial);

fs.writeFileSync(file, code);
