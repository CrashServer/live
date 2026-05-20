// URL hash loader + Space hotkey scene cycler.

import { loadScene, cycleScene, getScenes } from './registry.js';

const DEFAULT_SCENE = 'minimal';

export function initControl() {
  // Load scene from URL hash (or default)
  applyHash();

  window.addEventListener('hashchange', applyHash);

  // Space cycles. Prevent scroll-down default on the container.
  window.addEventListener('keydown', (e) => {
    if (e.code === 'Space') {
      e.preventDefault();
      const s = cycleScene();
      if (s) {
        history.replaceState(null, '', '#' + s.name);
      }
    }
  });
}

function applyHash() {
  const raw = (location.hash || '').replace(/^#/, '').trim().toLowerCase();
  const scenes = getScenes();
  const target = scenes.find(s => s.name === raw);
  if (target) {
    loadScene(target.name);
  } else {
    // Unknown or empty → default
    loadScene(DEFAULT_SCENE);
    if (raw) console.warn(`Unknown scene "${raw}", falling back to ${DEFAULT_SCENE}`);
  }
}
