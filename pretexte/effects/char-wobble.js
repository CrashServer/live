// Per-character wobble. Each char gets a phase derived from its ID,
// y-offset = sin(phase + time). Amplitude breathes with BPM pulse.
// Proves: every character is independently animatable via its stable ID.

import { getCharSpans } from '../engine/charrenderer.js';

const AMP_PX       = 10;          // baseline amplitude
const AMP_ON_BEAT  = 22;          // amplitude added during BPM pulse
const WAVELENGTH   = 12;          // chars per full wave

let startTime = 0;

export const charWobble = {
  id: 'char-wobble',
  mode: 'char',

  enable() {
    document.body.classList.add('fx-char-wobble');
    startTime = performance.now();
  },
  disable() {
    document.body.classList.remove('fx-char-wobble');
    // Don't clear transforms — the base renderer owns them (translate to x,y).
    // Instead we'll go back to plain translate when disabled; renderer runs
    // per-frame-ish and rewrites transform anyway.
  },

  tick(reactive) {
    const spans = getCharSpans();
    if (!spans.size) return;

    const sinceStart = (performance.now() - startTime) / 1000;
    // phase advances at 2 wavelengths per beat-pair
    const beatPeriod = 60 / Math.max(40, reactive.bpm.value);
    const phase = (sinceStart / (beatPeriod * 2)) * Math.PI * 2;

    const amp = AMP_PX + AMP_ON_BEAT * reactive.bpm.pulse;

    for (const [id, span] of spans) {
      const k = (id / WAVELENGTH) * Math.PI * 2;
      const dy = Math.sin(k + phase) * amp;
      // Re-apply transform with added y offset. The base x/y from the
      // layout is encoded in the inline transform — we parse and add.
      // To keep this cheap, use a CSS variable for the wobble and let
      // CSS compose with the base transform.
      span.style.setProperty('--wobble-y', `${dy.toFixed(1)}px`);
    }
  },
};
