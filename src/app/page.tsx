
"use client";
import React, { useState, useEffect, useRef } from 'react';

export default function Page() {
  const [mounted, setMounted] = useState(false);
  const [entered, setEntered] = useState(false);
  const [introVisible, setIntroVisible] = useState(true);
  useEffect(() => { if (entered) setTimeout(() => setIntroVisible(false), 1000); }, [entered]);

  const gen20CarouselRef = useRef<HTMLDivElement>(null);
  const [activeGen20Idx, setActiveGen20Idx] = useState(0);
  const [activeDebateIdx, setActiveDebateIdx] = useState(0);
  const [activeZodiacPage, setActiveZodiacPage] = useState(0);
  const [activePaintasoIdx, setActivePaintasoIdx] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setActiveGen20Idx(prev => (prev + 1) % 4);
    }, 4000);
    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    const interval = setInterval(() => {
      setActiveDebateIdx(prev => (prev + 1) % 10);
    }, 4000);
    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    const interval = setInterval(() => {
      setActivePaintasoIdx(prev => (prev + 1) % 5);
    }, 4000);
    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    if (gen20CarouselRef.current) {
      const container = gen20CarouselRef.current;
      const activeChild = container.children[activeGen20Idx] as HTMLElement;
      if (activeChild) {
        const scrollLeft = activeChild.offsetLeft - container.clientWidth / 2 + activeChild.clientWidth / 2;
        container.scrollTo({ left: scrollLeft, behavior: 'smooth' });
      }
    }
  }, [activeGen20Idx]);

  useEffect(() => { setMounted(true); }, []);
  useEffect(() => {
    if (mounted) {
      if (!entered) {
        document.body.style.overflow = 'hidden';
      } else {
        document.body.style.overflow = '';
      }
    }
  }, [entered, mounted]);
  if (!mounted) return null;
























  return (
    <main className="w-full text-[#333] relative overflow-x-hidden bg-[#FDFCEE]">
      {/* ─── FLOATING NAVIGATION ─── */}
      <div className="fixed top-6 right-6 md:top-8 md:right-10 z-[110] flex flex-row gap-4">
         <a href="#home" className="group flex items-center justify-center px-6 py-2 bg-[#F9B658] border-[4px] border-white rounded-[20px] shadow-[4px_4px_0px_rgba(201,129,51,0.5)] hover:shadow-[4px_6px_0px_rgba(201,129,51,0.7)] hover:-translate-y-[2px] transition-all duration-300">
            <span className="font-['Fredoka'] font-bold text-white text-[17px] tracking-widest uppercase drop-shadow-sm">Home</span>
         </a>
         <a href="#toc" className="group flex items-center justify-center px-6 py-2 bg-[#89B66B] border-[4px] border-white rounded-[20px] shadow-[4px_4px_0px_rgba(108,133,88,0.5)] hover:shadow-[4px_6px_0px_rgba(108,133,88,0.7)] hover:-translate-y-[2px] transition-all duration-300">
            <span className="font-['Fredoka'] font-bold text-white text-[17px] tracking-widest uppercase drop-shadow-sm">TOC</span>
         </a>
      </div>

      
      {/* ─── INTERACTIVE INTRO ─── */}
      {introVisible && (
        <div className={`fixed inset-0 z-[100] bg-[#FDFCEE] flex flex-col items-center justify-center transition-transform duration-1000 ease-[cubic-bezier(0.76,0,0.24,1)] ${entered ? '-translate-y-full' : 'translate-y-0'}`}>
         <div className="absolute left-[-10%] top-[20%] w-[50%] h-[60%] bg-halftone-large opacity-10 z-0 animate-pulse" style={{clipPath: 'circle(50% at 30% 50%)'}}></div>
         <div className="absolute right-[-10%] bottom-[10%] w-[40%] h-[50%] bg-halftone-large opacity-10 z-0 animate-pulse" style={{clipPath: 'circle(50% at 70% 50%)'}}></div>
         
         <svg width="60" height="60" viewBox="0 0 100 100" className="absolute top-[20%] right-[20%] animate-float drop-shadow-sm rotate-[15deg]">
            <g stroke="#FCE8AC" strokeWidth="12" strokeLinecap="round">
              <line x1="50" y1="10" x2="50" y2="90"/>
              <line x1="15" y1="30" x2="85" y2="70"/>
              <line x1="15" y1="70" x2="85" y2="30"/>
            </g>
         </svg>
         
         <div className="relative z-10 flex flex-col items-center">
            <h1 className="text-[80px] sm:text-[100px] md:text-[120px] mb-8 text-center leading-[1.1] rotate-[-2deg] font-['Fredoka'] font-black text-stroke-white-shadow-orange animate-[fade-in-up_0.8s_ease-out_forwards] cursor-default hover:scale-105 hover:rotate-2 transition-transform duration-500 opacity-0">
               Welcome to<br/>My Scrapbook
            </h1>
            
            <div className="relative p-6 mt-4 group cursor-pointer animate-[fade-in-up_0.8s_ease-out_0.3s_forwards] opacity-0" onClick={() => setEntered(true)}>
              <div className="absolute inset-6 bg-[#F3A765] rounded-[2rem] transition-all duration-500 ease-out group-hover:translate-y-3 group-hover:translate-x-3 group-hover:rotate-2"></div>
              
              <div className="relative bg-[#89B66B] text-white font-['Fredoka'] font-bold text-3xl md:text-4xl px-12 md:px-16 py-5 md:py-6 rounded-[2rem] border-[6px] border-white transition-all duration-500 ease-out transform group-hover:-translate-y-2 group-hover:-translate-x-2 group-hover:scale-105 group-active:scale-95 group-hover:-rotate-2 flex items-center gap-3">
                 Open Portfolio
                 <svg width="32" height="32" viewBox="0 0 24 24" fill="#FFE885" className="animate-spin-slow">
                   <path d="M12 0 C12 10 22 12 22 12 C22 12 12 14 12 24 C12 14 2 12 2 12 C2 12 12 10 12 0 Z"/>
                 </svg>
              </div>
            </div>
         </div>
        </div>
      )}

      {/* Crossfade Cover - Fades out to reveal page, infinitely faster than fading the page in */}
      {introVisible && (
        <div className={`fixed inset-0 z-[90] bg-[#FAF4E1] transition-opacity duration-1000 ease-in-out pointer-events-none ${entered ? 'opacity-0' : 'opacity-100'}`}></div>
      )}

      <div className="">
        
        {/* ─── HERO SECTION ─── */}
        <section id="home" className="relative w-full min-h-screen flex flex-col items-center justify-center pt-24 pb-32 z-10 bg-[#FAF4E1] overflow-hidden">
          
          <div className="absolute bottom-[-5%] left-[-5%] w-[50%] h-[70%] bg-halftone-large opacity-[0.25] z-0" style={{clipPath: 'circle(50% at 20% 80%)'}}></div>
          <div className="absolute top-[-5%] right-[-5%] w-[50%] h-[60%] bg-halftone-large opacity-[0.25] z-0" style={{clipPath: 'circle(50% at 80% 20%)'}}></div>

          <div className="relative z-30 inline-flex flex-col items-center mt-12 group/folder transform -rotate-[8deg] skew-x-[-2deg]">
             
             {/* Back folder */}
             <div className={`absolute inset-0 bg-gradient-to-b from-[#F6B578] to-[#F1934B] rounded-[24px] md:rounded-[30px] border-[6px] border-white translate-x-6 md:translate-x-8 -translate-y-6 md:-translate-y-8 group-hover/folder:translate-x-12 group-hover/folder:-translate-y-12 group-hover/folder:rotate-[2deg] transition-transform duration-700 ease-[cubic-bezier(0.34,1.56,0.64,1)] opacity-0 ${entered ? 'animate-layer-up delay-100' : ''}`}>
                 <div className="absolute inset-0 rounded-[20px] overflow-hidden pointer-events-none">
                     </div>
                 
                 <div className="absolute -top-[45px] left-[-2px] w-[45%] h-[50px] flex z-10">
                     <div className="w-[80%] bg-[#F6B578] border-[6px] border-white border-b-0 border-r-0 rounded-tl-[24px]"></div>
                     <div className="flex-1 bg-[#F6B578] border-[6px] border-white border-b-0 border-l-0 origin-bottom-left skew-x-[35deg] rounded-tr-[16px] -ml-[6px]"></div>
                 </div>
             </div>

             {/* 
                Front folder 
                FIX: Increased padding-top/bottom to py-20 md:py-32.
                This makes the folder taller, giving horizontal elements MUCH more room to spread vertically.
             */}
             <div className={`relative bg-[#FFF0CA] rounded-[24px] md:rounded-[30px] border-[6px] md:border-[8px] border-white shadow-[0_15px_40px_rgba(0,0,0,0.06)] px-16 md:px-32 py-20 md:py-32 flex items-center justify-center transition-all duration-700 ease-[cubic-bezier(0.34,1.56,0.64,1)] group-hover/folder:-translate-y-2 group-hover/folder:shadow-[0_25px_50px_rgba(0,0,0,0.1)] opacity-0 ${entered ? 'animate-layer-up delay-300' : ''}`}>
                
                <div className="absolute inset-0 rounded-[18px] md:rounded-[24px] overflow-hidden pointer-events-none">
                   <div className="absolute inset-0 opacity-[0.03] mix-blend-multiply" style={{ backgroundImage: 'radial-gradient(#000 1.5px, transparent 1.5px)', backgroundSize: '12px 12px' }}></div>
                   </div>

                {/* Ribbon and Green Tab (2025) */}
                <div className={`absolute -top-[70px] left-[12%] z-20 flex flex-col items-center drop-shadow-md group/tab cursor-pointer opacity-0 ${entered ? 'animate-layer-up delay-500' : ''}`}>
                   <div className="absolute top-[40px] w-[50px] md:w-[60px] h-[100px] bg-[#E8704A] -z-10 transition-transform duration-500 group-hover/tab:scale-y-110 origin-top rotate-[5deg]" style={{clipPath: 'polygon(0 0, 100% 0, 100% 100%, 50% 80%, 0 100%)'}}>
                      </div>
                   <div className="relative w-[120px] md:w-[130px] h-[55px] md:h-[60px] transition-transform duration-500 group-hover/tab:-translate-y-2 flex items-center justify-center">
                      <svg width="100%" height="100%" viewBox="0 0 130 60" preserveAspectRatio="none" className="absolute inset-0">
                         <path d="M 12 5 L 118 5 L 130 60 L 0 60 Z" fill="#89B66B" stroke="white" strokeWidth="6" strokeLinejoin="round"/>
                      </svg>
                      <span className="relative z-10 font-['Fredoka'] text-white text-3xl font-black mt-1">2026</span>
                   </div>
                </div>

                {/* Grouped Text + Name Tag */}
                <div className={`opacity-0 ${entered ? 'animate-sticker-pop delay-600' : ''} relative z-30 transform rotate-[5deg] -translate-y-3 md:-translate-y-4`}>
                   
                   <h1 className="text-[60px] sm:text-[150px] md:text-[160px] font-['Fredoka'] font-black leading-none text-center text-3d-portfolio transition-all duration-500 group-hover/folder:text-3d-portfolio-hover group-hover/folder:scale-[1.02]" style={{ letterSpacing: '-0.02em' }}>
                      Portfolio
                   </h1>
                   
                   {/* 
                      FIX: Pushed down aggressively to -bottom-[85px]. 
                      Now completely detached from the text green body AND clearly below the shadow loops.
                   */}
                   <div className="absolute -bottom-[65px] md:-bottom-[85px] right-[5%] z-40">
                      <div className="relative bg-gradient-to-r from-[#F1934B] to-[#E8704A] text-white font-['Fredoka'] font-bold px-8 md:px-10 py-2 md:py-3 rounded-[12px] shadow-[3px_3px_0px_rgba(0,0,0,0.05)] text-lg md:text-xl border-[4px] border-white transform transition-transform duration-300 hover:scale-110 cursor-pointer">
                         <div className="absolute inset-0 rounded-[8px] overflow-hidden pointer-events-none">
                            </div>
                         <span className="relative z-10">Huyen Dao</span>
                      </div>
                   </div>
                </div>

                {/* ─── STICKERS (FIX: SPREAD OUT AND SCALED APPROPRIATELY) ─── */}
                
                {/* 1. Yellow Asterisk - Pushed out further left */}
                <div className={`absolute -left-[70px] md:-left-[100px] top-[15%] z-20 opacity-0 ${entered ? 'animate-sticker-pop delay-800' : ''} scale-65 md:scale-100`}>
                   <div className="animate-float-delayed hover:scale-125 transition-transform duration-500 cursor-pointer">
                      <svg width="100" height="100" viewBox="0 0 100 100" className="drop-shadow-md">
                        <g fill="none" stroke="#F9DB82" strokeWidth="18" strokeLinecap="round" strokeLinejoin="round">
                           <path d="M 50 15 L 50 85" />
                           <path d="M 20 35 L 80 65" />
                           <path d="M 20 65 L 80 35" />
                        </g>
                      </svg>
                   </div>
                </div>

                {/* 2. Orange Cursor Arrow - Pushed down and left */}
                <div className={`absolute -left-[50px] md:-left-[70px] bottom-[10%] z-20 opacity-0 ${entered ? 'animate-sticker-pop delay-1200' : ''} scale-65 md:scale-100`}>
                   <div className="animate-float rotate-[-15deg] cursor-pointer hover:rotate-0 transition-transform">
                      <svg width="85" height="85" viewBox="0 0 100 100" className="drop-shadow-md">
                        <path d="M 25 15 L 25 80 L 45 60 L 65 90 L 80 80 L 60 50 L 90 50 Z" fill="#F3A765" stroke="white" strokeWidth="6" strokeLinejoin="round"/>
                      </svg>
                   </div>
                </div>

                {/* 3. Clover Stamp - Pushed down to clear Portfolio text */}
                <div className={`absolute left-[30%] md:left-[35%] -bottom-[80px] md:-bottom-[100px] rotate-[-5deg] z-40 opacity-0 ${entered ? 'animate-sticker-pop delay-1200' : ''} scale-65 md:scale-100`}>
                   <div className="relative w-[110px] h-[130px] md:w-[130px] md:h-[150px] flex items-center justify-center animate-float hover:scale-110 transition-transform cursor-pointer">
                      <div className="absolute inset-0 bg-white stamp-mask shadow-[0_10px_20px_rgba(0,0,0,0.1)]"></div>
                      <div className="absolute inset-[10px] border-[1.5px] border-[#EEE] z-10 pointer-events-none rounded-[4px]"></div>

                      <svg className="absolute -top-3 -left-3 z-50 drop-shadow-sm" width="50" height="50" viewBox="0 0 100 100">
                         <path d="M50 50 C20 10 0 40 50 50 C80 10 100 40 50 50" fill="none" stroke="#E8704A" strokeWidth="6" strokeLinecap="round"/>
                         <path d="M50 50 L25 85 M50 50 L75 85" stroke="#E8704A" strokeWidth="6" strokeLinecap="round"/>
                         <circle cx="50" cy="50" r="5" fill="#E8704A"/>
                      </svg>
                         
                      <svg width="90" height="90" viewBox="0 0 100 100" className="relative z-20 drop-shadow-sm ml-2 mt-2">
                         <g fill="#89B66B">
                           <circle cx="35" cy="35" r="16"/>
                           <circle cx="65" cy="35" r="16"/>
                           <circle cx="35" cy="65" r="16"/>
                           <circle cx="65" cy="65" r="16"/>
                           <rect x="35" y="35" width="30" height="30" />
                         </g>
                         <circle cx="40" cy="48" r="4" fill="white"/>
                         <circle cx="60" cy="48" r="4" fill="white"/>
                         <path d="M44 56 Q50 62 56 56" fill="none" stroke="white" strokeWidth="4" strokeLinecap="round"/>
                      </svg>
                   </div>
                </div>

                {/* 4. Ai Puffy Star - Far Top Right */}
                <div className={`absolute -right-[40px] md:-right-[60px] -top-[40px] md:-top-[60px] rotate-[15deg] z-40 opacity-0 ${entered ? 'animate-sticker-pop delay-800' : ''} scale-65 md:scale-100`}>
                   <div className="animate-float hover:scale-110 transition-transform cursor-pointer">
                      <svg width="100" height="100" viewBox="0 0 100 100" className="drop-shadow-md">
                         <polygon points="50,15 61,38 86,41 68,58 74,84 50,70 26,84 32,58 14,41 39,38" fill="#F1934B" stroke="white" strokeWidth="8" strokeLinejoin="round"/>
                         <text x="50" y="55" fontFamily="'Fredoka', sans-serif" fontSize="34" fill="white" fontWeight="900" textAnchor="middle" dominantBaseline="middle">Ai</text>
                      </svg>
                   </div>
                </div>

                {/* 5. Leaf Blob - Spread to top 15% */}
                <div className={`absolute -right-[60px] md:-right-[100px] top-[15%] rotate-[15deg] z-20 opacity-0 ${entered ? 'animate-sticker-pop delay-900' : ''} scale-65 md:scale-100`}>
                   <div className="animate-float-delayed hover:scale-110 transition-transform cursor-pointer">
                      <svg width="85" height="85" viewBox="0 0 100 100" className="drop-shadow-md">
                         <polygon points="50,10 65,30 90,30 75,50 85,75 50,65 15,75 25,50 10,30 35,30" fill="#B5D799" stroke="white" strokeWidth="6" strokeLinejoin="round"/>
                         <path d="M 30 70 C 20 45, 45 30, 70 30 C 50 25, 25 50, 30 70 Z" fill="white" stroke="white" strokeWidth="2" strokeLinejoin="round"/>
                      </svg>
                   </div>
                </div>

                {/* 6. Figma Logo - Spread to top 42% */}
                <div className={`absolute -right-[50px] md:-right-[80px] top-[42%] rotate-[10deg] z-30 opacity-0 ${entered ? 'animate-sticker-pop delay-1000' : ''} scale-65 md:scale-100`}>
                   <div className="animate-float hover:scale-110 transition-transform cursor-pointer">
                      <svg width="85" height="85" viewBox="0 0 100 100" className="drop-shadow-md">
                         <rect x="15" y="15" width="70" height="70" rx="16" fill="#CDE7BC" stroke="white" strokeWidth="6"/>
                         <g transform="translate(50, 50) scale(1.1) translate(-50, -50)">
                            <circle cx="42" cy="34" r="7" fill="none" stroke="#89B66B" strokeWidth="3"/>
                            <circle cx="58" cy="34" r="7" fill="none" stroke="#89B66B" strokeWidth="3"/>
                            <circle cx="42" cy="50" r="7" fill="none" stroke="#89B66B" strokeWidth="3"/>
                            <circle cx="58" cy="50" r="7" fill="none" stroke="#89B66B" strokeWidth="3"/>
                            <path d="M 42 66 C 42 56, 50 56, 50 66 C 50 76, 42 76, 42 66 Z" fill="none" stroke="#89B66B" strokeWidth="3"/>
                         </g>
                      </svg>
                   </div>
                </div>

                {/* 7. Blender Logo - Spread to top 70% */}
                <div className={`absolute -right-[40px] md:-right-[90px] top-[70%] rotate-[5deg] z-20 opacity-0 ${entered ? 'animate-sticker-pop delay-1100' : ''} scale-65 md:scale-100`}>
                   <div className="animate-float-delayed hover:scale-110 transition-transform cursor-pointer">
                      <svg width="90" height="90" viewBox="0 0 100 100" className="drop-shadow-md">
                         <path d="M50,15 C60,15 65,30 75,35 C90,40 95,50 90,65 C85,75 75,85 60,85 C50,85 35,85 25,75 C15,65 15,50 25,35 C35,30 40,15 50,15 Z" fill="#F1934B" stroke="white" strokeWidth="6" strokeLinejoin="round"/>
                         <circle cx="48" cy="50" r="10" fill="none" stroke="white" strokeWidth="4"/>
                         <path d="M 48 40 Q 65 25 75 30" fill="none" stroke="white" strokeWidth="4" strokeLinecap="round"/>
                         <path d="M 38 43 L 28 32" fill="none" stroke="white" strokeWidth="4" strokeLinecap="round"/>
                      </svg>
                   </div>
                </div>

                {/* 8. Ps Sticker - Pushed far bottom right */}
                <div className={`absolute right-[-5px] md:right-[-25px] -bottom-[40px] md:-bottom-[50px] rotate-[-15deg] z-40 opacity-0 ${entered ? 'animate-sticker-pop delay-1200' : ''} scale-65 md:scale-100`}>
                   <div className="animate-float hover:scale-110 transition-transform cursor-pointer">
                      <svg width="90" height="90" viewBox="0 0 100 100" className="drop-shadow-md">
                         <circle cx="50" cy="50" r="40" fill="#89B66B" stroke="white" strokeWidth="6"/>
                         <text x="50" y="55" fontFamily="'Fredoka', sans-serif" fontSize="36" fill="white" fontWeight="900" textAnchor="middle" dominantBaseline="middle">Ps</text>
                      </svg>
                   </div>
                </div>
                
             </div>
          </div>
        </section>
                                                                                        {/* ─── ABOUT ME ─── */}
        <section className="relative w-full py-24 bg-[#FDFCEE] overflow-hidden">
           <div className="absolute inset-0 bg-halftone-large opacity-10 pointer-events-none z-0"></div>

           <div className="max-w-[1400px] mx-auto px-6 relative z-20 flex flex-col lg:flex-row gap-12 items-stretch justify-center">
              
              {/* LEFT COLUMN: GREEN PAPER */}
              <div className="w-full lg:w-[35%] bg-[#CBE0A3] py-16 pr-8 pl-12 rounded-[24px] border-[8px] border-white shadow-[12px_12px_0px_rgba(154,181,116,0.6)] relative rotate-[-1deg] flex flex-col gap-16">
                 {/* Education Tab */}
                 <div className="relative">
                     <div className="absolute -left-[70px] -top-6 bg-[#537A38] text-white font-['Fredoka'] font-black text-4xl px-8 py-3 rotate-[-2deg] border-[6px] border-white z-10" style={{ textShadow: '-2px -2px 0 #3A5723, 2px -2px 0 #3A5723, -2px 2px 0 #3A5723, 2px 2px 0 #3A5723, 4px 4px 0px rgba(0,0,0,0.2)' }}>
                        Education
                     </div>
                     <div className="relative z-10 text-[#3A5723] pt-16">
                        <div className="mb-6">
                           <p className="font-['Quicksand'] font-bold text-lg mb-1 opacity-80">Sep 2024 – Present</p>
                           <h4 className="font-['Fredoka'] font-black text-2xl mb-1 text-[#466B29] leading-tight" style={{ textShadow: '1px 1px 0px white' }}>Foreign Trade University</h4>
                           <p className="font-['Quicksand'] font-bold text-md">Bachelor of International Business</p>
                        </div>
                        <div>
                           <p className="font-['Quicksand'] font-bold text-lg mb-1 opacity-80">Sep 2021 – Jun 2024</p>
                           <h4 className="font-['Fredoka'] font-black text-2xl mb-1 text-[#466B29] leading-tight" style={{ textShadow: '1px 1px 0px white' }}>Tran Phu Gifted High School</h4>
                           <p className="font-['Quicksand'] font-bold text-md">Physics Honors Class</p>
                        </div>
                     </div>
                 </div>

                 {/* Achievement Tab */}
                 <div className="relative">
                     <div className="absolute -left-[70px] -top-6 bg-[#7AA65B] text-white font-['Fredoka'] font-black text-4xl px-8 py-3 rotate-[1deg] border-[6px] border-white z-10" style={{ textShadow: '-2px -2px 0 #466B29, 2px -2px 0 #466B29, -2px 2px 0 #466B29, 2px 2px 0 #466B29, 4px 4px 0px rgba(0,0,0,0.2)' }}>
                        Achievement
                     </div>
                     <div className="relative z-10 text-[#3A5723] font-['Quicksand'] font-bold text-md space-y-6 pt-16">
                        <div>
                           <h4 className="font-['Fredoka'] font-black text-xl text-[#466B29] leading-tight" style={{ textShadow: '1px 1px 0px white' }}>Google Digital Marketing Cert</h4>
                           <p className="opacity-80">Oct 2023</p>
                        </div>
                        <div>
                           <h4 className="font-['Fredoka'] font-black text-xl text-[#466B29] leading-tight" style={{ textShadow: '1px 1px 0px white' }}>City-Level Physics Excellence</h4>
                           <p className="opacity-80">Second Prize (Sep 2022)</p>
                        </div>
                        <div>
                           <h4 className="font-['Fredoka'] font-black text-xl text-[#466B29] leading-tight" style={{ textShadow: '1px 1px 0px white' }}>Hai Phong Youth Innovation</h4>
                           <p className="opacity-80">Consolation Prize (Jul 2021)</p>
                        </div>
                     </div>
                 </div>

                 {/* Skills Tab */}
                 <div className="relative">
                     <div className="absolute -left-[70px] -top-6 bg-[#6CA35C] text-white font-['Fredoka'] font-black text-4xl px-8 py-3 rotate-[-1deg] border-[6px] border-white z-10" style={{ textShadow: '-2px -2px 0 #3A5723, 2px -2px 0 #3A5723, -2px 2px 0 #3A5723, 2px 2px 0 #3A5723, 4px 4px 0px rgba(0,0,0,0.2)' }}>
                        Skills
                     </div>
                     <div className="relative z-10 text-[#3A5723] pt-16">
                        <div className="mb-4">
                           <p className="font-['Fredoka'] text-[#466B29] text-xl mb-2 font-black">Hard Skills</p>
                           <ul className="list-disc ml-6 font-['Quicksand'] font-bold text-md space-y-2 opacity-90">
                              <li>Product & UI/UX Design</li>
                              <li>Traditional & Digital Illustration</li>
                              <li>Content Creation & Public Relations</li>
                              
                           </ul>
                        </div>
                        <div>
                           <p className="font-['Fredoka'] text-[#466B29] text-xl mb-2 font-black">Soft Skills</p>
                           <ul className="list-disc ml-6 font-['Quicksand'] font-bold text-md space-y-2 opacity-90">
                              <li>Planning & Time Management</li>
                              <li>Communication & Presenting Ideas</li>
                              <li>Working Independently & in Groups</li>
                           </ul>
                        </div>
                     </div>
                 </div>

                 {/* Softwares Tab */}
                 <div className="relative">
                     <div className="absolute -left-[70px] -top-6 bg-[#487334] text-white font-['Fredoka'] font-black text-4xl px-8 py-3 rotate-[2deg] border-[6px] border-white z-10" style={{ textShadow: '-2px -2px 0 #2D4A20, 2px -2px 0 #2D4A20, -2px 2px 0 #2D4A20, 2px 2px 0 #2D4A20, 4px 4px 0px rgba(0,0,0,0.2)' }}>
                        Softwares
                     </div>
                     <div className="relative z-10 text-[#3A5723] pt-16">
                        
                        {/* Software Stickers replacing plain text */}
                        <div className="flex flex-wrap gap-4 mt-2">
                            {/* Figma Sticker */}
                            <div className="bg-[#2C2D33] text-white font-['Fredoka'] font-black text-lg px-4 py-2 rounded-[16px] border-[4px] border-white shadow-[4px_4px_0px_rgba(0,0,0,0.15)] rotate-[-3deg] flex items-center gap-2">
                                <svg width="18" height="26" viewBox="0 0 38 57" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M19 28.5C13.7533 28.5 9.5 24.2467 9.5 19C9.5 13.7533 13.7533 9.5 19 9.5L28.5 9.5V28.5L19 28.5Z" fill="#F24E1E"/>
                                    <path d="M19 47.5C13.7533 47.5 9.5 43.2467 9.5 38C9.5 32.7533 13.7533 28.5 19 28.5L28.5 28.5V47.5L19 47.5Z" fill="#A259FF"/>
                                    <path d="M19 28.5L28.5 28.5V9.5L19 9.5C13.7533 9.5 9.5 13.7533 9.5 19C9.5 24.2467 13.7533 28.5 19 28.5Z" fill="#F24E1E"/>
                                    <path d="M28.5 28.5C33.7467 28.5 38 24.2467 38 19C38 13.7533 33.7467 9.5 28.5 9.5L19 9.5V28.5L28.5 28.5Z" fill="#FF7262"/>
                                    <path d="M19 47.5L28.5 47.5V28.5L19 28.5C13.7533 28.5 9.5 32.7533 9.5 38C9.5 43.2467 13.7533 47.5 19 47.5Z" fill="#A259FF"/>
                                    <path d="M28.5 47.5C33.7467 47.5 38 43.2467 38 38C38 32.7533 33.7467 28.5 28.5 28.5L19 28.5V47.5L28.5 47.5Z" fill="#1ABCFE"/>
                                    <path d="M19 57C13.7533 57 9.5 52.7467 9.5 47.5C9.5 42.2533 13.7533 38 19 38L28.5 38L28.5 47.5C28.5 52.7467 24.2467 57 19 57Z" fill="#0ACF83"/>
                                </svg>
                                Figma
                            </div>
                            
                            {/* Photoshop Sticker */}
                            <div className="bg-[#31A8FF] text-[#001E36] font-['Fredoka'] font-black text-2xl px-3 py-1 rounded-[12px] border-[4px] border-white shadow-[4px_4px_0px_rgba(0,0,0,0.15)] rotate-[4deg]">
                                Ps
                            </div>
                            
                            {/* Illustrator Sticker */}
                            <div className="bg-[#FF9A00] text-[#330000] font-['Fredoka'] font-black text-2xl px-3 py-1 rounded-[12px] border-[4px] border-white shadow-[4px_4px_0px_rgba(0,0,0,0.15)] rotate-[-2deg]">
                                Ai
                            </div>

                            {/* Canva Sticker */}
                            <div className="bg-gradient-to-br from-[#00C4CC] to-[#7D2AE8] text-white font-['Fredoka'] font-black text-lg px-4 py-2 rounded-[16px] border-[4px] border-white shadow-[4px_4px_0px_rgba(0,0,0,0.15)] rotate-[3deg]">
                                Canva
                            </div>
                            
                            {/* CapCut Sticker */}
                            <div className="bg-black text-white font-['Fredoka'] font-black text-lg px-4 py-2 rounded-[16px] border-[4px] border-white shadow-[4px_4px_0px_rgba(0,0,0,0.15)] rotate-[-4deg]">
                                CapCut
                            </div>

                            {/* MS Office Sticker */}
                            <div className="bg-[#0072C6] text-white font-['Fredoka'] font-black text-lg px-4 py-2 rounded-[16px] border-[4px] border-white shadow-[4px_4px_0px_rgba(0,0,0,0.15)] rotate-[2deg]">
                                MS Office
                            </div>
                        </div>

                     </div>
                 </div>

              </div>

              {/* RIGHT COLUMN: INFO CARD & EXPERIENCE */}
              <div className="w-full lg:w-[65%] flex flex-col gap-12">
                 
                 {/* TOP CARD: INFO */}
                 <div id="profile" className="bg-[#FDF9E7] p-10 md:p-12 rounded-[40px] border-[8px] border-white shadow-[12px_12px_0px_rgba(209,205,188,0.5)] relative rotate-[1deg] flex flex-col xl:flex-row gap-12 items-center xl:items-start scroll-mt-24">
                    {/* Polaroid Avatar Frame */}
                    <div className="relative shrink-0 rotate-[-3deg] z-20">
                       <div className="bg-white p-4 pb-12 rounded-[16px] shadow-[8px_8px_0px_rgba(0,0,0,0.1)] border-[4px] border-white/50 w-[240px]">
                           <div className="relative w-full aspect-[3/4] overflow-hidden rounded-[8px]">
                               <img src="/assets/huyen-dao-avatar-2.jpg" className="absolute max-w-none" style={{ width: '270%', height: 'auto', left: '-52%', top: '-75%' }} alt="Avatar" />
                           </div>
                       </div>
                       <div className="absolute -top-4 left-1/2 -translate-x-1/2 w-[100px] h-[35px] bg-white/60 backdrop-blur-md border border-white/80 rotate-[4deg] shadow-sm z-30 rounded-sm"></div>
                    </div>

                    {/* Info Text */}
                    <div className="relative z-10 flex-1 w-full pt-2">
                       <h2 className="font-['Fredoka'] font-black text-[42px] md:text-[52px] text-[#86573C] mb-6 leading-[1.1]" style={{textShadow: '-3px -3px 0 #FFF, 3px -3px 0 #FFF, -3px 3px 0 #FFF, 3px 3px 0 #FFF, 5px 5px 0px rgba(0,0,0,0.1)'}}>
                          Dao Hoang Khanh Huyen
                       </h2>
                       
                       <div className="font-['Quicksand'] font-bold text-[#6D452F] text-lg space-y-3 mb-6 border-b-[3px] border-dashed border-[#C9C5B4] pb-6">
                          <div className="flex flex-wrap gap-x-8 gap-y-3">
                             <p><span className="opacity-70">Gender:</span> Female</p>
                             <p><span className="opacity-70">Date of birth:</span> 2006</p>
                          </div>
                          <p><span className="opacity-70">Nationality:</span> Vietnamese</p>
                          <p><span className="opacity-70">Role:</span> Product Design Intern</p>
                          
                          <div className="w-full h-[2px] bg-[#86573C]/20 my-4"></div>
                          
                          <p><span className="opacity-70">Contact:</span> 0942 451 288</p>
                          <p><span className="opacity-70">Email:</span> daohuyen2655@gmail.com</p>
                       </div>
                       
                       <p className="font-['Quicksand'] text-[#553523] font-semibold text-lg leading-relaxed mb-8">
                          A product designer with a passion for user experience, creative problem-solving, and visual communication. Eager to build hands-on experience in product strategy and engaging UI/UX design.
                       </p>
                       
                       <div className="flex justify-start">
                           <a href="https://www.linkedin.com/in/huyen-dao-584a53297/" target="_blank" rel="noopener noreferrer" className="font-['Fredoka'] font-black text-2xl bg-[#EBA355] text-white px-8 py-3 rounded-full border-[6px] border-white shadow-[6px_6px_0px_#C98133] hover:translate-y-1 hover:shadow-[3px_3px_0px_#C98133] transition-all rotate-[-2deg]" style={{textShadow: '1px 1px 0px rgba(0,0,0,0.2)'}}>
                               My LinkedIn ➔
                           </a>
                       </div>
                    </div>
                 </div>

                 {/* BOTTOM CARD: EXPERIENCE (Orange Paper with Notebook Edge) */}
                 <div className="bg-[#F5D586] p-10 md:p-14 rounded-b-[24px] rounded-t-none border-b-[8px] border-l-[8px] border-r-[8px] border-white shadow-[12px_12px_0px_rgba(209,174,90,0.5)] relative rotate-[-1deg] w-full flex-1 min-h-[300px] mt-6">
                    <div className="absolute -top-[24px] left-[-8px] w-[calc(100%+16px)] h-[24px] overflow-hidden drop-shadow-[0_-4px_0_white] z-10">
                       <svg width="100%" height="24" preserveAspectRatio="none">
                          <defs>
                             <pattern id="teeth-exp" width="40" height="24" patternUnits="userSpaceOnUse">
                                <path d="M0,24 L0,6 C0,2 6,2 12,2 L28,2 C34,2 40,2 40,6 L40,24 Z" fill="#F5D586"/>
                             </pattern>
                          </defs>
                          <rect width="100%" height="24" fill="url(#teeth-exp)"/>
                       </svg>
                    </div>

                    <div className="absolute -top-12 -right-8 md:-right-12 z-30">
                       <div className="bg-[#FFF] text-[#86573C] font-['Fredoka'] font-black text-4xl md:text-5xl px-12 py-4 shadow-[8px_8px_0px_rgba(209,174,90,0.8)] rotate-[3deg] border-[8px] border-white whitespace-nowrap" style={{textShadow: '2px 2px 0px rgba(0,0,0,0.1)'}}>
                          Experience
                       </div>
                    </div>

                    <div className="relative z-20 space-y-10 mt-16 text-[#6D452F]">
                       
                       {/* Exp 1: EveryLab.ai */}
                       <div className="flex flex-col font-['Quicksand'] border-b-4 border-dashed border-[#DEBA64] pb-8">
                          <div className="flex flex-col md:flex-row justify-between items-start gap-2">
                             <div className="flex-1">
                                <h4 className="font-['Fredoka'] font-black text-3xl md:text-4xl text-[#D8683E] mb-2 leading-tight" style={{textShadow: '-2px -2px 0 #FFF, 2px -2px 0 #FFF, -2px 2px 0 #FFF, 2px 2px 0 #FFF, 4px 4px 0px rgba(0,0,0,0.1)'}}>EveryLab.ai</h4>
                                <p className="font-bold text-xl opacity-90 mb-1">Product Design Intern / Content Creator</p>
                             </div>
                             <span className="font-black text-xl shrink-0 text-[#86573C] opacity-80 md:text-right pt-2">Jan 2026 - Aug 2026</span>
                          </div>
                       </div>

                       {/* Exp 2: CC FTU */}
                       <div className="flex flex-col font-['Quicksand'] border-b-4 border-dashed border-[#DEBA64] pb-8">
                          <div className="flex flex-col md:flex-row justify-between items-start gap-2">
                             <div className="flex-1">
                                <h4 className="font-['Fredoka'] font-black text-3xl md:text-4xl text-[#D8683E] mb-2 leading-tight" style={{textShadow: '-2px -2px 0 #FFF, 2px -2px 0 #FFF, -2px 2px 0 #FFF, 2px 2px 0 #FFF, 4px 4px 0px rgba(0,0,0,0.1)'}}>CC FTU</h4>
                                <p className="font-bold text-xl opacity-90 mb-1">Head of Public Relations</p>
                             </div>
                             <span className="font-black text-xl shrink-0 text-[#86573C] opacity-80 md:text-right pt-2">Oct 2024 - Jul 2026</span>
                          </div>
                       </div>

                       {/* Exp 3: Paintaso Club */}
                       <div className="flex flex-col font-['Quicksand'] border-b-4 border-dashed border-[#DEBA64] pb-8">
                          <div className="flex flex-col md:flex-row justify-between items-start gap-2">
                             <div className="flex-1">
                                <h4 className="font-['Fredoka'] font-black text-3xl md:text-4xl text-[#D8683E] mb-2 leading-tight" style={{textShadow: '-2px -2px 0 #FFF, 2px -2px 0 #FFF, -2px 2px 0 #FFF, 2px 2px 0 #FFF, 4px 4px 0px rgba(0,0,0,0.1)'}}>Paintaso Club</h4>
                                <p className="font-bold text-xl opacity-90 mb-1">Co - Organizer</p>
                             </div>
                             <span className="font-black text-xl shrink-0 text-[#86573C] opacity-80 md:text-right pt-2">2023 - 2024</span>
                          </div>
                       </div>

                       {/* Exp 4: Bang Bang Magazine */}
                       <div className="flex flex-col font-['Quicksand'] border-b-4 border-dashed border-[#DEBA64] pb-8">
                          <div className="flex flex-col md:flex-row justify-between items-start gap-2">
                             <div className="flex-1">
                                <h4 className="font-['Fredoka'] font-black text-3xl md:text-4xl text-[#D8683E] mb-2 leading-tight" style={{textShadow: '-2px -2px 0 #FFF, 2px -2px 0 #FFF, -2px 2px 0 #FFF, 2px 2px 0 #FFF, 4px 4px 0px rgba(0,0,0,0.1)'}}>Bang Bang Magazine</h4>
                                <p className="font-bold text-xl opacity-90 mb-1">Head of Public Relations</p>
                             </div>
                             <span className="font-black text-xl shrink-0 text-[#86573C] opacity-80 md:text-right pt-2">2024</span>
                          </div>
                       </div>

                       {/* Exp 5: GYPP Vietnam & Others */}
                       <div className="flex flex-col font-['Quicksand'] pb-2">
                          <div className="flex flex-col md:flex-row justify-between items-start gap-2">
                             <div className="flex-1">
                                <h4 className="font-['Fredoka'] font-black text-3xl md:text-4xl text-[#D8683E] mb-2 leading-tight" style={{textShadow: '-2px -2px 0 #FFF, 2px -2px 0 #FFF, -2px 2px 0 #FFF, 2px 2px 0 #FFF, 4px 4px 0px rgba(0,0,0,0.1)'}}>Other Activities</h4>
                                <ul className="list-disc ml-5 font-bold text-lg opacity-90 space-y-1">
                                   <li><span className="opacity-80">GYPP Vietnam -</span> Media Ambassador</li>
                                   <li><span className="opacity-80">The Fallen Project -</span> Head of Public Relations</li>
                                   <li><span className="opacity-80">LOGIA Debate Club -</span> Member</li>
                                   <li><span className="opacity-80">The Kori Project -</span> Member</li>
                                </ul>
                             </div>
                             <span className="font-black text-xl shrink-0 text-[#86573C] opacity-80 md:text-right pt-2">2023 - 2024</span>
                          </div>
                       </div>

                    </div>
                 </div>

              </div>
           </div>
           
        </section>
{/* ─── TABLE OF CONTENTS ─── */}
        
        {/* SEAM MARQUEE (Between About Me and TOC) */}
        <div className="relative w-full overflow-hidden rotate-[-1.5deg] bg-[#F9B658] border-y-[4px] border-[#333] z-40 -mt-8 -mb-4 shadow-sm flex flex-col justify-center">
            <div className="animate-marquee-infinite flex whitespace-nowrap font-['Fredoka'] font-black text-2xl md:text-3xl text-[#222] py-2.5 w-max">
                <div className="shrink-0 flex items-center gap-8 px-4">
                    <span>PRODUCT DESIGN</span><span className="text-xl">✳</span>
                    <span>PRODUCT DESIGN</span><span className="text-xl">✳</span>
                    <span>PRODUCT DESIGN</span><span className="text-xl">✳</span>
                    <span>PRODUCT DESIGN</span><span className="text-xl">✳</span>
                    <span>PRODUCT DESIGN</span><span className="text-xl">✳</span>
                    <span>PRODUCT DESIGN</span><span className="text-xl">✳</span>
                    <span>PRODUCT DESIGN</span><span className="text-xl">✳</span>
                    <span>PRODUCT DESIGN</span><span className="text-xl">✳</span>
                    <span>PRODUCT DESIGN</span><span className="text-xl">✳</span>
                    <span>PRODUCT DESIGN</span><span className="text-xl">✳</span>
                </div>
                <div className="shrink-0 flex items-center gap-8 px-4">
                    <span>PRODUCT DESIGN</span><span className="text-xl">✳</span>
                    <span>PRODUCT DESIGN</span><span className="text-xl">✳</span>
                    <span>PRODUCT DESIGN</span><span className="text-xl">✳</span>
                    <span>PRODUCT DESIGN</span><span className="text-xl">✳</span>
                    <span>PRODUCT DESIGN</span><span className="text-xl">✳</span>
                    <span>PRODUCT DESIGN</span><span className="text-xl">✳</span>
                    <span>PRODUCT DESIGN</span><span className="text-xl">✳</span>
                    <span>PRODUCT DESIGN</span><span className="text-xl">✳</span>
                    <span>PRODUCT DESIGN</span><span className="text-xl">✳</span>
                    <span>PRODUCT DESIGN</span><span className="text-xl">✳</span>
                </div>
            </div>
        </div>

        
        {/* ─── TABLE OF CONTENTS ─── */}
        <section id="toc" className="relative w-full pb-12 bg-[#F6F4EB] overflow-hidden pt-32 md:pt-24">
           {/* Background Textures */}
           <div className="absolute inset-0 bg-halftone-large opacity-[0.03] pointer-events-none z-0"></div>
           
           <div className="max-w-[1200px] mx-auto px-6 relative z-20">
              
              <div className="flex flex-col items-center mb-24">
                 <div className="relative group">
                    <h2 className="text-[70px] md:text-[100px] font-['Fredoka'] font-black text-[#222] rotate-[-2deg] transition-transform duration-500 group-hover:scale-105" style={{ textShadow: '-4px -4px 0 #FFF, 4px -4px 0 #FFF, -4px 4px 0 #FFF, 4px 4px 0 #FFF, 8px 8px 0px rgba(34,34,34,0.15)' }}>
                       Table of Contents
                    </h2>
                 </div>
              </div>

              {/* Grid 4 Columns */}
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-10 w-full justify-items-center">
                 {[
                    { id: "01", title: "Yapsu AI", color: "#F1934B", anchor: "yapsu-ai" },
                    { id: "02", title: "Chinese Debate '26", color: "#4EC4E1", anchor: "chinese-debate-2026" },
                    { id: "03", title: "Gen 20th Recruit", color: "#89B66B", anchor: "gen-20-recruit" },
                    { id: "04", title: "19th Anniversary", color: "#A890D8", anchor: "19th-birthday" },
                    { id: "05", title: "Chinese Debate '25", color: "#D4AF37", anchor: "chinese-debate-25" },
                    { id: "06", title: "E-Com Talkshow", color: "#58B3D3", anchor: "talkshow" },
                    { id: "07", title: "Zodiac", color: "#2C3E50", anchor: "zodiac" },
                    { id: "08", title: "Paintaso", color: "#E53935", anchor: "paintaso" }
                 ].map((item, idx) => (
                    <a key={idx} href={`#${item.anchor}`} className="group relative w-full max-w-[280px] h-[180px] block">
                       {/* Shadow / Base layer - solid color matching banner */}
                       <div className="absolute inset-0 bg-[#F9B658] rounded-[28px] translate-y-2 translate-x-2 opacity-0 group-hover:opacity-100 group-hover:translate-y-3 group-hover:translate-x-3 transition-all duration-300 border-[3px] border-[#222]"></div>
                       
                       {/* Top Card layer */}
                       <div className="absolute inset-0 bg-white rounded-[28px] border-[3px] border-[#E8E6DD] group-hover:border-[#222] transition-colors duration-300 flex flex-col justify-between p-6 overflow-hidden z-10">
                          
                          {/* Number Watermark (Fixed position to avoid cut-off) */}
                          <div className="absolute right-4 bottom-2 text-[65px] font-['Fredoka'] font-black text-[#F0EFE6] group-hover:text-[#F9B658] transition-colors duration-300 z-0 leading-none">
                             {item.id}
                          </div>

                          {/* Top Accent Pill */}
                          <div className="w-10 h-2 bg-[#E8E6DD] group-hover:bg-[#222] rounded-full transition-colors duration-300 z-10"></div>
                          
                          {/* Title */}
                          <h3 className="font-['Fredoka'] font-bold text-2xl text-[#475569] group-hover:text-[#222] leading-tight z-10 w-[80%] relative">
                             {item.title}
                          </h3>
                       </div>
                    </a>
                 ))}
              </div>
           </div>
        </section>

        {/* ─── 01. YAPSU AI ─── */}
        <section id="yapsu-ai" className="relative w-full pt-12 pb-32 bg-gradient-to-b from-[#FCFBF9] via-[#FFF3E6] to-[#FFD8B5] text-[#334155] font-sans">
           
           {/* Transition from TOC (Beige) to Yapsu (Light) */}
           <div className="absolute top-0 left-0 w-full h-[100px] bg-gradient-to-b from-[#F6F4EB] to-[#FCFBF9] z-10 pointer-events-none"></div>
           
           <div className="max-w-[1600px] mx-auto px-4 sm:px-8 relative z-20 flex flex-col">
              
              {/* 1. PRODUCT BRIEF (HERO) */}
              <div className="flex flex-col lg:flex-row items-center justify-between mb-32 gap-16 w-full max-w-[1400px] mx-auto pt-10">
                 <div className="w-full lg:w-[45%] flex flex-col items-start pt-10">
                    <h2 className="font-['Fredoka'] text-[70px] md:text-[85px] font-bold leading-tight mb-6 text-transparent bg-clip-text bg-gradient-to-r from-orange-500 to-amber-400 drop-shadow-sm tracking-tight">
                       Yapsu AI
                    </h2>
                    
                    <div className="px-6 py-2 border border-orange-200 text-orange-500 rounded-full text-base font-semibold mb-8 bg-orange-50 uppercase tracking-widest shadow-sm">
                       Product Design
                    </div>
                    
                    <p className="text-xl text-[#475569] leading-relaxed font-normal mb-6 max-w-lg">
                       Yapsu AI is a modern language learning app designed for individuals seeking a natural way to practice conversations with friendly AI tutors.
                    </p>
                    
                    <div className="mb-12 max-w-lg p-5 bg-white border border-gray-100 rounded-2xl shadow-sm relative overflow-hidden">
                       <div className="absolute left-0 top-0 w-1.5 h-full bg-gradient-to-b from-orange-400 to-amber-300"></div>
                       <p className="text-sm md:text-base text-[#64748b] leading-relaxed font-medium italic">
                          "I am deeply grateful to <strong className="text-orange-500 font-bold">Everlab Technology Co., Ltd.</strong> for their incredible support and resources, which empowered me to contribute my creative vision to the design of this app."
                       </p>
                    </div>
                    
                    <div className="w-[160px] h-[160px] rounded-[36px] shadow-[0_15px_40px_rgba(0,0,0,0.08)] shrink-0 overflow-hidden bg-white border border-gray-100 hover:-translate-y-2 transition-transform duration-500">
                       <img  src="/assets/portfolio_assets/Yapsu%20AI/yapsu_icon_premium.jpg" className="w-full h-full object-cover" />
                    </div>
                 </div>
                 
                 <div className="w-full lg:w-[55%] h-[700px] relative flex justify-center items-center perspective-[2000px] -mt-10 lg:mt-0">
                    <div className="absolute top-[40px] right-[50px] w-[290px] h-[620px] rounded-[48px] p-[6px] bg-white border border-gray-200 shadow-[0_20px_50px_-12px_rgba(0,0,0,0.15)]" style={{ transform: 'rotate(8deg)' }}>
                       <div className="w-full h-full bg-gray-50 rounded-[42px] overflow-hidden relative border border-gray-100">
                          <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[90px] h-[28px] bg-black rounded-full z-20"></div>
                          <img  src="/assets/portfolio_assets/Yapsu%20AI/snapshots/roadmap_04.jpg" className="w-full h-full object-cover" />
                       </div>
                    </div>
                    <div className="absolute top-[120px] left-[50px] w-[310px] h-[660px] rounded-[50px] p-[6px] bg-white border border-gray-200 shadow-[[-20px_30px_60px_rgba(0,0,0,0.15)]] z-10" style={{ transform: 'rotate(-4deg)' }}>
                       <div className="w-full h-full bg-gray-50 rounded-[44px] overflow-hidden relative border border-gray-100">
                          <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[95px] h-[30px] bg-black rounded-full z-20"></div>
                          <img  src="/assets/portfolio_assets/Yapsu%20AI/snapshots/roadmap_07.jpg" className="w-full h-full object-cover" />
                       </div>
                    </div>
                 </div>
              </div>

              {/* 2. APP DESIGN - ISOMETRIC */}
              <div className="w-full flex flex-col items-center mt-20 relative max-w-[1400px] mx-auto">
                 <h3 className="font-['Fredoka'] text-[50px] font-bold text-transparent bg-clip-text bg-gradient-to-r from-orange-500 to-amber-400 text-center mb-10 tracking-wide z-30 drop-shadow-sm">
                    App Design
                 </h3>
                 
                 <div className="relative w-[100vw] max-w-[100vw] h-[850px] flex justify-center items-center overflow-hidden z-20 pointer-events-none" 
                      style={{ WebkitMaskImage: 'linear-gradient(to bottom, transparent 0%, black 5%, black 95%, transparent 100%)', maskImage: 'linear-gradient(to bottom, transparent 0%, black 5%, black 95%, transparent 100%)' }}>
                    
                    <div className="absolute w-[2200px] flex justify-center items-center perspective-[2500px]">
                       <div className="flex gap-[50px] transform rotate-x-[55deg] rotate-z-[-35deg] scale-[0.8] translate-y-[40px]">
                          
                          {/* Column 1 */}
                          <div className="flex flex-col gap-[50px] translate-y-[150px]">
                             {["19_dark_ui.jpg", "onboard_27.jpg", "09_drill_fill.jpg", "13_roleplay_gradient.jpg"].map((src, i) => (
                                <div key={`iso1-${i}`} className="relative w-[280px] h-[600px] rounded-[45px] p-[6px] bg-white border border-gray-200 shadow-[0_20px_40px_rgba(0,0,0,0.1)] transition-transform duration-500 hover:-translate-y-8">
                                   <div className="w-full h-full bg-gray-50 rounded-[40px] overflow-hidden relative border border-gray-100">
                                      <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[85px] h-[26px] bg-black rounded-full z-20"></div>
                                      <img  src={`/assets/portfolio_assets/Yapsu%20AI/snapshots/${src}`} className="w-full h-full object-cover" />
                                   </div>
                                </div>
                             ))}
                          </div>
                          
                          {/* Column 2 */}
                          <div className="flex flex-col gap-[50px] -translate-y-[50px]">
                             {["03_onboard_aha.jpg", "18_boy_bill.jpg", "10_drill_matching.jpg", "14_roleplay_hint.jpg"].map((src, i) => (
                                <div key={`iso2-${i}`} className="relative w-[280px] h-[600px] rounded-[45px] p-[6px] bg-white border border-gray-200 shadow-[0_20px_40px_rgba(0,0,0,0.1)] transition-transform duration-500 hover:-translate-y-8">
                                   <div className="w-full h-full bg-gray-50 rounded-[40px] overflow-hidden relative border border-gray-100">
                                      <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[85px] h-[26px] bg-black rounded-full z-20"></div>
                                      <img  src={`/assets/portfolio_assets/Yapsu%20AI/snapshots/${src}`} className="w-full h-full object-cover" />
                                   </div>
                                </div>
                             ))}
                          </div>

                          {/* Column 3 */}
                          <div className="flex flex-col gap-[50px] translate-y-[100px]">
                             {["z_green_reminders.jpg", "05_roadmap_map.jpg", "11_drill_repeat.jpg", "15_roleplay_feedback.jpg"].map((src, i) => (
                                <div key={`iso3-${i}`} className="relative w-[280px] h-[600px] rounded-[45px] p-[6px] bg-white border border-gray-200 shadow-[0_20px_40px_rgba(0,0,0,0.1)] transition-transform duration-500 hover:-translate-y-8">
                                   <div className="w-full h-full bg-gray-50 rounded-[40px] overflow-hidden relative border border-gray-100">
                                      <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[85px] h-[26px] bg-black rounded-full z-20"></div>
                                      <img  src={`/assets/portfolio_assets/Yapsu%20AI/snapshots/${src}`} className="w-full h-full object-cover" />
                                   </div>
                                </div>
                             ))}
                          </div>

                          {/* Column 4 */}
                          <div className="flex flex-col gap-[50px] -translate-y-[20px]">
                             {["onboard_09.jpg", "roadmap_04.jpg", "z_orange_amazing.jpg", "16_roleplay_transcript.jpg"].map((src, i) => (
                                <div key={`iso4-${i}`} className="relative w-[280px] h-[600px] rounded-[45px] p-[6px] bg-white border border-gray-200 shadow-[0_20px_40px_rgba(0,0,0,0.1)] transition-transform duration-500 hover:-translate-y-8">
                                   <div className="w-full h-full bg-gray-50 rounded-[40px] overflow-hidden relative border border-gray-100">
                                      <div className="absolute top-[12px] left-1/2 -translate-x-1/2 w-[85px] h-[26px] bg-black rounded-full z-20"></div>
                                      <img  src={`/assets/portfolio_assets/Yapsu%20AI/snapshots/${src}`} className="w-full h-full object-cover" />
                                   </div>
                                </div>
                             ))}
                          </div>

                       </div>
                    </div>
                 </div>
              </div>

              {/* 3. EXPERIENCE FLOW - FLAT GRID */}
              <div className="w-full flex flex-col items-center mt-24 mb-16 pt-0">
                 <h3 className="font-['Fredoka'] text-[50px] font-bold text-transparent bg-clip-text bg-gradient-to-r from-orange-500 to-amber-400 text-center mb-16 tracking-wide drop-shadow-sm">
                    Experience Flow
                 </h3>
                 
                 <div className="grid grid-cols-2 md:grid-cols-4 xl:grid-cols-8 gap-4 w-full">
                    {[
                       // ---------------- ROW 1 (8 images) ----------------
                       // 6 ONBOARDING (Post-login)
                       "19_dark_ui.jpg",           // Dark UI (Imagine)
                       "03_onboard_aha.jpg",       // Japanese level
                       "z_green_reminders.jpg",    // Green reminders
                       "onboard_09.jpg",           // Blue tutor
                       "onboard_27.jpg",           // Pink cherry blossom
                       "z_bw_signin.jpg",          // B&W Sign in screen
                       
                       // 2 ROADMAP
                       "05_roadmap_map.jpg",       // Map path
                       "roadmap_04.jpg",           // Vocab table
                       
                       // ---------------- ROW 2 (8 images) ----------------
                       // 4 DRILL
                       "09_drill_fill.jpg",        // Fill in blank
                       "10_drill_matching.jpg",    // Matching
                       "11_drill_repeat.jpg",      // Repeat after
                       "z_orange_amazing.jpg",     // Orange amazing
                       
                       // 4 ROLEPLAY
                       "13_roleplay_gradient.jpg", // Gradient
                       "14_roleplay_hint.jpg",     // Hint
                       "15_roleplay_feedback.jpg", // Feedback
                       "16_roleplay_transcript.jpg"// Transcript
                    ].map((src, i) => (
                       <div key={`flat-${i}`} className="w-full aspect-[9/19] rounded-[24px] overflow-hidden shadow-sm border border-gray-200 bg-white hover:shadow-xl transition-shadow duration-300">
                          <img  src={`/assets/portfolio_assets/Yapsu%20AI/snapshots/${src}`} className="w-full h-full object-cover" />
                       </div>
                    ))}
                 </div>
              </div>

              {/* 4. LIVE PROTOTYPES */}
              <div className="w-full relative z-20 pb-20 pt-0 max-w-[1400px] mx-auto">
                 <h3 className="font-['Fredoka'] text-[50px] font-bold text-transparent bg-clip-text bg-gradient-to-r from-orange-500 to-amber-400 text-center mb-12 tracking-wide drop-shadow-sm">
                    Live Prototypes
                 </h3>
                 
                 <div className="flex flex-col lg:flex-row justify-center items-center gap-16 w-full mt-0">
                    
                    {[
                       { title: "Onboarding", src: "onboarding-feature.mp4" },
                       { title: "Roleplay", src: "roleplay-feature.mp4" },
                       { title: "Roadmap", src: "roadmap-drill-feature.mp4" }
                    ].map((vid, idx) => (
                       <div key={idx} className="flex flex-col items-center">
                          
                          <div className="mb-10 px-8 py-3 bg-white rounded-2xl shadow-sm border border-gray-200 flex items-center justify-center">
                             <h4 className="font-['Fredoka'] text-[24px] font-bold text-[#334155] tracking-wide">
                                {vid.title}
                             </h4>
                          </div>
                          
                          <div className="relative w-[310px] h-[660px] rounded-[52px] p-[8px] bg-white border border-gray-200 shadow-[0_25px_50px_-12px_rgba(0,0,0,0.15)]" style={{ WebkitBoxReflect: "below 12px linear-gradient(transparent 60%, rgba(255,255,255,0.4))" }}>
                             <div className="w-full h-full bg-gray-50 rounded-[44px] overflow-hidden relative border border-gray-100 shadow-[inset_0_0_10px_rgba(0,0,0,0.05)]">
                                <div className="absolute top-[14px] left-1/2 -translate-x-1/2 w-[100px] h-[30px] bg-black rounded-full z-20"></div>
                                <video src={`/assets/yapsu-ai/${vid.src}`} autoPlay muted loop playsInline className="w-full h-full object-cover" />
                             </div>
                          </div>
                          
                       </div>
                    ))}

                 </div>
              </div>

           </div>

           {/* SVG Wave Transition to Chinese Debate */}
           <div className="absolute bottom-0 left-0 w-full overflow-hidden leading-none z-10" style={{ transform: 'translateY(1px)' }}>
              <svg viewBox="0 0 1200 120" preserveAspectRatio="none" className="w-full h-[60px] md:h-[120px] block">
                 <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V120H0V95.8C59.71,118,130.85,121.22,192.4,111.45,236.4,104.5,282.91,73.1,321.39,56.44Z" fill="#06112E"></path>
              </svg>
           </div>
        </section>

                {/* ─── 02. CHINESE DEBATE 2026 ─── */}
        <section id="chinese-debate-2026" className="relative w-full pt-12 pb-24 bg-gradient-to-b from-[#06112E] to-[#0B1F4D] text-white overflow-hidden">
    {/* Decorative Tech Grid Background */}
    <div className="absolute inset-0 bg-[linear-gradient(rgba(34,211,238,0.03)_1px,transparent_1px),linear-gradient(90deg,rgba(34,211,238,0.03)_1px,transparent_1px)] bg-[size:40px_40px] pointer-events-none"></div>

    <div className="max-w-[1400px] mx-auto px-6 sm:px-10 relative z-20 flex flex-col">
        
        {/* 1. SECTION HEADER */}
        <div className="flex flex-col items-center mb-24 text-center">
            <div className="px-6 py-2 border border-cyan-500/30 text-cyan-400 rounded-full text-sm font-bold mb-6 tracking-widest uppercase bg-cyan-950/30 backdrop-blur-sm shadow-[0_0_15px_rgba(34,211,238,0.2)]">
                Event Branding & Social Media
            </div>
            <h2 className="font-['Fredoka'] text-[60px] md:text-[90px] font-black text-transparent bg-clip-text bg-gradient-to-r from-cyan-300 to-blue-500 leading-tight drop-shadow-[0_0_25px_rgba(34,211,238,0.4)] mb-6">
                Chinese Debate '26
            </h2>
            <p className="max-w-2xl text-lg text-blue-200/80 font-['Quicksand'] font-medium leading-relaxed">
                A vibrant and futuristic visual identity designed for the Chinese Debate competition. Emphasizing a dynamic, high-energy cyber aesthetic to captivate a modern youth audience.
            </p>
        </div>

        {/* 2. KEY VISUAL */}
        <div className="w-full mb-32 flex flex-col items-center">
            <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-cyan-400 mb-10 tracking-wide drop-shadow-[0_0_10px_rgba(34,211,238,0.5)]">
                Key Visual
            </h3>
            <div className="relative w-full max-w-5xl rounded-[24px] overflow-hidden border-2 border-cyan-500/50 shadow-[0_0_40px_rgba(34,211,238,0.2)]">
                <img  src="/assets/portfolio_assets/CC%20FTU/Chinese%20Debate%202026/KEY%20VISUAL/cover%20tbth.jpg" alt="Chinese Debate Key Visual Cover" className="w-full h-auto block" />
            </div>
            
            {/* Avatar Badge */}
            <div className="relative -mt-16 w-32 h-32 md:w-40 md:h-40 rounded-full p-1 bg-gradient-to-br from-cyan-400 to-blue-600 shadow-[0_0_30px_rgba(34,211,238,0.5)] z-10 group hover:-translate-y-2 transition-transform duration-300">
                <div className="w-full h-full rounded-full overflow-hidden bg-[#06112E]">
                    <img  src="/assets/portfolio_assets/CC%20FTU/Chinese%20Debate%202026/KEY%20VISUAL/avatar-01.jpg" alt="Chinese Debate Avatar" className="w-full h-full object-cover" />
                </div>
            </div>
        </div>

        {/* 3. EVENT APPLICATIONS */}
        <div className="w-full mb-32 flex flex-col items-center">
            <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-cyan-400 mb-10 tracking-wide text-center drop-shadow-[0_0_10px_rgba(34,211,238,0.5)]">
                Event Applications
            </h3>
            <div className="w-full max-w-5xl flex flex-col gap-16">
                {/* Backdrop */}
                <div className="flex flex-col items-center gap-5">
                    <div className="relative group w-full rounded-[24px] overflow-hidden border-2 border-cyan-900/60 hover:border-cyan-400/80 transition-colors duration-500 shadow-[0_0_30px_rgba(34,211,238,0.1)]">
                        <img  src="/assets/portfolio_assets/CC%20FTU/Chinese%20Debate%202026/Print%20&%20Event%20Applications/Backdrop-01.jpg" alt="Backdrop Design" className="w-full h-auto block group-hover:scale-[1.02] transition-transform duration-700" />
                    </div>
                    <h4 className="font-['Quicksand'] font-bold text-xl text-cyan-300 tracking-wider uppercase drop-shadow-md">Stage Backdrop</h4>
                </div>
                {/* Ticket */}
                <div className="flex flex-col items-center gap-5">
                    <div className="relative group w-full max-w-3xl mx-auto rounded-[24px] overflow-hidden border-2 border-cyan-900/60 hover:border-cyan-400/80 transition-colors duration-500 shadow-[0_0_30px_rgba(34,211,238,0.1)]">
                        <img  src="/assets/portfolio_assets/CC%20FTU/Chinese%20Debate%202026/Print%20&%20Event%20Applications/TICKET.jpg" alt="Event Ticket" className="w-full h-auto block group-hover:scale-[1.02] transition-transform duration-700 drop-shadow-xl" />
                    </div>
                    <h4 className="font-['Quicksand'] font-bold text-xl text-cyan-300 tracking-wider uppercase drop-shadow-md">Event Ticket</h4>
                </div>
            </div>
        </div>

        {/* 4. DIGITAL & SOCIAL */}
        <div className="w-full mb-10">
            <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-bold text-cyan-400 mb-10 tracking-wide text-center drop-shadow-[0_0_10px_rgba(34,211,238,0.5)]">
                Digital & Social
            </h3>
            
            {/* MASONRY LAYOUT FOR PERFECT PACKING */}
            <div className="columns-1 md:columns-2 lg:columns-3 gap-6 w-full max-w-7xl mx-auto">
                
                {/* Video Block */}
                <div className="relative rounded-[20px] overflow-hidden border-2 border-cyan-500/50 group shadow-[0_0_20px_rgba(34,211,238,0.2)] break-inside-avoid mb-6 inline-block w-full">
                    <video src="/assets/portfolio_assets/CC%20FTU/Chinese%20Debate%202026/VIDEO/Video%20công%20bố%20top%206%20chung%20kết_.mp4" autoPlay muted loop playsInline className="w-full h-auto block" />
                </div>

                {/* Social Posts */}
                {[
                    "Công bố quán quân.jpg", 
                    "GIA HẠN ĐƠN ĐĂNG KÝ.jpg", 
                    "Công bố Á quân.jpg", 
                    "Post giới thiệu đại sứ truyền thông.jpg", 
                    "Post mở đơn.jpg"
                ].map((filename, idx) => (
                    <div key={idx} className="relative rounded-[20px] overflow-hidden border-2 border-blue-900/60 group hover:border-cyan-400/80 transition-colors duration-300 shadow-md break-inside-avoid mb-6 inline-block w-full">
                        <img  src={`/assets/portfolio_assets/CC%20FTU/Chinese%20Debate%202026/Social%20Posts/${filename}`} alt={filename.replace('.jpg', '')} className="w-full h-auto block group-hover:scale-105 transition-transform duration-500" />
                    </div>
                ))}
            </div>
        </div>

    </div>
</section>

        {/* ─── 03. GEN 20 RECRUITMENT ─── */}
        <section id="gen-20-recruit" className="relative w-full py-24 bg-gradient-to-b from-[#EAF2E3] via-[#DCEBCE] to-[#C9E0B6] overflow-hidden">
           <div className="max-w-[1400px] mx-auto px-6 sm:px-10 relative z-20 flex flex-col">
              
              {/* 1. SECTION HEADER */}
              <div className="flex flex-col items-center mb-20 text-center">
                  <div className="px-6 py-2 border-[4px] border-white text-[#3B5B35] rounded-full text-sm font-bold mb-6 tracking-widest uppercase bg-white/50 backdrop-blur-sm shadow-md ">
                      Campaign Design
                  </div>
                  <h2 className="font-['Fredoka'] text-[50px] md:text-[80px] font-black text-transparent bg-clip-text bg-gradient-to-b from-[#82BA5D] to-[#2A5212] leading-none mb-6 pb-2" style={{ filter: 'drop-shadow(0px 0px 10px rgba(255,255,255,1))' }}>
                      Gen 20th Recruitment
                  </h2>
                  <p className="max-w-2xl text-lg text-[#3B5B35] font-['Quicksand'] font-bold leading-relaxed">
                      The annual recruitment campaign of the Chinese Club - Foreign Trade University (CC FTU).
                  </p>
              </div>

              {/* 2. KEY VISUAL */}
              <div className="w-full mb-32 flex flex-col items-center">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-black text-transparent bg-clip-text bg-gradient-to-b from-[#82BA5D] to-[#2A5212] mb-10 tracking-wide" style={{ filter: 'drop-shadow(0px 0px 8px rgba(255,255,255,0.9))' }}>
                      Key Visual
                  </h3>
                  <div className="relative w-full max-w-5xl rounded-[32px] overflow-hidden border-[4px] border-white shadow-[0_20px_50px_rgba(59,91,53,0.2)] group">
                      <img  src="/assets/portfolio_assets/CC%20FTU/CC%20FTU%20Gen%2020%20Recruitment/KEY%20VISUAL/cover%20tuyển%20gen.jpg" alt="Gen 20 Key Visual" className="w-full h-auto block group-hover:scale-105 transition-transform duration-700" />
                  </div>
                  
                  {/* Avatar Badge */}
                  <div className="relative -mt-20 w-32 h-32 md:w-44 md:h-44 rounded-full p-1 bg-white shadow-xl z-10 group hover:-translate-y-2 transition-transform duration-300 ">
                      <div className="w-full h-full rounded-full overflow-hidden bg-[#D9EBCB]">
                          <img  src="/assets/portfolio_assets/CC%20FTU/CC%20FTU%20Gen%2020%20Recruitment/KEY%20VISUAL/avt%20tuyển%20gen.jpg" alt="Gen 20 Avatar" className="w-full h-full object-cover" />
                      </div>
                  </div>
              </div>

              {/* 3. EVENT APPLICATIONS */}
              <div className="w-full mb-32 flex flex-col items-center">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-black text-transparent bg-clip-text bg-gradient-to-b from-[#82BA5D] to-[#2A5212] mb-10 tracking-wide text-center" style={{ filter: 'drop-shadow(0px 0px 8px rgba(255,255,255,0.9))' }}>
                      Event Applications
                  </h3>
                  <div className="w-full max-w-lg flex flex-col items-center gap-6">
                      <div className="relative group w-full rounded-[24px] overflow-hidden border-[6px] border-white shadow-[0_15px_40px_rgba(59,91,53,0.15)] hover:shadow-[0_25px_50px_rgba(59,91,53,0.25)] transition-all duration-500 ">
                          <img  src="/assets/portfolio_assets/CC%20FTU/CC%20FTU%20Gen%2020%20Recruitment/Print%20&%20Event%20Applications/frame.jpg" alt="Avatar Frame" className="w-full h-auto block group-hover:scale-[1.02] transition-transform duration-700" />
                      </div>
                      <h4 className="font-['Quicksand'] font-bold text-xl text-[#3B5B35] tracking-wider uppercase mt-4">Avatar Frame</h4>
                  </div>
              </div>

              {/* 4. DIGITAL & SOCIAL (AUTO-SCROLL CAROUSEL) */}
              <div className="w-full mb-10 overflow-hidden">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-black text-transparent bg-clip-text bg-gradient-to-b from-[#82BA5D] to-[#2A5212] mb-10 tracking-wide text-center" style={{ filter: 'drop-shadow(0px 0px 8px rgba(255,255,255,0.9))' }}>
                      Digital & Social
                  </h3>
                  
                  <div className="relative w-full max-w-6xl mx-auto group">
                      {/* Carousel Container */}
                      <div className="relative w-full h-[400px] sm:h-[450px] md:h-[550px] flex justify-center items-center overflow-hidden">
                          {[
                              "Q&A.jpg", 
                              "THÔNG BÁO KẾT QUẢ.jpg", 
                              "VIRAL POST.jpg", 
                              "Đóng đơn đăng ký.jpg"
                          ].map((filename, idx) => {
                              let diff = idx - activeGen20Idx;
                              if (diff === 3) diff = -1;
                              if (diff === -3) diff = 1;
                              if (diff === -2) diff = 2;
                              
                              let translateX = "0%";
                              let scale = 1;
                              let opacity = 1;
                              let zIndex = 30;
                              let blur = "0px";

                              if (diff === 0) {
                                  // Active
                                  translateX = "0%";
                                  scale = 1;
                                  opacity = 1;
                                  zIndex = 30;
                                  blur = "0px";
                              } else if (diff === 1) {
                                  // Right
                                  translateX = "110%";
                                  scale = 0.85;
                                  opacity = 0.3;
                                  zIndex = 20;
                                  blur = "3px";
                              } else if (diff === -1) {
                                  // Left
                                  translateX = "-110%";
                                  scale = 0.85;
                                  opacity = 0.3;
                                  zIndex = 20;
                                  blur = "3px";
                              } else {
                                  // Hidden
                                  translateX = "0%";
                                  scale = 0.5;
                                  opacity = 0;
                                  zIndex = 10;
                                  blur = "10px";
                              }

                              return (
                                  <div 
                                      key={idx} 
                                      onClick={() => setActiveGen20Idx(idx)}
                                      className="absolute top-1/2 left-1/2 cursor-pointer transition-all duration-700 ease-[cubic-bezier(0.25,1,0.5,1)] rounded-[24px] overflow-hidden border-[6px] border-white shadow-[0_15px_40px_rgba(59,91,53,0.3)] hover:opacity-80"
                                      style={{ 
                                          transform: `translate(-50%, -50%) translateX(${translateX}) scale(${scale})`,
                                          zIndex: zIndex,
                                          opacity: opacity,
                                          filter: `blur(${blur})`
                                      }}
                                  >
                                      <img  src={`/assets/portfolio_assets/CC%20FTU/CC%20FTU%20Gen%2020%20Recruitment/SOCIAL%20POST/${filename}`} alt={filename.replace('.jpg', '')} className="h-[280px] sm:h-[350px] md:h-[420px] w-auto max-w-none block object-contain" />
                                  </div>
                              );
                          })}
                      </div>
</div>
              </div>

           </div>
        </section>

        {/* ─── 04. 19TH ANNIVERSARY ─── */}
        <section id="19th-birthday" className="relative w-full py-24 bg-gradient-to-b from-[#F4EEF7] via-[#EAE1F4] to-[#D5C2ED] overflow-hidden">
           <div className="max-w-[1400px] mx-auto px-6 sm:px-10 relative z-20 flex flex-col">
              
              {/* 1. SECTION HEADER */}
              <div className="flex flex-col items-center mb-20 text-center">
                  <div className="px-6 py-2 border-[4px] border-white text-[#8665C3] rounded-full text-sm font-bold mb-6 tracking-widest uppercase bg-white/50 backdrop-blur-sm shadow-md">
                      Event Identity
                  </div>
                  <h2 className="font-['Fredoka'] text-[60px] md:text-[90px] font-black text-transparent bg-clip-text bg-gradient-to-b from-[#D1B3FF] to-[#6A3CC9] leading-none mb-6 pb-2" style={{ filter: 'drop-shadow(0px 0px 10px rgba(255,255,255,1))' }}>
                      19th Anniversary
                  </h2>
                  <p className="max-w-2xl text-lg text-[#6B4AA6]/90 font-['Quicksand'] font-bold leading-relaxed">
                      "Vân Hạ Diệp Mộng" - Celebrating the 19th Anniversary of the Chinese Club - Foreign Trade University (CC FTU).
                  </p>
              </div>

              {/* 2. KEY VISUAL */}
              <div className="w-full mb-32 flex flex-col items-center">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-black text-transparent bg-clip-text bg-gradient-to-b from-[#D1B3FF] to-[#6A3CC9] mb-10 tracking-wide" style={{ filter: 'drop-shadow(0px 0px 8px rgba(255,255,255,0.9))' }}>
                      Key Visual
                  </h3>
                  <div className="relative w-full max-w-5xl rounded-[32px] overflow-hidden border-[4px] border-white shadow-[0_20px_50px_rgba(134,101,195,0.2)] group">
                      <img  src="/assets/portfolio_assets/CC%20FTU/CC%20FTU%2019th%20Anniversary/Key%20Visual/cover%20tím.jpg" alt="19th Anniversary Key Visual" className="w-full h-auto block group-hover:scale-105 transition-transform duration-700" />
                  </div>
                  
                  {/* Avatar Badge */}
                  <div className="relative -mt-20 w-32 h-32 md:w-44 md:h-44 rounded-full p-1 bg-white shadow-xl z-10 group hover:-translate-y-2 transition-transform duration-300">
                      <div className="w-full h-full rounded-full overflow-hidden bg-[#E3D5F2]">
                          <img  src="/assets/portfolio_assets/CC%20FTU/CC%20FTU%2019th%20Anniversary/Key%20Visual/AVT%20tím.jpg" alt="19th Avatar" className="w-full h-full object-cover" />
                      </div>
                  </div>
              </div>

              {/* 3. EVENT APPLICATIONS (MASONRY) */}
              <div className="w-full mb-10">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-black text-transparent bg-clip-text bg-gradient-to-b from-[#D1B3FF] to-[#6A3CC9] mb-10 tracking-wide text-center" style={{ filter: 'drop-shadow(0px 0px 8px rgba(255,255,255,0.9))' }}>
                      Event Applications
                  </h3>
                  
                  <div className="columns-1 md:columns-2 gap-8 w-full max-w-4xl mx-auto">
                      {[
                          { file: "FRAME tím.jpg", name: "Avatar Frame" },
                          { file: "BACKDROP tím.jpg", name: "Event Backdrop" },
                          { file: "Social story.jpg", name: "Social Media Story" }
                      ].map((item, idx) => (
                          <div key={idx} className="break-inside-avoid flex flex-col items-center w-full mb-8">
                              <div className="relative rounded-[24px] overflow-hidden border-[6px] border-white group hover:border-[#8665C3] transition-colors duration-300 shadow-lg w-full mb-4">
                                  <img  src={`/assets/portfolio_assets/CC%20FTU/CC%20FTU%2019th%20Anniversary/Print%20&%20Event%20Applications/${item.file}`} alt={item.name} className="w-full h-auto block group-hover:scale-105 transition-transform duration-500" />
                              </div>
                              <h4 className="font-['Quicksand'] font-bold text-lg text-[#8665C3] tracking-wider uppercase text-center bg-white/60 px-6 py-2 rounded-full shadow-sm">{item.name}</h4>
                          </div>
                      ))}
                  </div>
              </div>

           </div>
        </section>

        {/* ─── 05. CHINESE DEBATE 2025 ─── */}
        <section id="chinese-debate-25" className="relative w-full py-24 bg-gradient-to-b from-[#4A2C11] via-[#3C230D] to-[#201206] overflow-hidden">
           <div className="max-w-[1400px] mx-auto px-6 sm:px-10 relative z-20 flex flex-col">
              
              {/* 1. SECTION HEADER */}
              <div className="flex flex-col items-center mb-20 text-center">
                  <div className="px-6 py-2 border-2 border-[#D4AF37] text-[#FFF2B2] rounded-full text-sm font-bold mb-6 tracking-widest uppercase bg-[#4A2C11]/50 backdrop-blur-sm shadow-[0_0_15px_rgba(212,175,55,0.3)]">
                      Event Identity
                  </div>
                  <h2 className="font-['Fredoka'] text-[60px] md:text-[90px] font-black text-transparent bg-clip-text bg-gradient-to-b from-[#FFF2B2] to-[#D4AF37] leading-none mb-6 pb-2" style={{ filter: 'drop-shadow(0px 0px 8px rgba(212,175,55,0.4))' }}>
                      Chinese Debate 2025
                  </h2>
                  <p className="max-w-2xl text-lg text-[#F3E5AB] font-['Quicksand'] font-bold leading-relaxed">
                      A fierce and explosive visual identity designed for the Chinese Debate competition. Emphasizing a dynamic, fiery golden dragon aesthetic to ignite passion and captivate a modern youth audience.
                  </p>
              </div>

              {/* 2. KEY VISUAL */}
              <div className="w-full mb-32 flex flex-col items-center">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-black text-transparent bg-clip-text bg-gradient-to-b from-[#FFF2B2] to-[#D4AF37] mb-10 tracking-wide" style={{ filter: 'drop-shadow(0px 0px 8px rgba(212,175,55,0.4))' }}>
                      Key Visual
                  </h3>
                  <div className="relative w-full max-w-5xl rounded-[32px] overflow-hidden border-[4px] border-[#D4AF37] shadow-[0_0_40px_rgba(212,175,55,0.3)] group">
                      <img  src="/assets/portfolio_assets/CC%20FTU/Chinese%20Debate%202025/KEY%20VISUAL/cover%20tbth1.jpg" alt="Debate 2025 Key Visual" className="w-full h-auto block group-hover:scale-105 transition-transform duration-700" />
                  </div>
                  
                  {/* Avatar Badge */}
                  <div className="relative -mt-20 w-32 h-32 md:w-44 md:h-44 rounded-full p-1 bg-[#D4AF37] shadow-[0_0_30px_rgba(212,175,55,0.4)] z-10 group hover:-translate-y-2 transition-transform duration-300">
                      <div className="w-full h-full rounded-full overflow-hidden bg-[#231710]">
                          <img  src="/assets/portfolio_assets/CC%20FTU/Chinese%20Debate%202025/KEY%20VISUAL/AVATAR%20TBTH.jpg" alt="Debate Avatar" className="w-full h-full object-cover" />
                      </div>
                  </div>
              </div>

              {/* 2.5 PRINT & EVENT APPLICATIONS */}
              <div className="w-full mb-32 flex flex-col items-center">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-black text-transparent bg-clip-text bg-gradient-to-b from-[#FFF2B2] to-[#D4AF37] mb-10 tracking-wide text-center" style={{ filter: 'drop-shadow(0px 0px 8px rgba(212,175,55,0.4))' }}>
                      Event Applications
                  </h3>
                  
                  <div className="w-full max-w-5xl flex flex-col gap-16">
                      <div className="flex flex-col items-center gap-5">
                          <div className="relative group w-full rounded-[24px] overflow-hidden border-2 border-[#D4AF37] shadow-[0_0_20px_rgba(212,175,55,0.2)] hover:border-[#F3E5AB] transition-colors duration-500">
                              <img  src="/assets/portfolio_assets/CC%20FTU/Chinese%20Debate%202025/Print%20&%20Event%20Applications/BACKDROP.jpg" alt="Event Backdrop" className="w-full h-auto block group-hover:scale-[1.02] transition-transform duration-700" />
                          </div>
                          <h4 className="font-['Quicksand'] font-bold text-xl text-[#FFF2B2] tracking-wider uppercase drop-shadow-md">Stage Backdrop</h4>
                      </div>
                      
                      <div className="columns-1 md:columns-3 gap-8 w-full">
                          {[
                              { file: "phướn_1.jpg", name: "Vertical Banner 1" },
                              { file: "phướn_Huyen.jpg", name: "Vertical Banner 2" },
                              { file: "phướn_Thu.jpg", name: "Vertical Banner 3" }
                          ].map((item, idx) => (
                              <div key={idx} className="flex flex-col items-center gap-5 mb-8 break-inside-avoid">
                                  <div className="relative group w-full rounded-[24px] overflow-hidden border-2 border-[#D4AF37] shadow-[0_0_20px_rgba(212,175,55,0.2)] hover:border-[#F3E5AB] transition-colors duration-500">
                                      <img  src={`/assets/portfolio_assets/CC%20FTU/Chinese%20Debate%202025/Print%20&%20Event%20Applications/${item.file}`} alt={item.name} className="w-full h-auto block group-hover:scale-[1.02] transition-transform duration-700" />
                                  </div>
                                  <h4 className="font-['Quicksand'] font-bold text-lg text-[#FFF2B2] tracking-wider uppercase drop-shadow-md text-center">{item.name}</h4>
                              </div>
                          ))}
                      </div>
                  </div>
              </div>

              {/* 3. DIGITAL & SOCIAL POSTS (CAROUSEL) */}
              <div className="w-full mb-24 overflow-hidden">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-black text-transparent bg-clip-text bg-gradient-to-b from-[#FFF2B2] to-[#D4AF37] mb-10 tracking-wide text-center" style={{ filter: 'drop-shadow(0px 0px 8px rgba(212,175,55,0.4))' }}>
                      Digital & Social
                  </h3>
                  
                  <div className="relative w-full h-[400px] sm:h-[450px] md:h-[550px] flex justify-center items-center">
                      {[
                          "MỞ ĐƠN.jpg",
                          "THÔNG BÁO QUÁN QUÂN.jpg",
                          "THỂ LỆ VÒNG SƠ KHẢO.jpg",
                          "THÔNG BÁO CƠ CẤU GIẢI THƯỞNG.jpg",
                          "QUYỀN LỢI KHI THAM GIA CUỘC THI.jpg",
                          "TỪ KHOÁ VÒNG CHUNG KẾT CUỘC THI.jpg",
                          "GIỚI THIỆU BẢO TRỢ TRUYỀN THÔNG.jpg",
                          "GIỚI THIỆU ĐỐI TÁC TRUYỀN THÔNG.jpg",
                          "GIỚI THIỆU NTT-1.jpg",
                          "GIỚI THIỆU NTT-2.jpg"
                      ].map((filename, idx) => {
                          let diff = idx - activeDebateIdx;
                          if (diff > 5) diff -= 10;
                          if (diff < -4) diff += 10;
                          
                          let translateX = "0%";
                          let scale = 1;
                          let opacity = 1;
                          let zIndex = 30;
                          let blur = "0px";
                          let pointerEvents = "auto";

                          if (diff === 0) {
                              // Active
                              translateX = "0%";
                              scale = 1;
                              opacity = 1;
                              zIndex = 30;
                              blur = "0px";
                          } else if (diff === 1) {
                              // Right
                              translateX = "110%";
                              scale = 0.85;
                              opacity = 0.4;
                              zIndex = 20;
                              blur = "3px";
                          } else if (diff === -1) {
                              // Left
                              translateX = "-110%";
                              scale = 0.85;
                              opacity = 0.4;
                              zIndex = 20;
                              blur = "3px";
                          } else {
                              // Hidden
                              translateX = "0%";
                              scale = 0.5;
                              opacity = 0;
                              zIndex = 10;
                              blur = "10px";
                              pointerEvents = "none";
                          }

                          return (
                              <div 
                                  key={idx} 
                                  onClick={() => setActiveDebateIdx(idx)}
                                  className="absolute top-1/2 left-1/2 cursor-pointer transition-all duration-700 ease-[cubic-bezier(0.25,1,0.5,1)] rounded-[24px] overflow-hidden border-[4px] border-[#D4AF37] shadow-[0_15px_40px_rgba(212,175,55,0.3)] hover:opacity-80"
                                  style={{ 
                                      transform: `translate(-50%, -50%) translateX(${translateX}) scale(${scale})`,
                                      zIndex: zIndex,
                                      opacity: opacity,
                                      filter: `blur(${blur})`,
                                      pointerEvents: pointerEvents as any
                                  }}
                              >
                                  <img  src={`/assets/portfolio_assets/CC%20FTU/Chinese%20Debate%202025/Social%20Posts/${filename}`} alt={filename.replace('.jpg', '')} className="h-[280px] sm:h-[350px] md:h-[420px] w-auto max-w-none block object-contain" />
                              </div>
                          );
                      })}
                  </div>
              </div>

              {/* 4. VIDEO PRODUCTION */}
              <div className="w-full mb-10 flex flex-col items-center">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-black text-transparent bg-clip-text bg-gradient-to-b from-[#FFF2B2] to-[#D4AF37] mb-10 tracking-wide text-center" style={{ filter: 'drop-shadow(0px 0px 8px rgba(212,175,55,0.4))' }}>
                      Video Production
                  </h3>
                  <div className="w-full max-w-4xl relative rounded-[24px] overflow-hidden border-[4px] border-[#D4AF37] shadow-[0_0_40px_rgba(212,175,55,0.3)] bg-black">
                      <video 
                          src="/assets/portfolio_assets/CC%20FTU/Chinese%20Debate%202025/Video/THỂ%20LỆ%20VÒNG%20CHUNG%20KẾT.mp4"
                          autoPlay
                          playsInline
                          controls
                          muted
                          loop
                          className="w-full h-auto block"
                      />
                  </div>
                  <h4 className="font-['Quicksand'] font-bold text-lg text-[#FFF2B2] tracking-wider mt-6">
                      Final Round Rules & Trailer
                  </h4>
              </div>

           </div>
        </section>

        {/* ─── 06. TALKSHOW ─── */}
        <section id="talkshow" className="relative w-full py-24 bg-gradient-to-b from-[#E8F4F8] via-[#DBEDF4] to-[#BBD9E5] overflow-hidden">
           <div className="max-w-[1400px] mx-auto px-6 sm:px-10 relative z-20 flex flex-col">
              
              {/* 1. SECTION HEADER */}
              <div className="flex flex-col items-center mb-20 text-center">
                  <div className="px-6 py-2 border-[3px] border-[#58B3D3] text-[#4194B1] rounded-full text-sm font-bold mb-6 tracking-widest uppercase bg-white/60 backdrop-blur-sm shadow-[0_0_15px_rgba(88,179,211,0.2)]">
                      Event Identity
                  </div>
                  <h2 className="font-['Fredoka'] text-[60px] md:text-[90px] font-black text-transparent bg-clip-text bg-gradient-to-b from-[#8DD1E8] to-[#4194B1] leading-none mb-6 pb-2" style={{ filter: 'drop-shadow(0px 0px 10px rgba(255,255,255,1))' }}>
                      E-Commerce Talkshow
                  </h2>
                  <p className="max-w-2xl text-lg text-[#58B3D3] font-['Quicksand'] font-bold leading-relaxed">
                      "Từ Trung Quốc đến Việt Nam: Livestream đã cách mạng hóa ngành bán lẻ như thế nào?" - A modern and engaging talkshow exploring the e-commerce livestream revolution.
                  </p>
              </div>

              {/* 2. KEY VISUAL */}
              <div className="w-full mb-24 flex flex-col items-center">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-black text-transparent bg-clip-text bg-gradient-to-b from-[#8DD1E8] to-[#4194B1] mb-10 tracking-wide" style={{ filter: 'drop-shadow(0px 0px 8px rgba(255,255,255,0.9))' }}>
                      Key Visual
                  </h3>
                  <div className="relative w-full max-w-5xl rounded-[32px] overflow-hidden border-[4px] border-white shadow-[0_20px_50px_rgba(88,179,211,0.2)] group">
                      <img  src="/assets/portfolio_assets/CC%20FTU/Talkshow/KEY%20VISUAL/cover%20nè%2022.04.05.jpg" alt="Talkshow Key Visual" className="w-full h-auto block group-hover:scale-105 transition-transform duration-700" />
                  </div>
                  
                  {/* Avatar Badge */}
                  <div className="relative -mt-20 w-32 h-32 md:w-44 md:h-44 rounded-full p-1 bg-white shadow-[0_15px_40px_rgba(88,179,211,0.3)] z-10 group hover:-translate-y-2 transition-transform duration-300">
                      <div className="w-full h-full rounded-full overflow-hidden bg-[#E8F4F8]">
                          <img  src="/assets/portfolio_assets/CC%20FTU/Talkshow/KEY%20VISUAL/avatar.jpg" alt="Talkshow Avatar" className="w-full h-full object-cover" />
                      </div>
                  </div>
              </div>

              {/* 3. DIGITAL & SOCIAL */}
              <div className="w-full mb-10 flex flex-col items-center">
                  <h3 className="font-['Fredoka'] text-3xl md:text-4xl font-black text-transparent bg-clip-text bg-gradient-to-b from-[#8DD1E8] to-[#4194B1] mb-10 tracking-wide text-center" style={{ filter: 'drop-shadow(0px 0px 8px rgba(255,255,255,0.9))' }}>
                      Digital & Social
                  </h3>
                  
                  <div className="flex flex-wrap justify-center gap-6 w-full max-w-[1200px] mx-auto">
                      {[
                          "NTT-04.jpg",
                          "NTT-01.jpg",
                          "NTT-02.jpg",
                          "NTT-03.jpg",
                          "Thông báo danh sách nhận ĐRL.jpg"
                      ].map((filename, idx) => (
                          <div key={idx} className="relative rounded-[16px] overflow-hidden border-[4px] border-white shadow-[0_15px_30px_rgba(88,179,211,0.15)] group hover:border-[#8DD1E8] transition-colors duration-300 w-full sm:w-[calc(50%-12px)] lg:w-[calc(33.333%-16px)] flex-shrink-0">
                              <img src={`/assets/portfolio_assets/CC%20FTU/Talkshow/SOCIAL%20POST/${filename}`} alt={filename.replace('.jpg', '')} className="w-full h-auto block group-hover:scale-105 transition-transform duration-500"  />
                          </div>
                      ))}
                  </div>
                  
              </div>

           </div>
        </section>

        {/* ─── 07. ZODIAC ─── */}
        <section id="zodiac" className="relative w-full pt-32 pb-[200px] md:pb-[250px] bg-gradient-to-b from-[#F9F7F3] via-[#F4F0E8] to-[#EBE4D5] overflow-hidden">
           
           <div className="absolute inset-0 opacity-[0.04] pointer-events-none" style={{ backgroundImage: 'url("data:image/svg+xml,%3Csvg viewBox=\'0 0 200 200\' xmlns=\'http://www.w3.org/2000/svg\'%3E%3Cfilter id=\'noiseFilter\'%3E%3CfeTurbulence type=\'fractalNoise\' baseFrequency=\'0.85\' numOctaves=\'3\' stitchTiles=\'stitch\'/%3E%3C/filter%3E%3Crect width=\'100%25\' height=\'100%25\' filter=\'url(%23noiseFilter)\'/%3E%3C/svg%3E")' }}></div>

           <div className="max-w-[1400px] mx-auto relative z-20 flex flex-col items-center">
              <div className="flex flex-col items-center mb-12 text-center px-6">
                  <div className="px-8 py-2 border-[3px] border-[#8C8377] text-[#8C8377] rounded-full text-sm font-bold mb-6 tracking-widest uppercase bg-transparent shadow-[0_0_15px_rgba(140,131,119,0.1)] font-['Quicksand']">
                      Branding
                  </div>
                  <h2 className="font-serif text-[60px] md:text-[90px] text-[#2C2822] leading-none mb-6 text-center font-light tracking-[0.1em]">
                      ZODIAC
                  </h2>
                  <p className="w-full max-w-[1100px] text-base md:text-lg text-[#736B60] font-serif italic font-normal leading-loose px-4 text-center">
                      A premium visual identity designed for Zodiac Collections. The signature circular emblem<br className="hidden md:block" />masterfully combines half sun and half moon, symbolizing the harmonious cycle of a full day.
                  </p>
              </div>

              <div className="relative w-full max-w-[1100px] h-[580px] sm:h-[650px] md:h-[800px] mx-auto mt-4 perspective-[1200px]">
                  {[
    { title: "MÁC 1", images: ["/assets/portfolio_assets/ZODIAC%20COLLECTIONS/Mác%201/LOGO%20MỚI/1.jpg", "/assets/portfolio_assets/ZODIAC%20COLLECTIONS/Mác%201/LOGO%20MỚI/2.jpg", "/assets/portfolio_assets/ZODIAC%20COLLECTIONS/Mác%201/LOGO%20MỚI/3.jpg", "/assets/portfolio_assets/ZODIAC%20COLLECTIONS/Mác%201/LOGO%20MỚI/4.jpg", "/assets/portfolio_assets/ZODIAC%20COLLECTIONS/Mác%201/LOGO%20MỚI/5.jpg"] },
    { title: "MÁC 2", images: ["/assets/portfolio_assets/ZODIAC%20COLLECTIONS/Mác%202/ẢNH%201%20LOGO%20MỚI.jpg", "/assets/portfolio_assets/ZODIAC%20COLLECTIONS/Mác%202/ẢNH%202.jpg"] },
    { title: "MÁC 3", images: ["/assets/portfolio_assets/ZODIAC%20COLLECTIONS/Mác%203/1%20MỚI.jpg", "/assets/portfolio_assets/ZODIAC%20COLLECTIONS/Mác%203/2.jpg", "/assets/portfolio_assets/ZODIAC%20COLLECTIONS/Mác%203/3.jpg", "/assets/portfolio_assets/ZODIAC%20COLLECTIONS/Mác%203/4.jpg", "/assets/portfolio_assets/ZODIAC%20COLLECTIONS/Mác%203/5.jpg", "/assets/portfolio_assets/ZODIAC%20COLLECTIONS/Mác%203/6.jpg"] },
    { title: "MÁC 4", images: ["/assets/portfolio_assets/ZODIAC%20COLLECTIONS/MÁC%204/MỚI.jpg"] },
    { title: "MÁC 5", images: ["/assets/portfolio_assets/ZODIAC%20COLLECTIONS/MÁC%205/LOGO%20TRÒN%20MỚI/10.jpg", "/assets/portfolio_assets/ZODIAC%20COLLECTIONS/MÁC%205/LOGO%20TRÒN%20MỚI/6.jpg", "/assets/portfolio_assets/ZODIAC%20COLLECTIONS/MÁC%205/LOGO%20TRÒN%20MỚI/7.jpg", "/assets/portfolio_assets/ZODIAC%20COLLECTIONS/MÁC%205/LOGO%20TRÒN%20MỚI/8.jpg", "/assets/portfolio_assets/ZODIAC%20COLLECTIONS/MÁC%205/LOGO%20TRÒN%20MỚI/9.jpg"] },
  ].map((page, idx) => {
                      let diff = idx - activeZodiacPage;
                      let translateX = "0px"; let translateY = "0px"; let rotate = "0deg"; let opacity = 1; let zIndex = 20 - idx; let pointerEvents = "auto"; let scale = 1;
                      
                      if (diff < 0) {
                          translateX = "-120%"; translateY = "-80%"; rotate = "-15deg"; opacity = 0; pointerEvents = "none"; scale = 0.85;
                      } else if (diff === 0) {
                          translateX = "0px"; translateY = "0px"; rotate = "0deg"; zIndex = 30;
                      } else {
                          translateX = `${diff * 15}px`; translateY = `${diff * 15}px`; rotate = `${diff * 1}deg`; zIndex = 20 - diff; scale = 1 - (diff * 0.02); opacity = 1 - (diff * 0.08); 
                      }

                      return (
                          <div 
                              key={idx}
                              className="absolute inset-0 bg-[#FDFCF9] rounded-[24px] border border-[#EBE6DD] p-6 sm:p-8 md:p-14 transition-all duration-[900ms] ease-[cubic-bezier(0.25,1,0.5,1)] overflow-hidden flex flex-col shadow-[0_20px_60px_rgba(90,80,70,0.08)]"
                              style={{ transform: `translate(${translateX}, ${translateY}) rotate(${rotate}) scale(${scale})`, opacity: opacity, zIndex: zIndex, pointerEvents: pointerEvents as any }}
                          >
                              <div className="w-full flex justify-between items-center mb-6 sm:mb-8 border-b border-[#EBE6DD] pb-4 sm:pb-6 shrink-0">
                                  <h3 className="font-serif italic text-2xl sm:text-3xl md:text-4xl text-[#2C2822] tracking-widest">
                                      {page.title}
                                  </h3>
                                  <button onClick={() => setActiveZodiacPage(prev => (prev + 1) % 5)} className="group flex items-center gap-2 font-sans font-light tracking-widest text-[#8C8377] hover:text-[#2C2822] transition-colors cursor-pointer text-[10px] sm:text-xs md:text-sm px-2 sm:px-4 py-2 uppercase">
                                      NEXT <span className="group-hover:translate-x-1 transition-transform">➔</span>
                                  </button>
                              </div>
                              
                              {/* PRECISE USER LAYOUT */}
                              <div className="w-full">
                                  <div style={{ display: 'flex', flexWrap: 'nowrap', overflowX: 'auto', paddingBottom: '16px', scrollbarWidth: 'none', msOverflowStyle: 'none' } as any} className="zodiac-scroll-container gap-4 sm:gap-6">
                                      {page.images.map((img, i) => (
                                          <div key={i} style={{ flexShrink: 0, borderRadius: '12px', overflow: 'hidden', border: '2px solid #F2EFEA', background: 'white', boxShadow: '0 8px 24px rgba(0,0,0,0.06)' }} className="h-[380px] sm:h-[450px] md:h-[580px] hover:scale-[1.02] transition-transform duration-300">
                                              <img src={img} alt="Zodiac Collection" style={{ height: '100%', width: 'auto', display: 'block' }}  />
                                          </div>
                                      ))}
                                  </div>
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

        {/* ─── 08. PAINTASO ─── */}
        <section id="paintaso" className="relative w-full py-24 bg-gradient-to-b from-[#EEF8FF] via-[#DDF3FB] to-[#BEE6F5] overflow-hidden">
           <div className="max-w-[1400px] mx-auto px-6 sm:px-10 relative z-20 flex flex-col">

              {/* 1. SECTION HEADER */}
              <div className="flex flex-col items-center mb-20 text-center">
                  <div className="px-6 py-2 border-[4px] border-white text-[#3A7FB5] rounded-full text-sm font-bold mb-6 tracking-widest uppercase bg-white/50 backdrop-blur-sm shadow-md font-['Quicksand']">
                      Event Design
                  </div>
                  <div className="relative inline-block mb-6 pb-2">
                      {/* Outline Layer */}
                      <h2 className="absolute inset-0 font-['Fredoka'] text-[60px] md:text-[90px] font-black leading-none pb-4" style={{ WebkitTextStroke: '10px #FFE885', color: '#FFE885' }} aria-hidden="true">
                          Healing Workshop
                      </h2>
                      {/* Gradient Fill Layer */}
                      <h2 className="relative font-['Fredoka'] text-[60px] md:text-[90px] font-black text-transparent bg-clip-text bg-gradient-to-b from-[#5EB8E6] to-[#2A7AA8] leading-none pb-4 z-10">
                          Healing Workshop
                      </h2>
                  </div>
                  <p className="max-w-2xl text-lg text-[#2A6090]/90 font-['Quicksand'] font-bold leading-relaxed">
                      A warm and creative visual identity designed for Paintaso's "Tô Bình Yên" painting workshop — where colors meet calm.
                  </p>
              </div>

              {/* 2. KEY VISUAL */}
              <div className="w-full mb-32 flex flex-col items-center">
                  <div className="relative inline-block mb-10">
                      <h3 className="absolute inset-0 font-['Fredoka'] text-3xl md:text-4xl font-black tracking-wide pb-2" style={{ WebkitTextStroke: '4px #FFE885', color: '#FFE885' }} aria-hidden="true">
                          Key Visual
                      </h3>
                      <h3 className="relative font-['Fredoka'] text-3xl md:text-4xl font-black tracking-wide text-transparent bg-clip-text bg-gradient-to-b from-[#5EB8E6] to-[#2A7AA8] pb-2 z-10">
                          Key Visual
                      </h3>
                  </div>
                  <div className="relative w-full max-w-5xl rounded-[32px] overflow-hidden border-[4px] border-white shadow-[0_20px_50px_rgba(58,127,181,0.2)] group">
                      <img  src="/assets/portfolio_assets/PAINTASO/KEY%20VISUAL/COVER.jpg" alt="Paintaso Key Visual" className="w-full h-auto block group-hover:scale-105 transition-transform duration-700" />
                  </div>
                  {/* Avatar Badge */}
                  <div className="relative -mt-20 w-32 h-32 md:w-44 md:h-44 rounded-full p-1 bg-white shadow-xl z-10 group hover:-translate-y-2 transition-transform duration-300">
                      <div className="w-full h-full rounded-full overflow-hidden bg-[#D0EEFA]">
                          <img  src="/assets/portfolio_assets/PAINTASO/KEY%20VISUAL/AVATAR.jpg" alt="Paintaso Avatar" className="w-full h-full object-cover" />
                      </div>
                  </div>
              </div>

              {/* 3. PRINT & EVENT APPLICATIONS — side by side, equal height */}
              <div className="w-full mb-32">
                  <div className="relative inline-block mb-10 text-center w-full flex justify-center">
                      <div className="relative inline-block">
                          <h3 className="absolute inset-0 font-['Fredoka'] text-3xl md:text-4xl font-black tracking-wide pb-2" style={{ WebkitTextStroke: '4px #FFE885', color: '#FFE885' }} aria-hidden="true">
                              Print &amp; Event Applications
                          </h3>
                          <h3 className="relative font-['Fredoka'] text-3xl md:text-4xl font-black tracking-wide text-transparent bg-clip-text bg-gradient-to-b from-[#5EB8E6] to-[#2A7AA8] pb-2 z-10">
                              Print &amp; Event Applications
                          </h3>
                      </div>
                  </div>
                  <div className="flex flex-row flex-wrap gap-8 justify-center items-start">
                      {/* Flyer — portrait, sets the reference height */}
                      <div className="flex flex-col items-center gap-4">
                          <div className="rounded-[24px] overflow-hidden border-[4px] border-white shadow-lg group hover:border-[#3A7FB5] transition-colors duration-300" style={{ height: '452px' }}>
                              <img  src="/assets/portfolio_assets/PAINTASO/Print%20&%20Event%20Applications/FLYER%20MỞ%20ĐƠN.jpg" alt="Flyer Mở Đơn" style={{ height: '100%', width: 'auto', display: 'block' }} className="group-hover:scale-105 transition-transform duration-500" />
                          </div>
                          <h4 className="font-['Quicksand'] font-bold text-lg text-[#3A7FB5] tracking-wider uppercase text-center bg-white/60 px-6 py-2 rounded-full shadow-sm">Flyer Mở Đơn</h4>
                      </div>
                      {/* Template Story — same height, border hugs naturally */}
                      <div className="flex flex-col items-center gap-4">
                          <div className="rounded-[24px] overflow-hidden border-[4px] border-white shadow-lg group hover:border-[#3A7FB5] transition-colors duration-300" style={{ height: '452px' }}>
                              <img  src="/assets/portfolio_assets/PAINTASO/Print%20&%20Event%20Applications/TEMPLATES%20STORY.jpg" alt="Templates Story" style={{ height: '100%', width: 'auto', display: 'block' }} className="group-hover:scale-105 transition-transform duration-500" />
                          </div>
                          <h4 className="font-['Quicksand'] font-bold text-lg text-[#3A7FB5] tracking-wider uppercase text-center bg-white/60 px-6 py-2 rounded-full shadow-sm">Templates Story</h4>
                      </div>
                  </div>
              </div>

              {/* 4. SOCIAL POSTS — Masonry layout (same as Chinese Debate 2026) */}
              <div className="w-full mb-10">
                  <div className="relative inline-block mb-10 text-center w-full flex justify-center">
                      <div className="relative inline-block">
                          <h3 className="absolute inset-0 font-['Fredoka'] text-3xl md:text-4xl font-black tracking-wide pb-2" style={{ WebkitTextStroke: '4px #FFE885', color: '#FFE885' }} aria-hidden="true">
                              Social Media Posts
                          </h3>
                          <h3 className="relative font-['Fredoka'] text-3xl md:text-4xl font-black tracking-wide text-transparent bg-clip-text bg-gradient-to-b from-[#5EB8E6] to-[#2A7AA8] pb-2 z-10">
                              Social Media Posts
                          </h3>
                      </div>
                  </div>
                  <div className="columns-1 md:columns-2 gap-6 w-full max-w-4xl mx-auto">
                      {/* Video block restored */}
                      <div className="relative rounded-[20px] overflow-hidden border-[4px] border-white group shadow-lg break-inside-avoid mb-6 inline-block w-full" style={{ lineHeight: 0 }}>
                          <video src="/assets/portfolio_assets/PAINTASO/SOCIAL%20POSTS/SOCIAL%20POST%20(GIF)%20AI%20SẼ%20ĐI%20CÙNG%20BẠN%20ĐẾN%20WORKSHOP.mov" autoPlay muted loop playsInline style={{ width: '100%', display: 'block' }} />
                      </div>
                      {/* Image posts */}
                      {[
                          "SOCIAL POST GIỚI THIỆU SẢN PHẨM.jpg",
                          "SOCIAL POST MỤC ĐÍCH WORKSHOP_.jpg",
                          "SOCIAL POST QUYỀN LỢI KHI THAM GIA WORKSHOP.jpg",
                      ].map((filename, idx) => (
                          <div key={idx} className="relative rounded-[20px] overflow-hidden border-[4px] border-white group hover:border-[#3A7FB5] transition-colors duration-300 shadow-md break-inside-avoid mb-6 inline-block w-full" style={{ lineHeight: 0 }}>
                              <img src={`/assets/portfolio_assets/PAINTASO/SOCIAL%20POSTS/${filename}`} alt={filename.replace('.jpg', '')} style={{ width: '100%', display: 'block' }}  className="group-hover:scale-105 transition-transform duration-500" />
                          </div>
                      ))}
                  </div>
              </div>

           
           </div>
           
           {/* Wavy Divider Transition to Footer */}
           <div className="absolute bottom-0 left-0 w-full overflow-hidden leading-[0] z-0">
               <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320" className="w-full h-16 sm:h-24 md:h-32 block" preserveAspectRatio="none">
                   <path fill="#FAF4E1" fillOpacity="1" d="M0,224L48,213.3C96,203,192,181,288,186.7C384,192,480,224,576,213.3C672,203,768,149,864,138.7C960,128,1056,160,1152,176C1248,192,1344,192,1392,192L1440,192L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path>
               </svg>
           </div>
        </section>


        {/* ─── HERO SECTION ─── */}
        <footer id="contact" className="relative w-full min-h-screen flex flex-col items-center justify-center pt-24 pb-32 z-10 bg-[#FAF4E1] overflow-hidden">
          
          <div className="absolute bottom-[-5%] left-[-5%] w-[50%] h-[70%] bg-halftone-large opacity-[0.25] z-0" style={{clipPath: 'circle(50% at 20% 80%)'}}></div>
          <div className="absolute top-[-5%] right-[-5%] w-[50%] h-[60%] bg-halftone-large opacity-[0.25] z-0" style={{clipPath: 'circle(50% at 80% 20%)'}}></div>

          <div className="relative z-30 inline-flex flex-col items-center mt-12 group/folder transform -rotate-[8deg] skew-x-[-2deg]">
             
             {/* Back folder */}
             <div className={`absolute inset-0 bg-gradient-to-b from-[#F6B578] to-[#F1934B] rounded-[24px] md:rounded-[30px] border-[6px] border-white translate-x-6 md:translate-x-8 -translate-y-6 md:-translate-y-8 group-hover/folder:translate-x-12 group-hover/folder:-translate-y-12 group-hover/folder:rotate-[2deg] transition-transform duration-700 ease-[cubic-bezier(0.34,1.56,0.64,1)] opacity-0 ${entered ? 'animate-layer-up delay-100' : ''}`}>
                 <div className="absolute inset-0 rounded-[20px] overflow-hidden pointer-events-none">
                     </div>
                 
                 <div className="absolute -top-[45px] left-[-2px] w-[45%] h-[50px] flex z-10">
                     <div className="w-[80%] bg-[#F6B578] border-[6px] border-white border-b-0 border-r-0 rounded-tl-[24px]"></div>
                     <div className="flex-1 bg-[#F6B578] border-[6px] border-white border-b-0 border-l-0 origin-bottom-left skew-x-[35deg] rounded-tr-[16px] -ml-[6px]"></div>
                 </div>
             </div>

             {/* 
                Front folder 
                FIX: Increased padding-top/bottom to py-20 md:py-32.
                This makes the folder taller, giving horizontal elements MUCH more room to spread vertically.
             */}
             <div className={`relative bg-[#FFF0CA] rounded-[24px] md:rounded-[30px] border-[6px] md:border-[8px] border-white shadow-[0_15px_40px_rgba(0,0,0,0.06)] px-16 md:px-32 py-16 md:py-24 flex items-center justify-center transition-all duration-700 ease-[cubic-bezier(0.34,1.56,0.64,1)] group-hover/folder:-translate-y-2 group-hover/folder:shadow-[0_25px_50px_rgba(0,0,0,0.1)] opacity-0 ${entered ? 'animate-layer-up delay-300' : ''}`}>
                
                <div className="absolute inset-0 rounded-[18px] md:rounded-[24px] overflow-hidden pointer-events-none">
                   <div className="absolute inset-0 opacity-[0.03] mix-blend-multiply" style={{ backgroundImage: 'radial-gradient(#000 1.5px, transparent 1.5px)', backgroundSize: '12px 12px' }}></div>
                </div>

                {/* Grouped Text + Contact Box */}
                <div className={`opacity-0 ${entered ? 'animate-sticker-pop delay-600' : ''} relative z-30 flex flex-col items-start w-full transform rotate-0 mb-4 md:mb-8`}>
                   
                   {/* Thankyou Text & CTA Button */}
                   <div className="relative transform rotate-0 mb-2 md:mb-4 pb-4 md:pb-8 inline-block w-max">
                      <h2 className="text-[100px] sm:text-[130px] md:text-[150px] font-['Fredoka'] font-black leading-none text-left text-3d-portfolio transition-transform duration-500 hover:scale-[1.02]" style={{ letterSpacing: '0.01em' }}>
                         Thankyou
                      </h2>

                      {/* CTA Button (Centered exactly under Thankyou) */}
                      <div className="absolute transform rotate-0 z-40 -bottom-[50px] md:-bottom-[60px] left-1/2 -translate-x-1/2 inline-block w-max">
                         <a href="#profile" className="group flex items-center justify-center bg-[#F1934B] hover:bg-[#E8704A] text-white px-10 py-2 md:px-14 md:py-3 rounded-full shadow-[0_10px_25px_rgba(241,147,75,0.3)] transition-all duration-300 hover:scale-105 border-[4px] border-white cursor-pointer">
                            <span className="font-['Fredoka'] font-bold text-2xl md:text-3xl tracking-wide drop-shadow-sm">Contact me</span>
                         </a>

                         {/* Orange Cursor Arrow (Pinned to bottom-left of CTA) */}
                         <div className="absolute -bottom-[30px] -left-[30px] rotate-[45deg] z-50 animate-float cursor-pointer hover:rotate-[35deg] hover:scale-110 transition-transform">
                            <svg width="70" height="70" viewBox="0 0 100 100" className="drop-shadow-md">
                               <path d="M 25 15 L 25 80 L 45 60 L 65 90 L 80 80 L 60 50 L 90 50 Z" fill="#FFE885" stroke="#F1934B" strokeWidth="6" strokeLinejoin="round"/>
                            </svg>
                         </div>
                      </div>
                   </div>
                </div>

                {/* ─── STICKERS (FIX: NO WHITE BORDERS, EXACT POSITIONS) ─── */}
                
                {/* 1. Yellow Asterisk - Pushed out further left */}
                <div className={`absolute -left-[50px] md:-left-[80px] top-[25%] z-20 opacity-0 ${entered ? 'animate-sticker-pop delay-800' : ''} scale-65 md:scale-100`}>
                   <div className="animate-float-delayed hover:scale-125 transition-transform duration-500 cursor-pointer">
                      <svg width="80" height="80" viewBox="0 0 100 100" className="drop-shadow-md">
                        <g fill="none" stroke="#F9DB82" strokeWidth="12" strokeLinecap="round" strokeLinejoin="round">
                           <path d="M 50 15 L 50 85" />
                           <path d="M 20 35 L 80 65" />
                           <path d="M 20 65 L 80 35" />
                        </g>
                      </svg>
                   </div>
                </div>


                {/* 3. Clover Stamp - Right Edge */}
                <div className={`absolute -right-[20px] md:-right-[40px] -bottom-[40px] md:-bottom-[50px] rotate-[5deg] z-40 opacity-0 ${entered ? 'animate-sticker-pop delay-1200' : ''} scale-65 md:scale-100`}>
                   <div className="relative w-[90px] h-[110px] md:w-[110px] md:h-[130px] flex items-center justify-center animate-float hover:scale-110 transition-transform cursor-pointer">
                      <div className="absolute inset-0 bg-white stamp-mask shadow-[0_10px_20px_rgba(0,0,0,0.1)]"></div>
                      <div className="absolute inset-[10px] border-[1.5px] border-[#EEE] z-10 pointer-events-none rounded-[4px]"></div>

                      <svg className="absolute -top-3 -left-3 z-50 drop-shadow-sm" width="35" height="35" viewBox="0 0 100 100">
                         <path d="M50 50 C20 10 0 40 50 50 C80 10 100 40 50 50" fill="none" stroke="#E8704A" strokeWidth="6" strokeLinecap="round"/>
                         <path d="M50 50 L25 85 M50 50 L75 85" stroke="#E8704A" strokeWidth="6" strokeLinecap="round"/>
                         <circle cx="50" cy="50" r="5" fill="#E8704A"/>
                      </svg>
                         
                      <svg width="65" height="65" viewBox="0 0 100 100" className="relative z-20 drop-shadow-sm ml-2 mt-2">
                         <g fill="#89B66B">
                           <circle cx="35" cy="35" r="16"/>
                           <circle cx="65" cy="35" r="16"/>
                           <circle cx="35" cy="65" r="16"/>
                           <circle cx="65" cy="65" r="16"/>
                           <rect x="35" y="35" width="30" height="30" />
                         </g>
                         <circle cx="45" cy="48" r="3" fill="white"/>
                         <circle cx="55" cy="48" r="3" fill="white"/>
                         <path d="M45 54 Q50 60 55 54" fill="none" stroke="white" strokeWidth="3" strokeLinecap="round"/>
                      </svg>
                   </div>
                </div>

                {/* 4. Ai Puffy Star - Top Right */}
                <div className={`absolute right-[-20px] md:right-[5%] -top-[30px] md:-top-[40px] rotate-[15deg] z-40 opacity-0 ${entered ? 'animate-sticker-pop delay-800' : ''} scale-65 md:scale-100`}>
                   <div className="animate-float hover:scale-110 transition-transform cursor-pointer">
                      <svg width="80" height="80" viewBox="0 0 100 100" className="drop-shadow-md">
                         <polygon points="50,15 61,38 86,41 68,58 74,84 50,70 26,84 32,58 14,41 39,38" fill="#F1934B" stroke="none"/>
                         <text x="50" y="55" fontFamily="'Fredoka', sans-serif" fontSize="34" fill="white" fontWeight="900" textAnchor="middle" dominantBaseline="middle">Ai</text>
                      </svg>
                   </div>
                </div>

                {/* 5. Leaf Blob - Spread to top 15% */}
                <div className={`absolute -right-[40px] md:-right-[60px] top-[15%] rotate-[15deg] z-20 opacity-0 ${entered ? 'animate-sticker-pop delay-900' : ''} scale-65 md:scale-100`}>
                   <div className="animate-float-delayed hover:scale-110 transition-transform cursor-pointer">
                      <svg width="75" height="75" viewBox="0 0 100 100" className="drop-shadow-md">
                         <polygon points="50,10 65,30 90,30 75,50 85,75 50,65 15,75 25,50 10,30 35,30" fill="#74A352" stroke="none"/>
                         <path d="M 30 70 C 20 45, 45 30, 70 30 C 50 25, 25 50, 30 70 Z" fill="none" stroke="white" strokeWidth="4" strokeLinecap="round"/>
                      </svg>
                   </div>
                </div>

                {/* 6. Figma Logo - Right side */}
                <div className={`absolute -right-[30px] md:-right-[50px] top-[45%] rotate-[10deg] z-30 opacity-0 ${entered ? 'animate-sticker-pop delay-1000' : ''} scale-65 md:scale-100`}>
                   <div className="animate-float hover:scale-110 transition-transform cursor-pointer">
                      <svg width="75" height="75" viewBox="0 0 100 100" className="drop-shadow-md">
                         <circle cx="50" cy="50" r="40" fill="#FFE885" stroke="#89B66B" strokeWidth="4"/>
                         <g transform="translate(50, 50) scale(1.1) translate(-50, -50)">
                            <circle cx="42" cy="34" r="7" fill="none" stroke="#89B66B" strokeWidth="3"/>
                            <circle cx="58" cy="34" r="7" fill="none" stroke="#89B66B" strokeWidth="3"/>
                            <circle cx="42" cy="50" r="7" fill="none" stroke="#89B66B" strokeWidth="3"/>
                            <circle cx="58" cy="50" r="7" fill="none" stroke="#89B66B" strokeWidth="3"/>
                            <path d="M 42 66 C 42 56, 50 56, 50 66 C 50 76, 42 76, 42 66 Z" fill="none" stroke="#89B66B" strokeWidth="3"/>
                         </g>
                      </svg>
                   </div>
                </div>


                {/* 8. Ps Sticker - Bottom Left edge */}
                <div className={`absolute -left-[40px] md:-left-[60px] bottom-[25%] md:bottom-[30%] rotate-[-15deg] z-40 opacity-0 ${entered ? 'animate-sticker-pop delay-1200' : ''} scale-65 md:scale-100`}>
                   <div className="animate-float hover:scale-110 transition-transform cursor-pointer">
                      <svg width="80" height="80" viewBox="0 0 100 100" className="drop-shadow-md">
                         <circle cx="50" cy="50" r="40" fill="#74A352" stroke="none"/>
                         <text x="50" y="55" fontFamily="'Fredoka', sans-serif" fontSize="36" fill="white" fontWeight="900" textAnchor="middle" dominantBaseline="middle">Ps</text>
                      </svg>
                   </div>
                </div>
                
             </div>
          </div>
        </footer>
      </div>
    </main>
  );
}
