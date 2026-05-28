// Sampler — buffer loading and character→bufferID map for play() patterns.

let _manifest = {};
let _loaded   = false;

export function samplesLoaded() { return _loaded; }

// Load manifest + all WAVs into SC buffers. Call once at boot.
export async function loadSamples(sc, onProgress) {
    const resp = await fetch('./samples/manifest.json');
    _manifest  = await resp.json();

    const allEntries = [];
    for (const [, info] of Object.entries(_manifest)) {
        for (let i = 0; i < info.count; i++) {
            allEntries.push({ url: info.urls[i], bufId: info.bufStart + i });
        }
    }

    let done = 0;
    const BATCH = 8;
    for (let i = 0; i < allEntries.length; i += BATCH) {
        await Promise.all(allEntries.slice(i, i + BATCH).map(async ({ url, bufId }) => {
            try {
                const r   = await fetch(url);
                const buf = await r.arrayBuffer();
                await sc.loadSample(bufId, buf);
            } catch (_) {}
            if (onProgress) onProgress(++done, allEntries.length);
        }));
    }
    _loaded = true;
}

// char + sampleIndex → SC buffer ID
export function charToBufId(char, sampleIdx = 0) {
    const info = _manifest[char];
    if (!info || info.count === 0) return null;
    return info.bufStart + (((sampleIdx % info.count) + info.count) % info.count);
}

// ── Pattern parsing ────────────────────────────────────────────────────────────
// Returns array of steps. Each step is one of:
//   null              — rest
//   { chars: [c,...], dur_mult: 1 }  — fire these chars simultaneously, full step
//   { sub: [c,...] }                 — subdivision: N chars each at dur/N
//
// "X  o"     → [{chars:['X']}, null, null, {chars:['o']}]
// "(Xo)"     → [{chars:['X','o']}]      — fire both at once
// "[XoXo]"   → [{sub:['X','o','X','o']}] — 4 equal subdivisions

export function parsePattern(str) {
    const steps = [];
    let i = 0;
    while (i < str.length) {
        const c = str[i];
        if (c === ' ') {
            steps.push(null);
            i++;
        } else if (c === '(') {
            const end = str.indexOf(')', i + 1);
            const slice = end === -1 ? str.slice(i + 1) : str.slice(i + 1, end);
            const chars = [...slice].filter(ch => ch !== ' ');
            steps.push(chars.length ? { chars } : null);
            i = end === -1 ? str.length : end + 1;
        } else if (c === '[') {
            const end = str.indexOf(']', i + 1);
            const slice = end === -1 ? str.slice(i + 1) : str.slice(i + 1, end);
            const chars = [...slice].filter(ch => ch !== ' ');
            steps.push(chars.length ? { sub: chars } : null);
            i = end === -1 ? str.length : end + 1;
        } else {
            steps.push({ chars: [c] });
            i++;
        }
    }
    return steps;
}

// ── PlayStringCall — returned by play(), detected in Player.__rshift__ ────────

export class PlayStringCall {
    constructor(pattern, opts) {
        this.pattern = pattern;
        this.opts    = opts;
    }
}
