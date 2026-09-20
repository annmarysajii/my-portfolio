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
The first stamp pressed there earns one sticker, "Your page" (`hnRewards.notebook()`), and the book's counter becomes n / 31;
more stamps earn nothing extra, so it cannot be farmed.

**The nav is a ruler; the footer is the desk's front edge.** `#nav` is a boxwood ruler laid across the top of the desk: flat
boxwood colour, graduations (1/5/10 mm ticks) along its bottom edge, links in her handwriting with a highlighter swipe on hover
(no colour change), the Work dropdown and the mobile flyout are index cards (tape on the dropdown), the lamp and sound buttons are
little pressed-in paper pills, Resume is a slightly crooked yellow label. No blur, no hairline border: the shadow comes from the
light tokens. The footer is the dark front face of the desk with a lit chamfer on its top edge, cream handwriting on wood
(contrast 6.9:1 worst case), the visitor counter as a stuck label. Footer links carry `data-dock-avoid` so the Passport yields.

**The five toys are objects, not popups.** Each open toy (`#wrap .pg-toy .playground-scrap-card`) is a paper card lying on the desk:
no border, 2px corners, the light-token edge and shadow, hand-lettered tag/title/hint, buttons as small paper tabs with the chosen
one highlighted (yellow) rather than filled, canvases with a hairline instead of a heavy ink border, and "put it back" in pencil at
the foot instead of a circled x. One shared rule set covers all five (`.pg-btn`, `.rubber-stamp-btn`, `.lut-btn`, `.chord-pad-btn`);
on top of it, each toy's whole card is its own object: Animate a flipbook (cloth binding, stacked page edges), Draw a spiral
sketchbook, Capture a clapper board (striped clap-stick, chalk lettering), Fonts a printer's specimen card (double printed rule), Strum a
walnut guitar top with a maple-edged soundhole. Room for the object's thickness comes from padding on the open `.pg-reveal-inner`
(the reveal wrapper clips overflow, so shadows outside the card would otherwise be cut off).
The objects also move when used (CSS Q3 + `initToyMotion`): pressing a principle thumbs the flipbook, Capture snaps the clap-stick
and flashes the slate. Both switch off under reduced motion.

**About: the badge follows you.** The closed Studio ID badge is `position: sticky` beside the tall notebook page, so the right of the
section is never a blank stretch of wood while the credentials are read (open, the Studio Desk drawer is tall and stays put). This needed
`body { overflow-x: clip }`: with `overflow-x: hidden` on both html and body, the body is a scroll container that never scrolls, and every
`position: sticky` on the site is silently inert.

**The bookmark is a ribbon.** The hero's blue tab is now a satin ribbon marker: it comes out from between the pages at the head of the
spine (darker there), lies down the gutter, and hangs out below the book with a swallowtail. Its shadow is a `drop-shadow` on the light
tokens (a box-shadow would ignore the swallowtail). It is hidden at 900px and below: there the pages stack (or the hero is the phone
flip pad), so there is no gutter for it to lie in.

**Take-away rewards ("For you" in the sticker book).** Fixed, not the visitor's choice, so it feels like being handed something. Finishing a
project's doodle set gives that project's card (Keep Yourself Safe, Jasmine, Dear Friend; Chase has none): a print-ready PNG, 2.5 x 3.5 in at
600 dpi, built from `assets/rewards/src/card.html` (`#kys`, `#jasmine`, `#dearfriend`; rendered with headless Chrome at 2x). All five stamps
give her business card: `assets/rewards/annmary-saji-business-card.pdf` (her own two-page card, phone number and LinkedIn left off the back,
only email and Instagram) and `annmary-saji.vcf` (adds her contact in one tap). Unlock is derived from what is already collected (`GIFTS` in
`initRewards`), so only "which have been shown" is stored (`seen`); the first time one appears it slides in once. Locked ones are pencil
envelopes with the hint. Nothing here blocks the page: it sits in the sticker book and a tiny notice says one has arrived.

**"Take my page".** The notebook's stamp page has a "take my page" button (enabled after the first stamp) that saves the visitor's stamped page
as a PNG at 2x, with "My page", "in Annmary Saji's notebook", the date and the site address. It is built as a standalone SVG (stamps redrawn from
their designs with their symbols, the handwriting and the ink-roughness filter embedded), painted to a canvas and saved: no library, nothing
uploaded. The image has the page's own proportions (tall on desktop).

**Load weight (checked Sept 2026).** Fresh load is about 3.6 MB of images with nothing downloaded that was not needed: the reward cards, thumbnails and
audio only load when used (the sound effects decode once room sound is switched on; the card PNGs are only fetched on Save). The notebook stamp
rack and its saved imprints are built the first time the page is turned to, because they draw with the 470 KB doodle sprite. The About badge SVGs were
optimised with svgo (1.3 MB to 251 KB and 2.1 MB to 794 KB, edge pixels only differ) and the six drawer objects are webp (925 KB to 507 KB); the
original PNGs are still in `assets/portfolio-data/My profile/`.

**The invitation (how a first-time visitor learns the passport exists).** Three quiet cues, all gone once the passport is taken
(`hn-passport-v1`): the dock tab reads "Get your passport" and wobbles every few seconds; 3 seconds in, a boarding-pass ticket ("Stay a while.
Stamps, doodles and stickers are hidden around this desk...", a red 0/30 stub, "Take my passport" / "not now") slides in above the tab and
tucks itself away after 18 s (Esc closes it; it returns on the next visit, at most three times); and the first time the sticker book opens, its
"How it works" folds open by itself (four lines: play, look closely, turn the page, stick anything anywhere), then stays folded. Opening the book
by any route counts as taking the passport, and anyone who already has stickers is never nagged.

**The notebook page takes a pen, a marker and words.** Besides the eight stamps, the visitor's page (`hn-stampage-v1`) has Pen, Marker (a highlighter:
wide, half-opaque, multiplied) and Words (click, type, Enter; the size is fitted so a line never runs off the page and is stored, so the page and the
saved image agree), eight inks (red, orange, green, teal, blue, purple, pink, black) and Undo. Everything is one ordered list (capped at 120 items and
6000 stroke points). A stroke is stored as points in permille of the page, drawn as a `non-scaling-stroke` SVG path, so it survives the page changing
size. "Take my page" saves all of it. The first mark of any kind still earns the "Your page" sticker.

**Arrival.** Taking the passport (the ticket, or just opening the book) stamps it "Arrival", a ticket-shaped sticker (`dd-ticket`, added to the
inline doodle sprite at boot), so the counter starts at 1 / 31 and the first press feels like a reward. Anyone who had already claimed gets it quietly.

**The guestbook (`#hn-gb`).** A panel like the sticker book (so it works on a phone), opened from the footer link "Leave a note in the guestbook" or
from the sticker book. There is no server: a note is POSTed to the same FormSubmit address as the contact form ("New guestbook note"), so she reads
and moderates every one. Approved notes are listed in `assets/notes/notes.json` (format and steps in `assets/notes/README.txt`) and appear on the wall as
coloured sticky notes. The sender sees their own note at once, marked "sent, waiting for me to read it" (kept in their browser, `hn-gb-v1`). Guards:
honeypot field, no links, 3 to 240 characters, one note per 45 seconds. `window.__hnGbDry = true` in the console stops it sending (for testing).

**Die-cut doodles are solid.** The project doodles are line drawings, so `assets/hand/project-doodles-fill.svg` holds a solid
silhouette of each (gaps closed, holes filled), drawn in white under the ink wherever a doodle is cut out over the mat.
Regenerate it (`pd_fill.py` in the build scripts) whenever a doodle is added or redrawn.
