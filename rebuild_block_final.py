for filename in ['project.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # The issue:
    # 1. `gal.innerHTML = htmlStr;` was moved / deleted.
    # 2. `if (id === 'nangele')` might be completely missing its `}` closure from the previous blocks.

    import re
    # We will slice out the ENTIRE native case studies block and reconstruct it flawlessly.
    start_str = "if (id === 'gobunny' || id === 'green-arrow' || id === 'nangele' || id === 'original-tracks' || id === 'wellbeing-planner' || id === 'ntu-fest') {"
    end_str = "// Default handling for other galleries"
    
    if start_str in html and end_str in html:
        prefix = html.split(start_str)[0]
        suffix = html.split(end_str)[1]
        
        new_block = start_str + """
                  let htmlStr = styleBlock;
                  
                  if (id === 'gobunny') {
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
                  } else if (id === 'green-arrow') {
                      const logo = findFile('LOGO GREEN ARROW');
                      const posters = findFiles('3.png').concat(findFiles('presents'));
                      const digital = findFiles('4.png').concat(findFiles('5.png'));
                      const merch = findFiles('6.png').concat(findFiles('7.png'));
                      
                      htmlStr += `
                      <div class="cs-section">
                          <h2 class="cs-heading">Color Palette</h2>
                          <div class="cs-palettes">
                              <div class="cs-color"><div class="cs-swatch" style="background:#243E36;"></div><span class="cs-hex">#243E36</span></div>
                              <div class="cs-color"><div class="cs-swatch" style="background:#7CA982;"></div><span class="cs-hex">#7CA982</span></div>
                              <div class="cs-color"><div class="cs-swatch" style="background:#E0EEC6;"></div><span class="cs-hex">#E0EEC6</span></div>
                              <div class="cs-color"><div class="cs-swatch" style="background:#C2A83E;"></div><span class="cs-hex">#C2A83E</span></div>
                              <div class="cs-color"><div class="cs-swatch" style="background:#F1F7ED;"></div><span class="cs-hex">#F1F7ED</span></div>
                          </div>
                      </div>`;
                      
                      htmlStr += `<div class="cs-section"><h2 class="cs-heading">Logo & Identity</h2><div class="masonry-container">`;
                      if(logo) htmlStr += renderMedia(logo).replace('masonry-item', 'masonry-item full-width');
                      htmlStr += `</div></div>`;
  
                      htmlStr += `<div class="cs-section"><h2 class="cs-heading">Posters & Events</h2><div class="masonry-container">`;
                      posters.forEach(f => { htmlStr += renderMedia(f); });
                      htmlStr += `</div></div>`;
  
                      htmlStr += `<div class="cs-section"><h2 class="cs-heading">Digital & App Mockups</h2><div class="masonry-container">`;
                      digital.forEach(f => { htmlStr += renderMedia(f); });
                      htmlStr += `</div></div>`;
  
                      htmlStr += `<div class="cs-section"><h2 class="cs-heading">Merchandise</h2><div class="masonry-container">`;
                      merch.forEach(f => { htmlStr += renderMedia(f); });
                      htmlStr += `</div></div>`;
                  } else if (id === 'ntu-fest') {
                      const video = findFile('youtu.be');
                      const cover = findFile('ntu fest cover');
                      const banner = findFile('ntufest_banner');
                      const performers = findFiles('performer images');
                      const vendor = findFile('SIGN UP');
                      const sundown = findFile('SunDown');
                      
                      htmlStr += `<div class="cs-section">
                          <div style="background:var(--surf); padding: 3rem; border-radius:12px; margin-bottom: 2rem; border: 1px solid var(--line);">
                              <h2 style="font-family:'Clash Display'; font-size:2.2rem; margin-bottom:1rem; margin-top:0;">Stepping up for NTU Fest</h2>
                              <p style="font-size:1.1rem; line-height:1.7; color:var(--ink5); margin-bottom:1.5rem;">
                                  <strong>Fun fact:</strong> I originally joined the committee in a different role, but when the original Publicity Director unexpectedly stepped down, I took over the position to ensure the festival's branding and outreach didn't skip a beat. All the production elements were primarily created using Canva and CapCut.
                              </p>
                              <div style="display:flex; flex-wrap:wrap; gap:1rem;">
                                  <div style="background:var(--bg); padding:0.8rem 1.5rem; border-radius:8px; border:1px solid var(--line); font-weight:600; font-size:0.95rem;">
                                      🌟 View the live 2024 graphics at <a href="https://instagram.com/ntufest" target="_blank" style="color:var(--blue); text-decoration:none;">@ntufest</a>
                                  </div>
                              </div>
                          </div>
                      </div>`;
  
                      htmlStr += `<div class="cs-section"><h2 class="cs-heading" style="font-size:1.8rem; margin-bottom:1.5rem; border-bottom:1px solid var(--ink12); padding-bottom:0.5rem;">Promotional Video</h2><div class="masonry-container">`;
                      if (video) htmlStr += renderMedia(video).replace('masonry-item', 'masonry-item full-width');
                      htmlStr += `</div></div>`;
                      
                      htmlStr += `<div class="cs-section"><h2 class="cs-heading" style="font-size:1.8rem; margin-bottom:1.5rem; border-bottom:1px solid var(--ink12); padding-bottom:0.5rem;">Hero & Banners</h2><div class="masonry-container">`;
                      if (cover) htmlStr += renderMedia(cover).replace('masonry-item', 'masonry-item full-width');
                      if (banner) htmlStr += renderMedia(banner).replace('masonry-item', 'masonry-item full-width');
                      if (sundown) htmlStr += renderMedia(sundown);
                      if (vendor) htmlStr += renderMedia(vendor);
                      htmlStr += `</div></div>`;
                      
                      if (performers.length > 0) {
                          htmlStr += `<div class="cs-section"><h2 class="cs-heading" style="font-size:1.8rem; margin-bottom:1.5rem; border-bottom:1px solid var(--ink12); padding-bottom:0.5rem;">Performer Lineup Announcements</h2><div class="masonry-container">`;
                          performers.forEach(f => { htmlStr += renderMedia(f); });
                          htmlStr += `</div></div>`;
                      }
                  } else if (id === 'nangele') {
                      htmlStr += `<div style="text-align:center; padding:3rem; background:var(--surf); border-radius:4px; margin-bottom:2rem;"><h2 style="margin-bottom:1rem; font-family:var(--fd);">Read the Comic</h2><p style="color:var(--ink5); margin-bottom:2rem;">Click below to open the interactive comic reader.</p><button onclick="openComicReader()" style="padding:1rem 2.5rem; font-size:1.1rem; background:var(--ink); color:var(--bg); border:none; border-radius:2px; font-weight:600; cursor:pointer;">Open Reader</button></div>`;
                      htmlStr += `<div class="masonry-container">`;
                      media.forEach(f => { htmlStr += renderMedia(f, true); });
                      htmlStr += `</div>`;
                  } else if (id === 'original-tracks' || id === 'wellbeing-planner') {
                      htmlStr += `<div class="masonry-container">`;
                      media.forEach(f => { htmlStr += renderMedia(f); });
                      htmlStr += `</div>`;
                  }
                  
                  gal.innerHTML = htmlStr;
                  return; // VERY IMPORTANT: Stop execution here so it doesn't run the default handler!
            }
            
            // Default handling for other galleries
"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(prefix + new_block + suffix)
        print("Successfully rebuilt entire case studies block!")
    else:
        print("FAILED to find bounds.")
