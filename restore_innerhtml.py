import re
with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Restore the accidentally deleted assignment
html = html.replace(
    "} else if (id === 'nangele') {",
    "}\n                  gal.innerHTML = htmlStr;\n                  \n                  if (id === 'nangele') {"
)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Restored gal.innerHTML assignment!")
