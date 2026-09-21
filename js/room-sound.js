/* The room sound engine, shared by portfolio.html and project.html (it used to live inline in portfolio.html).
   Loaded with <script src="js/room-sound.js" defer>. Needs a button with id="soundBtn" (icons .snd-off / .snd-on and an optional .snd-meter). */
(function () {
  // ================================================================
  // ROOM SOUND -- opt-in, separate from everything else.
  // Off by default. Never autoplays: nothing is even created until a user gesture. Night = quiet room tone with
  // faint rain on glass; day = soft room tone with distant birds; both seamless loops (AudioBufferSource,
  // loop = true, so no gap). Small UI sounds: a lamp click on the switch and a very quiet, throttled paper
  // rustle when a taped item is hovered. Loops crossfade over 800ms when the mode changes.
  // The audio files are supplied separately in public/audio/ (see README.txt there); nothing is synthesised.
  // If a file is missing the system stays quiet and says so; if storage is blocked it just does not persist.
  // Levels read the --snd-* CSS variables, like every other level in the lighting system.
  // ================================================================
  (function initRoomSound() {
    const btn = document.getElementById('soundBtn');
    if (!btn) return;
    const root = document.documentElement;
    const BASE = 'public/audio/';
    const EXTS = ['mp3', 'ogg'];                                         // first one that exists wins
    const say = (...a) => { try { console.info('[room sound]', ...a); } catch (e) {} };
    const warn = (...a) => { try { console.warn('[room sound]', ...a); } catch (e) {} };
    const FILES = { night: 'night-music', day: 'day-music', rain: 'rain-loop', click: 'lamp-click', drawerOpen: 'drawer-open', drawerClose: 'drawer-close' };
    // SOUND SLOTS: one per kind of thing that can make a sound. A slot plays public/audio/<own>-1.mp3, -2, -3, -4
    // (any that exist, random, never the same twice in a row). Until a slot has its own file it borrows the generic
    // fallback recordings (paper-1/2/3 for the three paper slots), and a slot with neither stays silent. So
    // adding a better sound for one kind is just dropping <own>-1.mp3 (and -2, -3 for variety) into public/audio/.
    const GENERIC_PAPER = ['paper-1', 'paper-2', 'paper-3'];
    const SLOTS = {
      paperPrint:  { own: 'paper-print',  fall: GENERIC_PAPER },   // a photo print or a card
      paperSheet:  { own: 'paper-sheet',  fall: GENERIC_PAPER },   // a big sheet or the notebook page
      paperSlip:   { own: 'paper-slip',   fall: GENERIC_PAPER },   // a torn slip, a sticky note, a taped scrap
      tape:        { own: 'tape',         fall: [] },              // tape peeled or pressed
      stamp:       { own: 'stamp',        fall: [] },              // a rubber stamp landing (a reward)
      stickerPeel: { own: 'sticker-peel', fall: [] },
      stickerPlace:{ own: 'sticker-place', fall: [] },
      reward:      { own: 'reward',       fall: [] },              // a small chime
      rewardFinal: { own: 'reward-final', fall: [] },              // the last stamp
      drawerOpen:  { own: 'drawer-open',  fall: [] },
      drawerClose: { own: 'drawer-close', fall: [] },
      pageTurn:    { own: 'page-turn',    fall: GENERIC_PAPER },   // turning the notebook's page
      toyBounce:   { own: 'toy-bounce',   fall: [] },              // Animate: a principle played on the ball
      toyClap:     { own: 'toy-clap',     fall: [] },              // Capture: the clapper
      toyDraw:     { own: 'toy-draw',     fall: [] },              // Draw: the pen starting a stroke
      drawerStrip: { own: 'drawer-strip', fall: [] }               // the paper strips in the open drawer: a soft thump
    };
    const NOW_PLAYING = { day: 'Jazz Rainy Lounge, Alex Morgan', night: '2 AM Lofi Chill, Music For Videos' };   // credit, shown in the button's tooltip
    const FADE = 0.8;                                                    // seconds
    let ctx = null, master = null, an = null, on = false, armed = false, loop = null, rain = null, loopMode = null, meterT = 0, silent = 0, lastErr = '';
    const bufs = {}, missing = {};
    // ---- one visit, several pages: if the sound was on when the visitor went to a project page (or back), it carries on there, from where
    // the music was. It is remembered for this tab only (sessionStorage), so a fresh visit is still opt-in. Browsers only allow sound after a
    // touch on the site; when the new page cannot start it by itself, the button shows as pressed and the next touch starts it.
    const SK = 'hn-snd';
    { const st = document.createElement('style'); st.textContent = '#soundBtn.is-armed{animation:hnSndWait 1.6s ease-in-out infinite}@keyframes hnSndWait{50%{scale:1.16}}@media (prefers-reduced-motion:reduce){#soundBtn.is-armed{animation:none}}'; document.head.appendChild(st); }
    let resumePos = 0, loopT0 = 0, loopOff = 0, loopDur = 0;
    const remember = v => { try { if (v) sessionStorage.setItem(SK, JSON.stringify({ m: mode() })); else sessionStorage.removeItem(SK); } catch (e) {} };
    function savePos() {
      try { if (!on || !loop || !ctx || !loopDur) return; sessionStorage.setItem(SK, JSON.stringify({ m: loopMode, p: (loopOff + ctx.currentTime - loopT0) % loopDur })); } catch (e) {}
    }

    const num = (name, fallback) => { const v = parseFloat(getComputedStyle(root).getPropertyValue(name)); return isNaN(v) ? fallback : v; };
    const mode = () => root.getAttribute('data-theme') === 'dark' ? 'night' : 'day';

    function paint(note) {
      const pressed = on || armed;
      btn.setAttribute('aria-pressed', pressed ? 'true' : 'false');
      const playing = on && loop ? 'now playing: ' + NOW_PLAYING[loopMode] : '';
      const msg = note || playing;
      btn.setAttribute('aria-label', msg ? 'Room sound (' + msg + ')' : 'Room sound');
      btn.title = msg ? 'Room sound: ' + msg : 'Room sound';
      btn.classList.toggle('is-on', pressed);
      btn.classList.toggle('is-armed', armed && !on);                      // waiting for the first tap (a phone will not start sound by itself)
    }
    function ensureCtx() {
      if (ctx) return ctx;
      const AC = window.AudioContext || window.webkitAudioContext;
      if (!AC) return null;
      ctx = new AC(); master = ctx.createGain(); master.gain.value = 1;
      const lim = ctx.createDynamicsCompressor();                          // a soft limiter: overlapping sounds never jump out
      lim.threshold.value = -16; lim.knee.value = 14; lim.ratio.value = 6; lim.attack.value = 0.003; lim.release.value = 0.2;
      master.connect(lim); lim.connect(ctx.destination);
      an = ctx.createAnalyser(); an.fftSize = 1024; master.connect(an);     // only listens; feeds the little meter on the button
      say('audio context created, state:', ctx.state, ', sample rate:', ctx.sampleRate);
      return ctx;
    }
    async function load(key, quiet) {
      if (bufs[key]) return bufs[key];
      if (missing[key] || !ctx) return null;
      const base = FILES[key] || key;
      for (const ext of (quiet ? ['mp3'] : EXTS)) {
        const url = BASE + base + '.' + ext;
        try {
          const r = await fetch(url);
          if (!r.ok) { if (!quiet) { lastErr = base + ' returned ' + r.status; warn(url, 'returned HTTP', r.status, '(is the public/ folder being served?)'); } continue; }
          const ab = await r.arrayBuffer();
          bufs[key] = await new Promise((res, rej) => ctx.decodeAudioData(ab, res, rej));
          say('loaded', url, '-', Math.round(bufs[key].duration) + 's,', bufs[key].numberOfChannels + ' channels');
          return bufs[key];
        } catch (e) { if (!quiet) { lastErr = base + ' could not be loaded'; warn('could not load or decode', url, e && (e.message || e)); } }
      }
      missing[key] = true;
      return null;
    }
    function fadeOut(l) {
      if (!l) return;
      const t = ctx.currentTime;
      l.g.gain.cancelScheduledValues(t); l.g.gain.setValueAtTime(l.g.gain.value, t); l.g.gain.linearRampToValueAtTime(0, t + FADE);
      setTimeout(() => { try { l.src.stop(); } catch (e) {} l.src.disconnect(); l.g.disconnect(); }, FADE * 1000 + 100);
    }
    async function startLoop(m) {
      if (!on || !ctx) return true;
      const b = await load(m);
      if (!on) return true;
      if (!b) { fadeOut(loop); loop = null; loopMode = null; return false; }     // no file for this mode: stay quiet
      if (loop && loopMode === m) return true;
      fadeOut(loop);
      const src = ctx.createBufferSource(); src.buffer = b; src.loop = true;
      const g = ctx.createGain(); g.gain.value = 0; src.connect(g); g.connect(master);
      const off = resumePos && b.duration ? resumePos % b.duration : 0; resumePos = 0;   // coming from another page: carry on where the music was
      src.start(0, off); loopT0 = ctx.currentTime; loopOff = off; loopDur = b.duration;
      ducked = anyAudible();                                             // a video with sound is playing: come in silent
      const target = ducked ? 0 : num('--snd-loop', .6);
      g.gain.linearRampToValueAtTime(target, ctx.currentTime + FADE);
      say('playing', m, 'loop at gain', target, ', context state:', ctx.state);
      silent = 0; loop = { src, g }; loopMode = m; paint();
      return true;
    }
    // ---- rain on the window: a second, quiet loop under the music (a little at day, more at night). It follows the same rules as the
    // music: opt-in, fades in and out, and steps aside while a video with sound plays. If the file is missing it is simply absent.
    const rainLevel = () => ducked ? 0 : num('--snd-rain', .1);
    async function startRain() {
      if (!on || !ctx) return;
      const b = await load('rain', true); if (!b || !on) return;
      const t = ctx.currentTime;
      if (rain) { rain.g.gain.cancelScheduledValues(t); rain.g.gain.setValueAtTime(rain.g.gain.value, t); rain.g.gain.linearRampToValueAtTime(rainLevel(), t + FADE * 1.5); return; }
      const src = ctx.createBufferSource(); src.buffer = b; src.loop = true;
      const g = ctx.createGain(); g.gain.value = 0; src.connect(g); g.connect(master); src.start(0);
      g.gain.linearRampToValueAtTime(rainLevel(), t + FADE * 2); rain = { src, g };
    }
    async function turnOn() {
      if (!ensureCtx()) { paint('not supported in this browser'); return; }
      try { await ctx.resume(); } catch (e) { warn('resume() failed', e && e.message); }
      on = true; armed = false; paint(); startMeter();
      const ok = await startLoop(mode());
      if (ok) { startRain(); remember(true); }
      preloadAll();
      if (!ok) {                                                                    // nothing to play: say why, stay off
        on = false; stopMeter(); paint(lastErr ? "couldn't start: " + lastErr : 'sound files have not been added yet');
      }
    }
    function turnOff() {
      on = false; armed = false; stopMeter(); paint(); remember(false);
      if (ctx) { fadeOut(loop); fadeOut(rain); } loop = null; rain = null; loopMode = null;
    }
    // The meter: three bars on the button that move with the REAL signal at the output stage. If they move but you
    // hear nothing, the page is playing and the problem is outside it (tab or window muted, wrong output device,
    // system volume). If they stay flat while it claims to play, the page says so in the console and the tooltip.
    const mbuf = new Float32Array(1024);
    function meter() {
      if (!on || !ctx || !an || document.hidden) return;
      an.getFloatTimeDomainData(mbuf);
      let sum = 0; for (let i = 0; i < mbuf.length; i++) sum += mbuf[i] * mbuf[i];
      const rms = Math.sqrt(sum / mbuf.length), db = rms > 1e-7 ? 20 * Math.log10(rms) : -100;
      btn.style.setProperty('--lvl', Math.max(0, Math.min(1, (db + 55) / 43)).toFixed(2));
      if (loop && ctx.state === 'running' && db < -80) {
        if (++silent === 40) { warn('the music is "playing" but the output is silent; context state:', ctx.state); paint('playing, but no signal reaches the output'); }
      } else silent = 0;
    }
    function startMeter() { if (!meterT) meterT = setInterval(meter, 100); }
    function stopMeter() { clearInterval(meterT); meterT = 0; btn.style.setProperty('--lvl', '0'); }
    btn.addEventListener('click', () => { (on || armed) ? turnOff() : turnOn(); });
    // safety net: some browsers and embedded panes suspend audio behind our back; any touch of the page brings it back
    ['pointerdown', 'touchend', 'click'].forEach(ev => document.addEventListener(ev, () => { if (on && ctx && ctx.state !== 'running') { say('context was', ctx.state, '- resuming'); ctx.resume().catch(() => {}); } }, true));

    // Sound is opt-in for every VISIT: a new tab or a new day starts silent. Within one tab, if it was on, it carries over to the next page
    // (portfolio to a project and back), see resumeFromSession below. A plain reload of the same page does the same, on purpose.

    // the loop follows the mode (crossfade); day and night each have their own room
    new MutationObserver(() => { if (on && ctx) { startLoop(mode()).then(ok => paint(ok ? '' : 'no sound file for this mode yet')); startRain(); } }).observe(root, { attributes: true, attributeFilter: ['data-theme'] });
    let hideT = 0;
    document.addEventListener('visibilitychange', () => {
      if (!ctx) return;
      clearTimeout(hideT);
      if (document.hidden) hideT = setTimeout(() => { if (document.hidden && on) ctx.suspend(); }, 5000);   // a tab left alone for 5s stops playing
      else if (on) ctx.resume();
    });

    const slotFiles = {};
    let lastPick = '';
    // ---- effects: everything is decoded ahead of time (as soon as sound is on), so a press plays at once, never after a
    // fetch. Each kind has its own trim so nothing jumps out over the music, and a fast second press cuts the first
    // one short instead of stacking on it.
    const SLOT_VOL = { paperPrint: .6, paperSheet: .6, paperSlip: .6, pageTurn: .8, tape: .7, stamp: .8, stickerPeel: .6, stickerPlace: .8,
      reward: .45, rewardFinal: .55, drawerOpen: .7, drawerClose: .7, toyBounce: .45, toyClap: .7, toyDraw: .55, drawerStrip: .7, click: .8 };
    const voices = {};
    async function discover(name) {                                       // find and decode every file of one slot
      const sl = SLOTS[name];
      if (!sl) { await load(name, true); return; }
      if (slotFiles[name]) return;
      const found = [];
      for (let i = 1; i <= 4; i++) { const k = sl.own + '-' + i; if (await load(k, true)) found.push(k); else break; }
      if (!found.length && await load(sl.own, true)) found.push(sl.own);
      const list = found.length ? found : sl.fall.slice();
      for (const k of list) await load(k, true);
      slotFiles[name] = list;
    }
    let preloading = false;
    async function preloadAll() {
      if (preloading) return; preloading = true;
      for (const n of Object.keys(SLOTS).concat('click')) { if (!on) break; try { await discover(n); } catch (e) {} }
      for (const k of Object.keys(SCRIB)) { if (!on) break; try { await scribbleReady(k); } catch (e) {} }
    }
    function pickSync(name) {                                             // a buffer key, null (nothing to play) or undefined (not decoded yet)
      if (!SLOTS[name]) return bufs[name] ? name : undefined;
      const list = slotFiles[name]; if (!list) return undefined;
      if (!list.length) return null;
      const pool = list.filter(k => k !== lastPick);
      const k = (pool.length ? pool : list)[Math.floor(Math.random() * (pool.length || list.length))];
      return bufs[k] ? k : undefined;
    }
    function play(key, name, vol) {
      lastPick = key;
      const t = ctx.currentTime, s = ctx.createBufferSource(); s.buffer = bufs[key];
      s.playbackRate.value = 0.96 + Math.random() * 0.08;                 // a hair of variation, so repeats do not sound like one sample
      const g = ctx.createGain(); g.gain.value = vol * (SLOT_VOL[name] || 1) * (0.9 + Math.random() * 0.2);
      s.connect(g); g.connect(master);
      const prev = voices[name];
      if (prev) { try { prev.g.gain.cancelScheduledValues(t); prev.g.gain.setValueAtTime(prev.g.gain.value, t); prev.g.gain.linearRampToValueAtTime(0, t + 0.04); prev.s.stop(t + 0.05); } catch (e) {} }
      voices[name] = { s, g };
      s.onended = () => { if (voices[name] && voices[name].s === s) delete voices[name]; try { g.disconnect(); } catch (e) {} };
      s.start(t);
    }
    async function once(name, vol) {
      if (!on || !ctx || ctx.state !== 'running' || ducked) return;
      let key = pickSync(name);
      if (key === undefined) { await discover(name); if (!on || !ctx) return; key = pickSync(name); }   // only if a press beats the preload
      if (key) play(key, name, vol);
    }
    // ---- a video with sound wins: while any video or audio element on the page is playing with its sound on (the reel, once its
    // Sound button is pressed), the room music fades out and the little effects stay quiet. When it is muted, paused or ends, the
    // music fades back in. The autoplaying background loops are muted, so they never trigger it.
    let ducked = false;
    const anyAudible = () => [...document.querySelectorAll('video, audio')].some(m => !m.paused && !m.ended && !m.muted && m.volume > 0);
    function syncDuck() {
      const want = anyAudible(); if (want === ducked) return; ducked = want;
      if (loop && ctx) { const t = ctx.currentTime; loop.g.gain.cancelScheduledValues(t); loop.g.gain.setValueAtTime(loop.g.gain.value, t); loop.g.gain.linearRampToValueAtTime(ducked ? 0 : num('--snd-loop', .6), t + 0.5); }
      if (rain && ctx) { const t = ctx.currentTime; rain.g.gain.cancelScheduledValues(t); rain.g.gain.setValueAtTime(rain.g.gain.value, t); rain.g.gain.linearRampToValueAtTime(rainLevel(), t + 0.5); }
      paint(ducked ? 'paused while a video with sound plays' : '');
    }
    ['play', 'playing', 'pause', 'ended', 'volumechange', 'emptied'].forEach(ev => document.addEventListener(ev, syncDuck, true));   // media events do not bubble, but they can be caught on the way down
    window.__hnRoom = { loopGain: () => (loop && ctx ? +loop.g.gain.value.toFixed(3) : null), rainGain: () => (rain && ctx ? +rain.g.gain.value.toFixed(3) : null), ducked: () => ducked };   // (for testing)
    window.__hnLampClick = () => once('click', num('--snd-ui', .3));
    // ---- scribbling: a pencil or a marker on the page sounds for exactly as long as the hand moves. Each kind is one short steady cut
    // (public/audio/scribble-pencil.mp3, scribble-marker.mp3) turned into a seamless loop here (its tail is crossfaded into its head),
    // played while the stroke lasts. The level and the pitch follow the speed of the pointer, so a slow careful line is quiet and a quick
    // one rasps; a hand held still is silent. window.__hnScribble.start('pencil'|'marker') on press, .move(pxPerMs) on every move, .end() on release.
    const SCRIB = { pencil: { file: 'scribble-pencil', vol: .5 }, marker: { file: 'scribble-marker', vol: .7 } };
    const scribBuf = {};
    let scrib = null;
    function seamless(b, xfSec) {                                        // a copy of b whose end runs straight back into its start
      const n = b.length, xf = Math.min(Math.floor(xfSec * b.sampleRate), Math.floor(n / 3)), len = n - xf, out = ctx.createBuffer(b.numberOfChannels, len, b.sampleRate);
      for (let c = 0; c < b.numberOfChannels; c++) {
        const s = b.getChannelData(c), d = out.getChannelData(c);
        for (let i = 0; i < len; i++) d[i] = s[i];
        for (let i = 0; i < xf; i++) { const a = (i / xf) * Math.PI / 2; d[i] = s[i] * Math.sin(a) + s[len + i] * Math.cos(a); }   // equal-power crossfade
      }
      return out;
    }
    async function scribbleReady(kind) {
      if (scribBuf[kind] || !SCRIB[kind]) return scribBuf[kind] || null;
      const b = await load(SCRIB[kind].file, true); if (b && !scribBuf[kind]) scribBuf[kind] = seamless(b, 0.18);
      return scribBuf[kind] || null;
    }
    function scribEnd() {
      const v = scrib; if (!v) return; scrib = null; clearInterval(v.t);
      const t = ctx.currentTime;
      try { v.g.gain.cancelScheduledValues(t); v.g.gain.setValueAtTime(v.g.gain.value, t); v.g.gain.linearRampToValueAtTime(0, t + 0.07); v.s.stop(t + 0.09); } catch (e) {}
      setTimeout(() => { try { v.g.disconnect(); } catch (e) {} }, 200);
    }
    window.__hnScribble = {
      start(kind) {
        scribEnd();
        if (!on || !ctx || ctx.state !== 'running' || ducked || !SCRIB[kind]) return;
        const b = scribBuf[kind]; if (!b) { scribbleReady(kind); return; }         // (first ever stroke before it decoded: the next one sounds)
        const s = ctx.createBufferSource(); s.buffer = b; s.loop = true;
        const g = ctx.createGain(); g.gain.value = 0; s.connect(g); g.connect(master);
        s.start(0, Math.random() * b.duration);
        const v = scrib = { s, g, kind, at: performance.now() };
        v.t = setInterval(() => { if (scrib !== v) return; const idle = performance.now() - v.at; if (idle > 4000) return scribEnd(); if (idle > 90) g.gain.setTargetAtTime(0, ctx.currentTime, 0.05); }, 60);
      },
      move(speed) {
        const v = scrib; if (!v || !ctx) return; v.at = performance.now();
        const k = Math.max(0, Math.min(1, speed / 1.4)), t = ctx.currentTime;
        v.g.gain.setTargetAtTime(speed < 0.02 ? 0 : SCRIB[v.kind].vol * (0.3 + 0.7 * k), t, 0.03);
        v.s.playbackRate.setTargetAtTime(0.9 + 0.22 * k, t, 0.05);
      },
      end() { scribEnd(); }
    };
    // the page's foley, for anything else to call by slot name (silent unless room sound is on)
    window.__hnSfx = (name, k) => once(name, (/^(paper|page)/.test(name) ? num('--snd-rustle', .13) : num('--snd-ui', .3)) * (k || 1));
    // Project cards and the paper strips in the open drawer answer the hand: a soft thump every time the pointer comes onto one (not once
    // per card: leave and come back and it sounds again, and sweeping across a row sounds each card in turn), and a heavier one the
    // moment one is pressed, on any pointer, with a short buzz on phones that have it. Everything is already decoded, so it plays at
    // once, cutting whatever was still sounding. The only guard is a 45 ms gap so one crossing cannot double-fire. Louder than the
    // other foley on purpose (2x on hover, 3x on press), so it can be felt. Only these cards; the other sheets stay quiet.
    const HOVER = [['.desk .grid .card', 'drawerStrip'], ['#downloads .dl-btn', 'drawerStrip']];
    let lastHover = 0;
    HOVER.forEach(([sel, slot]) => document.querySelectorAll(sel).forEach(el => {
      el.addEventListener('pointerenter', e => {
        if (e.pointerType !== 'mouse') return;
        const now = performance.now();
        if (now - lastHover < 45) return;
        lastHover = now; window.__hnSfx(slot, 2);
      });
      el.addEventListener('pointerdown', e => {
        if (e.button > 0) return;
        window.__hnSfx(slot, 3); lastHover = performance.now();
        if (e.pointerType === 'touch' && navigator.vibrate) { try { navigator.vibrate(9); } catch (x) {} }
      });
    }));
    // carrying the sound from page to page (see the note at the top): remember the spot when leaving, and pick it up when arriving
    addEventListener('pagehide', savePos);
    document.addEventListener('visibilitychange', () => { if (document.hidden) savePos(); });
    async function resumeFromSession() {
      let s = null; try { s = JSON.parse(sessionStorage.getItem(SK) || 'null'); } catch (e) {}
      if (!s || on || armed) return;
      if (s.m === mode() && s.p) resumePos = s.p;
      if (!ensureCtx()) return;
      ctx.resume().catch(() => {});                                       // without a touch on this page the promise may never settle: do not wait for it
      await new Promise(r => setTimeout(r, 250));
      if (ctx.state === 'running') { turnOn(); return; }
      armed = true; paint('on: it starts with your next touch');
      // Only a real tap or key press counts as permission to make sound (on an iPhone a mere pointerdown does not), so wait for those, and
      // only stop waiting once the audio really is running. A scroll is not a tap: the button pulses until the first one.
      const evs = ['touchend', 'pointerup', 'click', 'keydown'];
      const stop = () => evs.forEach(x => document.removeEventListener(x, go, true));
      const go = e => {
        if (!armed) { stop(); return; }
        if (btn.contains(e.target)) return;                                  // the button itself turns it off
        ctx.resume().then(() => { if (armed && ctx.state === 'running') { stop(); turnOn(); } }).catch(() => {});
      };
      evs.forEach(x => document.addEventListener(x, go, true));
    }
    resumeFromSession();
    // the About drawer (the badge that opens "Studio Desk"): a drawer sound as it opens and closes
    const bp = document.querySelector('.bp-badge--toggle');
    if (bp) bp.addEventListener('click', () => setTimeout(() => window.__hnSfx(bp.getAttribute('aria-expanded') === 'true' ? 'drawerOpen' : 'drawerClose'), 0));
  })();
})();
