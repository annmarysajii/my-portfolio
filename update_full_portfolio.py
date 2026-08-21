import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the Full Portfolio link
old_full = '<a href="assets/downloads/AnnMarySaji_FullPortfolio.pdf" class="dl-btn" download><span class="dl-ico iy"><i data-lucide="folder"></i></span><span class="dl-txt"><span class="dl-lbl">Combined PDF</span>Full Portfolio</span></a>'
new_full = '<a href="assets/portfolio-data/PORTFOLIO PDFS/ART DIRECTION PORTFOLIO.pdf" class="dl-btn" download><span class="dl-ico iy"><i data-lucide="folder"></i></span><span class="dl-txt"><span class="dl-lbl">Combined PDF</span>Art Direction Portfolio</span></a>'

html = html.replace(old_full, new_full)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated full portfolio link to Art Direction Portfolio")
