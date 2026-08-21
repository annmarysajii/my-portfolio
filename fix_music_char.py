import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace corrupted music character with proper unicode
html = html.replace("ctx.fillText('T', 0, 0);", "ctx.fillText('\u266A', 0, 0);")

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed music character")
