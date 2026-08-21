for filename in ['project.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update the outer if block to include internship-comics
    html = html.replace("id === 'nangele' || id === 'original-tracks'", "id === 'nangele' || id === 'internship-comics' || id === 'original-tracks'")
    
    # 2. Add the internship-comics layout
    internship_layout = """                } else if (id === 'internship-comics') {
                    htmlStr += `
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
                    <div class="cs-section">
                      <div style="background:var(--surf); padding: 3rem; border-radius:12px; margin-bottom: 2rem; border: 1px solid var(--line);">
                          <h2 style="font-family:'Clash Display'; font-size:2.2rem; margin-bottom:1rem; margin-top:0;">CAO Internship Comic Series</h2>
                          <p style="font-size:1.1rem; line-height:1.7; color:var(--ink5); margin-bottom:1.5rem;">
                              <strong>Project Description:</strong> How to tackle internships social media comic project (2023). Illustrated a series of 6+ original comics depicting student internship experiences, producing publication-ready artwork aligned with the office's student engagement brief.
                          </p>
                          <div style="display:flex; flex-wrap:wrap; gap:1rem;">
                              <div style="background:var(--bg); padding:0.8rem 1.5rem; border-radius:8px; border:1px solid var(--line); font-weight:600; font-size:0.95rem;">
                                  🌟 View the series on Instagram: <a href="https://www.instagram.com/p/CxfW4dyvDy_/?hl=en" target="_blank" style="color:var(--blue); text-decoration:none;">@ntucao</a>
                              </div>
                          </div>
                      </div>
                      <h2 class="cs-heading" style="text-align:center; margin-bottom:2rem;">Reading View</h2>
                      <div id="nangeli-reader"></div>
                    </div>"""
                    
    html = html.replace("} else if (id === 'nangele') {", internship_layout + "\n                } else if (id === 'nangele') {")

    # 3. Add to the inner condition where `renderBook` is defined
    html = html.replace("if (id === 'nangele') {", "if (id === 'nangele' || id === 'internship-comics') {")
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
print("Updated internship comics layout!")
