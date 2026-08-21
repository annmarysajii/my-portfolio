import re

for filename in ['portfolio.html', 'index.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # The structure is:
    # <div class="card" data-cat="XXX">
    #   <a href="YYY" class="card-img" ...>
    #     <img ...>
    #   </a>
    #   <div class="card-content">
    #     <h3 class="card-title">ZZZ</h3>
    #     <p class="card-desc">WWW</p>
    #   </div>
    # </div>
    
    # We will use regex to find this pattern and transform it
    pattern = re.compile(r'<div class="card([^"]*)"([^>]*)>\s*<a href="([^"]+)" class="card-img"([^>]*)>([\s\S]*?)</a>\s*<div class="card-content">([\s\S]*?)</div>\s*</div>')
    
    def repl(m):
        card_cls_extra = m.group(1)
        card_attrs = m.group(2)
        href = m.group(3)
        img_attrs = m.group(4)
        img_content = m.group(5)
        content = m.group(6)
        
        return f'<a href="{href}" class="card{card_cls_extra}"{card_attrs} style="text-decoration:none; color:inherit; display:block;">\n  <div class="card-img"{img_attrs}>{img_content}</div>\n  <div class="card-content">{content}</div>\n</a>'
        
    new_html = pattern.sub(repl, html)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_html)
print("Updated cards to be fully clickable!")
