import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

m_btn = '<button class="music-toggle pill-toggle" id="musicBtn" onclick="toggleMusic()" aria-label="Toggle music" style="position:fixed;top:2.5rem;right:2.5rem;z-index:11;"><i data-lucide="music" class="icon"></i><div class="pill-track"><div class="pill-knob"></div></div></button>'

t_btn = '<button class="theme-toggle pill-toggle" id="themeBtn" onclick="toggleTheme()" aria-label="Toggle dark mode" style="position:fixed;top:2.5rem;right:6.5rem;z-index:11;"><i data-lucide="moon" class="icon" id="themeIcon"></i><div class="pill-track"><div class="pill-knob"></div></div></button>'

html = re.sub(r'<button class="music-toggle pill-toggle".*?</button>', m_btn, html, count=1, flags=re.DOTALL)
html = re.sub(r'<button class="theme-toggle pill-toggle".*?</button>', t_btn, html, count=1, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed toggles in index.html")
