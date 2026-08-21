import re

for filename in ['portfolio.html', 'index.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Regex replace to force absolute colors
    html = re.sub(r'color:\s*var\(--ink\);', 'color: #111009;', html)
    html = re.sub(r'color:\s*var\(--ink5\);', 'color: rgba(17,16,9,0.7);', html)
    html = re.sub(r'color:\s*var\(--bg\);', 'color: #FFF;', html)

    # Re-inject the dark mode colors manually for awards
    if "[data-theme=\"dark\"] .awards-h" not in html:
        html = html.replace('</style>', """
[data-theme="dark"] .awards-h, [data-theme="dark"] .aw-n { color: #F0EEF5 !important; }
[data-theme="dark"] .aw-t { color: rgba(240,238,245,0.7) !important; }
[data-theme="dark"] .aw-i { color: #F0EEF5 !important; }
</style>""")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
print("Regex replace applied")
