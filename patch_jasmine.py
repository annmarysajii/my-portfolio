import re

for filename in ['portfolio.html', 'index.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Add jasmine-album override
    html = html.replace(
        "'short-film-score': 'assets/vidtogif/solace_shortfilmscore.gif'",
        "'short-film-score': 'assets/vidtogif/solace_shortfilmscore.gif',\n                'jasmine-album': 'assets/portfolio-data/Jasmine_Visdev/THE TRIO.png'"
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
print("Added Jasmine Album cover override!")
