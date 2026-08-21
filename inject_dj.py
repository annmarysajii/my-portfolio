import re

with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add original-tracks to the custom project interception block
old_intercept = "if (id === 'gobunny' || id === 'green-arrow' || id === 'nangele') {"
new_intercept = "if (id === 'gobunny' || id === 'green-arrow' || id === 'nangele' || id === 'original-tracks') {"

html = html.replace(old_intercept, new_intercept)

# Inject the original-tracks logic
injection = """                  } else if (id === 'original-tracks') {
                    htmlStr += `
                    <style>
                      .track-btn { display:flex; align-items:center; gap:1rem; padding:1rem; background:var(--surf); border:1px solid var(--line); border-radius:8px; cursor:pointer; transition:all 0.2s; text-align:left; }
                      .track-btn:hover { background:var(--ink05); transform:translateX(5px); }
                      .track-btn.active { border-color:var(--ink); background:var(--ink07); }
                      .track-icon { width:40px; height:40px; border-radius:50%; background:var(--ink); color:var(--bg); display:flex; align-items:center; justify-content:center; }
                      .track-btn.active .track-icon { animation: pulse 2s infinite; }
                      @keyframes pulse { 0% { box-shadow:0 0 0 0 rgba(var(--ink-rgb), 0.4); } 70% { box-shadow:0 0 0 10px rgba(var(--ink-rgb), 0); } 100% { box-shadow:0 0 0 0 rgba(var(--ink-rgb), 0); } }
                      #vinyl-player-section { position:relative; min-height:80vh; display:flex; flex-direction:column; align-items:center; justify-content:center; padding: 4rem 2rem; border-radius:12px; overflow:hidden; margin-bottom:4rem; }
                      #audio-viz { position:absolute; inset:0; width:100%; height:100%; z-index:0; }
                      .vp-content { display:flex; flex-wrap:wrap; gap:4rem; align-items:center; justify-content:center; width:100%; max-width:1000px; z-index:1; }
                      @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
                    </style>
                    <div id="vinyl-player-section">
                      <canvas id="audio-viz"></canvas>
                      <div class="vp-content">
                        
                        <div style="position:relative;">
                            <!-- Vinyl Disc -->
                            <div id="vinyl-disc" style="width:280px; height:280px; border-radius:50%; background:#111; position:relative; box-shadow: 0 20px 40px rgba(0,0,0,0.4); border:6px solid #222; display:flex; align-items:center; justify-content:center;">
                                <div style="position:absolute; inset:8%; border-radius:50%; border:1px solid #2a2a2a;"></div>
                                <div style="position:absolute; inset:16%; border-radius:50%; border:1px solid #2a2a2a;"></div>
                                <div style="position:absolute; inset:24%; border-radius:50%; border:1px solid #2a2a2a;"></div>
                                <div style="position:absolute; inset:32%; border-radius:50%; border:1px solid #2a2a2a;"></div>
                                <div style="position:absolute; inset:40%; border-radius:50%; border:1px solid #2a2a2a;"></div>
                                
                                <div id="vinyl-label" style="width:35%; height:35%; border-radius:50%; background:#FAF8F4; display:flex; align-items:center; justify-content:center; transition: background 0.5s;">
                                   <div style="width:12px; height:12px; border-radius:50%; background:#111; z-index:2;"></div>
                                </div>
                            </div>
                            
                            <!-- Tonearm -->
                            <div id="tonearm" style="position:absolute; top:-20px; right:-20px; width:15px; height:160px; background:linear-gradient(to right, #999, #eee, #999); transform-origin: 7.5px 15px; transform: rotate(10deg); border-radius:10px; transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1); box-shadow:-2px 5px 10px rgba(0,0,0,0.4); z-index:10;">
                                <!-- Tonearm Base -->
                                <div style="position:absolute; top:0; left:-12.5px; width:40px; height:40px; border-radius:50%; background:#333; box-shadow: inset 0 2px 5px rgba(255,255,255,0.2);"></div>
                                <!-- Stylus head -->
                                <div style="position:absolute; bottom:-10px; left:-10px; width:35px; height:50px; background:#222; border-radius:4px; transform: rotate(20deg);"></div>
                            </div>
                        </div>

                        <!-- Tracklist -->
                        <div style="flex:1; min-width:300px; background:rgba(255,255,255,0.85); backdrop-filter:blur(20px); padding:2rem; border-radius:16px; box-shadow:0 10px 40px rgba(0,0,0,0.08);">
                           <h2 style="margin-top:0; font-family:'Clash Display'; font-size:2rem; margin-bottom:1.5rem;">The DJ Booth</h2>
                           <div id="track-list" style="display:flex; flex-direction:column; gap:1rem;">
                              <!-- Tracks injected here -->
                           </div>
                           <audio id="main-audio" crossorigin="anonymous"></audio>
                        </div>
                        
                      </div>
                    </div>
                    `;
                  } else if (id === 'nangele') {"""

html = html.replace("} else if (id === 'nangele') {", injection)

