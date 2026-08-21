import re

for filename in ['portfolio.html', 'index.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update coverOverrides for the two new GIFs
    html = html.replace(
        "'ntu-fest': 'assets/portfolio-data/Ntu fest assets/ntufest_portfoliogif.gif.mp4'",
        "'ntu-fest': 'assets/vidtogif/ntu fest banner final.gif'"
    )
    html = html.replace(
        "'keep-yourself-safe': 'assets/vidtogif/keepyourselfsafe_cover.gif.mp4'",
        "'keep-yourself-safe': 'assets/vidtogif/KEEP_YOURSELF_SAFE.gif'"
    )

    # 2. Revert the forced image/video cropping to allow full original aspect ratios (Masonry layout style)
    html = html.replace(
        'style="width:100%;height:100%;object-fit:cover;aspect-ratio:4/3;border-radius:2px;"',
        'style="width:100%;height:auto;border-radius:2px;display:block;"'
    )
    
    # Just in case some had contain:
    html = html.replace(
        'style="width:100%;height:auto;object-fit:contain;"',
        'style="width:100%;height:auto;border-radius:2px;display:block;"'
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
print("Updated GIFs and reverted cropping!")
