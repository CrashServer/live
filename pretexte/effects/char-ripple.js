// Audio-spectrum-like char ripple: each character gets a y-offset
// driven by sin(id * k + t * bpm). Like a VU-meter array made of code.
// When bass hits (pulse), the wave amplitude jumps. Different from
// char-wobble: here the wave phase advances *per char ID* so you see
// a travelling wave through the whole visible text.

import { getCharSpans } from '../engine/charrenderer.js';

const BASE_AMP = 6;
const BEAT_AMP = 28;
const SPATIAL_FREQ = 0.18;   // radians per char id
let startTime = 0;

export const charRipple = {
  id: 'char-ripple',
  mode: 'char',

  enable() { document.body.classList.add('fx-char-ripple'); startTime = performance.now(); },
  disable() { document.body.classList.remove('fx-char-ripple'); },

  tick(reactive) {
    const spans = getCharSpans();
    if (!spans.size) return;

    const dt = (performance.now() - startTime) / 1000;
    const beatPeriod = 60 / Math.max(40, reactive.bpm.value);
    const tPhase = (dt / beatPeriod) * Math.PI * 2;    // 1 cycle per beat
    const amp = BASE_AMP + BEAT_AMP * reactive.bpm.pulse;

    for (const [id, span] of spans) {
      const phase = id * SPATIAL_FREQ + tPhase;
      const dy = Math.sin(phase) * amp;
      const scale = 1 + 0.05 * Math.max(0, Math.sin(phase));
      span.style.setProperty('--wobble-y', `${dy.toFixed(1)}px`);
      span.style.setProperty('--char-scale', scale.toFixed(3));
    }
  },
};
