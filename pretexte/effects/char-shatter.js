// Per-character shatter on strong beat. Each char flies out with random
// direction + rotation, returns to origin. Staggered by char ID so the
// blast ripples outward rather than triggering all chars at once — feels
// kinetic instead of slow even at equivalent duration.

import { getCharSpans } from '../engine/charrenderer.js';

const COOLDOWN_MS     = 180;
const DURATION_MS     = 280;       // fast
const MAX_STAGGER_MS  = 120;       // last char starts 120ms after first
const BURST_RADIUS    = 140;
const ROT_MAX         = 720;       // deg

let lastShatterAt = 0;

function shatterOne(span, delay) {
  const angle     = Math.random() * Math.PI * 2;
  const dist      = BURST_RADIUS * (0.5 + 0.5 * Math.random());
  const dx        = Math.cos(angle) * dist;
  const dy        = Math.sin(angle) * dist;
  const rot       = (Math.random() - 0.5) * ROT_MAX;
  const scaleDown = 0.4 + Math.random() * 0.4;

  span.animate(
    [
      { '--shatter-x': '0px',        '--shatter-y': '0px',        '--char-rot': '0deg',      '--char-scale': '1',           '--char-opacity': '1'   },
      { '--shatter-x': `${dx}px`,    '--shatter-y': `${dy}px`,    '--char-rot': `${rot}deg`, '--char-scale': `${scaleDown}`,'--char-opacity': '0.2', offset: 0.45 },
      { '--shatter-x': '0px',        '--shatter-y': '0px',        '--char-rot': '0deg',      '--char-scale': '1',           '--char-opacity': '1'   },
    ],
    {
      duration: DURATION_MS,
      delay,
      easing:   'cubic-bezier(0.15, 0.8, 0.25, 1)',
      fill:     'none',
    }
  );
}

export const charShatter = {
  id: 'char-shatter',
  mode: 'char',

  enable() { document.body.classList.add('fx-char-shatter'); lastShatterAt = 0; },
  disable() { document.body.classList.remove('fx-char-shatter'); },

  tick(reactive) {
    if (reactive.bpm.pulse < 0.85) return;
    const now = performance.now();
    if (now - lastShatterAt < COOLDOWN_MS) return;
    lastShatterAt = now;

    const spans = [...getCharSpans().values()];
    if (!spans.length) return;

    // Stagger outward from a random epicenter char for ripple-of-destruction feel
    const epicenter = Math.floor(Math.random() * spans.length);
    const maxDist = Math.max(epicenter, spans.length - epicenter - 1);
    spans.forEach((span, i) => {
      const d = Math.abs(i - epicenter);
      const delay = (d / Math.max(1, maxDist)) * MAX_STAGGER_MS;
      shatterOne(span, delay);
    });
  },
};
