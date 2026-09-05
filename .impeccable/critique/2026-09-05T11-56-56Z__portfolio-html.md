---
target: portfolio.html (full page, UI + key-work discoverability)
total_score: 23
max_score: 32
na_heuristics: 7,10
p0_count: 0
p1_count: 3
target_identity: "file:C:\\Users\\dipuj\\workspace\\annmary-portfolio\\portfolio.html"
target_fingerprint: "sha256:92988a13463145e798a614cd5f8c38de9d2f2dd131ec8c1bae8c89a4c18a9f51"
target_path: "C:\\Users\\dipuj\\workspace\\annmary-portfolio\\portfolio.html"
timestamp: 2026-09-05T11-56-56Z
slug: portfolio-html
closed: true
---
Method: dual-agent (Assessment A: design review · Assessment B: detector + browser evidence, run as two isolated sub-agents)

## Design Health Score

| # | Heuristic | Score | Key Issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 3 | Passport counter gives good progress feedback, but nothing in the nav highlights which of the 5 discipline sections you're currently scrolled through on a very long page. |
| 2 | Match System / Real World | 4 | Desk/notebook/tape/passport metaphor is legible and consistently applied throughout. |
| 3 | User Control and Freedom | 3 | Drawers, playground toys, and the passport modal all have explicit close controls; "skip to work" from the long hero wasn't confirmed to exist. |
| 4 | Consistency and Standards | 3 | Lead-card pattern is genuinely reused across 4/5 sections; breaks down at the nav, where "Work" gives no visual cue it's a dropdown. |
| 5 | Error Prevention | 3 | Contact form marks required fields before submission is attempted. |
| 6 | Recognition Rather Than Recall | 2 | The Work dropdown only reveals on hover/focus with zero static affordance (no chevron, no indicator) — nothing signals "more here" to a first-time visitor. |
| 7 | Flexibility and Efficiency | n/a | One-pass browsing experience, not a repeat-use tool; power-user shortcuts aren't the relevant axis here. |
| 8 | Aesthetic and Minimalist Design | 3 | Deliberately maximalist collage aesthetic is intentional and mostly controlled, but the Videography grid leaves an orphaned 4th card with a large dead gap beside it. |
| 9 | Error Recovery | 2 | No invalid-input flow was exercised, and no inline-validation styling was observed anywhere in the DOM at rest — likely weak, not confidently scored. |
| 10 | Help and Documentation | n/a | Not applicable to a portfolio "Experience" surface — no workflow complex enough to need documenting. |
| **Total** | | **23/32** | **Good (72%)** |

## Design Specificity Verdict

**LLM assessment:** Specific to this site, not generic template feedback. The desk/notebook/drawer/passport metaphor is fully built out and consistently themed — lead cards, tape, drawers, and the Studio Passport dock are bespoke, reused components, not boilerplate cards-in-a-grid. The four styled `.lc--*` lead cards (Keep Yourself Safe, Jasmine, VIPCOLOR, Acorn & Oak) each look like they belong to that specific project rather than a shared template stretched thin.

**Deterministic scan:** The CLI scan ran in **degraded mode** (HTML parser modules unavailable, fell back to regex matching — findings are an undercount, not a clean bill of health) and still found 43 static findings; the live-DOM pass in the browser found 157 flagged elements / 176 findings. The volume is large, but a lot of it is expected noise for a maximalist, component-heavy design:

