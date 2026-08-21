for filename in ['project.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # The current wellbeing-planner logic:
    # drafts.forEach(f => { htmlStr += renderMedia(f); });
    
    # We will replace it to use custom captions
    old_logic = "drafts.forEach(f => { htmlStr += renderMedia(f); });"
    new_logic = "drafts.forEach((f, i) => { htmlStr += renderMedia(f).replace(/<div class=\"media-caption\">.*?<\\/div>/, '<div class=\"media-caption\">Concept ' + (i+1) + '</div>'); });"
    
    html = html.replace(old_logic, new_logic)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
print("Updated concept drafts captions!")
