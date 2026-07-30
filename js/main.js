// ============================================================
// RASHMÉ — Main JS
// ============================================================

document.addEventListener('DOMContentLoaded', () => {
  // 1. Page Load Curtain Reveal
  setTimeout(() => {
    const curtain = document.getElementById('curtain');
    if (curtain) {
      curtain.classList.add('gone');
    }
  }, 100);

  // 2. Navbar Scroll State
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    });
  }

  // 3. Mobile Hamburger Menu
  const hamburger = document.querySelector('.navbar__hamburger');
  const mobileMenu = document.querySelector('.navbar__mobile');
  let menuOpen = false;

  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => {
      menuOpen = !menuOpen;
      hamburger.classList.toggle('open', menuOpen);
      mobileMenu.classList.toggle('open', menuOpen);
      document.body.style.overflow = menuOpen ? 'hidden' : '';
    });

    // Close menu when clicking a link
    const mobileLinks = mobileMenu.querySelectorAll('.navbar__mobile-link, .btn');
    mobileLinks.forEach(link => {
      link.addEventListener('click', () => {
        menuOpen = false;
        hamburger.classList.remove('open');
        mobileMenu.classList.remove('open');
        document.body.style.overflow = '';
      });
    });
  }

  // 4. Scroll Reveal Animations (Intersection Observer)
  const revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right');
  
  const observerOptions = {
    root: null,
    rootMargin: '0px 0px -80px 0px',
    threshold: 0.1
  };

  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target); // Only animate once
      }
    });
  }, observerOptions);

  revealElements.forEach(el => {
    revealObserver.observe(el);
  });

  // 5. Image Sliders
  document.querySelectorAll('.slider-box').forEach(box => {
    const slider = box.querySelector('.slider');
    const prev = box.querySelector('.prev');
    const next = box.querySelector('.next');
    if(slider && prev && next) {
      prev.addEventListener('click', () => {
        slider.scrollBy({ left: -slider.clientWidth, behavior: 'smooth' });
      });
      next.addEventListener('click', () => {
        slider.scrollBy({ left: slider.clientWidth, behavior: 'smooth' });
      });
    }
  });

  // Set active nav link based on current URL
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.navbar__link').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });
});
