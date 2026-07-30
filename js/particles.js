// ── Gold Particle Canvas ─────────────────────────────────────
function initParticles(canvasId) {
  const canvas = document.getElementById(canvasId);
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let particles = [];
  let animId;

  function resize() {
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
  }

  class Particle {
    constructor() { this.reset(); }
    reset() {
      this.x = Math.random() * canvas.width;
      this.y = Math.random() * canvas.height;
      this.size = Math.random() * 2 + 0.5;
      this.speedX = (Math.random() - 0.5) * 0.4;
      this.speedY = -(Math.random() * 0.6 + 0.2);
      this.opacity = Math.random() * 0.6 + 0.2;
      this.life = 0;
      this.maxLife = Math.random() * 200 + 100;
    }
    update() {
      this.x += this.speedX;
      this.y += this.speedY;
      this.life++;
      const lifeRatio = this.life / this.maxLife;
      this.opacity = lifeRatio < 0.2 ? lifeRatio * 5 * 0.8 : lifeRatio > 0.8 ? (1 - lifeRatio) * 5 * 0.8 : 0.8;
      if (this.life >= this.maxLife) this.reset();
    }
    draw() {
      ctx.save();
      ctx.globalAlpha = this.opacity * 0.7;
      ctx.fillStyle = `hsl(${38 + Math.random() * 10}, 65%, ${60 + Math.random() * 15}%)`;
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();
    }
  }

  function init() {
    resize();
    particles = Array.from({ length: 80 }, () => {
      const p = new Particle();
      p.life = Math.random() * p.maxLife; // stagger start
      return p;
    });
  }

  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(p => { p.update(); p.draw(); });
    animId = requestAnimationFrame(animate);
  }

  window.addEventListener('resize', () => { resize(); });
  init();
  animate();
}

initParticles('particleCanvas');
