import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace global resume links
html = html.replace('assets/downloads/AnnMarySaji_Resume.pdf', 'assets/portfolio-data/RESUMES/Annmary_Resume_2026.pdf')

# Animation section replacements
anim_old = '<a href="assets/portfolio-data/PORTFOLIO PDFS/AnnmarySaji_Production_Portfolio_2026 (1).pdf" class="sec-dl rv d2" download>+" PDF</a>'
anim_new = """<div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:flex-end;">
      <a href="assets/portfolio-data/PORTFOLIO PDFS/NewVisual development portfolio.pdf" class="sec-dl rv d2" download>+" Visual Dev Portfolio</a>
      <a href="assets/portfolio-data/PORTFOLIO PDFS/AnnmarySaji_Production_Portfolio_2026 (1).pdf" class="sec-dl rv d2" download>+" Production Portfolio</a>
      <a href="assets/portfolio-data/RESUMES/Annmary_Saji_Resume_Animation.pdf" class="sec-dl rv d2" download>+" Animation Resume</a>
     </div>"""

html = html.replace(anim_old, anim_new)

# Illustration section replacements
illus_old = '<a href="assets/portfolio-data/PORTFOLIO PDFS/AnnmarySaji_ComicPortfolio.pdf" class="sec-dl rv d2" download>+" PDF</a>'
illus_new = """<div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:flex-end;">
      <a href="assets/portfolio-data/PORTFOLIO PDFS/AnnmarySaji_ComicPortfolio.pdf" class="sec-dl rv d2" download>+" Comic Portfolio</a>
      <a href="assets/portfolio-data/RESUMES/AnnMary_Saji_Resume_Illustration.pdf" class="sec-dl rv d2" download>+" Illustration Resume</a>
     </div>"""

html = html.replace(illus_old, illus_new)

# Videography section replacements
video_old = '<a href="assets/portfolio-data/PORTFOLIO PDFS/AnnmarySaji_SocialmediaPortfolio (1).pdf" class="sec-dl rv d2" download>+" PDF</a>'
video_new = """<div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:flex-end;">
      <a href="assets/portfolio-data/PORTFOLIO PDFS/AnnmarySaji_SocialmediaPortfolio (1).pdf" class="sec-dl rv d2" download>+" Videography Portfolio</a>
      <a href="assets/portfolio-data/RESUMES/Annmary_Saji_Resume_DigitalMarketing.pdf" class="sec-dl rv d2" download>+" Marketing Resume</a>
     </div>"""

html = html.replace(video_old, video_new)

# Graphic Design section replacements
design_old = '<a href="assets/portfolio-data/PORTFOLIO PDFS/Brand Design Portfolio - Annmary Saji.pdf" class="sec-dl rv d2" download>+" PDF</a>'
design_new = """<div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:flex-end;">
      <a href="assets/portfolio-data/PORTFOLIO PDFS/Brand Design Portfolio - Annmary Saji.pdf" class="sec-dl rv d2" download>+" Brand Design Portfolio</a>
      <a href="assets/portfolio-data/PORTFOLIO PDFS/ART DIRECTION PORTFOLIO.pdf" class="sec-dl rv d2" download>+" Art Direction Portfolio</a>
      <a href="assets/portfolio-data/RESUMES/Annmary_Saji_Resume_Design.pdf" class="sec-dl rv d2" download>+" Design Resume</a>
     </div>"""

html = html.replace(design_old, design_new)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated portfolio.html with comprehensive PDF and Resume links")
