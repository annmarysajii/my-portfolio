---
target: hero page
total_score: 23
max_score: 32
na_heuristics: 7,10
p0_count: 0
p1_count: 3
target_identity: "file:C:\\Users\\dipuj\\workspace\\annmary-portfolio\\portfolio.html#hero"
timestamp: 2026-09-01T16-30-53Z
slug: portfolio-html-hero
closed: true
---
# Critique: Hero Section — portfolio.html (#hero, lines 13532-13714)

## Design Health Score
Mode: Experience (portfolio). Heuristics 7 and 10 n/a.

| # | Heuristic | Score | Key Issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 3 | Toggles/tabs give clear feedback; minor gap on reel-tab pressed state |
| 2 | Match System / Real World | 4 | In-world vocabulary throughout, nothing generic leaks in |
| 3 | User Control and Freedom | 3 | Lightbox has a real close; no true blocking flows in a hero |
| 4 | Consistency and Standards | 1 | Hero CSS forked its own color tokens across 4+ superseding !important blocks |
| 5 | Error Prevention | 3 | No destructive actions; muted-autoplay video, avatar onerror fallback |
| 6 | Recognition Rather Than Recall | 3 | Click-to-reveal tiles have no persistent affordance once nudge has played |
| 7 | Flexibility and Efficiency | n/a | No power-user path expected |
| 8 | Aesthetic and Minimalist Design | 3 | Detector confirms 4 nested-card instances, 7 sub-11px text elements |
| 9 | Error Recovery | 3 | Video onerror degrades gracefully |
| 10 | Help and Documentation | n/a | Not applicable to a hero |

Total: 23/32 (72%) -> Good. Pulled down almost entirely by heuristic 4.

## Design Specificity Verdict
High. Sketchbook conceit carried through consistently (stitched spine gradient,
torn-paper wordmark entrance, 4 distinct pinned-object stickers, discovery
nudge on metric tiles). CLI detector ran DEGRADED (regex fallback) and found
0 hits inside the hero across 36 site-wide findings; browser DOM/computed-
style overlay found 21 hits across 20 hero elements the regex pass cannot
see (undersized text, low contrast, nested cards, layout-transition). False
positive: broken-image at line 14156 is a canvas-capture lightbox target
populated on click, not an unfilled placeholder, and is outside hero range.

## Overall Impression
Hero identity is genuinely strong and distinctive. What holds it back is
structural drift from isolated refinement passes: properties redeclared
2-4 times across the file with the newest layer winning, and the hero has
quietly stopped using the site's own design tokens.

## What's Working
1. Torn-paper wordmark entrance (heroLogoWipe/heroLogoSettle) - convincing
   assembling-itself animation with a documented reduced-motion fallback.
2. Discovery-nudge on click-to-reveal metrics - delayed to not fight the
   tile's own reveal, fires once, documented reasoning for SVG targeting.
3. Dark-mode handling of collage assets - sketchbook goes near-black with a
   glow-drop-shadow instead of re-tinting the flattened wordmark asset.

## Priority Issues

[P1] Hero+footer never fits one viewport on common laptop sizes, contradicting
the code's own stated goal ("fit the full spread in one viewport" comment).
.hero-foot renders below the fold at both 1366x768 and 1280x800.
Fix: re-budget vertical rhythm against a real ~768-800px target height.
Suggested command: /impeccable layout

[P1] Fixed Studio Passport dock overlaps real hero content. Covers "Scroll to
explore" text and truncates language list at ~926x914; sits over the third
metric tile's label on mobile (375px). Confirmed via getBoundingClientRect
overlap.
Fix: scroll-aware offset respecting .hero-foot's box, or reserved safe space.
Suggested command: /impeccable harden

[P1] Several hero text elements are too small/low-contrast to read comfortably.
.seal-sub renders at 6.4px, .seal-title at 10.88px, three .metric-lbl at
10.24px, .d-pill-tag at 10.4px and 4.1:1 contrast (AA needs 4.5:1).
Fix: raise to >=11px, fix .d-pill-tag contrast.
Suggested command: /impeccable typeset

[P2] Hero CSS forked its own color tokens (hardcoded hex close-but-not-
identical to :root tokens across 4+ duplicate blocks); detector independently
confirms literal nested-card pattern on 4 hero elements.
Fix: consolidate onto :root tokens, delete superseded blocks, flatten nesting.
Suggested command: /impeccable harden

[P2] "Resume" nav CTA clipped on 375px mobile width - only "Resu" visible,
37px past viewport edge.
Fix: keep logo single-line at mobile width, or shrink CTA padding.
Suggested command: /impeccable harden

## Persona Red Flags
Jordan (Confused First-Timer): No persistent affordance that metric tiles
are interactive once the one-time nudge has played; likely never discovers
the click-to-reveal facts.
Casey (Distracted Mobile User): "Resume" CTA cut off mid-word; Studio
Passport widget covers the "2nd - NTU - Imperial Design-a-thon" achievement.
Riley (Deliberate Stress Tester): Hero+footer never actually fits one
viewport across 768/800/900px despite the source comment claiming that goal;
.hero-sketchbook declared 4+ times with escalating !important layers.

## Minor Observations
- .hero padding-top/min-height rule duplicated byte-for-byte at two locations.
- .hero-fabric-swatch gingham technique (crossed repeating-linear-gradients,
  no image asset) worth reusing elsewhere.
- .disc and reel-tab/expand/sound buttons lack custom :focus-visible unlike
  .metric-toggle/.card elsewhere on the page.
- Em-dash count: 27 by source regex vs 25 by rendered-text scan (not a bug).

## Questions to Consider
- Was the Studio Passport dock ever checked against the hero's own footer?
- Are the repeated "refinement pass" comments intentional history or debt?
- Was the taller-than-768px tuning viewport a deliberate target device?
