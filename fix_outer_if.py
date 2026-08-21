with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_cond = "if (id === 'gobunny' || id === 'green-arrow' || id === 'nangele' || id === 'original-tracks') {"
new_cond = "if (id === 'gobunny' || id === 'green-arrow' || id === 'nangele' || id === 'original-tracks' || id === 'wellbeing-planner' || id === 'ntu-fest') {"

html = html.replace(old_cond, new_cond)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed outer if condition!")
