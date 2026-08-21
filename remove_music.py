for filename in ['index.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    import re
    # Remove the musicBtn from index.html
    html = re.sub(
        r'<button class="music-toggle pill-toggle" id="musicBtn"[^>]*>[\s\S]*?</button>',
        '',
        html
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
print("Removed music toggle from index.html!")
