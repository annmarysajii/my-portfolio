import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

bad_chunk = """    ctx.restore();
  }

    ctx.closePath();

    ctx.fillStyle=color;ctx.fill();

    ctx.restore();

  }"""

good_chunk = """    ctx.restore();
  }"""

html = html.replace(bad_chunk, good_chunk)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed syntax error in portfolio.html")
