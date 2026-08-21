import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the mangled section with the correct version
old_mangled = """  window.currentCanvasTheme = 'star';
  function drawShape(ctx,x,y,r,rot,color){
    ctx.save();ctx.translate(x,y);
    if(window.currentCanvasTheme !== 'music') ctx.rotate(rot); // don't rotate notes so they stay upright
    ctx.fillStyle=color;
    
    const theme = window.currentCanvasTheme;
        if (theme === 'animation') { 
        ctx.beginPath(); ctx.arc(0, 0, r, 0, Math.PI*2); ctx.fill();
    } else if (theme === 'illustration') {
          // removed messy lines as requested
      }
        }
    } else if (theme === 'illustration') {
          // removed messy lines as requested
      }

    STARS.forEach(s=>{"""

new_fixed = """  window.currentCanvasTheme = 'star';
  function drawShape(ctx,x,y,r,rot,color){
    ctx.save();ctx.translate(x,y);
    if(window.currentCanvasTheme !== 'music') ctx.rotate(rot); // don't rotate notes so they stay upright
    ctx.fillStyle=color;
    
    const theme = window.currentCanvasTheme;
    if (theme === 'animation') { 
        ctx.beginPath(); ctx.arc(0, 0, r, 0, Math.PI*2); ctx.fill();
    } else if (theme === 'illustration') { 
        ctx.font = `600 ${r*3}px sans-serif`;
        ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText('🖌️', 0, 0);
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
    } else if (theme === 'music') { 
        ctx.font = `600 ${r*2.8}px "General Sans", sans-serif`;
        ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText('🎵', 0, 0);
    } else { 
        ctx.beginPath();
        for(let i=0;i<10;i++){
            const a=(i*Math.PI/5)-Math.PI/2;
            const rad=i%2===0?r:r*.42;
            i===0?ctx.moveTo(Math.cos(a)*rad,Math.sin(a)*rad):ctx.lineTo(Math.cos(a)*rad,Math.sin(a)*rad);
        }
        ctx.closePath(); ctx.fill();
    }
    ctx.restore();
  }

  function bgFrame(){
    bgX.clearRect(0,0,bW,bH);
    const theme = window.currentCanvasTheme;
    const isDarkNow = isDark();
    
    if (theme === 'graphic-design') {
        bgX.strokeStyle = isDarkNow ? 'rgba(240,238,245,0.12)' : 'rgba(17,16,9,0.1)';
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
        // removed messy lines as requested
    }

    STARS.forEach(s=>{"""

# I need to use regex because spacing might be slightly off.
# Let's just find `window.currentCanvasTheme = 'star';` up to `STARS.forEach(s=>{`
pattern = r"window\.currentCanvasTheme = 'star';.*?STARS\.forEach\(s=>\{"
html = re.sub(pattern, new_fixed, html, flags=re.DOTALL)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed corruption")
