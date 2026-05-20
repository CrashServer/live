// On hard beat (pulse near 1), momentarily push non-active lines outward
// from the viewport centre — code breathes outward on the downbeat.
// Uses Web Animations API so many elements animate in parallel cheaply.

let lastExplodeAt = 0;
const COOLDOWN_MS = 150;

export const explode = {
  id: 'explode',

  enable() {
    document.body.classList.add('fx-explode');
    lastExplodeAt = 0;
  },

  disable() {
    document.body.classList.remove('fx-explode');
  },

  tick(reactive) {
    // Only fire on strong beat, with cooldown to prevent re-trigger
    if (reactive.bpm.pulse < 0.85) return;
    const now = performance.now();
    if (now - lastExplodeAt < COOLDOWN_MS) return;
    lastExplodeAt = now;

    const lines = document.querySelectorAll('.code-line:not(.active)');
    if (!lines.length) return;

    const mid = lines.length / 2;
    lines.forEach((ln, i) => {
      const rel = (i - mid) / Math.max(1, mid);   // -1 .. +1 vertical position
      const dy = rel * 18;                          // px, radial outward
      const scale = 1 + 0.04 * Math.abs(rel);
      ln.animate(
        [
          { transform: `translateY(${dy}px) scale(${scale})`, opacity: 0.5, offset: 0 },
          { transform: 'translateY(0) scale(1)', opacity: 1, offset: 1 },
        ],
        { duration: 260, easing: 'cubic-bezier(0.2, 0.9, 0.2, 1)' },
      );
    });
  },
};
