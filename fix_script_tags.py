for filename in ['index.html', 'portfolio.html', 'project.html', 'jasmine_reader.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the raw text and wrap it in script tags
    raw_text = """    // BFCache fix for blank pages on back button navigation
    window.addEventListener('pageshow', function(event) {
        if (event.persisted) {
            document.body.classList.remove('page-exit');
        }
    });"""
    
    script_wrapped = f"<script>\n{raw_text}\n    </script>"
    
    if raw_text in html and "<script>\n    // BFCache fix" not in html:
        html = html.replace(raw_text, script_wrapped)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
            
print("Fixed script tags!")
