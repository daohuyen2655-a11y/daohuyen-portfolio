import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. FIX THE ISOMETRIC GRID (APP DESIGN) TO USE THE NEW COLORFUL 16 SCREENS
# It currently uses 4 columns with old duplicate arrays like `["onboard_04.jpg", "roadmap_10.jpg"...]`
col1_new = '["12_drill_amazing.jpg", "06_roadmap_progress.jpg", "19_dark_ui.jpg", "09_drill_fill.jpg"]'
col2_new = '["05_roadmap_map.jpg", "17_blue_tutor.jpg", "14_roleplay_hint.jpg", "11_drill_repeat.jpg"]'
col3_new = '["18_boy_bill.jpg", "15_roleplay_feedback.jpg", "02_onboard_permissions.jpg", "07_roadmap_vocab.jpg"]'
col4_new = '["10_drill_matching.jpg", "13_roleplay_gradient.jpg", "03_onboard_aha.jpg", "16_roleplay_transcript.jpg"]'

# We replace the map calls in Isometric grid to point to `/assets/portfolio_assets/Yapsu AI/final_screens/`
# First, let's just regex replace the arrays.
content = re.sub(r'\{\["onboard_04\.jpg", "roadmap_10\.jpg", "roleplay_03\.jpg", "onboard_21\.jpg"\]\.map', f'{{{col1_new}.map', content)
content = re.sub(r'\{\["roleplay_15\.jpg", "onboard_09\.jpg", "roadmap_15\.jpg", "roleplay_19\.jpg"\]\.map', f'{{{col2_new}.map', content)
content = re.sub(r'\{\["roadmap_07\.jpg", "roleplay_18\.jpg", "onboard_05\.jpg", "onboard_10\.jpg"\]\.map', f'{{{col3_new}.map', content)
content = re.sub(r'\{\["onboard_27\.jpg", "roadmap_04\.jpg", "roleplay_09\.jpg", "roadmap_20\.jpg"\]\.map', f'{{{col4_new}.map', content)

# Make sure Isometric grid uses final_screens directory
content = re.sub(r'<img src={`/assets/portfolio_assets/Yapsu AI/snapshots/\$\{src\}`} className="w-full h-full object-cover" />', r'<img src={`/assets/portfolio_assets/Yapsu AI/final_screens/${src}`} className="w-full h-full object-cover" />', content)


# 2. FIX THE FLAT GRID (EXPERIENCE FLOW) TO FIX BROKEN PATHS & USE PERFECT SEQUENCE
new_flat_grid = """{[
                       // ---------------- ROW 1: ONBOARDING & ROADMAP ----------------
                       // ONBOARDING (Dark UI, Green Permissions, Boy with Bill, Blue Tutor)
                       "19_dark_ui.jpg",
                       "02_onboard_permissions.jpg",
                       "18_boy_bill.jpg",
                       "17_blue_tutor.jpg",
                       
                       // ROADMAP (Map path, Progress radar, Vocab table, Cherry blossom map)
                       "05_roadmap_map.jpg",
                       "06_roadmap_progress.jpg",
                       "07_roadmap_vocab.jpg",
                       "03_onboard_aha.jpg",
                       
                       // ---------------- ROW 2: DRILL & ROLEPLAY ----------------
                       // DRILL (Amazing Orange, Fill blank, Matching, Repeat)
                       "12_drill_amazing.jpg",
                       "09_drill_fill.jpg",
                       "10_drill_matching.jpg",
                       "11_drill_repeat.jpg",
                       
                       // ROLEPLAY (Gradient BG, Hint modal, Feedback green, Transcript)
                       "13_roleplay_gradient.jpg",
                       "14_roleplay_hint.jpg",
                       "15_roleplay_feedback.jpg",
                       "16_roleplay_transcript.jpg"
                    ].map"""

content = re.sub(r'\{\[\s*// ---------------- ROW 1.*?\]\.map', new_flat_grid, content, flags=re.DOTALL)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
