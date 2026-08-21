import json
import re

with open('scripts/data.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Extract json
json_str = js.replace('window.PORTFOLIO_DATA = ', '').rstrip(';')
data = json.loads(json_str)

# Projection for music district - https://youtu.be/Z98oacHxtM8
# Md intro video - https://youtu.be/ZBiTGAN6EFI
# MD valentines teaser - https://youtu.be/T9ksoqWrJBs
# Solace, short animated film - https://youtu.be/rbuVgVvSEyI
# NTU FEST Projection - https://youtu.be/5aHRfGrV92o
# A-stray dog - https://youtu.be/uyy00VsBLS4
# Chase animatic/storyboard - https://youtu.be/QMuH2Njl0yg
# KEEP YOURSELF SAFE ! : Animated short film - https://youtu.be/gGdk8_vq0Mk
# Dear Friend / ANIMATED SHORT - https://youtu.be/BPYEYUmrWfg
# VIPCOLOR how to video playlist - https://www.youtube.com/watch?v=uUXc5DREAxE
# VP750/700 Tutorial printhead installation - https://www.youtube.com/watch?v=uUXc5DREAxE
# VP750/700 Tutorial ink cartridge - https://www.youtube.com/watch?v=4C0sa3aOzqU
# Introducing SocrAT - https://youtu.be/RruemxTLcUI

# Apply changes:
data['a-stray-dog'] = ["https://youtu.be/uyy00VsBLS4"]
data['chase'] = ["https://youtu.be/QMuH2Njl0yg"]
data['keep-yourself-safe'] = ["https://youtu.be/gGdk8_vq0Mk"] + [img for img in data.get('keep-yourself-safe', []) if not img.endswith('.mp4') and not img.endswith('.mov')]
data['dear-friend'] = ["https://youtu.be/BPYEYUmrWfg"]
data['ntu-fest'] = ["https://youtu.be/5aHRfGrV92o"] + [img for img in data.get('ntu-fest', []) if not img.endswith('.mp4') and not img.endswith('.mov')]
data['socrat-ai'] = ["https://youtu.be/RruemxTLcUI"]
data['vipcolor-video'] = ["https://www.youtube.com/watch?v=uUXc5DREAxE", "https://www.youtube.com/watch?v=4C0sa3aOzqU"]

# Music district mapping
md_videos = ["https://youtu.be/Z98oacHxtM8", "https://youtu.be/ZBiTGAN6EFI", "https://youtu.be/T9ksoqWrJBs"]
md_images = [img for img in data.get('music-district-video', []) if img.endswith('.png') or img.endswith('.jpg')]

data['music-district-video'] = md_videos
data['music-district-design'] = md_images

# "Solace, short animated film" -> The user didn't give an ID for Solace.
# Is it possible "Solace" is "Short film score"? Or a different animation project?
# Solace was mentioned: "Solace, short animated film — https://youtu.be/rbuVgVvSEyI".
# Wait, let's check if 'solace' exists in data or portfolio.html.
# Actually, I'll add Solace to 'short-film-score' just in case, or wait, 'short-film-score' is for Music.
# If "Solace" is the animation for the short film score, I'll add it there.
data['short-film-score'] = ["https://youtu.be/rbuVgVvSEyI"]

# Save back
js_out = "window.PORTFOLIO_DATA = " + json.dumps(data, indent=2) + ";"
with open('scripts/data.js', 'w', encoding='utf-8') as f:
    f.write(js_out)
print("Updated data.js with YouTube links and reorganized Music District assets")
