import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace("bgX.lineWidth = 1;", "bgX.lineWidth = 2;")
html = html.replace("rgba(240,238,245,0.15)", "rgba(240,238,245,0.25)")
html = html.replace("rgba(17,16,9,0.15)", "rgba(17,16,9,0.25)")

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated graphic design mesh thickness")
