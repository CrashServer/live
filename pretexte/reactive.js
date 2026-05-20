// Shared reactive state — WS signals + rAF-driven smoothing.
// Modules read from `reactive`, never mutate directly (except subscribe()).

export const reactive = {
  bpm:   { value: 120, lastBeatAt: 0, pulse: 0, phase01: 0 },
  cpu:   { value: 0, smoothed: 0 },
  audio: null, // placeholder: { bass, mid, treble, volume, spectrum[] } when mic lands
};

const PULSE_DECAY_PER_SEC = 3.0;  // clift2-style exponential decay
const CPU_SMOOTHING_TC    = 0.4;  // seconds

let lastFrameTime = performance.now();

export function handleWsMessage(msg) {
  switch (msg.type) {
    case 'bpm':
      if (typeof msg.bpm === 'number') reactive.bpm.value = msg.bpm;
      reactive.bpm.lastBeatAt = performance.now();
      reactive.bpm.pulse = 1.0;
      break;
    case 'cpu':
      if (typeof msg.cpu === 'number') reactive.cpu.value = msg.cpu;
      break;
  }
}

export function tickReactive() {
  const now = performance.now();
  const dt = Math.min(0.1, (now - lastFrameTime) / 1000);
  lastFrameTime = now;

  // Decaying pulse
  reactive.bpm.pulse = Math.max(0, reactive.bpm.pulse - PULSE_DECAY_PER_SEC * dt);

  // BPM phase 0..1 between beats (for continuous breathing animations)
  const beatPeriod = 60 / Math.max(40, reactive.bpm.value);
  const sinceBeat  = (now - reactive.bpm.lastBeatAt) / 1000;
  reactive.bpm.phase01 = Math.min(1, sinceBeat / beatPeriod);

  // Smooth CPU (0..1 normalized)
  const cpuTarget = Math.max(0, Math.min(1, reactive.cpu.value / 100));
  const alpha = 1 - Math.exp(-dt / CPU_SMOOTHING_TC);
  reactive.cpu.smoothed += (cpuTarget - reactive.cpu.smoothed) * alpha;

  return dt;
}
