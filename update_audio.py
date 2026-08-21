import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make the Audio track rendering in project.html cooler, with track titles
old_audio = """el = `<div style="display:flex; align-items:center; justify-content:center; width:100%; background:var(--surf); padding:2rem; border-radius:4px;"><audio src="${file}" controls style="width:100%;"></audio></div>`;"""

new_audio = """let title = file.split('/').pop().replace(/\\.(wav|mp3|m4a)$/i, '');
                  el = `<div style="background:var(--surf); border:1px solid var(--line); border-radius:4px; overflow:hidden; padding:2rem; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:1.5rem; aspect-ratio:4/3;">
                    <div style="width:100px; height:100px; border-radius:50%; background:var(--ink07); display:flex; align-items:center; justify-content:center;">
                        <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18V5l12-2v13"></path><circle cx="6" cy="18" r="3"></circle><circle cx="18" cy="16" r="3"></circle></svg>
                    </div>
                    <div style="font-weight:600; font-size:1.1rem; text-align:center;">${title}</div>
                    <audio src="${file}" controls style="width:100%; outline:none; height:40px;"></audio>
                  </div>`;"""

html = html.replace(old_audio, new_audio)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated Audio player component in project.html to include a graphic and track title")
