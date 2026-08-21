/* content.js — Loads data.json and renders all portfolio content */

async function loadData() {
  const res = await fetch('data/data.json');
  return res.json();
}

function imgOrPlaceholder(src, emoji, label) {
  if (src && src !== '') {
    return `<img src="${src}" alt="${label}" loading="lazy" />`;
  }
  return `
    <div class="project-card__img-placeholder">
      <div class="ph-icon">${emoji}</div>
      <span>Image coming soon</span>
    </div>`;
}

function renderProjectCard(proj, sectionColor) {
  const hasLink = proj.link && proj.link !== '';
  const tag = proj.isFlagship
    ? `<span class="project-card__flagship"><span class="tag tag--yellow">★ Flagship Case Study</span></span>`
    : proj.highlight
    ? `<div class="project-card__highlight">${proj.highlight}</div>`
    : '';

  const emojiMap = {
    animation: '🎬', illustration: '🎨', videography: '📹',
    'graphic-design': '✏️', music: '🎵'
  };
  const emoji = Object.keys(emojiMap).find(k => proj.tags && proj.tags.includes(k))
    ? emojiMap[Object.keys(emojiMap).find(k => proj.tags && proj.tags.includes(k))]
    : '🖼️';

  const overlayLink = hasLink
    ? `<a href="${proj.link}" class="project-card__overlay-link">View Case Study →</a>`
    : `<span class="project-card__overlay-link" style="opacity:0.7">Coming Soon</span>`;

  const tools = (proj.tools || []).slice(0, 3)
    .map(t => `<span class="project-card__tool">${t}</span>`)
    .join('');

  const wrapper = hasLink ? `a href="${proj.link}"` : 'div';
  const wrapperClose = hasLink ? 'a' : 'div';

  return `
    <article class="project-card reveal" id="proj-${proj.id}">
      <div class="project-card__img">
        ${imgOrPlaceholder(proj.image, emoji, proj.title)}
        ${tag}
        <div class="project-card__overlay">${overlayLink}</div>
      </div>
      <div class="project-card__body">
        <div class="project-card__year">${proj.year} · ${proj.client}</div>
        <h3 class="project-card__title">${proj.title}</h3>
        <p class="project-card__role">${proj.role}</p>
        <div class="project-card__tools">${tools}</div>
      </div>
    </article>`;
}

function renderSection(section, index) {
  const isEven = index % 2 === 1;
  const cards = section.projects.map(p => renderProjectCard(p, section.color)).join('');

  return `
    <section class="portfolio-section" id="${section.id}">
      <div class="container">
        <div class="section__header">
          <div>
            <p class="section__eyebrow reveal">0${index + 1} / 05</p>
            <h2 class="section__title reveal reveal-delay-1">${section.label}</h2>
            <p class="section__intro reveal reveal-delay-2">${section.intro}</p>
          </div>
          <a href="#" class="section__dl reveal reveal-delay-3" download>
            ↓ Download PDF
          </a>
        </div>
        <div class="project-grid">
          ${cards}
        </div>
      </div>
    </section>`;
}

function renderDownloads(data) {
  const sections = [
    { key: 'animation',      icon: '🎬', label: 'Animation & Visual Dev',    color: 'blue' },
    { key: 'illustration',   icon: '🎨', label: 'Illustration & Comics',      color: 'red' },
    { key: 'videography',    icon: '📹', label: 'Videography & Motion',       color: 'blue' },
    { key: 'graphicDesign',  icon: '✏️', label: 'Graphic Design & Brand',     color: 'red' },
    { key: 'musicProduction',icon: '🎵', label: 'Music Production',           color: 'yellow' },
  ];

  const btns = sections.map(s => `
    <a href="${data.downloads[s.key] || '#'}" class="dl-btn" download>
      <span class="dl-btn__icon dl-btn__icon--${s.color}">${s.icon}</span>
      <span class="dl-btn__text">
        <span class="dl-btn__label">Portfolio PDF</span>
        <span>${s.label}</span>
      </span>
    </a>`).join('');

  return `
    <section class="downloads" id="downloads">
      <div class="container downloads__inner">
        <div class="downloads__header">
          <h2 class="downloads__title">Don't want to scroll? <em>Download my portfolio.</em></h2>
        </div>
        <div class="downloads__grid">${btns}</div>
        <div class="downloads__featured">
          <a href="${data.downloads.fullPortfolio || '#'}" class="dl-btn dl-btn--featured" download>
            <span class="dl-btn__icon dl-btn__icon--yellow">📁</span>
            <span class="dl-btn__text">
              <span class="dl-btn__label">Combined</span>
              <span>Full Portfolio PDF</span>
            </span>
          </a>
          <a href="${data.downloads.resume || '#'}" class="dl-btn dl-btn--featured" download>
            <span class="dl-btn__icon dl-btn__icon--blue">📄</span>
            <span class="dl-btn__text">
              <span class="dl-btn__label">CV / Résumé</span>
              <span>Download Resume</span>
            </span>
          </a>
        </div>
      </div>
    </section>`;
}

