import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

bad_css = "position:fixed;top:2.5rem;left:50%;transform:translateX(-50%);z-index:11;"
good_css = "position:fixed;top:2.5rem;left:0;width:100%;text-align:center;z-index:11;"

html = html.replace(bad_css, good_css)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed gw-header centering")
