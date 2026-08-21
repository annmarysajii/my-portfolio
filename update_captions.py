import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_overrides = """        const overrides = {
          '11 february (2)': 'Makeout Drive',
          'Untitled design (22)': 'Recruitment Image',
          'MELODY OF THE DROWNED (10)': 'Melody of the Drowned',
          'sunset jams (1)': 'Sunset Jams',
          'FINAL IMAGE': 'Final Artwork',
          'nangeli cover image': 'Nangeli Cover',"""

html = html.replace('const overrides = {', new_overrides)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated caption overrides")
