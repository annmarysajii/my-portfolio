import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_audio = """            el = `<div class="media-el" style="background:var(--surf); border:1px solid var(--line); border-radius:4px; overflow:hidden; padding:2rem; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:1.5rem; aspect-ratio:4/3; break-inside: avoid; margin-bottom: 2rem;">
              <div style="width:100px; height:100px; border-radius:50%; background:var(--ink07); display:flex; align-items:center; justify-content:center;">
                  <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18V5l12-2v13"></path><circle cx="6" cy="18" r="3"></circle><circle cx="18" cy="16" r="3"></circle></svg>
              </div>
              <div style="font-weight:600; font-size:1.1rem; text-align:center;">${name}</div>
              <audio src="${file}" controls style="width:100%; outline:none; height:40px;"></audio>
            </div>`;"""

new_audio = """            el = `<div class="media-el" style="background:var(--surf); border:1px solid var(--line); border-radius:4px; overflow:hidden; display:flex; flex-direction:column; align-items:center; justify-content:center; break-inside: avoid; margin-bottom: 2rem; box-shadow:0 4px 20px rgba(0,0,0,0.05);">
              <div style="width:100%; aspect-ratio:1; background: var(--surf); display:flex; align-items:center; justify-content:center; overflow:hidden; border-bottom: 1px solid var(--line);">
                <div style="width:65%; height:65%; border-radius:50%; background: #111; position:relative; display:flex; align-items:center; justify-content:center; box-shadow: 2px 4px 12px rgba(0,0,0,0.15);">
                  <div style="position:absolute; inset:8%; border-radius:50%; border:1px solid #222;"></div>
                  <div style="position:absolute; inset:16%; border-radius:50%; border:1px solid #222;"></div>
                  <div style="position:absolute; inset:24%; border-radius:50%; border:1px solid #222;"></div>
                  <div style="width:33%; height:33%; border-radius:50%; background:#D02F5A; display:flex; align-items:center; justify-content:center;">
                    <div style="width:12%; height:12%; border-radius:50%; background:var(--surf);"></div>
                  </div>
                </div>
              </div>
              <div style="width:100%; padding:1.5rem; text-align:center;">
                  <div style="font-weight:600; font-size:1.15rem; margin-bottom:1rem; font-family:'Clash Display', sans-serif;">${name}</div>
                  <audio src="${file}" controls style="width:100%; outline:none; height:40px; border-radius:20px;"></audio>
              </div>
            </div>`;"""

html = html.replace(old_audio, new_audio)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated project.html audio player to vinyl")
