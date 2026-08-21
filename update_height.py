import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Change video/img styles to use height:auto
html = html.replace('style="width:100%; height:100%; object-fit:contain;', 'style="width:100%; height:auto; display:block;')
html = html.replace('style="width:100%; height:100%; object-fit:cover;', 'style="width:100%; height:auto; display:block;')

# In portfolio.html, I removed aspect-ratio:4/3; from .card-img. Let's make sure img tag is height:auto
with open('portfolio.html', 'r', encoding='utf-8') as f:
    phtml = f.read()

phtml = phtml.replace('style="width:100%;height:100%;object-fit:contain;', 'style="width:100%;height:auto;object-fit:contain;')

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(phtml)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed height:auto for natural aspect ratios")
