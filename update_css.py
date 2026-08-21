import re

with open('css/motion.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add float animation for the avatar
float_anim = """
@keyframes float {
    0% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-10px) rotate(2deg); }
    100% { transform: translateY(0px) rotate(0deg); }
}
"""
css += float_anim

# Simplify advanced mograph interactions to prevent lag
# Remove the per-character logic
css = re.sub(r'/\* --- ADVANCED MOGRAPH INTERACTIONS --- \*/.*', '', css, flags=re.DOTALL)

# Add back lightweight performant animations for the headers!
lightweight_mograph = """
/* --- ADVANCED MOGRAPH INTERACTIONS --- */

/* 1. Animation Section - Squash & Stretch on whole word */
.sec#animation .sec-title {
    transition: transform 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94), color 0.4s;
    display: inline-block;
    transform-origin: left bottom;
}
.sec#animation .sec-title:hover {
    transform: scale(1.1, 0.9) skewX(-5deg);
    color: var(--yel);
}

/* 2. Graphic Design - Construction/Wireframe effect on whole word */
.sec#graphic-design .sec-title {
    transition: all 0.3s ease;
    display: inline-block;
}
.sec#graphic-design .sec-title:hover {
    color: transparent;
    -webkit-text-stroke: 1.5px var(--ink);
    text-shadow: 4px 4px 0px rgba(0,0,0,0.1);
}

/* 3. Graphic Design Background - Blueprint Grid Reveal (GPU optimized) */
.sec#graphic-design {
    position: relative;
    overflow: hidden;
}
.sec#graphic-design::before {
    content: '';
    position: absolute;
    inset: -50%;
    background-image: linear-gradient(var(--ink12) 1px, transparent 1px), linear-gradient(90deg, var(--ink12) 1px, transparent 1px);
    background-size: 40px 40px;
    opacity: 0;
    transition: opacity 0.5s;
    pointer-events: none;
    z-index: 0;
    will-change: transform, opacity;
}
.sec#graphic-design:hover::before {
    opacity: 1;
    animation: grid-pan 30s linear infinite;
}
@keyframes grid-pan {
    0% { transform: translate(0, 0); }
    100% { transform: translate(40px, 40px); }
}

/* 4. Illustration Background - Halftone Dots (GPU optimized) */
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
    transition: opacity 0.5s;
    pointer-events: none;
    z-index: 0;
}
.sec#illustration:hover::before {
    opacity: 0.15;
}

/* 5. Videography - Glitch Hover on whole word */
.sec#videography .sec-title {
    transition: text-shadow 0.2s;
    display: inline-block;
}
.sec#videography .sec-title:hover {
    animation: simple-glitch 0.3s infinite;
}
@keyframes simple-glitch {
    0% { transform: translate(0); text-shadow: none; }
    25% { transform: translate(-1px, 1px); text-shadow: 2px 0 red, -2px 0 cyan; }
    50% { transform: translate(1px, -1px); text-shadow: none; }
    75% { transform: translate(-1px, 0px); text-shadow: -2px 0 red, 2px 0 cyan; }
    100% { transform: translate(0); text-shadow: none; }
}
"""
css += lightweight_mograph

with open('css/motion.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated CSS with performant mographs and float animation")
