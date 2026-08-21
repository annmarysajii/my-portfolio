with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_tools = "tools:['Adobe Illustrator','Adobe Photoshop','InDesign'],"
new_tools = "tools:['Canva','CapCut'],"

if old_tools in html:
    html = html.replace(old_tools, new_tools)
    
    with open('project.html', 'w', encoding='utf-8') as f:
        f.write(html)
print("Updated NTU Fest tools to Canva and CapCut!")
