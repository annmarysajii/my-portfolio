import glob
import re

files = glob.glob('*.html')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the IIFE initialization
    old_init = r"if\(btn\)btn\.textContent=saved==='dark'\?'.*?':'.*?';"
    old_init_2 = r"if\(btn\)btn\.innerHTML=saved==='dark'\?'.*?':'.*?';"
    
    new_init = """if(btn) btn.classList.toggle('on', saved==='dark');
  const initIcon = document.getElementById('themeIcon');
  if(initIcon) {
    initIcon.setAttribute('data-lucide', saved==='dark' ? 'sun' : 'moon');
  }"""
    
    html = re.sub(old_init, new_init, html)
    html = re.sub(old_init_2, new_init, html)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("Fixed initial load logic")
