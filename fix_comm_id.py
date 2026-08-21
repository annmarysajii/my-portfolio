import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace("id === 'commissions'", "id === 'freelance-commissions'")

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed commissions ID")
