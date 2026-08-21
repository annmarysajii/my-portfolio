css_additions = """
/* --- ADVANCED MOGRAPH INTERACTIONS --- */

/* 1. Animation Section - Squash & Stretch per letter */
.sec#animation .char.hovered {
    animation: char-squash 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) both !important;
    color: var(--yel);
    display: inline-block;
    transform-origin: center bottom;
}

@keyframes char-squash {
    0% { transform: scale(1, 1); }
    15% { transform: scale(1.4, 0.6); }
    30% { transform: scale(0.6, 1.4); }
    45% { transform: scale(1.2, 0.8); }
    60% { transform: scale(0.9, 1.1); }
    75% { transform: scale(1.05, 0.95); }
    100% { transform: scale(1, 1); }
}

/* 2. Graphic Design - Construction/Wireframe effect on hover */
.sec#graphic-design .char.hovered {
    animation: construct-stroke 1s forwards !important;
    color: transparent;
    -webkit-text-stroke: 2px var(--ink);
    position: relative;
}
.sec#graphic-design .char.hovered::after {
    content: '';
    position: absolute;
    width: 6px; height: 6px;
    background: var(--bg);
    border: 2px solid var(--ink);
    border-radius: 50%;
    top: 0; left: 0;
    animation: anchor-point 1s infinite;
}
@keyframes construct-stroke {
    0% { -webkit-text-stroke: 2px transparent; color: var(--ink); }
    20% { -webkit-text-stroke: 2px var(--ink); color: transparent; }
    80% { -webkit-text-stroke: 2px var(--ink); color: transparent; }
    100% { -webkit-text-stroke: 2px transparent; color: var(--ink); }
}
@keyframes anchor-point {
    0% { transform: translate(0,0); opacity:1; }
    25% { transform: translate(15px, 5px); }
    50% { transform: translate(5px, 20px); }
    100% { transform: translate(0,0); opacity:0; }
}

/* 3. Graphic Design Background - Blueprint Grid Reveal */
.sec#graphic-design {
    position: relative;
    overflow: hidden;
}
.sec#graphic-design::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image: linear-gradient(var(--ink12) 1px, transparent 1px), linear-gradient(90deg, var(--ink12) 1px, transparent 1px);
    background-size: 40px 40px;
    opacity: 0;
    transition: opacity 1s;
    pointer-events: none;
    z-index: 0;
}
.sec#graphic-design:hover::before {
    opacity: 1;
    animation: grid-pan 20s linear infinite;
}
@keyframes grid-pan {
    0% { transform: translate(0, 0); }
    100% { transform: translate(-40px, -40px); }
}

/* 4. Illustration Background - Halftone Dots */
.sec#illustration {
    position: relative;
    overflow: hidden;
}
.sec#illustration::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image: radial-gradient(var(--yel) 2px, transparent 2px);
    background-size: 20px 20px;
    opacity: 0;
    transition: opacity 1s, transform 2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    transform: scale(0.5);
    pointer-events: none;
    z-index: 0;
}
.sec#illustration:hover::before {
    opacity: 0.15;
    transform: scale(1);
}

/* 5. Videography - Glitch Hover per letter */
.sec#videography .char.hovered {
    animation: text-glitch 0.4s infinite !important;
}
@keyframes text-glitch {
    0% { transform: translate(0); text-shadow: none; }
    20% { transform: translate(-2px, 1px); text-shadow: 2px 0 red, -2px 0 cyan; }
    40% { transform: translate(2px, -1px); text-shadow: none; }
    60% { transform: translate(-1px, 2px); text-shadow: -2px 0 red, 2px 0 cyan; }
    80% { transform: translate(1px, -2px); text-shadow: none; }
    100% { transform: translate(0); text-shadow: 2px 0 red, -2px 0 cyan; }
}
"""

with open('css/motion.css', 'a', encoding='utf-8') as f:
    f.write(css_additions)
print("Added advanced mograph interactions to motion.css")
