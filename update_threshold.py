import re

with open('scripts/motion.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace threshold 0.4 with a safe threshold
js = js.replace('threshold: 0.4', 'threshold: 0.15')

with open('scripts/motion.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated bgObserver threshold")
