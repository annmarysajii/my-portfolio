import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace PDF links
html = html.replace('href="assets/downloads/AnnMarySaji_Portfolio_Animation.pdf"', 'href="assets/portfolio-data/PORTFOLIO PDFS/AnnmarySaji_Production_Portfolio_2026 (1).pdf"')
html = html.replace('href="assets/downloads/AnnMarySaji_Portfolio_Illustration.pdf"', 'href="assets/portfolio-data/PORTFOLIO PDFS/AnnmarySaji_ComicPortfolio.pdf"')
html = html.replace('href="assets/downloads/AnnMarySaji_Portfolio_Videography.pdf"', 'href="assets/portfolio-data/PORTFOLIO PDFS/AnnmarySaji_SocialmediaPortfolio (1).pdf"')
html = html.replace('href="assets/downloads/AnnMarySaji_Portfolio_GraphicDesign.pdf"', 'href="assets/portfolio-data/PORTFOLIO PDFS/Brand Design Portfolio - Annmary Saji.pdf"')

# What about Music? The user didn't provide a Music PDF. I'll just remove the button for Music.
html = re.sub(r'<a href="assets/downloads/AnnMarySaji_Portfolio_Music\.pdf".*?</a>', '', html)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated PDF download links")
