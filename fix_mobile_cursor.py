for filename in ['portfolio.html', 'index.html', 'project.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    css_fix = """
  @media (pointer: coarse), (max-width: 768px) {
    #cur { display: none !important; }
    * { cursor: auto !important; }
  }
"""
    if "@media (pointer: coarse)" not in html:
        html = html.replace("</style>", css_fix + "\n  </style>")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)

print("Cursor fixed for mobile!")
