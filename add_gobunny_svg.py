for filename in ['scripts/data.js']:
    with open(filename, 'r', encoding='utf-8') as f:
        js = f.read()

    import re
    js = js.replace('"assets/portfolio-data/GoBunny_brand/4.png",', '"assets/portfolio-data/GoBunny_brand/4.png",\n    "assets/portfolio-data/GoBunny_brand/BRANDCOLOR_GOBUNNY.svg",')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(js)
print("Added BRANDCOLOR_GOBUNNY.svg to gobunny array!")
