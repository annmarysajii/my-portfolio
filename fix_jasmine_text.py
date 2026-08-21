import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Indo-jazz
old_indo = 'Indo-jazz fusion multimedia project'
new_indo = 'jazz inspired multimedia project'
html = html.replace(old_indo, new_indo)

# Apply Jasmine description to the comic side
# Find the comic card-role
old_comic_desc = 'Comic and illustration work within the Jasmine world — character portraits, sequential comic panels, and world-building spreads.'
# The jasmine description from before
jasmine_desc = """Jasmine (2026) is a jazz inspired multimedia project featuring comics, music, character interviews and screenplay. This project is a story of a woman named Jasmine, who quits her job in New York to revive a jazz bar in Singapore. Jasmine aims to highlight the reality of managing creative spaces in Singapore and how we can find ways to sustain art related spaces in this economy. This is a concept album project with graphic storytelling elements, original music production and character explorations. Digital drawing tools like clip studio paint and Photoshop as well as music production tools such as Garageband, bandlab and splice were used to produce the final music for his project. This project is not just a story of a woman reviving a jazz bar but also a project about chasing your dreams and overcoming fears and building new bridges with people. Other than the complexities of managing a bar, interpersonal relationships and character dynamics are also explored in this story. This project is unique in the way it combines music and visual storytelling so that each chapter has a track specifically made for it that best represents the emotions and vibes of the story. It is present in a print format and can also be presented in a social media platform with the music produced for it playing in the background, thus making it a very adaptable project."""

html = html.replace(old_comic_desc, jasmine_desc)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated Jasmine descriptions and removed Indo-jazz")
