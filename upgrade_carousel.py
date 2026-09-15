import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the hook logic
old_hook = """  const gen20CarouselRef = useRef<HTMLDivElement>(null);
  useEffect(() => {
    const interval = setInterval(() => {
       if (gen20CarouselRef.current) {
           const { scrollLeft, scrollWidth, clientWidth } = gen20CarouselRef.current;
           if (scrollLeft + clientWidth >= scrollWidth - 10) {
               gen20CarouselRef.current.scrollTo({ left: 0, behavior: 'smooth' });
           } else {
               gen20CarouselRef.current.scrollBy({ left: clientWidth * 0.7, behavior: 'smooth' });
           }
       }
    }, 3000);
    return () => clearInterval(interval);
  }, []);"""

new_hook = """  const gen20CarouselRef = useRef<HTMLDivElement>(null);
  const [activeGen20Idx, setActiveGen20Idx] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setActiveGen20Idx(prev => (prev + 1) % 4);
    }, 3000);
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
  }, [activeGen20Idx]);"""

content = content.replace(old_hook, new_hook)

# 2. Update Header Text
old_text = "Chiến dịch tuyển thành viên thường niên lớn nhất của Câu lạc bộ Tiếng Trung - Trường Đại học Ngoại thương (CC FTU)."
new_text = "The annual recruitment campaign of the Chinese Club - Foreign Trade University (CC FTU)."
content = content.replace(old_text, new_text)

# 3. Update Carousel JSX
old_carousel = """                      {/* Carousel Container */}
                      <div 
                          ref={gen20CarouselRef}
                          className="flex overflow-x-auto gap-6 snap-x snap-mandatory scroll-smooth pb-8"
                          style={{ scrollbarWidth: 'none', msOverflowStyle: 'none' }}
                      >
                          {[
                              "Q&A.png", 
                              "THÔNG BÁO KẾT QUẢ.png", 
                              "VIRAL POST.png", 
                              "Đóng đơn đăng ký.png"
                          ].map((filename, idx) => (
                              <div key={idx} className="flex-none w-[85%] md:w-[60%] lg:w-[45%] snap-center relative rounded-[24px] overflow-hidden border-[6px] border-white shadow-lg transition-transform duration-500 hover:scale-[1.02]">
                                  <img src={`/assets/portfolio_assets/CC FTU/CC FTU Gen 20 Recruitment/SOCIAL POST/${filename}`} alt={filename.replace('.png', '')} className="w-full h-auto block" />
                              </div>
                          ))}
                      </div>"""

new_carousel = """                      {/* Carousel Container */}
                      <div 
                          ref={gen20CarouselRef}
                          className="flex overflow-x-hidden gap-10 scroll-smooth pb-12 pt-6 px-10"
                          style={{ scrollbarWidth: 'none', msOverflowStyle: 'none' }}
                      >
                          {[
                              "Q&A.png", 
                              "THÔNG BÁO KẾT QUẢ.png", 
                              "VIRAL POST.png", 
                              "Đóng đơn đăng ký.png"
                          ].map((filename, idx) => (
                              <div 
                                  key={idx} 
                                  onClick={() => setActiveGen20Idx(idx)}
                                  className={`flex-none w-[80%] md:w-[50%] lg:w-[40%] cursor-pointer transition-all duration-700 ease-out relative rounded-[24px] overflow-hidden border-[6px] border-white shadow-[0_15px_40px_rgba(59,91,53,0.3)] ${
                                      activeGen20Idx === idx 
                                      ? 'opacity-100 scale-100 rotate-0 z-20' 
                                      : 'opacity-40 scale-90 blur-[3px] hover:blur-[1px] hover:opacity-70 z-10'
                                  }`}
                              >
                                  <img src={`/assets/portfolio_assets/CC FTU/CC FTU Gen 20 Recruitment/SOCIAL POST/${filename}`} alt={filename.replace('.png', '')} className="w-full h-auto block" />
                                  
                                  {/* Glassmorphism overlay for inactive state */}
                                  {activeGen20Idx !== idx && (
                                      <div className="absolute inset-0 bg-[#EAF2E3]/20 backdrop-blur-[2px]"></div>
                                  )}
                              </div>
                          ))}
                      </div>"""
content = content.replace(old_carousel, new_carousel)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("SUCCESS")
