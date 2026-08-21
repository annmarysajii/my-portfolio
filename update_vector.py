import re

with open('css/motion.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_vector = """@keyframes vector-build {
    0% { color: transparent; -webkit-text-stroke: 1.5px var(--yel); }
    40% { color: transparent; -webkit-text-stroke: 1.5px var(--ink); }
    100% { color: var(--ink); -webkit-text-stroke: 0px transparent; }
}"""

new_vector = """@keyframes vector-build {
    0% { color: transparent; -webkit-text-stroke: 2.5px #1850A8; }
    50% { color: transparent; -webkit-text-stroke: 2.5px var(--ink); }
    100% { color: var(--ink); -webkit-text-stroke: 0px transparent; }
}"""

css = css.replace(old_vector, new_vector)

with open('css/motion.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated vector build animation")
