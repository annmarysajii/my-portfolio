import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Emojis dictionary
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

for k, v in reps.items():
    html = html.replace(k, v)

# Toggles (Switch to Stadium Pill)
# Replace the theme and music buttons
music_btn = '<button class="music-toggle pill-toggle" id="musicBtn" onclick="toggleMusic()" aria-label="Toggle music"><i data-lucide="music" class="icon"></i><div class="pill-track"><div class="pill-knob"></div></div></button>'
theme_btn = '<button class="theme-toggle pill-toggle" id="themeBtn" onclick="toggleTheme()" aria-label="Toggle dark mode"><i data-lucide="moon" class="icon" id="themeIcon"></i><div class="pill-track"><div class="pill-knob"></div></div></button>'

# Find the list items containing these buttons
html = re.sub(r'<button class="music-toggle".*?</button>', music_btn, html, flags=re.DOTALL)
html = re.sub(r'<button class="theme-toggle".*?</button>', theme_btn, html, flags=re.DOTALL)

# Update the JS for toggle buttons
toggle_js = """
window.toggleMusic=function(){
  const m=document.getElementById('bg-music');
  const b=document.getElementById('musicBtn');
  if(m.paused){
    m.play().catch(e=>console.log('Music play prevented:',e));
    if(b) b.classList.add('on');
  }else{
    m.pause();
    if(b) b.classList.remove('on');
  }
};
window.toggleTheme=function(){
  const cur=document.documentElement.getAttribute('data-theme');
  const next=cur==='dark'?'light':'dark';
  document.documentElement.setAttribute('data-theme',next);
  localStorage.setItem('theme',next);
  const tb = document.getElementById('themeBtn');
  if(tb) {
      if(next === 'dark') tb.classList.add('on');
      else tb.classList.remove('on');
  }
  const ti = document.getElementById('themeIcon');
  if(ti) ti.setAttribute('data-lucide', next==='dark'?'moon':'sun');
  if(window.lucide) lucide.createIcons();
  
  const isDark = next === 'dark';
  const sf=document.getElementById('sf');
  if(sf&&!document.querySelector('#cur').classList.contains('hov')) {
    sf.setAttribute('fill',next==='dark'?'#F0EEF5':'#111009');
  }
  // redraw bg if exists
  if(typeof drawBg==='function') drawBg();
};
"""

# Replace the old toggle functions
html = re.sub(r'window\.toggleMusic=function\(\).*?window\.toggleTheme=function\(\).*?// redraw bg', toggle_js + '\n  // redraw bg', html, flags=re.DOTALL)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Replaced emojis and updated toggles in portfolio")
