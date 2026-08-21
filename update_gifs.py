import re

# 1. Update cover logic in portfolio.html and index.html
override_logic = """          const coverOverrides = {
              'ntu-fest': 'assets/portfolio-data/Ntu fest assets/ntufest_portfoliogif.gif.mp4',
              'gobunny': 'assets/portfolio-data/GoBunny_brand/GO BUNNY.png',
              'keep-yourself-safe': 'assets/vidtogif/keepyourselfsafe_cover.gif.mp4',
              'dear-friend': 'assets/vidtogif/dear_friend.gif',
              'a-stray-dog': 'assets/vidtogif/A-STRAY-DOG.gif',
              'chase': 'assets/vidtogif/The_chase.gif',
              'socrat-ai': 'assets/vidtogif/HDR_SOCRATVIDEO.gif',
              'vipcolor-video': 'assets/vidtogif/vipcolor_vid.gif',
              'gcf-documentary': 'assets/vidtogif/GCF VIDEO FOR ORIENTATION.gif',
              'music-district-video': 'assets/vidtogif/musicdistrict_projection.gif',
              'short-film-score': 'assets/vidtogif/solace_shortfilmscore.gif'
          };
          if (coverOverrides[id]) file = coverOverrides[id];"""

for filename in ['portfolio.html', 'index.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the old overrides block
    old_ifs = """          if (id === 'ntu-fest') file = 'assets/portfolio-data/Ntu fest assets/ntufest_portfoliogif.gif.mp4';
            if (id === 'gobunny') file = 'assets/portfolio-data/GoBunny_brand/GO BUNNY.png';"""
    
    if old_ifs in html:
        html = html.replace(old_ifs, override_logic)
    elif "const coverOverrides =" not in html:
        # Fallback if whitespace differs
        html = re.sub(
            r'if \(id === \'ntu-fest\'\) file = [^;]+;\s*if \(id === \'gobunny\'\) file = [^;]+;',
            override_logic,
            html
        )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)


# 2. Update the Short Film Score title in project.html
with open('project.html', 'r', encoding='utf-8') as f:
    proj_html = f.read()

proj_html = proj_html.replace(
    "title:'Short Film Score',",
    "title:'Solace — Short Film Score',"
)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(proj_html)

print("Covers updated and Solace renamed!")
