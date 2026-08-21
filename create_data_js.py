import json

with open('assets/portfolio-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

js_content = "window.PORTFOLIO_DATA = " + json.dumps(data, indent=2) + ";"

with open('scripts/data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
print("Created scripts/data.js")
