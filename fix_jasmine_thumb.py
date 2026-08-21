import json

with open('scripts/data.js', 'r', encoding='utf-8') as f:
    js = f.read()

json_str = js.replace('window.PORTFOLIO_DATA = ', '').rstrip(';')
data = json.loads(json_str)

# Prepend cover image to jasmine-comic so portfolio.html uses it
cover_img = "assets/portfolio-data/Jasmine_music_concept album/jasmine cover album.jpg"
if 'jasmine-comic' in data:
    # Ensure it's not already there
    if cover_img not in data['jasmine-comic']:
        data['jasmine-comic'].insert(0, cover_img)

js_out = "window.PORTFOLIO_DATA = " + json.dumps(data, indent=2) + ";"
with open('scripts/data.js', 'w', encoding='utf-8') as f:
    f.write(js_out)
print("Updated data.js with jasmine cover image for comic")
