import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'<button class="music-toggle pill-toggle".*?</button>', '', html)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Removed from project.html")
