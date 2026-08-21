for filename in ['project.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # The exact block we are replacing
    old_line = "                if (id === 'green-arrow') {"
    
    new_gobunny_block = """                if (id === 'gobunny') {
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
    
    # We want to replace the SECOND occurrence of old_line.
    parts = html.split(old_line)
    if len(parts) >= 3:
        # Reconstruct with the replacement at the second occurrence
        html = parts[0] + old_line + parts[1] + new_gobunny_block + parts[2]
        for p in parts[3:]:
            html += old_line + p
            
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
print("Injected GoBunny layout perfectly this time!")
