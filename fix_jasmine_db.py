import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace 'jasmine': { ... } with 'jasmine-visdev' and 'jasmine-comic'
jasmine_old = r"'jasmine':\{.*?\}(?=,\s*'[a-z\-]+':\{)"
match = re.search(jasmine_old, html, flags=re.DOTALL)
if match:
    j_text = match.group(0)
    j_visdev = j_text.replace("'jasmine':{", "'jasmine-visdev':{")
    j_visdev = j_visdev.replace("discipline:'Animation, Comics'", "discipline:'Animation'")
    j_visdev = j_visdev.replace("title:'Jasmine'", "title:'Jasmine (Visual Development)'")
    
    j_comic = j_text.replace("'jasmine':{", "'jasmine-comic':{")
    j_comic = j_comic.replace("discipline:'Animation, Comics'", "discipline:'Comics'")
    j_comic = j_comic.replace("title:'Jasmine'", "title:'Jasmine (Comic Full)'")
    
    html = html.replace(j_text, j_visdev + ",\n  " + j_comic)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated project.html database keys")
