import re
import unicodedata

with open('src/app/page.tsx', 'r') as f:
    content = f.read()

def normalize_match(match):
    original = match.group(0)
    return unicodedata.normalize('NFC', original)

# Find all src strings and normalize them to NFC
content = re.sub(r'src="[^"]+"', normalize_match, content)
content = re.sub(r'src=\{`[^`]+`\}', normalize_match, content)

with open('src/app/page.tsx', 'w') as f:
    f.write(content)
