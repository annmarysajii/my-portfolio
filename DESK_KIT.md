# Desk Kit — design direction for portfolio.html

The single source of truth for the site's visual metaphor and its shared physical
components. Read this before any visual, motion, or layout work on `portfolio.html`.

A rendered version of every component below — real CSS, no images — lives at
`desk-kit.html` in this repo. Open it in a browser to see the parts.

---

## 1. The rule

> **Work lies flat. The person is in a drawer.**

That one line decides where anything new belongs. Professional output is laid out
on the desk with nothing hidden. Anything personal about Annmary is behind
something the visitor has to pull open.

## 2. Four metaphors, one job each

The site was running a book, a drawer and a desk simultaneously with no rule about
which meant what, which is why it read as "a lot of nice paper" instead of one place.
Each metaphor now has exactly one job:

| Metaphor | Job | Notes |
|---|---|---|
| **Desk / cutting mat** | The place | Always underneath. Never interactive. |
| **Sheets of paper** | The work | Flat, public, scrolled down through. |
| **Drawers** | The person | All 7 click-to-reveal facts are drawers. |
| **Stamps** | The visitor's trace | Opening a drawer is what earns a stamp. |

## 3. The arc

1. **Hero** — her book is open on the desk. You arrive at a surface mid-use.
2. **Quick look** — a drawer slides out. First pull; it teaches the gesture.
3. **The five sections** — down through the stack of work, one sheet per discipline.
4. **About** — you reach the desk itself, its drawers, and the person.
5. **Contact** — a note taped on top, addressed to you.

This arc is already latent in the build (light paper → dark physical board → note).
It has simply never been named, so nothing reinforced it.

---

## 4. The parts

Parts are referenced by code. When implementing, reuse the part — never write a
one-off. The reason this document exists is that tape was implemented **nine
separate times** (`.hero-tape-top`, `.hero-tape-bottom`, `.about-tape-tl`,
`.about-tape-tr`, `.notebook-tape-tl` ×2, `.notebook-tape-tr` ×2, `.polaroid-tape`,
`.notes-pin-tape` ×2, `.scrap-tape-corner`) before anyone noticed.

### SRF — Surface

| Code | Part | Used by |
|---|---|---|
| SRF-01 | Self-healing cutting mat | Page ground, sitewide |
| SRF-02 | Loose cream sheet | Every `.sec` |
| SRF-03 | Desk timber | About only |

```css
/* SRF-01 — the mat, on body. Theme-aware via tokens. */
:root {
  --mat: #B7C5BE;
  --mat-rule: rgba(20, 34, 28, .17);
  --mat-rule-fine: rgba(20, 34, 28, .07);
  --mat-guide: rgba(20, 34, 28, .10);
}
[data-theme="dark"] {
  --mat: #101B16;
  --mat-rule: rgba(126, 214, 180, .17);
  --mat-rule-fine: rgba(126, 214, 180, .07);
  --mat-guide: rgba(126, 214, 180, .12);
}
body {
  background-color: var(--mat);
  background-image:
    repeating-linear-gradient(0deg,  var(--mat-rule) 0 1px, transparent 1px 48px),
    repeating-linear-gradient(90deg, var(--mat-rule) 0 1px, transparent 1px 48px),
    repeating-linear-gradient(0deg,  var(--mat-rule-fine) 0 1px, transparent 1px 12px),
    repeating-linear-gradient(90deg, var(--mat-rule-fine) 0 1px, transparent 1px 12px);
}
```

The mat sits **behind** the sections. The five `--sec-*-bg` paper colours are
unchanged — sections become bounded sheets resting on the mat, not full-bleed bands.

### FST — Fastener

One component, four variants. Replaces all nine legacy tape classes.

```css
/* FST-01 strip / FST-02 corner */
.tape {
  --tape-color: var(--gold);
  --tape-angle: -6deg;
  --tape-w: 116px;
  --tape-h: 32px;
  width: var(--tape-w);
  height: var(--tape-h);
  background:
    repeating-linear-gradient(90deg, rgba(255,255,255,.22) 0 5px, transparent 5px 11px),
    var(--tape-color);
  opacity: .93;
  transform: rotate(var(--tape-angle));
  /* torn short ends — never square */
  clip-path: polygon(2% 4%, 26% 0, 61% 3%, 98% 0, 100% 34%, 97% 70%,
                     99% 100%, 66% 96%, 31% 100%, 3% 97%, 0 62%, 2% 30%);
  box-shadow: 0 1px 2px rgba(16,28,22,.22);
}
.tape--corner { --tape-angle: -45deg; --tape-w: 62px; --tape-h: 22px; }
```

FST-03 is a paper clip (inline SVG, hangs off a top edge), FST-04 a push pin
(radial-gradient circle) — both in `desk-kit.html`.

### CNT — Container

What content is printed on. A work card is never "just a card" — it is one of these,
chosen per section.

