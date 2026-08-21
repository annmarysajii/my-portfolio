import re

def inject_lucide(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if 'unpkg.com/lucide' not in html:
        html = html.replace('</body>', '  <script src="https://unpkg.com/lucide@latest"></script>\n  <script>lucide.createIcons();</script>\n</body>')
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(html)

for f in ['index.html', 'portfolio.html', 'project.html']:
    inject_lucide(f)

print("Injected Lucide")
