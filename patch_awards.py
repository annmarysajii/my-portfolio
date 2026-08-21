import re

for filename in ['portfolio.html', 'index.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Remove old awards styles
    html = re.sub(r'\.awards\{.*?\}', '', html)
    html = re.sub(r'\.awards-h\{.*?\}', '', html)
    html = re.sub(r'\.aw\{.*?\}', '', html)
    html = re.sub(r'\.aw:last-child\{.*?\}', '', html)
    html = re.sub(r'\.aw-i\{.*?\}', '', html)
    html = re.sub(r'\.aw-t\{.*?\}', '', html)
    html = re.sub(r'\.aw-n\{.*?\}', '', html)
    
    # Also remove dark mode overrides for awards if any
    html = re.sub(r'\[data-theme="dark"\] \.aw-n\{.*?\}', '', html)

    new_css = """
/* --- PREMIUM AWARDS SECTION --- */
.awards {
    margin-top: 3rem;
    padding: 2.5rem;
    background: linear-gradient(145deg, rgba(0,0,0,0.02), rgba(0,0,0,0.05));
    border: 1px solid rgba(0,0,0,0.06);
    border-radius: 16px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.03);
    position: relative;
    overflow: hidden;
}
[data-theme="dark"] .awards {
    background: linear-gradient(145deg, rgba(255,255,255,0.04), rgba(255,255,255,0.01));
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 10px 40px rgba(0,0,0,0.2);
}
.awards::before {
    content: '';
    position: absolute;
    top: 0; left: 0; width: 100%; height: 4px;
    background: linear-gradient(90deg, var(--blue), var(--red), var(--yel));
}
.awards-h {
    font-family: 'Clash Display', sans-serif;
    font-size: 1.6rem;
    font-weight: 600;
    letter-spacing: -0.02em;
    color: var(--ink);
    margin-bottom: 2rem;
}
.aw {
    display: flex;
    gap: 1.25rem;
    padding: 1.25rem 0;
    border-bottom: 1px solid rgba(0,0,0,0.06);
    transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
[data-theme="dark"] .aw {
    border-bottom: 1px solid rgba(255,255,255,0.06);
}
.aw:hover {
    transform: translateX(8px);
}
.aw:last-child {
    border-bottom: none;
    padding-bottom: 0;
}
.aw-i {
    width: 48px;
    height: 48px;
    border-radius: 12px;
    background: rgba(0,0,0,0.04);
    border: 1px solid rgba(0,0,0,0.05);
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--ink);
    flex-shrink: 0;
    box-shadow: 0 4px 10px rgba(0,0,0,0.02);
    transition: all 0.3s;
}
[data-theme="dark"] .aw-i {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
}
.aw:hover .aw-i {
    background: var(--ink);
    color: var(--bg);
    transform: scale(1.05) rotate(5deg);
}
.aw-t {
    font-size: 1rem;
    line-height: 1.6;
    color: var(--ink5);
}
.aw-n {
    font-family: 'Clash Display', sans-serif;
    font-size: 1.2rem;
    font-weight: 600;
    color: var(--ink);
    display: block;
    margin-bottom: 0.3rem;
}
"""
    
    html = html.replace('</style>', new_css + '\n</style>')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
print("Updated awards CSS")
