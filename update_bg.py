import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The new draw function
new_draw = """
  window.currentCanvasTheme = 'star';
  function drawShape(ctx,x,y,r,rot,color){
    ctx.save();ctx.translate(x,y);
    if(window.currentCanvasTheme !== 'music') ctx.rotate(rot); // don't rotate notes so they stay upright
    ctx.fillStyle=color;
    
    const theme = window.currentCanvasTheme;
    if (theme === 'animation') { 
        ctx.beginPath(); ctx.arc(0, 0, r, 0, Math.PI*2); ctx.fill();
    } else if (theme === 'illustration') { 
        ctx.beginPath();
        ctx.moveTo(0, -r*1.2); ctx.quadraticCurveTo(r*.3, -r*.3, r*1.2, 0);
        ctx.quadraticCurveTo(r*.3, r*.3, 0, r*1.2);
        ctx.quadraticCurveTo(-r*.3, r*.3, -r*1.2, 0);
        ctx.quadraticCurveTo(-r*.3, -r*.3, 0, -r*1.2);
        ctx.fill();
    } else if (theme === 'motion') { 
        ctx.beginPath();
        ctx.moveTo(r*1.1, 0); ctx.lineTo(-r*0.6, r*.9); ctx.lineTo(-r*0.6, -r*.9);
        ctx.closePath(); ctx.fill();
    } else if (theme === 'brand') { 
        ctx.fillRect(-r*0.8, -r*0.8, r*1.6, r*1.6);
    } else if (theme === 'music') { 
        ctx.font = `600 ${r*2.8}px "General Sans", sans-serif`;
        ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText('♪', 0, 0);
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
"""

# Replace the old function
html = re.sub(r'function drawStar\(ctx,x,y,r,rot,color\)\{.*?\n\s+\}', new_draw.strip(), html, flags=re.DOTALL)

# Replace the call
html = html.replace('drawStar(bgX,s.x,s.y,sz,s.rot,color);', 'drawShape(bgX,s.x,s.y,sz,s.rot,color);')

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('scripts/motion.js', 'a', encoding='utf-8') as f:
    f.write("""

    // 5. Thematic Falling Backgrounds
    const bgObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                if (entry.target.classList.contains('hero')) {
                    window.currentCanvasTheme = 'star';
                } else if (entry.target.id === 'animation') {
                    window.currentCanvasTheme = 'animation';
                } else if (entry.target.id === 'illustration') {
                    window.currentCanvasTheme = 'illustration';
                } else if (entry.target.id === 'motion') {
                    window.currentCanvasTheme = 'motion';
                } else if (entry.target.id === 'brand') {
                    window.currentCanvasTheme = 'brand';
                } else if (entry.target.id === 'music') {
                    window.currentCanvasTheme = 'music';
                }
            }
        });
    }, { threshold: 0.4 });
    
    document.querySelectorAll('.sec, .hero').forEach(el => bgObserver.observe(el));
""")

print("Updated canvas and bg observer")
