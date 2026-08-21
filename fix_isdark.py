import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace isDark() with the actual logic inline
html = html.replace('isDark()', "(document.documentElement.getAttribute('data-theme') === 'dark')")
# Also fix the `isDarkNow=isDark();`
html = html.replace('isDarkNow=isDark();', "isDarkNow=(document.documentElement.getAttribute('data-theme') === 'dark');")

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed isDark error")
