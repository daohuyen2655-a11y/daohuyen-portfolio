import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Image Replacement (Experience Flow Row 1, Image 6)
# Locate the array and replace "18_boy_bill.jpg" with "04_onboard_signin.jpg"
old_flat_grid = """
                       // 6 ONBOARDING (Post-login)
                       "19_dark_ui.jpg",           // Dark UI (Imagine)
                       "03_onboard_aha.jpg",       // Japanese level
                       "z_green_reminders.jpg",    // Green reminders
                       "onboard_09.jpg",           // Blue tutor
                       "onboard_27.jpg",           // Pink cherry blossom
                       "18_boy_bill.jpg",          // Orange boy with bill"""

new_flat_grid = """
                       // 6 ONBOARDING (Post-login)
                       "19_dark_ui.jpg",           // Dark UI (Imagine)
                       "03_onboard_aha.jpg",       // Japanese level
                       "z_green_reminders.jpg",    // Green reminders
                       "onboard_09.jpg",           // Blue tutor
                       "onboard_27.jpg",           // Pink cherry blossom
                       "04_onboard_signin.jpg",    // Sign in screen (Replaced as requested)"""

content = content.replace(old_flat_grid, new_flat_grid)


# 2. App Design Spacing
# Title margin: mb-10 -> mb-2
content = content.replace(
    '''App Design\n                 </h3>\n                 \n                 <div className="relative w-[100vw] max-w-[100vw] h-[1000px]''',
    '''App Design\n                 </h3>\n                 \n                 <div className="relative w-[100vw] max-w-[100vw] h-[850px]'''
)
content = content.replace(
    '''text-center mb-10 tracking-wide z-30 drop-shadow-sm">\n                    App Design''',
    '''text-center mb-2 tracking-wide z-30 drop-shadow-sm">\n                    App Design'''
)

# Mask gradient & Grid translation
old_mask = '''style={{ WebkitMaskImage: 'linear-gradient(to bottom, transparent 0%, black 15%, black 85%, transparent 100%)', maskImage: 'linear-gradient(to bottom, transparent 0%, black 15%, black 85%, transparent 100%)' }}>
                    
                    <div className="absolute w-[2200px] flex justify-center items-center perspective-[2500px]">
                       <div className="flex gap-[50px] transform rotate-x-[55deg] rotate-z-[-35deg] scale-[0.8] translate-y-[100px]">'''

new_mask = '''style={{ WebkitMaskImage: 'linear-gradient(to bottom, transparent 0%, black 5%, black 95%, transparent 100%)', maskImage: 'linear-gradient(to bottom, transparent 0%, black 5%, black 95%, transparent 100%)' }}>
                    
                    <div className="absolute w-[2200px] flex justify-center items-center perspective-[2500px]">
                       <div className="flex gap-[50px] transform rotate-x-[55deg] rotate-z-[-35deg] scale-[0.8] translate-y-[-20px]">'''

content = content.replace(old_mask, new_mask)


# 3. Experience Flow -> Live Prototypes Spacing
# Experience Flow Wrapper
content = content.replace(
    '''{/* 3. EXPERIENCE FLOW - FLAT GRID */}
              <div className="w-full flex flex-col items-center mt-32 mb-48 pt-10">''',
    '''{/* 3. EXPERIENCE FLOW - FLAT GRID */}
              <div className="w-full flex flex-col items-center mt-24 mb-16 pt-0">'''
)

# Live Prototypes Wrapper
content = content.replace(
    '''{/* 4. LIVE PROTOTYPES */}
              <div className="w-full relative z-20 pb-48 pt-10 max-w-[1400px] mx-auto">''',
    '''{/* 4. LIVE PROTOTYPES */}
              <div className="w-full relative z-20 pb-20 pt-0 max-w-[1400px] mx-auto">'''
)

# Live Prototypes Title Margin
content = content.replace(
    '''Live Prototypes
                 </h3>
                 
                 <div className="flex flex-col lg:flex-row justify-center items-center gap-16 w-full mt-10">''',
    '''Live Prototypes
                 </h3>
                 
                 <div className="flex flex-col lg:flex-row justify-center items-center gap-16 w-full mt-0">'''
)
content = content.replace(
    '''text-center mb-24 tracking-wide drop-shadow-sm">\n                    Live Prototypes''',
    '''text-center mb-12 tracking-wide drop-shadow-sm">\n                    Live Prototypes'''
)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("SUCCESS")
