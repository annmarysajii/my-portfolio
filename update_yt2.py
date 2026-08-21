import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Change the embed logic
old_yt = """if (window.location.protocol === 'file:') {"""
new_yt = """if (window.location.protocol === 'file:' || window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {"""
html = html.replace(old_yt, new_yt)

old_nocookie = """embedUrl = `https://www.youtube-nocookie.com/embed/${ytId}?rel=0&modestbranding=1`;"""
new_nocookie = """embedUrl = `https://www.youtube.com/embed/${ytId}?rel=0&modestbranding=1`;"""
html = html.replace(old_nocookie, new_nocookie)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated YouTube fallback to catch localhost and reverted nocookie")
