# Annmary Saji Portfolio — Visual Audit & Rebuild Plan

*Written after reviewing your walkthrough recording and reading the actual codebase (portfolio.html, index.html, project.html, game.html, jasmine.html, css/, js/, scripts/, and the assets folder) directly on your machine. Everything below is grounded in what's actually in the repo, not guesswork.*

---

## 1. The honest diagnosis

Your read on the site is correct, and the code explains exactly why. This isn't a "your taste is off" problem — it's a "the file structure is fighting you" problem, and it's fixable.

Here's what's actually going on under the hood:

- **`portfolio.html` (your main page) has an 11,468-line `<style>` block embedded directly in the HTML file** — no external stylesheet at all. It's 15,605 lines and 485KB total.
- **`index.html` and `project.html` each have their own separate `<style>` blocks** (three in index.html, five in project.html — two of which are generated dynamically inside `<script>` tags). None of them share a stylesheet with `portfolio.html`.
- You also have `css/styles.css` (1,190 lines) and `css/motion.css` (303 lines) sitting in the repo — but **`portfolio.html`, your main page, doesn't load either one.** `motion.css` is used by index/project/jasmine; `styles.css` is only used by `jasmine.html`. They're a second, parallel design system that most of your site ignores.
- Inside that giant embedded stylesheet, there are **3,915 uses of `!important`**. That's not a typo — nearly one in three rules needs a specificity override to win. That's the fingerprint of a stylesheet that's been patched over and over rather than architected, and it's exactly why a "small fix" from an AI tool can silently not show up (something more specific already wins) or why fixing it "the normal way" ends up touching more than expected.
- Dark mode isn't a second, designed theme — it's `[data-theme="dark"]` overrides bolted onto a light-mode-first system. Some selectors get overridden **two or three separate times** in different parts of the file (e.g. `.about-notebook-sheet` has three separate dark-mode rule blocks, `.hero-sketchbook` has two) — again, patch-on-patch rather than one source of truth.
- I found one genuinely invisible bug: in `css/styles.css`, `--surface-2: #EBEBЕ6;` — that middle "Е" is a **Cyrillic capital letter (U+0415)**, not a Latin E. It's an invalid hex color, so that CSS variable is silently broken wherever it's used.

**This is the actual root cause of "feels like a culmination of ideas without cohesiveness."** It's not that your design instincts are wrong — you clearly have a strong, specific aesthetic point of view (the collage wordmark, the polaroid cards, the stickers, the game easter egg are all genuinely good ideas). The problem is that five pages are each independently reinventing the same design tokens, colors, and dark-mode rules, and they've drifted apart from each other over the course of many edits. Every future prompt to Claude Code that says "make it more cohesive" is fighting five different sources of truth at once — that's also why edits have felt expensive and unpredictable.

The fix isn't "redesign everything." It's "consolidate to one source of truth, *then* redesign," and that order matters a lot for keeping Claude Code cheap and predictable (more on this in Section 5).

---

## 2. Visual critique

