import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix TOC entries
old_toc_19 = '{ id: "04", title: "19th Birthday", color: "#A890D8", anchor: "19th-birthday" }'
new_toc_19 = '{ id: "04", title: "19th Anniversary", color: "#A890D8", anchor: "19th-birthday" }'
content = content.replace(old_toc_19, new_toc_19)

old_toc_talkshow = '{ id: "06", title: "Talkshow", color: "#58B3D3", anchor: "talkshow" }'
new_toc_talkshow = '{ id: "06", title: "E-Com Talkshow", color: "#58B3D3", anchor: "talkshow" }'
content = content.replace(old_toc_talkshow, new_toc_talkshow)

# 2. Fix Section 06 Title
old_title = "Talkshow Livestream"
new_title = "E-Commerce Talkshow"
content = content.replace(old_title, new_title)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS")
