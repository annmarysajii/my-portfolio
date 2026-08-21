with open('css/motion.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('.hero-h {', '.hero-name {')

with open('css/motion.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixed sheen target class")
