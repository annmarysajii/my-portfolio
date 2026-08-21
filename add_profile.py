import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Locate the about text
old_about = """<p class="about-label">About</p>
     <h2 class="about-h rv d1">One person.<br><em>Many mediums.</em></h2>"""

new_about = """<p class="about-label">About</p>
     <div style="display:flex; flex-wrap:wrap; gap:2rem; align-items:flex-start;">
       <div style="flex: 1 1 400px;">
         <h2 class="about-h rv d1">One person.<br><em>Many mediums.</em></h2>"""

html = html.replace(old_about, new_about)

# Locate the end of the text
old_end = """<div class="fact"><span class="f-em"><i data-lucide="message-square"></i></span><span class="f-lbl">Languages</span><span class="f-val">English, Malayalam, Hindi</span></div>
      </div>
     </div>"""

new_end = """<div class="fact"><span class="f-em"><i data-lucide="message-square"></i></span><span class="f-lbl">Languages</span><span class="f-val">English, Malayalam, Hindi</span></div>
      </div>
       </div>
       <div style="flex: 1 1 250px; display:flex; justify-content:center; padding-top:2rem;">
         <img src="assets/portfolio-data/My profile/me avatar.png" style="width:100%; max-width:350px; border-radius:1rem; transform:rotate(2deg); border:8px solid white; box-shadow:0 10px 30px rgba(0,0,0,0.1);">
       </div>
     </div>
     </div>"""

html = html.replace(old_end, new_end)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Added profile picture to About section")
