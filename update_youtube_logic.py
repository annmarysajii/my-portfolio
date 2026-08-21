import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add YouTube support to project.html
yt_logic = """const isVideo = !!file.match(/\.(mp4|mov|webm)$/i);
            const isAudio = !!file.match(/\.(m4a|mp3|wav)$/i);
            const isYouTube = !!file.match(/youtube\.com|youtu\.be/i);
            
            if (isYouTube) {
                let embedUrl = file;
                const ytMatch = file.match(/(?:youtu\.be\/|youtube\.com\/(?:watch\?v=|embed\/))([^&\?]+)/);
                if (ytMatch && ytMatch[1]) {
                    embedUrl = `https://www.youtube.com/embed/${ytMatch[1]}`;
                }
                el = `<iframe src="${embedUrl}" style="width:100%; aspect-ratio:16/9; display:block; border-radius:4px; border:none;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`;
            } else if (isVideo) {"""

html = html.replace('const isVideo = !!file.match(/\.(mp4|mov|webm)$/i);\n              const isAudio = !!file.match(/\.(m4a|mp3|wav)$/i);\n              \n              if (isVideo) {', yt_logic)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Added YouTube support to project.html")

with open('portfolio.html', 'r', encoding='utf-8') as f:
    phtml = f.read()

# Add YouTube support to portfolio.html thumbnail loader
p_yt_logic = """const file = data[id].find(f => f.match(/\.(png|jpe?g|gif|webm|mp4|mov)$/i) || f.match(/youtube\.com|youtu\.be/i)) || data[id][0];
        if (file) {
          const isYouTube = !!file.match(/youtube\.com|youtu\.be/i);
          if (isYouTube) {
              const ytMatch = file.match(/(?:youtu\.be\/|youtube\.com\/(?:watch\?v=|embed\/))([^&\?]+)/);
              const ytId = ytMatch ? ytMatch[1] : '';
              a.innerHTML = `<img src="https://img.youtube.com/vi/${ytId}/maxresdefault.jpg" alt="YouTube Video" style="width:100%;height:auto;object-fit:contain;background:var(--surf);border-radius:2px;" onerror="this.src='https://img.youtube.com/vi/${ytId}/hqdefault.jpg'">`;
          } else if (file.match(/\.(mp4|mov|webm)$/i)) {"""

# Replace old logic
old_p_logic = """const file = data[id].find(f => f.match(/\.(png|jpe?g|gif|webm|mp4|mov)$/i)) || data[id][0];
        if (file) {
          if (file.match(/\.(mp4|mov|webm)$/i)) {"""

phtml = phtml.replace(old_p_logic, p_yt_logic)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(phtml)
print("Added YouTube support to portfolio.html thumbnails")
