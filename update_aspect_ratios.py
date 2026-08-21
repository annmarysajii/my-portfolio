import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Change object-fit:cover to object-fit:contain for portfolio thumbnails
html = html.replace('object-fit:cover;"', 'object-fit:contain;"')
# Also remove aspect-ratio from .card-img? If we use object-fit:contain, the aspect-ratio: 4/3 provides a clean bounding box while the image fits inside.
# But wait, the user said "use the full aspect ratio of the image". Let's change aspect-ratio:4/3 to aspect-ratio:auto so it takes the image's height.
html = html.replace('aspect-ratio:4/3;', '')

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated portfolio.html image styles")

with open('project.html', 'r', encoding='utf-8') as f:
    html2 = f.read()

# Change object-fit:cover to object-fit:contain in project.html injection
html2 = html2.replace('object-fit:cover;', 'object-fit:contain;')

# Also in project.html, I used fixed grid classes: gallery-hero, gallery-row2, gallery-row3.
# We should allow images to determine height. 
html2 = html2.replace('aspect-ratio:16/9;', '')
html2 = html2.replace('aspect-ratio:4/3;', '')
html2 = html2.replace('aspect-ratio:1/1;', '')

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html2)
print("Updated project.html image styles")
