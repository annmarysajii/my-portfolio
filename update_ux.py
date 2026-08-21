import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the injected JS text splitter
html = re.sub(r'// Advanced Typography Mograph Splitter.*?</script>', '</script>', html, flags=re.DOTALL)

# 2. Remove the injected profile picture div I wrongly added
# I injected: <div style="flex: 1 1 250px; display:flex; justify-content:center; padding-top:2rem;">...</div>
# Let's find and remove it.
wrong_img = r'<div style="flex: 1 1 250px; display:flex; justify-content:center; padding-top:2rem;">\s*<img src="assets/portfolio-data/My profile/me avatar.png"[^>]*>\s*</div>'
html = re.sub(wrong_img, '', html)

# 3. Replace the actual .about-photo box
old_photo = '<div class="about-photo"><span class="ab-ph-t">Photo coming soon</span></div>'
new_photo = '<img src="assets/portfolio-data/My profile/me avatar.png" class="about-photo" style="object-fit:cover; width:100%; height:auto; animation: float 6s ease-in-out infinite;">'
html = html.replace(old_photo, new_photo)

# 4. Replace Jasmine Description
# Since it's a massive description, I'll put it in Jasmine - Concept Album card.
jasmine_desc = """Jasmine (2026) is a jazz inspired multimedia project featuring comics, music, character interviews and screenplay. This project is a story of a woman named Jasmine, who quits her job in New York to revive a jazz bar in Singapore. Jasmine aims to highlight the reality of managing creative spaces in Singapore and how we can find ways to sustain art related spaces in this economy. This is a concept album project with graphic storytelling elements, original music production and character explorations. Digital drawing tools like clip studio paint and Photoshop as well as music production tools such as Garageband, bandlab and splice were used to produce the final music for his project. This project is not just a story of a woman reviving a jazz bar but also a project about chasing your dreams and overcoming fears and building new bridges with people. Other than the complexities of managing a bar, interpersonal relationships and character dynamics are also explored in this story. This project is unique in the way it combines music and visual storytelling so that each chapter has a track specifically made for it that best represents the emotions and vibes of the story. It is present in a print format and can also be presented in a social media platform with the music produced for it playing in the background, thus making it a very adaptable project."""

# We will replace the text of Jasmine - Concept Album card-role
old_jasmine_role = 'Original Indo-jazz fusion EP composed, produced, and directed for physical and streaming release. Tracks: "Welcome to the Jasmine," "Home Pt. 1 and 2," "Night Time," "Kopi."'
html = html.replace(old_jasmine_role, jasmine_desc)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Cleaned up HTML, fixed avatar, and updated Jasmine desc")
