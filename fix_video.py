import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace return statement to conditionally add full-width
old_return = "return `<div class=\"masonry-item ${isComic ? 'comic-item' : ''}\">${el}${captionHtml}</div>`;"
new_return = "const fwClass = (isYouTube || isVideo || isPDF) ? 'full-width' : '';\n        return `<div class=\"masonry-item ${isComic ? 'comic-item' : ''} ${fwClass}\">${el}${captionHtml}</div>`;"
html = html.replace(old_return, new_return)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed full-width wrapper correctly")
