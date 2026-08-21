import re

with open('scripts/motion.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add a check to the draw loop
old_draw = "function draw(){"
new_draw = "function draw(){\n      if(window.matchMedia('(hover: none)').matches || window.innerWidth < 768) { requestAnimationFrame(draw); return; }"

js = js.replace(old_draw, new_draw)

with open('scripts/motion.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Disabled canvas drawing loop on mobile/touch devices")
