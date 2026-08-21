import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix Original Tracks cover
html = html.replace(
    "`<div style=\"background:var(--ink05); aspect-ratio:1; display:flex; align-items:center; justify-content:center; color:var(--ink);\"><i data-lucide=\"music\" style=\"width:48px;height:48px;\"></i></div>`;",
    "`<div style=\"background: linear-gradient(135deg, #1850A8 0%, #D02F5A 100%); aspect-ratio:1; display:flex; align-items:center; justify-content:center; color:white; overflow:hidden;\"><img src=\"assets/portfolio-data/My profile/me avatar.png\" style=\"width:100%; height:100%; object-fit:cover; mix-blend-mode: overlay; opacity:0.6;\"></div>`;"
)

# 2. Fix Commissions Labels (Remove captionHtml for commissions)
html = html.replace(
    "if (id !== 'original-tracks') {",
    "if (id !== 'original-tracks' && id !== 'commissions') {"
)

# 3. Rewrite Nangeli logic to avoid innerHTML script tag issue
# We need to find the `} else if (id === 'nangele') { ... }` block and replace it.
nangele_regex = r"\} else if \(id === 'nangele'\) \{.*?(?=\} else if \(id === 'green-arrow'\) \{)"

new_nangele = """} else if (id === 'nangele') {
                    htmlStr += `<style>
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
                    </style>`;
                    
                    htmlStr += `
                    <div class="cs-section">
                      <h2 class="cs-heading" style="text-align:center; margin-bottom:2rem;">Nangeli — Reading View</h2>
                      <div id="nangeli-reader"></div>
                    </div>
                    `;
                """

html = re.sub(nangele_regex, new_nangele, html, flags=re.DOTALL)

# And now we inject the actual logic AFTER `gal.innerHTML = htmlStr;`
post_inject_regex = r"(gal\.innerHTML = htmlStr;\n\s*return;\n\s*\})"
post_inject_logic = """gal.innerHTML = htmlStr;
                
                if (id === 'nangele') {
                    const nangeliMedia = media.filter(f => f.match(/\.(png|jpe?g)$/i));
                    let curPage = 0;
                    const renderBook = (direction) => {
                        const r = document.getElementById('nangeli-reader');
                        if(!r) return;
                        let p1 = nangeliMedia[curPage] ? `<img src="${nangeliMedia[curPage]}" style="width:100%; height:100%; object-fit:contain; padding:2rem;">` : '';
                        let p2 = nangeliMedia[curPage+1] ? `<img src="${nangeliMedia[curPage+1]}" style="width:100%; height:100%; object-fit:contain; padding:2rem;">` : '';
                        let animClass = direction === 'next' ? 'flip-next' : (direction === 'prev' ? 'flip-prev' : '');
                        
                        r.innerHTML = `
                        <div class="book-container ${animClass}">
                          <button class="page-flip-btn prev" id="n-prev" ${curPage===0?'disabled':''}><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg></button>
                          <div class="book-page left">${p1}</div>
                          <div class="book-page right">${p2}</div>
                          <button class="page-flip-btn next" id="n-next" ${curPage>=nangeliMedia.length-2?'disabled':''}><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg></button>
                        </div>
                        <div style="text-align:center; margin-top:1.5rem; font-size:0.95rem; font-weight:500; color:var(--ink5);">Spread ${Math.floor(curPage/2)+1} of ${Math.ceil(nangeliMedia.length/2)}</div>
                        `;
                        
                        const pBtn = document.getElementById('n-prev');
                        if (pBtn) pBtn.onclick = () => { curPage = Math.max(0, curPage-2); renderBook('prev'); };
                        const nBtn = document.getElementById('n-next');
                        if (nBtn) nBtn.onclick = () => { curPage = Math.min(nangeliMedia.length-1, curPage+2); renderBook('next'); };
                    };
                    renderBook('');
                }
                return;
            }"""

html = re.sub(post_inject_regex, post_inject_logic, html)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Applied project.html fixes")
