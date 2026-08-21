import json

with open('scripts/data.js', 'r', encoding='utf-8') as f:
    js = f.read()

json_str = js.replace('window.PORTFOLIO_DATA = ', '').rstrip(';')
data = json.loads(json_str)

if 'nangele' in data:
    arr = data['nangele']
    # find starting page
    start_page = next((x for x in arr if 'starting page' in x.lower()), None)
    if start_page:
        arr.remove(start_page)
        arr.insert(0, start_page)
    data['nangele'] = arr

js_out = "window.PORTFOLIO_DATA = " + json.dumps(data, indent=2) + ";"
with open('scripts/data.js', 'w', encoding='utf-8') as f:
    f.write(js_out)
print("Fixed Nangeli sorting")
