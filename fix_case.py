import re
import os
import urllib.parse

def find_file_ignore_case(path):
    parts = path.strip('/').split('/')
    current = 'public'
    for part in parts:
        if part == 'public': continue
        
        # Decode url encoded spaces if any
        part = urllib.parse.unquote(part)
        
        try:
            entries = os.listdir(current)
        except OSError:
            return None
            
        found = False
        for entry in entries:
            if entry.lower() == part.lower():
                current = os.path.join(current, entry)
                found = True
                break
        if not found:
            return None
    return current.replace('public', '', 1)

with open('src/app/page.tsx', 'r') as f:
    content = f.read()

# Replace bg-[#FFE885] with bg-[#FAF4E1] for the folder fronts (hero and footer)
content = content.replace('bg-[#FFE885] rounded-[24px]', 'bg-[#FAF4E1] rounded-[24px]')

# Find all src strings
# Looking for src="...", src={'...'}, src={`...`}
# But since some are template literals, it's safer to just find all /assets/...
paths = re.findall(r'(/assets/[a-zA-Z0-9_/% \.\-\+áàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵĐđ]+)', content)
paths = list(set(paths))

for p in paths:
    # Skip if it contains variables like ${}
    if '${' in p:
        continue
        
    actual_path = find_file_ignore_case(p)
    if actual_path and actual_path != p:
        print(f"Fixing casing: {p} -> {actual_path}")
        content = content.replace(p, actual_path)

with open('src/app/page.tsx', 'w') as f:
    f.write(content)
