with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix literal newlines inside the string quotes in TOC array
content = content.replace('"Chinese\nDebate \'26"', '`Chinese\\nDebate \'26`')
content = content.replace('"Gen 20th\nRecruit"', '`Gen 20th\\nRecruit`')
content = content.replace('"19th\nBirthday"', '`19th\\nBirthday`')
content = content.replace('"Chinese\nDebate \'25"', '`Chinese\\nDebate \'25`')

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
