for filename in ['project.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    new_gobunny_block = """                  if (id === 'gobunny') {
                      const brandColorSvg = findFile('BRANDCOLOR_GOBUNNY.svg');
                      const logoPrimary = findFile('GO BUNNY.png');
                      const artDirection = findFiles('ART DIRECTION PORTFOLIO');
                      const otherAssets = media.filter(f => 
                          !f.includes('BRANDCOLOR_GOBUNNY') && 
                          !f.includes('GO BUNNY.png') && 
                          !f.includes('ART DIRECTION PORTFOLIO')
                      );
                      
                      htmlStr += `<div class="cs-section">
                          <h2 class="cs-heading" style="font-family: 'More Sugar', var(--fd); margin-bottom: 2rem;">Brand Colors</h2>`;
                      if (brandColorSvg) {
                          htmlStr += renderMedia(brandColorSvg).replace('masonry-item', 'masonry-item full-width');
                      }
                      htmlStr += `</div>`;
                      
                      if (logoPrimary || artDirection.length > 0) {
                          htmlStr += `<div class="cs-section"><h2 class="cs-heading" style="font-family: 'More Sugar', var(--fd);">Logo & Art Direction</h2><div class="masonry-container">`;
                          if(logoPrimary) htmlStr += renderMedia(logoPrimary).replace('masonry-item', 'masonry-item full-width');
                          artDirection.forEach(f => { htmlStr += renderMedia(f); });
                          htmlStr += `</div></div>`;
                      }
  
                      if (otherAssets.length > 0) {
                          htmlStr += `<div class="cs-section"><h2 class="cs-heading" style="font-family: 'More Sugar', var(--fd);">Brand Assets & Collateral</h2><div class="masonry-container">`;
                          otherAssets.forEach(f => { htmlStr += renderMedia(f); });
                          htmlStr += `</div></div>`;
                      }
                  } else if (id === 'green-arrow') {"""
    
    html = html.replace("                  if (id === 'green-arrow') {", new_gobunny_block)

    # We also need to fix the duplicate `if (id === 'ntu-fest') {` blocks. 
    # The duplicate block occurs before `gal.innerHTML = htmlStr;`. We'll just leave it if it works, or fix it if it's easy.
    # Actually, it's safer to just let it be if it was working before, but let's check if the duplicate causes issues.
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
print("Injected GoBunny layout!")
