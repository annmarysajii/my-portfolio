import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add PDF support
old_logic = """} else {
                  el = `<img src="${file}" alt="" style="width:100%; height:auto; display:block; background:var(--surf); border-radius:4px;">`;
              }"""
new_logic = """} else if (!!file.match(/\\.pdf$/i)) {
                  el = `<iframe src="${file}" style="width:100%; height:85vh; border:none; border-radius:4px; background:var(--surf);"></iframe>`;
              } else {
                  el = `<img src="${file}" alt="" style="width:100%; height:auto; display:block; background:var(--surf); border-radius:4px;">`;
              }"""

html = html.replace(old_logic, new_logic)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Added PDF embed support to project.html")
