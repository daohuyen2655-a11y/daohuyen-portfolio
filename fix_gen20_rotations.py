import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the interval to 5000ms
content = content.replace("}, 3000);", "}, 5000);")

# 2. Extract Gen 20 Section and remove all rotations
start_marker = "{/* ─── 03. GEN 20 RECRUITMENT ─── */}"
end_marker = "{/* ─── 04. 19TH BIRTHDAY ─── */}"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    gen20_code = content[start_idx:end_idx]
    
    # Remove all instances of rotate-[-Xdeg] and rotate-[Xdeg]
    gen20_code = re.sub(r'\brotate-\[.*?\]\s*', '', gen20_code)
    
    content = content[:start_idx] + gen20_code + content[end_idx:]
    
    with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS")
else:
    print("FAILED TO FIND MARKERS")

