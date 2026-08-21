import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_logic = "const isComic = id === 'nangele' || id === 'internship-comics' || id === 'wellbeing-planner' || id === 'jasmine-comic';"
new_logic = "const isComic = id === 'internship-comics' || id === 'wellbeing-planner' || id === 'jasmine-comic';"

html = html.replace(old_logic, new_logic)

custom_nangele = """              } else if (id === 'mock-posters') {
                  let htmlStr = styleBlock + `<div class="masonry-container">`;
                  media.forEach(file => { htmlStr += renderMedia(file); });
                  htmlStr += `</div>`;
                  gal.innerHTML = htmlStr;
                  return;
"""
# I need to insert custom logic for nangele inside the if/else block!
