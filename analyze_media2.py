import os
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
valid_exts = ('.png', '.jpg', '.jpeg', '.gif', '.mp4', '.mov', '.webm', '.m4a', '.mp3', '.wav', '.pdf')

for folder, id_name in mapping.items():
    folder_path = os.path.join(base_dir, folder)
    if os.path.isdir(folder_path):
        files_list = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith(valid_exts):
                    rel_path = os.path.relpath(os.path.join(root, file), base_dir)
                    files_list.append(f"assets/portfolio-data/{rel_path}".replace('\\', '/'))
        project_media[id_name] = files_list

# Save to a JSON file
with open('assets/portfolio-data.json', 'w', encoding='utf-8') as f:
    json.dump(project_media, f, indent=2)
print("Saved to assets/portfolio-data.json")
