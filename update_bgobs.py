import re
with open('scripts/motion.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the bgObserver creation
old_obs = "const bgObserver = new IntersectionObserver((entries) => {"
new_obs = """const bgObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const id = entry.target.id;
            if (entry.target.classList.contains('hero')) window.currentCanvasTheme = 'star';
            else if (id) window.currentCanvasTheme = id;
        }
    });
}, { rootMargin: "-40% 0px -40% 0px", threshold: 0 });"""

# We'll use regex to cleanly replace the whole block
js = re.sub(r'const bgObserver = new IntersectionObserver.*?\{ threshold: 0.15 \}\);', new_obs, js, flags=re.DOTALL)
js = re.sub(r'const bgObserver = new IntersectionObserver.*?\{ threshold: 0.4 \}\);', new_obs, js, flags=re.DOTALL) # just in case

with open('scripts/motion.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated bgObserver logic")
