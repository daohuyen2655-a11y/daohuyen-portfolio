import re

with open('src/app/page.tsx', 'r') as f:
    content = f.read()

def encode_src(match):
    original_path = match.group(1)
    encoded = original_path.replace(' ', '%20').replace('́', '%CC%81')
    return f'src="{encoded}"'

content = re.sub(r'src="(/assets/[^"]+)"', encode_src, content)

def encode_src_template(match):
    original_path = match.group(1)
    encoded = original_path.replace(' ', '%20').replace('́', '%CC%81')
    return f'src={{`{encoded}`}}'

content = re.sub(r'src=\{`(/assets/[^`]+)`\}', encode_src_template, content)

with open('src/app/page.tsx', 'w') as f:
    f.write(content)
