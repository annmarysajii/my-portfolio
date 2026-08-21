import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('const sz=s.r+(s.lit*6.5);', 'const sz=(s.r*0.55)+(s.lit*3);')
html = html.replace('const a=s.alpha+(s.lit*.6);', 'const a=(s.alpha*0.5)+(s.lit*.3);')

# Make lines thinner and less opaque for graphic-design
html = html.replace("bgX.lineWidth = 2;", "bgX.lineWidth = 1;")
html = html.replace("rgba(240,238,245,0.25)", "rgba(240,238,245,0.12)")
html = html.replace("rgba(17,16,9,0.25)", "rgba(17,16,9,0.1)")

# Also illustration
html = html.replace("'rgba(217,48,32,0.2)' : 'rgba(217,48,32,0.3)'", "'rgba(217,48,32,0.12)' : 'rgba(217,48,32,0.15)'")

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Made background canvas elements smaller and more subtle")
