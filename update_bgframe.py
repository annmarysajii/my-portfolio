import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

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

html = re.sub(r'function bgFrame\(\)\{\s*bgX\.clearRect\(0,0,bW,bH\);\s*STARS\.forEach\(s=>\{', bgFrame_new.strip(), html)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated bgFrame in portfolio.html")
