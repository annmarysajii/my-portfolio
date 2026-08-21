import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make nangele native
html = html.replace("const isComic = id === 'nangele' || id === 'internship-comics' || id === 'wellbeing-planner' || id === 'jasmine-comic';", 
                    "const isComic = id === 'internship-comics' || id === 'wellbeing-planner' || id === 'jasmine-comic';")

html = html.replace("if (id === 'gobunny' || id === 'green-arrow') {", 
                    "if (id === 'gobunny' || id === 'green-arrow' || id === 'nangele') {")

nangeli_logic = """              } else if (id === 'nangele') {
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
                  <script>
                    const nangeliMedia = ${JSON.stringify(media.filter(f => f.match(/\.(png|jpe?g)$/i)))};
                    let curPage = 0;
                    window.renderBook = function(direction) {
                        const r = document.getElementById('nangeli-reader');
                        let p1 = nangeliMedia[curPage] ? \`<img src="\${nangeliMedia[curPage]}" style="width:100%; height:100%; object-fit:contain; padding:2rem;">\` : '';
                        let p2 = nangeliMedia[curPage+1] ? \`<img src="\${nangeliMedia[curPage+1]}" style="width:100%; height:100%; object-fit:contain; padding:2rem;">\` : '';
                        
                        let animClass = direction === 'next' ? 'flip-next' : (direction === 'prev' ? 'flip-prev' : '');
                        
                        r.innerHTML = \`
                        <div class="book-container \${animClass}">
                          <button class="page-flip-btn prev" onclick="curPage=Math.max(0, curPage-2); window.renderBook('prev');" \${curPage===0?'disabled':''}><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg></button>
                          <div class="book-page left">\${p1}</div>
                          <div class="book-page right">\${p2}</div>
                          <button class="page-flip-btn next" onclick="curPage=Math.min(nangeliMedia.length-1, curPage+2); window.renderBook('next');" \${curPage>=nangeliMedia.length-2?'disabled':''}><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg></button>
                        </div>
                        <div style="text-align:center; margin-top:1.5rem; font-size:0.95rem; font-weight:500; color:var(--ink5);">Spread \${Math.floor(curPage/2)+1} of \${Math.ceil(nangeliMedia.length/2)}</div>
                        \`;
                    };
                    setTimeout(window.renderBook, 50);
                  </script>
                  `;
              }"""

html = html.replace("              } else if (id === 'green-arrow') {", 
                    nangeli_logic + "\n              } else if (id === 'green-arrow') {")

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated nangele logic")
