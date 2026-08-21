import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

stars_def = """const STARS=Array.from({length:45},()=>({
  x:Math.random()*window.innerWidth,
  y:Math.random()*window.innerHeight,
  r:2.5+Math.random()*5,
  speed:.35+Math.random()*.55,
  drift:(Math.random()-0.5)*.28,
  rot:Math.random()*Math.PI*2,
  spin:(Math.random()-0.5)*.018,
  alpha:.08+Math.random()*.1,
  hue:HUES[Math.floor(Math.random()*3)],
  lit:0
}));
"""

# Insert STARS definition before window.currentCanvasTheme
html = html.replace("  window.currentCanvasTheme = 'star';", stars_def + "\n  window.currentCanvasTheme = 'star';")

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Restored STARS array")
