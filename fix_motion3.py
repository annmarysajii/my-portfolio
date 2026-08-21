import re

# 1. Update CSS
with open('css/motion.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix IDs
css = css.replace('.sec#motion', '.sec#videography')
css = css.replace('.sec#brand', '.sec#graphic-design')

# Make animations slower
css = css.replace('animation: squash-stretch 0.6s', 'animation: squash-stretch 1s')
css = css.replace('animation: whip-pan 0.6s', 'animation: whip-pan 1s')
css = css.replace('animation: comic-pop 0.5s', 'animation: comic-pop 0.8s')
css = css.replace('animation: brand-track 0.8s', 'animation: brand-track 1.2s')
css = css.replace('animation: waveform 1s', 'animation: waveform 1.5s')

# Add interactive individual letter hover for all chars
interactive_hover = """
/* Interactive individual letter hover (Squash & Stretch) */
.split-text .char:hover {
    animation: char-squash 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94) both !important;
    color: var(--yel);
    cursor: none;
}
@keyframes char-squash {
    0% { transform: scale(1, 1); }
    30% { transform: scale(1.3, 0.7); }
    40% { transform: scale(0.7, 1.3); }
    50% { transform: scale(1.15, 0.85); }
    65% { transform: scale(0.95, 1.05); }
    75% { transform: scale(1.05, 0.95); }
    100% { transform: scale(1, 1); }
}
"""

if "char-squash" not in css:
    css += interactive_hover

with open('css/motion.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update JS
with open('scripts/motion.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace("=== 'motion'", "=== 'videography'")
js = js.replace("=== 'brand'", "=== 'graphic-design'")
js = js.replace("window.currentCanvasTheme = 'motion'", "window.currentCanvasTheme = 'videography'")
js = js.replace("window.currentCanvasTheme = 'brand'", "window.currentCanvasTheme = 'graphic-design'")

with open('scripts/motion.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Fixed section IDs and added interactive char hover")
