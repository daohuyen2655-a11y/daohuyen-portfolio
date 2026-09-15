import re
import unicodedata

with open('src/app/page.tsx', 'r') as f:
    content = f.read()

# 1. Fix folder color
content = content.replace('bg-[#FFE885] rounded-[24px]', 'bg-[#FFF0CA] rounded-[24px]')

# 2. Normalize all Vietnamese NFD strings in the file to NFC!
# This is crucial because Mac uses NFD but git/Linux uses NFC.
content = unicodedata.normalize('NFC', content)

with open('src/app/page.tsx', 'w') as f:
    f.write(content)
