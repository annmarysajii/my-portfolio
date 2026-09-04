---
target: about section
total_score: 24
max_score: 32
na_heuristics: 7,10
p0_count: 0
p1_count: 3
p2_count: 2
target_identity: "file:C:\\Users\\dipuj\\workspace\\annmary-portfolio\\portfolio.html#about"
timestamp: 2026-09-03T17-58-15Z
slug: portfolio-html-about
closed: false
---
# Critique: About Section — portfolio.html (#about)

## Design Health Score
Mode: Experience (portfolio). Heuristics 7 and 10 n/a.

| # | Heuristic | Score | Key Issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 3 | Buttons signal state; empty widget panel could tell more |
| 2 | Match System / Real World | 4 | Notebook / lanyard / desk vocabulary carried through |
| 3 | User Control and Freedom | 3 | All drawers close; no traps |
| 4 | Consistency and Standards | 2 | New spec block styled generic; rest of section is stationery |
| 5 | Error Prevention | 4 | Nothing destructive |
| 6 | Recognition Rather Than Recall | 3 | Object icons clear; widget panel empty state passive |
| 7 | Flexibility and Efficiency | n/a | No power-user path expected |
| 8 | Aesthetic and Minimalist Design | 3 | 7 sub-11px text elements; three widget buttons look sparse where 5 fit |
| 9 | Error Recovery | 4 | No error surfaces |
| 10 | Help and Documentation | n/a | Not applicable to About |

Total: 24/32 (75%) — Good. Pulled down by heuristics 4 and 8.

## Design Specificity Verdict
High. The notebook conceit is coherent: STUDIO NOTEBOOK kicker, ransom-note
name card with lanyard clip, dashed tear-here perforations top and bottom,
desk-scattered objects with hover notes. Nothing about the section reads as
generic. The credentials block introduced in the previous pass sits inside
this vocabulary but does not yet speak it: it's a flat dl on the red ground.

## What's Working
1. Credentials visible without a click (recruiter-scannable) — previously
   hidden behind 5 objects, now surfaced.
2. Desk-object scatter with per-object drawer notes — cheerful, in-world,
   avoids the classroom feel that the field-notes system had.
3. Two-column intro: text on the left, name-tag on the right, with the
   headline "One person. Many mediums." carrying the whole argument in
   six words.
4. Tear-here perforations at top and bottom hand the section off to the
   Music and Contact sections physically rather than as flat colour swaps.

## Priority Issues

[P1] Six spec labels render at 10.56px and the "A few facts" heading at
10.88px. Both below the 11px readability threshold established in the
hero critique.
Fix: raise `.about-spec dt` to 0.72rem and `.bp-facts-heading` similarly.
Applied in this pass.

[P1] Spec block visual language does not match the section. Everything else
uses stitching, tape, torn edges, sticker-stamped labels. The spec block
uses solid hairline rules on flat red — reads as an afterthought overlay
rather than a page of the notebook.
Fix: dashed rule pattern echoing .bp-tear at the top and between rows so
the spec sits in the notebook rather than on top of it. Applied.

[P1] Empty state text of the widget panel reads "☝ pick an object to open
it". A recruiter who does not click never learns what the drawers contain,
so the widget adds nothing to a passive scan.
Fix: replace with a preview that lists the drawer names: "Toolkit ·
Words · Awards — open one to see what's inside". Applied.

[P2] Three widget objects (Toolkit, Words, Awards) look sparse in a row
that was designed for five (the School and Now drawers were removed in
the previous pass because their contents are now in the visible spec).
Fix: either rebalance to fill a smaller row (two-up + one-up) or add a
fourth drawer that is genuinely different from the visible facts —
candidates: Fun facts (currently only reachable via the name-card back);
Reading; Studio setup.

[P2] Section is 1874px tall on desktop. Vertical rhythm is loose in the
middle band between the desk scatter and the widget row. The scatter
container is fixed height with absolute-positioned objects, so its air
is intentional; the invite line's margins are the compressible piece.
Fix: reduce top/bottom margins on `.bp-invite` and `.bp-widget` by ~10%.

## What NOT to change
Per Annmary's brief: keep the ransom-note wordmark, keep the name card as-is
(including the OPEN FOR WORK stamp and the stickers), keep the star cursor,
keep the drawer/passport metaphor. The critique's fixes preserve all of the
above. No branding element is removed by this pass.
