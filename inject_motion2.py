import os

with open('css/motion.css', 'a', encoding='utf-8') as f:
    f.write("""

/* --- SHEEN EFFECT --- */
.hero-h {
    background: linear-gradient(120deg, var(--ink) 35%, #D93020 45%, var(--yel) 50%, #D93020 55%, var(--ink) 65%);
    background-size: 300% auto;
    color: transparent;
    -webkit-background-clip: text;
    background-clip: text;
    animation: sheen 5s linear infinite;
}
@keyframes sheen {
    0% { background-position: 100% center; }
    20% { background-position: 0% center; }
    100% { background-position: 0% center; }
}

/* --- THEMATIC TYPOGRAPHY ANIMATIONS --- */
.split-text { display: inline-block; }
.split-text .char { display: inline-block; white-space: pre; will-change: transform, filter, color, letter-spacing; }

/* 01 Animation: Squash & Stretch */
.sec#animation .sec-title.play-anim .char, .sec#animation .sec-title:hover .char {
    animation: squash-stretch 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
    animation-delay: calc(var(--char-index) * 0.03s);
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

/* 02 Illustration: Comic Pop */
.sec#illustration .sec-title.play-anim .char, .sec#illustration .sec-title:hover .char {
    animation: comic-pop 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) both;
    animation-delay: calc(var(--char-index) * 0.04s);
    transform-origin: bottom center;
}
@keyframes comic-pop {
    0% { transform: scale(1) rotate(0); color: inherit; }
    30% { transform: scale(1.3) rotate(-5deg); color: var(--yel); }
    70% { transform: scale(0.9) rotate(5deg); }
    100% { transform: scale(1) rotate(0); color: inherit; }
}

/* 03 Videography & Motion: Whip Pan */
.sec#motion .sec-title.play-anim .char, .sec#motion .sec-title:hover .char {
    animation: whip-pan 0.6s cubic-bezier(0.4, 0, 0.2, 1) both;
    animation-delay: calc(var(--char-index) * 0.02s);
}
@keyframes whip-pan {
    0% { transform: translateX(-20px) skewX(25deg); filter: blur(4px); opacity: 0; }
    50% { transform: translateX(5px) skewX(-10deg); filter: blur(1px); opacity: 1; }
    100% { transform: translateX(0) skewX(0); filter: blur(0); opacity: 1; }
}

/* 04 Brand: Tracking / Grid Expansion */
.sec#brand .sec-title.play-anim, .sec#brand .sec-title:hover {
    animation: brand-track 0.8s cubic-bezier(0.25, 1, 0.5, 1) forwards;
}
@keyframes brand-track {
    0% { letter-spacing: normal; font-weight: 600; }
    40% { letter-spacing: 0.15em; font-weight: 700; color: #D93020; }
    100% { letter-spacing: normal; font-weight: 600; }
}

/* 05 Music: Waveform */
.sec#music .sec-title.play-anim .char, .sec#music .sec-title:hover .char {
    animation: waveform 1s ease-in-out infinite;
    animation-delay: calc(var(--char-index) * 0.08s);
}
@keyframes waveform {
    0%, 100% { transform: translateY(0); color: inherit; }
    50% { transform: translateY(-8px); color: var(--yel); }
}
""")

with open('scripts/motion.js', 'a', encoding='utf-8') as f:
    f.write("""
    
    // 4. Text Splitting for Typography Animations
    document.querySelectorAll('.sec-title').forEach(title => {
        const html = title.innerHTML;
        const parts = html.split(/<br\\s*\\/?>/i);
        
        let charIndex = 0;
        const newHtml = parts.map(part => {
            const tempDiv = document.createElement('div');
            tempDiv.innerHTML = part;
            const text = tempDiv.textContent; 
            
            let partHtml = '';
            for(let i=0; i<text.length; i++){
                const char = text[i];
                if(char === ' ') {
                    partHtml += ' '; 
                } else {
                    partHtml += `<span class="char" style="--char-index:${charIndex}">${char}</span>`;
                    charIndex++;
                }
            }
            return partHtml;
        }).join('<br>');
        
        title.innerHTML = newHtml;
        title.classList.add('split-text');
    });

    // Add .play-anim class when intersecting
    const typeObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('play-anim');
                // Remove class after animation completes so hover can re-trigger it
                setTimeout(() => entry.target.classList.remove('play-anim'), 1200);
            }
        });
    }, { threshold: 0.5 });
    
    document.querySelectorAll('.sec-title').forEach(el => typeObserver.observe(el));
""")

print("Injected Sheen and Typography Animations")
