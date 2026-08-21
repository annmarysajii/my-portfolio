import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_dl = '<a href="assets/portfolio-data/PORTFOLIO PDFS/AnnmarySaji_Production_Portfolio_2026 (1).pdf" class="dl-btn" download><span class="dl-ico ib"><i data-lucide="sparkles"></i></span><span class="dl-txt"><span class="dl-lbl">Portfolio PDF</span>Animation &amp; Visual Dev</span></a>'

new_dl = """<a href="assets/portfolio-data/PORTFOLIO PDFS/NewVisual development portfolio.pdf" class="dl-btn" download><span class="dl-ico ib"><i data-lucide="sparkles"></i></span><span class="dl-txt"><span class="dl-lbl">Portfolio PDF</span>Animation &amp; Visual Dev</span></a>
      <a href="assets/portfolio-data/PORTFOLIO PDFS/AnnmarySaji_Production_Portfolio_2026 (1).pdf" class="dl-btn" download><span class="dl-ico iy"><i data-lucide="video"></i></span><span class="dl-txt"><span class="dl-lbl">Portfolio PDF</span>Production</span></a>"""

html = html.replace(old_dl, new_dl)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated the quick look download section")
