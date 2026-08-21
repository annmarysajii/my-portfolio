from PIL import Image
from collections import Counter
import sys

def get_colors(img_path, num_colors):
    try:
        img = Image.open(img_path)
        img = img.convert('RGB')
        img.thumbnail((200, 200))
        pixels = list(img.getdata())
        counts = Counter(pixels)
        return counts.most_common(num_colors)
    except Exception as e:
        return str(e)

print("Green Arrow:")
print(get_colors("assets/portfolio-data/Green arrow/EcoFuture Color Pallette.png", 10))

print("\nGoBunny:")
print(get_colors("assets/portfolio-data/GoBunny_brand/GO BUNNY.png", 5))
