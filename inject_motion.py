import re

for fname in ['index.html', 'portfolio.html', 'project.html', 'jasmine.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # Inject CSS before </head> if not there
    if 'css/motion.css' not in content:
        content = content.replace('</head>', '  <link rel="stylesheet" href="css/motion.css"/>\n</head>')
    
    # Inject JS before </body> if not there
    if 'scripts/motion.js' not in content:
        content = content.replace('</body>', '  <script src="scripts/motion.js"></script>\n</body>')

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

print("Injected motion assets into HTML files safely.")
