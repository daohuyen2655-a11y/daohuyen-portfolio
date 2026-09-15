import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure all images point to snapshots/ so there's no path confusion
content = content.replace('final_screens/', 'snapshots/')

# 1. Update App Design Isometric Grid
col1_new = '["z_orange_amazing.jpg", "onboard_04.jpg", "onboard_21.jpg", "roadmap_15.jpg"]'
col2_new = '["z_green_splash.jpg", "onboard_15.jpg", "roleplay_03.jpg", "z_orange_halfway.jpg"]'
col3_new = '["z_green_reminders.jpg", "roadmap_07.jpg", "roleplay_15.jpg", "onboard_09.jpg"]'
col4_new = '["roadmap_04.jpg", "onboard_27.jpg", "roadmap_20.jpg", "roleplay_19.jpg"]'

content = re.sub(r'\{\["12_drill_amazing\.jpg"[^\}]+\}\.map', f'{{{col1_new}.map', content)
content = re.sub(r'\{\["05_roadmap_map\.jpg"[^\}]+\}\.map', f'{{{col2_new}.map', content)
content = re.sub(r'\{\["18_boy_bill\.jpg"[^\}]+\}\.map', f'{{{col3_new}.map', content)
content = re.sub(r'\{\["10_drill_matching\.jpg"[^\}]+\}\.map', f'{{{col4_new}.map', content)


# 2. Update Experience Flow Flat Grid
new_flat_grid = """{[
                       // ---------------- ROW 1: ONBOARDING & ROADMAP ----------------
                       // ONBOARDING
                       "z_green_splash.jpg",
                       "onboard_04.jpg",
                       "z_green_reminders.jpg",
                       "onboard_21.jpg",
                       
                       // ROADMAP
                       "roadmap_07.jpg",
                       "roadmap_04.jpg",
                       "onboard_15.jpg",
                       "onboard_27.jpg",
                       
                       // ---------------- ROW 2: DRILL & ROLEPLAY ----------------
                       // DRILL
                       "z_orange_halfway.jpg",
                       "roadmap_15.jpg",
                       "z_orange_amazing.jpg",
                       "roleplay_19.jpg",
                       
                       // ROLEPLAY
                       "onboard_09.jpg",
                       "roleplay_03.jpg",
                       "roleplay_15.jpg",
                       "roadmap_20.jpg"
                    ].map"""

content = re.sub(r'\{\[\s*// ---------------- ROW 1.*?\]\.map', new_flat_grid, content, flags=re.DOTALL)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
