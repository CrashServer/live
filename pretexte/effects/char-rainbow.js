// Per-character hue cycling. Color-only effect (no motion). Each char gets
// its own hue derived from its ID + time; the spectrum rotates continuously.
// BPM pulse briefly saturates + brightens. Genuinely different from motion effects.

import { getCharSpans } from '../engine/charrenderer.js';

const HUE_SPEED    = 40;     // degrees per second
const HUE_PER_CHAR = 8;      // spatial hue increment per char ID

let startTime = 0;

export const charRainbow = {
  id: 'char-rainbow',
  mode: 'char',

  enable() { document.body.classList.add('fx-char-rainbow'); startTime = performance.now(); },
  disable() {
    document.body.classList.remove('fx-char-rainbow');
    for (const span of getCharSpans().values()) span.style.removeProperty('color');
  },

  tick(reactive) {
    const spans = getCharSpans();
    if (!spans.size) return;

    const dt = (performance.now() - startTime) / 1000;
    const timeHue = dt * HUE_SPEED;
    const sat = 70 + 25 * reactive.bpm.pulse;
    const light = 55 + 15 * reactive.bpm.pulse;

    for (const [id, span] of spans) {
      const h = (id * HUE_PER_CHAR + timeHue) % 360;
      span.style.color = `hsl(${h.toFixed(0)}, ${sat.toFixed(0)}%, ${light.toFixed(0)}%)`;
    }
  },
};
