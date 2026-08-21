for filename in ['portfolio.html', 'index.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    print(f"--- {filename} ---")
    if 'class="awards"' in html:
        idx = html.find('class="awards"')
        print(html[idx-10:idx+800])
    else:
        print("NO AWARDS HTML FOUND!")
