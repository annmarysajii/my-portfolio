import json
import re

with open('scripts/data.js', 'r', encoding='utf-8') as f:
    js = f.read()

json_str = js.replace('window.PORTFOLIO_DATA = ', '').rstrip(';')
data = json.loads(json_str)

# Replace gcf-documentary with YouTube links
data['gcf-documentary'] = [
    "https://youtu.be/uTqkfJAd1Cw",
    "https://youtu.be/QIRoZpu3-Go"
]

js_out = "window.PORTFOLIO_DATA = " + json.dumps(data, indent=2) + ";"
with open('scripts/data.js', 'w', encoding='utf-8') as f:
    f.write(js_out)
print("Updated GCF videos to YouTube embeds")
