for filename in ['portfolio.html', 'index.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace(
        "const file = data[id].find(f => f.match(/\.(png|jpe?g|gif|webm|mp4|mov)$/i) || \nf.match(/youtube\.com|youtu\.be/i)) || data[id][0];", 
        "let file = data[id].find(f => f.match(/\.(png|jpe?g|gif|webm|mp4|mov)$/i) || \nf.match(/youtube\.com|youtu\.be/i)) || data[id][0];"
    )
    html = html.replace(
        "const file = data[id].find(f => f.match(/\.(png|jpe?g|gif|webm|mp4|mov)$/i) || \n        f.match(/youtube\.com|youtu\.be/i)) || data[id][0];", 
        "let file = data[id].find(f => f.match(/\.(png|jpe?g|gif|webm|mp4|mov)$/i) || \n        f.match(/youtube\.com|youtu\.be/i)) || data[id][0];"
    )
    html = html.replace(
        "const file = data[id].find(f => f.match(/\.(png|jpe?g|gif|webm|mp4|mov)$/i) || \n            f.match(/youtube\.com|youtu\.be/i)) || data[id][0];", 
        "let file = data[id].find(f => f.match(/\.(png|jpe?g|gif|webm|mp4|mov)$/i) || \n            f.match(/youtube\.com|youtu\.be/i)) || data[id][0];"
    )
    
    # Just in case whitespace is annoying, use regex
    import re
    html = re.sub(
        r'const file = data\[id\]\.find\(f => f\.match\(\/\\\.\(png\|jpe\?g\|gif\|webm\|mp4\|mov\)\\\$\/i\) \|\| \s*f\.match\(\/youtube\\\.com\|youtu\\\.be\/i\)\) \|\| data\[id\]\[0\];',
        r'let file = data[id].find(f => f.match(/\\.(png|jpe?g|gif|webm|mp4|mov)$/i) || f.match(/youtube\\.com|youtu\\.be/i)) || data[id][0];',
        html
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
print("Changed const to let")
