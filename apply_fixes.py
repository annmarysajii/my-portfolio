import os
import re

# 1. Update data.js
with open('scripts/data.js', 'r', encoding='utf-8') as f:
    data_js = f.read()

# Fix keep-yourself-safe
data_js = data_js.replace('      "assets/portfolio-data/Keep yourself safe/shotee.png"\n', '')
# Ensure no trailing comma
data_js = data_js.replace(',\n    ],\n    "music-district-video"', '\n    ],\n    "music-district-video"')

# Fix dear-friend
dear_friend_imgs = [
    '"assets/portfolio-data/Dear friend/credit1.png"',
    '"assets/portfolio-data/Dear friend/rain7.png"',
    '"assets/portfolio-data/Dear friend/room layout.png"',
    '"assets/portfolio-data/Dear friend/staticshot_4.png"',
    '"assets/portfolio-data/Dear friend/topshotd.png"'
]
df_replacement = '"dear-friend": [\n      "https://youtu.be/BPYEYUmrWfg",\n      ' + ',\n      '.join(dear_friend_imgs) + '\n    ]'
data_js = re.sub(r'"dear-friend": \[\n\s*"https://youtu\.be/BPYEYUmrWfg"\n\s*\]', df_replacement, data_js)

with open('scripts/data.js', 'w', encoding='utf-8') as f:
    f.write(data_js)

# 2. Fix portfolio.html CSS
with open('portfolio.html', 'r', encoding='utf-8') as f:
    port_html = f.read()

# Add display:block to card-img to prevent inline-block bottom gap overlap
port_html = port_html.replace('.card-img{position:relative;', '.card-img{display:block;position:relative;')

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(port_html)

# 3. Make YouTube video bigger in project.html
with open('project.html', 'r', encoding='utf-8') as f:
    proj_html = f.read()

old_video_div = """              return `
              <div class="${isComic ? 'comic-item' : 'masonry-item'}">
                  <div class="video-container" """

new_video_div = """              return `
              <div class="${isComic ? 'comic-item' : 'masonry-item full-width'}" style="column-span: all; margin-bottom: 2rem;">
                  <div class="video-container" """

proj_html = proj_html.replace(old_video_div, new_video_div)

# Make full-width work with CSS column layout
proj_html = proj_html.replace('.masonry-item { break-inside: avoid; margin-bottom: 1.5rem; }', '.masonry-item { break-inside: avoid; margin-bottom: 1.5rem; }\n              .masonry-item.full-width { column-span: all; width: 100%; max-width: 900px; margin: 0 auto 3rem auto; }')

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(proj_html)

print("Applied fixes")
