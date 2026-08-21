import re

for filename in ['portfolio.html', 'index.html', 'project.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix hardcoded text colors that broke dark mode
    html = re.sub(r'color:\s*#111009;', 'color: var(--ink);', html)
    html = re.sub(r'color:\s*rgba\(17,16,9,0\.7\);', 'color: var(--ink5);', html)
    html = re.sub(r'color:\s*rgba\(17,16,9,\.7\);', 'color: var(--ink5);', html)
    
    # Fix hardcoded backgrounds
    html = re.sub(r'background-color:\s*#FFF;', 'background: var(--bg);', html)
    html = re.sub(r'background:\s*#FFF(?! !important)(?!;)', 'background: var(--bg)', html)
    
    # Fix Nav bar background
    html = html.replace('background:rgba(250,248,244,.96)', 'background:var(--bg)')
    
    # Fix body specifically if it was missed
    html = re.sub(r'body\s*{[^}]*background-color:\s*#FFF;[^}]*}', lambda m: m.group(0).replace('background-color: #FFF;', 'background: var(--bg);'), html)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

print("Restored CSS variables!")
