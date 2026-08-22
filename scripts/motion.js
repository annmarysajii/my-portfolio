document.addEventListener("DOMContentLoaded", () => {
    // 1. Force reveal all elements immediately on iPad / all screens
    const forceShow = () => {
        document.querySelectorAll('.sec, .card, .gw-header, .sec-title, .gallery-h, .text-block, .reveal, .rv').forEach(el => {
            el.classList.add('visible', 'show');
        });
    };
    forceShow();
    window.addEventListener('load', forceShow);
    setTimeout(forceShow, 200);
    setTimeout(forceShow, 800);

    // 2. Smooth Page Transitions (Safe)
    const links = document.querySelectorAll('a[href]:not([target="_blank"]):not([href^="#"]):not([download])');
    links.forEach(link => {
        link.addEventListener('click', (e) => {
            const href = link.getAttribute('href');
            if (href && !href.startsWith('mailto:') && !href.startsWith('javascript:') && !href.startsWith('tel:')) {
                // allow normal navigation
            }
        });
    });

    // 3. Text Splitting for Thematic Typography Animations
    document.querySelectorAll('.sec-title').forEach(title => {
        const html = title.innerHTML;
        const parts = html.split(/<br\s*\/?>/i);
        
        let charIndex = 0;
        const newHtml = parts.map(part => {
            const tempDiv = document.createElement('div');
            tempDiv.innerHTML = part;
            const text = tempDiv.textContent; 
            
            let partHtml = '';
            for(let i = 0; i < text.length; i++){
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

    // 4. Thematic Falling Backgrounds
    let intersectingSecs = new Set();
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
            if (sec.id === 'music' && (window.innerHeight + window.scrollY) >= document.body.offsetHeight - 100) {
                best = sec;
                minDiff = -1;
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
    }, { threshold: [0, 0.1, 0.2, 0.3, 0.5] });
    
    document.querySelectorAll('.sec, .hero').forEach(el => bgObserver.observe(el));
});
