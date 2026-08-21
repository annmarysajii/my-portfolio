import re

# 1. FIX MOTION.CSS
with open('css/motion.css', 'r', encoding='utf-8') as f:
    mcss = f.read()

# Remove transform from body
mcss = mcss.replace('transform: translateY(10px);', '')
mcss = mcss.replace('transform: translateY(0);', '')
mcss = mcss.replace('transform: translateY(-10px) !important;', '')

with open('css/motion.css', 'w', encoding='utf-8') as f:
    f.write(mcss)

# 2. FIX MOTION.JS
with open('scripts/motion.js', 'r', encoding='utf-8') as f:
    mjs = f.read()

mjs = mjs.replace('a[href]:not([target="_blank"]):not([href^="#"])', 'a[href]:not([target="_blank"]):not([href^="#"]):not([download])')

with open('scripts/motion.js', 'w', encoding='utf-8') as f:
    f.write(mjs)

print("Fixed motion CSS and JS")
