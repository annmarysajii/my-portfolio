for filename in ['portfolio.html', 'index.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    js_inject = """
    // Make entire cards clickable
    document.querySelectorAll('.card').forEach(card => {
        card.style.cursor = 'pointer';
        card.addEventListener('click', (e) => {
            if (!e.target.closest('a') && !e.target.closest('button')) {
                const link = card.querySelector('a[href]');
                if (link) window.location.href = link.href;
            }
        });
    });
    """
    
    if "Make entire cards clickable" not in html:
        html = html.replace("</script>\n</body>", js_inject + "</script>\n</body>")
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
print("Injected card clickability!")
