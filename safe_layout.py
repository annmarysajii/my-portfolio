with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = "                if (id === 'gobunny') {\n                      const brandColorSvg"
end_marker = "                  } else if (id === 'green-arrow') {"

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_block = """                if (id === 'gobunny') {
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
    html = html[:start_idx] + new_block + html[end_idx:]
    with open('project.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Safely replaced GoBunny layout!")
else:
    print("Failed to find markers!")
