// Per-line horizontal sine drift. Wave travels vertically through the code
// window at BPM rate, each line's x-offset = sin(y_index + t * speed).
// Mild amplitude by default — readable, adds life. Cranks with bass later.

const AMPLITUDE_PX  = 18;
const WAVELENGTH    = 4;    // code lines per full wave period
let   startTime = 0;

export const warp = {
  id: 'warp',

  enable() {
    document.body.classList.add('fx-warp');
    startTime = performance.now();
  },
  disable() {
    document.body.classList.remove('fx-warp');
    for (const ln of document.querySelectorAll('.code-line')) {
      ln.style.transform = '';
    }
  },
  tick(reactive) {
    const lines = document.querySelectorAll('.code-line');
    if (!lines.length) return;

    // Time phase advances per beat (so wave travels 1 wavelength per N beats)
    const sinceStart = (performance.now() - startTime) / 1000;
    const beatPeriod = 60 / Math.max(40, reactive.bpm.value);
    const phase = (sinceStart / (beatPeriod * 2)) * Math.PI * 2;  // 2 beats per cycle

    // Amplitude subtly breathes with BPM pulse (more motion right after beat)
    const amp = AMPLITUDE_PX * (0.7 + 0.6 * reactive.bpm.pulse);

    lines.forEach((ln, i) => {
      const k = (i / WAVELENGTH) * Math.PI * 2;
      const dx = Math.sin(k + phase) * amp;
      ln.style.transform = `translateX(${dx.toFixed(2)}px)`;
    });
  },
};
