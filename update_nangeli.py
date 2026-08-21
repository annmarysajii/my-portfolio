import json
import re

with open('scripts/data.js', 'r', encoding='utf-8') as f:
    js = f.read()

json_str = js.replace('window.PORTFOLIO_DATA = ', '').rstrip(';')
data = json.loads(json_str)

# Sort nangeli using natural sort
def natural_sort_key(s, _nsre=re.compile('([0-9]+)')):
    return [int(text) if text.isdigit() else text.lower() for text in _nsre.split(s)]

if 'nangele' in data:
    data['nangele'].sort(key=natural_sort_key)

js_out = "window.PORTFOLIO_DATA = " + json.dumps(data, indent=2) + ";"
with open('scripts/data.js', 'w', encoding='utf-8') as f:
    f.write(js_out)
print("Sorted Nangeli pages")

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make Nangeli render as a book
old_gallery = """              // Layout: First item is hero, next 2 are medium row, next are square grid
              if (idx === 0) {"""
new_gallery = """              // If it's a comic, just stack them vertically
              if (id === 'nangele' || id === 'internship-comics' || id === 'wellbeing-planner') {
                  htmlStr += `<div style="margin-bottom:1rem;">${el}</div>`;
                  return;
              }
              
              // Layout: First item is hero, next 2 are medium row, next are square grid
              if (idx === 0) {"""

html = html.replace(old_gallery, new_gallery)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated project.html to render comics as a vertical scroll (book view)")
