import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract the script block
script_pattern = re.compile(r'(// RENDER\s*const id.*?)(</script>)', re.DOTALL)
match = script_pattern.search(html)

if not match:
    print("Could not find script block")
    exit(1)

old_script = match.group(1)

new_script = """// RENDER
  const id = new URLSearchParams(location.search).get('id');
  const p = PROJECTS[id];
  const main = document.getElementById('main');
  
  if (p) {
      let badges = '';
      if (p.badge) {
          const bs = Array.isArray(p.badge) ? p.badge : [p.badge];
          bs.forEach(b => badges += `<span class="badge bs">${b}</span>`);
      }
      const tools = (p.tools || []).map(t => `<span class="tool">${t}</span>`).join('');
      
      main.innerHTML = `
      <header class="ph-header">
          ${badges ? `<div class="ph-badges">${badges}</div>` : ''}
          <h1 class="ph-title">${p.name}</h1>
          <p class="ph-desc">${p.role}</p>
          ${tools ? `<div class="card-tools" style="margin-top:1.5rem;">${tools}</div>` : ''}
      </header>
      <div id="dynamic-gallery"></div>
      <div class="ph-foot">
          <a href="index.html" class="ph-back">← Back to Portfolio</a>
      </div>
      `;
  }

  // Format string for captions and alt text
  function formatName(str) {
      let name = str.split('/').pop().replace(/\\.[^/.]+$/, "");
      name = name.replace(/[-_]/g, ' ').replace(/\\s*\\(\\d+\\)\\s*/g, ' ').trim();
      return name.charAt(0).toUpperCase() + name.slice(1);
  }

  function renderMedia(file, isComic = false) {
      const isVideo = !!file.match(/\\.(mp4|mov|webm)$/i);
      const isAudio = !!file.match(/\\.(m4a|mp3|wav)$/i);
      const isYouTube = !!file.match(/youtube\\.com|youtu\\.be/i);
      const isPDF = !!file.match(/\\.pdf$/i);
      const name = formatName(file);
      
      let el = '';
      if (isYouTube) {
          const ytMatch = file.match(/(?:youtu\\.be\\/|youtube\\.com\\/(?:watch\\?v=|embed\\/))([^&\\?]+)/);
          if (ytMatch && ytMatch[1]) {
              const ytId = ytMatch[1];
              if (window.location.protocol === 'file:' || window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
                  const watchUrl = `https://www.youtube.com/watch?v=${ytId}`;
                  const thumbUrl = `https://img.youtube.com/vi/${ytId}/maxresdefault.jpg`;
                  el = `<div class="media-el full-width yt-fallback" style="position:relative; width:100%; aspect-ratio:16/9; background:#111; border-radius:4px; overflow:hidden; break-inside: avoid; margin-bottom: 2rem;">
                      <img src="${thumbUrl}" alt="${name}" style="width:100%; height:100%; object-fit:cover; opacity:0.5;" onerror="this.src='https://img.youtube.com/vi/${ytId}/hqdefault.jpg'">
                      <a href="${watchUrl}" target="_blank" style="position:absolute; inset:0; display:flex; flex-direction:column; align-items:center; justify-content:center; text-decoration:none; color:white; transition:transform 0.2s;">
                          <svg width="68" height="48" viewBox="0 0 68 48"><path fill="#FF0000" d="M66.52 7.74c-.78-2.93-2.49-5.41-5.42-6.19C55.79.13 34 .13 34 .13s-21.79 0-27.1.14c-2.93.78-4.64 3.26-5.42 6.19C1.34 11.55 1.34 24 1.34 24s0 12.45.14 16.26c.78 2.93 2.49 5.41 5.42 6.19C12.21 47.87 34 47.87 34 47.87s21.79 0 27.1-.14c2.93-.78 4.64-3.26 5.42-6.19C66.66 36.45 66.66 24 66.66 24s0-12.45-.14-16.26z"/><path fill="#FFFFFF" d="M45 24 27 14v20z"/></svg>
                          <div style="margin-top:1rem; font-family:'Clash Display',sans-serif; font-size:1.2rem; background:rgba(0,0,0,0.7); padding:0.5rem 1rem; border-radius:4px; text-align:center;">Watch on YouTube<br><span style="font-size:0.9rem; font-family:'General Sans',sans-serif; font-weight:normal; color:#ccc;">(Local preview mode)</span></div>
                      </a>
                  </div>`;
              } else {
                  const embedUrl = `https://www.youtube.com/embed/${ytId}?rel=0&modestbranding=1`;
                  el = `<iframe class="media-el full-width" src="${embedUrl}" style="width:100%; aspect-ratio:16/9; display:block; border-radius:4px; border:none; break-inside: avoid; margin-bottom: 2rem;" allow="fullscreen; encrypted-media; picture-in-picture" allowfullscreen></iframe>`;
              }
          }
      } else if (isVideo) {
          el = `<video class="media-el full-width" src="${file}" controls style="width:100%; height:auto; display:block; background:var(--surf); border-radius:4px; break-inside: avoid; margin-bottom: 2rem;"></video>`;
      } else if (isAudio) {
          el = `<div class="media-el" style="background:var(--surf); border:1px solid var(--line); border-radius:4px; overflow:hidden; padding:2rem; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:1.5rem; aspect-ratio:4/3; break-inside: avoid; margin-bottom: 2rem;">
            <div style="width:100px; height:100px; border-radius:50%; background:var(--ink07); display:flex; align-items:center; justify-content:center;">
                <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18V5l12-2v13"></path><circle cx="6" cy="18" r="3"></circle><circle cx="18" cy="16" r="3"></circle></svg>
            </div>
            <div style="font-weight:600; font-size:1.1rem; text-align:center;">${name}</div>
            <audio src="${file}" controls style="width:100%; outline:none; height:40px;"></audio>
          </div>`;
      } else if (isPDF) {
          el = `<iframe class="media-el full-width" src="${file}" style="width:100%; height:85vh; border:none; border-radius:4px; background:var(--surf); break-inside: avoid; margin-bottom: 2rem;"></iframe>`;
      } else {
          el = `<img class="media-el" src="${file}" alt="${name}" style="width:100%; height:auto; display:block; background:var(--surf); border-radius:4px;">`;
      }
      
      const captionHtml = (isYouTube || isPDF || isAudio || isComic) ? '' : `<div class="media-caption">${name}</div>`;
      
      return `<div class="masonry-item ${isComic ? 'comic-item' : ''}">${el}${captionHtml}</div>`;
  }

  window.onload = () => {
    let checkData = setInterval(() => {
      if (window.PORTFOLIO_DATA) {
          clearInterval(checkData);
          const data = window.PORTFOLIO_DATA;
          
          if (id === 'gobunny') {
              document.documentElement.style.setProperty('--bg', '#FFEBF0');
              document.documentElement.style.setProperty('--surf', '#FFF5F7');
              document.documentElement.style.setProperty('--ink', '#D02F5A');
              document.documentElement.style.setProperty('--line', 'rgba(208, 47, 90, 0.2)');
              document.querySelector('.con').style.maxWidth = '1200px';
          } else if (id === 'green-arrow') {
              document.documentElement.style.setProperty('--bg', '#EBF4ED');
              document.documentElement.style.setProperty('--surf', '#F4F9F5');
              document.documentElement.style.setProperty('--ink', '#2B5E39');
              document.documentElement.style.setProperty('--line', 'rgba(43, 94, 57, 0.2)');
              document.querySelector('.con').style.maxWidth = '1200px';
          }

          let rawMedia = data[id] || [];
          
          // Filter out missing image placeholders
          const media = rawMedia.filter(f => !f.toLowerCase().includes('image coming soon') && !f.toLowerCase().includes('placeholder'));

          const gal = document.getElementById('dynamic-gallery');
          if (media.length === 0) {
              gal.innerHTML = `<div class="gallery-hero"><div class="tape tape-tl"></div><div class="tape tape-tr"></div><span class="ph-label">Media coming soon</span></div>`;
              return;
          }
          
          let styleBlock = `<style>
            /* Sitewide CSS Columns Masonry */
            .masonry-container {
                column-count: 3;
                column-gap: 1.5rem;
                width: 100%;
            }
            .masonry-item {
                break-inside: avoid;
                margin-bottom: 2.5rem;
                position: relative;
            }
            .masonry-item.full-width {
                column-span: all;
            }
            .media-caption {
                font-size: 0.75rem;
                font-weight: 500;
                letter-spacing: 0.04em;
                text-transform: uppercase;
                color: rgba(120, 120, 120, 0.8);
                margin-top: 0.75rem;
                text-align: left;
            }
            
            /* Comic styling */
            .comic-grid { max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; gap: 0rem; }
            .comic-item { margin-bottom: 0; }
            .comic-item img { border-radius: 0 !important; }
            
            /* Responsive Masonry */
            @media (max-width: 900px) { .masonry-container { column-count: 2; } }
            @media (max-width: 600px) { .masonry-container { column-count: 1; } }

            /* Case Study Sections */
            .cs-section { margin-top: 4rem; margin-bottom: 2rem; break-inside: avoid; column-span: all; }
            .cs-heading {
                font-family: var(--fd);
                font-size: clamp(2rem, 4vw, 2.5rem);
                font-weight: 700;
                line-height: 1;
                margin-bottom: 1.5rem;
                border-bottom: 2px solid var(--line);
                padding-bottom: 0.5rem;
            }
            .cs-palettes { display: flex; flex-wrap: wrap; gap: 1rem; margin-bottom: 2rem; }
            .cs-color {
                flex: 1 1 100px;
                display: flex;
                flex-direction: column;
                gap: 0.5rem;
            }
            .cs-swatch {
                aspect-ratio: 1;
                border-radius: 4px;
                box-shadow: inset 0 0 0 1px rgba(0,0,0,0.1);
            }
            .cs-hex {
                font-size: 0.85rem;
                font-family: var(--fb);
                color: var(--ink);
                text-transform: uppercase;
            }
            .in-context-img img {
                box-shadow: 0 12px 24px rgba(0,0,0,0.15);
                transform: scale(1.02);
            }
            
            [data-theme='dark'] .media-caption { color: rgba(250,248,244,.5); }
            [data-theme='dark'] .cs-swatch { box-shadow: inset 0 0 0 1px rgba(255,255,255,0.1); }
          </style>`;

          if (id === 'jasmine-album') {
              const imgs = media.filter(f => f.match(/\\/\\d\\.(png|jpe?g)$/i)).sort();
              const audios = media.filter(f => f.match(/\\.(wav|mp3|m4a)$/i));
              
              let albumHtml = styleBlock + '<style>.album-grid{display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:2rem;}</style><div class="album-grid">';
              const count = Math.min(imgs.length, audios.length);
              for(let i=0; i<count; i++) {
                  let img = imgs[i] ? `<img src="${imgs[i]}" alt="Track ${i+1}" style="width:100%; height:auto; border-radius:4px 4px 0 0; display:block;">` : '';
                  let aud = audios[i] ? `<audio src="${audios[i]}" controls style="width:100%; outline:none; height:40px;"></audio>` : '';
                  let title = audios[i] ? audios[i].split('/').pop().replace(/\\.(wav|mp3|m4a)$/i, '') : `Track ${i+1}`;
                  albumHtml += `<div style="background:var(--surf); border:1px solid var(--line); border-radius:4px; overflow:hidden;">
                      ${img}
                      <div style="padding:1rem;">
                        <div style="font-weight:600; font-family:'Clash Display', sans-serif; margin-bottom:0.5rem; font-size:1.1rem;">${title}</div>
                        ${aud}
                      </div>
                  </div>`;
              }
              albumHtml += '</div>';
              gal.innerHTML = albumHtml;
              return;
          }

          // Native Case Studies
          if (id === 'gobunny' || id === 'green-arrow') {
              let htmlStr = styleBlock;
              
              const findFile = (keyword) => media.find(f => f.toLowerCase().includes(keyword.toLowerCase()));
              const findFiles = (keyword) => media.filter(f => f.toLowerCase().includes(keyword.toLowerCase()));
              const notFound = (list) => media.filter(f => !list.includes(f));
              
              if (id === 'gobunny') {
                  const logoPrimary = findFile('GO BUNNY');
                  const logoSecondary = findFiles('Your paragraph text').filter(f => f.includes('35') || f.includes('36') || f.includes('33')); 
                  const pack1 = findFile('3.png');
                  const pack2 = findFile('4.png');
                  const apps = findFiles('ART DIRECTION PORTFOLIO').concat(findFiles('Your paragraph text (37)')).concat(findFiles('Your paragraph text (30)'));
                  const inContext = findFiles('It is time for some strawberries');
                  
                  // Palette
                  htmlStr += `
                  <div class="cs-section">
                      <h2 class="cs-heading">Concept / Mood</h2>
                      <div class="masonry-container">
                  `;
                  // We can infer mood from other unlisted files if any, but let's just group leftovers here if they fit, else skip
                  const otherConcept = notFound([logoPrimary, ...logoSecondary, pack1, pack2, ...apps, ...inContext].filter(Boolean));
                  otherConcept.forEach(f => { htmlStr += renderMedia(f); });
                  htmlStr += `</div></div>`;

                  htmlStr += `
                  <div class="cs-section">
                      <h2 class="cs-heading">Color Palette</h2>
                      <div class="cs-palettes">
                          <div class="cs-color"><div class="cs-swatch" style="background:#D02F5A;"></div><span class="cs-hex">#D02F5A</span></div>
                          <div class="cs-color"><div class="cs-swatch" style="background:#FFEBF0;"></div><span class="cs-hex">#FFEBF0</span></div>
                          <div class="cs-color"><div class="cs-swatch" style="background:#FFF5F7;"></div><span class="cs-hex">#FFF5F7</span></div>
                          <div class="cs-color"><div class="cs-swatch" style="background:#E26F8D;"></div><span class="cs-hex">#E26F8D</span></div>
                          <div class="cs-color"><div class="cs-swatch" style="background:#F2A4B8;"></div><span class="cs-hex">#F2A4B8</span></div>
                      </div>
                  </div>`;
                  
                  htmlStr += `<div class="cs-section"><h2 class="cs-heading">Logo & Mark</h2><div class="masonry-container">`;
                  if(logoPrimary) htmlStr += renderMedia(logoPrimary).replace('masonry-item', 'masonry-item full-width'); // Make primary lockup prominent
                  logoSecondary.forEach(f => { htmlStr += renderMedia(f); });
                  htmlStr += `</div></div>`;
                  
                  htmlStr += `<div class="cs-section"><h2 class="cs-heading">Packaging / Product Design</h2><div class="masonry-container">`;
                  if(pack1) htmlStr += renderMedia(pack1);
                  if(pack2) htmlStr += renderMedia(pack2);
                  htmlStr += `</div></div>`;
                  
                  htmlStr += `<div class="cs-section"><h2 class="cs-heading">Applications</h2><div class="masonry-container">`;
                  apps.forEach(f => { htmlStr += renderMedia(f); });
                  htmlStr += `</div></div>`;
                  
                  htmlStr += `<div class="cs-section"><h2 class="cs-heading">In Context</h2><div class="masonry-container">`;
                  inContext.forEach(f => { htmlStr += renderMedia(f).replace('masonry-item', 'masonry-item in-context-img'); });
                  htmlStr += `</div></div>`;
              } else if (id === 'green-arrow') {
                  const apps = findFiles('poster').concat(findFiles('mockup')).concat(findFiles('carousel'));
                  const inContext = findFiles('tote').concat(findFiles('t-shirt'));
                  
                  htmlStr += `
                  <div class="cs-section">
                      <h2 class="cs-heading">Color Palette</h2>
                      <div class="cs-palettes">
                          <div class="cs-color"><div class="cs-swatch" style="background:#2B5E39;"></div><span class="cs-hex">#2B5E39</span></div>
                          <div class="cs-color"><div class="cs-swatch" style="background:#EBF4ED;"></div><span class="cs-hex">#EBF4ED</span></div>
                          <div class="cs-color"><div class="cs-swatch" style="background:#F4F9F5;"></div><span class="cs-hex">#F4F9F5</span></div>
                          <div class="cs-color"><div class="cs-swatch" style="background:#558F65;"></div><span class="cs-hex">#558F65</span></div>
                          <div class="cs-color"><div class="cs-swatch" style="background:#8FBC9B;"></div><span class="cs-hex">#8FBC9B</span></div>
                      </div>
                  </div>`;
                  
                  htmlStr += `<div class="cs-section"><h2 class="cs-heading">Brand Identity & Applications</h2><div class="masonry-container">`;
                  const identityFiles = notFound([...inContext].filter(Boolean));
                  identityFiles.forEach(f => { htmlStr += renderMedia(f); });
                  htmlStr += `</div></div>`;
                  
                  htmlStr += `<div class="cs-section"><h2 class="cs-heading">In Context / Real-World Mockups</h2><div class="masonry-container">`;
                  inContext.forEach(f => { htmlStr += renderMedia(f).replace('masonry-item', 'masonry-item in-context-img'); });
                  htmlStr += `</div></div>`;
              }
              
              gal.innerHTML = htmlStr;
              return;
          }

          // Default handling for other galleries
          const isComic = id === 'nangele' || id === 'internship-comics' || id === 'wellbeing-planner' || id === 'jasmine-comic';
          let htmlStr = styleBlock + `<div class="${isComic ? 'comic-grid' : 'masonry-container'}">`;
          
          media.forEach((file) => {
              htmlStr += renderMedia(file, isComic);
          });
          htmlStr += '</div>';
          gal.innerHTML = htmlStr;

    }
    }, 50);
  }
"""

new_html = html[:match.start(1)] + new_script + html[match.end(2):]

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
print("Updated project.html successfully")
