for filename in ['portfolio.html', 'index.html', 'project.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    style_opens = html.count("<style>") + html.count("<style ")
    style_closes = html.count("</style>")
    print(f"{filename}: style tags {style_opens} open, {style_closes} close")
    
    div_opens = html.count("<div")
    div_closes = html.count("</div>")
    print(f"{filename}: div tags {div_opens} open, {div_closes} close (Note: string literals might throw this off, just checking for massive discrepancies)")
