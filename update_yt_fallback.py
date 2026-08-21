import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_yt = """if (ytMatch && ytMatch[1]) {
                      embedUrl = `https://www.youtube-nocookie.com/embed/${ytMatch[1]}?rel=0&modestbranding=1&origin=https://annmarysaji.github.io`;
                  }
                  el = `<iframe src="${embedUrl}" style="width:100%; aspect-ratio:16/9; display:block; border-radius:4px; border:none;" allow="fullscreen; encrypted-media; picture-in-picture" allowfullscreen></iframe>`;"""

new_yt = """if (ytMatch && ytMatch[1]) {
                      const ytId = ytMatch[1];
                      if (window.location.protocol === 'file:') {
                          const watchUrl = `https://www.youtube.com/watch?v=${ytId}`;
                          const thumbUrl = `https://img.youtube.com/vi/${ytId}/maxresdefault.jpg`;
                          el = `<div style="position:relative; width:100%; aspect-ratio:16/9; background:#111; border-radius:4px; overflow:hidden;">
                              <img src="${thumbUrl}" style="width:100%; height:100%; object-fit:cover; opacity:0.5;" onerror="this.src='https://img.youtube.com/vi/${ytId}/hqdefault.jpg'">
                              <a href="${watchUrl}" target="_blank" style="position:absolute; inset:0; display:flex; flex-direction:column; align-items:center; justify-content:center; text-decoration:none; color:white; transition:transform 0.2s;">
                                  <svg width="68" height="48" viewBox="0 0 68 48"><path fill="#FF0000" d="M66.52 7.74c-.78-2.93-2.49-5.41-5.42-6.19C55.79.13 34 .13 34 .13s-21.79 0-27.1.14c-2.93.78-4.64 3.26-5.42 6.19C1.34 11.55 1.34 24 1.34 24s0 12.45.14 16.26c.78 2.93 2.49 5.41 5.42 6.19C12.21 47.87 34 47.87 34 47.87s21.79 0 27.1-.14c2.93-.78 4.64-3.26 5.42-6.19C66.66 36.45 66.66 24 66.66 24s0-12.45-.14-16.26z"/><path fill="#FFFFFF" d="M45 24 27 14v20z"/></svg>
                                  <div style="margin-top:1rem; font-family:'Clash Display',sans-serif; font-size:1.2rem; background:rgba(0,0,0,0.7); padding:0.5rem 1rem; border-radius:4px; text-align:center;">Watch on YouTube<br><span style="font-size:0.9rem; font-family:'General Sans',sans-serif; font-weight:normal; color:#ccc;">(Local preview mode)</span></div>
                              </a>
                          </div>`;
                      } else {
                          embedUrl = `https://www.youtube-nocookie.com/embed/${ytId}?rel=0&modestbranding=1`;
                          el = `<iframe src="${embedUrl}" style="width:100%; aspect-ratio:16/9; display:block; border-radius:4px; border:none;" allow="fullscreen; encrypted-media; picture-in-picture" allowfullscreen></iframe>`;
                      }
                  }"""

html = html.replace(old_yt, new_yt)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated video embed logic to detect file:// protocol")
