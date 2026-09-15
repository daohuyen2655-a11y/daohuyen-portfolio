import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the wrong green sign-in screen with the true Black & White one extracted from the video's end
old_flat_grid = """
                       // 6 ONBOARDING (Post-login)
                       "19_dark_ui.jpg",           // Dark UI (Imagine)
                       "03_onboard_aha.jpg",       // Japanese level
                       "z_green_reminders.jpg",    // Green reminders
                       "onboard_09.jpg",           // Blue tutor
                       "onboard_27.jpg",           // Pink cherry blossom
                       "04_onboard_signin.jpg",    // Sign in screen (Replaced as requested)"""

new_flat_grid = """
                       // 6 ONBOARDING (Post-login)
                       "19_dark_ui.jpg",           // Dark UI (Imagine)
                       "03_onboard_aha.jpg",       // Japanese level
                       "z_green_reminders.jpg",    // Green reminders
                       "onboard_09.jpg",           // Blue tutor
                       "onboard_27.jpg",           // Pink cherry blossom
                       "z_bw_signin.jpg",          // B&W Sign in screen"""

content = content.replace(old_flat_grid, new_flat_grid)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("SUCCESS")
