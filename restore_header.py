import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_header_pattern = re.compile(r'      main\.innerHTML = `\s*<header class="ph-header">.*?</header>', re.DOTALL)

new_header = """      main.innerHTML = `
    <div class="con">
      <div class="proj-header">
        <div class="proj-disc-tag">${p.discipline}${p.context?' &bull; '+p.context:''}</div>
        <h1 class="proj-title">${p.title}</h1>
        ${p.badge ? `<div class="proj-badge">${p.badge}</div>` : ''}
        <div class="proj-meta-row">
          <span class="proj-meta-item"><strong>Year</strong> &nbsp;${p.year}</span>
          <div class="proj-meta-sep"></div>
          <span class="proj-meta-item"><strong>Role</strong> &nbsp;${p.role}</span>
        </div>
        ${p.tools && p.tools.length ? `<div class="proj-tools" style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-top:2rem;">
            ${p.tools.map(t=>`<span class="tool">${t}</span>`).join('')}
        </div>` : ''}
      </div>"""

html = old_header_pattern.sub(new_header, html)

# We also need to add a closing </div> for .con after the gallery
old_footer = """      <div class="ph-foot">
          <a href="index.html" class="ph-back">← Back to Portfolio</a>
      </div>
      `;"""
new_footer = """      <div class="ph-foot" style="margin-top: 4rem; padding-bottom: 4rem;">
          <a href="index.html" class="nav-back"><i data-lucide="arrow-left" style="width:16px; height:16px;"></i> Back to Portfolio</a>
      </div>
    </div>
      `;"""
html = html.replace(old_footer, new_footer)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Restored original project header layout and wrapped in .con")
