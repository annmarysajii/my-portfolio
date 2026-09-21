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
| Stamp (5) | playing with a section's toy (the Desk Passport already counts these) | a rubber-stamp moment + a die-cut sticker of the section's doodle in its colour | `window.unlockStamp` (wrapped) |
| Doodle (24) | looking closely at a project: its characters and props peek over the edge of its sheet or print, drawn as paper cut-outs; click one to keep it | a die-cut sticker of that doodle | the `PEEK` table in the rewards script |
| Set | finding every doodle of one project | that project's hand-lettered title as a big sticker (Keep Yourself Safe has none yet) | `TITLES` |
| Everything | all five stamps | a gold star sticker and a thank-you slip | `final()` |

Jasmine's twelve doodles are spread over three sections (Illustration lead sheet, its Animation card, its Music card), on purpose:
completing her set means exploring the whole desk.

Everything earned is a sticker, and it all lives in ONE place: the **Desk Passport tab** (bottom right) opens a small
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
The first stamp pressed there earns one sticker, "Your page" (`hnRewards.notebook()`), and the book's counter becomes n / 39 (it was 38 before the photo sticker was added);
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

**Rain on the window.** With room sound on, a quiet rain loop (`public/audio/rain-loop.mp3`, a seamless 40 s cut of her rain-on-window recording) plays under
the music: `--snd-rain` is .10 by day and .32 at night, it re-levels when the lamp is switched, and it ducks with the music while a video plays.

**Secrets: peelable tape (seven stickers with the runner, counted in the total, now n / 38).** Five taped scraps can be peeled (`SECRETS` in `initRewards`: the notebook's red and gold tapes, the reel's two corners, the
letter's tape). Peeling lifts the tape (the `tape` sound slot), drops a paper slip with a line of hers taken verbatim from her own notes on the site (the fake IKEA plant, the HB pencil, the stationery, the chocolate
milk tea), gives a sticker the first time, and the tape presses back down so the desk is never stripped. To change what a tape says, edit its `text` in `SECRETS`. (A draggable lamp was the sixth secret; it was removed, see below.)

**The desk is not always still (the seventh secret).** When the page goes quiet, one of her doodles (the runner) runs along under the top bar. The first run comes
after ~35 s of the visit once the visitor has been idle for 9 s; later ones need 75 s since the last and a 20 s pause (or 3.5 minutes regardless); never more than
five a visit, never while the sticker book or guestbook is open or the tab is hidden. Pressing it catches it (a sticker the first time, a slip either way). With
reduced motion it stands still under the bar for 9 s instead of running. `hnRewards.runner()` starts one for testing.

**The toy sheets are paper in both modes.** Draw, Fonts and Strum used to turn their canvases dark at night (and quietly turned the black pen white), so a dark
pen could not be seen. The sheets are now paper day and night like everything else on the desk, and the pen colours are what they say they are.

**Memory: a rank, a welcome back, a gentle hint.** The passport has ranks (`RANKS` in `initRewards`: Visitor, Regular at 3, Studio Mate at 10, Desk Neighbour at 20,
Insider at 32, Keeper of the Desk at everything): shown beside the count in the book and as the tab's tooltip, with one tiny notice when a new one is reached.
A returning visitor (second visit or later, having found something besides Arrival) is greeted once, after ~4 s: "Welcome back. You have found 12 of 38 (Studio Mate).
Psst: ..." with one hint and a link to the book. Someone who has taken the passport but found nothing for ~3 minutes gets a hint (at most two a visit); nobody who
has not taken the passport is ever hinted at. A hint is one thing that is still hiding, chosen at random from stamps, doodles and secrets (`hintText`), never a list.
`hnRewards.hint()` and `.rank()` are there for testing.

