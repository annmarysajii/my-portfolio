for filename in ['portfolio.html', 'index.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('[data-theme="dark"] \n\n[data-theme="dark"] .about', '[data-theme="dark"] .about')
    html = html.replace('[data-theme="dark"] \r\n[data-theme="dark"] .about', '[data-theme="dark"] .about')
    html = html.replace('[data-theme="dark"] \n[data-theme="dark"] .about', '[data-theme="dark"] .about')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
print("Cleaned up CSS")
