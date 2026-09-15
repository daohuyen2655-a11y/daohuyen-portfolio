import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace the 16-item array in App Design
old_array_str = """[
                       // Row 1 (8 completely distinct screens)
                       "onboard_15.jpg",   // Green Splash
                       "roleplay_19.jpg",  // Dark Chat Dense
                       "onboard_09.jpg",   // Blue boy
                       "roadmap_04.jpg",   // White clean map
                       "roleplay_03.jpg",  // Avatar selection cards
                       "onboard_10.jpg",   // Orange bill boy
                       "roadmap_07.jpg",   // Drill completion (green accents)
                       "onboard_21.jpg",   // Orange header setup
                       
                       // Row 2 (8 completely distinct screens)
                       "onboard_05.jpg",   // Green mascot greeting
                       "roleplay_15.jpg",  // Feedback modal
                       "roadmap_20.jpg",   // Map alt
                       "roleplay_05.jpg",  // Tutor list
                       "onboard_27.jpg",   // Settings options
                       "roleplay_18.jpg",  // Light chat
                       "roadmap_15.jpg",   // Detailed list
                       "onboard_04.jpg"    // Clean white list
                    ]"""

new_array_str = """[
                       // Row 1
                       "onboard_15.jpg",   // Boy with bill
                       "roleplay_19.jpg",  // Radar chart
                       "onboard_09.jpg",   // Blue mascot/girl
                       "roadmap_04.jpg",   // White table
                       "roleplay_03.jpg",  // Chat modal keyboard
                       "onboard_30.jpg",   // NEW 1
                       "roadmap_07.jpg",   // Drill icons
                       "onboard_21.jpg",   // Dark people
                       
                       // Row 2
                       "roleplay_20.jpg",  // NEW 2
                       "roleplay_15.jpg",  // White chat green bubble
                       "onboard_02.jpg",   // NEW 3
                       "roadmap_03.jpg",   // NEW 4
                       "onboard_27.jpg",   // Peach cherry blossom
                       "roadmap_08.jpg",   // NEW 5
                       "roadmap_15.jpg",   // Matching pairs
                       "onboard_04.jpg"    // Language list
                    ]"""

if old_array_str in content:
    content = content.replace(old_array_str, new_array_str)
else:
    # Use regex if exact string match fails due to formatting
    pattern = re.compile(r'\[\s*// Row 1.*?"onboard_04\.jpg"\s*// Clean white list\s*\]', re.DOTALL)
    content = re.sub(pattern, new_array_str, content)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