- **Likely real, worth fixing:** widespread undersized text (57 instances below an 11px floor, another 25 in the 11-12px "tiny-text" band), a handful of concrete contrast failures, 5 instances of a skipped heading level (h2 → h4, no h3), and a repeated console warning for a missing "instagram" Lucide icon (18×).
- **Likely false positives given this site's documented design system:** 39 "nested-cards" flags mostly correspond to the intentional badge/stamp/passport component system Assessment A called out as a strength, not the generic template smell the rule targets; the "codex-grid-background" advisory is the site's own documented 24px graph-paper token; "pulsing-dot" is the intentional idle-ball playground toy; "repeating-stripes-gradient" is very likely the tape/washi decoration. One flagged "ai-color-palette" cyan gradient on `.hero-fabric-swatch` is worth a manual look specifically because it's the one that might genuinely clash with this project's own documented red/blue/yellow-plus-shared-secondaries color rule, unlike the others.
- **Needs a manual check, not a clear call either way:** a "low-contrast" flag at an alarming 1.0:1 between two near-identical off-whites (possibly a mismatched selector pairing, not real rendered text); the 4 "broken-image" CLI hits (given degraded/regex-mode scanning, these may be template markup rather than live broken tags); a "buried-raster" `<img>` sitting at opacity 0 under "Original Tracks — Interactive Sound Lab" (could be intentional pre-fade state or a real bug); and 4 "gpt-thin-border-wide-shadow" flags on the Keep Yourself Safe lead card, which is worth checking against this project's own written rule ("no 1px light border on a photograph — it reads as a stray outline; use shadow").

**Visual overlays:** injection succeeded in an isolated sub-agent's own browser tab during this run, but that tab has since been closed — there is no overlay currently visible in your browser to look at. The findings above are the console/script output captured before it closed.

## Overall Impression

The site's structural hierarchy device — the lead card — is doing real work and is the single strongest thing about how "key work" surfaces today: it's first in the DOM, visually distinct, and impossible to scroll past without noticing. The gap is one level up: nothing above the section level tells a visitor *which section's lead, or which project overall, is the best of the best*. The nav's new discipline dropdown (added recently) solves "where are the sections" but not "which one should I look at first," which is exactly the question a recruiter with 15 seconds is actually asking. Alongside that, a real volume of undersized text turned up that a manual pass wouldn't have caught systematically.

## What's Working

1. **The lead-card pattern is a genuine hierarchy win.** In every section that has one, it's structurally first, visually distinct (own ground color, wider column, a five-step process strip), and labeled — a visitor scanning past a section header cannot miss it.
2. **Section-specific lead-card styling is disciplined.** Keep Yourself Safe (dark, filmic), Jasmine (burgundy/gold), VIPCOLOR (industrial navy), and Acorn & Oak (olive/cream) each read as belonging to that project, not a shared template.
3. **Music's deliberate lack of a lead card is a rare, documented restraint** — most portfolios over-apply their own pattern everywhere; this one resisted that on the one section where a flat grid was the right call.

## Priority Issues

