import re
with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

pattern = r"\} else if \(id === 'wellbeing-planner'\) \{[^\}]*?\} else if \(id === 'original-tracks'\) \{"

matches = list(re.finditer(pattern, html, flags=re.DOTALL))
if len(matches) == 2:
    # Replace the SECOND match back to just original-tracks
    m = matches[1]
    html = html[:m.start()] + "} else if (id === 'original-tracks') {" + html[m.end():]

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Removed second accidental injection")
