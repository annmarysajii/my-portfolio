import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update jasmine IDs
html = html.replace('"project.html?id=jasmine"', '"project.html?id=jasmine-visdev"', 1) # first is in animation
html = html.replace('"project.html?id=jasmine"', '"project.html?id=jasmine-comic"', 1) # second is in comics

# Remove Elevandi and VIP Color from Graphic Design
# In portfolio.html, we need to delete the entire <article class="card..."> block for elevandi and vipcolor-campaign
# Elevandi:
html = re.sub(r'<article class="card[^>]*>\s*<a href="project\.html\?id=elevandi".*?</article>', '', html, flags=re.DOTALL)
# VIP Color Campaign:
html = re.sub(r'<article class="card[^>]*>\s*<a href="project\.html\?id=vipcolor-campaign".*?</article>', '', html, flags=re.DOTALL)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated portfolio.html with new Jasmine IDs and removed Graphic Design items")
