// Pattern helpers — all patterns expose a .get(step) method.
// patGet resolves any value: plain scalar, array, or pattern object.

export function patGet(val, step, def) {
    if (val === null || val === undefined) return def;
    if (typeof val?.get === 'function') return val.get(step);
    if (Array.isArray(val)) return val[((step % val.length) + val.length) % val.length];
    return val;
}

// ── Basic sequences ──────────────────────────────────────────────────────────

// PRand(lo, hi) — random integer in [lo, hi). PRand([arr]) picks from array.
export function PRand(lo, hi) {
    if (Array.isArray(lo)) { const a = lo; return { get: () => a[Math.floor(Math.random() * a.length)] }; }
    if (hi === undefined) { hi = lo; lo = 0; }
    return { get: () => Math.floor(Math.random() * (hi - lo)) + lo };
}

// PWhite(lo=0, hi=1) — random float in [lo, hi]
export function PWhite(lo = 0, hi = 1) {
    return { get: () => lo + Math.random() * (hi - lo) };
}

// PWalk(max=7, step=1, start=0) — random walk bounded to ±max
export function PWalk(max = 7, step = 1, start = 0) {
    let cur = start;
    return {
        get: () => {
            const v = cur;
            cur = Math.max(-max, Math.min(max, cur + (Math.random() < 0.5 ? step : -step)));
            return v;
        }
    };
}

// PDur(k, n, dur=1) — Euclidean durations: k pulses in n steps
export function PDur(k, n, dur = 1) {
    const steps = Array(n).fill(0);
    for (let i = 0; i < k; i++) steps[Math.round(i * n / k)] = 1;
    const durs = [];
    let acc = 0;
    for (let i = 0; i < n; i++) {
        if (steps[i] === 1 && i > 0) { durs.push(acc * dur / n); acc = 1; }
        else acc++;
    }
    if (acc > 0) durs.push(acc * dur / n);
    return durs;
}

// PPing(arr) — ping-pong through array [0,1,2,3,2,1,0,1,...]
export function PPing(arr) {
    const fwd = [...arr], rev = [...arr].reverse().slice(1, -1);
    const loop = [...fwd, ...rev];
    return { get: (i) => loop[i % loop.length] };
}

// ── Repetition / rotation ─────────────────────────────────────────────────────

// PStutter(seq, n) — each value repeated n times: [0,2,4] n=2 → [0,0,2,2,4,4]
export function PStutter(seq, n = 2) {
    const arr  = Array.isArray(seq) ? seq : [seq];
    const nArr = Array.isArray(n)   ? n   : null;
    const flat = arr.flatMap((v, i) => Array(nArr ? nArr[i % nArr.length] : n).fill(v));
    return { get: (step) => flat[step % flat.length] };
}

// PAlt(p1, p2, ...) — alternate between patterns one step at a time
export function PAlt(...pats) {
    return { get: (step) => patGet(pats[step % pats.length], step) };
}

// PShuf(seq) — shuffle once at creation, cycle forever
export function PShuf(seq) {
    const arr = [...(Array.isArray(seq) ? seq : [seq])];
    for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return { get: (step) => arr[step % arr.length] };
}

// ── Probability ──────────────────────────────────────────────────────────────

// PBern(p=0.5, a=1, b=0) — Bernoulli: returns a with prob p, else b
export function PBern(p = 0.5, a = 1, b = 0) {
    return { get: () => Math.random() < p ? a : b };
}

// PCoin — alias for PBern
export const PCoin = PBern;

// ── Euclidean ────────────────────────────────────────────────────────────────

// PEuclid(n, k, offset=0) — k pulses in n steps; returns 1/0 per step
export function PEuclid(n, k, offset = 0) {
    const seq = _euclid(n, k);
    return { get: (step) => seq[(step + offset) % seq.length] };
}

function _euclid(n, k) {
    const seq = Array(n).fill(0);
    let b = 0;
    for (let i = 0; i < n; i++) { b += k; if (b >= n) { b -= n; seq[i] = 1; } }
    return seq;
}

// ── Range / step ─────────────────────────────────────────────────────────────

// PRange(lo, hi, step=1) — cycle through arithmetic range
export function PRange(lo, hi, step = 1) {
    const arr = [];
    for (let v = lo; v < hi; v += step) arr.push(v);
    return { get: (s) => arr[s % arr.length] };
}

// PStep(mapping, cycle) — sparse {stepIndex: value} lookup, default 0
export function PStep(mapping, cycle = null) {
    const entries = Object.entries(mapping).map(([k, v]) => [Number(k), v]);
    const max = cycle ?? (Math.max(...entries.map(([k]) => k)) + 1);
    return { get: (step) => { const s = ((step % max) + max) % max; return mapping[s] ?? 0; } };
}

// ── Shape ────────────────────────────────────────────────────────────────────

// PSine(lo, hi, steps) — sinusoidal sweep
export function PSine(lo = 0, hi = 1, steps = 16) {
    return {
        get: (step) => {
            const t = (step % steps) / steps;
            return lo + (hi - lo) * (Math.sin(t * Math.PI * 2) * 0.5 + 0.5);
        }
    };
}

// PTri(lo, hi, steps) — triangular sweep
export function PTri(lo = 0, hi = 1, steps = 16) {
    return {
        get: (step) => {
            const t = (step % steps) / steps;
            return lo + (hi - lo) * (t < 0.5 ? t * 2 : (1 - t) * 2);
        }
    };
}

// ── Markov chains ────────────────────────────────────────────────────────────

// PChain(mapping) — {value: [nextValues...], ...} Markov chain
export function PChain(mapping) {
    const keys = Object.keys(mapping);
    let cur = keys[0];
    return {
        get: () => {
            const nexts = mapping[cur];
            cur = (!nexts || !nexts.length)
                ? keys[Math.floor(Math.random() * keys.length)]
                : String(nexts[Math.floor(Math.random() * nexts.length)]);
            return isNaN(Number(cur)) ? cur : Number(cur);
        }
    };
}

export const PMarkov = PChain;
