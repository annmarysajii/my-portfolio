import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the illustration shape with a paintbrush emoji
html = html.replace("      } else if (theme === 'illustration') { \n          ctx.beginPath(); ctx.arc(0, 0, r*0.7, 0, Math.PI*2); ctx.fill();", 
                    "      } else if (theme === 'illustration') { \n          ctx.font = `600 ${r*3}px sans-serif`;\n          ctx.textAlign = 'center'; ctx.textBaseline = 'middle';\n          ctx.fillText('🖌️', 0, 0);")

# Remove the messy red lines
html = re.sub(r"\} else if \(theme === 'illustration'\) \{.*?bgX\.stroke\(\);\n\s*\}\n\s*\}", "} else if (theme === 'illustration') {\n          // removed messy lines as requested\n      }", html, flags=re.DOTALL)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed illustration background")
