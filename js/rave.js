/* CLUB GOT BOOTS: walking into a small, packed club, seen through your own eyes, cut to the song.
   Annmary's brief: you come into a party, everyone's going for it, you're a little hesitant at first,
   then the beat catches you and before you know it you're dancing. A small club, not a big one: packed,
   intimate. The song's own structure (from its baked spectrum, 117.5 BPM, bars of 2.043 s) sets the story:
     0:00  no kick, an experimental intro     outside the door: a dark corridor, the room glimpsed beyond
     0:08  the kick lands                     you step through the doorway, on the downbeat
     0:08  full groove with the melody        a low room, a DJ at the back, the crowd loose and out of step,
                                              finding the beat together; you start to bob
     0:32  the melody drops, bass and hats    everyone in step, you bounce on every beat, the lights go deep red
     1:20  the peak                           you're dancing: swaying, hands up, mirror-ball light on the walls
     1:52  the stripped outro                 one warm light, you drift back toward the door
     2:08  it stops dead                      lights out
   Drawn at low resolution into a buffer and scaled up once (soft by nature, and fast). Everything is a
   function of the song time, so scrubbing works. No flashes: kick pulses lift the lights by a fraction.
   With reduced motion the camera holds still and the crowd barely moves.
   Used by the Sound Lab (project.html, club branch) and the tape deck (js/deck.js). */
