import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the form tag
html = html.replace('<form class="form" id="contactForm" onsubmit="sub(event)">', '<form class="form" id="contactForm" action="https://formsubmit.co/annie10302004@gmail.com" method="POST">')

# Add name attributes to inputs
html = html.replace('<input id="fn" class="finp" type="text" placeholder="Jane Smith" required/>', '<input id="fn" name="name" class="finp" type="text" placeholder="Jane Smith" required/>')
html = html.replace('<input id="fe" class="finp" type="email" placeholder="jane@studio.com" required/>', '<input id="fe" name="email" class="finp" type="email" placeholder="jane@studio.com" required/>')
html = html.replace('<textarea id="fm" class="ftxt" placeholder="Tell me about your project" required></textarea>', '<textarea id="fm" name="message" class="ftxt" placeholder="Tell me about your project" required></textarea>')

# Add a honeypot field and next redirect (optional, but good for formsubmit)
# Actually, standard formsubmit works without it, it just redirects to their thank you page.

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed contact form")
