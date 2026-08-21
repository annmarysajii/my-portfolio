import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace all occurrences of class="ph" injected in the script
html = html.replace('<div class="ph">', '<div class="ph" style="aspect-ratio:4/3;">')
# I already replaced one with min-height: 200px. Let's reset that.
html = html.replace('<div class="ph" style="min-height: 200px;">', '<div class="ph" style="aspect-ratio:4/3;">')

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
