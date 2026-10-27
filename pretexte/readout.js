// Permanent bottom-right readout — Ikeda-style data chrome.
// Shows active scene + BPM + CPU %. Highlights briefly on scene change.

import { getCurrentScene, enabledList } from './registry.js';
import { audioState } from './audio.js';

let el;
let lastSceneName = '';
let sceneHighlightUntil = 0;

export function initReadout() {
  el = document.getElementById('readout');
  if (!el) {
    el = document.createElement('div');
    el.id = 'readout';
    document.body.appendChild(el);
  }
}

export function tickReadout(reactive) {
  if (!el) return;
  const scene = getCurrentScene();
  const sceneName = scene ? scene.name : '—';
  const cpuPct = Math.round(reactive.cpu.smoothed * 100);
  const bpm = reactive.bpm.value;
  const mods = enabledList().map(id => id.replace(/^fx-/, '')).join(' · ');

  if (sceneName !== lastSceneName) {
    sceneHighlightUntil = performance.now() + 1000;
    lastSceneName = sceneName;
  }
  const highlight = performance.now() < sceneHighlightUntil;

  const audioBadge = audioState.active
    ? `<span class="r-aud r-aud-on">AUD ${Math.round(audioState.volume * 100)}</span>`
    : `<span class="r-aud r-aud-off">AUD OFF</span>`;

  el.innerHTML =
    `<span class="r-label">SCENE</span> ` +
    `<span class="r-scene${highlight ? ' r-hl' : ''}">${sceneName}</span>` +
    (mods ? `<span class="r-mods"> ${mods}</span>` : '') +
    `<span class="r-sep"></span>` +
    `<span class="r-bpm">${bpm} BPM</span>` +
    `<span class="r-cpu">${cpuPct}%</span>` +
    ` ${audioBadge}`;
}
