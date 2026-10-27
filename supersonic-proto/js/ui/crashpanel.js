// Crashpanel — collapsible right sidebar: clock state, scale, players.

import { Scale, Root } from '../engine/scale.js';

let _clock = null;
let _timer  = null;
let _tapTimes = [];
let _tapTimer = null;

export function initCrashPanel(clock) {
    _clock = clock;
    _restoreSize();
    _initResize();
    _initToggle();
    _initTap();
    _initTheme();
    _initScaleRoot();
    _timer = setInterval(_update, 250);
    _update();
}

// ── Update loop ──────────────────────────────────────────────────────────────

function _update() {
    if (!_clock) return;
    _updateBpm();
    _updateBeat();
    _updatePlayers();
}

function _updateBpm() {
    const el = document.getElementById('cp-bpm-val');
    if (el) el.textContent = _clock.bpm;
}

function _updateBeat() {
    const el = document.getElementById('cp-beat');
    if (!el) return;
    const now = _clock.now();
    if (now <= 0) { el.textContent = '—'; return; }
    const bar  = Math.floor(now / 4) + 1;
    const beat = Math.floor(now % 4) + 1;
    const sub  = Math.floor((now % 1) * 4);
    el.textContent = `${bar} . ${beat}`;
    const sub2 = document.getElementById('cp-beat-sub');
    if (sub2) sub2.textContent = '▪'.repeat(sub) + '◦'.repeat(4 - sub);
}

function _updatePlayers() {
    const container = document.getElementById('cp-players');
    if (!container || !_clock._players) return;

    const entries = [..._clock._players.entries()];
    // Remove rows for gone players
    for (const row of [...container.querySelectorAll('.cp-player-row')]) {
        if (!_clock._players.has(row.dataset.name)) row.remove();
    }

    for (const [name, p] of entries) {
        let row = container.querySelector(`[data-name="${name}"]`);
        if (!row) {
            row = document.createElement('div');
            row.className = 'cp-player-row';
            row.dataset.name = name;
            row.innerHTML = `
                <span class="cp-player-name">${name}</span>
                <span class="cp-player-synth"></span>
                <button class="cp-player-stop" title="stop">■</button>`;
            row.querySelector('.cp-player-stop').onclick = () => p.stop();
            container.appendChild(row);
        }
        row.classList.toggle('active', !!p._active);
        const synthEl = row.querySelector('.cp-player-synth');
        if (synthEl) synthEl.textContent = p._synth ?? '';
    }
}

// ── Tap tempo ────────────────────────────────────────────────────────────────

function _initTap() {
    const btn = document.getElementById('cp-tap');
    if (!btn) return;
    btn.onclick = () => {
        const now = performance.now();
        _tapTimes.push(now);
        // Keep only last 8 taps
        if (_tapTimes.length > 8) _tapTimes.shift();

        clearTimeout(_tapTimer);
        _tapTimer = setTimeout(() => { _tapTimes = []; btn.classList.remove('tapping'); }, 3000);

        if (_tapTimes.length >= 2) {
            const intervals = [];
            for (let i = 1; i < _tapTimes.length; i++) intervals.push(_tapTimes[i] - _tapTimes[i - 1]);
            const avg = intervals.reduce((a, b) => a + b, 0) / intervals.length;
            const bpm = Math.round(60000 / avg);
            if (bpm >= 20 && bpm <= 300) {
                if (_clock) _clock.bpm = bpm;
                const inp = document.getElementById('bpm-input');
                if (inp) inp.value = bpm;
                btn.textContent = `tap  ${bpm} BPM`;
            }
        } else {
            btn.textContent = 'tap…';
        }
        btn.classList.add('tapping');
    };
}

// ── Scale / Root selects ─────────────────────────────────────────────────────

function _initScaleRoot() {
    const scaleEl = document.getElementById('cp-scale-sel');
    const rootEl  = document.getElementById('cp-root-sel');

    if (scaleEl) {
        const scales = ['major','minor','dorian','phrygian','lydian','mixolydian',
                        'pentatonic','minPentatonic','chromatic','diminished','bhairav'];
        scales.forEach(s => {
            const o = document.createElement('option');
            o.value = o.textContent = s;
            if (s === 'minor') o.selected = true;
            scaleEl.appendChild(o);
        });
        scaleEl.onchange = () => { Scale.default = scaleEl.value; };
        // Reflect external changes back to select
        setInterval(() => {
            if (Scale.default && scaleEl.value !== Scale.default) scaleEl.value = Scale.default;
        }, 500);
    }

    if (rootEl) {
        const notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'];
        notes.forEach((n, i) => {
            const o = document.createElement('option');
            o.value = i; o.textContent = n;
            rootEl.appendChild(o);
        });
        rootEl.onchange = () => { Root.default = Number(rootEl.value); };
        setInterval(() => {
            if (rootEl.value !== String(Root.default ?? 0)) rootEl.value = Root.default ?? 0;
        }, 500);
    }
}

// ── Panel toggle ─────────────────────────────────────────────────────────────

function _initToggle() {
    const btn   = document.getElementById('panel-toggle-btn');
    const panel = document.getElementById('crash-panel');
    if (!btn || !panel) return;

    const stored = localStorage.getItem('cpHidden');
    if (stored === 'true') panel.classList.add('hidden');

    btn.onclick = () => {
        panel.classList.toggle('hidden');
        localStorage.setItem('cpHidden', panel.classList.contains('hidden'));
    };
}

// ── Theme selector ───────────────────────────────────────────────────────────

function _initTheme() {
    const sel = document.getElementById('theme-select');
    if (!sel) return;
    const stored = localStorage.getItem('theme') ?? 'dark';
    document.documentElement.className = stored === 'dark' ? '' : stored;
    sel.value = stored;
    sel.onchange = () => {
        const t = sel.value;
        document.documentElement.className = t === 'dark' ? '' : t;
        localStorage.setItem('theme', t);
    };
}

// ── Resizable log panel ───────────────────────────────────────────────────────

function _initResize() {
    const handle    = document.getElementById('log-handle');
    const logPanel  = document.getElementById('log');
    const container = document.getElementById('editor-container');
    if (!handle || !logPanel || !container) return;

    let dragging = false, startY = 0, startH = 0;

    handle.addEventListener('mousedown', (e) => {
        dragging = true;
        startY = e.clientY;
        startH = logPanel.offsetHeight;
        document.body.style.cursor = 'row-resize';
        e.preventDefault();
    });

    document.addEventListener('mousemove', (e) => {
        if (!dragging) return;
        const delta = startY - e.clientY;
        const newH  = Math.max(30, Math.min(startH + delta, container.offsetHeight - 100));
        logPanel.style.height = newH + 'px';
        localStorage.setItem('logHeight', newH);
    }, { passive: true });

    document.addEventListener('mouseup', () => {
        if (dragging) { dragging = false; document.body.style.cursor = ''; }
    });
}

function _restoreSize() {
    const h = localStorage.getItem('logHeight');
    if (h) {
        const logPanel = document.getElementById('log');
        if (logPanel) logPanel.style.height = h + 'px';
    }
}