**[P1] The nav's discipline dropdown shows *where* the sections are but not *which project is the best of the best***
- **Why it matters:** This is the exact discoverability question you asked about. "Work" reveals no static affordance (no chevron, hover/focus-only) so a first-time visitor has no visual reason to open it at all, and once open it lists all 5 disciplines as flat, equally-weighted links in page order — no steer toward your single strongest credential (Keep Yourself Safe's Annecy 2025 selection currently lives in body-copy paragraph three, not the kicker or a badge). A recruiter can find *a* section but not *the* standout without reading everything.
- **Fix:** Add a static caret so "Work" visibly reads as a dropdown without hovering. Consider a "Start with the reel" or featured-project shortcut near the hero CTAs, and promote your strongest external credential (Annecy) to a kicker/badge instead of paragraph three, on at least the Animation lead card.
- **Suggested command:** `/impeccable clarify`

**[P1] Studio Passport dock overlaps About-section credentials on mobile**
- **Why it matters:** The fixed-position dock button sits directly on top of the "Status" row text in `.about-spec` on a 375px viewport — exactly the credentials block your own project notes say exists specifically so a recruiter scanning quickly doesn't have to open a drawer to see availability. A floating gamification badge covering that line undermines its whole purpose on the device class most portfolio traffic arrives on.
- **Fix:** Extend the existing `[data-dock-avoid]` / `initPassportDockYield` mechanism (already watching hero elements) to the `.about-spec` block, or reposition the dock on mobile breakpoints specifically.
- **Suggested command:** `/impeccable harden`

**[P1] Widespread undersized and tiny UI text**
- **Why it matters:** The live-DOM scan found 57 elements below an 11px legibility floor and another 25 in an 11-12px "tiny-text" band — spread across motion-lab tags, margin notes, and other small-print UI. This is a broad, mechanically-verified legibility gap a manual pass wouldn't systematically catch, and it runs against your own project's standing rule to verify contrast/accessibility numerically rather than by eye.
- **Fix:** Sweep the flagged selectors (motion-lab pg-tag spans, margin-note-inner spans, and similar small-print elements) and raise them to at least 11-12px, or confirm which are truly decorative and can stay small.
- **Suggested command:** `/impeccable audit`

**[P2] Videography grid leaves an orphaned card and a dead gap**
- **Why it matters:** Below the VIPCOLOR lead card, the grid renders 3 cards in one row and a 4th alone in the next, leaving roughly half a row visibly empty at desktop width. It reads as a layout bug, not a design choice, and undercuts the polish evident everywhere else.
- **Fix:** Add a 5th card, let the last card span two columns, or center the final short row instead of left-aligning it into visible emptiness.
- **Suggested command:** `/impeccable polish`

**[P2] A handful of concrete contrast failures**
- **Why it matters:** The live scan found real contrast violations, including `#c08800` on `#f5edd8` at 2.7:1 (needs 3:1 for large text) — a direct, numeric violation of your own project's standing rule to verify contrast rather than eyeball it. One additional flag at a suspicious 1.0:1 between two near-identical off-whites needs a manual look before fixing (it may be a mismatched selector, not real rendered text).
- **Fix:** Verify each flagged pairing against WCAG AA (4.5:1 body / 3:1 large text) and adjust the ones that are genuinely failing.
- **Suggested command:** `/impeccable audit`

## Persona Red Flags

**Jordan (Confused First-Timer):** Lands on a busy, personality-forward hero and scrolls past quick-facts, a resume drawer, and a download bar before the first actual project appears — fine once, but with no nav affordance signaling "there's a shortcut to my best work," Jordan's only path to your strongest piece is scrolling the whole page or accidentally hovering "Work." Jordan is also handed unexplained vocabulary ("Studio Passport," "Playground") with no legend at first contact.

**Casey (Distracted Mobile User):** Hits the passport-dock-over-credentials overlap in About directly — the exact section meant to answer "is she hireable/available," partially covered by a floating badge. Casey also disproportionately feels the undersized-text findings, since small text shrinks further relative to thumb-scale interaction. The hamburger's indented sub-list (added recently) correctly substitutes for hover on the dropdown, though — that part is handled well.

**Riley (Deliberate Stress Tester):** Would find the orphaned Videography grid card and immediately suspect other grids gap at intermediate viewport widths (900-1100px) too, since a masonry system that breaks at one breakpoint rarely stays clean at every other one — worth a wider sweep across all 5 section grids.

## Minor Observations

- Category pill dot-colors in the hero don't map to the `--sec-*-accent` tokens used later in each section — a small missed reinforcement opportunity.
- The before/after comparison slider on `project.html` is a genuinely strong, specific interaction worth reusing on other technical case studies, not just noting once.
- 5 instances of a skipped heading level (h2 → h4, missing h3) turned up in the live scan — a real semantic/accessibility gap the static scan didn't catch.
- 18 repeated console warnings for a missing "instagram" Lucide icon in the Contact footer — low severity, but visible polish gap and worth a quick swap to a working icon name.
- "Also from the build" (project.html's catch-all for unmatched groups) wasn't directly spot-checked this run — worth a look given how easily a `match` typo could route work there silently.

## Questions to Consider

1. If the lead card exists to say "this is the standout," why does your single most externally validated credential (Annecy 2025 selection) live in body-copy paragraph three instead of the kicker or a badge — would a recruiter actually notice it before deciding to keep scrolling or bounce?
2. The nav dropdown organizes by discipline, which mirrors how you think about your practice — but does it mirror how a recruiter decides where to click first? Would a "Start here" or "most awarded" shortcut get someone to your strongest work faster than an alphabetical-by-discipline list?
3. Music was deliberately left without a lead card as a hierarchy statement — but is "no lead" distinguishable, to a first-time visitor, from "ran out of best work here"? Is there a way to signal the restraint is a choice rather than a gap?
