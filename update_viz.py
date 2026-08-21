import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_sim = """function getSimulatedFreqs(genre, time) {
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
                    }"""

new_sim = """function getSimulatedFreqs(genre, time) {
                        let arr = new Array(32).fill(0);
                        let vol = audio.volume; 
                        let beat = (time * (genre === 'club' ? 2.2 : 1.2)) % 1; 
                        let kick = beat < 0.1 ? 1 : Math.max(0, 1 - beat * 3);
                        let snare = (beat > 0.45 && beat < 0.55) ? 1 : 0;
                        
                        for(let i=0; i<32; i++) {
                            if (genre === 'club') {
                                let base = Math.sin(time * 3 + i) * 0.5 + 0.5;
                                if (i < 4) arr[i] = kick * 255 * vol;
                                else if (i > 10 && i < 14) arr[i] = snare * 180 * vol;
                                else arr[i] = (base * 100) * vol;
                            } else if (genre === 'experimental') {
                                // Smooth, moody, slow rolling waves without glitchy noise
                                let wave = Math.sin(time * 1.5 + i * 0.15) * 0.5 + 0.5;
                                let wave2 = Math.cos(time * 0.8 - i * 0.1) * 0.5 + 0.5;
                                arr[i] = (wave * 120 + wave2 * 80) * vol;
                            } else {
                                // Pop: bouncy but smooth
                                let wave = Math.sin(time * 2 - i * 0.2) * 0.5 + 0.5;
                                arr[i] = (wave * 100 + kick * 60) * vol;
                            }
                        }
                        return arr;
                    }"""

html = html.replace(old_sim, new_sim)

# Also fix the `vRot += 1.5;` to respect volume so it slows down or is just smooth
old_vrot = "if (isPlaying) {\n                            vRot += 1.5; \n                            let pulse = 1 + (avg/255) * 0.03;"
new_vrot = "if (isPlaying) {\n                            vRot += 1.0; \n                            let pulse = 1 + (avg/255) * 0.02 * audio.volume;"
html = html.replace(old_vrot, new_vrot)

# Fix experimental circle glitch (avg is used for radius)
old_circ = "let r = isPlaying ? 100 + avg*1.5 : 100;"
new_circ = "let r = isPlaying ? 100 + avg*0.8 : 100;"
html = html.replace(old_circ, new_circ)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated visualizer")
