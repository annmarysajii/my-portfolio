import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_ga_logic = """              } else if (id === 'green-arrow') {
                  const apps = findFiles('poster').concat(findFiles('mockup')).concat(findFiles('carousel'));
                  const inContext = findFiles('tote').concat(findFiles('t-shirt'));
                  
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
                  
                  htmlStr += `<div class="cs-section"><h2 class="cs-heading">Brand Identity & Applications</h2><div class="masonry-container">`;
                  const identityFiles = notFound([...inContext].filter(Boolean));
                  identityFiles.forEach(f => { htmlStr += renderMedia(f); });
                  htmlStr += `</div></div>`;
                  
                  htmlStr += `<div class="cs-section"><h2 class="cs-heading">In Context / Real-World Mockups</h2><div class="masonry-container">`;
                  inContext.forEach(f => { htmlStr += renderMedia(f).replace('masonry-item', 'masonry-item in-context-img'); });
                  htmlStr += `</div></div>`;
              }"""

new_ga_logic = """              } else if (id === 'green-arrow') {
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

                  htmlStr += `<div class="cs-section"><h2 class="cs-heading">Digital & Social Media</h2><div class="masonry-container">`;
                  digital.forEach(f => { htmlStr += renderMedia(f); });
                  htmlStr += `</div></div>`;
                  
                  htmlStr += `<div class="cs-section"><h2 class="cs-heading">Merchandise</h2><div class="masonry-container">`;
                  merch.forEach(f => { htmlStr += renderMedia(f).replace('masonry-item', 'masonry-item in-context-img'); });
                  htmlStr += `</div></div>`;
              }"""

html = html.replace(old_ga_logic, new_ga_logic)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated Green Arrow sorting")
