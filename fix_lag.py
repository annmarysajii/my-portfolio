import re
with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

bad_illustration = """    } else if (theme === 'illustration') { 
        ctx.font = `600 ${r*3}px sans-serif`;
        ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText('🖌️', 0, 0);"""

good_illustration = """    } else if (theme === 'illustration') { 
        ctx.beginPath();
        ctx.arc(0, 0, r, 0, Math.PI);
        ctx.lineTo(0, -r*1.8);
        ctx.closePath();
        ctx.fill();"""

html = html.replace(bad_illustration, good_illustration)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed illustration lag")
