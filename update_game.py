import re

with open('game.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_script = """<script>
  /* ✦✦ CURSOR ✦✦ */
  const cur=document.getElementById('cur'),csq=document.getElementById('csq');
  let mx=innerWidth/2,my=innerHeight/2,cx=mx,cy=my,lx=mx,ly=my,ang=0;
  document.addEventListener('mousemove',e=>{mx=e.clientX;my=e.clientY;});
  (function cl(){cx+=(mx-cx)*.16;cy+=(my-cy)*.16;cur.style.left=cx+'px';cur.style.top=cy+'px';const sp=Math.hypot(mx-lx,my-ly);lx=mx;ly=my;ang+=1+sp*.5;csq.style.transform='rotate('+ang+'deg)';requestAnimationFrame(cl);})();
  
  /* ✦✦ GAME ENGINE (LUNAR RUNNER) ✦✦ */
  const canvas=document.getElementById('game'),ctx=canvas.getContext('2d');
  const $$=id=>document.getElementById(id);
  const scoreDisp=$$('scoreDisp'),hiDisp=$$('hiDisp'),lastDisp=$$('lastDisp'),promptEl=$$('prompt'),statusMsg=$$('statusMsg');
  const DPR=Math.min(window.devicePixelRatio||1,2);
  const CW=Math.min(680,window.innerWidth-40),CH=210;
  canvas.width=CW*DPR;canvas.height=CH*DPR;canvas.style.width=CW+'px';canvas.style.height=CH+'px';
  ctx.scale(DPR,DPR);
  
  /* Constants */
  const GY=CH-45, PLANET_R=1200; 
  const GRAVITY=0.68, JUMP_V=-9.0, DBLJ_V=-8.0, STAR_R=13, STAR_X=90, CEIL_Y=STAR_R+10;
  const BASE_SPD=5.0, SPD_INC=0.0008, MAX_SPD=14;
  
  /* Moon visual dots */
  const MOON_DOTS=Array.from({length:80},()=>({
      ang: (Math.random()-0.5)*1.2, 
      depth: Math.random()*40,
      r: 0.5 + Math.random()*1.5
  }));

  const BG_STARS=Array.from({length:105},()=>({
    x:Math.random()*CW,y:Math.random()*(GY-6),
    r:.4+Math.random()*1.5,twinkle:Math.random()*Math.PI*2,
    twinkleSpd:.025+Math.random()*.07,speed:.06+Math.random()*.16
  }));
  
  const SHOOTS=[];
  function mkShoot(){
    return {
      x:CW*.25+Math.random()*CW*.8, y:Math.random()*(GY*.45),
      vx:-(3.5+Math.random()*7), vy:.8+Math.random()*2.2,
      len:55+Math.random()*95, alpha:0, active:false, life:0,
      delay:Math.floor(Math.random()*360+120)
    };
  }
  for(let i=0;i<5;i++) SHOOTS.push(mkShoot());
  
  /* Player */
  let star={x:STAR_X,y:GY-STAR_R,vy:0,rot:0,grounded:true,jumps:0};
  let jumpHeld=false,starSX=1,starSY=1,wasGrounded=true;
  
  /* State */
  let obstacles=[],nextObs=80,particles=[],state='idle';
  let score=0,hi=0,last=0,speed=BASE_SPD,elapsed=0,flashTimer=0,trail=[];
  let planetAngOffset=0;

  /* Milestones */
  const milestones = [
      {s: 50, m: "Annmary is a visual storyteller."},
      {s: 150, m: "BFA Animation @ NTU ADM."},
      {s: 250, m: "Selected for Annecy 2025."},
      {s: 350, m: "Multidisciplinary creative."},
      {s: 450, m: "Animator, Illustrator, Designer."}
  ];
  let curMilestone = null;
  let milestoneTimer = 0;
  
  /* Input */
  function tryJump(){
    if(state==='idle'||state==='dead'){startGame();return;}
    if(star.jumps<2){
      star.vy=star.jumps===0?JUMP_V:DBLJ_V;
      star.grounded=false;star.jumps++;
      starSX=0.65;starSY=1.48;
      spawnJumpPfx();jumpHeld=true;
    }
  }
  function releaseJump(){jumpHeld=false;}
  document.addEventListener('keydown',e=>{if(e.code==='Space'||e.code==='ArrowUp'){e.preventDefault();tryJump();}});
  document.addEventListener('keyup',e=>{if(e.code==='Space'||e.code==='ArrowUp')releaseJump();});
  canvas.addEventListener('touchstart',e=>{e.preventDefault();tryJump();},{passive:false});
  canvas.addEventListener('touchend',e=>{e.preventDefault();releaseJump();},{passive:false});
  canvas.addEventListener('mousedown',tryJump);
  canvas.addEventListener('mouseup',releaseJump);
  
  /* Start */
  function startGame(){
    state='running';score=0;speed=BASE_SPD;elapsed=0;planetAngOffset=0;
    star={x:STAR_X,y:GY-STAR_R,vy:0,rot:0,grounded:true,jumps:0};
    starSX=1;starSY=1;wasGrounded=true;
    obstacles=[];particles=[];trail=[];nextObs=80;flashTimer=0;
    curMilestone=null;milestoneTimer=0;
    promptEl.style.opacity='0';statusMsg.textContent='Orbit maintained.';
  }
  
  function obsGap(){
    const base=85-Math.floor(elapsed/320)*5;
    return Math.max(Math.floor(base+Math.random()*88),38);
  }
  
  function spawnObs(){
    const tier=score<100?0:score<220?1:2;
    const r=Math.random();
    let variant,w,h;
    
    // Spawn a crater or a rock
    if(Math.random() < 0.25) {
        variant = 'crater';
        w = 35 + Math.random()*25;
        h = 20; // depth
    } else {
        if(tier===0){
          if(r<.50){variant='rock';w=20+r*38;h=15+Math.random()*20;}
          else if(r<.78){variant='pillar';w=10+Math.random()*9;h=26+Math.random()*26;}
          else{variant='cluster';w=32+Math.random()*24;h=13+Math.random()*13;}
        } else if(tier===1){
          if(r<.32){variant='rock';w=26+Math.random()*26;h=22+Math.random()*26;}
          else if(r<.58){variant='pillar';w=12+Math.random()*10;h=34+Math.random()*30;}
          else if(r<.78){variant='cluster';w=38+Math.random()*28;h=18+Math.random()*15;}
          else{variant='double';w=18+Math.random()*14;h=44+Math.random()*18;}
        } else {
          if(r<.28){variant='rock';w=30+Math.random()*28;h=28+Math.random()*28;}
          else if(r<.52){variant='pillar';w=14+Math.random()*12;h=44+Math.random()*32;}
          else if(r<.72){variant='double';w=20+Math.random()*16;h=50+Math.random()*20;}
          else{variant='cluster';w=46+Math.random()*30;h=22+Math.random()*18;}
        }
    }
    
    const dist = CW - STAR_X + 60;
    const ang = dist / PLANET_R;
    obstacles.push({ang, variant, w, h, scored:false});
  }
  
  /* Particles */
  function spawnJumpPfx(){
    for(let i=0;i<8;i++){
      const a=Math.PI+(Math.random()-.5)*1.2;
      particles.push({x:star.x,y:star.y+STAR_R*.7,vx:Math.cos(a)*(1+Math.random()*3),vy:Math.sin(a)*(1+Math.random()*3)-.5,life:1,decay:.06+Math.random()*.04,r:.8+Math.random()*1.8,col:'rgba(255,255,255,1)',type:'d'});
    }
  }
  function spawnLandPfx(){
    for(let i=0;i<6;i++){
      particles.push({x:star.x+(Math.random()-.5)*STAR_R,y:star.y+STAR_R,vx:(Math.random()-.5)*3,vy:-(Math.random()*2.2),life:1,decay:.07+Math.random()*.05,r:.7+Math.random()*1.5,col:'rgba(200,196,228,1)',type:'d'});
    }
  }
  function spawnDeathPfx(){
    const cols=['#D93020','#FF6654','#E8B000','#FF9944','#FF4433'];
    for(let i=0;i<28;i++){
      const a=Math.random()*Math.PI*2,sp=2+Math.random()*7;
      particles.push({x:star.x,y:star.y,vx:Math.cos(a)*sp,vy:Math.sin(a)*sp-2,life:1,decay:.02+Math.random()*.03,r:2+Math.random()*4,col:cols[Math.floor(Math.random()*cols.length)],type:'s'});
    }
  }
  function spawnScorePfx(x,y){
    for(let i=0;i<5;i++){
      particles.push({x,y,vx:(Math.random()-.5)*2,vy:-1-Math.random()*2.5,life:1,decay:.06,r:1,col:'rgba(255,255,255,.75)',type:'d'});
    }
  }
  
  /* DRAWING HELPERS */
  function drawStar(x,y,r,rot,sx,sy){
    ctx.save();ctx.translate(x,y);ctx.rotate(rot);ctx.scale(sx,sy);
    ctx.shadowColor='rgba(217,48,32,.85)';ctx.shadowBlur=8+sy*9;
    ctx.beginPath();
    for(let i=0;i<10;i++){
      const a=(i*Math.PI/5)-Math.PI/2,rad=i%2===0?r:r*.42;
      i===0?ctx.moveTo(Math.cos(a)*rad,Math.sin(a)*rad):ctx.lineTo(Math.cos(a)*rad,Math.sin(a)*rad);
    }
    ctx.closePath();
    const rg=ctx.createRadialGradient(0,-r*.3,1,0,0,r);
    rg.addColorStop(0,'#FF7060');rg.addColorStop(.5,'#D93020');rg.addColorStop(1,'#7A1208');
    ctx.fillStyle=rg;ctx.fill();
    ctx.save();ctx.clip();
    ctx.strokeStyle='rgba(0,0,0,.22)';ctx.lineWidth=.65;
    for(let xi=-r;xi<r;xi+=2.5){ctx.beginPath();ctx.moveTo(xi,-r);ctx.lineTo(xi+2.5,r);ctx.stroke();}
    ctx.restore();
    ctx.shadowBlur=0;
    ctx.strokeStyle='rgba(255,255,255,.18)';ctx.lineWidth=.9;ctx.stroke();
    ctx.beginPath();ctx.arc(-r*.18,-r*.3,r*.16,0,Math.PI*2);
    ctx.fillStyle='rgba(255,180,160,.42)';ctx.fill();
    ctx.restore();
  }

  const obsImgs = {
    rock: new Image(), pillar: new Image(), cluster: new Image(), double: new Image()
  };
  obsImgs.rock.src = 'assets/rocks/rock.svg';
  obsImgs.pillar.src = 'assets/rocks/double.svg';
  obsImgs.cluster.src = 'assets/rocks/cluster.svg';
  obsImgs.double.src = 'assets/rocks/double.svg';
  
  /* HIT TEST */
  function hitTest(){
    const HR=STAR_R*.58;
    for(const o of obstacles){
      const linearX = STAR_X + (o.ang * PLANET_R);
      const l = linearX - o.w/2;
      const r = linearX + o.w/2;
      
      if(o.variant === 'crater') {
          // If star is directly over crater horizontally
          // And Y is near the ground level (it didn't jump over the crater)
          if(star.x > l + 5 && star.x < r - 5) { // generous hitbox
              if(star.y >= GY - STAR_R - 5) return true;
          }
      } else {
          const t = GY - o.h;
          const nx=Math.max(l,Math.min(star.x,r)),ny=Math.max(t,Math.min(star.y,GY));
          if(Math.hypot(star.x-nx,star.y-ny)<HR)return true;
      }
    }
    return false;
  }
  
  /* UPDATE */
  function update(){
    if(state!=='running')return;
    elapsed++;
    speed=Math.min(MAX_SPD,BASE_SPD+elapsed*SPD_INC);
    score=Math.floor(elapsed/5);
    scoreDisp.textContent=score;
    
    // Milestones
    const reached = milestones.find(m => score === m.s);
    if(reached && (!curMilestone || curMilestone.s !== reached.s)){
        curMilestone = reached;
        milestoneTimer = 220; // about 3.5 seconds
    }
    if(milestoneTimer > 0) milestoneTimer--;

    trail.unshift({x:star.x,y:star.y,life:1});
    if(trail.length>20)trail.pop();
    trail.forEach(p=>p.life-=.055);
    
    const g=jumpHeld&&star.vy<0?GRAVITY*.6:GRAVITY;
    star.vy+=g;star.y+=star.vy;
    
    if(star.y>=GY-STAR_R){
      if(!wasGrounded){spawnLandPfx();starSX=1.52;starSY=0.58;}
      star.y=GY-STAR_R;star.vy=0;star.grounded=true;star.jumps=0;
    } else star.grounded=false;
    
    if(star.y<CEIL_Y){star.y=CEIL_Y;star.vy=Math.max(star.vy,0);}
    wasGrounded=star.grounded;
    
    starSX+=(1-starSX)*.2;starSY+=(1-starSY)*.2;
    star.rot+=star.grounded?.022:.1;
  
    const angularSpeed = speed / PLANET_R;
    planetAngOffset -= angularSpeed;

    nextObs--;
    if(nextObs<=0){spawnObs();nextObs=obsGap();}
    
    for(const o of obstacles){
        o.ang -= angularSpeed;
        const linearX = STAR_X + (o.ang * PLANET_R);
        if(!o.scored && linearX + o.w/2 < star.x){
            o.scored=true;
            spawnScorePfx(star.x,star.y-STAR_R);
        }
    }
    obstacles=obstacles.filter(o=> (o.ang * PLANET_R) > -100);
    
    if(hitTest())die();
    
    BG_STARS.forEach(s=>{s.x-=s.speed;if(s.x<0)s.x=CW;s.twinkle+=s.twinkleSpd;});
    SHOOTS.forEach(s=>{
      if(s.delay>0){s.delay--;return;}
      if(!s.active){s.active=true;s.life=0;}
      s.x+=s.vx;s.y+=s.vy;s.life++;
      if(s.life<8)s.alpha=s.life/8;
      else if(s.x<-70||s.y>GY+10){
          Object.assign(s, mkShoot());
      }
      else s.alpha=Math.max(0,s.alpha-.016);
    });
    
    particles.forEach(p=>{p.x+=p.vx;p.y+=p.vy;p.vy+=.11;p.life-=p.decay;});
    particles=particles.filter(p=>p.life>0);
    if(flashTimer>0)flashTimer--;
  }
  
  function die(){
    state='dead';last=score;if(score>hi)hi=score;
    hiDisp.textContent=hi;lastDisp.textContent=last;
    spawnDeathPfx();flashTimer=14;
    promptEl.style.opacity='1';
    promptEl.innerHTML='<span>Space</span> / tap to re-launch';
    statusMsg.textContent='Signal lost.';
  }
  
  /* DRAW */
  function draw(){
    if(flashTimer>0&&flashTimer%2===0){ctx.fillStyle='rgba(217,48,32,.13)';ctx.fillRect(0,0,CW,CH);return;}
    ctx.clearRect(0,0,CW,CH);
    
    // Sky
    ctx.fillStyle='#050407';ctx.fillRect(0,0,CW,CH);
    
    // Background Stars
    ctx.fillStyle='#F0EEF5';
    BG_STARS.forEach(s=>{
      ctx.globalAlpha=Math.abs(Math.sin(s.twinkle));
      ctx.beginPath();ctx.arc(s.x,s.y,s.r,0,Math.PI*2);ctx.fill();
    });
    ctx.globalAlpha=1;
    
    // Shooting Stars
    ctx.lineWidth=1.5;
    SHOOTS.forEach(s=>{
      if(!s.active)return;
      ctx.globalAlpha=s.alpha;
      const grad=ctx.createLinearGradient(s.x,s.y,s.x-s.vx*5,s.y-s.vy*5);
      grad.addColorStop(0,'rgba(255,255,255,1)');grad.addColorStop(1,'rgba(255,255,255,0)');
      ctx.strokeStyle=grad;
      ctx.beginPath();ctx.moveTo(s.x,s.y);ctx.lineTo(s.x-s.vx*(s.len/10),s.y-s.vy*(s.len/10));ctx.stroke();
    });
    ctx.globalAlpha=1;

    const CX = STAR_X;
    const CY = GY + PLANET_R;
    
    ctx.save();
    ctx.translate(CX, CY);
    
    // Draw base moon
    ctx.beginPath();
    ctx.arc(0, 0, PLANET_R, 0, Math.PI*2);
    ctx.fillStyle = '#0a080c'; // Slightly off-bg to distinguish
    ctx.fill();
    ctx.lineWidth = 1.2;
    ctx.strokeStyle = 'rgba(240,238,245,0.4)';
    ctx.stroke();

    // Draw Moon Dots (Craters / Texture)
    ctx.fillStyle = 'rgba(240,238,245,0.1)';
    MOON_DOTS.forEach(d => {
        const a = d.ang + planetAngOffset;
        const rad = PLANET_R - d.depth;
        const dx = Math.sin(a) * rad;
        const dy = -Math.cos(a) * rad;
        ctx.beginPath(); ctx.arc(dx, dy, d.r, 0, Math.PI*2); ctx.fill();
    });

    // Draw Obstacles & Craters
    obstacles.forEach(o => {
        ctx.save();
        ctx.rotate(o.ang);
        
        if (o.variant === 'crater') {
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
            ctx.stroke();
        } else {
            if(obsImgs[o.variant] && obsImgs[o.variant].complete){
                ctx.drawImage(obsImgs[o.variant], -o.w/2, -PLANET_R - o.h + 1, o.w, o.h);
            } else {
                ctx.fillStyle = 'rgba(240,238,245,0.2)';
                ctx.fillRect(-o.w/2, -PLANET_R - o.h, o.w, o.h);
            }
        }
        ctx.restore();
    });
    ctx.restore();
    
    // Player Trail
    ctx.beginPath();
    trail.forEach((p,i)=>{
      ctx.lineWidth=p.life*5;ctx.strokeStyle=`rgba(217,48,32,${p.life*.4})`;
      i===0?ctx.moveTo(p.x,p.y):ctx.lineTo(p.x,p.y);
    });
    ctx.stroke();
    
    // Player
    if(state!=='dead') drawStar(star.x,star.y,STAR_R,star.rot,starSX,starSY);
    
    // Particles
    particles.forEach(p=>{
      ctx.fillStyle=p.col;ctx.beginPath();
      if(p.type==='s') ctx.rect(p.x-p.r,p.y-p.r,p.r*2,p.r*2);
      else ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
      ctx.fill();
    });

    // Milestones
    if (curMilestone && milestoneTimer > 0) {
        ctx.save();
        const alpha = milestoneTimer > 180 ? (220 - milestoneTimer)/40 : (milestoneTimer < 40 ? milestoneTimer/40 : 1);
        ctx.globalAlpha = Math.max(0, Math.min(1, alpha));
        ctx.fillStyle = '#F0EEF5';
        ctx.textAlign = 'center';
        ctx.font = '600 clamp(0.7rem, 2.5vw, 1.1rem) "Clash Display", sans-serif';
        ctx.shadowColor = 'rgba(5,4,7,0.9)';
        ctx.shadowBlur = 8;
        ctx.fillText(curMilestone.m, CW/2, CH * 0.35);
        ctx.restore();
    }
    
    // Intro Prompt
    if(state==='idle'){
      ctx.fillStyle='rgba(240,238,245,.8)';ctx.textAlign='center';
      ctx.font='500 1rem "General Sans",sans-serif';
      ctx.fillText('Press Space to Launch',CW/2,CH/2);
    }
  }
  
  function loop(){update();draw();requestAnimationFrame(loop);}
  requestAnimationFrame(loop);
</script>"""

html = re.sub(r'<script>.*?</script>', new_script, html, flags=re.DOTALL)

with open('game.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Game overwritten with lunar logic.")
