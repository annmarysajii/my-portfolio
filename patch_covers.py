import re

svg_li = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>'
svg_ig = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>'

for filename in ['portfolio.html', 'index.html', 'project.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Replace lucide icons
    html = html.replace('<i data-lucide="linkedin"></i>', svg_li)
    html = html.replace('<i data-lucide="instagram"></i>', svg_ig)
    
    # In index and portfolio, override covers
    if filename in ['portfolio.html', 'index.html']:
        old_file = "if (file) {"
        new_file = """if (id === 'ntu-fest') file = 'assets/portfolio-data/Ntu fest assets/SunDown.png';
          if (id === 'gobunny') file = 'assets/portfolio-data/GoBunny_brand/GO BUNNY.png';
          if (file) {"""
        
        # Only inject if not already there
        if "id === 'ntu-fest'" not in html:
            html = html.replace(old_file, new_file)
            
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
print("Replaced icons and covers")
