import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the link for jasmine-comic
html = html.replace('"project.html?id=jasmine-comic"', '"jasmine_reader.html"')

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated portfolio.html to link directly to jasmine_reader.html")
