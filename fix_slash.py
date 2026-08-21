import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace("} else if (id === \\'green-arrow\\') {", "} else if (id === 'green-arrow') {")

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed backslash")
