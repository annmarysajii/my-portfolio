import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make all videos span full width, fix iframe URL
old_yt = """if (ytMatch && ytMatch[1]) {
                      embedUrl = `https://www.youtube.com/embed/${ytMatch[1]}`;
                  }
                  el = `<iframe src="${embedUrl}" style="width:100%; aspect-ratio:16/9; display:block; border-radius:4px; border:none;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`;"""

new_yt = """if (ytMatch && ytMatch[1]) {
                      embedUrl = `https://www.youtube-nocookie.com/embed/${ytMatch[1]}?rel=0&modestbranding=1&origin=https://annmarysaji.github.io`;
                  }
                  el = `<iframe src="${embedUrl}" style="width:100%; aspect-ratio:16/9; display:block; border-radius:4px; border:none;" allow="fullscreen; encrypted-media; picture-in-picture" allowfullscreen></iframe>`;"""

html = html.replace(old_yt, new_yt)

# Make videos span 100% full width (grid-column: 1 / -1)
old_append = """if (isComic) {
                  htmlStr += `<div>${el}</div>`;
              } else {
                  htmlStr += `<div style="margin-bottom:1.5rem; background:var(--surf); border-radius:4px; overflow:hidden;">${el}</div>`;
              }"""
new_append = """if (isComic) {
                  htmlStr += `<div>${el}</div>`;
              } else {
                  let wrapperStyle = "margin-bottom:1.5rem; background:var(--surf); border-radius:4px; overflow:hidden;";
                  if (isVideo || isYouTube) {
                      wrapperStyle += " grid-column: 1 / -1;"; // Make films huge
                  }
                  htmlStr += `<div style="${wrapperStyle}">${el}</div>`;
              }"""

html = html.replace(old_append, new_append)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated video embed URL and grid-column for full width.")
