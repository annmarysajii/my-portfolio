import re

with open('jasmine_reader.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('max-width:480px;', 'max-width:800px;')

with open('jasmine_reader.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated max-width in jasmine_reader.html")
