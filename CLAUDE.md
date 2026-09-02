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
