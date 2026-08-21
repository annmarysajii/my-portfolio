import re

for filename in ['portfolio.html', 'index.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Fix the image object-fit issues for the project cards
    html = html.replace(
        '<img src="${file}" alt="" style="width:100%;height:auto;object-fit:contain;">',
        '<img src="${file}" alt="" style="width:100%;height:100%;object-fit:cover;aspect-ratio:4/3;border-radius:2px;">'
    )
    
    html = html.replace(
        '<video src="${file}" autoplay loop muted playsinline style="width:100%;height:auto;object-fit:contain;"></video>',
        '<video src="${file}" autoplay loop muted playsinline style="width:100%;height:100%;object-fit:cover;aspect-ratio:4/3;border-radius:2px;"></video>'
    )

    # 2. Fix the Awards text visibility by forcing explicit hex colors and robust z-indexes
    old_css = """.awards-h {
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
  }"""

    new_css = """.awards-h {
      font-family: 'Clash Display', sans-serif;
      font-size: 1.6rem;
      font-weight: 600;
      letter-spacing: -0.02em;
      color: #111009;
      margin-bottom: 2rem;
      position: relative;
      z-index: 10;
  }
  [data-theme="dark"] .awards-h { color: #F0EEF5; }
  .aw {
      display: flex;
      gap: 1.25rem;
      padding: 1.25rem 0;
      border-bottom: 1px solid rgba(0,0,0,0.06);
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      position: relative;
      z-index: 10;
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
      color: #111009;
      flex-shrink: 0;
      box-shadow: 0 4px 10px rgba(0,0,0,0.02);
      transition: all 0.3s;
  }
  [data-theme="dark"] .aw-i {
      background: rgba(255,255,255,0.05);
      border: 1px solid rgba(255,255,255,0.1);
      color: #F0EEF5;
  }
  .aw:hover .aw-i {
      background: #1850A8;
      color: #FFF;
      transform: scale(1.05) rotate(5deg);
  }
  .aw-t {
      font-size: 1rem;
      line-height: 1.6;
      color: rgba(17,16,9,0.6);
  }
  [data-theme="dark"] .aw-t { color: rgba(240,238,245,0.7); }
  .aw-n {
      font-family: 'Clash Display', sans-serif;
      font-size: 1.2rem;
      font-weight: 600;
      color: #111009;
      display: block;
      margin-bottom: 0.3rem;
  }
  [data-theme="dark"] .aw-n { color: #F0EEF5; }"""

    html = html.replace(old_css, new_css)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
print("Applied CSS fixes!")