**Developing prints (project cards).** The first time a card scrolls into view its picture comes up out of cream with a warm tint at the middle, like a print in the tray
(`initDevelop`). Built to cost nothing: only opacity animates (the veil is a compositor layer, nothing repaints), it plays once per card, only for cards that were below
the fold at load, only two or three run at once, and it is off for reduced motion, phones (<= 640px) and the adaptive `hn-lite` mode. The veil sits on the card, not in the
picture, because the card loader rewrites the picture's contents; it removes itself when it ends and after 3 s regardless, so a card can never stay covered. Measured
before and after on a 9000 px scroll through all 24 cards: median 16.7 ms, p95 16.8 ms, max 17 ms, none over 33 ms both times (the same as with it switched off).
A flip-to-a-back-side was deliberately left out: it would only repeat the text already on the card. It would earn its place once there are credits to put on the back.

**The drawer you actually pull (`initDrawerPull`).** The quick-look drawer's handle can be held and dragged: the tray's height is the pointer's travel (1:1, so the front and the
handle stay under the hand, because the tray grows above the front), and on letting go it settles open or shut (over ~32% of the way opens a shut drawer, an open one needs to be
pushed below ~62% to close, so it does not flutter). A plain click and the keyboard still toggle it, a drag is not also a click, and it makes its sound once, when it settles. Only
the drawer's own box restyles while it moves. Touch: the handle has `touch-action: none`.

**Tidy the pouch (the eighth secret).** In the About "Studio Desk" drawer, below her desk objects, the pouch is a mess: six pieces of stationery (her pencil and ruler doodles, and four
glyphs drawn for it: fineliner, eraser, washi roll, highlighter) are scattered in a loose spread and can be dragged into the pouch, each with the clapper's clack and a shake of the
pouch (`initTidy`). The last one gives the pouch a flourish, a line ("All tidy. (It will not last.)") and the "Pencil case" sticker; "mess it up again" reshuffles it. Keyboard: pressing a
piece puts it in. A plain press also puts a piece in, so a slow or shaky hand is never blocked.

**About: the Studio Desk drawer in three tabs, and text you can read.** The drawer had become one 1500 px scroll (her words, six objects, the pouch game, five photos). It is now a
folder with three index tabs (`initDeskTabs`): "On my desk" (her words and the six objects), "Photos" (the uni polaroids, three across, two on a phone) and "Play" (tidy the
pouch; a red dot until it has been opened). One shows at a time: the drawer is 480-600 px tall instead of ~1500, nothing is clipped, and the pieces are only moved, not changed.
Text in About was small: handwriting needs to be larger than print to read as easily, and the small caps labels were 11 px. Now the intro is 21 px, the credentials 21 px with the
label above the value (so the value gets the whole card width instead of a narrow column), the drawer text 20 px, the labels 13 px and the chips 13.4 px.

**About: the inventory in two columns.** The three inventory cards were 353 / 234 / 522 px tall side by side, a ragged row. From 821 px up it is two columns: Toolkit and Words &
Languages stacked on the left, Awards & Recognition on the right, so both sides end at about the same height (row 753 to 680 px) and the awards titles fit on one line each. Below
821 px it is the single column it always was.

