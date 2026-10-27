// Obstacle orb: a circular SVG shape breathes with BPM in the centre,
// code lines passing through the orb's y-range get their max-width shrunk
// so text flows around (actually: beside) the orb. A real text-around-obstacle
// demo that CSS alone cannot do.

let svg, circle, ring;

export const orb = {
  id: 'orb',

  enable() {
    document.body.classList.add('fx-orb');
    if (!svg) {
      svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
      svg.id = 'orb-svg';
      ring = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
      circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
      ring.setAttribute('class', 'orb-ring');
      circle.setAttribute('class', 'orb-fill');
      svg.appendChild(ring);
      svg.appendChild(circle);
      document.body.appendChild(svg);
    }
    svg.style.display = 'block';
  },

  disable() {
    document.body.classList.remove('fx-orb');
    if (svg) svg.style.display = 'none';
    for (const ln of document.querySelectorAll('.code-line')) {
      ln.style.maxWidth = '';
      ln.style.marginLeft = '';
    }
  },

  tick(reactive) {
    if (!svg) return;
    const vw = window.innerWidth;
    const vh = window.innerHeight;
    const cx = vw / 2;
    const cy = vh / 2;

    // Radius: breathing at BPM rate + transient swell on beat
    const baseR = Math.min(vw, vh) * 0.18;
    const phaseBreathe = 1 + 0.06 * Math.sin(reactive.bpm.phase01 * Math.PI * 2);
    const pulseSwell = 1 + 0.25 * reactive.bpm.pulse;
    const r = baseR * phaseBreathe * pulseSwell;

    circle.setAttribute('cx', cx);
    circle.setAttribute('cy', cy);
    circle.setAttribute('r', r);
    ring.setAttribute('cx', cx);
    ring.setAttribute('cy', cy);
    ring.setAttribute('r', r * 1.12);

    // Push code lines around the orb
    const container = document.getElementById('code-container');
    if (!container) return;
    const containerRect = container.getBoundingClientRect();

    const lines = document.querySelectorAll('.code-line');
    lines.forEach(ln => {
      const rect = ln.getBoundingClientRect();
      const lineCentreY = rect.top + rect.height / 2;
      const dy = Math.abs(lineCentreY - cy);

      if (dy < r) {
        // Chord-width of the circle at this y — how much horizontal space is blocked
        const chord = Math.sqrt(r * r - dy * dy);
        // Force line into the LEFT half only, width = (cx - padding) - orbLeftEdge shift
        const freeRight = cx - chord - 24;  // right edge of free zone (from viewport)
        const freeWidth = Math.max(50, freeRight - containerRect.left);
        ln.style.maxWidth = `${freeWidth}px`;
        ln.style.marginLeft = '0';
      } else {
        ln.style.maxWidth = '';
        ln.style.marginLeft = '';
      }
    });
  },
};
