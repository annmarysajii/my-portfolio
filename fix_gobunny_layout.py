import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix GoBunny Colors (regex to catch any whitespace)
old_colors = r"if\s*\(id\s*===\s*'gobunny'\)\s*\{\s*document\.documentElement\.style\.setProperty\('--bg',\s*'#FFEBF0'\);\s*document\.documentElement\.style\.setProperty\('--surf',\s*'#FFF5F7'\);\s*document\.documentElement\.style\.setProperty\('--ink',\s*'#D02F5A'\);\s*document\.documentElement\.style\.setProperty\('--line',\s*'rgba\(208, 47, 90, 0\.2\)'\);"
new_colors = """if (id === 'gobunny') {
                document.documentElement.style.setProperty('--bg', '#FFF2F0');
                document.documentElement.style.setProperty('--surf', '#FFFFFF');
                document.documentElement.style.setProperty('--ink', '#FF3522');
                document.documentElement.style.setProperty('--line', 'rgba(255, 53, 34, 0.2)');"""

html = re.sub(old_colors, new_colors, html)

# 2. Fix the Custom Names mapping
html = html.replace("'It is time for some strawberries': 'Billboard Mockup',", "'It is time for some strawberries': 'Mobile UI',")
html = html.replace("'ART DIRECTION PORTFOLIO': 'Brand Guidelines',", "'ART DIRECTION PORTFOLIO': 'Billboard Mockup',")
html = html.replace("'ART DIRECTION PORTFOLIO (1)': 'Brand Guidelines',", "'ART DIRECTION PORTFOLIO (1)': 'Brand Guidelines',")
html = html.replace("'Copy of ART DIRECTION PORTFOLIO (3)': 'Brand Presentation',", "'Copy of ART DIRECTION PORTFOLIO (3)': 'Brand Presentation',")
html = html.replace("'3': isGoBunny ? 'Product Packaging' : 'Event Poster',", "'3': isGoBunny ? 'Packaging Design' : 'Event Poster',")
html = html.replace("'4': isGoBunny ? 'Product Packaging' : 'Instagram Campaign',", "'4': isGoBunny ? 'Packaging Details' : 'Instagram Campaign',")

# Group all "Your paragraph text" into Social Media / Guidelines
# Group logo into Logo
# Group the rest into Mockups

# Rewrite the GoBunny layout block
old_layout_start = html.find("if (id === 'gobunny') {")
# Find the second instance of "if (id === 'gobunny') {" (which is the layout one)
first_idx = html.find("if (id === 'gobunny') {")
layout_idx = html.find("if (id === 'gobunny') {", first_idx + 1)
end_idx = html.find("} else if (id === 'green-arrow') {", layout_idx)

new_layout = """if (id === 'gobunny') {
                      const brandColorSvg = findFile('BRANDCOLOR_GOBUNNY.svg');
                      const logoPrimary = findFile('GO BUNNY.png');
                      const billboard = findFile('ART DIRECTION PORTFOLIO.png');
                      const mobileUI = findFile('It is time for some strawberries');
                      const packaging = media.filter(f => f.includes('3.png') || f.includes('4.png'));
                      const guidelines = media.filter(f => f.includes('Your paragraph text') || f.includes('ART DIRECTION PORTFOLIO (1)') || f.includes('Copy of ART DIRECTION PORTFOLIO'));
                      
                      htmlStr += `<div class="cs-section">
                          <h2 class="cs-heading" style="font-family: 'More Sugar', var(--fd); margin-bottom: 2rem;">Brand Colors</h2>`;
                      if (brandColorSvg) htmlStr += renderMedia(brandColorSvg).replace('masonry-item', 'masonry-item full-width');
                      htmlStr += `</div>`;
                      
                      htmlStr += `<div class="cs-section"><h2 class="cs-heading" style="font-family: 'More Sugar', var(--fd);">Logo & Brand Identity</h2><div class="masonry-container">`;
                      if(logoPrimary) htmlStr += renderMedia(logoPrimary).replace('masonry-item', 'masonry-item full-width');
                      guidelines.forEach(f => { htmlStr += renderMedia(f); });
                      htmlStr += `</div></div>`;
                      
                      htmlStr += `<div class="cs-section"><h2 class="cs-heading" style="font-family: 'More Sugar', var(--fd);">Digital & App Mockups</h2><div class="masonry-container">`;
                      if(mobileUI) htmlStr += renderMedia(mobileUI);
                      htmlStr += `</div></div>`;

                      htmlStr += `<div class="cs-section"><h2 class="cs-heading" style="font-family: 'More Sugar', var(--fd);">Posters & Advertising</h2><div class="masonry-container">`;
                      if(billboard) htmlStr += renderMedia(billboard);
                      htmlStr += `</div></div>`;

                      htmlStr += `<div class="cs-section"><h2 class="cs-heading" style="font-family: 'More Sugar', var(--fd);">Packaging & Products</h2><div class="masonry-container">`;
                      packaging.forEach(f => { htmlStr += renderMedia(f); });
                      htmlStr += `</div></div>`;
"""

html = html[:layout_idx] + new_layout + html[end_idx:]

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed GoBunny!")
