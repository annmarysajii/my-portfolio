import re
with open('project.html', 'r', encoding='utf-8') as f:
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

# Find all occurrences of `if (id === 'green-arrow') {` regardless of whitespace
# We know the second occurrence is the one we want to replace (it's inside the htmlStr generation).
# The first occurrence is the CSS override `document.documentElement.style.setProperty(...)`

matches = list(re.finditer(r"\n\s*if\s*\(\s*id\s*===\s*'green-arrow'\s*\)\s*\{", html))
if len(matches) >= 2:
    match = matches[1]
    html = html[:match.start()] + "\n" + new_gobunny_block + html[match.end():]
    with open('project.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("SUCCESSFULLY matched and replaced the second occurrence!")
else:
    print(f"FAILED to find 2 occurrences. Found {len(matches)}")
