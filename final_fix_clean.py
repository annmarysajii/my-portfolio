import re
with open('project.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update overrides
old_overrides = "const overrides = {"
new_overrides = """        const overrides = {
          '1': 'Brand Exploration',
          '2': 'Visual System',
          'credit1': 'End Credits',
          'rain7': 'Rain Sequence',
          'staticshot_4': 'Establishing Shot',
          'ver1': 'Concept Version 1',
          'version2': 'Concept Version 2',
          'Home pt 1': 'Home (Part 1)',
          'character designs': 'Character Designs',
          'fusion jazz pg2': 'Fusion Jazz',
          'final_therapyscene': 'Therapy Scene',
          'pg1': 'Page 1',
          'ph2': 'Phase 2',
          'shot2': 'Shot 2',"""
if old_overrides in html and 'End Credits' not in html:
    html = html.replace(old_overrides, new_overrides)

# 2. Update captionHtml to ignore freelance-commissions
old_cap = "const captionHtml = (isYouTube || isPDF || isAudio || isComic) ? '' : `<div class=\"media-caption\">${name}</div>`;"
new_cap = "const captionHtml = (isYouTube || isPDF || isAudio || isComic || id === 'freelance-commissions') ? '' : `<div class=\"media-caption\">${name}</div>`;"
if old_cap in html:
    html = html.replace(old_cap, new_cap)

# 3. Replace the entire Custom Block securely!
pattern = r"if \(id === 'gobunny' \|\| id === 'green-arrow'\) \{.*?gal\.innerHTML = htmlStr;\n\s*return;\n\s*\}"
match = re.search(pattern, html, flags=re.DOTALL)
if match:
    old_block = match.group(0)
    new_block = """if (id === 'gobunny' || id === 'green-arrow' || id === 'nangele' || id === 'original-tracks') {
                let htmlStr = styleBlock;
                
                if (id === 'gobunny') {
                    const logoPrimary = findFile('GO BUNNY');
                    const logoSecondary = findFiles('Your paragraph text').filter(f => f.includes('35') || f.includes('36') || f.includes('33')); 
                    const colors = findFiles('Your paragraph text').filter(f => f.includes('27') || f.includes('37'));
                    const guidelines = findFiles('Brand identity');
                    const mockups = findFiles('Your paragraph text').filter(f => f.includes('29') || f.includes('30') || f.includes('28') || f.includes('38') || f.includes('23') || f.includes('24'));
                    
                    htmlStr += `<div class="cs-section"><h2 class="cs-heading">Color Palette</h2>
                        <div class="cs-palettes">
                            <div class="cs-color"><div class="cs-swatch" style="background:#D02F5A;"></div><span class="cs-hex">#D02F5A</span></div>
                            <div class="cs-color"><div class="cs-swatch" style="background:#FF9A9E;"></div><span class="cs-hex">#FF9A9E</span></div>
                            <div class="cs-color"><div class="cs-swatch" style="background:#FFF5F7;"></div><span class="cs-hex">#FFF5F7</span></div>
                            <div class="cs-color"><div class="cs-swatch" style="background:#2A2A2A;"></div><span class="cs-hex">#2A2A2A</span></div>
                        </div>
                    </div>`;
                    
                    htmlStr += `<div class="cs-section"><h2 class="cs-heading">Logo Variations</h2><div class="masonry-container">`;
                    if(logoPrimary) htmlStr += renderMedia(logoPrimary).replace('masonry-item', 'masonry-item full-width');
                    logoSecondary.forEach(f => { htmlStr += renderMedia(f); });
                    htmlStr += `</div></div>`;

                    htmlStr += `<div class="cs-section"><h2 class="cs-heading">Typography & Colors</h2><div class="masonry-container">`;
                    colors.forEach(f => { htmlStr += renderMedia(f); });
                    htmlStr += `</div></div>`;

                    htmlStr += `<div class="cs-section"><h2 class="cs-heading">Brand Guidelines</h2><div class="masonry-container">`;
                    guidelines.forEach(f => { htmlStr += renderMedia(f); });
                    htmlStr += `</div></div>`;

                    htmlStr += `<div class="cs-section"><h2 class="cs-heading">Applications</h2><div class="masonry-container">`;
                    mockups.forEach(f => { htmlStr += renderMedia(f); });
                    htmlStr += `</div></div>`;
                } else if (id === 'green-arrow') {
                    const logo = findFile('LOGO GREEN ARROW');
                    const posters = findFiles('3.png').concat(findFiles('presents'));
                    const digital = findFiles('4.png').concat(findFiles('5.png'));
                    const merch = findFiles('6.png').concat(findFiles('7.png'));
                    
                    htmlStr += `
                    <div class="cs-section">
                        <h2 class="cs-heading">Color Palette</h2>
                        <div class="cs-palettes">
                            <div class="cs-color"><div class="cs-swatch" style="background:#243E36;"></div><span class="cs-hex">#243E36</span></div>
                            <div class="cs-color"><div class="cs-swatch" style="background:#7CA982;"></div><span class="cs-hex">#7CA982</span></div>
                            <div class="cs-color"><div class="cs-swatch" style="background:#E0EEC6;"></div><span class="cs-hex">#E0EEC6</span></div>
                            <div class="cs-color"><div class="cs-swatch" style="background:#C2A83E;"></div><span class="cs-hex">#C2A83E</span></div>
                            <div class="cs-color"><div class="cs-swatch" style="background:#F1F7ED;"></div><span class="cs-hex">#F1F7ED</span></div>
                        </div>
                    </div>`;
                    
                    htmlStr += `<div class="cs-section"><h2 class="cs-heading">Logo & Identity</h2><div class="masonry-container">`;
                    if(logo) htmlStr += renderMedia(logo).replace('masonry-item', 'masonry-item full-width');
                    htmlStr += `</div></div>`;

                    htmlStr += `<div class="cs-section"><h2 class="cs-heading">Posters & Events</h2><div class="masonry-container">`;
                    posters.forEach(f => { htmlStr += renderMedia(f); });
                    htmlStr += `</div></div>`;

                    htmlStr += `<div class="cs-section"><h2 class="cs-heading">Digital & Web</h2><div class="masonry-container">`;
                    digital.forEach(f => { htmlStr += renderMedia(f); });
                    htmlStr += `</div></div>`;

                    htmlStr += `<div class="cs-section"><h2 class="cs-heading">Merchandise</h2><div class="masonry-container">`;
                    merch.forEach(f => { htmlStr += renderMedia(f); });
                    htmlStr += `</div></div>`;
                } else if (id === 'nangele') {
                    htmlStr += `
                    <style>
                    .book-container { position:relative; width:100%; max-width:1000px; margin:0 auto; aspect-ratio: 1.4; background:#fff; box-shadow:0 10px 40px rgba(0,0,0,0.1); border-radius:4px; display:flex; perspective:2000px; }
                    .book-page { flex:1; width:50%; height:100%; position:relative; background:#fff; border:1px solid #eee; border-left:none; transform-origin: left center; transition: transform 0.6s cubic-bezier(0.645, 0.045, 0.355, 1); transform-style: preserve-3d; }
                    .book-page.left { border-left:1px solid #eee; border-right:1px solid #ddd; transform-origin: right center; }
                    .book-page img { width:100%; height:100%; object-fit:contain; position:absolute; inset:0; background:#fff; backface-visibility: hidden; }
                    .page-flip-btn { position:absolute; top:50%; transform:translateY(-50%); background:var(--ink); color:var(--bg); border:none; width:50px; height:50px; border-radius:50%; cursor:pointer; z-index:10; font-size:1.2rem; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 12px rgba(0,0,0,0.2); transition:transform 0.2s, background 0.2s; }
                    .page-flip-btn:hover { background:var(--blue); transform:translateY(-50%) scale(1.1); }
                    .page-flip-btn:disabled { opacity:0.3; cursor:not-allowed; }
                    .page-flip-btn.prev { left:-25px; }
                    .page-flip-btn.next { right:-25px; }
                    @media(max-width:768px) {
                      .book-container { aspect-ratio: 0.7; flex-direction: column; }
                      .book-page { width:100%; border-left:1px solid #eee; }
                      .book-page.left { border-bottom:1px solid #ddd; border-right:1px solid #eee; }
                      .page-flip-btn { width:40px; height:40px; }
                      .page-flip-btn.prev { left:10px; top:10px; transform:none; }
                      .page-flip-btn.next { right:10px; top:10px; transform:none; }
                      .page-flip-btn:hover { transform:scale(1.1); }
                    }
                    </style>
                    <div class="cs-section">
                      <h2 class="cs-heading" style="text-align:center; margin-bottom:2rem;">Nangeli — Reading View</h2>
                      <div id="nangeli-reader"></div>
                    </div>
                    `;
                } else if (id === 'original-tracks') {
                    htmlStr += `
                    <style>
                      .track-btn { display:flex; align-items:center; gap:1.5rem; padding:1.25rem 1.5rem; background:rgba(255,255,255,0.6); border:1px solid rgba(0,0,0,0.1); border-radius:12px; cursor:pointer; transition:all 0.3s cubic-bezier(0.4, 0, 0.2, 1); text-align:left; box-shadow:0 4px 15px rgba(0,0,0,0.02); }
                      .track-btn:hover { background:#fff; transform:translateX(8px); box-shadow:0 8px 25px rgba(0,0,0,0.08); }
                      .track-btn.active { border-color:var(--ink); background:#fff; box-shadow:0 10px 30px rgba(0,0,0,0.12); }
                      .track-icon { width:48px; height:48px; border-radius:50%; background:var(--ink); color:var(--bg); display:flex; align-items:center; justify-content:center; box-shadow:0 4px 12px rgba(0,0,0,0.15); transition:all 0.3s; }
                      .track-btn:hover .track-icon { transform:scale(1.1); }
                      .track-btn.active .track-icon { animation: pulse 2s infinite; }
                      @keyframes pulse { 0% { box-shadow:0 0 0 0 rgba(var(--ink-rgb), 0.4); } 70% { box-shadow:0 0 0 15px rgba(var(--ink-rgb), 0); } 100% { box-shadow:0 0 0 0 rgba(var(--ink-rgb), 0); } }
                      #vinyl-player-section { position:relative; min-height:85vh; display:flex; flex-direction:column; align-items:center; justify-content:center; padding: 4rem 2rem; border-radius:16px; overflow:hidden; margin-bottom:4rem; background:#111; transition: background 1s ease; }
                      #audio-viz { position:absolute; inset:0; width:100%; height:100%; z-index:0; }
                      .vp-content { display:flex; flex-wrap:wrap; gap:5rem; align-items:center; justify-content:center; width:100%; max-width:1100px; z-index:1; }
                      
                      .turntable-base { position:relative; width:380px; height:320px; background: linear-gradient(145deg, #e6e6e6, #ffffff); border-radius:24px; box-shadow: 0 30px 60px rgba(0,0,0,0.4), inset 0 2px 5px rgba(255,255,255,0.8), inset 0 -4px 10px rgba(0,0,0,0.1); display:flex; align-items:center; justify-content:center; border: 1px solid #d1d1d1; }
                      .platter { position:absolute; left:20px; width:280px; height:280px; border-radius:50%; background: radial-gradient(circle, #555 0%, #222 90%); box-shadow: 0 10px 20px rgba(0,0,0,0.3), inset 0 2px 4px rgba(255,255,255,0.3); display:flex; align-items:center; justify-content:center; border:4px solid #b3b3b3; }
                      .spindle { position:absolute; width:14px; height:14px; border-radius:50%; background: radial-gradient(circle at 30% 30%, #fff, #999); z-index:20; box-shadow: 0 2px 4px rgba(0,0,0,0.5); }
                      .slider { position:absolute; right:20px; top:40px; width:10px; height:120px; background:#222; border-radius:5px; box-shadow: inset 0 2px 5px rgba(0,0,0,0.5); }
                      .slider-knob { position:absolute; top:50%; left:-10px; width:30px; height:15px; background: linear-gradient(to bottom, #ddd, #999); border-radius:2px; box-shadow: 0 4px 8px rgba(0,0,0,0.3); transform:translateY(-50%); border-top:1px solid #fff; border-bottom:1px solid #555; }
                      .dial { position:absolute; right:20px; bottom:40px; width:30px; height:30px; border-radius:50%; background: linear-gradient(145deg, #ccc, #fff); box-shadow: 0 4px 8px rgba(0,0,0,0.2), inset 0 1px 2px rgba(255,255,255,1); }
                      .dial::after { content:''; position:absolute; top:4px; left:14px; width:2px; height:8px; background:#444; }
                      
                      #vinyl-disc { width:260px; height:260px; border-radius:50%; background:#111; position:relative; box-shadow: 0 4px 10px rgba(0,0,0,0.5); display:flex; align-items:center; justify-content:center; }
                      .groove { position:absolute; border-radius:50%; border:1px solid rgba(255,255,255,0.08); }
                      #vinyl-label { width:35%; height:35%; border-radius:50%; background:#FAF8F4; transition: background 0.5s; display:flex; align-items:center; justify-content:center; box-shadow: inset 0 0 10px rgba(0,0,0,0.3); }
                      
                      #tonearm { position:absolute; top:20px; right:40px; width:20px; height:180px; background:linear-gradient(to right, #ccc, #eee, #ccc); transform-origin: 10px 20px; transform: rotate(15deg); border-radius:10px; transition: transform 0.6s cubic-bezier(0.34, 1.56, 0.64, 1); box-shadow:-5px 10px 15px rgba(0,0,0,0.3); z-index:10; }
                      .ta-base { position:absolute; top:0; left:-15px; width:50px; height:50px; border-radius:50%; background: radial-gradient(circle at 30% 30%, #555, #222); box-shadow: 0 5px 10px rgba(0,0,0,0.4), inset 0 2px 5px rgba(255,255,255,0.2); }
                      .ta-head { position:absolute; bottom:-10px; left:-12px; width:30px; height:55px; background: linear-gradient(to bottom, #333, #111); border-radius:4px; transform: rotate(25deg); box-shadow: -2px 4px 8px rgba(0,0,0,0.4); border-top:1px solid #555; }
                      
                      .track-list-container { flex:1; min-width:320px; background:rgba(255,255,255,0.85); backdrop-filter:blur(30px); padding:2.5rem; border-radius:24px; box-shadow:0 20px 50px rgba(0,0,0,0.15); border: 1px solid rgba(255,255,255,0.5); }
                    </style>
                    <div id="vinyl-player-section">
                      <canvas id="audio-viz"></canvas>
                      <div class="vp-content">
                        
                        <!-- Premium Turntable -->
                        <div class="turntable-base">
                            <div class="platter">
                                <div id="vinyl-disc">
                                    <div class="groove" style="inset:8%;"></div>
                                    <div class="groove" style="inset:16%;"></div>
                                    <div class="groove" style="inset:24%;"></div>
                                    <div class="groove" style="inset:32%;"></div>
                                    <div class="groove" style="inset:40%;"></div>
                                    <div id="vinyl-label"></div>
                                </div>
                                <div class="spindle"></div>
                            </div>
                            
                            <div class="slider"><div class="slider-knob"></div></div>
                            <div class="dial"></div>
                            
                            <div id="tonearm">
                                <div class="ta-base"></div>
                                <div class="ta-head"></div>
                            </div>
                        </div>

                        <!-- Tracklist -->
                        <div class="track-list-container">
                           <h2 style="margin-top:0; font-family:'Clash Display'; font-size:2.5rem; margin-bottom:0.5rem; letter-spacing:-1px;">The DJ Booth</h2>
                           <p style="color:var(--ink5); margin-bottom:2rem; font-size:1.05rem;">Select a track to start the experience.</p>
                           <div id="track-list" style="display:flex; flex-direction:column; gap:1.25rem;">
                              <!-- Tracks injected here -->
                           </div>
                           <audio id="main-audio"></audio>
                        </div>
                        
                      </div>
                    </div>
                    `;
                }
                
                gal.innerHTML = htmlStr;
                
                if (id === 'nangele') {
                    const nangeliMedia = media.filter(f => f.match(/\.(png|jpe?g)$/i));
                    let curPage = 0;
                    const renderBook = (direction) => {
                        const r = document.getElementById('nangeli-reader');
                        if(!r) return;
                        let p1 = nangeliMedia[curPage] ? `<img src="${nangeliMedia[curPage]}" style="width:100%; height:100%; object-fit:contain; padding:2rem;">` : '';
                        let p2 = nangeliMedia[curPage+1] ? `<img src="${nangeliMedia[curPage+1]}" style="width:100%; height:100%; object-fit:contain; padding:2rem;">` : '';
                        let animClass = direction === 'next' ? 'flip-next' : (direction === 'prev' ? 'flip-prev' : '');
                        
                        r.innerHTML = `
                        <div class="book-container ${animClass}">
                          <button class="page-flip-btn prev" id="n-prev" ${curPage===0?'disabled':''}><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg></button>
                          <div class="book-page left">${p1}</div>
                          <div class="book-page right">${p2}</div>
                          <button class="page-flip-btn next" id="n-next" ${curPage>=nangeliMedia.length-2?'disabled':''}><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg></button>
                        </div>
                        <div style="text-align:center; margin-top:1.5rem; font-size:0.95rem; font-weight:500; color:var(--ink5);">Spread ${Math.floor(curPage/2)+1} of ${Math.ceil(nangeliMedia.length/2)}</div>
                        `;
                        
                        const pBtn = document.getElementById('n-prev');
                        if (pBtn) pBtn.onclick = () => { curPage = Math.max(0, curPage-2); renderBook('prev'); };
                        const nBtn = document.getElementById('n-next');
                        if (nBtn) nBtn.onclick = () => { curPage = Math.min(nangeliMedia.length-1, curPage+2); renderBook('next'); };
                    };
                    renderBook('');
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
                            <div class="track-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg></div>
                            <div>
                                <div style="font-weight:700; font-size:1.2rem; font-family:'Clash Display';">${t.name}</div>
                                <div style="font-size:0.85rem; color:var(--ink5); text-transform:uppercase; letter-spacing:1.5px; margin-top:4px; font-weight:600;">${t.genre} Mix</div>
                            </div>
                        </button>
                        `;
                    });
                    
                    const audio = document.getElementById('main-audio');
                    const vinyl = document.getElementById('vinyl-disc');
                    const tonearm = document.getElementById('tonearm');
                    const label = document.getElementById('vinyl-label');
                    const canvas = document.getElementById('audio-viz');
                    const ctx = canvas ? canvas.getContext('2d') : null;
                    const section = document.getElementById('vinyl-player-section');
                    
                    let vRot = 0;
                    let currentIdx = -1;
                    
                    function getSimulatedFreqs(genre, time) {
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
                    }
                    
                    function drawViz() {
                        requestAnimationFrame(drawViz);
                        if(!ctx || currentIdx === -1) return;
                        
                        canvas.width = section.offsetWidth;
                        canvas.height = section.offsetHeight;
                        const W = canvas.width;
                        const H = canvas.height;
                        
                        const track = tracks[currentIdx];
                        let isPlaying = !audio.paused && !audio.ended;
                        
                        let dataArray = getSimulatedFreqs(track.genre, audio.currentTime);
                        let sum = 0;
                        for(let i=0; i<32; i++) sum += dataArray[i];
                        let avg = sum / 32;
                        
                        if (isPlaying) {
                            vRot += 1.5; 
                            let pulse = 1 + (avg/255) * 0.03;
                            vinyl.style.transform = `scale(${pulse}) rotate(${vRot}deg)`;
                            tonearm.style.transform = `rotate(36deg)`;
                        } else {
                            tonearm.style.transform = `rotate(15deg)`;
                        }
                        
                        ctx.clearRect(0, 0, W, H);
                        
                        if (track.genre === 'club') {
                            section.style.background = '#08080a';
                            let bass = isPlaying ? dataArray[1]/255 : 0;
                            
                            ctx.fillStyle = `rgba(255, 0, 85, ${bass * 0.4})`;
                            ctx.fillRect(0, 0, W, H);
                            
                            let barW = (W / 32) - 4;
                            for(let i=0; i<32; i++) {
                                let barH = isPlaying ? (dataArray[i] / 255) * (H * 0.7) : 10;
                                ctx.fillStyle = `rgba(0, 255, 255, ${0.4 + (dataArray[i]/255)*0.6})`;
                                ctx.beginPath();
                                ctx.roundRect(i * (barW + 4), H - barH, barW, barH, [4, 4, 0, 0]);
                                ctx.fill();
                            }
                        } else if (track.genre === 'experimental') {
                            section.style.background = '#e6f2ff';
                            
                            ctx.beginPath();
                            ctx.moveTo(0, H/2);
                            for(let i=0; i<64; i++) {
                                let sim = isPlaying ? (Math.sin(audio.currentTime * 3 + i * 0.2) * 0.5 + 0.5) : 0.5;
                                let y = H/2 + (sim - 0.5) * H/2;
                                ctx.lineTo(i * (W/64), y);
                            }
                            ctx.lineTo(W, H/2);
                            ctx.strokeStyle = `rgba(0, 150, 255, 0.8)`;
                            ctx.lineWidth = 8;
                            ctx.stroke();
                            
                            let r = isPlaying ? 100 + avg*1.5 : 100;
                            ctx.beginPath();
                            ctx.arc(W/2, H/2, r, 0, Math.PI*2);
                            ctx.fillStyle = `rgba(0, 150, 255, 0.15)`;
                            ctx.fill();
                        } else if (track.genre === 'pop') {
                            section.style.background = '#FFF0F5';
                            
                            for(let i=0; i<15; i++) {
                                let val = isPlaying ? dataArray[i*2]/255 : 0;
                                let r = 20 + val * 120;
                                ctx.beginPath();
                                ctx.arc(W * (i+1)/16, H/2 + Math.sin(Date.now()*0.002 + i) * 150, r, 0, Math.PI*2);
                                ctx.fillStyle = `hsla(${340 + i*6}, 100%, 65%, 0.6)`;
                                ctx.fill();
                            }
                        }
                    }
                    drawViz();
                    
                    tracks.forEach((t, i) => {
                        document.getElementById(`tbtn-${i}`).onclick = () => {
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
    html = html.replace(old_block, new_block)

with open('project.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Final fix completed flawlessly")
