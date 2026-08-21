import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the unescaped script tag and the extra closing brace
pattern = r'</script>\s*`;\s*\}\s*\}\s*else if \(id === \'green-arrow\'\) \{'
replacement = r'<\/script>\n                    `;\n              } else if (id === \'green-arrow\') {'

html = re.sub(pattern, replacement, html)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed project.html script closure with regex")
