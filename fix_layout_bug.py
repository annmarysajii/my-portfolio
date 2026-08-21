import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace column-count masonry with a robust Flexbox or Grid layout
old_style = """.masonry-grid { column-count: 1; column-gap: 1.5rem; }
            @media(min-width: 768px) { .masonry-grid { column-count: 2; } }
            @media(min-width: 1024px) { .masonry-grid { column-count: 3; } }"""

new_style = """.masonry-grid { 
              display: grid; 
              grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); 
              gap: 1.5rem; 
              align-items: start; 
            }"""

html = html.replace(old_style, new_style)

# Remove break-inside: avoid from the items, as grid doesn't need it and it can cause bugs
html = html.replace('break-inside:avoid;', '')

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated project.html layout to CSS Grid to fix iframe disappearance bugs")
