import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the even background
html = html.replace('.sec:nth-child(even){background:var(--surf);}', '/* .sec:nth-child(even) background removed to reveal canvas */')

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Removed opaque background from even sections")
