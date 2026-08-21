import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the title and tools styling in the script block
old_header = """      main.innerHTML = `
      <header class="ph-header">
          ${badges ? `<div class="ph-badges">${badges}</div>` : ''}
          <h1 class="ph-title">${p.name}</h1>
          <p class="ph-desc">${p.role}</p>
          ${tools ? `<div class="card-tools" style="margin-top:1.5rem;">${tools}</div>` : ''}
      </header>"""

new_header = """      main.innerHTML = `
      <header class="ph-header">
          ${badges ? `<div class="ph-badges">${badges}</div>` : ''}
          <h1 class="ph-title">${p.title}</h1>
          <p class="ph-desc">${p.role}</p>
          ${tools ? `<div class="card-tools" style="margin-top:1.5rem; display:flex; flex-wrap:wrap; gap:0.5rem;">${tools}</div>` : ''}
      </header>"""

html = html.replace(old_header, new_header)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed project.html header (title and tool gaps)")
