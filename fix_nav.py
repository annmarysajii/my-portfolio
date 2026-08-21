for filename in ['project.html', 'jasmine_reader.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix Back to Portfolio links
    html = html.replace('href="index.html" class="nav-back"', 'href="portfolio.html" class="nav-back"')
    html = html.replace('href="index.html" style="position:fixed; top:20px; left:20px;', 'href="portfolio.html" style="position:fixed; top:20px; left:20px;')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

for filename in ['index.html', 'portfolio.html', 'project.html', 'jasmine_reader.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix bfcache issue where back button causes blank page
    bfcache_fix = """
    // BFCache fix for blank pages on back button navigation
    window.addEventListener('pageshow', function(event) {
        if (event.persisted) {
            document.body.classList.remove('page-exit');
        }
    });
    """
    if "BFCache fix" not in html:
        html = html.replace("</body>", bfcache_fix + "\n</body>")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
            
print("Navigation fixes applied!")
