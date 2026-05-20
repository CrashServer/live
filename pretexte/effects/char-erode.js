// On each strong beat, pick a random visible non-whitespace character,
// animate it: scale up, spin, fade out. When the animation finishes, the
// char is permanently removed (until the source text re-renders).
//
// In idle (no cursor/typing activity) the text slowly erodes beat by beat.
// Any WS cursor update rebuilds the text fresh from source.

import { getCharSpans, removeCharSpan } from '../engine/charrenderer.js';

const COOLDOWN_MS    = 150;    // min gap between erodes
const PULSE_THRESH   = 0.75;   // how strong a beat counts
const EROSION_MS     = 520;    // explode duration

let lastErodeAt = 0;

function explodeAndRemove(id, span) {
  span.dataset.eroding = '1';
  // Preserve base position (renderer wrote --base-x/--base-y); animate only
  // the composable vars so we inherit the translate naturally.
  const anim = span.animate(
    [
      { '--char-scale': 1,   '--char-rot': '0deg',   '--char-opacity': 1 },
      { '--char-scale': 3.5, '--char-rot': '540deg', '--char-opacity': 0 },
    ],
    {
      duration: EROSION_MS,
      easing: 'cubic-bezier(0.3, 0, 0.8, 0.3)',
      fill:   'forwards',
    }
  );
  anim.onfinish = () => { removeCharSpan(id); };
}

export const charErode = {
  id: 'char-erode',
  mode: 'char',

  enable() { document.body.classList.add('fx-char-erode'); lastErodeAt = 0; },
  disable() { document.body.classList.remove('fx-char-erode'); },

  tick(reactive) {
    if (reactive.bpm.pulse < PULSE_THRESH) return;
    const now = performance.now();
    if (now - lastErodeAt < COOLDOWN_MS) return;
    lastErodeAt = now;

    // Collect non-whitespace, not-already-eroding candidates
    const spans = getCharSpans();
    const candidates = [];
    for (const [id, span] of spans) {
      if (span.dataset.eroding) continue;
      const t = span.textContent;
      if (!t || !t.trim()) continue;
      candidates.push([id, span]);
    }
    if (!candidates.length) return;

    const [id, span] = candidates[Math.floor(Math.random() * candidates.length)];
    explodeAndRemove(id, span);
  },
};
