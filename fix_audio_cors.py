import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove crossorigin to prevent CORS errors on file:// or local testing
html = html.replace('<audio id="main-audio" crossorigin="anonymous"></audio>', '<audio id="main-audio"></audio>')

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Removed crossorigin")
