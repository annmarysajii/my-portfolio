import re

vinyl_card = """a.innerHTML = `<div style="width:100%; aspect-ratio:4/3; background: var(--surf); display:flex; align-items:center; justify-content:center; overflow:hidden; border: 1px solid var(--line); border-radius:2px;"><div style="width:100px; height:100px; border-radius:50%; background: #111; position:relative; display:flex; align-items:center; justify-content:center; box-shadow: 2px 4px 12px rgba(0,0,0,0.15);"><div style="position:absolute; inset:8px; border-radius:50%; border:1px solid #222;"></div><div style="position:absolute; inset:16px; border-radius:50%; border:1px solid #222;"></div><div style="position:absolute; inset:24px; border-radius:50%; border:1px solid #222;"></div><div style="width:34px; height:34px; border-radius:50%; background:#D02F5A; display:flex; align-items:center; justify-content:center;"><div style="width:6px; height:6px; border-radius:50%; background:var(--surf);"></div></div></div></div>`;"""

for filename in ['portfolio.html', 'index.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = re.sub(r'a\.innerHTML = `<div style="width:100%; aspect-ratio:4/3; background: linear-gradient.*?</div>`;', vinyl_card, html)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated cards to vinyl")
