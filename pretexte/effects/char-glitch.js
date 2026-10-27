// Per-character glitch: random chars briefly replaced with garbage glyph,
// then restored. Driven by CPU load (more chaos under pressure) + beat triggers.
// Very different from motion-based effects — this is SUBSTITUTION.

import { getCharSpans } from '../engine/charrenderer.js';

const GLITCH_POOL = '█▓▒░@#$%&*!?=+~<>[]{}|/\\▌▐■□▲▼◆◇';
const BASE_RATE   = 0.0015;  // prob per char per frame at idle
const BEAT_RATE   = 0.08;    // prob per char on strong beat
const GLITCH_MS   = 90;      // how long garbage char shows before restore

const pending = new Map();   // span → restoreAt timestamp

function randomGlitchChar() {
  return GLITCH_POOL.charAt(Math.floor(Math.random() * GLITCH_POOL.length));
}

export const charGlitch = {
  id: 'char-glitch',
  mode: 'char',

  enable() { document.body.classList.add('fx-char-glitch'); pending.clear(); },
  disable() {
    document.body.classList.remove('fx-char-glitch');
    // Restore any pending glitched chars
    for (const [span] of pending) {
      if (span.dataset.originalChar) {
        span.textContent = span.dataset.originalChar;
        delete span.dataset.originalChar;
      }
    }
    pending.clear();
  },

  tick(reactive) {
    const now = performance.now();
    const spans = getCharSpans();

    // Beat-triggered burst or baseline noise, modulated by CPU load
    const rate = BASE_RATE + (reactive.cpu.smoothed * 0.02) + reactive.bpm.pulse * BEAT_RATE;

    for (const span of spans.values()) {
      // Restore anything whose time is up
      const restoreAt = pending.get(span);
      if (restoreAt !== undefined && now >= restoreAt) {
        span.textContent = span.dataset.originalChar || span.textContent;
        delete span.dataset.originalChar;
        pending.delete(span);
      }
      // Maybe glitch a new one (don't re-glitch already glitched)
      if (!pending.has(span) && Math.random() < rate) {
        span.dataset.originalChar = span.textContent;
        span.textContent = randomGlitchChar();
        pending.set(span, now + GLITCH_MS);
      }
    }
  },
};
