import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

injector = """<script>
fetch('assets/portfolio-data.json').then(r=>r.json()).then(data => {
  document.querySelectorAll('a.card-img').forEach(a => {
    const href = a.getAttribute('href');
    if (href && href.includes('id=')) {
      const id = href.split('id=')[1];
      if (data[id] && data[id].length > 0) {
        const file = data[id].find(f => f.match(/\.(png|jpe?g|gif|webm|mp4|mov)$/i)) || data[id][0];
        if (file) {
          if (file.match(/\.(mp4|mov|webm)$/i)) {
            a.innerHTML = `<video src="${file}" autoplay loop muted playsinline style="width:100%;height:100%;object-fit:cover;"></video>`;
          } else if (file.match(/\.(png|jpe?g|gif)$/i)) {
            a.innerHTML = `<img src="${file}" alt="" style="width:100%;height:100%;object-fit:cover;">`;
          } else if (file.match(/\.(pdf)$/i)) {
            a.innerHTML = `<div class="ph"><i data-lucide="file-text" class="ph-icon" style="width:32px;height:32px;margin-bottom:.5rem;"></i><span class="ph-label">PDF Document</span></div>`;
          } else if (file.match(/\.(mp3|wav|m4a)$/i)) {
            a.innerHTML = `<div class="ph"><i data-lucide="music" class="ph-icon" style="width:32px;height:32px;margin-bottom:.5rem;"></i><span class="ph-label">Audio Track</span></div>`;
          }
        }
      }
    }
  });
  if(window.lucide) window.lucide.createIcons();
});
</script>
</body>"""

# Ensure it's not already injected
if "fetch('assets/portfolio-data.json')" not in html:
    html = html.replace('</body>', injector)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Injected dynamic thumbnail loader into portfolio.html")
