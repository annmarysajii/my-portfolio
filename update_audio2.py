import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_inner = """              <div style="width:100%; aspect-ratio:1; background: linear-gradient(135deg, #1850A8 0%, #D02F5A 100%); display:flex; align-items:center; justify-content:center; overflow:hidden; position:relative;">
                  <img src="assets/portfolio-data/My profile/me avatar.png" style="width:100%; height:100%; object-fit:cover; mix-blend-mode: overlay; opacity:0.8;">
                  <div style="position:absolute; inset:0; background:rgba(0,0,0,0.2);"></div>
                  <svg style="position:absolute; width:48px; height:48px; color:white; opacity:0.8;" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18V5l12-2v13"></path><circle cx="6" cy="18" r="3"></circle><circle cx="18" cy="16" r="3"></circle></svg>
              </div>"""

new_inner = """              <div style="width:100%; aspect-ratio:1; background: var(--surf); display:flex; align-items:center; justify-content:center; overflow:hidden; border-bottom: 1px solid var(--line);">
                <div style="width:65%; height:65%; border-radius:50%; background: #111; position:relative; display:flex; align-items:center; justify-content:center; box-shadow: 2px 4px 12px rgba(0,0,0,0.15);">
                  <div style="position:absolute; inset:8%; border-radius:50%; border:1px solid #222;"></div>
                  <div style="position:absolute; inset:16%; border-radius:50%; border:1px solid #222;"></div>
                  <div style="position:absolute; inset:24%; border-radius:50%; border:1px solid #222;"></div>
                  <div style="width:33%; height:33%; border-radius:50%; background:#D02F5A; display:flex; align-items:center; justify-content:center;">
                    <div style="width:12%; height:12%; border-radius:50%; background:var(--surf);"></div>
                  </div>
                </div>
              </div>"""

html = html.replace(old_inner, new_inner)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated audio player inner")
