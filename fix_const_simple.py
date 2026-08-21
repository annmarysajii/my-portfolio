for filename in ['portfolio.html', 'index.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('const file = data[id].find', 'let file = data[id].find')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
print("Replaced simple const to let")
