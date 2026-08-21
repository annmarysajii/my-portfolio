import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_formatName = """  // Format string for captions and alt text
  function formatName(str) {
      let name = str.split('/').pop().replace(/\.[^/.]+$/, "");
      name = name.replace(/[-_]/g, ' ').replace(/\s*\(\d+\)\s*/g, ' ').trim();
      return name.charAt(0).toUpperCase() + name.slice(1);
  }"""

new_formatName = """  // Format string for captions and alt text
  function formatName(str) {
      const overrides = {
          'Your paragraph text (35)': 'Badge Logo',
          'Your paragraph text (36)': 'Logo Inverse',
          'Your paragraph text (33)': 'Logo Secondary',
          'Your paragraph text (30)': 'Sticker Pack',
          'Your paragraph text (37)': 'Social Media Asset',
          'ART DIRECTION PORTFOLIO': 'Brand Guidelines',
          'ART DIRECTION PORTFOLIO (1)': 'Brand Guidelines',
          'Copy of ART DIRECTION PORTFOLIO (3)': 'Brand Presentation',
          'It is time for some strawberries': 'Billboard Mockup',
          '3': 'Product Packaging',
          '4': 'Product Packaging',
          '5': 'Brand Asset',
          '6': 'Brand Asset',
          '7': 'Brand Asset',
          'presents': 'Presentation Slide'
      };
      
      let rawName = str.split('/').pop().replace(/\.[^/.]+$/, "");
      if (overrides[rawName]) return overrides[rawName];
      
      let name = rawName.replace(/[-_]/g, ' ').replace(/\s*\(\d+\)\s*/g, ' ').trim();
      return name.charAt(0).toUpperCase() + name.slice(1);
  }"""

html = html.replace(old_formatName, new_formatName)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Added override dictionary for captions")
