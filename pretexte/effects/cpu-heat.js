// CPU → warm background tint (cool blue at 0, amber/red at 1).

export const cpuHeat = {
  id: 'cpu-heat',
  enable() {
    document.body.classList.add('fx-cpu-heat');
  },
  disable() {
    document.body.classList.remove('fx-cpu-heat');
    document.documentElement.style.removeProperty('--cpu-heat');
  },
  tick(reactive) {
    document.documentElement.style.setProperty(
      '--cpu-heat',
      reactive.cpu.smoothed.toFixed(3)
    );
  },
};
