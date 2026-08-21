import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add Green Arrow overrides
old_overrides = """      const overrides = {
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
      };"""

new_overrides = """      const overrides = {
          // GoBunny
          'Your paragraph text (35)': 'Badge Logo',
          'Your paragraph text (36)': 'Logo Inverse',
          'Your paragraph text (33)': 'Logo Secondary',
          'Your paragraph text (30)': 'Sticker Pack',
          'Your paragraph text (37)': 'Social Media Asset',
          'ART DIRECTION PORTFOLIO': 'Brand Guidelines',
          'ART DIRECTION PORTFOLIO (1)': 'Brand Guidelines',
          'Copy of ART DIRECTION PORTFOLIO (3)': 'Brand Presentation',
          'It is time for some strawberries': 'Billboard Mockup',
          
          // Green Arrow overrides mapping
          '3': 'Event Poster',
          '4': 'Instagram Campaign',
          '5': 'Website Mockup',
          '6': 'Merchandise (T-Shirt)',
          '7': 'Merchandise (Tote Bag)',
          'presents': 'Competition Poster',
          'LOGO GREEN ARROW': 'Primary Lockup',
          'EcoFuture Color Pallette': 'Color Palette'
      };
      
      // Since 3,4,5,6,7 clash between GoBunny and GreenArrow, let's fix the logic
      // by inspecting the full path in formatName!
"""

html = html.replace(old_overrides, new_overrides)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated overrides, but wait, need to fix the path context!")
