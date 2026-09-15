import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Yapsu AI
content = content.replace('bg-[#FCFBF9] text-[#334155]', 'bg-gradient-to-b from-[#FCFBF9] to-[#FFF3E6] text-[#334155]')

# Bridge to Chinese Debate 2026
content = content.replace('from-[#FCFBF9] to-[#06112E]', 'from-[#FFF3E6] to-[#06112E]')

# Chinese Debate 2026
content = content.replace('bg-[#06112E] text-white', 'bg-gradient-to-b from-[#06112E] to-[#0B1F4D] text-white')

# Gen 20th Recruit
content = content.replace('bg-[#EAF2E3] overflow-hidden', 'bg-gradient-to-b from-[#EAF2E3] to-[#D9EBCB] overflow-hidden')

# 19th Birthday
content = content.replace('bg-[#F4EEF7] overflow-hidden', 'bg-gradient-to-b from-[#F4EEF7] to-[#E3D5F2] overflow-hidden')

# Chinese Debate 2025
content = content.replace('bg-[#231710] overflow-hidden', 'bg-gradient-to-b from-[#231710] to-[#3D2719] overflow-hidden')

# Talkshow
content = content.replace('bg-[#E8F4F8] overflow-hidden', 'bg-gradient-to-b from-[#E8F4F8] to-[#CDE6EF] overflow-hidden')

# Zodiac
content = content.replace('bg-[#EAEBF2] overflow-hidden', 'bg-gradient-to-b from-[#EAEBF2] to-[#D4D7EB] overflow-hidden')

# Paintaso
content = content.replace('bg-[#FDF2F5] overflow-hidden', 'bg-gradient-to-b from-[#FDF2F5] to-[#FAD4DD] overflow-hidden')

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("SUCCESS")
