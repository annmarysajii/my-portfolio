<script>

document.body.classList.add('js-on');



// CURSOR

const cur=document.getElementById('cur');

const sf=document.getElementById('sf');

const csq=document.getElementById('csq');

let mx=innerWidth/2,my=innerHeight/2,cx=mx,cy=my,lx=mx,ly=my,ang=0;

document.addEventListener('mousemove',e=>{mx=e.clientX;my=e.clientY;});

(function loop(){

  cx+=(mx-cx)*.16;cy+=(my-cy)*.16;

  cur.style.left=cx+'px';cur.style.top=cy+'px';

  const spd=Math.hypot(mx-lx,my-ly);lx=mx;ly=my;

  ang+=1.5+spd*.8;csq.style.transform='rotate('+ang+'deg)';

  requestAnimationFrame(loop);

})();

document.addEventListener('mouseover',e=>{

  const h=!!e.target.closest('a,button,.card,.soc,.dl-btn');

  const d=!!e.target.closest('.about,.foot,.dl-sec');

  cur.classList.toggle('hov',h);

  const isDark = document.documentElement.getAttribute('data-theme') === 'dark';

  sf.setAttribute('fill',d?'#E8B000':h?'#D93020':(isDark?'#F0EEF5':'#111009'));

});



// CANVAS STARS

const bgC=document.getElementById('bg-c');

if(bgC){

  const bgX=bgC.getContext('2d');

  let bW,bH;

  const HUES=[0,210,45];

  function rsz(){bW=bgC.width=innerWidth;bH=bgC.height=innerHeight;}

  window.addEventListener('resize',rsz);rsz();



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
        ctx.fillText('â™ª', 0, 0);
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

    ctx.closePath();

    ctx.fillStyle=color;ctx.fill();

    ctx.restore();

  }



  const STARS=Array.from({length:45},()=>({

    x:Math.random()*window.innerWidth,

    y:Math.random()*window.innerHeight,

    r:2.5+Math.random()*5,

    speed:.35+Math.random()*.55,

    drift:(Math.random()-.5)*.28,

    rot:Math.random()*Math.PI*2,

    spin:(Math.random()-.5)*.018,

    alpha:.08+Math.random()*.1,

    hue:HUES[Math.floor(Math.random()*3)],

    lit:0

  }));



  const isDark=()=>document.documentElement.getAttribute('data-theme')==='dark';



  function bgFrame(){

    bgX.clearRect(0,0,bW,bH);

    STARS.forEach(s=>{

      s.y+=s.speed;s.x+=s.drift;s.rot+=s.spin;

      if(s.y>bH+20){s.y=-20;s.x=Math.random()*bW;}



      const dist=Math.hypot(cx-s.x,cy-s.y);

      const prox=Math.max(0,1-dist/110);

      s.lit=Math.max(s.lit*.94,prox);



      const sz=s.r+(s.lit*6.5);

      const a=s.alpha+(s.lit*.6);

      const isDarkNow=isDark();

      const color=s.lit>.04

        ?`hsla(${s.hue},88%,52%,${a})`

        :isDarkNow?`rgba(240,238,245,${s.alpha})`:`rgba(17,16,9,${s.alpha})`;



      drawShape(bgX,s.x,s.y,sz,s.rot,color);

    });

    requestAnimationFrame(bgFrame);

  }

  bgFrame();

}



// DARK MODE

(function initTheme(){

  const saved=localStorage.getItem('theme')||'light';

  document.documentElement.setAttribute('data-theme',saved);

  const btn=document.getElementById('themeBtn');

  if(btn)btn.textContent=saved==='dark'?'â˜€':'ðŸŒ™';

})();

window.toggleTheme=function(){

  const dark=document.documentElement.getAttribute('data-theme')==='dark';

  const next=dark?'light':'dark';

  document.documentElement.setAttribute('data-theme',next);

  localStorage.setItem('theme',next);

  const btn=document.getElementById('themeBtn');

  if(btn)btn.textContent=next==='dark'?'â˜€':'ðŸŒ™';

  const sf=document.getElementById('sf');

  if(sf&&!document.querySelector('#cur').classList.contains('hov')) {

    sf.setAttribute('fill',next==='dark'?'#F0EEF5':'#111009');

  }

};



window.toggleMusic=function(){

  const m=document.getElementById('bg-music');

  const b=document.getElementById('musicBtn');

  if(m.paused){

    m.play().catch(e=>console.log('Music play prevented:',e));

    if(b)b.textContent='ðŸ”ˆ';

  } else {

    m.pause();

    if(b)b.textContent='ðŸ”ˆ';

  }

};



