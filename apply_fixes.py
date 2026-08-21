for filename in ['project.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update GoBunny colors
    old_css_if = """            if (id === 'gobunny') {
                document.documentElement.style.setProperty('--bg', '#FFEBF0');
                document.documentElement.style.setProperty('--surf', '#FFF5F7');
                document.documentElement.style.setProperty('--ink', '#D02F5A');
                document.documentElement.style.setProperty('--line', 'rgba(208, 47, 90, 0.2)');"""
                
    new_css_if = """            if (id === 'gobunny') {
                document.documentElement.style.setProperty('--bg', '#FFF2F0');
                document.documentElement.style.setProperty('--surf', '#FFFFFF');
                document.documentElement.style.setProperty('--ink', '#FF3522');
                document.documentElement.style.setProperty('--line', 'rgba(255, 53, 34, 0.2)');"""
    html = html.replace(old_css_if, new_css_if)

    # 2. Rename Wellbeing Planner drafts
    old_drafts = "drafts.forEach(f => { htmlStr += renderMedia(f); });"
    new_drafts = "drafts.forEach((f, i) => { htmlStr += renderMedia(f).replace(/<div class=\"media-caption\">.*?<\\/div>/, '<div class=\"media-caption\">Concept ' + (i+1) + '</div>'); });"
    html = html.replace(old_drafts, new_drafts)

    # 3. Add Internship Comics custom layout
    # Change outer block check
    html = html.replace("id === 'nangele' || id === 'original-tracks'", "id === 'nangele' || id === 'internship-comics' || id === 'original-tracks'")
    
    # Insert internship comics layout BEFORE nangele
    internship_layout = """                } else if (id === 'internship-comics') {
                    htmlStr += `
                    <div class="cs-section">
                      <div style="background:var(--surf); padding: 3rem; border-radius:12px; margin-bottom: 2rem; border: 1px solid var(--line);">
                          <h2 style="font-family:'Clash Display'; font-size:2.2rem; margin-bottom:1rem; margin-top:0;">CAO Internship Comic Series</h2>
                          <p style="font-size:1.1rem; line-height:1.7; color:var(--ink5); margin-bottom:1.5rem;">
                              <strong>Project Description:</strong> How to tackle internships social media comic project (2023). Illustrated a series of 6+ original comics depicting student internship experiences, producing publication-ready artwork aligned with the office's student engagement brief.
                          </p>
                          <div style="display:flex; flex-wrap:wrap; gap:1rem;">
                              <div style="background:var(--bg); padding:0.8rem 1.5rem; border-radius:8px; border:1px solid var(--line); font-weight:600; font-size:0.95rem;">
                                  \u2B50 View the series on Instagram: <a href="https://www.instagram.com/p/CxfW4dyvDy_/?hl=en" target="_blank" style="color:var(--blue); text-decoration:none;">@ntucao</a>
                              </div>
                          </div>
                      </div>
                      <h2 class="cs-heading" style="text-align:center; margin-bottom:2rem;">Reading View</h2>
                      <div id="internship-reader"></div>
                    </div>`;"""
    
    # We replace precisely
    html = html.replace("} else if (id === 'nangele') {", internship_layout + "\n                } else if (id === 'nangele') {")

    # Now handle the inner logic for JS interactive book rendering
    # We will just duplicate the renderBook logic for internship-comics
    internship_js = """                if (id === 'internship-comics') {
                    const comicMedia = media.filter(f => f.match(/\\.(png|jpe?g)$/i));
                    let curPage = 0;
                    const renderBook = (direction) => {
                        const r = document.getElementById('internship-reader');
                        if(!r) return;
                        let p1 = comicMedia[curPage] ? `<img src="${comicMedia[curPage]}" style="width:100%; height:100%; object-fit:contain; padding:2rem;">` : '';
                        let p2 = comicMedia[curPage+1] ? `<img src="${comicMedia[curPage+1]}" style="width:100%; height:100%; object-fit:contain; padding:2rem;">` : '';
                        let animClass = direction === 'next' ? 'flip-next' : (direction === 'prev' ? 'flip-prev' : '');
                        
                        r.innerHTML = `
                        <style>
                        .book-container { position:relative; width:100%; max-width:1000px; margin:0 auto; aspect-ratio: 1.4; background:#fff; box-shadow:0 10px 40px rgba(0,0,0,0.1); border-radius:4px; display:flex; perspective:2000px; }
                        .book-page { flex:1; width:50%; height:100%; position:relative; background:#fff; border:1px solid #eee; border-left:none; transform-origin: left center; transition: transform 0.6s cubic-bezier(0.645, 0.045, 0.355, 1); transform-style: preserve-3d; }
                        .book-page.left { border-left:1px solid #eee; border-right:1px solid #ddd; transform-origin: right center; }
                        .book-page img { width:100%; height:100%; object-fit:contain; position:absolute; inset:0; background:#fff; backface-visibility: hidden; }
                        .page-flip-btn { position:absolute; top:50%; transform:translateY(-50%); background:var(--ink); color:var(--bg); border:none; width:50px; height:50px; border-radius:50%; cursor:pointer; z-index:10; font-size:1.2rem; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 12px rgba(0,0,0,0.2); transition:transform 0.2s, background 0.2s; }
                        .page-flip-btn:hover { background:var(--blue); transform:translateY(-50%) scale(1.1); }
                        .page-flip-btn:disabled { opacity:0.3; cursor:not-allowed; }
                        .page-flip-btn.prev { left:-25px; }
                        .page-flip-btn.next { right:-25px; }
                        @media(max-width:768px) {
                          .book-container { aspect-ratio: 0.7; flex-direction: column; }
                          .book-page { width:100%; border-left:1px solid #eee; }
                          .book-page.left { border-bottom:1px solid #ddd; border-right:1px solid #eee; }
                          .page-flip-btn { width:40px; height:40px; }
                          .page-flip-btn.prev { left:10px; top:10px; transform:none; }
                          .page-flip-btn.next { right:10px; top:10px; transform:none; }
                          .page-flip-btn:hover { transform:scale(1.1); }
                        }
                        </style>
                        <div class="book-container ${animClass}">
                          <button class="page-flip-btn prev" id="i-prev" ${curPage===0?'disabled':''}><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg></button>
                          <div class="book-page left">${p1}</div>
                          <div class="book-page right">${p2}</div>
                          <button class="page-flip-btn next" id="i-next" ${curPage>=comicMedia.length-2?'disabled':''}><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg></button>
                        </div>
                        <div style="text-align:center; margin-top:1.5rem; font-size:0.95rem; font-weight:500; color:var(--ink5);">Spread ${Math.floor(curPage/2)+1} of ${Math.ceil(comicMedia.length/2)}</div>
                        `;
                        
                        const pBtn = document.getElementById('i-prev');
                        if (pBtn) pBtn.onclick = () => { curPage = Math.max(0, curPage-2); renderBook('prev'); };
                        const nBtn = document.getElementById('i-next');
                        if (nBtn) nBtn.onclick = () => { curPage = Math.min(comicMedia.length-1, curPage+2); renderBook('next'); };
                    };
                    renderBook('');
                }
"""
    
    html = html.replace("                if (id === 'nangele') {", internship_js + "\n                if (id === 'nangele') {")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
print("Updated all correctly!")
