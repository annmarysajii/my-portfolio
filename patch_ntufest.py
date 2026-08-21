import re

# 1. Update the portfolio thumbnail
for filename in ['portfolio.html', 'index.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    html = html.replace(
        "if (id === 'ntu-fest') file = 'assets/portfolio-data/Ntu fest assets/SunDown.png';",
        "if (id === 'ntu-fest') file = 'assets/portfolio-data/Ntu fest assets/ntufest_portfoliogif.gif.mp4';"
    )
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)


# 2. Inject the custom layout in project.html
with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_block = "} else if (id === 'wellbeing-planner') {"
new_block = """} else if (id === 'ntu-fest') {
                    const video = findFile('youtu.be');
                    const cover = findFile('ntu fest cover');
                    const banner = findFile('ntufest_banner');
                    const performers = findFiles('performer images');
                    const vendor = findFile('SIGN UP');
                    const sundown = findFile('SunDown');
                    
                    htmlStr += `<div class="cs-section">
                        <div style="background:var(--surf); padding: 3rem; border-radius:12px; margin-bottom: 2rem; border: 1px solid var(--line);">
                            <h2 style="font-family:'Clash Display'; font-size:2.2rem; margin-bottom:1rem; margin-top:0;">Stepping up for NTU Fest</h2>
                            <p style="font-size:1.1rem; line-height:1.7; color:var(--ink5); margin-bottom:1.5rem;">
                                <strong>Fun fact:</strong> I originally joined the committee in a different role, but when the original Publicity Director unexpectedly stepped down, I took over the position to ensure the festival's branding and outreach didn't skip a beat. All the production elements were primarily created using Canva and CapCut.
                            </p>
                            <div style="display:flex; flex-wrap:wrap; gap:1rem;">
                                <div style="background:var(--bg); padding:0.8rem 1.5rem; border-radius:8px; border:1px solid var(--line); font-weight:600; font-size:0.95rem;">
                                    🔗 View the live 2024 graphics at <a href="https://instagram.com/ntufest" target="_blank" style="color:var(--blue); text-decoration:none;">@ntufest</a>
                                </div>
                            </div>
                        </div>
                    </div>`;

                    htmlStr += `<div class="cs-section"><h2 class="cs-heading" style="font-size:1.8rem; margin-bottom:1.5rem; border-bottom:1px solid var(--ink12); padding-bottom:0.5rem;">Promotional Video</h2><div class="masonry-container">`;
                    if (video) htmlStr += renderMedia(video).replace('masonry-item', 'masonry-item full-width');
                    htmlStr += `</div></div>`;

                    htmlStr += `<div class="cs-section"><h2 class="cs-heading" style="font-size:1.8rem; margin-bottom:1.5rem; border-bottom:1px solid var(--ink12); padding-bottom:0.5rem;">Hero & Banners</h2><div class="masonry-container">`;
                    if (cover) htmlStr += renderMedia(cover).replace('masonry-item', 'masonry-item full-width');
                    if (banner) htmlStr += renderMedia(banner).replace('masonry-item', 'masonry-item full-width');
                    htmlStr += `</div></div>`;

                    htmlStr += `<div class="cs-section"><h2 class="cs-heading" style="font-size:1.8rem; margin-bottom:1.5rem; border-bottom:1px solid var(--ink12); padding-bottom:0.5rem;">Performer Features</h2><div class="masonry-container">`;
                    performers.forEach(f => { htmlStr += renderMedia(f); });
                    htmlStr += `</div></div>`;

                    htmlStr += `<div class="cs-section"><h2 class="cs-heading" style="font-size:1.8rem; margin-bottom:1.5rem; border-bottom:1px solid var(--ink12); padding-bottom:0.5rem;">Event Collaterals</h2><div class="masonry-container">`;
                    if (vendor) htmlStr += renderMedia(vendor);
                    if (sundown) htmlStr += renderMedia(sundown);
                    htmlStr += `</div></div>`;
                } else if (id === 'wellbeing-planner') {"""

if "id === 'ntu-fest'" not in html:
    html = html.replace(old_block, new_block)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Applied NTU Fest updates!")
