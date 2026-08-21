with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Change javascript:window.close() to portfolio.html
html = html.replace('href="javascript:window.close()"', 'href="portfolio.html"')

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated top back button fallback in project.html!")