# Post-inject logic
post_inject = """                    renderBook('');
                } else if (id === 'original-tracks') {
                    const tracks = [
                      { file: 'assets/portfolio-data/Original demo tracks/Club got boots (2).m4a', name: 'Club Got Boots', genre: 'club', color: '#FF0055' },
                      { file: 'assets/portfolio-data/Original demo tracks/Cloudy days.m4a', name: 'Cloudy Days', genre: 'experimental', color: '#00D2FF' },
                      { file: 'assets/portfolio-data/Original demo tracks/Paradise demo (2).m4a', name: 'Paradise', genre: 'pop', color: '#FF9A9E' }
                    ];
                    
                    const list = document.getElementById('track-list');
                    tracks.forEach((t, i) => {
                        list.innerHTML += `
                        <button class="track-btn" id="tbtn-${i}">
                            <div class="track-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg></div>
                            <div>
                                <div style="font-weight:600; font-size:1.1rem; font-family:'Clash Display';">${t.name}</div>
                                <div style="font-size:0.85rem; color:var(--ink5); text-transform:uppercase; letter-spacing:1px; margin-top:2px;">${t.genre} Mix</div>
                            </div>
                        </button>
                        `;
                    });
                    
                    let audioCtx, analyser, dataArray, sourceNode;
                    let currentIdx = -1;
                    const audio = document.getElementById('main-audio');
                    const vinyl = document.getElementById('vinyl-disc');
                    const tonearm = document.getElementById('tonearm');
                    const label = document.getElementById('vinyl-label');
                    const canvas = document.getElementById('audio-viz');
                    const ctx = canvas ? canvas.getContext('2d') : null;
                    
                    let vRot = 0;
                    
                    function drawViz() {
                        requestAnimationFrame(drawViz);
                        if(!ctx || !analyser || currentIdx === -1) return;
                        
                        // Resize canvas
                        const section = document.getElementById('vinyl-player-section');
                        canvas.width = section.offsetWidth;
                        canvas.height = section.offsetHeight;
                        const W = canvas.width;
                        const H = canvas.height;
                        
                        analyser.getByteFrequencyData(dataArray);
                        let sum = 0;
                        for(let i=0; i<dataArray.length; i++) sum += dataArray[i];
                        let avg = sum / dataArray.length;
                        
                        const track = tracks[currentIdx];
                        
                        if (!audio.paused) {
                            vRot += 1; // 60 RPM approx
                            let pulse = 1 + (avg/255) * 0.05;
                            vinyl.style.transform = `scale(${pulse}) rotate(${vRot}deg)`;
                            tonearm.style.transform = `rotate(35deg)`;
                        } else {
                            tonearm.style.transform = `rotate(10deg)`;
                        }
                        
                        ctx.clearRect(0, 0, W, H);
                        
                        if (track.genre === 'club') {
                            let bass = dataArray[2]/255;
                            ctx.fillStyle = `#0a0a0c`;
                            ctx.fillRect(0, 0, W, H);
                            
                            // Laser flashes
                            ctx.fillStyle = `rgba(255, 0, 85, ${bass * 0.6})`;
                            ctx.fillRect(0, 0, W, H);
                            
                            // Equalizer bars
                            let barW = (W / 32) - 4;
                            for(let i=0; i<32; i++) {
                                let barH = (dataArray[i*4] / 255) * (H * 0.6);
                                ctx.fillStyle = `rgba(0, 255, 255, ${0.3 + (dataArray[i*4]/255)*0.7})`;
                                ctx.fillRect(i * (barW + 4), H - barH, barW, barH);
                            }
                        } else if (track.genre === 'experimental') {
                            ctx.fillStyle = `#f0f8ff`;
                            ctx.fillRect(0, 0, W, H);
                            
                            // Wavy organic lines
                            ctx.beginPath();
                            ctx.moveTo(0, H/2);
                            for(let i=0; i<64; i++) {
                                let v = dataArray[i*2] / 128.0; 
                                let y = v * H/3 + H/6;
                                ctx.lineTo(i * (W/64), y);
                            }
                            ctx.lineTo(W, H/2);
                            ctx.strokeStyle = `rgba(0, 210, 255, 0.6)`;
                            ctx.lineWidth = 6;
                            ctx.stroke();
                            
                            // Ambient pulsating circles
                            ctx.beginPath();
                            ctx.arc(W/2, H/2, 100 + avg*1.5, 0, Math.PI*2);
                            ctx.fillStyle = `rgba(0, 210, 255, 0.1) !important`;
                            ctx.fill();
                        } else if (track.genre === 'pop') {
                            ctx.fillStyle = `#FFF5F7`;
                            ctx.fillRect(0, 0, W, H);
                            
                            // Bouncing bubbles
                            for(let i=0; i<12; i++) {
                                let val = dataArray[i*8] / 255;
                                let r = 20 + val * 100;
                                ctx.beginPath();
                                ctx.arc(W * (i+1)/13, H/2 + Math.sin(Date.now()*0.003 + i) * 100, r, 0, Math.PI*2);
                                ctx.fillStyle = `hsla(${340 + i*5}, 100%, 75%, 0.5)`;
                                ctx.fill();
                            }
                        }
                    }
                    
                    tracks.forEach((t, i) => {
                        document.getElementById(`tbtn-${i}`).onclick = () => {
                            if (!audioCtx) {
                                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                                analyser = audioCtx.createAnalyser();
                                analyser.fftSize = 256;
                                sourceNode = audioCtx.createMediaElementSource(audio);
                                sourceNode.connect(analyser);
                                analyser.connect(audioCtx.destination);
                                dataArray = new Uint8Array(analyser.frequencyBinCount);
                                drawViz();
                            }
                            
                            document.querySelectorAll('.track-btn').forEach(b => b.classList.remove('active'));
                            document.getElementById(`tbtn-${i}`).classList.add('active');
                            
                            if (currentIdx === i) {
                                if (audio.paused) audio.play();
                                else audio.pause();
                            } else {
                                currentIdx = i;
                                audio.src = t.file;
                                audio.play();
                                label.style.background = t.color;
                            }
                        };
                    });
                }
                return;
            }"""

html = html.replace("                    renderBook('');\n                }\n                return;\n            }", post_inject)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Injected DJ vinyl player")
