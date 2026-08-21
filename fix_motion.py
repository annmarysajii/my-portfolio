import re

with open('scripts/motion.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace .card-img with .card for the reveal observer
old_reveal = "document.querySelectorAll('.sec, .card-img, .gw-header, .sec-title, .gallery-h, .text-block')"
new_reveal = "document.querySelectorAll('.sec, .card, .gw-header, .sec-title, .gallery-h, .text-block')"
js = js.replace(old_reveal, new_reveal)

with open('scripts/motion.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated motion.js")
