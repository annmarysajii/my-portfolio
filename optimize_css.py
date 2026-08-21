css_additions = """
/* --- MOBILE & TOUCH OPTIMIZATIONS --- */
@media (hover: none), (max-width: 768px) {
    body, button, a, .dl-btn, .fsub, .pill-toggle {
        cursor: auto !important;
    }
    #cur {
        display: none !important;
    }
    #bg-c {
        display: none !important;
    }
    .sec#graphic-design::before,
    .sec#illustration::before {
        display: none !important;
        animation: none !important;
    }
    /* Revert to simple colors without hover transitions to prevent mobile tap lag */
    .sec#animation .sec-title:active { transform: none; color: inherit; }
    .sec#graphic-design .sec-title:active { -webkit-text-stroke: 0; color: inherit; text-shadow: none; }
    .sec#videography .sec-title:active { animation: none; }
}
"""

with open('css/motion.css', 'a', encoding='utf-8') as f:
    f.write(css_additions)
print("Added mobile optimizations to motion.css")
