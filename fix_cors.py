import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace fetch in portfolio.html
old_fetch = "fetch('assets/portfolio-data.json').then(r=>r.json()).then(data => {"
new_fetch = "const data = window.PORTFOLIO_DATA; if(data) {"
html = html.replace(old_fetch, new_fetch)

# Add <script src="scripts/data.js"> if not present
if '<script src="scripts/data.js"></script>' not in html:
    html = html.replace('<script src="scripts/motion.js"></script>', '<script src="scripts/data.js"></script>\n  <script src="scripts/motion.js"></script>')

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated portfolio.html")

with open('project.html', 'r', encoding='utf-8') as f:
    html2 = f.read()

html2 = html2.replace("fetch('assets/portfolio-data.json').then(r=>r.json()).then(data => {", "const data = window.PORTFOLIO_DATA; if(data) {")

if '<script src="scripts/data.js"></script>' not in html2:
    html2 = html2.replace('<script src="scripts/motion.js"></script>', '<script src="scripts/data.js"></script>\n  <script src="scripts/motion.js"></script>')

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html2)
print("Updated project.html")
