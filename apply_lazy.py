for filename in ['project.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    html = html.replace('<img class="media-el" src="${file}"', '<img class="media-el" src="${file}" loading="lazy" decoding="async"')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
print("Applied lazy loading to project.html!")
