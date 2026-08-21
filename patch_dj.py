import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add conic gradient shine to vinyl and interactive IDs to slider
html = html.replace(
    '#vinyl-disc { width:260px; height:260px; border-radius:50%; background:#111;',
    '#vinyl-disc { width:260px; height:260px; border-radius:50%; background: conic-gradient(from 45deg, #111 0%, #333 25%, #111 50%, #333 75%, #111 100%);'
)

html = html.replace(
    '<div class="slider"><div class="slider-knob"></div></div>',
    '<div class="slider" id="vol-slider" style="cursor:pointer;"><div class="slider-knob" id="vol-knob" style="pointer-events:none;"></div></div>'
)

# 2. Update the javascript for interactivity and improved visualizer
old_sim = """function getSimulatedFreqs(genre, time) {
                        let arr = new Array(32).fill(0);
                        let beat = (time * (genre === 'club' ? 2.2 : 1.8)) % 1; 
                        let kick = beat < 0.1 ? 1 : Math.max(0, 1 - beat * 4);
                        
                        for(let i=0; i<32; i++) {
                            let base = Math.sin(time * 5 + i) * 0.5 + 0.5;
                            if (genre === 'club') {
                                arr[i] = (i < 4 ? kick * 255 : (base * 100 + Math.random() * 50));
                            } else if (genre === 'experimental') {
                                arr[i] = (Math.sin(time * 2 + i * 0.5) * 0.5 + 0.5) * 200 + Math.random()*20;
                            } else {
                                arr[i] = (Math.sin(time * 8 - i) * 0.5 + 0.5) * (150 + kick*100);
                            }
                        }
                        return arr;
                    }"""

new_sim = """function getSimulatedFreqs(genre, time) {
                        let arr = new Array(32).fill(0);
                        let beat = (time * (genre === 'club' ? 2.2 : 1.8)) % 1; 
                        let kick = beat < 0.1 ? 1 : Math.max(0, 1 - beat * 4);
                        let snare = (beat > 0.45 && beat < 0.55) ? 1 : 0;
                        let hihat = (time * 8) % 1 < 0.2 ? Math.random() : 0;
                        
                        for(let i=0; i<32; i++) {
                            let base = (Math.sin(time * 5 + i) * 0.5 + 0.5) * (Math.sin(time * 2.3 + i * 0.7) * 0.5 + 0.5);
                            if (genre === 'club') {
                                if (i < 4) arr[i] = kick * 255;
                                else if (i > 10 && i < 14) arr[i] = snare * 200 + Math.random()*50;
                                else if (i > 24) arr[i] = hihat * 150 + Math.random()*30;
                                else arr[i] = base * 120 + Math.random() * 60;
                            } else if (genre === 'experimental') {
                                arr[i] = (Math.sin(time * 3 + i * 0.4) * Math.cos(time * 1.5 - i * 0.2) * 0.5 + 0.5) * 220 + hihat * 50 + Math.random()*20;
                            } else {
                                arr[i] = (Math.sin(time * 7 - i * 0.5) * 0.5 + 0.5) * (150 + kick*80 + snare*50);
                            }
                        }
                        return arr;
                    }
                    
                    // Volume Slider Logic
                    const slider = document.getElementById('vol-slider');
                    const knob = document.getElementById('vol-knob');
                    if (slider && knob) {
                        let isDragging = false;
                        const updateVol = (e) => {
                            const rect = slider.getBoundingClientRect();
                            let y = e.clientY - rect.top;
                            y = Math.max(0, Math.min(y, rect.height));
                            let vol = 1 - (y / rect.height);
                            audio.volume = vol;
                            knob.style.top = y + 'px';
                        };
                        slider.onmousedown = (e) => { isDragging = true; updateVol(e); };
                        window.onmousemove = (e) => { if(isDragging) updateVol(e); };
                        window.onmouseup = () => { isDragging = false; };
                    }"""

html = html.replace(old_sim, new_sim)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated vinyl shine and volume slider")
