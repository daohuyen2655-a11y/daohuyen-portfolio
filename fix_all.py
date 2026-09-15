import re

with open('src/app/page.tsx', 'r') as f:
    content = f.read()

# 1. Fix the folder colors from yellow to light beige
content = content.replace('bg-[#FFE885] rounded-[24px]', 'bg-[#FAF4E1] rounded-[24px]')

# 2. Fix the URL encoding for src="" strings
def encode_src(match):
    original_path = match.group(1)
    # Just encode the path, don't add extra /assets
    encoded = original_path.replace(' ', '%20').replace('́', '%CC%81')
    return f'src="{encoded}"'

content = re.sub(r'src="([^"]+/assets/[^"]+)"', encode_src, content)

# 3. Fix the URL encoding for src={`...`} strings
def encode_src_template(match):
    original_path = match.group(1)
    encoded = original_path.replace(' ', '%20').replace('́', '%CC%81')
    return f'src={{`{encoded}`}}'

content = re.sub(r'src=\{`([^`]+/assets/[^`]+)`\}', encode_src_template, content)

with open('src/app/page.tsx', 'w') as f:
    f.write(content)
