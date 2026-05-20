// Cursor as repulsor: opposite of attractor. Lines near cursor get pushed
// horizontally away (sign depends on cursor's x-position). Uses
// getBoundingClientRect for line y-positions.

export const repulsor = {
  id: 'repulsor',

  enable() { document.body.classList.add('fx-repulsor'); },

  disable() {
    document.body.classList.remove('fx-repulsor');
    for (const ln of document.querySelectorAll('.code-line')) {
      ln.style.transform = '';
    }
  },

  tick() {
    const actives = document.querySelectorAll('.code-line.active');
    if (!actives.length) return;

    // Compute active y positions once
    const actYs = [...actives].map(a => {
      const r = a.getBoundingClientRect();
      return r.top + r.height / 2;
    });

    const lines = document.querySelectorAll('.code-line');
    lines.forEach(ln => {
      if (ln.classList.contains('active')) { ln.style.transform = ''; return; }
      const rect = ln.getBoundingClientRect();
      const y = rect.top + rect.height / 2;
      // Force from nearest active line (inverse distance)
      let force = 0;
      for (const ay of actYs) {
        const d = (y - ay);
        const f = 60 / (1 + Math.abs(d) * 0.05);   // 60px max, decays with distance
        // Direction: push away from active
        force += Math.sign(d) * f * Math.exp(-Math.abs(d) / 80);
      }
      ln.style.transform = `translateX(${force.toFixed(1)}px)`;
    });
  },
};
