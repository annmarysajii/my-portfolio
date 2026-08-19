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

    document.querySelectorAll('.sec, .card-img, .gw-header, .sec-title, .gallery-h, .text-block').forEach(el => {
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
            
            card.style.transform = perspective(1000px) scale3d(1.01, 1.01, 1.01) rotateX( + rotateX + deg) rotateY( + rotateY + deg);
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = perspective(1000px) scale3d(1, 1, 1) rotateX(0deg) rotateY(0deg);
            setTimeout(() => {
                card.style.transition = '';
            }, 100);
        });
        
        card.addEventListener('mouseenter', () => {
            card.style.transition = 'none';
        });
    });
});
