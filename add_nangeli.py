for filename in ['scripts/data.js']:
    with open(filename, 'r', encoding='utf-8') as f:
        js = f.read()

    import re
    js = js.replace('"assets/portfolio-data/Nangeli/nangeli pg 20.png"\n    ]', '"assets/portfolio-data/Nangeli/nangeli pg 20.png",\n    "assets/portfolio-data/Nangeli/nangeli pg 21.png"\n    ]')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(js)
print("Added Nangeli pg 21 to data.js!")
