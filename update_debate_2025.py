import re

with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Subtext
old_subtext = """"BỨT PHÁ" - The explosive academic debate arena with a fierce, burning, and breakthrough spirit hosted by the Chinese Club - Foreign Trade University (CC FTU)."""
new_subtext = """A vibrant, futuristic visual identity tailored for the Chinese Debate competition, featuring a dynamic, high-energy cyber aesthetic designed to captivate a modern youth audience."""
content = content.replace(old_subtext, new_subtext)

# 2. Update Carousel Interval from 5000 to 4000
old_effect = """setActiveDebateIdx(prev => (prev + 1) % 10);
    }, 5000);"""
new_effect = """setActiveDebateIdx(prev => (prev + 1) % 10);
    }, 4000);"""
content = content.replace(old_effect, new_effect)

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS")
