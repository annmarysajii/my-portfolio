import re

with open('jasmine_reader.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Change all 800px max-widths to 1200px
html = html.replace('max-width:800px;', 'max-width:1200px;')

# Change script width to 900px
html = html.replace('max-width:640px;', 'max-width:900px;')

with open('jasmine_reader.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated jasmine reader for wider web optimization")