### What's already working — keep and protect this
- The open-notebook hero with the cut-paper ransom-note wordmark is a genuinely distinctive concept. It's the single biggest reason this site would stand out in a stack of Webflow-template portfolios — don't lose it in a cleanup pass.
- The small bespoke details (Annecy '25 selection sticker, the persistent Studio Passport badge, washi tape, polaroid corners) are exactly the "this person thinks about details" signal you want recruiters to walk away with. This is working — there's just too little consistency in *where* it shows up.
- The hover-preview videos are already properly optimized: for every raw GIF master in `assets/vidtogif/` (22–38MB each), you also have a compressed `.mp4` (under 3MB) and a `.webp` poster, and the live pages correctly link to the `.mp4` versions. Genuinely good instinct — this is not costing you page speed today.
- The showreel uses a poster image + lazy video pattern, which is correct.

### What's undermining the "vibrant but tasteful" goal
Your stated color instinct — saturated red/yellow/blue, arranged tastefully against neutrals — is right, and it's *in* the codebase (`--blue`, `--red`, `--yellow-sat` etc. are defined and used for buttons, stickers, the wordmark). But each of the five work categories (Animation, Illustration, Videography, Graphic Design, Music) currently gets a **full-bleed pastel background wash** across the entire section — light blue, pink, mint, tan, lavender. Scrolling through, it reads less like "one vibrant, tastefully-arranged site" and more like five different slides that don't quite agree on a palette, because the *background itself* is changing five times, not just an accent.

The fix isn't to remove the category color-coding — it's a smart wayfinding idea. It's to demote it from "background wash" to "accent": a colored section-number, icon, card border or tag chip, sitting on one consistent neutral paper canvas the whole way down. That's a small, mechanical CSS change (colors/backgrounds only, see Prompt 5) with a disproportionately large effect on "does this feel like one coherent thing."

### Dark mode
I didn't catch a light↔dark toggle in your walkthrough, so this critique is from the code rather than a screenshot — but the code tells a clear story. Dark mode is implemented as a second pass of overrides on top of a light-mode-first system, not as an equal, designed theme. The clearest example: your hero wordmark image swap already exists in JS (`updateHeroImage()` correctly swaps `hero_name.webp` → `hero_name_dark.webp`), so the *mechanism* is fine — but you clearly felt the current dark asset wasn't good enough, which is exactly why you made `hero_page_name_newdark.svg`. Good news: wiring that in is a five-minute job (Prompt 4), not a redesign, because the swap infrastructure already exists.

The pastel category backgrounds mentioned above are the other place dark mode will need real (not just "invert everything") attention once Section 5's Phase 1 is done — a muddy pastel simply darkened tends to go muddy-dark rather than rich, so those will likely want distinct dark-surface colors rather than a filter.

### The hero showreel card
Small, concrete, high-impact fix: the video player in the hero is a plain white rectangle sitting inside an otherwise fully tactile, textured, torn-paper page. It's the one element that looks like it was dropped in from a generic template. Framing it with the same polaroid/tape/torn-edge language you already use on project cards (Prompt 3) is a CSS-only fix that will make the hero read as more of a single, considered object.

---

## 3. Recruiter-access critique (this is the one with real stakes)

Goal #2 was "recruiters can access my work easily." Two findings here are genuinely urgent, not just aesthetic:

1. **The "Combined PDF / Full Portfolio" download button links to a 76MB PDF** (`AnnmarySaji_Production_Portfolio_2026 (1).pdf`). The other per-discipline portfolio PDF downloads are 4–34MB each. These are almost certainly unflattened, uncompressed image exports straight from InDesign/Illustrator. A recruiter on office wifi or a phone will often just... not wait for a 76MB download, especially compared to five other tabs open. This is the single highest-priority fix in this whole document, and it's also the cheapest to fix (Prompt 8 — recompress with Ghostscript, no code changes at all).
2. **`jasmine_reader.html` is 31MB as an HTML file.** It's linked from your main work grid as "Jasmine — Illustration and Comics." A 31MB HTML document (versus, say, referencing separate optimized image files) means that specific project page will be slow or may hang on a weak connection — exactly where you don't want your capstone project to stall out. Worth a dedicated pass to see whether it's embedding base64 images inline rather than linking to files.
3. Smaller and lower-stakes: your resume PDF (101KB) is already lightweight and fine — no action needed there.

None of this requires a redesign — it's compression and asset hygiene, and it directly serves the goal you actually stated.

---

## 4. Repo hygiene (affects your Claude Code costs directly, not just the live site)

- `assets/hero-collage.gif` (72MB), `assets/reel.mp4` (38MB), and `assets/master_reel.mp4` (112MB) are committed to git but **not referenced anywhere** in any HTML file — they're dead weight in your repo history. `master_reel.mp4` alone is over GitHub's 100MB hard per-file push limit, and the 76MB PDF above is close to it.
- Folders like `assets/scrapbook assets for reference/`, `assets/svg assets for portfolio/`, and `assets/paper texture refs/` (89MB + 71MB + 6.6MB) look like mood-board/reference material rather than deployed assets — worth confirming they're meant to be in the deployed repo at all versus kept locally outside git.
- Every one of these adds up to a much heavier `git clone`/`git status`/`git push`, and — relevant to your stated goal of not burning tokens on small asks — a much bigger surface for any AI coding tool to have to search through when it's trying to find "the CSS for the hero." A leaner repo makes every future Claude Code session faster and cheaper by default, before you even touch the design.

---

## 5. The fix strategy: two phases, in this order

**Phase 1 — Consolidate (structural, do this first, treat it as its own project).** Merge the tokens, base styles, and dark-mode rules that are currently duplicated across `portfolio.html`, `index.html`, and `project.html`'s five separate `<style>` blocks into one real file (`css/design-system.css`), linked by all three pages. This is a *consolidation*, explicitly not a redesign — the visual output should look identical before and after. This single step is what makes every future visual ask cheap: one file to point Claude Code at, one set of dark-mode rules, no more `!important` wars because there's no more specificity conflict to fight.

**Phase 2 — Polish (visual, do this after, and expect this to be most of your ongoing work).** Once there's one source of truth, every visual ask (de-saturate the category backgrounds, reframe the hero video, wire in the new dark asset, fix the Cyrillic bug, dedupe the leftover dark-mode overrides) becomes a small, scoped, cheap prompt against a small file instead of a search through a 15,000-line HTML document.

Doing Phase 2 before Phase 1 is exactly how you got here — every fix has to be re-applied across multiple duplicated stylesheets, or only fixes one of the three pages, which is what "reports as updated but doesn't change on the site" usually means in practice.

---

## 6. Claude Code prompt library

Use these roughly in order. Each is scoped to do one thing — resist the urge to combine them, even though it feels slower. Commit to git (or at least `git add -A && git commit -m "..."`) after each one lands cleanly, so a bad result is a `git checkout -- .` away rather than a "please undo that" conversation, which costs more tokens than the fix did.

**Prompt 0 — Audit only, no edits (run this first, in a fresh session)**
```
Don't change anything yet. Read portfolio.html, index.html, project.html,
game.html, and jasmine.html, plus everything in css/ and js/. Report back:
1) which pages actually load css/styles.css, css/motion.css, and each js/
   file, vs. which pages have their own inline <style> block
2) how many separate <style> blocks exist across all pages, with line counts
3) any selector defined more than once inside the same file (exact duplicates)
4) a count of !important declarations per file
Output this as a short report in the chat. Do not edit any file.
```

**Prompt 1 — Fix the invisible bug (trivial, isolated)**
```
In css/styles.css, the line `--surface-2: #EBEBЕ6;` contains a Cyrillic
capital "Е" (U+0415) instead of a Latin "E", making it an invalid hex color.
Replace it with a valid hex value consistent with the surrounding neutral
palette (e.g. #EBEBE6). Change only this one line.
```

**Prompt 2 — Structural consolidation (the big one — see Section 7 on which model)**
```
Create a new file css/design-system.css. Move the :root token block, base
reset, typography rules, button/card/tag primitives, and the [data-theme="dark"]
overrides that are currently duplicated across the inline <style> blocks in
portfolio.html, index.html, and project.html into this one file, keeping the
CURRENT visual output pixel-identical — this is a consolidation, not a
redesign. Link css/design-system.css from all three pages before any other
stylesheet. Remove the now-redundant duplicate rules from each page's inline
<style> block, but leave page-specific/one-off rules where they are. Do not
touch game.html or jasmine.html in this pass. Afterward, list every selector
you moved and confirm none were changed in value, only relocated.
```

**Prompt 3 — Hero video frame (do after Phase 1)**
```
In portfolio.html, the .reel-frame element (the showreel video container in
the hero) currently renders as a plain white rectangle. Give it the same
tactile treatment as the polaroid project cards elsewhere on the site — a
slight rotation, taped or torn-paper edge, a soft drop shadow — reusing the
existing washi-tape/polaroid CSS already defined on the page. CSS-only,
do not touch the video element's JS or attributes.
```

**Prompt 4 — Wire in your new dark hero asset**
```
Convert assets/hero_page_name_newdark.svg to a WebP at the same quality/
settings as the existing assets/svg-opt/hero_name_dark.webp (target ~250KB),
and save it as assets/svg-opt/hero_name_dark.webp, replacing the current
file. Confirm updateHeroImage() in portfolio.html still points to that exact
filename. No other files should change.
```

**Prompt 5 — Category background de-saturation**
```
Across portfolio.html, each work category section (#animation, #illustration,
#videography, #graphic-design, #music) currently uses a full-bleed pastel
background tint. Change these sections to share one neutral canvas background
(matching the hero), and move each category's color to an accent treatment
instead — the section number, an icon, and card top-border/tag color — so the
red/yellow/blue identity reads as deliberate accents rather than five
different-colored slides. Colors and backgrounds only — no layout, spacing,
or copy changes.
```

**Prompt 6 — Dark-mode dedupe**
```
Search portfolio.html for selectors under [data-theme="dark"] that are
defined more than once (for example .about-notebook-sheet appears in three
separate places). For each duplicate, merge them into one rule at the
earliest occurrence, keeping the most complete/most recent property set, and
delete the later repeats. Show me a diff before/after for review.
```

**Prompt 7 — Repo cleanup**
```
First confirm that assets/hero-collage.gif, assets/reel.mp4, and
assets/master_reel.mp4 are not referenced by portfolio.html, index.html,
project.html, game.html, or jasmine.html. If confirmed unused, add them to
.gitignore and run git rm --cached on each (leave the files on disk, just
stop tracking them).
```

**Prompt 8 — PDF compression (biggest real-world impact, do this one soon)**
```
Write a one-off script (using Ghostscript if installed, otherwise tell me
what to install) that recompresses every PDF in
"assets/portfolio-data/PORTFOLIO PDFS/" for on-screen viewing (roughly
150dpi image quality), saving results as *-compressed.pdf alongside the
originals so I can compare size/quality before swapping the site's download
links. Don't edit any HTML yet.
```

**Reusable template for every future one-off ask:**
```
FILE: [exact path]
SCOPE: [exact selector / function / element]
Change ONLY [the specific thing]. Do not modify any other file or selector.
Show me a diff, not the whole file, when done.
```

---

## 7. Tools worth adding to the workflow

- **Ghostscript** (`gs`) or Adobe Acrobat's "Reduce File Size" — for the PDF problem in Section 3. This alone probably has the best effort-to-impact ratio of everything in this document.
- **ffmpeg** (you likely already have it, given `vidtogif/` exists) — for any future GIF-to-video conversions; you're already doing this right, just keep the pattern going.
- **SVGO** (`npx svgo`) — for optimizing SVGs like `rock_samples.svg` (1.2MB) and `butterfly_bg.svg` (1.6MB) if they're ever wired into a page; also useful any time a design tool exports a bloated SVG.
- **Squoosh** (squoosh.app) — quick manual image/WebP compression when you want to eyeball the quality tradeoff yourself before handing a file to Claude Code.
- **WebAIM Contrast Checker** — worth running your dark-mode text/background pairs through this once Phase 1 lands, since dark mode is getting a real pass.
- A **60/30/10 rule** as a concrete anchor for "vibrant but tasteful": roughly 60% neutral/paper canvas, 30% supporting color (the category accents), 10% full-saturation accents (the wordmark, primary buttons, stickers). Useful as literal language to hand Claude Code so "make it feel balanced" has a number attached instead of being a vibe.
- **Stylelint**, optionally, once `design-system.css` exists — it can flag duplicate selectors going forward so this doesn't quietly happen again over six more months of edits.

---

## 8. Sonnet or Opus?

Split it by phase, don't pick one model for the whole project:

**Use Opus for Phase 1 (Prompt 2, the consolidation).** This step touches three large files at once, has to preserve pixel-identical output while moving thousands of lines around, and a mistake here is expensive to unwind (it's the one step where "confidently wrong" is worse than "slow"). It's also a one-time cost — you're not going to do this consolidation every week, so it's worth paying for the more careful model exactly once.

**Use Sonnet for everything else** — Prompts 0, 1, 3–8, and every future small visual ask once Phase 1 is done. These are exactly Sonnet's sweet spot: small, well-scoped, single-file changes where speed and cost matter more than deep architectural judgment, and this is where the bulk of your day-to-day iteration will actually happen. Once `design-system.css` exists as a single source of truth, there's very little left that genuinely needs Opus-level reasoning.

This mirrors your own stated goal: pay for the expensive model once, where it actually matters, then keep the long tail of small tweaks cheap.

---

## 9. Keeping future prompts cheap (the habit, not just the one-time fix)

- One concern per prompt. "Fix the hero video frame" and "fix the dark mode" are two prompts, not one.
- Always name the exact file and selector/function — never "make the site better."
- Explicitly say "do not modify any other file" every time. It's the single sentence that prevents the "asked for one text fix, got three sections deleted" experience from your memory of the Antigravity/Gemini attempt.
- Ask for a diff back, not a full-file rewrite in the response — cheaper for you to review, cheaper in tokens.
- Commit (or at least stage) after every prompt that lands correctly, so a bad one is a revert, not a repair conversation.
- Handle pure copy/text swaps and image-path changes yourself in a text editor — spending an agent call on "change this one word" is the kind of small thing that adds up for no reason.