function renderHero(data) {
  const { hero } = data;
  const disciplines = hero.subheadline.split(' · ').map(d =>
    `<span class="tag tag--blue">${d}</span>`).join('');

  const trust = hero.trustSignals.map(t => `
    <div class="hero__trust-item">
      <div class="hero__trust-label">${t.label}</div>
      <div class="hero__trust-detail">${t.detail}</div>
    </div>`).join('');

  const headlineParts = hero.headline.split('\n');
  const headlineHTML = headlineParts.map((p, i) =>
    i === 0 ? p : `<em>${p}</em>`).join('\n');

  return `
    <section class="hero" id="home">
      <div class="container" style="display:contents">
        <div class="hero__bg-text" aria-hidden="true">AMS</div>
        <div class="hero__content" style="padding: 0 clamp(1.5rem,5vw,4rem)">
          <div class="hero__eyebrow reveal">
            <span class="hero__eyebrow-dot"></span>
            <span class="t-label">Portfolio 2026</span>
          </div>
          <h1 class="hero__headline reveal reveal-delay-1">${headlineHTML}</h1>
          <p class="hero__tagline reveal reveal-delay-2">${hero.tagline}</p>
          <div class="hero__disciplines reveal reveal-delay-3">${disciplines}</div>
          <div class="hero__trust reveal reveal-delay-4">${trust}</div>
        </div>
        <div class="hero__visual" style="padding: 0 clamp(1.5rem,5vw,4rem)">
          <div class="hero__collage-wrap reveal">
            <video autoplay muted loop playsinline>
              <source src="assets/hero-collage.mp4" type="video/mp4" />
            </video>
            <span class="hero__chip hero__chip--1">Annecy 2025 ✦</span>
            <span class="hero__chip hero__chip--2">50+ Commissions</span>
            <span class="hero__chip hero__chip--3">BFA Animation</span>
          </div>
        </div>
      </div>
    </section>`;
}

function renderAbout(data) {
  const { about } = data;
  const facts = about.funFacts.map(f => `
    <div class="about__fact">
      <span class="about__fact-emoji">${f.emoji}</span>
      <span class="about__fact-label">${f.label}</span>
      <span class="about__fact-value">${f.value}</span>
    </div>`).join('');

  const photoHTML = about.photo && about.photo !== ''
    ? `<img src="${about.photo}" alt="Ann Mary Saji" />`
    : `<div class="about__photo-placeholder">Photo coming soon</div>`;

  return `
    <section class="about" id="about">
      <div class="container">
        <div class="about__grid">
          <div class="reveal">
            <p class="about__eyebrow">About</p>
            <h2 class="about__title">One person.<br><em>Many mediums.</em></h2>
            <p class="about__bio">${about.bio}</p>
            <div class="about__facts">${facts}</div>
            <div class="about__awards" style="margin-top:2rem">
              <div class="about__awards-title">Awards & Recognition</div>
              <div class="award-item">
                <div class="award-item__badge">🏆</div>
                <div class="award-item__text">
                  <span class="award-item__name">Annecy International Animation Film Festival</span><br>
                  Selected & Screened — Keep Yourself Safe (2025)
                </div>
              </div>
              <div class="award-item">
                <div class="award-item__badge">🥈</div>
                <div class="award-item__text">
                  <span class="award-item__name">NTU × Imperial College London Design-a-thon</span><br>
                  2nd Place — ReKindle app concept
                </div>
              </div>
              <div class="award-item">
                <div class="award-item__badge">📜</div>
                <div class="award-item__text">
                  <span class="award-item__name">Marketing Certifications (Coursera, 2026)</span><br>
                  IE Business School · University of Virginia
                </div>
              </div>
            </div>
          </div>
          <div class="reveal reveal-delay-2">
            <div class="about__photo-wrap">${photoHTML}</div>
          </div>
        </div>
      </div>
    </section>`;
}

