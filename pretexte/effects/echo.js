// Tape-echo feedback: snapshot the code container each BPM beat,
// render past snapshots as ghost layers behind the current code
// with decaying opacity and y-offset — visible trail of past edits.

const MAX_ECHOES = 5;

const snapshots = [];  // [{ html, t }]
let   observedBeat = 0;

export const echo = {
  id: 'echo',

  enable() {
    document.body.classList.add('fx-echo');
    ensureGhostContainer();
    snapshots.length = 0;
  },

  disable() {
    document.body.classList.remove('fx-echo');
    const ghost = document.getElementById('echo-container');
    if (ghost) ghost.innerHTML = '';
    snapshots.length = 0;
    observedBeat = 0;
  },

  tick(reactive) {
    // Trigger a snapshot each beat (when lastBeatAt advances)
    if (reactive.bpm.lastBeatAt !== observedBeat && reactive.bpm.lastBeatAt > 0) {
      observedBeat = reactive.bpm.lastBeatAt;
      captureSnapshot();
      renderEchoes();
    }
  },
};

function ensureGhostContainer() {
  if (document.getElementById('echo-container')) return;
  const ghost = document.createElement('div');
  ghost.id = 'echo-container';
  // Insert BEFORE code-container so echoes render behind
  const code = document.getElementById('code-container');
  code.parentNode.insertBefore(ghost, code);
}

function captureSnapshot() {
  const container = document.getElementById('code-container');
  if (!container) return;
  snapshots.push({
    html: container.innerHTML,
    t:   performance.now(),
  });
  while (snapshots.length > MAX_ECHOES) snapshots.shift();
}

function renderEchoes() {
  const ghost = document.getElementById('echo-container');
  if (!ghost) return;
  ghost.innerHTML = '';
  // Oldest → newest so newest paints on top
  snapshots.forEach((snap, i) => {
    const layer = document.createElement('div');
    layer.className = 'echo-layer';
    layer.innerHTML = snap.html;
    const age = snapshots.length - i;           // 1..N (1 = newest)
    const opacity = 0.35 * Math.pow(1 - (age - 1) / MAX_ECHOES, 2);
    const offsetY = (age - 1) * 6;               // px down per step
    layer.style.opacity = opacity.toFixed(3);
    layer.style.transform = `translateY(${offsetY}px)`;
    ghost.appendChild(layer);
  });
}
