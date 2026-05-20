// Active-line halo glow pulsing on beat. Pure CSS-var driven.

export const bpmPulse = {
  id: 'bpm-pulse',
  enable() {
    document.body.classList.add('fx-bpm-pulse');
  },
  disable() {
    document.body.classList.remove('fx-bpm-pulse');
    document.documentElement.style.removeProperty('--bpm-pulse');
    document.documentElement.style.removeProperty('--bpm-phase');
  },
  tick(reactive) {
    const root = document.documentElement;
    root.style.setProperty('--bpm-pulse', reactive.bpm.pulse.toFixed(3));
    root.style.setProperty('--bpm-phase', reactive.bpm.phase01.toFixed(3));
  },
};
