import re
with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove target="_blank" from all project links inside portfolio.html
html = html.replace('" target="_blank" class="card-img">', '" class="card-img">')
html = html.replace('" target="_blank" class="card-img" style=', '" class="card-img" style=')

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Removed target=_blank from portfolio.html links!")
