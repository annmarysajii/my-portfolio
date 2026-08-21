import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

pattern = r'\} else if \(file\.match\(/\\\.\(mp3\|wav\|m4a\)\\\$/i\)\) \{\s*a\.innerHTML = `<div class="ph".*?Audio Track.*?</div>`;\s*\}'
replacement = """} else if (file.match(/\\.(mp3|wav|m4a)$/i)) {
              a.innerHTML = `<div style="width:100%; aspect-ratio:4/3; background: linear-gradient(135deg, #1850A8 0%, #D02F5A 100%); display:flex; align-items:center; justify-content:center; overflow:hidden; position:relative;"><img src="assets/portfolio-data/My profile/me avatar.png" style="width:100%; height:100%; object-fit:cover; mix-blend-mode: overlay; opacity:0.8;"><div style="position:absolute; inset:0; background:rgba(0,0,0,0.2);"></div><svg style="position:absolute; width:48px; height:48px; color:white; opacity:0.8;" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18V5l12-2v13"></path><circle cx="6" cy="18" r="3"></circle><circle cx="18" cy="16" r="3"></circle></svg></div>`;
            }"""

html = re.sub(pattern, replacement, html)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Regex replace portfolio")
