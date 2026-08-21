document.addEventListener("DOMContentLoaded", () => {
    // 1. Intersection Observer for Scroll Reveals
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.05, rootMargin: "0px 0px -40px 0px" });

    document.querySelectorAll('.sec, .card, .gw-header, .sec-title, .gallery-h, .text-block').forEach(el => {
        if (!el.classList.contains('reveal')) {
            el.classList.add('reveal');
        }
        observer.observe(el);
    });

    // 2. Smooth Page Transitions
    const links = document.querySelectorAll('a[href]:not([target="_blank"]):not([href^="#"]):not([download])');
    links.forEach(link => {
        link.addEventListener('click', (e) => {
            const href = link.getAttribute('href');
            if (href && !href.startsWith('mailto:') && !href.startsWith('javascript:')) {
                e.preventDefault();
                document.body.classList.add('fade-out');
                setTimeout(() => {
                    window.location.href = href;
                }, 350); 
            }
        });
    });

    // 3. 3D Tilt Effect on Cards
    const cards = document.querySelectorAll('.card-img, .gw-opt');
    cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            
            // Max tilt 4 degrees
            const rotateX = ((y - centerY) / centerY) * -4;
            const rotateY = ((x - centerX) / centerX) * 4;
            
            card.style.transform = `perspective(1000px) scale3d(1.01, 1.01, 1.01) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = `perspective(1000px) scale3d(1, 1, 1) rotateX(0deg) rotateY(0deg)`;
            setTimeout(() => {
                card.style.transition = '';
            }, 100);
        });
        
        card.addEventListener('mouseenter', () => {
            card.style.transition = 'none';
        });
    });
});

    
    // 4. Text Splitting for Typography Animations
    document.querySelectorAll('.sec-title').forEach(title => {
        const html = title.innerHTML;
        const parts = html.split(/<br\s*\/?>/i);
        
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


    // 5. Thematic Falling Backgrounds
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
}, { threshold: [0, 0.1, 0.2, 0.3, 0.5] });
    
    document.querySelectorAll('.sec, .hero').forEach(el => bgObserver.observe(el));
