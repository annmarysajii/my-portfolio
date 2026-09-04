# Annmary Saji — portfolio

Personal portfolio site for Annmary Saji, BFA Animation (NTU ADM, Class of 2026).
Static HTML/CSS/JS, deployed to GitHub Pages. `portfolio.html` is the main page.

## Read before visual work

- **`DESK_KIT.md`** — the design direction: the site's metaphor, its shared physical
  components (part codes SRF / FST / CNT / MRK / EDG), section assignments, and the
  build order. Read it before any visual, motion, or layout change.
- **`desk-kit.html`** — the same components rendered in a browser. Open it to see a
  part before rebuilding one.
- **`WEBSITE_AUDIT_AND_PLAN.md`** — the earlier structural audit (CSS architecture,
  duplicate stylesheets, `!important` debt). Still accurate on the code's condition.

## The design rule

> Work lies flat. The person is in a drawer.

Professional output is laid out on the desk with nothing hidden. Anything personal
about Annmary is behind something the visitor pulls open. This decides where
anything new belongs.

## Codebase facts worth knowing up front

- `portfolio.html` is ~17,000 lines with one large embedded `<style>` block. There is
  no external stylesheet for this page.
- Heavy `!important` use (thousands of occurrences). Check what already wins before
  adding a rule.
- Duplicate rule blocks are common — the **last** definition in source order renders.
  Delete legacy blocks rather than stacking another override on top.
- Line endings have been mixed CRLF/LF historically. Match byte-exact when editing.
- Category background colours (`--sec-*-bg`) are deliberately desaturated; the
  saturated identity colours live separately in `--sec-*-accent`. Don't re-saturate
  the backgrounds — "bold covers, calm pages".
- `#about` defines its own fixed custom properties that do **not** react to the
  light/dark toggle. Global `--ink`, `--blue`, `--paper` etc. do. Mixing the two
  scopes has caused real contrast bugs twice.

## Standing expectations

- Respect the existing global `@media (prefers-reduced-motion: reduce)` rule for
  anything animated.
- Verify colour contrast numerically (4.5:1 body, 3:1 large text) rather than by eye.
- Reuse an existing component before writing a new one. Tape was independently
  implemented nine times before it was caught.
- Don't commit or push unless asked — work is reviewed as a diff first.

## Project pages (`project.html`)

Three levels, cheapest first. Use the lowest one that does the job.

1. **`hero: {src, alt, caption}`** on a project entry renders one full-width plate
   under the header (`.proj-hero-plate`). Optional; projects without it are
   unchanged. Use it so the strongest artefact is the first thing seen.
2. **`groups: [{id, tab, title, note, match:[...]}]`** replaces the single masonry
   with titled `.cs-section` blocks, and adds one binder tab per group. `match` is
   substring matching against that project's `window.PORTFOLIO_DATA` paths.
   Anything no group claims still renders under "Also from the build", so a typo
   in a match rule can never silently drop a file.
3. **A bespoke branch** in the gallery builder, for a project whose own art
   direction should drive the page. `acorn-oak`, `gobunny` and `green-arrow` have
   one. Namespace the CSS (`.aocs-*`) and inject it with the branch.

Notes that cost time to learn:

- The Studio Passport is not on project pages and should stay off them.
- Field-note post-its are shared stationery in yellow/pink/blue. On a page with
  its own palette, restyle them in the branch rather than living with the clash.
- Full-bleed inside `.con`: `margin-left:calc(50% - 50vw); width:100vw`.
- The body carries a 24px graph grid site-wide. A brand page that isn't about
  graph paper should switch it off (`body { background-image:none }`).
- `renderMedia()` treats anything that isn't video/audio/YouTube/PDF as an image,
  so `.svg` and `.webp` both work in `PORTFOLIO_DATA`.

## Assets

- Vectors lift out of a PDF with `pdftocairo -svg` and stay sharp at any size.
  Crop them to their ink before use: several deck pages were under 20% ink and
  rendered as mostly empty white tiles.
