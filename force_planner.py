with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_block = "} else if (id === 'original-tracks') {"
new_block = """} else if (id === 'wellbeing-planner') {
                    const finalImg = media[0];
                    const drafts = media.slice(1);
                    
                    htmlStr += `<div class="cs-section">
                        <h2 class="cs-heading" style="font-size: 2rem; border-bottom: 2px solid var(--ink12); padding-bottom: 0.5rem; margin-bottom: 2rem;">Final Published Design</h2>
                        <div class="masonry-container">`;
                    if (finalImg) htmlStr += renderMedia(finalImg).replace('masonry-item', 'masonry-item full-width');
                    htmlStr += `</div></div>`;
                    
                    htmlStr += `<div class="cs-section">
                        <h2 class="cs-heading" style="font-size: 1.75rem; margin-top: 2rem; border-bottom: 1px solid var(--ink12); padding-bottom: 0.5rem; margin-bottom: 2rem;">Ideation & Concept Drafts</h2>
                        <div class="masonry-container">`;
                    drafts.forEach(f => { htmlStr += renderMedia(f); });
                    htmlStr += `</div></div>`;
                } else if (id === 'original-tracks') {"""

html = html.replace(old_block, new_block)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Forced Campus planner injection")
