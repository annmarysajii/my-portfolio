import glob

files = glob.glob('*.html')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    html = html.replace(".classList.toggle('active'", ".classList.toggle('on'")
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
print("Changed active to on for pill toggles")
