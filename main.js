document.addEventListener('DOMContentLoaded', () => {
  // 2. Theme Toggle (Dark/Light Mode)
  const themeToggle = document.getElementById('themeToggle');
  const themeIcon = themeToggle.querySelector('.theme-icon');
  const html = document.documentElement;

  // Check saved theme or system preference
  const savedTheme = localStorage.getItem('theme');
  const systemDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  
  if (savedTheme === 'dark' || (!savedTheme && systemDark)) {
    html.setAttribute('data-theme', 'dark');
    themeIcon.classList.replace('fa-moon', 'fa-sun');
  }

  themeToggle.addEventListener('click', () => {
    const currentTheme = html.getAttribute('data-theme');
    if (currentTheme === 'dark') {
      html.setAttribute('data-theme', 'light');
      localStorage.setItem('theme', 'light');
      themeIcon.classList.replace('fa-sun', 'fa-moon');
    } else {
      html.setAttribute('data-theme', 'dark');
      localStorage.setItem('theme', 'dark');
      themeIcon.classList.replace('fa-moon', 'fa-sun');
    }
  });

  // 3. Navbar Scroll Effect
  const navbar = document.getElementById('navbar');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      navbar.style.padding = '1rem 0';
      navbar.style.boxShadow = 'var(--shadow-md)';
    } else {
      navbar.style.padding = '1.5rem 0';
      navbar.style.boxShadow = 'none';
    }
  });

  // 4. Typing Effect for Hero Section
  const typedTextSpan = document.getElementById('typedText');
  const textArray = ["Fasilitator Pembelajaran", "Inovator Pendidikan", "Guru Profesional"];
  const typingDelay = 100;
  const erasingDelay = 50;
  const newTextDelay = 2000; // Delay between current and next text
  let textArrayIndex = 0;
  let charIndex = 0;

  function type() {
    if (charIndex < textArray[textArrayIndex].length) {
      typedTextSpan.textContent += textArray[textArrayIndex].charAt(charIndex);
      charIndex++;
      setTimeout(type, typingDelay);
    } 
    else {
      setTimeout(erase, newTextDelay);
    }
  }

  function erase() {
    if (charIndex > 0) {
      typedTextSpan.textContent = textArray[textArrayIndex].substring(0, charIndex-1);
      charIndex--;
      setTimeout(erase, erasingDelay);
    } 
    else {
      textArrayIndex++;
      if (textArrayIndex >= textArray.length) textArrayIndex = 0;
      setTimeout(type, typingDelay + 1100);
    }
  }

  if (textArray.length) setTimeout(type, newTextDelay + 250);

  // 5. Particle Canvas Background
  const canvas = document.getElementById('particleCanvas');
  const ctx = canvas.getContext('2d');
  
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  canvas.style.position = 'fixed';
  canvas.style.top = '0';
  canvas.style.left = '0';
  canvas.style.zIndex = '-1';
  canvas.style.opacity = '0.3';

  let particlesArray = [];
  const numberOfParticles = 50;

  class Particle {
    constructor() {
      this.x = Math.random() * canvas.width;
      this.y = Math.random() * canvas.height;
      this.size = Math.random() * 3 + 1;
      this.speedX = Math.random() * 1 - 0.5;
      this.speedY = Math.random() * 1 - 0.5;
      this.color = document.documentElement.getAttribute('data-theme') === 'dark' ? '#ffffff' : '#FF6B6B';
    }
    update() {
      this.x += this.speedX;
      this.y += this.speedY;
      
      if (this.x > canvas.width) this.x = 0;
      if (this.x < 0) this.x = canvas.width;
      if (this.y > canvas.height) this.y = 0;
      if (this.y < 0) this.y = canvas.height;
    }
    draw() {
      ctx.fillStyle = this.color;
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fill();
    }
  }

  function init() {
    particlesArray = [];
    for (let i = 0; i < numberOfParticles; i++) {
      particlesArray.push(new Particle());
    }
  }

  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (let i = 0; i < particlesArray.length; i++) {
      particlesArray[i].update();
      particlesArray[i].draw();
    }
    requestAnimationFrame(animate);
  }

  init();
  animate();

  window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    init();
  });

  // 6. Portfolio Filters Toggle
  const switchBtns = document.querySelectorAll('.switch-btn');
  switchBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      switchBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    });
  });

  const siklusBtns = document.querySelectorAll('.tier-siklus .pill-btn');
  const categoryBtns = document.querySelectorAll('.tier-category .pill-btn-outline');
  const portfolioCards = document.querySelectorAll('.portfolio-card');

  function filterCards() {
    const activeSiklus = document.querySelector('.tier-siklus .pill-btn.active').getAttribute('data-siklus');
    const activeCategory = document.querySelector('.tier-category .pill-btn-outline.active').getAttribute('data-kategori');

    portfolioCards.forEach(card => {
      const cardSiklus = card.getAttribute('data-siklus');
      const cardCategory = card.getAttribute('data-kategori');

      const matchSiklus = activeSiklus === 'semua' || cardSiklus === activeSiklus;
      const matchCategory = activeCategory === 'semua' || cardCategory === activeCategory;

      if (matchSiklus && matchCategory) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
  }

  siklusBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      siklusBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      filterCards();
    });
  });

  categoryBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      categoryBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      filterCards();
    });
  });

  // 7. Analysis Panel Logic
  const analysisBtns = document.querySelectorAll('.btn-analysis');
  const analysisOverlay = document.getElementById('analysisOverlay');
  const closePanelBtns = document.querySelectorAll('.btn-close-panel');

  function openPanel(e) {
    e.preventDefault();
    const targetId = this.getAttribute('data-target');
    const panel = document.getElementById(targetId);
    if (panel) {
      analysisOverlay.classList.add('active');
      panel.classList.add('active');
      document.body.style.overflow = 'hidden'; // prevent background scrolling
    }
  }

  function closePanel() {
    analysisOverlay.classList.remove('active');
    document.querySelectorAll('.analysis-panel.active').forEach(p => p.classList.remove('active'));
    document.body.style.overflow = 'auto'; // restore background scrolling
  }

  analysisBtns.forEach(btn => {
    btn.addEventListener('click', openPanel);
  });

  closePanelBtns.forEach(btn => {
    btn.addEventListener('click', closePanel);
  });
  
  if (analysisOverlay) {
    analysisOverlay.addEventListener('click', closePanel);
  }
});
