import re

with open('src/app/page.tsx', 'r') as f:
    content = f.read()

# Replace plain src={`...`} with src={encodeURI(`...`)}
content = re.sub(r'src=\{`(/assets/[^`]+)`\}', r'src={encodeURI(`/assets/\1`)}', content)

# Replace plain src="..." with src={encodeURI("...")}
# Carefully match only /assets/ paths inside src=""
content = re.sub(r'src="/assets/([^"]+)"', r'src={encodeURI("/assets/\1")}', content)

# But wait, we shouldn't encodeURI twice.
# And we shouldn't break existing {encodeURI(...)}

with open('src/app/page.tsx', 'w') as f:
    f.write(content)
