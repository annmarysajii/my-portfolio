with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace("htmlStr += `</div></div>`;\n} else if (id === 'green-arrow') {", "htmlStr += `</div></div>`;\n} else if (id === 'green-arrow') {")
# Wait, I just need to add the closing brace.
html = html.replace("htmlStr += `</div></div>`;\n} else if (id === 'green-arrow')", "htmlStr += `</div></div>`;\n                  } else if (id === 'green-arrow')")

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
