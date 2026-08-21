/* cursor.js — Custom star cursor with smooth lerp follow */
(function () {
  const cursor = document.getElementById('customCursor');
  if (!cursor) return;

  let mouseX = -100, mouseY = -100;
  let curX = -100, curY = -100;

  document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
  });

  // Smooth lerp
  function lerp(a, b, t) { return a + (b - a) * t; }

  function animate() {
    curX = lerp(curX, mouseX, 0.12);
    curY = lerp(curY, mouseY, 0.12);
    cursor.style.left = curX + 'px';
    cursor.style.top  = curY + 'px';
    requestAnimationFrame(animate);
  }
  animate();

  // Hover effects
  function addHover(selector, cls) {
    document.querySelectorAll(selector).forEach(el => {
      el.addEventListener('mouseenter', () => cursor.classList.add(cls));
      el.addEventListener('mouseleave', () => cursor.classList.remove(cls));
    });
  }

  // Delegate for dynamic content
  document.addEventListener('mouseover', (e) => {
    const target = e.target.closest('a, button, .project-card, .gateway__option, .dl-btn, .social-link, .track-item');
    if (target) {
      cursor.classList.add('hover');
    } else {
      cursor.classList.remove('hover');
    }
  });

  // Dark bg sections
  document.addEventListener('mouseover', (e) => {
    const dark = e.target.closest('.about, .downloads, .footer, .case-hero');
    if (dark) cursor.classList.add('on-dark');
    else cursor.classList.remove('on-dark');
  });
})();
