import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update GoBunny Theme Variables
html = html.replace(
    "document.documentElement.style.setProperty('--bg', '#FFEBF0');\n                document.documentElement.style.setProperty('--surf', '#FFF5F7');\n                document.documentElement.style.setProperty('--ink', '#D02F5A');\n                document.documentElement.style.setProperty('--line', 'rgba(208, 47, 90, 0.2)');",
    "document.documentElement.style.setProperty('--bg', '#FFE6F0');\n                document.documentElement.style.setProperty('--surf', '#FFF5F8');\n                document.documentElement.style.setProperty('--ink', '#FF3522');\n                document.documentElement.style.setProperty('--line', 'rgba(255, 53, 34, 0.2)');"
)

# Update Green Arrow Theme Variables
html = html.replace(
    "document.documentElement.style.setProperty('--bg', '#EBF4ED');\n                document.documentElement.style.setProperty('--surf', '#F4F9F5');\n                document.documentElement.style.setProperty('--ink', '#2B5E39');\n                document.documentElement.style.setProperty('--line', 'rgba(43, 94, 57, 0.2)');",
    "document.documentElement.style.setProperty('--bg', '#F1F7ED');\n                document.documentElement.style.setProperty('--surf', '#FFFFFF');\n                document.documentElement.style.setProperty('--ink', '#243E36');\n                document.documentElement.style.setProperty('--line', 'rgba(36, 62, 54, 0.2)');"
)

# Update GoBunny Palette Swatches
old_gobunny_palette = """<div class="cs-color"><div class="cs-swatch" style="background:#D02F5A;"></div><span class="cs-hex">#D02F5A</span></div>
                          <div class="cs-color"><div class="cs-swatch" style="background:#FFEBF0;"></div><span class="cs-hex">#FFEBF0</span></div>
                          <div class="cs-color"><div class="cs-swatch" style="background:#FFF5F7;"></div><span class="cs-hex">#FFF5F7</span></div>
                          <div class="cs-color"><div class="cs-swatch" style="background:#E26F8D;"></div><span class="cs-hex">#E26F8D</span></div>
                          <div class="cs-color"><div class="cs-swatch" style="background:#F2A4B8;"></div><span class="cs-hex">#F2A4B8</span></div>"""

new_gobunny_palette = """<div class="cs-color"><div class="cs-swatch" style="background:#FF3522;"></div><span class="cs-hex">#FF3522</span></div>
                          <div class="cs-color"><div class="cs-swatch" style="background:#FF7076;"></div><span class="cs-hex">#FF7076</span></div>
                          <div class="cs-color"><div class="cs-swatch" style="background:#FFB6D9;"></div><span class="cs-hex">#FFB6D9</span></div>
                          <div class="cs-color"><div class="cs-swatch" style="background:#FFE6F0;"></div><span class="cs-hex">#FFE6F0</span></div>
                          <div class="cs-color"><div class="cs-swatch" style="background:#FFFFFF;"></div><span class="cs-hex">#FFFFFF</span></div>"""
html = html.replace(old_gobunny_palette, new_gobunny_palette)

# Update Green Arrow Palette Swatches
old_ga_palette = """<div class="cs-color"><div class="cs-swatch" style="background:#2B5E39;"></div><span class="cs-hex">#2B5E39</span></div>
                          <div class="cs-color"><div class="cs-swatch" style="background:#EBF4ED;"></div><span class="cs-hex">#EBF4ED</span></div>
                          <div class="cs-color"><div class="cs-swatch" style="background:#F4F9F5;"></div><span class="cs-hex">#F4F9F5</span></div>
                          <div class="cs-color"><div class="cs-swatch" style="background:#558F65;"></div><span class="cs-hex">#558F65</span></div>
                          <div class="cs-color"><div class="cs-swatch" style="background:#8FBC9B;"></div><span class="cs-hex">#8FBC9B</span></div>"""

new_ga_palette = """<div class="cs-color"><div class="cs-swatch" style="background:#243E36;"></div><span class="cs-hex">#243E36</span></div>
                          <div class="cs-color"><div class="cs-swatch" style="background:#7CA982;"></div><span class="cs-hex">#7CA982</span></div>
                          <div class="cs-color"><div class="cs-swatch" style="background:#E0EEC6;"></div><span class="cs-hex">#E0EEC6</span></div>
                          <div class="cs-color"><div class="cs-swatch" style="background:#C2A83E;"></div><span class="cs-hex">#C2A83E</span></div>
                          <div class="cs-color"><div class="cs-swatch" style="background:#F1F7ED;"></div><span class="cs-hex">#F1F7ED</span></div>"""
html = html.replace(old_ga_palette, new_ga_palette)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated brand colors for GoBunny and Green Arrow.")
