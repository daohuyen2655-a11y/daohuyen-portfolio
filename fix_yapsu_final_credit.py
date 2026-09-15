import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Everlab Credit to Product Brief
old_desc = """<p className="text-xl text-[#475569] leading-relaxed font-normal mb-12 max-w-lg">
                       Yapsu AI is a modern language learning app designed for individuals seeking a natural way to practice conversations with friendly AI tutors.
                    </p>"""

new_desc = """<p className="text-xl text-[#475569] leading-relaxed font-normal mb-6 max-w-lg">
                       Yapsu AI is a modern language learning app designed for individuals seeking a natural way to practice conversations with friendly AI tutors.
                    </p>
                    
                    <div className="mb-12 max-w-lg p-5 bg-white border border-gray-100 rounded-2xl shadow-sm relative overflow-hidden">
                       <div className="absolute left-0 top-0 w-1.5 h-full bg-gradient-to-b from-orange-400 to-amber-300"></div>
                       <p className="text-sm md:text-base text-[#64748b] leading-relaxed font-medium italic">
                          "I am deeply grateful to <strong className="text-orange-500 font-bold">Everlab Technology Co., Ltd.</strong> for their incredible support and resources, which empowered me to contribute my creative vision to the design of this app."
                       </p>
                    </div>"""

content = content.replace(old_desc, new_desc)

# 2. Adjust Spacing in App Design (Move title up / screens down)
content = content.replace(
    '''text-center mb-2 tracking-wide z-30 drop-shadow-sm">\n                    App Design''',
    '''text-center mb-10 tracking-wide z-30 drop-shadow-sm">\n                    App Design'''
)

content = content.replace(
    '''<div className="flex gap-[50px] transform rotate-x-[55deg] rotate-z-[-35deg] scale-[0.8] translate-y-[-20px]">''',
    '''<div className="flex gap-[50px] transform rotate-x-[55deg] rotate-z-[-35deg] scale-[0.8] translate-y-[40px]">'''
)

# 3. Move the two phones slightly up if they want them to match the new text height
content = content.replace(
    '''<div className="w-full lg:w-[55%] h-[700px] relative flex justify-center items-center perspective-[2000px]">
                    <div className="absolute top-[60px] right-[50px]''',
    '''<div className="w-full lg:w-[55%] h-[700px] relative flex justify-center items-center perspective-[2000px] -mt-10 lg:mt-0">
                    <div className="absolute top-[40px] right-[50px]'''
)
content = content.replace(
    '''<div className="absolute top-[140px] left-[50px]''',
    '''<div className="absolute top-[120px] left-[50px]'''
)


with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("SUCCESS")
