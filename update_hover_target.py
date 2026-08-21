import re

with open('css/motion.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .char:hover with :hover .char so the whole title animates together!
css = css.replace('.sec-title .char:hover', '.sec-title:hover .char')

with open('css/motion.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated hover selectors to trigger the whole title")
