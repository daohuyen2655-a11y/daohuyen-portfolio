import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update App Design Isometric Grid
col1_new = '["19_dark_ui.jpg", "onboard_27.jpg", "09_drill_fill.jpg", "13_roleplay_gradient.jpg"]'
col2_new = '["03_onboard_aha.jpg", "18_boy_bill.jpg", "10_drill_matching.jpg", "14_roleplay_hint.jpg"]'
col3_new = '["z_green_reminders.jpg", "05_roadmap_map.jpg", "11_drill_repeat.jpg", "15_roleplay_feedback.jpg"]'
col4_new = '["onboard_09.jpg", "roadmap_04.jpg", "z_orange_amazing.jpg", "16_roleplay_transcript.jpg"]'

# Using a simpler regex to catch the columns regardless of their current content
content = re.sub(r'\{\[.*?\]\.map\(\(src, i\) => \(\s*<div key={`iso1-\$\{i\}`}', f'{{{col1_new}.map((src, i) => (\n                                <div key={{`iso1-${{i}}`}}', content, flags=re.DOTALL)
content = re.sub(r'\{\[.*?\]\.map\(\(src, i\) => \(\s*<div key={`iso2-\$\{i\}`}', f'{{{col2_new}.map((src, i) => (\n                                <div key={{`iso2-${{i}}`}}', content, flags=re.DOTALL)
content = re.sub(r'\{\[.*?\]\.map\(\(src, i\) => \(\s*<div key={`iso3-\$\{i\}`}', f'{{{col3_new}.map((src, i) => (\n                                <div key={{`iso3-${{i}}`}}', content, flags=re.DOTALL)
content = re.sub(r'\{\[.*?\]\.map\(\(src, i\) => \(\s*<div key={`iso4-\$\{i\}`}', f'{{{col4_new}.map((src, i) => (\n                                <div key={{`iso4-${{i}}`}}', content, flags=re.DOTALL)


# 2. Update Experience Flow Flat Grid
new_flat_grid = """{[
                       // ---------------- ROW 1 (8 images) ----------------
                       // 6 ONBOARDING (Post-login)
                       "19_dark_ui.jpg",           // Dark UI (Imagine)
                       "03_onboard_aha.jpg",       // Japanese level
                       "z_green_reminders.jpg",    // Green reminders
                       "onboard_09.jpg",           // Blue tutor
                       "onboard_27.jpg",           // Pink cherry blossom
                       "18_boy_bill.jpg",          // Orange boy with bill
                       
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
                    ].map((src, i) => ("""

content = re.sub(r'\{\[\s*// ---------------- ROW 1.*?\]\.map\(\(src, i\) => \(', new_flat_grid, content, flags=re.DOTALL)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
