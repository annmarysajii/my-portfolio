import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add float animation keyframes
html = html.replace("</style>", "@keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-15px); } }\n</style>")

# Modify the image tag
old_img = """<img src="assets/portfolio-data/My profile/me avatar.png" style="object-fit:cover; width:100%; max-width:280px; height:auto; border-radius:12px; box-shadow:0 20px 40px rgba(0,0,0,0.2); animation: float 6s ease-in-out infinite;">"""
new_img = """<img src="assets/portfolio-data/My profile/me avatar.png" style="object-fit:contain; width:100%; max-width:420px; height:auto; animation: float 5s ease-in-out infinite; transform-origin: center center; filter: drop-shadow(0 20px 30px rgba(0,0,0,0.15)); margin: 0 auto; display: block;">"""

html = html.replace(old_img, new_img)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated avatar")
