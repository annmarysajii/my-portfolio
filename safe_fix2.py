import re
with open('project.html', 'r', encoding='utf-8') as f:
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
if old_css_if in html:
    html = html.replace(old_css_if, new_css_if)

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

# Match EXACTLY the block we want to replace
pattern = re.compile(r"                if \(id === 'gobunny'\) \{[\s\S]*?\} else if \(id === 'green-arrow'\) \{")
if pattern.search(html):
    html = pattern.sub(new_logic, html, count=1)
    print("Safely replaced logic block via precise regex!")
else:
    print("Regex match failed.")

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