function renderContact(data) {
  const { contact } = data;
  return `
    <section class="contact" id="contact">
      <div class="container">
        <div class="contact__grid">
          <div class="reveal">
            <h2 class="contact__title">Let's make something together.</h2>
            <a href="mailto:${contact.email}" class="contact__email">${contact.email}</a>
            <div class="contact__socials">
              <a href="${contact.linkedin}" target="_blank" rel="noopener" class="social-link">
                <span class="social-link__icon">💼</span> LinkedIn — annmary-saji
              </a>
              <a href="${contact.instagram}" target="_blank" rel="noopener" class="social-link">
                <span class="social-link__icon">📸</span> Instagram — @loudarmybombs
              </a>
              <a href="${contact.resumePDF}" class="social-link" download>
                <span class="social-link__icon">📄</span> Download Resume PDF
              </a>
            </div>
          </div>
          <div class="reveal reveal-delay-2">
            <form class="contact-form" onsubmit="handleFormSubmit(event)">
              <div class="form-group">
                <label class="form-label" for="cf-name">Your Name</label>
                <input id="cf-name" class="form-input" type="text" placeholder="Jane Smith" required />
              </div>
              <div class="form-group">
                <label class="form-label" for="cf-email">Email Address</label>
                <input id="cf-email" class="form-input" type="email" placeholder="jane@studio.com" required />
              </div>
              <div class="form-group">
                <label class="form-label" for="cf-msg">Message</label>
                <textarea id="cf-msg" class="form-textarea" placeholder="Tell me about your project…" required></textarea>
              </div>
              <button type="submit" class="form-submit" id="form-submit-btn">Send Message →</button>
            </form>
          </div>
        </div>
      </div>
    </section>`;
}

// Scroll reveal
function initReveal() {
  const els = document.querySelectorAll('.reveal');
  const obs = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); } });
  }, { threshold: 0.1 });
  els.forEach(el => obs.observe(el));
}

// Nav scroll behaviour
function initNav() {
  const nav = document.querySelector('.nav');
  if (!nav) return;
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 60);
  });
}

// Active filter from gateway
function getFilter() {
  const params = new URLSearchParams(window.location.search);
  return params.get('filter') || 'all';
}

function applyFilter(filter, sections) {
  if (filter === 'all') return sections;
  const filterMap = {
    'animation-illustration': ['animation', 'illustration'],
    'design-video': ['graphic-design', 'videography'],
  };
  const allowed = filterMap[filter];
  if (!allowed) return sections;
  return sections.filter(s => allowed.includes(s.id));
}

window.handleFormSubmit = function(e) {
  e.preventDefault();
  const btn = document.getElementById('form-submit-btn');
  btn.textContent = 'Sent ✓';
  btn.style.background = '#1850A8';
  setTimeout(() => { btn.textContent = 'Send Message →'; btn.style.background = ''; }, 3000);
};

// Main init
async function init() {
  const app = document.getElementById('app');
  if (!app) return;

  const data = await loadData();
  const filter = getFilter();
  const visibleSections = applyFilter(filter, data.sections);

  let html = renderHero(data);
  html += renderDownloads(data);
  visibleSections.forEach((s, i) => { html += renderSection(s, i); });
  html += renderAbout(data);
  html += renderContact(data);

  app.innerHTML = html;

  initNav();
  initReveal();

  // Trigger reveal for hero elements immediately
  setTimeout(() => {
    document.querySelectorAll('.hero .reveal').forEach(el => el.classList.add('visible'));
  }, 100);
}

document.addEventListener('DOMContentLoaded', init);