- When auto-detecting an ink bounding box, render against **magenta**, not black.
  Black artwork on a black ground is invisible to the detector and gets cropped
  off (this ate a lockup's tagline once).
- Motion covers on the home page need a still in `assets/vidtogif/posters/`.
  The card loader hands it to the `<video>` as `poster`, so the card is never
  empty, and reduced-motion visitors get the still and no video download at all.

## The lead card (`.lc`)

One component, one instance per section. The section's other work stays in its
`.grid` at equal weight; the lead is wider, on its own ground, and carries a
five-step process strip. That is the whole hierarchy fix: **range only reads as
range when something in it stands taller.**

Four instances exist, one per section except Music:

| section | modifier | project | leads on |
|---|---|---|---|
| `#animation` | `.lc--kys` | Keep Yourself Safe | a film that got into Annecy |
| `#illustration` | `.lc--jasmine` | Jasmine | the final year project, 70+ pages and 6 tracks |
| `#videography` | `.lc--vipcolor` | VIPCOLOR | how the work was *run*, not how it looks |
| `#graphic-design` | `.lc--acorn` | Acorn & Oak | a brand argued from naming outwards |

Music has three cards and no lead, deliberately: hierarchy is what fixes a grid
of nine, not a grid of three.

A fifth gets one by declaring a modifier that sets the custom properties, and
nothing else:

```css
.lc--<name>{
  --lc-ground-fill: /* the card's surface */;
  --lc-ink:    /* primary text, needs 4.5:1 on the ground */;
  --lc-dim:    /* secondary text, also 4.5:1 */;
  --lc-accent: /* kicker, step numbers, CTA background */;
  --lc-cta-ink:/* text on the accent */;
  --lc-mount:  /* the cream artwork tiles sit on */;
  --lc-rule:   /* hairline rules */;
  --lc-veil:   /* optional overlay if the ground is a scan */;
}
```

Learned the hard way:

- A **flat ground**, or a texture. Not an illustration. The first `.lc--kys`
  used a film still as the card ground and the card competed with itself.
- Artwork tiles are `object-fit:contain` on the mount; **photography** takes
  `.lc-thumb--photo` and bleeds. Mounting a dark photo on cream looks like a bug.
- No 1px light border on a photograph. It reads as a stray outline; use shadow.
- The CTA carries `data-dock-avoid` so the Studio Passport yields to it.
  `initPassportDockYield` watches `[data-dock-avoid]` plus its two hero elements,
  so anything else the dock covers opts out with that attribute.

## Facts worth getting right

From Annmary's own production portfolio, which outranks anything already in the
markup:

- VIP Color "How To?" is **18 videos**, and it is an **internship at Venture
  Corporation**, not commission work. Both pages say so now.
- *Keep Yourself Safe* runs **1 min 30 s**, hand-drawn, screened in the Paris
  Lyon Singapore programme at Annecy 2025.
- *Jasmine* is **70+ comic pages and 6 original tracks** (not yet reflected on
  the site).
- *Dear Friend* (2024) is a **second** self-produced film, which is what makes
  the animation case more than a single title. Not yet given a lead card.

## Production notes (`.prod-notes`)

Replaces the old post-it field-notes system (pastel construction paper +
handwriting font + tape strip + emoji-prefixed titles) with an editorial block
that takes each project page's own colour tokens (`--ink`, `--accent`,
`--line`). One renderer in `project.html`; no per-page overrides.

- Kicker `PRODUCTION NOTES` in `--accent` with a hairline rule extending right
- Numbers in monospace, titles in Clash Display, body in the site's body face
- Three-column grid at desktop, two at 900px, one at 560px
- `:has()` selectors adjust the grid track count for 1-note and 2-note blocks
  so the layout does not read as broken when a project only has one entry
- Emoji prefixes on titles are stripped at render time; the source data is
  intact in case they're wanted somewhere else

Titles were previously carrying decoration (an emoji + a capitalised phrase).
The editorial layout doesn't need it; every emoji-prefixed title on every
project now renders without the icon, and the source data still has them.

## About section restructure

Credentials used to be behind five click-to-reveal objects (Toolkit, Words,
School, Awards, Now). A recruiter scanning the page never saw graduation year,
availability or reach without actively opening a drawer. That was a bad trade
for the drawer concept, which was meant for personal material.

Now, in About:

- `.about-spec` is a visible 6-row credentials block right under the intro
  tagline. Ink and label colours are hand-picked for contrast on the red
  ground (cream 7:1, warm-cream label 5.8:1). Rows are Degree, Status, Based
  in, Reach, Publicity (NTU FEST Director), Funded ($7,000+ Music District).
- Five widget objects reduced to three (Toolkit, Words, Awards). School and
  Now templates deleted since their contents are now visible.
- Four free-floating SVG doodles (swirl, spark, note, heart) deleted. The
  desk objects (plant, boba, headphones, journal, pouch, pencil) stay because
  they hold real personal micro-notes.
- Dead CSS for the four deleted doodles was left in place; the elements are
  gone but the class rules aren't hurting anything.

Design rule preserved: work lies flat, the person is in a drawer. The drawer
is still there — it just no longer hides the credentials.
