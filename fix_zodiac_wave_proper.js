const fs = require('fs');
const file = 'src/app/page.tsx';
let code = fs.readFileSync(file, 'utf8');

// Remove from ABOUT ME section (line 570ish)
const mistakenWave = `           {/* Wavy Divider Transition to Paintaso */}
           <div className="absolute bottom-0 left-0 w-full overflow-hidden leading-[0] z-0">
               <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320" className="w-full h-16 sm:h-24 md:h-32 block" preserveAspectRatio="none">
                   <path fill="#EEF8FF" fillOpacity="1" d="M0,224L48,213.3C96,203,192,181,288,186.7C384,192,480,224,576,213.3C672,203,768,149,864,138.7C960,128,1056,160,1152,176C1248,192,1344,192,1392,192L1440,192L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path>
               </svg>
           </div>
`;
code = code.replace(mistakenWave, '');

// Now add it to Zodiac
const zodiacEndAnchor = `                                      </div>
                                  )}
                              </div>
                          </div>
                      );
                  })}
              </div>
           </div>
        </section>

        {/* ─── 08. PAINTASO ─── */}`;

const newZodiacEnd = `                                      </div>
                                  )}
                              </div>
                          </div>
                      );
                  })}
              </div>
           </div>
           
           {/* Wavy Divider Transition to Paintaso */}
           <div className="absolute bottom-0 left-0 w-full overflow-hidden leading-[0] z-0">
               <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320" className="w-full h-16 sm:h-24 md:h-32 block" preserveAspectRatio="none">
                   <path fill="#EEF8FF" fillOpacity="1" d="M0,224L48,213.3C96,203,192,181,288,186.7C384,192,480,224,576,213.3C672,203,768,149,864,138.7C960,128,1056,160,1152,176C1248,192,1344,192,1392,192L1440,192L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path>
               </svg>
           </div>
        </section>

        {/* ─── 08. PAINTASO ─── */}`;

code = code.replace(zodiacEndAnchor, newZodiacEnd);

fs.writeFileSync(file, code);
