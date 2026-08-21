import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix Jasmine album loop
old_album = """const imgs = media.filter(f => f.match(/\\.(png|jpe?g)$/i));
              const audios = media.filter(f => f.match(/\\.(wav|mp3|m4a)$/i));
              
              let albumHtml = '<style>.album-grid{display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:2rem;}</style><div class="album-grid">';
              for(let i=0; i<Math.max(imgs.length, audios.length); i++) {"""

new_album = """const imgs = media.filter(f => f.match(/\\/\\d\\.(png|jpe?g)$/i)).sort(); // Matches 1.png, 2.png, etc.
              const audios = media.filter(f => f.match(/\\.(wav|mp3|m4a)$/i));
              
              let albumHtml = '<style>.album-grid{display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:2rem;}</style><div class="album-grid">';
              const count = Math.min(imgs.length, audios.length);
              for(let i=0; i<count; i++) {"""

html = html.replace(old_album, new_album)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed Jasmine album array length mismatch")
