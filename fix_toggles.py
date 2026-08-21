import glob
import re

files = glob.glob('*.html')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix theme toggle
    old_theme = r"if\(btn\)btn\.textContent=next==='dark'\?'.*?':'.*?';"
    new_theme = """if(btn) btn.classList.toggle('active', next==='dark');
  const tIcon = document.getElementById('themeIcon');
  if(tIcon) {
    tIcon.setAttribute('data-lucide', next==='dark' ? 'sun' : 'moon');
    if(window.lucide) window.lucide.createIcons();
  }"""
    html = re.sub(old_theme, new_theme, html)
    
    # Another variant of theme toggle
    old_theme_2 = r"if\(btn\)btn\.innerHTML=next==='dark'\?'.*?':'.*?';"
    html = re.sub(old_theme_2, new_theme, html)

    # Fix music toggle
    old_music1 = r"if\(b\)b\.textContent=.*?\;"
    old_music2 = r"if\(b\)b\.innerHTML=.*?\;"
    
    def m_replacer(match):
        return """if(b) b.classList.toggle('active', !m.paused);
      const mIcon = b.querySelector('.icon');
      if(mIcon) {
        mIcon.setAttribute('data-lucide', m.paused ? 'music' : 'volume-2');
        if(window.lucide) window.lucide.createIcons();
      }"""
    
    html = re.sub(old_music1, m_replacer, html)
    html = re.sub(old_music2, m_replacer, html)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Fixed toggle buttons logic across all HTML files")
