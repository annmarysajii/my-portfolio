import re

with open('scripts/motion.js', 'r', encoding='utf-8') as f:
    js = f.read()

bad1 = "card.style.transform = perspective(1000px) scale3d(1.01, 1.01, 1.01) rotateX( + rotateX + deg) rotateY( + rotateY + deg);"
good1 = "card.style.transform = `perspective(1000px) scale3d(1.01, 1.01, 1.01) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;"

bad2 = "card.style.transform = perspective(1000px) scale3d(1, 1, 1) rotateX(0deg) rotateY(0deg);"
good2 = "card.style.transform = `perspective(1000px) scale3d(1, 1, 1) rotateX(0deg) rotateY(0deg)`;"

js = js.replace(bad1, good1).replace(bad2, good2)

with open('scripts/motion.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Fixed backticks in motion.js")
