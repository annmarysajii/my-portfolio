import re

with open('scripts/motion.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_obs = """let intersectingSecs = new Set();
const bgObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            intersectingSecs.add(entry.target);
        } else {
            intersectingSecs.delete(entry.target);
        }
    });
    
    let best = null;
    let minDiff = Infinity;
    const centerY = window.innerHeight * 0.5;
    
    intersectingSecs.forEach(sec => {
        const rect = sec.getBoundingClientRect();
        // If it's the music section (last) and we're at the bottom of the page, prioritize it
        if (sec.id === 'music' && (window.innerHeight + window.scrollY) >= document.body.offsetHeight - 100) {
            best = sec;
            minDiff = -1; // force it
        } else {
            const secCenter = rect.top + rect.height/2;
            const diff = Math.abs(secCenter - centerY);
            if (diff < minDiff) {
                minDiff = diff;
                best = sec;
            }
        }
    });
    
    if (best) {
        if (best.classList.contains('hero')) window.currentCanvasTheme = 'star';
        else if (best.id) window.currentCanvasTheme = best.id;
    }
}, { threshold: [0, 0.1, 0.2, 0.3, 0.5] });"""

# Replace the existing bgObserver block
js = re.sub(r'const bgObserver = new IntersectionObserver.*?\{ rootMargin: "-40% 0px -40% 0px", threshold: 0 \}\);', new_obs, js, flags=re.DOTALL)
js = re.sub(r'const bgObserver = new IntersectionObserver.*?\{ rootMargin: "-30%.*?\}\);', new_obs, js, flags=re.DOTALL)

with open('scripts/motion.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated bgObserver to calculate closest center section")
