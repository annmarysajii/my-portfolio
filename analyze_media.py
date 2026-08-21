import os
import re
import json

base_dir = r"assets\portfolio-data"
mapping = {
    "A stray dog": "a-stray-dog",
    "Campus wellbeing comic": "wellbeing-planner",
    "Character and concept art": "freelance-commissions",
    "Chase_storyboard": "chase",
    "Dear friend": "dear-friend",
    "Digital painting": "digital-paintings",
    "Event posters": "mock-posters",
    "Global connect fellowship": "gcf-documentary",
    "GoBunny_brand": "gobunny",
    "Green arrow": "green-arrow",
    "Internship experience comic series": "internship-comics",
    "jasmine comic full": "jasmine-comic",
    "Jasmine_music_concept album": "jasmine-album",
    "Jasmine_Visdev": "jasmine-visdev",
    "Keep yourself safe": "keep-yourself-safe",
    "Music district assets": "music-district-video", 
    "Nangeli": "nangele",
    "Ntu fest assets": "ntu-fest",
    "NTU web and social banners": "ntu-banners",
    "obesity": "obesity-infographic",
    "Original demo tracks": "original-tracks",
    "RE-kindle": "rekindle",
    "Short film score": "short-film-score",
    "Socrat ai": "socrat-ai",
    "VIP_color how to series": "vipcolor-video"
}

project_media = {}

for folder, id_name in mapping.items():
    folder_path = os.path.join(base_dir, folder)
    if os.path.isdir(folder_path):
        files = []
        for file in os.listdir(folder_path):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.mp4', '.mov', '.webm')):
                files.append(f"assets/portfolio-data/{folder}/{file}".replace('\\', '/'))
        project_media[id_name] = files

print(json.dumps(project_media, indent=2))
