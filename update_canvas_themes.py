import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

bgFrame_old = """  function bgFrame(){
    bgX.clearRect(0,0,bW,bH);
    STARS.forEach(s=>{"""

bgFrame_new = """  function bgFrame(){
    bgX.clearRect(0,0,bW,bH);
    const theme = window.currentCanvasTheme;
    const isDarkNow = isDark();
    
    if (theme === 'graphic-design') {
        bgX.strokeStyle = isDarkNow ? 'rgba(240,238,245,0.15)' : 'rgba(17,16,9,0.15)';
        bgX.lineWidth = 1;
        for(let i=0; i<STARS.length; i++) {
            for(let j=i+1; j<STARS.length; j++) {
                const dx = STARS[i].x - STARS[j].x;
                const dy = STARS[i].y - STARS[j].y;
                if (dx*dx + dy*dy < 25000) {
                    bgX.beginPath(); bgX.moveTo(STARS[i].x, STARS[i].y); bgX.lineTo(STARS[j].x, STARS[j].y); bgX.stroke();
                }
            }
        }
    } else if (theme === 'illustration') {
        bgX.strokeStyle = isDarkNow ? 'rgba(217,48,32,0.2)' : 'rgba(217,48,32,0.3)';
        bgX.lineWidth = 2;
        for(let i=0; i<STARS.length-2; i+=3) {
            bgX.beginPath();
            bgX.moveTo(STARS[i].x, STARS[i].y);
            bgX.quadraticCurveTo(STARS[i+1].x, STARS[i+1].y, STARS[i+2].x, STARS[i+2].y);
            bgX.stroke();
        }
    }

    STARS.forEach(s=>{"""

html = html.replace(bgFrame_old, bgFrame_new)

# Update the shapes for these themes
# illustration: draw a small circle at the anchor points
# graphic-design: draw a small blue/solid square (like vector handles)
shape_replace = """    if (theme === 'animation') { 
        ctx.beginPath(); ctx.arc(0, 0, r, 0, Math.PI*2); ctx.fill();
    } else if (theme === 'illustration') { 
        ctx.beginPath(); ctx.arc(0, 0, r*0.7, 0, Math.PI*2); ctx.fill();
    } else if (theme === 'videography') { 
        ctx.beginPath();
        ctx.moveTo(r*1.1, 0); ctx.lineTo(-r*0.6, r*.9); ctx.lineTo(-r*0.6, -r*.9);
        ctx.closePath(); ctx.fill();
    } else if (theme === 'graphic-design') { 
        ctx.fillStyle = '#1850A8'; // blue vector handle
        ctx.fillRect(-r*0.8, -r*0.8, r*1.6, r*1.6);
        ctx.strokeStyle = isDark() ? '#fff' : '#000';
        ctx.lineWidth = 1;
        ctx.strokeRect(-r*0.8, -r*0.8, r*1.6, r*1.6);
    } else if (theme === 'music') {"""

# We need to replace the old shape logic carefully using regex
old_shape_logic = r"if \(theme === 'animation'\) \{.*?\} else if \(theme === 'music'\) \{"
html = re.sub(old_shape_logic, shape_replace, html, flags=re.DOTALL)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated canvas backgrounds for illustration and graphic design")
