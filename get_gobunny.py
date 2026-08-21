from PIL import Image
from collections import Counter

img = Image.open("assets/portfolio-data/GoBunny_brand/Your paragraph text (35).png")
img = img.convert('RGB')
pixels = list(img.getdata())
counts = Counter(pixels)
print("GoBunny 35:", counts.most_common(3))

img2 = Image.open("assets/portfolio-data/GoBunny_brand/Your paragraph text (33).png")
img2 = img2.convert('RGB')
print("GoBunny 33:", Counter(list(img2.getdata())).most_common(3))