| Code | Part |
|---|---|
| CNT-01 | Index card (red header rule, blue feint) |
| CNT-02 | Instant print (deep bottom margin) |
| CNT-03 | Punched leaf (holes at 25px pitch, ruled) |
| CNT-04 | Sticker sheet (die-cut kiss line) |

### MRK — Marker

The layer that says a person touched this. Reward marks for exploring belong
here — not in a new system.

| Code | Part |
|---|---|
| MRK-01 | Rubber stamp (−8°, mottled ink mask) |
| MRK-02 | Die-cut sticker (4px kiss border) |
| MRK-03 | Sticky flag |
| MRK-04 | Marker note — the existing handwritten asides |

### EDG — Edge

How one sheet meets the next. Sections should not *start*; they should **overlap**.

| Code | Part |
|---|---|
| EDG-01 | Torn edge — the next sheet slides under it |
| EDG-02 | Drawer front — already built on the quick-look block |
| EDG-03 | Index tab — replaces the deleted 01–05 numerals |

```css
/* EDG-02 — the drawer. One gesture for all 7 personal reveals. */
.drawer {
  --drawer-color: var(--gold);
  overflow: hidden;
}
.drawer-front {           /* visible closed state: this is what says "pull me" */
  background: linear-gradient(#1D3E7A, #16305E);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.22), inset 0 -2px 4px rgba(0,0,0,.3);
}
.drawer-pull {
  width: 44px; height: 8px; border-radius: 5px;
  background: linear-gradient(var(--drawer-color), #C98A0C);
}
```

Reveal motion: content **slides out** rather than fading — slow start, quick settle,
using the site's existing `cubic-bezier(.34,1.56,.64,1)` for the settle. Same gesture
in all seven places.

---

## 5. Section assignments

| Section | Object | Status | Parts |
|---|---|---|---|
| Hero | Open book on the mat | built | SRF-01, FST-01 |
| Quick look | Drawer pulled open | built | EDG-02 |
| Animation | Peg-bar layout sheets | **new** | CNT-03, FST-03 |
| Illustration | Sketchbook spread | **new** | CNT-03, CNT-04 |
| Videography | Contact sheet | **new** | CNT-02, MRK-04 |
| Graphic Design | Proofs pinned to the mat | **new** | SRF-01, FST-04 |
| Music | Cassette J-card | **new** | CNT-01, MRK-04 |
| About | The drawer's contents | built | SRF-03, MRK-01 |
| Contact | Letter, taped down | built | SRF-02, FST-01 |

Peg bar detail worth getting right: a real peg bar is **oblong / round / oblong**,
not three identical holes.

---

## 6. Build order

The order matters. Pass 01 makes the other two cheap; doing it backwards means
building the same nine tapes a tenth time.

**Pass 01 — Foundation.** Nothing visibly new; this is the pass that buys cohesion.
- Collapse the nine tape classes into one `.tape` component with variants.
- Put the mat behind the whole page, not just the hero.
- Give `.sec` a real sheet: paper, lift, and an overlap onto the section above.
- Unify all 7 reveals into one `.drawer` component with the shared pull gesture.

**Pass 02 — Identity.** Each section becomes an assembly of existing parts.
- Peg bar, sketchbook, contact sheet, pinned proofs, J-card — one per section.
- Index tabs return the numerals as a physical thing rather than a label.
- Work cards inherit their section's container.

**Pass 03 — Life.**
- Logo placement, badge stamping, doodle drift, the one-time discovery nudge.
- Passport stamps become MRK-01 marks earned by opening drawers — **not** a
  separate progress system.
- Lazy-load everything below the first sheet.

---

## 7. Working constraints

- `portfolio.html` is ~17,000 lines with a single embedded `<style>` block and heavy
  `!important` use. Check what already wins before adding a rule.
- Duplicate rule blocks are common; the **last** definition in source order is the
  one that renders. Delete legacy blocks rather than adding a tenth override.
- Mixed CRLF/LF has been an issue historically — match byte-exact when editing.
- Every animated property must respect the existing global
  `@media (prefers-reduced-motion: reduce)` rule.
- Verify contrast numerically (WCAG: 4.5:1 body, 3:1 large) rather than by eye.
  Contrast bugs have shipped on this project twice.

---

## 8. Extended direction (Sept 2026): one desk, one light, one camera

Decided with Annmary after the hero notebook and lighting work. It supersedes anything above that conflicts.

- **The site is a desk viewed from above; scrolling is the camera moving down it.** Not a website with a desk theme.
  Exploring someone's desk: things are pulled, lifted, flipped, opened. Every object has one small thing to find.
- **The mat is under everything.** Sections are objects on it, never full-width colour bands. Section colour lives in
  marks: tape, pen, tab, doodle. (`html body` paints the mat from a 600px tile, `mat-day/night.webp`.)
