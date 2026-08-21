import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Delete the chip spans
html = re.sub(r'<span class="chip ch\d">.*?</span>', '', html)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Removed chips")
