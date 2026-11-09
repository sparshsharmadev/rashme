// ============================================================
// RASHMÉ — Main JS
// ============================================================

document.addEventListener('DOMContentLoaded', () => {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // 1. Page Load Curtain Reveal
  const curtain = document.getElementById('curtain');
  if (curtain) {
    setTimeout(() => curtain.classList.add('gone'), 150);
    setTimeout(() => { curtain.style.display = 'none'; }, 1300);
  }

  // 2. Scroll progress bar
  const progress = document.createElement('div');
  progress.className = 'scroll-progress';
  document.body.appendChild(progress);

  // 3. Navbar Scroll State + progress + parallax
  const navbar = document.querySelector('.navbar');
  const parallaxEls = Array.from(document.querySelectorAll('.hero__bg-img, .editorial-banner__bg'));
  let ticking = false;

  function renderScroll() {
    const y = window.scrollY;
    if (navbar) navbar.classList.toggle('scrolled', y > 40);

    const scrollable = document.documentElement.scrollHeight - window.innerHeight;
    progress.style.transform = `scaleX(${scrollable > 0 ? Math.min(y / scrollable, 1) : 0})`;

    if (!reduceMotion && window.innerWidth > 768) {
      const vh = window.innerHeight;
      parallaxEls.forEach(el => {
        const parent = el.parentElement;
        if (!parent) return;
        const rect = parent.getBoundingClientRect();
        if (rect.bottom < -200 || rect.top > vh + 200) return;
        const offset = (rect.top + rect.height / 2 - vh / 2) * -0.09;
        el.style.transform = `translate3d(0, ${offset.toFixed(2)}px, 0) scale(1.06)`;
      });
    }

    ticking = false;
  }

  window.addEventListener('scroll', () => {
    if (!ticking) {
      window.requestAnimationFrame(renderScroll);
      ticking = true;
    }
  }, { passive: true });
  renderScroll();

  // 4. Mobile Hamburger Menu
  const hamburger = document.querySelector('.navbar__hamburger');
  let mobileMenu = document.querySelector('.navbar__mobile');
  let menuOpen = false;

  // Build a mobile menu for pages that only ship the desktop navbar
  if (hamburger && !mobileMenu) {
    mobileMenu = document.createElement('div');
    mobileMenu.className = 'navbar__mobile';
    document.querySelectorAll('.navbar__link').forEach(link => {
      const item = document.createElement('a');
      item.href = link.getAttribute('href');
      item.className = 'navbar__mobile-link';
      item.textContent = link.textContent.trim();
      mobileMenu.appendChild(item);
    });
    const cta = document.createElement('a');
    cta.href = 'products.html';
    cta.className = 'btn btn-red';
    cta.style.marginTop = '2rem';
    cta.textContent = 'Buy Now';
    mobileMenu.appendChild(cta);
    document.body.appendChild(mobileMenu);
  }

  function setMenu(open) {
    menuOpen = open;
    if (!hamburger || !mobileMenu) return;
    hamburger.classList.toggle('open', menuOpen);
    hamburger.setAttribute('aria-expanded', String(menuOpen));
    hamburger.setAttribute('aria-label', menuOpen ? 'Close navigation menu' : 'Open navigation menu');
    mobileMenu.classList.toggle('open', menuOpen);
    document.body.classList.toggle('menu-open', menuOpen);
    document.body.style.overflow = menuOpen ? 'hidden' : '';
  }

  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => setMenu(!menuOpen));

    const mobileLinks = mobileMenu.querySelectorAll('.navbar__mobile-link, .btn');
    mobileLinks.forEach(link => {
      link.addEventListener('click', () => setMenu(false));
    });

    document.addEventListener('keydown', e => {
      if (e.key === 'Escape' && menuOpen) setMenu(false);
    });
  }

  // 5. Scroll Reveal Animations (Intersection Observer)
  const revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right');
  const isMobile = window.innerWidth <= 768;

  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, {
    root: null,
    rootMargin: isMobile ? '0px 0px 80px 0px' : '0px 0px -60px 0px',
    threshold: isMobile ? 0.01 : 0.08
  });

  revealElements.forEach(el => revealObserver.observe(el));

  // 6. Animated stat counters
  const statNums = document.querySelectorAll('.stats__num');
  if (statNums.length) {
    const counterObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        const el = entry.target;
        const raw = el.textContent.trim();
        const match = raw.match(/^([^\d]*)(\d+)(.*)$/);

        if (reduceMotion || !match) {
          observer.unobserve(el);
          return;
        }

        const prefix = match[1];
        const target = parseInt(match[2], 10);
        const suffix = match[3];
        const duration = 1400;
        const start = performance.now();

        function tick(now) {
          const p = Math.min((now - start) / duration, 1);
          const eased = 1 - Math.pow(1 - p, 3);
          el.textContent = prefix + Math.round(target * eased) + suffix;
          if (p < 1) requestAnimationFrame(tick);
        }

        requestAnimationFrame(tick);
        observer.unobserve(el);
      });
    }, { threshold: 0.6 });

    statNums.forEach(el => counterObserver.observe(el));
  }

  // 7. Image Sliders
  document.querySelectorAll('.slider-box').forEach(box => {
    const slider = box.querySelector('.slider');
    const prev = box.querySelector('.prev');
    const next = box.querySelector('.next');
    if (slider && prev && next) {
      prev.addEventListener('click', () => {
        slider.scrollBy({ left: -slider.clientWidth, behavior: 'smooth' });
      });
      next.addEventListener('click', () => {
        slider.scrollBy({ left: slider.clientWidth, behavior: 'smooth' });
      });
    }
  });

  // 8. Set active nav link based on current URL
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.navbar__link').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });

  // Ensure active mobile subnav link is scrolled into view smoothly
  const activeSubnavLink = document.querySelector('.navbar__links .navbar__link.active');
  if (activeSubnavLink) {
    const container = activeSubnavLink.closest('.navbar__links');
    if (container && container.scrollWidth > container.clientWidth) {
      const centerPos = activeSubnavLink.offsetLeft - (container.clientWidth / 2) + (activeSubnavLink.clientWidth / 2);
      container.scrollTo({ left: Math.max(0, centerPos), behavior: 'smooth' });
    }
  }
});
