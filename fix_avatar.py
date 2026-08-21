import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_img = 'class="about-photo" style="object-fit:cover; width:100%; height:auto; animation: float 6s ease-in-out infinite;"'
new_img = 'style="object-fit:cover; width:100%; max-width:280px; height:auto; border-radius:12px; box-shadow:0 20px 40px rgba(0,0,0,0.2); animation: float 6s ease-in-out infinite;"'

html = html.replace(old_img, new_img)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Removed about-photo class from avatar to strip dashed box styling")
