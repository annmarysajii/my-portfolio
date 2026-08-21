import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

pattern = r'<div style="width:100%; aspect-ratio:1; background: linear-gradient.*?</div>'
replacement = """<div style="width:100%; aspect-ratio:1; background: var(--surf); display:flex; align-items:center; justify-content:center; overflow:hidden; border-bottom: 1px solid var(--line);">
                <div style="width:65%; height:65%; border-radius:50%; background: #111; position:relative; display:flex; align-items:center; justify-content:center; box-shadow: 2px 4px 12px rgba(0,0,0,0.15);">
                  <div style="position:absolute; inset:8%; border-radius:50%; border:1px solid #222;"></div>
                  <div style="position:absolute; inset:16%; border-radius:50%; border:1px solid #222;"></div>
                  <div style="position:absolute; inset:24%; border-radius:50%; border:1px solid #222;"></div>
                  <div style="width:33%; height:33%; border-radius:50%; background:#D02F5A; display:flex; align-items:center; justify-content:center;">
                    <div style="width:12%; height:12%; border-radius:50%; background:var(--surf);"></div>
                  </div>
                </div>
              </div>"""

html = re.sub(pattern, replacement, html, flags=re.DOTALL)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Regex replace audio player inner")
