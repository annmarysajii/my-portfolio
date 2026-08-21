with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_str = "// Native Case Studies"
new_str = """// Native Case Studies
            const findFile = (str) => media.find(f => f.includes(str));
            const findFiles = (str) => media.filter(f => f.includes(str));"""

if "const findFile =" not in html:
    html = html.replace(old_str, new_str)
    
    with open('project.html', 'w', encoding='utf-8') as f:
        f.write(html)
print("Injected findFile helpers!")
