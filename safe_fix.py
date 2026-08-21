for filename in ['project.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove the pink CSS variables for GoBunny
    old_css_if = """            if (id === 'gobunny') {
                document.documentElement.style.setProperty('--bg', '#FFEBF0');
                document.documentElement.style.setProperty('--surf', '#FFF5F7');
                document.documentElement.style.setProperty('--ink', '#D02F5A');
                document.documentElement.style.setProperty('--line', 'rgba(208, 47, 90, 0.2)');
                (document.querySelector('.con') || document.querySelector('#main')).style.maxWidth = '1200px';
            } else if (id === 'green-arrow') {"""
            
    new_css_if = "            if (id === 'green-arrow') {"
    html = html.replace(old_css_if, new_css_if)

    old_logic = """                if (id === 'gobunny') {
                    const logoPrimary = findFile('GO BUNNY');
                    const logoSecondary = findFiles('Your paragraph text').filter(f => f.includes('35') || f.includes('36') || f.includes('33')); 
                    const colors = findFiles('Your paragraph text').filter(f => f.includes('27') || f.includes('37'));
                    const guidelines = findFiles('Brand identity');
                    const mockups = findFiles('Your paragraph text').filter(f => f.includes('29') || f.includes('30') || f.includes('28') || f.includes('38') || f.includes('23') || f.includes('24'));
                    
                    htmlStr += `<div class="cs-section"><h2 class="cs-heading">Color Palette</h2>
                        <div class="cs-palettes">
                            <div class="cs-color"><div class="cs-swatch" style="background:#D02F5A;"></div><span class="cs-hex">#D02F5A</span></div>
                            <div class="cs-color"><div class="cs-swatch" style="background:#FF9A9E;"></div><span class="cs-hex">#FF9A9E</span></div>
                            <div class="cs-color"><div class="cs-swatch" style="background: var(--bg)5F7;"></div><span class="cs-hex">#FFF5F7</span></div>
                            <div class="cs-color"><div class="cs-swatch" style="background:#2A2A2A;"></div><span class="cs-hex">#2A2A2A</span></div>
                        </div>
                    </div>`;
                    
                    htmlStr += `<div class="cs-section"><h2 class="cs-heading">Logo Variations</h2><div class="masonry-container">`;
                    if(logoPrimary) htmlStr += renderMedia(logoPrimary).replace('masonry-item', 'masonry-item full-width');
                    logoSecondary.forEach(f => { htmlStr += renderMedia(f); });
                    htmlStr += `</div></div>`;

                    htmlStr += `<div class="cs-section"><h2 class="cs-heading">Typography & Colors</h2><div class="masonry-container">`;
                    colors.forEach(f => { htmlStr += renderMedia(f); });
                    htmlStr += `</div></div>`;

                    htmlStr += `<div class="cs-section"><h2 class="cs-heading">Brand Guidelines</h2><div class="masonry-container">`;
                    guidelines.forEach(f => { htmlStr += renderMedia(f); });
                    htmlStr += `</div></div>`;
                    
                    htmlStr += `<div class="cs-section"><h2 class="cs-heading">Mockups & Application</h2><div class="masonry-container">`;
                    mockups.forEach(f => { htmlStr += renderMedia(f); });
                    htmlStr += `</div></div>`;
                } else if (id === 'green-arrow') {"""
                
    new_logic = """                if (id === 'gobunny') {
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

    if old_logic in html:
        html = html.replace(old_logic, new_logic)
        print("Safely replaced logic block without touching anything else!")
    else:
        print("COULD NOT FIND LOGIC BLOCK TO REPLACE")
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
