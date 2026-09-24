/* THE TAPE DECK (the Music lead). Pick a tape up off the desk: it flies into the deck,
   the reels turn, the music plays and the screen shows the picture it was made for. Eject puts it back.
   A new tape is one entry in TAPES. Room sound ducks by itself while the deck is audible (room-sound.js
   watches every playing media element). */
(() => {
  const deck = document.getElementById('tape-deck');
  if (!deck) return;
  const calm = () => matchMedia('(prefers-reduced-motion: reduce)').matches;
  const sfx = (n, k) => { try { window.__hnSfx && window.__hnSfx(n, k); } catch (e) {} };
  const T = 'assets/projects/tapes/';

  const TAPES = [
    { id: 'score', title: 'Short Film Score', side: 'A', shell: '#3a1f1c', band: '#C0502E', r: '-4deg',
      note: 'the score for a friend’s short film', href: 'project.html?id=short-film-score',
      film: T + 'score-film.mp4', poster: T + 'score-poster.webp',
      cap: 'An original score written for a friend’s short film, to carry the story without speaking over the picture. The film plays with its own soundtrack.' },
    { id: 'tracks', title: 'Original Tracks', side: 'B', shell: '#17221c', band: '#2FD27F', r: '-2deg',
      note: 'three tracks, each with a room', href: 'project.html?id=original-tracks',
      film: 'assets/portfolio-data/music_video/clubgotboots_stream.mp4', from: 90.5, poster: T + 'club-poster.webp',
      cap: 'Club Got Boots, from the Sound Lab, where each of the three tracks gets its own room. This one: a small packed club, cut to the song’s bars.' },
  ];

  const cassette = t =>
    `<div class="cas" style="--shell:${t.shell};--band:${t.band}"><div class="cas-label"></div>` +
    `<span class="cas-title">${t.title}</span><span class="cas-side">${t.side}</span>` +
    `<div class="cas-window"><span class="cas-reel"></span><span class="cas-reel is-r"></span></div>` +
    `<div class="cas-foot"></div><i></i><i></i><i></i><i></i></div>`;

  deck.querySelector('.deck-body').appendChild(deck.querySelector('.deck-tapes'));   // the tapes lie beside the player
  const shelf = deck.querySelector('.deck-tapes'), slot = deck.querySelector('.deck-slot'), vis = deck.querySelector('.deck-vis');
  const cap = deck.querySelector('.deck-cap'), nowT = deck.querySelector('.deck-now-t'), time = deck.querySelector('.deck-time');
  const bPlay = deck.querySelector('.deck-play'), bEject = deck.querySelector('.deck-eject'), cta = deck.querySelector('.deck-cta');
  const idle = vis.innerHTML;
  TAPES.forEach(t => {
    const b = document.createElement('button');
    b.type = 'button'; b.className = 'cas-btn'; b.dataset.id = t.id; b.style.setProperty('--r', t.r);
    b.setAttribute('aria-label', 'Play the ' + t.title + ' tape'); b.setAttribute('aria-pressed', 'false');
    b.innerHTML = cassette(t) + `<span class="cas-note">${t.note}</span>`;
    b.addEventListener('click', () => load(t, b));
    shelf.appendChild(b);
  });

  let cur = null, media = null, loopVid = null, busy = false;
  const fmt = s => { s = Math.max(0, Math.floor(s || 0)); return Math.floor(s / 60) + ':' + String(s % 60).padStart(2, '0'); };
  const EASE = 'cubic-bezier(.2, .7, .2, 1)';

  function fly(fromEl, toEl) {
    // the tape travels from where it lay on the desk into the deck's door
    if (calm()) return Promise.resolve();
    const a = fromEl.getBoundingClientRect(), z = toEl.getBoundingClientRect();
    const ghost = fromEl.cloneNode(true);
    Object.assign(ghost.style, { position: 'fixed', left: a.left + 'px', top: a.top + 'px', width: a.width + 'px', margin: 0, zIndex: 9000, pointerEvents: 'none' });
    document.body.appendChild(ghost);
    const s = z.width / a.width, dx = z.left - a.left, dy = z.top - a.top;
    return ghost.animate([
      { transform: 'none' },
      { transform: `translate(${dx * .5}px, ${dy * .5 - 60}px) rotate(-6deg) scale(${(1 + s) / 2})`, offset: .55 },
      { transform: `translate(${dx}px, ${dy}px) scale(${s})` },
    ], { duration: 620, easing: EASE }).finished.then(() => ghost.remove());
  }

  // ---- the rave, drawn live on the screen from the track's baked spectrum (js/rave.js, scripts/track_spectrum.js)
  let raveRaf = 0;
  const need = src => new Promise(res => { if (document.querySelector(`script[src="${src}"]`)) return res(); const s = document.createElement('script'); s.src = src; s.onload = s.onerror = res; document.body.appendChild(s); });
  async function rave() {
    const cv = document.createElement('canvas'); cv.setAttribute('aria-hidden', 'true');
    Object.assign(cv.style, { position: 'absolute', inset: '0', width: '100%', height: '100%' });
    vis.appendChild(cv);
    await need('scripts/track_spectrum.js'); await need('js/rave.js');
    const ctx = cv.getContext('2d'), st = {};
    const tick = () => {
      if (!cv.isConnected || !window.ClubRave) return;
      raveRaf = requestAnimationFrame(tick);
      const dpr = Math.min(devicePixelRatio || 1, 2), W = vis.clientWidth, H = vis.clientHeight;
      if (cv.width !== Math.round(W * dpr)) { cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr); }
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      const t = media ? media.currentTime : 0, playing = !!media && !media.paused;
      const i = window.ClubRave.fromSpectrum(t, st) || { e: { sub: 0, bass: 0, mid: 0, lead: 0, hat: 0, air: 0 }, active: 0 };
      window.ClubRave.draw(ctx, W, H, dpr, Object.assign(i, { t, playing, gain: 1, calm: calm() }));
    };
    tick();
  }

  function stopMedia() {
    cancelAnimationFrame(raveRaf);
    [media, loopVid].forEach(m => { if (m) { m.pause(); m.removeAttribute('src'); m.load(); } });
    media = loopVid = null;
  }

  async function load(t, btn) {
    if (busy) return;
    if (cur && cur.t === t) { toggle(); return; }
    busy = true;
    if (cur) await eject(true);
    sfx('paperGrab');
    btn.classList.add('is-out'); btn.setAttribute('aria-pressed', 'true');
    await fly(btn.querySelector('.cas'), slot);
    slot.innerHTML = cassette(t);
    sfx('stamp', .7);                                         // the clunk of the door
    cur = { t, btn };
    nowT.textContent = t.title; cap.textContent = t.cap;
    cta.href = t.href; bPlay.disabled = bEject.disabled = false;

    vis.innerHTML = '';
    if (t.film) {
      media = document.createElement('video');
      Object.assign(media, { src: t.film, playsInline: true, controls: false, preload: 'auto' }); if (t.poster) media.poster = t.poster;
      media.setAttribute('aria-label', t.title + ': the film with its score');
      vis.appendChild(media);
    } else {
      media = new Audio(t.audio); media.preload = 'auto';
      if (t.rave) rave();
      if (t.loop) {
        loopVid = document.createElement('video');
        Object.assign(loopVid, { src: t.loop, muted: true, loop: true, playsInline: true, autoplay: !calm() });
        loopVid.setAttribute('aria-hidden', 'true');
        vis.appendChild(loopVid);
      }
    }
    if (t.from) media.addEventListener('loadedmetadata', e => { e.target.currentTime = t.from; }, { once: true });
    media.addEventListener('timeupdate', e => { time.textContent = fmt(e.target.currentTime - (cur && cur.t.from || 0)); });
    media.addEventListener('ended', () => deck.classList.remove('is-playing'));
    media.addEventListener('play', () => deck.classList.add('is-playing'));
    media.addEventListener('pause', () => deck.classList.remove('is-playing'));
    busy = false;
    media.play().catch(() => {});
  }
  function toggle() {
    if (!media) return;
    sfx('stamp', .4);
    media.paused ? media.play().catch(() => {}) : media.pause();
  }
  async function eject(quiet) {
    if (!cur) return;
    const { btn } = cur;
    stopMedia(); deck.classList.remove('is-playing');
    if (!quiet) sfx('paperSlip', 1.2);
    const tape = slot.querySelector('.cas');
    if (tape) await fly(tape, btn.querySelector('.cas'));
    slot.innerHTML = '';
    btn.classList.remove('is-out'); btn.setAttribute('aria-pressed', 'false');
    cur = null;
    nowT.textContent = 'no tape in'; time.textContent = '0:00'; cap.textContent = '';
    bPlay.disabled = bEject.disabled = true;
    vis.innerHTML = idle;
  }
  window.__tapeDeck = { seek: t => { if (media) media.currentTime = t; }, time: () => media && media.currentTime };   // (for testing)
  bPlay.addEventListener('click', toggle);
  bEject.addEventListener('click', () => { if (!busy) eject(false); });
  // leaving the section stops the tape (the page should never keep playing out of sight)
  if ('IntersectionObserver' in window) new IntersectionObserver(es => { if (!es[0].isIntersecting && media && !media.paused) media.pause(); }, { threshold: 0 }).observe(deck);
})();
