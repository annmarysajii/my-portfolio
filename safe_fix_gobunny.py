with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix GoBunny Colors safely using exact string replacement of the specific hex values
html = html.replace("document.documentElement.style.setProperty('--bg', '#FFEBF0');", "document.documentElement.style.setProperty('--bg', '#FFF2F0');")
html = html.replace("document.documentElement.style.setProperty('--surf', '#FFF5F7');", "document.documentElement.style.setProperty('--surf', '#FFFFFF');")
html = html.replace("document.documentElement.style.setProperty('--ink', '#D02F5A');", "document.documentElement.style.setProperty('--ink', '#FF3522');")
html = html.replace("document.documentElement.style.setProperty('--line', 'rgba(208, 47, 90, 0.2)');", "document.documentElement.style.setProperty('--line', 'rgba(255, 53, 34, 0.2)');")

# 2. Fix the Custom Names mapping
html = html.replace("'It is time for some strawberries': 'Billboard Mockup',", "'It is time for some strawberries': 'Mobile UI',")
html = html.replace("'ART DIRECTION PORTFOLIO': 'Brand Guidelines',", "'ART DIRECTION PORTFOLIO': 'Billboard Mockup',")
html = html.replace("'3': isGoBunny ? 'Product Packaging' : 'Event Poster',", "'3': isGoBunny ? 'Packaging Design' : 'Event Poster',")
html = html.replace("'4': isGoBunny ? 'Product Packaging' : 'Instagram Campaign',", "'4': isGoBunny ? 'Packaging Details' : 'Instagram Campaign',")

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Safely fixed GoBunny labels and colors!")
