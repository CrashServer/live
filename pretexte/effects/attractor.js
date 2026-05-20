// Cursor as gravitational attractor: lines near a cursor get boosted glow,
// tighter letter-spacing (code "tenses" near attention), and slight scale.
// Force drops off with line-distance from cursor (inverse-square-ish).

export const attractor = {
  id: 'attractor',

  enable() {
    document.body.classList.add('fx-attractor');
  },

  disable() {
    document.body.classList.remove('fx-attractor');
    for (const ln of document.querySelectorAll('.code-line')) {
      ln.style.removeProperty('--attract');
    }
  },

  tick() {
    const actives = [...document.querySelectorAll('.code-line.active')]
      .map(ln => parseInt(ln.dataset.lineNumber || 0));
    if (!actives.length) return;

    const lines = document.querySelectorAll('.code-line');
    lines.forEach(ln => {
      const num = parseInt(ln.dataset.lineNumber || 0);
      if (!num) return;
      // Inverse-square force from nearest cursor
      let maxF = 0;
      for (const a of actives) {
        const d = Math.abs(num - a);
        const f = 1 / (1 + d * d * 0.3);   // 1.0 at d=0, 0.77 at d=1, 0.43 at d=2…
        if (f > maxF) maxF = f;
      }
      ln.style.setProperty('--attract', maxF.toFixed(3));
    });
  },
};
