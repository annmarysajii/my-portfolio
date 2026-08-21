import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace .con with #main
html = html.replace("document.querySelector('.con')", "(document.querySelector('.con') || document.querySelector('#main'))")

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed null reference to .con in project.html")
