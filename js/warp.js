/* warp.js — 3D Space Tunnel Warp Transition */
(function () {
  const canvas = document.getElementById('warp-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let W, H, stars, animId, destination;

  function resize() {
    W = canvas.width  = window.innerWidth;
    H = canvas.height = window.innerHeight;
  }

  window.addEventListener('resize', resize);
  resize();

  function createStar() {
    return {
      x: (Math.random() - 0.5) * W,
      y: (Math.random() - 0.5) * H,
      z: Math.random() * W,
      pz: 0
    };
  }

  function initStars(count) {
    stars = Array.from({ length: count }, createStar);
    stars.forEach(s => s.pz = s.z);
  }

  let speed = 0;
  let progress = 0;
  let running = false;

  function drawFrame() {
    // Background fade to dark
    const alpha = Math.min(1, progress * 1.5);
    ctx.fillStyle = `rgba(5, 8, 20, ${0.15 + alpha * 0.15})`;
    ctx.fillRect(0, 0, W, H);

    speed = 20 + progress * 120;
    const cx = W / 2, cy = H / 2;

    stars.forEach(s => {
      s.pz = s.z;
      s.z -= speed;

      if (s.z <= 0) {
        s.x  = (Math.random() - 0.5) * W;
        s.y  = (Math.random() - 0.5) * H;
        s.z  = W;
        s.pz = s.z;
      }

      const sx  = (s.x  / s.z)  * W + cx;
      const sy  = (s.y  / s.z)  * H + cy;
      const spx = (s.x  / s.pz) * W + cx;
      const spy = (s.y  / s.pz) * H + cy;

      const size = Math.max(0.5, (1 - s.z / W) * 3.5);
      const brightness = Math.floor((1 - s.z / W) * 255);
      const r = Math.min(255, brightness + 80);
      const g = Math.min(255, brightness + 60);
      const b = 255;

      ctx.beginPath();
      ctx.moveTo(spx, spy);
      ctx.lineTo(sx, sy);
      ctx.strokeStyle = `rgba(${r},${g},${b},${0.4 + (1 - s.z / W) * 0.6})`;
      ctx.lineWidth = size;
      ctx.stroke();
    });

    progress += 0.012;

    if (progress >= 1) {
      running = false;
      cancelAnimationFrame(animId);
      navigate();
    } else {
      animId = requestAnimationFrame(drawFrame);
    }
  }

  function navigate() {
    if (destination) {
      setTimeout(() => { window.location.href = destination; }, 80);
    }
  }

  // Check prefers-reduced-motion
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  window.triggerWarp = function (filter) {
    destination = 'portfolio.html?filter=' + filter;
    if (prefersReduced) { window.location.href = destination; return; }

    // Fade gateway out
    const gateway = document.getElementById('gateway');
    if (gateway) gateway.classList.add('fade-out');

    canvas.classList.add('active');
    ctx.clearRect(0, 0, W, H);
    ctx.fillStyle = '#050814';
    ctx.fillRect(0, 0, W, H);

    initStars(380);
    progress = 0;
    running = true;
    animId = requestAnimationFrame(drawFrame);
  };
})();
