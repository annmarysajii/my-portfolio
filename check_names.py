import json
import re

with open('scripts/data.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Extract the JSON part
json_str = js_content.replace('window.PORTFOLIO_DATA = ', '').strip().rstrip(';')

try:
    data = json.loads(json_str)
    all_files = []
    for key, files in data.items():
        if isinstance(files, list):
            all_files.extend(files)
        elif isinstance(files, dict):
            # some are dicts with title, year etc. the media is not here?
            pass
            
    for f in all_files:
        name = f.split('/')[-1].split('.')[0]
        # Check for weird names
        if re.search(r'\d+$', name) or re.search(r'copy|untitled|final|test|design|image|comm', name.lower()):
            print(f"[{key}] {name}")
except Exception as e:
    print("Error parsing:", e)

