// Fully audio-reactive text. Each character is mapped to an FFT bin by its
// horizontal position. Its color hue = bin index, saturation/lightness =
// energy, y-offset and scale also driven by that bin's energy.
// Whole text becomes a spectrum analyzer made of code.

import { getCharSpans } from '../engine/charrenderer.js';
import { audioState, energyAtX } from '../audio.js';

const Y_AMP       = 42;      // max upward push (px) at energy=1
const SCALE_AMP   = 0.55;    // +55% scale at energy=1
const IDLE_COLOR_OPACITY = 0.45;

export const charAudio = {
  id: 'char-audio',
  mode: 'char',

  enable() { document.body.classList.add('fx-char-audio'); },

  disable() {
    document.body.classList.remove('fx-char-audio');
    for (const span of getCharSpans().values()) {
      span.style.removeProperty('color');
      span.style.removeProperty('--wobble-y');
      span.style.removeProperty('--char-scale');
    }
  },

  tick(reactive) {
    const spans = getCharSpans();
    if (!spans.size) return;
    const vw = window.innerWidth;

    // If audio isn't active yet, apply a gentle BPM-pulse spectrum-fake
    // so you can still see per-char color before mic permission.
    const fakeMode = !audioState.active;
    const fakeBase = reactive.bpm.pulse;

    for (const [id, span] of spans) {
      // Read base-x from the CSS var the renderer wrote
      const baseXStr = span.style.getPropertyValue('--base-x');
      const baseX = parseFloat(baseXStr) || 0;
      const x01 = Math.max(0, Math.min(1, baseX / vw));

      let energy;
      if (fakeMode) {
        // Gentle per-char phase-based fake; each char-id gets a spatial hue.
        energy = 0.15 + fakeBase * 0.35 * (0.5 + 0.5 * Math.sin(id * 0.31));
      } else {
        energy = energyAtX(x01);
      }

      // Hue from x position (so color is spatially coherent — bass=left=red,
      // mid=green, treble=right=blue-purple, not random per char)
      const hue  = x01 * 300;       // 0..300 deg (skip magenta circle)
      const sat  = 60 + energy * 40;
      const light = 40 + energy * 40;

      span.style.color = `hsl(${hue.toFixed(0)}, ${sat.toFixed(0)}%, ${light.toFixed(0)}%)`;
      span.style.setProperty('--wobble-y',   `${(energy * -Y_AMP).toFixed(1)}px`);
      span.style.setProperty('--char-scale', (1 + energy * SCALE_AMP).toFixed(3));
    }
  },
};
