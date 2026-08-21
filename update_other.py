import re

reps = {
    "🏆": '<i data-lucide="award"></i>',
    "🥈": '<i data-lucide="medal"></i>',
    "📜": '<i data-lucide="scroll-text"></i>',
    "🌟": '<i data-lucide="star"></i>',
    "🧰": '<i data-lucide="briefcase"></i>',
    "💬": '<i data-lucide="message-square"></i>',
    "📍": '<i data-lucide="map-pin"></i>',
    "🎓": '<i data-lucide="graduation-cap"></i>',
    "💼": '<i data-lucide="linkedin"></i>',
    "📱": '<i data-lucide="instagram"></i>',
    "✨": '<i data-lucide="sparkles"></i>',
    "🖍️": '<i data-lucide="pen-tool"></i>',
    "🎬": '<i data-lucide="clapperboard"></i>',
    "🎨": '<i data-lucide="palette"></i>',
    "🎵": '<i data-lucide="music"></i>',
    "📂": '<i data-lucide="folder"></i>',
    "📄": '<i data-lucide="file-text"></i>',
    "✦": '<i data-lucide="image"></i>'
}

music_btn = '<button class="music-toggle pill-toggle" id="musicBtn" onclick="toggleMusic()" aria-label="Toggle music"><i data-lucide="music" class="icon"></i><div class="pill-track"><div class="pill-knob"></div></div></button>'
theme_btn = '<button class="theme-toggle pill-toggle" id="themeBtn" onclick="toggleTheme()" aria-label="Toggle dark mode"><i data-lucide="moon" class="icon" id="themeIcon"></i><div class="pill-track"><div class="pill-knob"></div></div></button>'

for fname in ['index.html', 'project.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    for k, v in reps.items():
        html = html.replace(k, v)

    html = re.sub(r'<button class="music-toggle".*?</button>', music_btn, html, flags=re.DOTALL)
    html = re.sub(r'<button class="theme-toggle".*?</button>', theme_btn, html, flags=re.DOTALL)
    
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated index and project")
