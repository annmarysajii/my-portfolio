import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace footer link
old_footer_link = r'<a href="game.html" class="foot-egg">Curious what happens when you go offline\?</a>'
new_footer_link = r"""
<a href="game.html" class="foot-egg" aria-label="Hidden game">
    <i data-lucide="ghost"></i>
</a>
<style>
.foot-egg {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    color: var(--ink05);
    transition: color 0.3s, transform 0.3s;
    animation: idle-bounce 15s infinite;
    text-decoration: none;
}
.foot-egg:hover {
    color: var(--ink);
    transform: scale(1.1);
    animation: none;
}
@keyframes idle-bounce {
    0%, 90% { transform: translateY(0); }
    92% { transform: translateY(-5px) rotate(-10deg); }
    94% { transform: translateY(0) rotate(10deg); }
    96% { transform: translateY(-3px) rotate(-5deg); }
    98% { transform: translateY(0) rotate(0); }
    100% { transform: translateY(0); }
}
</style>
"""
html = re.sub(old_footer_link, new_footer_link, html)

# Inject vague line into About section
old_about = 'categories and start talking to each other.</p>'
new_about = 'categories and start talking to each other. <span style="opacity:0.8; font-style:italic;">Bored? There might be something to do about that.</span></p>'
if old_about in html:
    html = html.replace(old_about, new_about)

# Inject console.log at the end of the body
console_log_script = """<script>
    console.log("%cTry pressing space...", "color: #D02F5A; font-size: 14px; font-weight: bold; font-family: monospace;");
</script>
</body>"""
html = html.replace('</body>', console_log_script)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated portfolio.html successfully")
