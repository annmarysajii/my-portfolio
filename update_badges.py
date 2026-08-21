import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the floating chip CSS
html = re.sub(r'\.chip\{.*?\n.*?keyframes fl.*?\}\n', '', html, flags=re.DOTALL)

# Add new badge container CSS
html = html.replace('.hero-vis{position:relative;}', '.hero-vis{position:relative; display:flex; flex-direction:column; gap:1.5rem;}\n.hero-badges{display:flex; flex-wrap:wrap; gap:0.75rem; justify-content:center;}\n.hero-badge{padding:0.5rem 1rem; border-radius:100px; font-size:0.85rem; font-weight:600; background:var(--ink07); color:var(--ink); border:1px solid var(--ink12); display:flex; align-items:center; gap:0.5rem;}')

# Replace HTML
old_chips = """      <span class="chip ch1">Annecy 2025</span>
      <span class="chip ch2">50+ Commissions</span>
      <span class="chip ch3">BFA Animation</span>"""

new_chips = """      <div class="hero-badges">
        <span class="hero-badge" style="background:var(--blue); color:#fff; border-color:var(--blue);"><i data-lucide="award" style="width:16px; height:16px;"></i> Annecy 2025</span>
        <span class="hero-badge" style="background:var(--yel); color:var(--ink); border-color:var(--yel);"><i data-lucide="briefcase" style="width:16px; height:16px;"></i> 50+ Commissions</span>
        <span class="hero-badge" style="background:var(--white); color:var(--ink);"><i data-lucide="graduation-cap" style="width:16px; height:16px;"></i> BFA Animation</span>
      </div>"""

html = html.replace(old_chips, new_chips)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed hero badges")
