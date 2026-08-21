import re

with open('game.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make the moon white
html = html.replace("ctx.fillStyle = '#0a080c'; // Slightly off-bg to distinguish", "ctx.fillStyle = '#E5E2EC'; // Light moon fill")
html = html.replace("ctx.strokeStyle = 'rgba(240,238,245,0.4)';", "ctx.strokeStyle = '#D93020'; // Red moon edge")

# Replace crater drawing
old_crater = """        if (o.variant === 'crater') {
            // Cutout crater mask
            ctx.globalCompositeOperation = 'destination-out';
            ctx.beginPath();
            ctx.ellipse(0, -PLANET_R, o.w/2, o.h, 0, 0, Math.PI*2);
            ctx.fill();
            
            // Draw rim
            ctx.globalCompositeOperation = 'source-over';
            ctx.strokeStyle = 'rgba(240,238,245,0.2)';
            ctx.lineWidth = 1.2;
            ctx.stroke();
            
            // Faint inner shadow/lines
            ctx.beginPath();
            ctx.ellipse(0, -PLANET_R+2, o.w/2 - 2, o.h - 2, 0, 0, Math.PI);
            ctx.strokeStyle = 'rgba(240,238,245,0.05)';
            ctx.stroke();"""

new_crater = """        if (o.variant === 'crater') {
            // Cutout crater mask to show deep space
            ctx.globalCompositeOperation = 'destination-out';
            ctx.beginPath();
            ctx.ellipse(0, -PLANET_R, o.w/2, o.h, 0, 0, Math.PI*2);
            ctx.fill();
            ctx.globalCompositeOperation = 'source-over';
            
            // Fill with space color so it's clearly a hole
            ctx.fillStyle = '#050407';
            ctx.beginPath();
            ctx.ellipse(0, -PLANET_R, o.w/2, o.h, 0, 0, Math.PI*2);
            ctx.fill();

            // Draw crater lip/rim
            ctx.strokeStyle = '#D93020'; // Red rim to match theme
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.ellipse(0, -PLANET_R, o.w/2, o.h, 0, 0, Math.PI*2);
            ctx.stroke();
            
            // Inner shadow arc
            ctx.beginPath();
            ctx.ellipse(0, -PLANET_R + o.h*0.3, o.w/2 * 0.8, o.h * 0.7, 0, 0, Math.PI);
            ctx.strokeStyle = 'rgba(217, 48, 32, 0.4)';
            ctx.lineWidth = 3;
            ctx.stroke();"""

html = html.replace(old_crater, new_crater)

# Ensure moon dots are dark against white moon
html = html.replace("ctx.fillStyle = 'rgba(240,238,245,0.1)';\n    MOON_DOTS", "ctx.fillStyle = 'rgba(5,4,7,0.15)';\n    MOON_DOTS")

# Ensure obstacles are dark or properly visible against white moon
html = html.replace("ctx.fillStyle = 'rgba(240,238,245,0.2)';\n                ctx.fillRect", "ctx.fillStyle = '#111009';\n                ctx.fillRect")

with open('game.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated game visual styles")