// NAV

const nav=document.getElementById('nav');

window.addEventListener('scroll',()=>nav.classList.toggle('sc',scrollY>60),{passive:true});



// Zoom entry

const f=new URLSearchParams(location.search).get('f');

if(f) document.body.classList.add('from-warp');

if(f==='about'){window.addEventListener('load',()=>{setTimeout(()=>document.getElementById('about')?.scrollIntoView({behavior:'smooth'}),900);});}

if(f&&f!=='all'&&f!=='about'){

  const m={anim:['animation','illustration'],brand:['graphic-design','videography']};

  const ids=m[f]||[];

  if(ids.length) document.querySelectorAll('.sec[id]').forEach(s=>{if(!ids.includes(s.id))s.style.display='none';});

}



// Reveal

const rvs=document.querySelectorAll('.rv');

if('IntersectionObserver' in window){

  const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('show');io.unobserve(e.target);}}),{threshold:.08});

  rvs.forEach(el=>io.observe(el));

}else{rvs.forEach(el=>el.classList.add('show'));}

requestAnimationFrame(()=>document.querySelectorAll('#hero .rv').forEach(el=>el.classList.add('show')));



// Smooth scroll

document.addEventListener('click',e=>{

  const a=e.target.closest('a[href^="#"]');

  if(!a)return;e.preventDefault();

  document.querySelector(a.getAttribute('href'))?.scrollIntoView({behavior:'smooth'});

});



// Page Transitions

document.addEventListener('click', e => {

  const a = e.target.closest('a[href]');

  if(a && !a.href.includes('#') && a.target !== '_blank' && a.hostname === location.hostname && !a.hasAttribute('download') && !a.getAttribute('href').startsWith('javascript:')){

    e.preventDefault();

    document.body.classList.add('page-exit');

    setTimeout(() => { window.location.href = a.href; }, 350);

  }

});



// Parallax Chips

const chips = document.querySelectorAll('.chip[data-speed]');

window.addEventListener('scroll', () => {

  const y = window.scrollY;

  chips.forEach(c => {

    const s = parseFloat(c.getAttribute('data-speed'));

    c.style.setProperty('--py', (y * s) + 'px');

  });

}, {passive:true});



// 3D Card Tilts

document.querySelectorAll('.card').forEach(card => {

  card.addEventListener('mousemove', e => {

    const rect = card.getBoundingClientRect();

    const x = e.clientX - rect.left;

    const y = e.clientY - rect.top;

    const centerX = rect.width / 2;

    const centerY = rect.height / 2;

    const rotateX = ((y - centerY) / centerY) * -4;

    const rotateY = ((x - centerX) / centerX) * 4;

    card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.01, 1.01, 1.01)`;

  });

  card.addEventListener('mouseleave', () => {

    card.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)`;

    card.style.transition = `transform 0.4s ease`;

  });

  card.addEventListener('mouseenter', () => {

    card.style.transition = `none`;

  });

});



// Magnetic Buttons

document.querySelectorAll('.magnetic').forEach(btn => {

  btn.addEventListener('mousemove', e => {

    const rect = btn.getBoundingClientRect();

    const x = e.clientX - rect.left - rect.width / 2;

    const y = e.clientY - rect.top - rect.height / 2;

    btn.style.transform = `translate(${x * 0.3}px, ${y * 0.3}px)`;

  });

  btn.addEventListener('mouseleave', () => {

    btn.style.transform = `translate(0px, 0px)`;

  });

});



// Form

window.sub=function(e){

  e.preventDefault();

  const b=document.getElementById('fsb');

  const p=document.getElementById('plane-icon');

  

  p.style.transform = 'translate(60px, -60px) scale(0.5)';

  p.style.opacity = '0';

  

  b.querySelector('span').textContent='Sent!';

  b.style.background='#1850A8';b.style.borderColor='#1850A8';b.style.color='#fff';

  

  setTimeout(()=>{

    b.querySelector('span').textContent='Send Message';

    b.style.background='';b.style.borderColor='';b.style.color='';

    p.style.transition = 'none';

    p.style.transform = 'translate(-30px, 30px) scale(0.5)';

    setTimeout(()=>{

      p.style.transition = 'transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.4s ease';

      p.style.transform = 'translate(0,0) scale(1)';

      p.style.opacity = '1';

    }, 50);

  },3000);

};

</script>
