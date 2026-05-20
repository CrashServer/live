// Hardcoded scene list. Cycle order = declaration order.
// Each scene has a `mode`: 'line' (DOM span per line, natural flow) or
// 'char' (char-layout engine: pretext-driven, span per character).
// focus-cone + eval-flash are baked into the line-mode renderer.

const EVAL = 'eval-flash';

export const SCENES = [
  // ── Flow demo: the actual pretext killer feature ─────────────────
  // Moving SVG circle + text reflows around it via layoutNextLine.
  { name: 'flow',      mode: 'flow', modules: [] },

  // ── Line mode scenes (current renderer) ──────────────────────────
  { name: 'minimal',   mode: 'line', modules: [EVAL] },
  { name: 'pulse',     mode: 'line', modules: [EVAL, 'bpm-pulse'] },
  { name: 'heat',      mode: 'line', modules: [EVAL, 'bpm-pulse', 'cpu-heat'] },
  { name: 'orb',       mode: 'line', modules: [EVAL, 'bpm-pulse', 'orb'] },
  { name: 'echo',      mode: 'line', modules: [EVAL, 'bpm-pulse', 'echo'] },
  { name: 'warp',      mode: 'line', modules: [EVAL, 'bpm-pulse', 'warp'] },
  { name: 'explode',   mode: 'line', modules: [EVAL, 'bpm-pulse', 'explode'] },
  { name: 'attract',   mode: 'line', modules: [EVAL, 'bpm-pulse', 'attractor'] },
  { name: 'repel',     mode: 'line', modules: [EVAL, 'bpm-pulse', 'repulsor'] },
  { name: 'ikeda',     mode: 'line', modules: [EVAL, 'bpm-pulse'] },
  { name: 'neon',      mode: 'line', modules: [EVAL, 'bpm-pulse', 'warp', 'attractor'] },
  { name: 'full',      mode: 'line', modules: [EVAL, 'bpm-pulse', 'cpu-heat', 'orb', 'echo', 'explode'] },

  // ── Char mode scenes (pretext char-layout engine) ────────────────
  // Each is a different EFFECT TYPE.
  { name: 'audio',     mode: 'char', modules: ['char-audio'] },                 // fully FFT-reactive
  { name: 'erode',     mode: 'char', modules: ['bpm-pulse', 'char-erode'] },    // erasure on beat
  { name: 'wobble',    mode: 'char', modules: ['bpm-pulse', 'char-wobble'] },   // motion
  { name: 'shatter',   mode: 'char', modules: ['bpm-pulse', 'char-shatter'] },  // physics
  { name: 'glitch',    mode: 'char', modules: ['bpm-pulse', 'char-glitch'] },   // substitution
  { name: 'rainbow',   mode: 'char', modules: ['bpm-pulse', 'char-rainbow'] },  // color
];
