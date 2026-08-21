import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Locate the gallery generation block
block_start = "let htmlStr = '';"
block_end = "gal.innerHTML = htmlStr;"

# We will replace everything from block_start to block_end
new_logic = """
          if (id === 'jasmine-album') {
              const imgs = media.filter(f => f.match(/\\.(png|jpe?g)$/i));
              const audios = media.filter(f => f.match(/\\.(wav|mp3|m4a)$/i));
              
              let albumHtml = '<style>.album-grid{display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:2rem;}</style><div class="album-grid">';
              for(let i=0; i<Math.max(imgs.length, audios.length); i++) {
                  let img = imgs[i] ? `<img src="${imgs[i]}" style="width:100%; height:auto; border-radius:4px 4px 0 0; display:block;">` : '';
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

          let styleBlock = `<style>
            .masonry-grid { column-count: 1; column-gap: 1.5rem; }
            @media(min-width: 768px) { .masonry-grid { column-count: 2; } }
            @media(min-width: 1024px) { .masonry-grid { column-count: 3; } }
            .comic-grid { max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; gap: 1rem; }
          </style>`;
          
          const isComic = id === 'nangele' || id === 'internship-comics' || id === 'wellbeing-planner' || id === 'jasmine-comic';
          let htmlStr = styleBlock + `<div class="${isComic ? 'comic-grid' : 'masonry-grid'}">`;
          
          media.forEach((file, idx) => {
              let el = '';
              const isVideo = !!file.match(/\\.(mp4|mov|webm)$/i);
              const isAudio = !!file.match(/\\.(m4a|mp3|wav)$/i);
              const isYouTube = !!file.match(/youtube\\.com|youtu\\.be/i);
              const isPDF = !!file.match(/\\.pdf$/i);
              
              if (isYouTube) {
                  let embedUrl = file;
                  const ytMatch = file.match(/(?:youtu\\.be\\/|youtube\\.com\\/(?:watch\\?v=|embed\\/))([^&\\?]+)/);
                  if (ytMatch && ytMatch[1]) {
                      embedUrl = `https://www.youtube.com/embed/${ytMatch[1]}`;
                  }
                  el = `<iframe src="${embedUrl}" style="width:100%; aspect-ratio:16/9; display:block; border-radius:4px; border:none;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`;
              } else if (isVideo) {
                  el = `<video src="${file}" controls style="width:100%; height:auto; display:block; background:var(--surf); border-radius:4px;"></video>`;
              } else if (isAudio) {
                  el = `<div style="display:flex; align-items:center; justify-content:center; width:100%; background:var(--surf); padding:2rem; border-radius:4px;"><audio src="${file}" controls style="width:100%;"></audio></div>`;
              } else if (isPDF) {
                  el = `<iframe src="${file}" style="width:100%; height:85vh; border:none; border-radius:4px; background:var(--surf);"></iframe>`;
              } else {
                  el = `<img src="${file}" alt="" style="width:100%; height:auto; display:block; background:var(--surf); border-radius:4px;">`;
              }
              
              if (isComic) {
                  htmlStr += `<div>${el}</div>`;
              } else {
                  htmlStr += `<div style="margin-bottom:1.5rem; break-inside:avoid;">${el}</div>`;
              }
          });
          htmlStr += '</div>';
          gal.innerHTML = htmlStr;
"""

# Now we need to safely replace the old block.
# Since the old block spans multiple lines and has varying indentation, we will use regex DOTALL.
pattern = re.compile(r"let htmlStr = '';.*?gal\.innerHTML = htmlStr;", re.DOTALL)
html = pattern.sub(new_logic, html)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated project.html gallery generation logic")
