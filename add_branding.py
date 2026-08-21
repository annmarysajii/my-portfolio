import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add brand styling logic
inject_logic = """if (p.badge) { ... } // just a locator"""

old_logic = "const media = data[id] || [];"
new_logic = """const media = data[id] || [];
          
          if (id === 'gobunny') {
              document.documentElement.style.setProperty('--bg', '#FFEBF0');
              document.documentElement.style.setProperty('--surf', '#FFF5F7');
              document.documentElement.style.setProperty('--ink', '#D02F5A');
              document.documentElement.style.setProperty('--line', 'rgba(208, 47, 90, 0.2)');
              document.querySelector('.con').style.maxWidth = '1200px';
          } else if (id === 'green-arrow') {
              document.documentElement.style.setProperty('--bg', '#EBF4ED');
              document.documentElement.style.setProperty('--surf', '#F4F9F5');
              document.documentElement.style.setProperty('--ink', '#2B5E39');
              document.documentElement.style.setProperty('--line', 'rgba(43, 94, 57, 0.2)');
              document.querySelector('.con').style.maxWidth = '1200px';
          }"""

html = html.replace(old_logic, new_logic)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Injected dynamic brand styling for GoBunny and Green Arrow")
