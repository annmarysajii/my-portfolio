import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update thumbnail loader to handle jasmine_reader.html
old_js = """    if (href && href.includes('id=')) {
      const id = href.split('id=')[1];"""
new_js = """    let id = null;
    if (href && href.includes('id=')) {
      id = href.split('id=')[1];
    } else if (href && href.includes('jasmine_reader.html')) {
      id = 'jasmine-comic';
    }
    
    if (id) {"""

html = html.replace(old_js, new_js)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated thumbnail logic in portfolio.html")
