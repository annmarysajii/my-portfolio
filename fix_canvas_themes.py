import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace("theme === 'motion'", "theme === 'videography'")
html = html.replace("theme === 'brand'", "theme === 'graphic-design'")

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated canvas theme checks in portfolio.html")
