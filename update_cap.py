import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_cap = "const captionHtml = (isYouTube || isPDF || isAudio || isComic) ? '' : `<div class=\"media-caption\">${name}</div>`;"
new_cap = "const captionHtml = (isYouTube || isPDF || isAudio || isComic || id === 'commissions') ? '' : `<div class=\"media-caption\">${name}</div>`;"

html = html.replace(old_cap, new_cap)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Removed commission labels")
