import re

with open('scripts/data.js', 'r', encoding='utf-8') as f:
    js = f.read()

old_arr = """  "ntu-fest": [
    "https://youtu.be/5aHRfGrV92o",
    "assets/portfolio-data/Ntu fest assets/SIGN UP AS A STUDENT VENDOR HERE (1).png",
    "assets/portfolio-data/Ntu fest assets/SunDown.png"
  ],"""

new_arr = """  "ntu-fest": [
    "assets/portfolio-data/Ntu fest assets/ntufest_portfoliogif.gif.mp4",
    "https://youtu.be/5aHRfGrV92o",
    "assets/portfolio-data/Ntu fest assets/ntufest_banner.png",
    "assets/portfolio-data/Ntu fest assets/ntu fest cover.png",
    "assets/portfolio-data/Ntu fest assets/performer images (1).png",
    "assets/portfolio-data/Ntu fest assets/performer images (2).png",
    "assets/portfolio-data/Ntu fest assets/performer images (3).png",
    "assets/portfolio-data/Ntu fest assets/SIGN UP AS A STUDENT VENDOR HERE (1).png",
    "assets/portfolio-data/Ntu fest assets/SunDown.png"
  ],"""

if 'ntufest_portfoliogif' not in js:
    # try regex replacement to ignore whitespace issues
    js = re.sub(r'"ntu-fest":\s*\[[^\]]+\]\s*,', new_arr, js)
    
    with open('scripts/data.js', 'w', encoding='utf-8') as f:
        f.write(js)
print("Updated data.js")
