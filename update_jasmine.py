import re

with open('jasmine_comic_full.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace fonts
font_link = '<link rel="preload" as="style" href="https://api.fontshare.com/v2/css?f[]=clash-display@500,600,700&f[]=general-sans@400,500,600&display=swap" onload="this.onload=null;this.rel=\'stylesheet\'"/>'
html = re.sub(r'<link href="https://fonts.googleapis.com/css2[^>]+>', font_link, html)

# Replace variables
html = html.replace('--ink:#f3ead9;', '--ink:#F0EEF5;')
html = html.replace('--paper:#17130f;', '--paper:#0D0C11;')
html = html.replace('--paper2:#1e1a15;', '--paper2:#1A1828;')
html = html.replace('--line: rgba(243,234,217,0.14);', '--line: rgba(240,238,245,0.14);')

# Replace font-family
html = html.replace("font-family:'Work Sans', sans-serif;", "font-family:'General Sans', system-ui, sans-serif;")
html = html.replace("font-family:'Kalam', cursive;", "font-family:'Clash Display', Georgia, serif;")
html = html.replace("font-family:'Special Elite', monospace;", "font-family:'General Sans', system-ui, sans-serif; font-weight: 500;")

with open('jasmine_comic_full.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated jasmine_comic_full.html styles")
