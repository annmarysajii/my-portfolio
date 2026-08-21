import re
with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

pattern = r"\} else if \(id === 'ntu-fest'\) \{[\s\S]*?\} else if \(id === 'ntu-fest'\) \{"
html = re.sub(pattern, "} else if (id === 'ntu-fest') {", html, count=1)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Removed duplicate NTU Fest block!")
