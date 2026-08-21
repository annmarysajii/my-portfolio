import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the missing </script> tag
old_str = "    }, 50);\n  }\n\n\n  <script src=\"scripts/data.js\">"
new_str = "    }, 50);\n  }\n</script>\n\n  <script src=\"scripts/data.js\">"

html = html.replace(old_str, new_str)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Restored missing </script> tag in project.html")
