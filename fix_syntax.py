with open('src/app/page.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the invalid JSX comments
content = content.replace("{/* Mác 1 & 3: 2 Rows, Left-Aligned, Fully Visible (Small size) */}", "")
content = content.replace("{/* Mác 2, 4, 5: Small size, Horizontal Scroll */}", "")

with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("SUCCESS")
