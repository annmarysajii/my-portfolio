import re

def replace_in_file(filepath, old_text, new_text):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_text in content:
        content = content.replace(old_text, new_text)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"Text not found in {filepath}")

old_desc = "Jasmine (2026) is a jazz inspired multimedia project featuring comics, music, character interviews and screenplay. This project is a story of a woman named Jasmine, who quits her job in New York to revive a jazz bar in Singapore. Jasmine aims to highlight the reality of managing creative spaces in Singapore and how we can find ways to sustain art related spaces in this economy. This is a concept album project with graphic storytelling elements, original music production and character explorations. Digital drawing tools like clip studio paint and Photoshop as well as music production tools such as Garageband, bandlab and splice were used to produce the final music for his project. This project is not just a story of a woman reviving a jazz bar but also a project about chasing your dreams and overcoming fears and building new bridges with people. Other than the complexities of managing a bar, interpersonal relationships and character dynamics are also explored in this story. This project is unique in the way it combines music and visual storytelling so that each chapter has a track specifically made for it that best represents the emotions and vibes of the story. It is present in a print format and can also be presented in a social media platform with the music produced for it playing in the background, thus making it a very adaptable project."

new_desc = "Jasmine (2026) is a jazz-inspired multimedia project featuring comics, music, character interviews, and a screenplay. It follows Jasmine, a woman who quits her job in New York to revive a jazz bar in Singapore, highlighting the reality of sustaining creative spaces in this economy. This concept album merges original music production (GarageBand, BandLab, Splice) with graphic storytelling (Clip Studio Paint, Photoshop). Beyond the complexities of managing a bar, it's a story about chasing dreams, overcoming fears, and interpersonal dynamics. Uniquely, each chapter features a dedicated track representing its emotional core, designed to be adaptable across print and social media platforms."

replace_in_file('portfolio.html', old_desc, new_desc)
replace_in_file('project.html', old_desc, new_desc)
