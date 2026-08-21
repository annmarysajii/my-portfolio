import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('a.innerHTML = `<div class="ph">', 'a.innerHTML = `<div class="ph" style="min-height: 200px;">')

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