(() => {
  const BPM = 117.5, BEAT = 60 / BPM, T0 = 0.07, BAR = BEAT * 4;
  const bar = n => T0 + n * BAR;
  const IN = bar(4), GROOVE = bar(16), PEAK = bar(39), OUTRO = bar(55), END = 128.1;
  const TAU = Math.PI * 2;
  const clamp = (x, a = 0, c = 1) => Math.max(a, Math.min(c, x));
  const lerp = (a, b, k) => a + (b - a) * k;
  const seg = (t, a, b) => clamp((t - a) / (b - a));
  const eio = x => x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
  const eout = x => 1 - Math.pow(1 - x, 3);
  let seed = 41; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  const rgba = (c, a) => `rgba(${c[0] | 0},${c[1] | 0},${c[2] | 0},${a})`;
  const mixc = (p, q, k) => [lerp(p[0], q[0], k), lerp(p[1], q[1], k), lerp(p[2], q[2], k)];

  // ---- people: head-and-shoulders silhouettes, drawn once. 4 builds x arms down/up x 3 depths of haze
  const HAZE = [[30, 14, 30], [14, 7, 16], [2, 1, 4]];       // far rows take on the room's haze; near rows are black
  function person(v, arms, fill, blur) {
    const c = document.createElement('canvas'); c.width = 220; c.height = 300;
    const x = c.getContext('2d'); x.fillStyle = fill; x.strokeStyle = fill; x.lineCap = 'round';
    if (blur) x.filter = `blur(${blur}px)`;
    const cx = 110, head = [26, 24, 28, 25][v], sh = [70, 62, 76, 66][v];
    x.beginPath(); x.moveTo(cx - sh, 300); x.quadraticCurveTo(cx - sh, 150, cx - 26, 140); x.lineTo(cx + 26, 140); x.quadraticCurveTo(cx + sh, 150, cx + sh, 300); x.fill();
    x.beginPath(); x.ellipse(cx, 100, head, head * 1.18, 0, 0, TAU); x.fill();
    if (v === 1) { x.beginPath(); x.arc(cx + 4, 64, 15, 0, TAU); x.fill(); }                        // a bun
    if (v === 2) { x.beginPath(); x.ellipse(cx, 80, head * 1.25, head * .5, 0, Math.PI, TAU); x.fill(); x.fillRect(cx - 4, 76, head * 1.6, 8); }   // a cap
    if (v === 3) { x.beginPath(); x.moveTo(cx + 18, 90); x.quadraticCurveTo(cx + 40, 150, cx + 26, 185); x.lineWidth = 14; x.stroke(); }     // a ponytail
    if (arms) {
      x.lineWidth = 20;
      for (const s of [-1, 1]) { x.beginPath(); x.moveTo(cx + s * sh * .7, 170); x.quadraticCurveTo(cx + s * sh * 1.05, 90, cx + s * sh * .75, 18); x.stroke(); x.beginPath(); x.arc(cx + s * sh * .75, 16, 12, 0, TAU); x.fill(); }
    }
    return c;
  }
  const SPR = HAZE.map((h, d) => [0, 1, 2, 3].map(v => [0, 1].map(a => person(v, a, `rgb(${h})`, d === 2 ? 5 : 0))));

  // ---- the crowd: five rows, packed, from the booth to the lens
  const ROWS = [
    { z: .2, n: 14, y: .06, s: .16, haze: 0 }, { z: .32, n: 12, y: .12, s: .24, haze: 0 },
    { z: .48, n: 9, y: .22, s: .36, haze: 1 }, { z: .7, n: 7, y: .38, s: .56, haze: 1 }, { z: 1, n: 4, y: .62, s: .95, haze: 2 },
  ];
  const crowd = [];
  ROWS.forEach((r, ri) => { for (let i = 0; i < r.n; i++) crowd.push({ ri, x: (i + .5 + (rnd() - .5) * .7) / r.n * 1.5 - .75, v: (rnd() * 4) | 0,
    ph: rnd() * TAU, own: .7 + rnd() * .9, lag: rnd() * .25, hands: rnd() < .4, size: .88 + rnd() * .24 }); });
  const specks = Array.from({ length: 70 }, () => ({ a: rnd() * TAU, r: .2 + rnd() * .8, y: rnd(), s: 1 + rnd() * 1.6 }));

  const buf = document.createElement('canvas'), b = buf.getContext('2d');
  const grain = document.createElement('canvas'); grain.width = grain.height = 128;
  (() => { const x = grain.getContext('2d'), d = x.createImageData(128, 128); for (let i = 0; i < d.data.length; i += 4) { const v = rnd() * 255; d.data[i] = d.data[i + 1] = d.data[i + 2] = v; d.data[i + 3] = 255; } x.putImageData(d, 0, 0); })();

  // the lights, by section
  const LIGHT = {
    intro: [[255, 120, 60], [120, 60, 200]], A: [[255, 110, 50], [255, 60, 120]],
    B: [[230, 20, 60], [180, 20, 160]], peak: [[255, 40, 160], [60, 200, 255]], outro: [[255, 150, 70], [255, 150, 70]],
  };
  const BOOTH = [70, 255, 150];                                 // the track's green, on the DJ's lamp

  window.ClubRave = {
    /* o: { t, playing, gain, e:{sub,bass,mid,lead,hat,air}, kick, isKick, drop, tension, active, calm } */
    draw(ctx, Wd, Ht, dpr, o) {
      const R = .45, w = Math.max(2, Math.round(Wd * R)), h = Math.max(2, Math.round(Ht * R));
      if (buf.width !== w || buf.height !== h) { buf.width = w; buf.height = h; }
      const t = o.t, live = o.playing && o.gain > 0, calm = !!o.calm, e = o.e || {};
      const beatT = (t - T0) / BEAT, beatPh = ((beatT % 1) + 1) % 1, barPh = ((((t - T0) / BAR) % 1) + 1) % 1, barN = Math.floor((t - T0) / BAR);
      const kick = live ? (o.kick || 0) : 0;
      const beatDip = Math.pow(1 - beatPh, 2.2);                 // 1 on the beat, easing away
      const motion = calm ? .12 : 1;

      // where in the story we are
      const inside = seg(t, IN - .45, IN + .25);                // the step through the door
      const sync = t < IN ? 0 : lerp(.15, 1, eio(seg(t, IN, GROOVE)));   // the crowd finding the beat together
      const deep = seg(t, GROOVE - .2, GROOVE + .3), peak = seg(t, PEAK - .2, PEAK + BAR), out = seg(t, OUTRO, END - 1);
      const dead = t >= END ? 1 : 0;
      const L = t < IN ? LIGHT.intro : t < GROOVE ? LIGHT.A : t < PEAK ? LIGHT.B : t < OUTRO ? (barN % 2 ? LIGHT.peak.slice().reverse() : LIGHT.peak) : LIGHT.outro;
      const lift = live ? .75 + (e.bass || 0) * .25 + kick * .18 : .5;

      // the camera: hesitant outside, then bobbing more and more with the beat, swaying at the peak, drifting back at the end
      const you = live ? (t < IN ? 0 : lerp(.25, 1, deep) * (1 - out * .7)) * motion : 0;
      const camBob = -beatDip * .018 * you;
      const camSway = (Math.sin(t * .7) * .006 + (peak ? Math.sin(beatT * Math.PI / 2) * .03 * peak * (1 - out) : 0)) * motion;
      const camRot = (peak ? Math.sin(beatT * Math.PI / 2 + .6) * 1.6 * peak * (1 - out) : Math.sin(t * .5) * .3) * motion * Math.PI / 180;
      const nerves = t < IN ? Math.sin(t * 1.3) * .006 + Math.sin(t * 2.9) * .003 : 0;
      const zoom = (1 + deep * .04 + peak * .05 - out * .12) * lerp(.82, 1, inside) * (1 + (live ? kick * .006 : 0) * motion);

      b.setTransform(1, 0, 0, 1, 0, 0);
      b.globalCompositeOperation = 'source-over'; b.globalAlpha = 1; b.filter = 'none';
      b.fillStyle = '#050307'; b.fillRect(0, 0, w, h);
      b.save();
      b.translate(w / 2 + (camSway + nerves) * h, h * .46 + camBob * h);
      b.rotate(camRot); b.scale(zoom, zoom);
      const U = h;                                              // world units: 1 = the buffer's height

      // ---- the room: a low ceiling, a back wall with the booth, the walls close in
      const bw = 3 * U, bh = .42 * U, by = -.3 * U;              // back wall, wall to wall: a small room
      const wallG = b.createLinearGradient(0, by, 0, by + bh);
      wallG.addColorStop(0, rgba(mixc([20, 10, 16], L[0], .12), 1)); wallG.addColorStop(1, rgba(mixc([10, 6, 10], L[1], .1), 1));
      b.fillStyle = wallG; b.fillRect(-bw / 2, by, bw, bh);
      b.fillStyle = '#0a0609';                                  // ceiling and side walls, in perspective
      b.beginPath(); b.moveTo(-bw / 2, by); b.lineTo(bw / 2, by); b.lineTo(U * 1.4, -U * .9); b.lineTo(-U * 1.4, -U * .9); b.fill();
      b.fillStyle = '#07050a';
      b.beginPath(); b.moveTo(-bw / 2, by); b.lineTo(-U * 1.4, -U * .9); b.lineTo(-U * 1.4, U * 1.2); b.lineTo(-bw / 2, by + bh); b.fill();
      b.beginPath(); b.moveTo(bw / 2, by); b.lineTo(U * 1.4, -U * .9); b.lineTo(U * 1.4, U * 1.2); b.lineTo(bw / 2, by + bh); b.fill();
      // the booth: a table, the DJ, a green lamp
      const boothY = by + bh * .55, djBob = live ? beatDip * .012 * U * motion : 0;
      const lamp = b.createRadialGradient(0, boothY - .02 * U, 0, 0, boothY - .02 * U, .28 * U);
      lamp.addColorStop(0, rgba(BOOTH, .8 * lift)); lamp.addColorStop(1, rgba(BOOTH, 0));
      b.globalCompositeOperation = 'lighter'; b.fillStyle = lamp; b.fillRect(-.3 * U, boothY - .3 * U, .6 * U, .5 * U); b.globalCompositeOperation = 'source-over';
      b.drawImage(SPR[0][2][0], -.07 * U, boothY - .2 * U + djBob, .14 * U, .19 * U);
      b.fillStyle = '#0b0a0c'; b.fillRect(-.16 * U, boothY - .025 * U, .32 * U, .08 * U);
      b.fillStyle = rgba(BOOTH, .9); b.fillRect(-.02 * U, boothY - .035 * U, .04 * U, .01 * U);
      // the lights on the ceiling bar, and their cones through the haze
      b.globalCompositeOperation = 'lighter';
      const nL = 4;
      for (let i = 0; i < nL; i++) {
        const lx = (i / (nL - 1) - .5) * .7 * U, ly = by - .04 * U, col = L[i % 2];
        const swing = (t < IN ? Math.sin(t * 3 + i * 2) * .5 : Math.sin(beatT * Math.PI / 4 + i * 1.3)) * .35 * (calm ? .3 : 1);
        const tx = lx + Math.sin(swing) * .7 * U, ty = .55 * U;
        const flick = t < IN ? (Math.sin(t * 7 + i * 3) > .6 ? 1 : .35) : 1;   // the intro: lights that cannot decide
        const a = (.3 + deep * .12 + peak * .1) * lift * flick * (1 - out * .5 * (i % 2));
        const g = b.createLinearGradient(lx, ly, tx, ty);
        g.addColorStop(0, rgba(col, a)); g.addColorStop(1, rgba(col, 0));
        b.fillStyle = g; b.beginPath(); b.moveTo(lx - .01 * U, ly); b.lineTo(lx + .01 * U, ly); b.lineTo(tx + .2 * U, ty); b.lineTo(tx - .2 * U, ty); b.fill();
        b.fillStyle = rgba(col, .9 * flick); b.beginPath(); b.arc(lx, ly, .012 * U, 0, TAU); b.fill();
      }
      // mirror-ball light, sweeping the walls and ceiling at the peak
      if (peak > .01 && t < OUTRO + BAR) {
        const spin = t * .35;
        for (const s of specks) {
          const a = s.a + spin, x = Math.cos(a) * s.r * 1.2 * U, y = (s.y - .75) * .9 * U;
          b.fillStyle = rgba([255, 240, 250], .55 * peak * (1 - out)); b.fillRect(x, y, s.s * U * .004, s.s * U * .004);
        }
      }
      // haze in the light
      const hz = b.createRadialGradient(0, -.05 * U, 0, 0, -.05 * U, .9 * U);
      hz.addColorStop(0, rgba(L[0], .3 * lift)); hz.addColorStop(.6, rgba(L[1], .1 * lift)); hz.addColorStop(1, rgba(L[1], 0));
      b.fillStyle = hz; b.fillRect(-1.2 * U, -1 * U, 2.4 * U, 2 * U);
      b.globalCompositeOperation = 'source-over';

      // ---- the crowd, far to near. Each person has their own groove; `sync` pulls everyone onto the beat
      const handsUp = live ? clamp(peak * (1 - out) + (t > GROOVE && barPh > .75 && barN % 4 === 3 ? .6 : 0)) : 0;
      let row = -1;
      for (const p of crowd) {
        const r = ROWS[p.ri];
        if (p.ri !== row) {                                     // haze between the rows: every row stands against light
          row = p.ri;
          if (row > 0 && row < 4) {
            const hy = (r.y - .2) * U, hb = b.createLinearGradient(0, hy - .15 * U, 0, hy + .1 * U);
            hb.addColorStop(0, rgba(L[row % 2], 0)); hb.addColorStop(.6, rgba(L[row % 2], .09 * lift)); hb.addColorStop(1, rgba(L[row % 2], 0));
            b.globalCompositeOperation = 'lighter'; b.fillStyle = hb; b.fillRect(-1.6 * U, hy - .15 * U, 3.2 * U, .25 * U); b.globalCompositeOperation = 'source-over';
          }
        }
        const own = Math.sin(t * TAU * p.own * .5 + p.ph) * .5 + .5;
        const onBeat = Math.pow(1 - (((beatT - p.lag * (1 - sync)) % 1) + 1) % 1, 2.2);
        const groove = live ? lerp(own * .5, onBeat, sync) * (.4 + deep * .6) : own * .15;
        const bob = groove * .05 * r.s * U * motion;
        const sway = (live ? Math.sin(beatT * Math.PI / 2 + p.ph) * (.2 + peak * .8) : 0) * .03 * r.s * U * motion;
        const arms = p.hands && handsUp > .5 ? 1 : 0;
        const sz = r.s * p.size * U;
        const img = SPR[r.haze][p.v][arms];
        b.drawImage(img, p.x * U * (1 + r.z * .6) + sway - sz * .37, (r.y - .12) * U + bob - sz * .3, sz * .73, sz);
      }
      b.restore();

      // ---- the door: you are outside it until the kick lands, then you walk through it
      if (inside < 1) {
        const open = eio(inside), dw = lerp(.32, 2.6, open) * h, dh = lerp(.52, 3.4, open) * h;
        const cx = w / 2 + nerves * h, cy = h * .47;
        b.fillStyle = '#020103';
        b.beginPath(); b.rect(0, 0, w, h); b.rect(cx - dw / 2, cy - dh / 2, dw, dh); b.fill('evenodd');
        const spill = b.createLinearGradient(0, cy + dh / 2, 0, h);                // light spilling out along the corridor floor
        spill.addColorStop(0, rgba(L[0], .22 * (1 - open))); spill.addColorStop(1, rgba(L[0], 0));
        b.fillStyle = spill; b.beginPath(); b.moveTo(cx - dw / 2, cy + dh / 2); b.lineTo(cx + dw / 2, cy + dh / 2); b.lineTo(cx + dw * 1.8, h); b.lineTo(cx - dw * 1.8, h); b.fill();
        b.fillStyle = `rgba(0,0,0,${.35 * (1 - open)})`; b.fillRect(cx - dw / 2, cy - dh / 2, dw, dh);   // muffled, from out here
      }
      // grain, a vignette, and lights out when it ends
      b.globalCompositeOperation = 'overlay'; b.globalAlpha = .1;
      const gx = (Math.floor(t * 24) * 37) % 128, gy = (Math.floor(t * 24) * 71) % 128;
      for (let x = -gx; x < w; x += 128) for (let y = -gy; y < h; y += 128) b.drawImage(grain, x, y);
      b.globalAlpha = 1; b.globalCompositeOperation = 'source-over';
      const v = b.createRadialGradient(w / 2, h * .45, h * .25, w / 2, h * .45, Math.max(w, h) * .75);
      v.addColorStop(0, 'rgba(0,0,0,0)'); v.addColorStop(1, 'rgba(0,0,0,.65)');
      b.fillStyle = v; b.fillRect(0, 0, w, h);
      if (dead || (!live && t === 0)) { b.fillStyle = dead ? '#000' : 'rgba(0,0,0,.35)'; b.fillRect(0, 0, w, h); }

      ctx.save();
      ctx.imageSmoothingEnabled = true; ctx.imageSmoothingQuality = 'medium';
      ctx.globalCompositeOperation = 'copy';
      ctx.drawImage(buf, 0, 0, Wd, Ht);
      ctx.restore();
      return true;
    },

    /* the same inputs worked out straight from the baked spectrum (for the tape deck, which has no analyser) */
    fromSpectrum(t, st) {
      const S = window.TRACK_SPECTRUM && window.TRACK_SPECTRUM.club;
      if (!S) return null;
      const f = S.frames[Math.min(S.frames.length - 1, Math.max(0, Math.floor(t * S.fps)))] || [];
      const e = { air: (f[0] || 0) * 1.5, hat: (f[1] || 0) * 1.4, lead: (f[2] || 0) * 1.2, mid: (f[3] || 0) * 1.1, bass: (f[4] || 0) * 1.2, sub: (f[5] || 0) * 1.3 };
      for (const k in e) e[k] = clamp(e[k]);
      st.hist = st.hist || []; st.hist.push(e.sub); if (st.hist.length > 30) st.hist.shift();
      const avg = st.hist.reduce((a, c) => a + c, 0) / st.hist.length;
      const isKick = e.sub > avg * 1.28 + .06 && t - (st.lastKick ?? -9) > .2;
      if (isKick) st.lastKick = t;
      const kick = Math.pow(clamp(1 - (t - (st.lastKick ?? -9)) / .35), 2);
      return { e, isKick, kick, drop: false, active: 6, tension: 0 };
    },
  };
})();
