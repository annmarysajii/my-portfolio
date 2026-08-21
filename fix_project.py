import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Escape the closing script tag inside the JS template string
html = html.replace('</script>\n                    `;\n                }\n              } else if (id === \'green-arrow\') {', 
                    '<\\/script>\n                    `;\n              } else if (id === \'green-arrow\') {')

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed script tag closure")
