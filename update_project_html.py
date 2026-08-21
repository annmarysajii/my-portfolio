import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# I want to find where `if(!p){` starts.
old_js = """if(!p){
    main.innerHTML=`<div class="con" style="padding:6rem 0;text-align:center;"><p style="font-size:1rem;color:var(--ink5);">Project not found.</p><a href="portfolio.html" style="display:inline-block;margin-top:1rem;font-size:.9rem;font-weight:600;color:var(--blue);">Back to portfolio</a></div>`;
  } else {
    document.title = p.title + ' — Annmary Saji';

    function imgSlot(size,idx){
      // for projects with 1 image
      if(!p.images[idx]) return ''; 
      const im=p.images[idx];
      const cls=size==='sq' ? 'gallery-img gallery-img-sq' : 'gallery-img';
      return `<div class="${cls}"><span class="ph-icon">${im.emoji}</span><span class="ph-label">${im.label}</span></div>`;
    }

    // Determine gallery rows to hide if no images
    const r2 = imgSlot('med',1) + imgSlot('med',2);
    const r3 = imgSlot('sq',3) + imgSlot('sq',4) + imgSlot('sq',5);

    main.innerHTML=`
  <div class="con">
    <div class="proj-header">
      <div class="proj-disc-tag">${p.discipline}${p.context?' • '+p.context:''}</div>
      <h1 class="proj-title">${p.title}</h1>
      ${p.badge ? `<div class=\"proj-badge\">${p.badge}</div>` : ''}
      <div class="proj-meta-row">
        <span class="proj-meta-item"><strong>Year</strong> &nbsp;${p.year}</span>
        <div class="proj-meta-sep"></div>
        <span class="proj-meta-item"><strong>Role</strong> &nbsp;${p.role}</span>
      </div>
    </div>

    <div class="proj-desc-grid">
      <div class="proj-desc-col">
        <h2 class="proj-desc-title">Overview</h2>
        <p class="proj-desc-text">${p.overview}</p>
        <div class="proj-tools">
          ${p.tools.map(t=>`<span class=\"tool\">${t}</span>`).join('')}
        </div>
      </div>
      <div class="proj-desc-col">
        <h2 class="proj-desc-title">Process & Approach</h2>
        <p class="proj-desc-text">${p.process}</p>
      </div>
    </div>

    <div class="gallery-h">Visual Development / Output</div>
    
    <div id="dynamic-gallery">
      <div class="gallery-hero">
        <div class="tape tape-tl"></div>
        <div class="tape tape-tr"></div>
        <span class="ph-icon"><i data-lucide="image"></i></span>
        <span class="ph-label">Loading media...</span>
      </div>
    </div>

    <div class="proj-footer">
      <a href="portfolio.html" class="back-btn">← Back to Portfolio</a>
      <a href="portfolio.html" class="portfolio-btn">View All Work →</a>
    </div>
  </div>`;
  
    // Fetch and populate gallery
    fetch('assets/portfolio-data.json').then(r=>r.json()).then(data => {
        const media = data[id] || [];
        const gal = document.getElementById('dynamic-gallery');
        if (media.length === 0) {
            gal.innerHTML = `<div class="gallery-hero"><div class="tape tape-tl"></div><div class="tape tape-tr"></div><span class="ph-label">Media coming soon</span></div>`;
            return;
        }
        
        let htmlStr = '';
        media.forEach((file, idx) => {
            let el = '';
            const isVideo = !!file.match(/\.(mp4|mov|webm)$/i);
            const isAudio = !!file.match(/\.(m4a|mp3|wav)$/i);
            
            if (isVideo) {
                el = `<video src="${file}" controls style="width:100%; height:100%; object-fit:cover; background:var(--surf); border-radius:4px;"></video>`;
            } else if (isAudio) {
                el = `<div style="display:flex; align-items:center; justify-content:center; width:100%; height:100%; background:var(--surf); padding:2rem;"><audio src="${file}" controls style="width:100%;"></audio></div>`;
            } else {
                el = `<img src="${file}" alt="" style="width:100%; height:100%; object-fit:cover; background:var(--surf); border-radius:4px;">`;
            }
            
            // Layout: First item is hero, next 2 are medium row, next are square grid
            if (idx === 0) {
                htmlStr += `<div class="gallery-hero"><div class="tape tape-tl"></div><div class="tape tape-tr"></div>${el}</div>`;
            } else if (idx === 1 || idx === 2) {
                if (idx === 1) htmlStr += `<div class="gallery-row2">`;
                htmlStr += `<div class="gallery-img">${el}</div>`;
                if (idx === 2 || idx === media.length-1) htmlStr += `</div>`;
            } else {
                if (idx === 3) htmlStr += `<div class="gallery-row3">`;
                htmlStr += `<div class="gallery-img gallery-img-sq">${el}</div>`;
                if (idx === media.length-1) htmlStr += `</div>`;
            }
        });
        gal.innerHTML = htmlStr;
    }).catch(err => {
        console.error("Error loading media:", err);
    });
  }"""

# Actually, I'll just regex replace from `if(!p){` to the end of the script tag!
html = re.sub(r'if\(!p\)\{.*</div>`;\s*\}', old_js, html, flags=re.DOTALL)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated project.html to load media dynamically")
