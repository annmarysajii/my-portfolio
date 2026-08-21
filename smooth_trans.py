import re

# Fix index.html Warp animation colors
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    "ctx.fillStyle='#FAF8F4';ctx.fillRect(0,0,W,H);",
    "const isDark = document.body.getAttribute('data-theme') === 'dark' || document.documentElement.getAttribute('data-theme') === 'dark'; const bgHex = isDark ? '#111009' : '#FAF8F4'; ctx.fillStyle=bgHex;ctx.fillRect(0,0,W,H);"
)
html = html.replace(
    "ctx.fillStyle=`rgba(250,248,244,${.2+prog*.22})`;",
    "const bgRGB = (document.body.getAttribute('data-theme') === 'dark' || document.documentElement.getAttribute('data-theme') === 'dark') ? '17,16,9' : '250,248,244'; ctx.fillStyle=`rgba(${bgRGB},${.2+prog*.22})`;"
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# Add Page Transition Overlay to all pages
overlay_css = """
<style>
/* Smooth Page Load Overlay */
#page-transition-overlay {
    position: fixed;
    inset: 0;
    background: var(--bg);
    z-index: 999999;
    pointer-events: none;
    opacity: 1;
    transition: opacity 0.8s cubic-bezier(0.4, 0, 0.2, 1);
}
.loaded #page-transition-overlay {
    opacity: 0;
}
</style>
"""

overlay_html = '<div id="page-transition-overlay"></div>'
overlay_js = """<script>
window.addEventListener('load', () => document.body.classList.add('loaded'));
setTimeout(() => document.body.classList.add('loaded'), 800); // safety fallback
</script>"""

for filename in ['portfolio.html', 'project.html', 'index.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if "page-transition-overlay" not in html:
        # insert CSS before </head>
        html = html.replace("</head>", overlay_css + "\n</head>")
        
        # insert HTML after <body>
        html = html.replace("<body>", "<body>\n" + overlay_html)
        
        # insert JS before </body>
        html = html.replace("</body>", overlay_js + "\n</body>")
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)

print("Added smooth transitions and fixed flashbang")
