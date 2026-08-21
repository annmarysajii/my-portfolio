import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add new overrides
new_overrides = """        const overrides = {
          '1': 'Brand Exploration',
          '2': 'Visual System',
          'credit1': 'End Credits',
          'rain7': 'Rain Sequence',
          'staticshot_4': 'Establishing Shot',
          'ver1': 'Concept Version 1',
          'version2': 'Concept Version 2',
          'Home pt 1': 'Home (Part 1)',
          'character designs': 'Character Designs',
          'fusion jazz pg2': 'Fusion Jazz',
          'final_therapyscene': 'Therapy Scene',
          'pg1': 'Page 1',
          'ph2': 'Phase 2',
          'shot2': 'Shot 2',"""

html = html.replace('const overrides = {', new_overrides)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated naming overrides sitewide")
