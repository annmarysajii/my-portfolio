import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# portfolio.html had:
# const data = window.PORTFOLIO_DATA; if(data) {
# ...
# });

html = html.replace('const data = window.PORTFOLIO_DATA; if(data) {', 'setTimeout(() => {\nconst data = window.PORTFOLIO_DATA; if(data) {')
html = html.replace('});\n</script>\n</body>', '}\n}, 50);\n</script>\n</body>')

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('project.html', 'r', encoding='utf-8') as f:
    html2 = f.read()

html2 = html2.replace('const data = window.PORTFOLIO_DATA; if(data) {', 'setTimeout(() => {\nconst data = window.PORTFOLIO_DATA; if(data) {')

# Find the end of the fetch block in project.html
# It was:
# }).catch(err => {
#    console.error("Error loading media:", err);
# });

end_block_old = """    }).catch(err => {
        console.error("Error loading media:", err);
    });"""

end_block_new = """    }
    }, 50);"""

html2 = html2.replace(end_block_old, end_block_new)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html2)
print("Fixed syntax errors by wrapping in setTimeout")