**Tidy the pouch: dragging.** A piece is never re-inserted into the page while it is held (doing that drops the browser's pointer capture, which made dragging feel sticky); move and release
are listened for on the window; a drop counts if the piece's centre or the pointer is within ~22 px of the pouch, which glows to say "here"; a press with under 5 px of movement is a
press and puts the piece in. Verified with real mouse drags.

**The movable lamp was removed, and why (Sept 2026).** A draggable lamp was built (nav button drawn as a lamp, drag it to aim the light, a page-wide light split from the hero's) and it went wrong: the
lighting the site had before (window-pane shadow by day, warm lamp pool at night) disappeared on her machine and the site looked flat. Two causes were found. (1) The page's adaptive "lite" mode
(`initFrameMonitor`) hides the window shadow, the lamp pool and the warm glow when frames average slower than 30 ms, and it remembered that in `sessionStorage` for the whole tab session: a laptop capped at 30 fps
(33 ms) tripped it at once, and it stayed off even after reloading. It now needs an average slower than 46 ms (about 22 fps) for three stretches in a row, starts watching after 7 s, and never remembers (it also
clears any old flag). (2) The lamp itself changed how the lighting was wired, and by day moved the window shadow, which must stay put. All of that was taken out: the page-wide layers read `--light-x/--light-y` again
exactly as before, the window shadow is fixed, the nav button is the plain day/night toggle, and the lamp sticker is gone (seven secrets, counter n / 38). If a lamp is ever tried again it should touch nothing
that the day/night lighting reads (a separate overlay that is moved with `transform`, which costs nothing), and it should be tested on a slower machine first.

**The lamp was tried again as a hero desk object, and removed (Sept 2026).** It was built the safe way (a button in `#hero`, moved with `translate`, its light a plain translucent gradient, nothing set on the root) but it was not wanted on the page, so it is gone: no lamp code, no lamp CSS, no lamp sticker. The site has no lamp; the nav button is the plain day/night toggle. Counter is n / 39.

**The passport book, redone (Sept 2026).** `renderAlbum` now opens on a summary card (a progress ring, the rank as a stamp with a dot ladder and "n more to be <next rank>", four counts with bars: Stamps, Doodles, Secrets, Extras) and three tabs: Stickers (the old sections plus the how-it-works guide), Creations (the visitor's photos) and For you (the gifts). The ring only fills when the book is opened, not on every tab click.

**Save my passport.** `passportSVG` builds a 1080-wide portrait card as a standalone SVG (the same trick as "take my page": the symbols and the hand font are embedded, so it needs no library), paints it to a canvas and offers it as a PNG in a small preview (`#hn-share`, with Save picture, Share where the device supports files, and Close). The card shows the rank as a rotated stamp, the big count and its bar (ticks at the rank thresholds), the four counts, every sticker (found ones in colour, missing ones as dashed circles), the gold star if earned, the latest four polaroids, the date and the site address. `window.__hnLastPassport` holds the last blob for testing.

**Keep a photo (`initPhotos`, `hn-photos-v1`).** Each of the five toys has a "Keep a photo in my book" button. It photographs what the visitor made: the three canvases directly (Draw, Fonts/Bezier, Strum), the Capture scene, and for the bouncing ball an onion-skin of its last move (the ball's position is sampled every 50 ms while the toy is open; the last burst of movement is redrawn as fading ghosts). The picture goes on a polaroid (paper frame, hand-lettered caption, toy name and date), is stored as a JPEG data URL in localStorage (12 at most, about 20 to 40 KB each), flashes, and flies to the passport tab. An empty drawing sheet is refused with a message. The first photo earns a sticker (`photo`, third of the "Along the way" extras). Photos can be saved or removed from the Creations tab; "start over" does not delete them. Nothing is uploaded. API: `window.hnPhotos` (`list`, `count`, `remove`, `save`, `keep(toy)`, `onchange`).

**Card and strip sounds answer every hover and every press (Sept 2026).** The first version let a card sound once, then stay quiet for 8 seconds, and the last hover 200 ms ago also blocked the next card, so re-entering a card or sweeping a row did nothing. Now every `pointerenter` of a project card or a drawer strip plays the soft thump (guard: 45 ms between two, so a single crossing cannot double-fire), and every `pointerdown` plays a heavier one on any pointer, with a 9 ms buzz on phones that support it. `window.__hnSfx(name, k)` takes an optional gain multiplier: hover is 2x, press 3x, the louder-than-the-other-foley level being deliberate so it can be felt. Cards also press down 2 px while held (`.desk .grid .card:active`). Only the cards and drawer strips do this; other sheets stay silent.

**Project pages in the desk's language (Sept 2026).** `css/hn-project.css`, linked at the end of `project.html`'s head, restyles every project page except `gobunny`, `green-arrow` and `acorn-oak` (their own brand art direction). A small script in the head adds `hn-proj` to `<html>` for the rest, and every rule is scoped to it. `--fd` is repointed to the hand-lettered face, so every `var(--fd)` heading follows; the 11 hard-coded `'Clash Display'` uses in `project.html` were turned into `var(--fd)` for this (on the three excluded pages `--fd` is still Clash, so they render as before). The nav is the boxwood ruler with a yellow crooked "Back to Portfolio" label, the footer is the wood front edge, the intro box and sidebar blocks are paper with tape, badges and buttons are yellow paper labels, tools are highlighted words, binder tabs are index tabs, the work is mounted as prints (white mat via a spread box-shadow, because the images clip their own outline), and the title gets a hand-drawn underline in the page's accent. Each page's own tokens (`--bg`, `--ink`, `--accent`, `--line`) are read, never overridden, and light and dark both work. `font-synthesis: none` stops a faked bold on the single-weight face. Tape on the masonry items was tried and dropped: the multi-column layout strands the tape of an item that has not loaded its image. Checked in a loop over all 24 other project pages: all render the hand title with no horizontal scrolling.

**Round of key improvements (Sept 2026).**
- *Night light.* The lamp sits near the middle of the screen (`--light-x/y` 48/42 at night, was 30/36), its pool is wider (hero 90% x 72%, page-wide 130% x 116%) and a little stronger. The hero lamp and the page-wide `html::after` are `soft-light` and the mat glow sits under the paper, so ink is never lifted; the light is a wash on paper, not on text.
- *Sound follows the visitor.* The room-sound engine moved to `js/room-sound.js`, loaded by both `portfolio.html` and `project.html` (every project page has the speaker button in the nav). If sound is on when the visitor leaves a page it is remembered for this tab only (`sessionStorage hn-snd`, with the spot in the track) and resumes on the next page, so a new tab or a new day is still opt-in. Browsers only allow sound after a touch on the site; `ctx.resume()` can hang without one, so the engine does not wait on it: if it cannot start at once the button shows as pressed and the next touch starts it.
- *The floating doodles are back* in every section (`#wrap .desk .sec-bg-canvas`, they had been hidden by the desk redesign). They drift over mat and paper alike (z-index 4, never catch a click), rest as a slate line and light up in their own colour near the pointer; the palettes are the bright versions so they read on the navy mat.
- *The Desk Passport tab* (renamed from Studio Passport everywhere): a paper label with a red passport booklet, a strip of tape and a rubber-stamped count; icon-only on phones.
- *The hero no longer ends in a line* above "Need a quick look?": the last 90px of the hero fade out (one `mask-image` on `#hero`, no measurable cost in a scroll test; off in lite mode) and the footer line sits above the fade. Where the mat meets the wooden About section the wood now gets a soft shadow (`#about::before`).

**The gateway and the send button (Sept 2026).** `index.html` ("What are you looking for?") now loads `css/hn-gateway.css`: the same navy mat under a soft lamp, the question on a torn paper slip with tape, the four answers as taped index cards (a doodle from `assets/hand/doodles-sprite.svg`, the line in her hand, and where it leads), the speaker button (so sound can start here and carry on to the portfolio), and the cards thump on hover and press like the project cards. Choosing one lifts the slip and cards away, shows "You're at the right place.", then the hyperspace warp runs as before but recoloured for the mat (cream streaks rushing out of the navy, ending on the navy the portfolio opens on), and it goes to `portfolio.html?f=...`. The contact form's Send Message button is a crooked yellow paper label (straightens on hover, presses on click), and the form labels are in her hand (`#contact .letter #fsb.fsub`, section AM of the site CSS).

**The guestbook's notes live in Supabase (Sept 2026).** `supabase/setup.sql` creates one table, `guestbook_notes`, with row-level security enforced by the database: the site's public key can add a note (only name, text and colour, always saved not-approved) and read approved notes, nothing else. Guards in the database: 6 new notes a minute site-wide, 300 waiting at once, no links, trimmed text. She approves by ticking a box in the Supabase Table Editor; the wall shows it straight away, and she still gets an email heads-up through FormSubmit. `const SB = { url, key }` at the top of `hn-guestbook.js` holds the project URL and the anon / publishable key (public by design; never the service_role key). While it is empty the guestbook works the old way. Notes in `assets/notes/notes.json` are still shown first, for pinning a favourite by hand.

**Phones (Sept 2026).** Nothing about the look is cut on a phone. What changed to make it lighter: the peeking doodles draw their cream body and die-cut border as one stroked shape inside the sprite (`class="pdf"`, sprite `?v=7`), so each needs one drop-shadow instead of five stacked filters; the floating doodles stay, lit by a finger, drawn at half rate with fewer of them; and the frame monitor judges a phone sooner (34 ms average, about 29 fps, three stretches in a row; a laptop is still 46 ms) and only then switches to lite mode by itself. `?lite=1` forces lite, `?lite=0` keeps it off.
**Phone frame costs found from a real phone (section AN of the site CSS).** The hero scrolled badly, the drawer glitched and stamping blinked the whole page. On a phone only: the hero's four blended light layers (they sat over the playing reel, so every video frame re-blended a tall surface) are replaced by the plain-alpha glow and edge that lite mode uses, and the hero fade mask is off; the drawer opens at once with its contents fading in instead of animating its height; a pressed stamp is plain (no SVG turbulence filter or blend mode). Desktop is untouched.
**Taps that jumped to another section: found, and fixed (Sept 2026, phones).** Root cause (section AO of the site CSS): on a phone the Work/About/Contact menu is a flyout closed with `opacity:0; visibility:hidden`, but its Work sub-list sets its own `visibility:visible; pointer-events:auto`, which beats the parent's `hidden`. Its five links (Animation, Illustration, Videography, Graphic design, Music) therefore sat invisible under the bar (about 220 x 320 px, top right of the screen), and any tap there jumped to that section; it looked like a ghost click. It is a bug from when the hamburger was built. While the menu is closed nothing inside it is tappable now. Two extra safety nets stay: the old passport screen (`#passport-modal`, whose slots jump to sections) is removed at load, and `initScrollGuard` (`hn-guard.js`) puts the page back if, on a touch device, it moves by most of a screen within 2.5 s of a plain tap that was not on a link to a section or the menu (each catch adds 1 to `sessionStorage['hn-guard']`).
**The notebook's next page works on a phone.** The "turn the page" corner is shown at every width. Below 640px the page opens as a full-screen sheet of the same paper (`.hn-sp.is-fs`: moved to `<body>` while open and put back when closed, the page behind locked with `html.hn-sp-open`, `touch-action: none` so a finger can stamp, draw with the pen or marker and write). Stamping it still earns the "Your page" sticker, so every reward is reachable on a phone.
**Sound after a reload on a phone.** A phone will not start audio without a tap, so the engine waits for the first real tap (`touchend` / `pointerup` / `click` / `keydown`; a `pointerdown` does not count on an iPhone) and only stops waiting once the audio is running; meanwhile the speaker button pulses (`.is-armed`). `js/room-sound.js` is `?v=2` on all three pages.

**A video with sound wins.** While any `<video>`/`<audio>` on the page is playing with its sound on (the hero reel after its Sound button, or in the
lightbox), the room music fades out and the effects go quiet; muting, pausing or the end of the video fades the music back in (`syncDuck` in
`initRoomSound`, driven by the media events caught at the document, so it needs no per-video wiring).

**Die-cut doodles are solid.** The project doodles are line drawings, so `assets/hand/project-doodles-fill.svg` holds a solid
silhouette of each (gaps closed, holes filled), drawn in white under the ink wherever a doodle is cut out over the mat.
Regenerate it (`pd_fill.py` in the build scripts) whenever a doodle is added or redrawn.

**Scribble sound (Sept 2026).** A pencil or marker on the page no longer plays a one-shot; it sounds for as long as the hand moves.
`public/audio/scribble-pencil.mp3` (5.5 s, cut from `assets/sound/freesound_community-pencil-29272.mp3`) and `scribble-marker.mp3` (2 s, cut from
`freesound_community-marker-lineswav-14823.mp3`, Pixabay) are turned into seamless loops at run time (`seamless()` in `js/room-sound.js`: the tail
is crossfaded into the head, equal power, 0.18 s). `window.__hnScribble.start('pencil'|'marker')` on press, `.move(pxPerMs)` on every move, `.end()`
on release: the level and pitch follow the pointer's speed and a hand held still is silent (a 60 ms watchdog fades it after 90 ms without a move).
Used by the notebook's Pen and Marker and by the Illustration toy's Sketch Pen (wired in `initToyMotion`). A stroke no longer plays the `stamp`
sound when it ends: only a rubber stamp does (`push()` in `initStampPage`). The `toyDraw` slot is now unused. Re-cut a loop with ffmpeg from the originals
in `assets/sound/` if a different section is wanted.

**The notebook page: move, select, change (Sept 2026).** A fourth tool, Move (four-arrow icon), joins Pen / Marker / Words; with nothing in hand any mark can be
grabbed and dragged directly. Hit-testing is geometric (`hit()`: distance to the polyline for strokes, the element's box for stamps and words), so thin
pen lines are easy to catch. A selected mark gets a dashed box and a small tag (smaller / bigger / turn / remove; strokes only have remove); the arrow keys
nudge it (Shift = 4x), Delete removes it, Esc lets go. Stamps carry an optional `z` (scale, CSS `--z`), words their `fs`, both honoured by "take my page".
Every change (add, move, resize, turn, remove) goes on `hist`, keyed by the mark object (`elOf` is a WeakMap mark -> element, so the saved JSON stays plain
data), and `undo` steps back through them; after a reload, with no history, undo still takes the last mark off. Pen and marker each have thin / medium / thick
(three dots by the inks, shown only while drawing), and the line under "Your page" tells you what the current tool does (`hint()`).

**Notebook sounds (Sept 2026).** Three new sound slots in `js/room-sound.js` (`pick`, `key`, `paperGrab`; files in `public/audio/`). Picking up a stamp, the
pen, the marker or the words tool plays `pick` (an ink plays it at 0.6), and so does a stamp in the Draw toy; every letter typed with the Words tool plays `key`;
turning the notebook's page plays `paperGrab` (x2.2, the rustle base level is quiet), open and close. Wired in `initStampPage` and `initToyMotion`. The needle drop and
vinyl crackle that exist in the Reels were left out of the site on purpose. `js/room-sound.js` is now `?v=4` on portfolio, project and index.

**Section doodles were still hidden; hero night deepened (Sept 2026).** The floating doodles had been "restored" by raising their z-index and opacity, but an older
`#wrap .desk .sec-bg-canvas { display: none !important }` (from the desk redesign) still hid all five section canvases (height 0); check `display`, not just z-index. The
rule now also sets `display: block` and `pointer-events: none`, and the five tall sections draw more, larger, stronger doodles than the hero (`const tall` in the doodle
script). Section AP of the site CSS re-grades the hero at night (desktop, not lite): steeper falloff where the book ends, a warm spill and deeper shadow around the book,
a stronger mat glow. Measured on the darkest paper: ink 9:1 or better, secondary text 5.6:1 or better.

**Project pages with their own colours, in the dark theme (Sept 2026).** Dear Friend "grayed out" on a phone whenever the stored theme (`localStorage.theme`, set by the
lamp button on any project page) was dark: the page kept its pale rose ground but took the dark theme's pale ink and dark overlay, so it went muddy grey with low-contrast
text; toggling back to light also lost the palette. `project.html` now keeps the four palettes (`PROJECT_PALETTES`) in one table, applies them only in the light theme, and the lamp
button (`toggleTheme`) uses the same `__applyProjectPalette(dark)` both ways. Dear Friend and Acorn & Oak also hard-code light-only colours all the way down the page
(their headings and paragraphs vanish on a dark ground), so they are kept in light whatever is stored (`__lightOnly`, not saved) and the lamp button is hidden on them. GoBunny and
Green Arrow read well in both themes and keep the button.
