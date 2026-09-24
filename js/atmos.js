/* ATMOSPHERE LAYER. Loaded on every visit by portfolio.html (head). See css/atmos.css.
   1. the lamp: a pool of light that settles on the artwork in view, and the shadows that follow it
   2. pick it up: any artwork in a section lifts off the desk into a viewer; leaf through that section with arrows
   3. the Animation toy's buttons become rubber stamps */
(() => {
  const root = document.documentElement;
  const calm = () => matchMedia('(prefers-reduced-motion: reduce)').matches;
  const sfx = (n, k) => { try { window.__hnSfx && window.__hnSfx(n, k); } catch (e) {} };
  const SECTIONS = [...document.querySelectorAll('#wrap .sec.desk')];
  if (!SECTIONS.length) return;
  const all = sel => SECTIONS.flatMap(sec => [...sec.querySelectorAll(sel)]);

  // ---------------------------------------------------------------- 1. the lamp
  const lamp = document.createElement('div');
  lamp.className = 'atm-lamp'; lamp.setAttribute('aria-hidden', 'true');
  document.body.appendChild(lamp);
  const hero = document.getElementById('hero');
  // what the lamp is allowed to look at: the lead artwork, then each print
  // (the lead is lit as one block, image and words together, so its text is never left in the dark)
  const targets = () => all('.lc-body, .lc-steps, .grid .card');
  // the objects whose shadows answer the lamp
  const casters = () => all('.lc, .lc-scene img, .lc-scene video, .lc-thumb, .grid .card');
  let cur = null, want = null, raf = 0, on = 0;
  function pick() {
    const vh = innerHeight, mid = vh * 0.46;
    let best = null, bestD = Infinity;
    for (const el of targets()) {
      const r = el.getBoundingClientRect();
      if (r.bottom < 0 || r.top > vh || r.height === 0) continue;
      const cy = Math.min(Math.max(mid, r.top), r.bottom);   // distance from the reading line to the element, 0 if it spans it
      const d = Math.abs(cy - mid) + (el.matches('.lc-body') ? -120 : 0);
      if (d < bestD) { bestD = d; best = r; }
    }
    if (!best) return null;
    const pad = 1.45;
    return { x: best.left + best.width / 2, y: best.top + best.height / 2, w: Math.max(best.width * pad, 520), h: Math.max(best.height * 1.35 + 160, 420) };
  }
  function heroShare() {
    if (!hero) return 0;
    const r = hero.getBoundingClientRect();
    return Math.max(0, Math.min(1, r.bottom / innerHeight));
  }
  function frame() {
    raf = 0;
    want = pick() || want;
    const targetOn = want ? 1 - heroShare() : 0;         // the hero has its own light; this one takes over as it leaves
    if (!cur && want) cur = { ...want };
    const k = calm() ? 1 : 0.14;
    let moving = false;
    if (cur && want) for (const p of ['x', 'y', 'w', 'h']) { const d = want[p] - cur[p]; if (Math.abs(d) > 0.5) moving = true; cur[p] += d * k; }
    on += (targetOn - on) * (calm() ? 1 : 0.2); if (Math.abs(targetOn - on) > 0.005) moving = true;
    if (cur) {
      lamp.style.setProperty('--lx', cur.x + 'px'); lamp.style.setProperty('--ly', cur.y + 'px');
      lamp.style.setProperty('--lw', cur.w / 2 + 'px'); lamp.style.setProperty('--lh', cur.h / 2 + 'px');
      // shadows fall away from the pool, longer the further an object sits from it (the lamp is ~1.3 viewport-heights up)
      const lx = cur.x, ly = cur.y - innerHeight * 0.35, H = innerHeight * 1.3;
      for (const el of casters()) {
        const r = el.getBoundingClientRect();
        if (r.bottom < -200 || r.top > innerHeight + 200) continue;
        const dx = (r.left + r.width / 2 - lx) / H, dy = (r.top + r.height / 2 - ly) / H;
        el.style.setProperty('--sx', Math.max(-1.4, Math.min(1.4, dx * 1.6)).toFixed(3));
        el.style.setProperty('--sy', Math.max(0.25, Math.min(1.5, dy * 1.6)).toFixed(3));
      }
    }
    lamp.style.setProperty('--atm-on', on.toFixed(3));
    if (moving) raf = requestAnimationFrame(frame);
  }
  const kick = () => { if (!raf) raf = requestAnimationFrame(frame); };
  addEventListener('scroll', kick, { passive: true });
  addEventListener('resize', kick);
  new MutationObserver(kick).observe(root, { attributes: true, attributeFilter: ['data-theme'] });
  kick();

  // ---------------------------------------------------------------- 2. pick it up
  const esc = s => String(s || '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  function items(SECTION) {
    const out = [];
    const lead = SECTION.querySelector('.lc');
    const leadHref = lead && lead.querySelector('.lc-cta') ? lead.querySelector('.lc-cta').getAttribute('href') : null;
    const leadTitle = lead ? lead.querySelector('.lc-title').textContent.trim() : '';
    const scene = SECTION.querySelector('.lc-scene img, .lc-scene video');
    if (scene) out.push({ el: scene, media: scene, title: leadTitle, desc: (SECTION.querySelector('.lc-scene figcaption') || {}).textContent, href: leadHref });
    SECTION.querySelectorAll('.lc-step').forEach(st => {
      const img = st.querySelector('.lc-thumb'); if (!img) return;
      out.push({ el: img, media: img, title: leadTitle + ': ' + (st.querySelector('.lc-step-t') || {}).textContent, desc: (st.querySelector('.lc-step-d') || {}).textContent, href: leadHref });
    });
    SECTION.querySelectorAll('.grid .card').forEach(card => {
      const a = card.querySelector('.card-img'); if (!a) return;
      const media = a.querySelector('img, video'); if (!media) return;
      out.push({ el: a, media, title: (card.querySelector('.card-name') || {}).textContent, desc: (card.querySelector('.card-role') || {}).textContent, href: a.getAttribute('href') });
    });
    return out;
  }

  const dlg = document.createElement('dialog');
  dlg.className = 'atm-view';
  dlg.setAttribute('aria-label', 'Artwork viewer');
  const arrow = d => `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="${d}"/></svg>`;
  dlg.innerHTML =
    '<button type="button" class="atm-close">put it back</button>' +
    '<button type="button" class="atm-nav atm-prev" aria-label="Previous piece">' + arrow('M15 5l-7 7 7 7') + '</button>' +
    '<button type="button" class="atm-nav atm-next" aria-label="Next piece">' + arrow('M9 5l7 7-7 7') + '</button>' +
    '<div class="atm-stage"><div class="atm-print"></div><div class="atm-label"></div></div>';
  document.body.appendChild(dlg);
  const print = dlg.querySelector('.atm-print'), label = dlg.querySelector('.atm-label'), stage = dlg.querySelector('.atm-stage');
  let list = [], idx = 0, busy = false;
  const cursor = document.getElementById('star-cursor'), cursorHome = cursor && cursor.parentNode;

  function fill(i) {
    const it = list[i];
    const m = it.media;
    let node;
    if (m.tagName === 'VIDEO') {
      node = document.createElement('video');
      node.src = m.currentSrc || m.src; if (m.poster) node.poster = m.poster;
      node.muted = true; node.loop = true; node.playsInline = true; node.autoplay = !calm();
      node.setAttribute('aria-label', it.title || '');
    } else {
      node = document.createElement('img');
      node.src = m.currentSrc || m.src; node.alt = m.alt || it.title || '';
    }
    print.replaceChildren(node);
    label.innerHTML =
      '<p class="atm-title">' + esc(it.title) + '</p>' +
      (it.desc ? '<p class="atm-desc">' + esc(it.desc.trim()) + '</p>' : '') +
      (it.href ? '<a class="atm-cta" href="' + esc(it.href) + '">open the case study</a>' : '') +
      '<span class="atm-count">' + (i + 1) + ' / ' + list.length + '</span>';
    return node.tagName === 'IMG' && !node.complete ? new Promise(r => { node.onload = node.onerror = r; setTimeout(r, 900); }) : Promise.resolve();
  }
  const EASE = 'cubic-bezier(.2, .7, .2, 1)';
  function flipFrom(src) {
    // the print starts exactly where the piece lies on the desk, then lifts toward you
    const a = src.getBoundingClientRect(), b = print.getBoundingClientRect();
    if (!a.width || !b.width) return null;
    const s = a.width / b.width;
    const dx = (a.left + a.width / 2) - (b.left + b.width / 2), dy = (a.top + a.height / 2) - (b.top + b.height / 2);
    return `translate(${dx}px, ${dy}px) scale(${s})`;
  }
  async function open(i, fromEl, fromSec) {
    if (busy) return; busy = true;
    list = items(fromSec); idx = i;
    await fill(idx);
    if (cursor) dlg.appendChild(cursor);                  // the site's own cursor rides along into the top layer
    dlg.showModal();
    root.classList.add('atm-engaged');
    sfx('paperSheet', 1.6);
    const from = fromEl && flipFrom(fromEl);
    if (from && !calm()) {
      print.animate([{ transform: from, boxShadow: '0 1px 2px rgba(0,0,0,.3)' }, { transform: 'none' }], { duration: 560, easing: EASE });
      label.animate([{ opacity: 0, transform: 'translateY(14px)' }, { opacity: 1, transform: 'none' }], { duration: 420, delay: 260, easing: EASE, fill: 'backwards' });
    } else {
      stage.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 200 });
    }
    busy = false;
    dlg.querySelector('.atm-next').focus({ preventScroll: true });
  }
  async function go(dir) {
    if (busy || list.length < 2) return; busy = true;
    const next = (idx + dir + list.length) % list.length;
    sfx('pageTurn');
    if (!calm()) await stage.animate([{ transform: 'none', opacity: 1 }, { transform: `translateX(${-dir * 38}vw) rotate(${-dir * 7}deg)`, opacity: 0 }], { duration: 300, easing: 'cubic-bezier(.5,0,.75,0)' }).finished;
    idx = next; await fill(idx);
    if (!calm()) await stage.animate([{ transform: `translateX(${dir * 30}vw) rotate(${dir * 5}deg)`, opacity: 0 }, { transform: 'none', opacity: 1 }], { duration: 420, easing: EASE }).finished;
    busy = false;
  }
  async function close() {
    if (busy || !dlg.open) return; busy = true;
    sfx('paperSlip', 1.4);
    const it = list[idx], to = it && flipFrom(it.el);
    const vis = it && (r => r.bottom > 0 && r.top < innerHeight)(it.el.getBoundingClientRect());
    if (!calm()) {
      if (to && vis) {
        label.animate([{ opacity: 1 }, { opacity: 0 }], { duration: 160, fill: 'forwards' });
        await print.animate([{ transform: 'none' }, { transform: to }], { duration: 440, easing: EASE, fill: 'forwards' }).finished;
      } else {
        await stage.animate([{ opacity: 1, transform: 'none' }, { opacity: 0, transform: 'translateY(30px) scale(.96)' }], { duration: 260, fill: 'forwards' }).finished;
      }
    }
    dlg.close();
  }
  dlg.addEventListener('close', () => {
    print.getAnimations().forEach(a => a.cancel()); label.getAnimations().forEach(a => a.cancel()); stage.getAnimations().forEach(a => a.cancel());
    print.replaceChildren();
    if (cursor && cursorHome) cursorHome.appendChild(cursor);
    busy = false;
    const it = list[idx]; if (it && it.el.focus) it.el.focus({ preventScroll: true });
  });
  dlg.addEventListener('cancel', e => { e.preventDefault(); close(); });
  dlg.querySelector('.atm-close').addEventListener('click', close);
  dlg.querySelector('.atm-prev').addEventListener('click', () => go(-1));
  dlg.querySelector('.atm-next').addEventListener('click', () => go(1));
  dlg.addEventListener('click', e => { if (e.target === dlg) close(); });      // a click on the dimmed desk puts it back
  dlg.addEventListener('keydown', e => {
    if (e.key === 'ArrowRight') { e.preventDefault(); go(1); }
    else if (e.key === 'ArrowLeft') { e.preventDefault(); go(-1); }
  });
  let sx0 = null;
  dlg.addEventListener('pointerdown', e => { sx0 = e.clientX; });
  dlg.addEventListener('pointerup', e => { if (sx0 === null) return; const d = e.clientX - sx0; sx0 = null; if (Math.abs(d) > 60 && e.pointerType !== 'mouse') go(d < 0 ? 1 : -1); });

  // anything in the section that is artwork can be picked up. A card's link still works with a modifier
  // (new tab) and from the viewer's "open the case study".
  SECTIONS.forEach(SECTION => SECTION.addEventListener('click', e => {
    const el = e.target.closest('.lc-scene img, .lc-scene video, .lc-thumb, .grid .card-img');
    if (!el || e.metaKey || e.ctrlKey || e.shiftKey || e.button > 0) return;
    const got = items(SECTION), i = got.findIndex(it => it.el === el || it.el.contains(el));
    if (i < 0) return;
    e.preventDefault();
    open(i, got[i].media, SECTION);
  }));
  // the Sound Lab loop plays only while it is on screen, and never for reduced motion (the poster stays)
  all('.lc-scene video').forEach(v => {
    if (calm() || !('IntersectionObserver' in window)) return;
    new IntersectionObserver(es => { es[0].isIntersecting ? v.play().catch(() => {}) : v.pause(); }, { threshold: .25 }).observe(v);
  });
  all('.lc-scene img, .lc-scene video, .lc-thumb').forEach(img => {
    img.tabIndex = 0; img.setAttribute('role', 'button');
    img.setAttribute('aria-label', 'Pick up: ' + (img.alt || img.getAttribute('aria-label') || 'artwork'));
    img.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); img.click(); } });
  });

  // ---------------------------------------------------------------- 3. stamps, and the invitation
  const FACES = {
    squash: '<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><ellipse cx="20" cy="27" rx="13" ry="6.5"/><path d="M6 35h28"/><path d="M20 5v8M15 9l5 4 5-4"/></svg>',
    bounce: '<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><path d="M4 33c3-18 8-18 11 0c2-11 6-11 8 0c1.5-6 4-6 5.5 0"/><circle cx="33" cy="30" r="3.2" fill="currentColor"/><path d="M3 36h34"/></svg>',
    ease: '<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><path d="M6 33C20 33 20 7 34 7"/><circle cx="6" cy="33" r="2.4" fill="currentColor"/><circle cx="34" cy="7" r="2.4" fill="currentColor"/></svg>',
  };
  document.querySelectorAll('#pg-animation .motion-preset-btn').forEach(btn => {
    const text = btn.textContent.trim();
    btn.setAttribute('aria-label', text);
    btn.innerHTML = '<span class="hn-sp-handle" aria-hidden="true"></span><span class="hn-sp-face" aria-hidden="true">' + (FACES[btn.dataset.motion] || '') + '</span><span class="atm-lbl" aria-hidden="true">' + esc(text) + '</span>';
    btn.addEventListener('click', () => sfx('stamp', .9));
  });
})();
