import re
with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r"ctx\.fillText\('[^']+', 0, 0\);", "ctx.fillText('\\u266A', 0, 0);", html)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed music character via regex")
