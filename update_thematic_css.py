import re

with open('css/motion.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove the generic hover
css = re.sub(r'/\* Interactive individual letter hover.*?\n}', '', css, flags=re.DOTALL)
css = re.sub(r'@keyframes char-squash \{.*?\}', '', css, flags=re.DOTALL)

# Let's completely replace the thematic typography section to make it pristine
thematic_start = css.find("/* --- THEMATIC TYPOGRAPHY ANIMATIONS --- */")
if thematic_start != -1:
    css = css[:thematic_start]

new_thematic = """/* --- THEMATIC TYPOGRAPHY ANIMATIONS --- */
.split-text { display: inline-block; }
.split-text .char { display: inline-block; white-space: pre; will-change: transform, filter, color, letter-spacing; }

/* 01 Animation: Squash & Stretch */
.sec#animation .sec-title.play-anim .char {
    animation: squash-stretch 1s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
    animation-delay: calc(var(--char-index) * 0.03s);
}
.sec#animation .sec-title .char:hover {
    animation: char-squash 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94) both !important;
    color: var(--yel) !important;
}
@keyframes squash-stretch {
    0% { transform: scale(1, 1); }
    30% { transform: scale(1.25, 0.75); }
    40% { transform: scale(0.75, 1.25); }
    50% { transform: scale(1.15, 0.85); }
    65% { transform: scale(0.95, 1.05); }
    75% { transform: scale(1.05, 0.95); }
    100% { transform: scale(1, 1); }
}
@keyframes char-squash {
    0% { transform: scale(1, 1); }
    30% { transform: scale(1.3, 0.7); }
    40% { transform: scale(0.7, 1.3); }
    50% { transform: scale(1.15, 0.85); }
    65% { transform: scale(0.95, 1.05); }
    100% { transform: scale(1, 1); }
}

/* 02 Illustration: Comic Pop */
.sec#illustration .sec-title.play-anim .char {
    animation: comic-pop 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275) both;
    animation-delay: calc(var(--char-index) * 0.04s);
    transform-origin: bottom center;
}
.sec#illustration .sec-title .char:hover {
    animation: comic-pop 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) both !important;
    color: var(--yel) !important;
}
@keyframes comic-pop {
    0% { transform: scale(1) rotate(0); color: inherit; }
    30% { transform: scale(1.3) rotate(-5deg); color: var(--yel); }
    70% { transform: scale(0.9) rotate(5deg); }
    100% { transform: scale(1) rotate(0); color: inherit; }
}

/* 03 Videography & Motion: Whip Pan */
.sec#videography .sec-title.play-anim .char {
    animation: whip-pan 1s cubic-bezier(0.4, 0, 0.2, 1) both;
    animation-delay: calc(var(--char-index) * 0.02s);
}
.sec#videography .sec-title .char:hover {
    animation: whip-pan 0.6s cubic-bezier(0.4, 0, 0.2, 1) both !important;
}
@keyframes whip-pan {
    0% { transform: translateX(-20px) skewX(25deg); filter: blur(4px); opacity: 0; }
    50% { transform: translateX(5px) skewX(-10deg); filter: blur(1px); opacity: 1; }
    100% { transform: translateX(0) skewX(0); filter: blur(0); opacity: 1; }
}

/* 04 Graphic Design & Brand: Vector Path Construction */
.sec#graphic-design .sec-title.play-anim .char {
    animation: vector-build 1.2s cubic-bezier(0.25, 1, 0.5, 1) both;
    animation-delay: calc(var(--char-index) * 0.08s);
}
.sec#graphic-design .sec-title .char:hover {
    animation: vector-build 0.8s cubic-bezier(0.25, 1, 0.5, 1) both !important;
}
@keyframes vector-build {
    0% { color: transparent; -webkit-text-stroke: 1.5px var(--yel); }
    40% { color: transparent; -webkit-text-stroke: 1.5px var(--ink); }
    100% { color: var(--ink); -webkit-text-stroke: 0px transparent; }
}

/* 05 Music: Waveform */
.sec#music .sec-title.play-anim .char {
    animation: waveform 1.5s ease-in-out infinite;
    animation-delay: calc(var(--char-index) * 0.08s);
}
.sec#music .sec-title .char:hover {
    animation: waveform-hover 0.8s ease-in-out both !important;
    color: var(--yel) !important;
}
@keyframes waveform {
    0%, 100% { transform: translateY(0); color: inherit; }
    50% { transform: translateY(-8px); color: var(--yel); }
}
@keyframes waveform-hover {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-12px); }
}
"""

css += new_thematic

with open('css/motion.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated motion.css with thematic hover interactions")
