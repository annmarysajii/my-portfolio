with open('jasmine_reader.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add Back to Portfolio button
back_btn = '<a href="index.html" style="position:fixed; top:20px; left:20px; z-index:9999; color:var(--ink); background:var(--paper); padding:10px 20px; border-radius:24px; text-decoration:none; font-weight:600; box-shadow:0 4px 16px rgba(0,0,0,0.15); font-size:14px; display:flex; align-items:center; gap:8px; border:1px solid rgba(0,0,0,0.05);">&larr; Back to Portfolio</a>'

if "&larr; Back to Portfolio" not in html:
    html = html.replace('<body>', f'<body>\n{back_btn}')

# Add lazy/async to dynamic images
html = html.replace("img.className = 'page-img';", "img.className = 'page-img';\n      img.loading = 'lazy';\n      img.decoding = 'async';")

with open('jasmine_reader.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated jasmine_reader.html!")