- **One light.** The variables from the hero (`--light-x/y`, `--lr..`, `--sr..`, `--sh-k`, `--key-*`) drive everything.
  Shadows: only the `--hn-sh-*` tokens (three stacked layers, direction from the light). Below the hero the light is two
  fixed, plain-alpha layers (`html::after` warm pool, `body::after` falloff). **No blend modes over scrolling content**
  (re-blended every frame; it was the cause of the hero lag).
- **One paper, both modes.** `--hn-paper-*` are identical day and night; light does the dimming. Paper recipe:
  `--hn-paper-r` + `--hn-paper-veil` + `paper-light-tile.webp` at 400px.
- **Type.** Handwriting (`--hn-hand`, extended with dashes, dot, curly quotes, ellipsis, x, % from her own strokes) for
  anything a person writes: titles, names, tags, links, annotations. Small printed labels and long copy stay in
  General Sans on the sheet, like a printed form with handwriting on it. No cut-out letters beyond the wordmark.
  Clash Display is retired from section content as sections are rebuilt.
- **Objects.** Animation = punched layout sheets on a peg bar (built); the rest follow section by section
  (Illustration sketchbook, Videography contact sheet, Graphic Design proofs taped to the mat, Music cassette J-card,
  About = wooden desk + drawer, Contact = letter taped down). A visible drawer opens for anything personal.
- **Rewards** (later): stamps earned by exploring become stickers the visitor can place on the notebook.
- **Sound**: opt-in only, never on load, never resumed by itself. Music loops in `public/audio/`, foley one-shots to come.

---

## 9. Rewards: one planned system (Sept 2026)

Design rule: **a reward must come from doing what a visitor already came to do (look at the work), must be something
that belongs on a desk, and must never get in the way.** No pop-ups, no dialogs, nothing that dims the page.

| Tier | Earned by | What you get | Where it lives |
|---|---|---|---|
| Stamp (5) | playing with a section's toy (the Studio Passport already counts these) | a rubber-stamp moment + a die-cut sticker of the section's doodle in its colour | `window.unlockStamp` (wrapped) |
| Doodle (24) | looking closely at a project: its characters and props peek over the edge of its sheet or print, drawn as paper cut-outs; click one to keep it | a die-cut sticker of that doodle | the `PEEK` table in the rewards script |
| Set | finding every doodle of one project | that project's hand-lettered title as a big sticker (Keep Yourself Safe has none yet) | `TITLES` |
| Everything | all five stamps | a gold star sticker and a thank-you slip | `final()` |

Jasmine's twelve doodles are spread over three sections (Illustration lead sheet, its Animation card, its Music card), on purpose:
completing her set means exploring the whole desk.

Everything earned is a sticker, and it all lives in ONE place: the **Studio Passport tab** (bottom right) opens a small
sticker book panel: stamps and every project's doodles, found ones in colour, missing ones as outlines with a hint about
where to look. It is not a dialog: nothing dims, the page stays usable, and it closes with its x, Esc, or the tab. Pick a
sticker there, click anywhere on the page to stick it; it stays on the visitor's desk on later visits (localStorage
`hn-rewards-v1`); click it there to move it; Esc puts it back. Notices are one tiny slip above the tab that fades by
itself. Sounds are slots (`stamp`, `reward`, `stickerPeel`, `stickerPlace`, `rewardFinal`) that stay silent until a file
exists (see public/audio/README.txt).

**Adding to it:** draw a doodle into `assets/hand/project-doodles-sprite.svg` (id `pd-...`), add its size to `PD` and one
line to `PEEK` (which card, which edge, how far along, how big). A new project: add its name to `PROJ`, its card to `HOSTS`,
optionally a title lettering to `TITLES`. Testing: `hnRewards.find('pd-kys-phone')`, `.findAll()`, `.grant('music')`,
`.grantAll()`, `.reset()` in the console.

**The next page of the notebook (desktop).** The hero notebook's right page has a lifted corner, "turn the page". The next page
is blank dotted paper, "Your page", with a rack of eight rubber stamps and three ink pads. The stamps are built from her own doodles and true facts about her
(NTU ADM class of 2026, Annecy 2025 with the Keep Yourself Safe head, Open for work, Stationery addict, A daily Milo, Jazzmine,
Music District, Singapore), lettered in her handwriting. No generic phrases: if a stamp says something, it is something she said. A visitor picks a stamp and presses it anywhere; it stays (localStorage `hn-stampage-v1`). Nothing on
that page is hers: it is the visitor's page in her book. It uses the `stamp` sound slot.
The first stamp pressed there earns one sticker, "Your page" (`hnRewards.notebook()`), and the book's counter becomes n / 30;
more stamps earn nothing extra, so it cannot be farmed.

**Die-cut doodles are solid.** The project doodles are line drawings, so `assets/hand/project-doodles-fill.svg` holds a solid
silhouette of each (gaps closed, holes filled), drawn in white under the ink wherever a doodle is cut out over the mat.
Regenerate it (`pd_fill.py` in the build scripts) whenever a doodle is added or redrawn.
