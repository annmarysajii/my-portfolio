import re
with open('scripts/data.js', 'r', encoding='utf-8') as f:
    data = f.read()
# Add nangeli cover image as the first image
data = re.sub(r'"nangele": \[\n', '"nangele": [\n      "assets/portfolio-data/Nangeli/nangeli cover image.png",\n', data)
with open('scripts/data.js', 'w', encoding='utf-8') as f:
    f.write(data)
print("Added nangeli cover")
