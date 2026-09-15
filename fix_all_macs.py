import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = "{/* ─── 07. ZODIAC ─── */}"
end_marker = "{/* ─── 08. PAINTASO ─── */}"
start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    zodiac_section = content[start_idx:end_idx]
    
    # We replace the entire Invisible Scrollbar Content block
    block_start = zodiac_section.find("{/* Invisible Scrollbar Content */}")
    if block_start == -1:
        block_start = zodiac_section.find("{/* Invisible Scrollbar Content")
        
    # The end of the block is just before the end of the page mapping return `</div>\n                      );`
    # Let's just use regex to replace the content of that div.
    
    # Alternatively, replace the entire map block
    map_start_str = "{js_array_str}.map((page, idx) => {"
    # I'll just rewrite the whole section to be absolutely safe.
