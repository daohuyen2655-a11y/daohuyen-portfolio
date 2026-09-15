import re

with open('src/app/page.tsx', 'r') as f:
    content = f.read()

# Replace spaces with %20 ONLY in the specific portfolio_assets paths!
content = content.replace('/assets/portfolio_assets/Yapsu AI/', '/assets/portfolio_assets/Yapsu%20AI/')
content = content.replace('/assets/portfolio_assets/CC FTU/', '/assets/portfolio_assets/CC%20FTU/')
content = content.replace('/assets/portfolio_assets/PAINTASO/', '/assets/portfolio_assets/PAINTASO/')
content = content.replace('/assets/portfolio_assets/ZODIAC COLLECTIONS/', '/assets/portfolio_assets/ZODIAC%20COLLECTIONS/')

# Also encode spaces in the rest of the paths if they exist
def encode_spaces(match):
    return match.group(0).replace(' ', '%20')

# Safely encode any remaining spaces inside /assets/... strings
content = re.sub(r'(/assets/[^"\'`]+)', encode_spaces, content)

with open('src/app/page.tsx', 'w') as f:
    f.write(content)
