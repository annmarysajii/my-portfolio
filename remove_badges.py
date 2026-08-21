import re
with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'<div class="hero-badges">.*?</div>', '', html, flags=re.DOTALL)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Removed hero badges")
